"""Fast parallel user enrichment using concurrent requests."""
import requests
import json
import os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

DATA_DIR = Path(__file__).parent / "data"
API_USER_ABOUT = "https://api.twitterapi.io/twitter/user_about"

key_file = Path(__file__).parent / "api_key.txt"
API_KEY = os.environ.get("TWITTER_API_KEY") or key_file.read_text().strip()
HEADERS = {"X-API-Key": API_KEY}

# Load already-enriched
existing = set()
user_file = DATA_DIR / "users_about.jsonl"
if user_file.exists():
    with open(user_file) as f:
        for line in f:
            if line.strip():
                u = json.loads(line)
                existing.add(u.get("userName", ""))

# Collect unique usernames
usernames = set()
for fpath in DATA_DIR.glob("tweets_*.jsonl"):
    with open(fpath) as f:
        for line in f:
            if line.strip():
                tweet = json.loads(line)
                un = tweet.get("author", {}).get("userName", "")
                if un:
                    usernames.add(un)

to_fetch = [u for u in usernames if u not in existing]
print(f"{len(usernames)} unique authors, {len(existing)} cached, {len(to_fetch)} to fetch")

def fetch_user(username):
    try:
        resp = requests.get(API_USER_ABOUT, headers=HEADERS, params={"userName": username}, timeout=15)
        if resp.status_code == 200:
            data = resp.json().get("data", {})
            if data:
                return data
    except:
        pass
    return None

fetched = 0
with open(user_file, "a") as f:
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(fetch_user, u): u for u in to_fetch}
        for future in as_completed(futures):
            result = future.result()
            if result:
                f.write(json.dumps(result, ensure_ascii=False) + "\n")
                f.flush()
                fetched += 1
                if fetched % 100 == 0:
                    country = result.get("about_profile", {}).get("account_based_in", "?")
                    print(f"  {fetched}/{len(to_fetch)} done (last: @{result.get('userName','')} -> {country})")

print(f"\nDone! {fetched} new profiles fetched.")
