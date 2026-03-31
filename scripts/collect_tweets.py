"""
Tweet collector for Lebanon discourse analysis project.
Uses twitterapi.io to collect tweets about Lebanon/Hezbollah/civil war.

Usage:
    python collect_tweets.py                 # collect tweets only
    python collect_tweets.py --enrich        # also fetch user country data
    python collect_tweets.py --enrich-only   # skip tweets, just enrich existing data
"""

import requests
import json
import time
import os
import sys
from datetime import datetime
from pathlib import Path

API_SEARCH = "https://api.twitterapi.io/twitter/tweet/advanced_search"
API_USER_ABOUT = "https://api.twitterapi.io/twitter/user_about"
DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

# Search queries
QUERIES = {
    "english": '(Lebanon OR Hezbollah OR Maronite) (war OR conflict OR displacement OR shia OR sunni OR christian OR druze OR Israel OR "civil war") lang:en since:2026-03-02 -filter:retweets',
    "arabic_broad": '(لبنان OR حزب الله) lang:ar since:2026-03-02 -filter:retweets',
    "arabic_war": 'لبنان (حرب OR "حرب أهلية" OR قصف OR غارات) lang:ar since:2026-03-02 -filter:retweets',
    "arabic_sectarian": 'لبنان (شيعة OR سنة OR موارنة OR دروز OR طائفية) lang:ar since:2026-03-02 -filter:retweets',
}


def collect_tweets(api_key: str, query_name: str, query: str, max_tweets: int = 50000):
    """Collect tweets for a single query, paginating through results."""

    headers = {"X-API-Key": api_key}
    params = {"query": query, "queryType": "Latest"}

    all_tweets = []
    cursor = None
    page = 0
    output_file = DATA_DIR / f"tweets_{query_name}.jsonl"

    # Resume from existing file if present
    if output_file.exists():
        with open(output_file) as f:
            all_tweets = [json.loads(line) for line in f if line.strip()]
        print(f"  Resuming from {len(all_tweets)} existing tweets")
        cursor_file = DATA_DIR / f"cursor_{query_name}.txt"
        if cursor_file.exists():
            cursor = cursor_file.read_text().strip()
            if cursor:
                print(f"  Resuming from cursor: {cursor[:30]}...")

    print(f"\nCollecting '{query_name}' tweets...")
    print(f"  Query: {query[:80]}...")

    with open(output_file, "a") as f:
        while len(all_tweets) < max_tweets:
            if cursor:
                params["cursor"] = cursor

            try:
                resp = requests.get(API_SEARCH, headers=headers, params=params, timeout=30)

                if resp.status_code == 429:
                    print("  Rate limited, waiting 10s...")
                    time.sleep(10)
                    continue

                if resp.status_code != 200:
                    print(f"  Error {resp.status_code}: {resp.text[:200]}")
                    break

                data = resp.json()
                tweets = data.get("tweets", [])

                if not tweets:
                    print("  No more tweets found.")
                    break

                for tweet in tweets:
                    f.write(json.dumps(tweet, ensure_ascii=False) + "\n")
                    all_tweets.append(tweet)

                cursor = data.get("next_cursor", "")
                page += 1

                # Save cursor for resume
                cursor_file = DATA_DIR / f"cursor_{query_name}.txt"
                cursor_file.write_text(cursor or "")

                print(f"  Page {page}: got {len(tweets)} tweets (total: {len(all_tweets)})")

                if not cursor:
                    print("  No more pages.")
                    break

                time.sleep(0.5)

            except requests.exceptions.RequestException as e:
                print(f"  Request error: {e}")
                time.sleep(5)
                continue
            except KeyboardInterrupt:
                print("\n  Interrupted. Progress saved.")
                break

    print(f"  Done! Collected {len(all_tweets)} {query_name} tweets total.")
    return len(all_tweets)


def enrich_users(api_key: str):
    """Fetch account_based_in country for all unique tweet authors."""

    headers = {"X-API-Key": api_key}
    user_file = DATA_DIR / "users_about.jsonl"

    # Load already-enriched users
    existing = {}
    if user_file.exists():
        with open(user_file) as f:
            for line in f:
                if line.strip():
                    u = json.loads(line)
                    existing[u.get("userName", "")] = u
        print(f"  Already have {len(existing)} user profiles cached")

    # Collect unique usernames from all tweet files
    usernames = set()
    for fpath in DATA_DIR.glob("tweets_*.jsonl"):
        with open(fpath) as f:
            for line in f:
                if line.strip():
                    tweet = json.loads(line)
                    un = tweet.get("author", {}).get("userName", "")
                    if un:
                        usernames.add(un)

    # Filter out already-enriched
    to_fetch = [u for u in usernames if u not in existing]
    print(f"\n  {len(usernames)} unique authors, {len(to_fetch)} need enrichment")

    if not to_fetch:
        print("  All users already enriched!")
        return

    fetched = 0
    errors = 0
    with open(user_file, "a") as f:
        for i, username in enumerate(to_fetch):
            try:
                resp = requests.get(
                    API_USER_ABOUT,
                    headers=headers,
                    params={"userName": username},
                    timeout=15,
                )

                if resp.status_code == 429:
                    print(f"  Rate limited at user {i+1}/{len(to_fetch)}, waiting 10s...")
                    time.sleep(10)
                    # Retry
                    resp = requests.get(
                        API_USER_ABOUT,
                        headers=headers,
                        params={"userName": username},
                        timeout=15,
                    )

                if resp.status_code == 200:
                    data = resp.json().get("data", {})
                    if data:
                        f.write(json.dumps(data, ensure_ascii=False) + "\n")
                        f.flush()
                        fetched += 1
                        about = data.get("about_profile", {})
                        country = about.get("account_based_in", "?")
                        if (fetched % 50 == 0) or fetched <= 5:
                            print(f"  [{fetched}/{len(to_fetch)}] @{username} -> {country}")
                else:
                    errors += 1

                time.sleep(0.3)  # Be gentle

            except requests.exceptions.RequestException as e:
                errors += 1
                time.sleep(2)
                continue
            except KeyboardInterrupt:
                print(f"\n  Interrupted. Saved {fetched} profiles.")
                break

    print(f"  Enrichment done! {fetched} new profiles, {errors} errors.")


def main():
    api_key = os.environ.get("TWITTER_API_KEY") or ""

    key_file = Path(__file__).parent / "api_key.txt"
    if not api_key and key_file.exists():
        api_key = key_file.read_text().strip()

    if not api_key:
        print("No API key found. Set TWITTER_API_KEY env var or put it in api_key.txt")
        sys.exit(1)

    enrich_only = "--enrich-only" in sys.argv
    do_enrich = "--enrich" in sys.argv or enrich_only

    print(f"Using API key: {api_key[:8]}...")
    print(f"Data directory: {DATA_DIR}")

    if not enrich_only:
        total = 0
        for name, query in QUERIES.items():
            count = collect_tweets(api_key, name, query, max_tweets=50000)
            total += count

        print(f"\n=== Collection complete: {total} tweets total ===")

        for name in QUERIES:
            fpath = DATA_DIR / f"tweets_{name}.jsonl"
            if fpath.exists():
                with open(fpath) as f:
                    count = sum(1 for _ in f)
                print(f"  {name}: {count} tweets")

    if do_enrich:
        print("\n=== Enriching user profiles ===")
        enrich_users(api_key)


if __name__ == "__main__":
    main()
