#!/usr/bin/env python3
"""
clean_spam.py - Remove definite spam from Lebanon tweet dataset.

Removes three HIGH CONFIDENCE spam categories:
  1. @grok AI bot replies (author.userName == "grok")
  2. Sectarian spam accounts (@alhasany_news, @LgmanHkeem)
  3. Automated accounts (author.isAutomated == true)

Input:  data/all_tweets_merged.jsonl  (50,811 tweets)
Output: data/all_tweets_cleaned.jsonl  (cleaned version)
        data/cleaning_report.txt       (removal report)

Idempotent: safe to run multiple times; overwrites output files.
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DATA_DIR = Path(__file__).resolve().parent / "data"
INPUT_FILE = DATA_DIR / "all_tweets_merged.jsonl"
OUTPUT_FILE = DATA_DIR / "all_tweets_cleaned.jsonl"
REPORT_FILE = DATA_DIR / "cleaning_report.txt"

# Spam account usernames (exact match, case-sensitive as stored in data)
GROK_USERNAME = "grok"
SECTARIAN_ACCOUNTS = {"alhasany_news", "LgmanHkeem"}

# ---------------------------------------------------------------------------
# Classification helpers
# ---------------------------------------------------------------------------

def classify_spam(tweet: dict) -> str | None:
    """Return a spam category string if the tweet is spam, else None."""
    author = tweet.get("author", {})
    username = author.get("userName", "")

    # Category 1: @grok AI bot replies
    if username == GROK_USERNAME:
        return "grok_bot"

    # Category 2: Sectarian spam accounts
    if username in SECTARIAN_ACCOUNTS:
        return "sectarian_spam"

    # Category 3: Automated accounts
    if author.get("isAutomated") is True:
        return "automated"

    return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if not INPUT_FILE.exists():
        print(f"ERROR: Input file not found: {INPUT_FILE}")
        raise SystemExit(1)

    # Counters
    total_in = 0
    removed = {"grok_bot": 0, "sectarian_spam": 0, "automated": 0}
    kept = 0

    # Sample removals for the report (keep up to 5 per category)
    samples: dict[str, list[dict]] = {k: [] for k in removed}

    # Process line by line (memory-efficient for large files)
    tmp_output = OUTPUT_FILE.with_suffix(".jsonl.tmp")
    with open(INPUT_FILE, "r", encoding="utf-8") as fin, \
         open(tmp_output, "w", encoding="utf-8") as fout:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            total_in += 1
            tweet = json.loads(line)
            category = classify_spam(tweet)

            if category is not None:
                removed[category] += 1
                # Collect samples
                if len(samples[category]) < 5:
                    samples[category].append({
                        "id": tweet.get("id"),
                        "author": tweet.get("author", {}).get("userName", ""),
                        "text_preview": tweet.get("text", "")[:120],
                    })
            else:
                fout.write(json.dumps(tweet, ensure_ascii=False) + "\n")
                kept += 1

    # Atomic rename so partial writes never corrupt the output
    os.replace(tmp_output, OUTPUT_FILE)

    total_removed = sum(removed.values())

    # ---------------------------------------------------------------------------
    # Print summary to stdout
    # ---------------------------------------------------------------------------
    print("=" * 60)
    print("  Lebanon Tweet Dataset - Spam Cleaning Report")
    print("=" * 60)
    print(f"  Input file:  {INPUT_FILE.name}")
    print(f"  Output file: {OUTPUT_FILE.name}")
    print(f"  Run time:    {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print("-" * 60)
    print(f"  Total input tweets:        {total_in:>7,}")
    print(f"  Removed - @grok bot:       {removed['grok_bot']:>7,}")
    print(f"  Removed - sectarian spam:  {removed['sectarian_spam']:>7,}")
    print(f"  Removed - automated:       {removed['automated']:>7,}")
    print(f"  ----------------------------------------")
    print(f"  Total removed:             {total_removed:>7,}  ({100*total_removed/total_in:.1f}%)")
    print(f"  Tweets remaining:          {kept:>7,}  ({100*kept/total_in:.1f}%)")
    print("=" * 60)

    # ---------------------------------------------------------------------------
    # Write detailed report
    # ---------------------------------------------------------------------------
    with open(REPORT_FILE, "w", encoding="utf-8") as rpt:
        rpt.write("Lebanon Tweet Dataset - Spam Cleaning Report\n")
        rpt.write(f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}\n")
        rpt.write(f"Input:  {INPUT_FILE.name} ({total_in:,} tweets)\n")
        rpt.write(f"Output: {OUTPUT_FILE.name} ({kept:,} tweets)\n\n")

        rpt.write("REMOVAL SUMMARY\n")
        rpt.write("-" * 50 + "\n")
        rpt.write(f"  @grok AI bot replies:       {removed['grok_bot']:>6,}\n")
        rpt.write(f"  Sectarian spam accounts:    {removed['sectarian_spam']:>6,}\n")
        rpt.write(f"    - @alhasany_news\n")
        rpt.write(f"    - @LgmanHkeem\n")
        rpt.write(f"  Automated accounts:         {removed['automated']:>6,}\n")
        rpt.write(f"  {'':->40}\n")
        rpt.write(f"  TOTAL REMOVED:              {total_removed:>6,}  ({100*total_removed/total_in:.1f}%)\n")
        rpt.write(f"  TWEETS REMAINING:           {kept:>6,}  ({100*kept/total_in:.1f}%)\n\n")

        rpt.write("SAMPLE REMOVED TWEETS\n")
        rpt.write("=" * 50 + "\n")
        category_labels = {
            "grok_bot": "@grok AI bot replies",
            "sectarian_spam": "Sectarian spam accounts",
            "automated": "Automated accounts",
        }
        for cat, label in category_labels.items():
            rpt.write(f"\n--- {label} (showing up to 5 of {removed[cat]:,}) ---\n")
            for s in samples[cat]:
                rpt.write(f"  ID: {s['id']}  Author: @{s['author']}\n")
                rpt.write(f"  Text: {s['text_preview']}\n\n")

    print(f"\n  Report saved to: {REPORT_FILE.name}")
    print(f"  Cleaned data:    {OUTPUT_FILE.name}")


if __name__ == "__main__":
    main()
