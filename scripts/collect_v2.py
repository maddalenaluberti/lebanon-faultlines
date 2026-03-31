"""
Fast parallel tweet collector v2 — broader queries, concurrent execution.
"""
import requests
import json
import time
import os
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

API_SEARCH = "https://api.twitterapi.io/twitter/tweet/advanced_search"
DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

key_file = Path(__file__).parent / "api_key.txt"
API_KEY = os.environ.get("TWITTER_API_KEY") or key_file.read_text().strip()
HEADERS = {"X-API-Key": API_KEY}

QUERIES = {
    # English — broad
    "en_lebanon": "Lebanon lang:en since:2026-03-02 -filter:retweets",
    "en_hezbollah": "Hezbollah lang:en since:2026-03-02 -filter:retweets",
    "en_beirut": "Beirut war lang:en since:2026-03-02 -filter:retweets",
    "en_maronite": "(Maronite OR Christian Lebanon) lang:en since:2026-03-02 -filter:retweets",
    "en_idf_lebanon": "IDF Lebanon lang:en since:2026-03-02 -filter:retweets",
    # Arabic — broad
    "ar_lebanon_war": "لبنان حرب lang:ar since:2026-03-02 -filter:retweets",
    "ar_hezbollah": "حزب الله lang:ar since:2026-03-02 -filter:retweets",
    "ar_beirut": "بيروت lang:ar since:2026-03-02 -filter:retweets",
    "ar_south_lb": "جنوب لبنان lang:ar since:2026-03-02 -filter:retweets",
    "ar_displacement": "نازحين لبنان lang:ar since:2026-03-02 -filter:retweets",
    "ar_sectarian": "لبنان (شيعة OR سنة OR موارنة OR دروز) lang:ar since:2026-03-02 -filter:retweets",
    "ar_israel": "اسرائيل لبنان lang:ar since:2026-03-02 -filter:retweets",
}

MAX_PER_QUERY = 10000


def load_all_seen_ids():
    """Load all tweet IDs from v1 and v2 files to avoid duplicates."""
    seen = set()
    for fpath in DATA_DIR.glob("*tweets_*.jsonl"):
        with open(fpath) as f:
            for line in f:
                if line.strip():
                    try:
                        seen.add(json.loads(line).get("id", ""))
                    except:
                        pass
    return seen

SEEN_IDS = load_all_seen_ids()
SEEN_LOCK = __import__("threading").Lock()


def collect_query(name, query):
    """Collect all tweets for a single query."""
    global SEEN_IDS
    params = {"query": query, "queryType": "Latest"}
    output_file = DATA_DIR / f"v2_tweets_{name}.jsonl"
    cursor_file = DATA_DIR / f"v2_cursor_{name}.txt"

    # Resume
    count = 0
    cursor = None
    if output_file.exists():
        with open(output_file) as f:
            count = sum(1 for _ in f)
        if cursor_file.exists():
            cursor = cursor_file.read_text().strip()

    if count >= MAX_PER_QUERY:
        return name, count

    dupes = 0
    page = 0
    with open(output_file, "a") as f:
        while count < MAX_PER_QUERY:
            if cursor:
                params["cursor"] = cursor

            try:
                resp = requests.get(API_SEARCH, headers=HEADERS, params=params, timeout=30)

                if resp.status_code == 429:
                    time.sleep(5)
                    continue
                if resp.status_code != 200:
                    break

                data = resp.json()
                tweets = data.get("tweets", [])
                if not tweets:
                    break

                for tweet in tweets:
                    tid = tweet.get("id", "")
                    with SEEN_LOCK:
                        if tid in SEEN_IDS:
                            dupes += 1
                            continue
                        SEEN_IDS.add(tid)
                    f.write(json.dumps(tweet, ensure_ascii=False) + "\n")
                    count += 1

                cursor = data.get("next_cursor", "")
                cursor_file.write_text(cursor or "")
                page += 1

                if page % 25 == 0:
                    print(f"  [{name}] page {page}, {count} tweets", flush=True)

                if not cursor:
                    break

                time.sleep(0.3)

            except requests.exceptions.RequestException:
                time.sleep(3)
                continue
            except KeyboardInterrupt:
                break

    print(f"  [{name}] done: {count} tweets, {dupes} dupes skipped", flush=True)
    return name, count


def main():
    print(f"Starting v2 collection with {len(QUERIES)} queries...", flush=True)
    print(f"Credits check...", flush=True)

    resp = requests.get("https://api.twitterapi.io/oapi/my/info", headers=HEADERS)
    info = resp.json()
    total_credits = info.get("recharge_credits", 0) + info.get("total_bonus_credits", 0)
    print(f"Credits available: {total_credits}", flush=True)

    # Run 4 queries concurrently
    results = {}
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(collect_query, name, query): name for name, query in QUERIES.items()}
        for future in as_completed(futures):
            name, count = future.result()
            results[name] = count
            print(f"  {name}: {count} tweets ✓", flush=True)

    total = sum(results.values())
    print(f"\n=== v2 collection done: {total} new tweets ===", flush=True)
    for name, count in sorted(results.items()):
        print(f"  {name}: {count}", flush=True)

    # Final credit check
    resp = requests.get("https://api.twitterapi.io/oapi/my/info", headers=HEADERS)
    info = resp.json()
    remaining = info.get("recharge_credits", 0) + info.get("total_bonus_credits", 0)
    print(f"\nCredits remaining: {remaining}", flush=True)


if __name__ == "__main__":
    main()
