#!/usr/bin/env python3
"""
Blame attribution classifier for Lebanon conflict tweets.

Classifies ~49k tweets by:
  1. blame_targets (multi-label): who the tweet blames for conflict/suffering
  2. stance (single-label): the political framing of the tweet

Uses Qwen2.5-7B-Instruct via vLLM for fast batched inference on a single GPU.
Supports resumption -- skips tweets already present in the output file.

Usage:
    python classify_blame.py [--model MODEL] [--batch-size N] [--max-tokens N]

Requirements (see classify_requirements.txt):
    pip install vllm transformers torch tqdm
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

from tqdm import tqdm

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

DATA_DIR = Path(__file__).resolve().parent / "data"
INPUT_FILE = DATA_DIR / "all_tweets_cleaned.jsonl"
OUTPUT_FILE = DATA_DIR / "all_tweets_classified.jsonl"

VALID_BLAME_TARGETS = {
    "hezbollah",
    "israel",
    "iran",
    "lebanese_government",
    "sectarian_system",
    "international_community",
    "no_clear_blame",
}

VALID_STANCES = {
    "pro_resistance",
    "pro_israel",
    "anti_war",
    "analytical",
    "unclear",
}

DEFAULT_MODEL = "Qwen/Qwen2.5-7B-Instruct"
DEFAULT_BATCH_SIZE = 64
DEFAULT_MAX_TOKENS = 256

# ---------------------------------------------------------------------------
# Prompt
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """\
You are an expert annotator for political discourse analysis on the 2026 Lebanon War. \
You will be given a tweet (in English or Arabic) and must classify it along two dimensions.

### 1. blame_targets (multi-label)
Who does the tweet blame or hold responsible for the conflict, suffering, or instability? \
Select ALL that apply from the list below. A single tweet may blame multiple parties.

- hezbollah          -- blames Hezbollah, the resistance, or its military actions
- israel             -- blames Israel, the IDF, Israeli government, or Zionism
- iran               -- blames Iran, the Islamic Republic, or Iranian proxies/influence
- lebanese_government-- blames the Lebanese state, politicians, army, or ruling class
- sectarian_system   -- blames sectarianism, confessionalism, or communal divisions in general
- international_community -- blames the US, UN, Western nations, or the broader international order
- no_clear_blame     -- the tweet is informational, news reporting, or does not assign blame to any party

If the tweet clearly assigns blame, do NOT include "no_clear_blame". \
Only use "no_clear_blame" when the tweet is genuinely neutral or purely factual reporting.

### 2. stance (single-label)
What is the overall political stance or framing of the tweet? Pick exactly ONE:

- pro_resistance  -- sympathetic to Hezbollah / axis of resistance / anti-Israel framing
- pro_israel      -- sympathetic to Israeli military operations / security narrative
- anti_war        -- condemns violence from all sides, calls for peace
- analytical      -- neutral, journalistic, factual reporting without clear bias
- unclear         -- the stance cannot be determined

### Output format
Respond with ONLY a JSON object, no other text:
{"blame_targets": ["target1", "target2"], "stance": "stance_label"}\
"""


def build_user_prompt(text: str) -> str:
    """Build the user-turn prompt for a single tweet."""
    # Truncate extremely long tweets to avoid blowing up context
    text = text[:1500]
    return f"Classify this tweet:\n\n{text}"


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

# Regex to find the first JSON object in the model output
_JSON_RE = re.compile(r"\{[^{}]*\}", re.DOTALL)


def parse_classification(raw: str) -> dict:
    """
    Parse the model's raw output into a validated classification dict.
    Returns a dict with blame_targets (list[str]) and stance (str).
    Raises ValueError on unparseable or invalid output.
    """
    # Try to find a JSON object in the output
    match = _JSON_RE.search(raw)
    if not match:
        raise ValueError(f"No JSON object found in output: {raw!r}")

    data = json.loads(match.group())

    # Validate blame_targets
    blame = data.get("blame_targets")
    if not isinstance(blame, list) or len(blame) == 0:
        raise ValueError(f"blame_targets missing or empty: {data}")
    # Normalize: strip whitespace, lowercase
    blame = [t.strip().lower() for t in blame]
    # Filter to valid targets only; keep at least what we can
    blame_valid = [t for t in blame if t in VALID_BLAME_TARGETS]
    if not blame_valid:
        raise ValueError(f"No valid blame_targets after filtering: {blame}")

    # Validate stance
    stance = data.get("stance", "").strip().lower()
    if stance not in VALID_STANCES:
        raise ValueError(f"Invalid stance '{stance}', expected one of {VALID_STANCES}")

    return {"blame_targets": blame_valid, "stance": stance}


# ---------------------------------------------------------------------------
# Resume support
# ---------------------------------------------------------------------------

def load_already_processed(output_path: Path) -> set:
    """Load tweet IDs that have already been classified."""
    done = set()
    if output_path.exists():
        with open(output_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                    done.add(obj["id"])
                except (json.JSONDecodeError, KeyError):
                    continue
    return done


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Classify blame in Lebanon conflict tweets")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="HuggingFace model ID")
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE,
                        help="Number of tweets per vLLM batch")
    parser.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS,
                        help="Max tokens for model generation")
    parser.add_argument("--input", type=str, default=str(INPUT_FILE),
                        help="Input JSONL file path")
    parser.add_argument("--output", type=str, default=str(OUTPUT_FILE),
                        help="Output JSONL file path")
    parser.add_argument("--temperature", type=float, default=0.1,
                        help="Sampling temperature (low = more deterministic)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Process only the first batch, for testing")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        print(f"ERROR: Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    # -----------------------------------------------------------------------
    # Load input tweets
    # -----------------------------------------------------------------------
    print(f"Loading tweets from {input_path} ...")
    tweets = []
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                tweets.append(json.loads(line))
    print(f"  Loaded {len(tweets):,} tweets total.")

    # -----------------------------------------------------------------------
    # Resume: skip already-processed tweets
    # -----------------------------------------------------------------------
    already_done = load_already_processed(output_path)
    if already_done:
        print(f"  Found {len(already_done):,} already-classified tweets in {output_path.name}. Resuming.")
    pending = [t for t in tweets if t["id"] not in already_done]
    print(f"  {len(pending):,} tweets remaining to classify.")

    if not pending:
        print("Nothing to do -- all tweets already classified.")
        print_summary(output_path)
        return

    # -----------------------------------------------------------------------
    # Initialize vLLM
    # -----------------------------------------------------------------------
    print(f"\nLoading model: {args.model}")
    print("  (This may take a minute to download and load weights...)")

    from vllm import LLM, SamplingParams

    llm = LLM(
        model=args.model,
        dtype="half",                 # float16, fits well on 3090 24GB
        max_model_len=4096,           # tweets are short; no need for huge context
        gpu_memory_utilization=0.90,
        trust_remote_code=True,
    )

    sampling_params = SamplingParams(
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        stop=["\n\n"],  # JSON output should be a single line/block
    )

    tokenizer = llm.get_tokenizer()

    # -----------------------------------------------------------------------
    # Process in batches
    # -----------------------------------------------------------------------
    total_batches = (len(pending) + args.batch_size - 1) // args.batch_size
    if args.dry_run:
        total_batches = 1
        pending = pending[: args.batch_size]
        print(f"\n** DRY RUN: processing only first batch ({len(pending)} tweets) **\n")

    stats = {"success": 0, "error": 0, "total": len(pending)}
    start_time = time.time()

    # Open output in append mode for resume safety
    with open(output_path, "a", encoding="utf-8") as out_f:
        for batch_idx in tqdm(range(total_batches), desc="Batches", unit="batch"):
            batch_start = batch_idx * args.batch_size
            batch_end = min(batch_start + args.batch_size, len(pending))
            batch = pending[batch_start:batch_end]

            # Build prompts using the chat template
            prompts = []
            for tweet in batch:
                messages = [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": build_user_prompt(tweet["text"])},
                ]
                prompt_text = tokenizer.apply_chat_template(
                    messages,
                    tokenize=False,
                    add_generation_prompt=True,
                )
                prompts.append(prompt_text)

            # Run inference
            outputs = llm.generate(prompts, sampling_params)

            # Parse results and write
            for tweet, output in zip(batch, outputs):
                raw_text = output.outputs[0].text.strip()
                try:
                    classification = parse_classification(raw_text)
                    tweet["blame_targets"] = classification["blame_targets"]
                    tweet["stance"] = classification["stance"]
                    tweet["_classification_raw"] = raw_text
                    tweet["_classification_error"] = None
                    stats["success"] += 1
                except (ValueError, json.JSONDecodeError, KeyError) as e:
                    tweet["blame_targets"] = ["error"]
                    tweet["stance"] = "error"
                    tweet["_classification_raw"] = raw_text
                    tweet["_classification_error"] = str(e)
                    stats["error"] += 1

                out_f.write(json.dumps(tweet, ensure_ascii=False) + "\n")

            # Flush after each batch so progress is saved
            out_f.flush()

    elapsed = time.time() - start_time

    # -----------------------------------------------------------------------
    # Summary
    # -----------------------------------------------------------------------
    print(f"\n{'='*60}")
    print(f"Classification complete.")
    print(f"  Processed:  {stats['total']:,} tweets in {elapsed:.1f}s "
          f"({stats['total']/elapsed:.1f} tweets/sec)")
    print(f"  Successful: {stats['success']:,}")
    print(f"  Errors:     {stats['error']:,} "
          f"({100*stats['error']/max(stats['total'],1):.1f}%)")
    print(f"  Output:     {output_path}")
    print(f"{'='*60}\n")

    print_summary(output_path)


def print_summary(output_path: Path):
    """Print distribution stats from the classified output file."""
    if not output_path.exists():
        return

    blame_counts = {}
    stance_counts = {}
    error_count = 0
    total = 0

    with open(output_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            total += 1

            stance = obj.get("stance", "unknown")
            if stance == "error":
                error_count += 1
            stance_counts[stance] = stance_counts.get(stance, 0) + 1

            for target in obj.get("blame_targets", []):
                blame_counts[target] = blame_counts.get(target, 0) + 1

    print(f"=== Distribution Summary ({total:,} tweets) ===\n")

    print("Blame Targets (multi-label counts):")
    for target, count in sorted(blame_counts.items(), key=lambda x: -x[1]):
        pct = 100 * count / max(total, 1)
        bar = "#" * int(pct / 2)
        print(f"  {target:<25s} {count:>6,}  ({pct:5.1f}%)  {bar}")

    print(f"\nStance (single-label counts):")
    for stance, count in sorted(stance_counts.items(), key=lambda x: -x[1]):
        pct = 100 * count / max(total, 1)
        bar = "#" * int(pct / 2)
        print(f"  {stance:<25s} {count:>6,}  ({pct:5.1f}%)  {bar}")

    if error_count:
        print(f"\n  ** {error_count:,} tweets had classification errors ({100*error_count/total:.1f}%) **")

    print()


if __name__ == "__main__":
    main()
