# Country Breakdown Analysis

**Dataset:** `all_tweets_classified.jsonl` — 49,149 tweets, 150 unique countries
**Generated:** 2026-03-21

---

## Overview

The dataset has a `_country` field for each tweet. 55.3% of tweets (27,180) have `_country: "Unknown"`. Some entries are region-level rather than country-level (e.g., "West Asia", "Europe", "North America") — these are noted separately. The analysis below focuses on the 21,969 tweets with identifiable countries.

Two languages dominate: English (34,216 tweets, 69.6%) and Arabic (14,933 tweets, 30.4%). Zero Farsi tweets were found in the dataset.

---

## 1. Country Breakdown by Group

### Arab Countries (Middle East + North Africa)

**Total: 5,729 tweets (11.7% of all)**

| Rank | Country | Tweets | % of Arab | % of All |
|------|---------|--------|-----------|----------|
| 1 | Saudi Arabia | 2,384 | 41.6% | 4.9% |
| 2 | Iraq | 563 | 9.8% | 1.1% |
| 3 | Egypt | 504 | 8.8% | 1.0% |
| 4 | Kuwait | 413 | 7.2% | 0.8% |
| 5 | UAE | 358 | 6.2% | 0.7% |
| 6 | Yemen | 279 | 4.9% | 0.6% |
| 7 | Qatar | 221 | 3.9% | 0.4% |
| 8 | Jordan | 211 | 3.7% | 0.4% |
| 9 | Syria | 150 | 2.6% | 0.3% |
| 10 | Morocco | 125 | 2.2% | 0.3% |
| 11 | Algeria | 118 | 2.1% | 0.2% |
| 12 | Oman | 108 | 1.9% | 0.2% |
| 13 | Palestine | 100 | 1.7% | 0.2% |
| 14 | Tunisia | 91 | 1.6% | 0.2% |
| 15 | Libya | 52 | 0.9% | 0.1% |

**Key finding:** Saudi Arabia alone accounts for 41.6% of all identified Arab-country tweets — it dominates this group by a massive margin. The Gulf states collectively (Saudi + Kuwait + UAE + Qatar + Bahrain + Oman + Yemen) make up 72.0% of the Arab group.

### Western Countries

**Total: 7,427 tweets (15.1% of all)** (including region-level "Europe", "North America", "Australasia")

| Rank | Country | Tweets | % of Western | % of All |
|------|---------|--------|-------------|----------|
| 1 | United States | 2,419 | 32.6% | 4.9% |
| 2 | United Kingdom | 1,624 | 21.9% | 3.3% |
| 3 | *Europe (region)* | 553 | 7.4% | 1.1% |
| 4 | Canada | 514 | 6.9% | 1.0% |
| 5 | Germany | 358 | 4.8% | 0.7% |
| 6 | Australia | 323 | 4.3% | 0.7% |
| 7 | *North America (region)* | 278 | 3.7% | 0.6% |
| 8 | France | 276 | 3.7% | 0.6% |
| 9 | Netherlands | 181 | 2.4% | 0.4% |
| 10 | Ireland | 143 | 1.9% | 0.3% |
| 11 | Sweden | 131 | 1.8% | 0.3% |
| 12 | Italy | 85 | 1.1% | 0.2% |
| 13 | Belgium | 61 | 0.8% | 0.1% |
| 14 | Spain | 60 | 0.8% | 0.1% |
| 15 | New Zealand | 46 | 0.6% | 0.1% |

**Key finding:** US + UK = 54.4% of all Western tweets. The Anglosphere (US + UK + Canada + Australia + Ireland + NZ) = 68.9% of the Western group. Continental Europe contributes meaningfully through Germany, France, Netherlands, and Sweden.

### Lebanon (standalone)

**4,048 tweets (8.2% of all)** — the single largest identified country.

### Israel (standalone)

**578 tweets (1.2% of all)**

### Iran (standalone)

**Only 13 tweets (0.03%)** — essentially absent from the dataset.

### South & Southeast Asia

**Total: 1,372 tweets (2.8%)**

| Country | Tweets | % of Group |
|---------|--------|-----------|
| India | 579 | 42.2% |
| Pakistan | 364 | 26.5% |
| *South Asia (region)* | 165 | 12.0% |
| Singapore | 39 | 2.8% |
| Malaysia | 37 | 2.7% |
| Thailand | 32 | 2.3% |
| Bangladesh | 32 | 2.3% |
| Indonesia | 28 | 2.0% |
| Philippines | 28 | 2.0% |

### Turkey / Turkiye

**364 tweets (0.7%)** (combining both spellings)

### Sub-Saharan Africa

**Total: 627 tweets (1.3%)**

| Country | Tweets | % of Group |
|---------|--------|-----------|
| Nigeria | 242 | 38.6% |
| *Africa (region)* | 118 | 18.8% |
| South Africa | 102 | 16.3% |
| Kenya | 46 | 7.3% |
| Ghana | 34 | 5.4% |

### Ambiguous Region-Level Entries (not resolved to a country)

| Region Label | Tweets |
|-------------|--------|
| West Asia | 1,298 |
| Europe | 553 |
| North America | 278 |
| North Africa | 180 |
| South Asia | 165 |
| Africa | 118 |
| Southeast Asia | 37 |
| Australasia | 36 |
| Eastern Europe (Non-EU) | 27 |
| South America | 10 |
| East Asia | 6 |

"West Asia" (1,298) is a notable bloc — likely a mix of Lebanese, Syrian, Iraqi, and Gulf users that the geocoder could not resolve further.

---

## 2. Arab Diaspora — Which Countries?

Saudi Arabia is overwhelmingly the #1 contributor with 2,384 tweets (41.6% of all Arab-country tweets). After that:

- **Iraq** (563) and **Egypt** (504) are the clear #2 and #3.
- **Gulf bloc** (Kuwait 413, UAE 358, Yemen 279, Qatar 221, Oman 108, Bahrain 39) collectively adds 1,418 more.
- **Jordan** (211) is significant — a country with a large Palestinian-origin population.
- **Syria** (150) and **Palestine** (100) represent conflict-adjacent populations.
- **North Africa** (Morocco 125, Algeria 118, Tunisia 91, Libya 52) contributes 386 collectively.

### Blame patterns differ sharply across Arab countries:

**Saudi Arabia / Kuwait / Yemen / Oman / Bahrain** — overwhelmingly blame Iran (67-70% rate). These are the anti-Iran, anti-Hezbollah hardliners.

**Egypt** — more balanced: Iran 39%, Israel 41%, analytical/anti-war stance dominant.

**Qatar** — Israel blame (44%) exceeds Iran blame (37%), consistent with Qatar's Al Jazeera-aligned editorial position.

**UAE** — Iran blame (37%) slightly above Israel blame (23%), but much more "no clear blame" (22%) and analytical.

---

## 3. Western Group — Which Countries?

The Western group is **dominated by the Anglosphere:**

| Country | Tweets | Share of Western |
|---------|--------|-----------------|
| United States | 2,419 | 32.6% |
| United Kingdom | 1,624 | 21.9% |
| Canada | 514 | 6.9% |
| Australia | 323 | 4.3% |
| Ireland | 143 | 1.9% |
| New Zealand | 46 | 0.6% |
| **Anglosphere subtotal** | **5,069** | **68.2%** |

Continental Europe contributors:

| Country | Tweets | Share of Western |
|---------|--------|-----------------|
| Germany | 358 | 4.8% |
| France | 276 | 3.7% |
| Netherlands | 181 | 2.4% |
| Sweden | 131 | 1.8% |
| Italy | 85 | 1.1% |
| Belgium | 61 | 0.8% |
| Spain | 60 | 0.8% |

### Critical finding: Many "Western" country tweets are actually Arab diaspora

The Arabic-language share of tweets varies dramatically across Western countries:

| Country | Total Tweets | Arabic % | Notes |
|---------|-------------|----------|-------|
| Germany | 358 | **65%** | Likely large Arab/Syrian diaspora |
| Denmark | 33 | **61%** | Arab diaspora |
| France | 276 | **58%** | Large North African diaspora |
| Sweden | 131 | **57%** | Iraqi/Syrian diaspora |
| Belgium | 61 | **48%** | Moroccan/Turkish diaspora |
| Norway | 43 | **42%** | |
| Netherlands | 181 | **40%** | Moroccan/Turkish diaspora |
| Italy | 85 | **33%** | |
| Canada | 514 | **31%** | Lebanese/Arab diaspora |
| Austria | 42 | **24%** | |
| Spain | 60 | **22%** | |
| Australia | 323 | **15%** | Lebanese diaspora |
| United States | 2,419 | **12%** | |
| United Kingdom | 1,624 | **10%** | |
| Ireland | 143 | **6%** | |
| New Zealand | 46 | **2%** | |

**Germany, France, Sweden, Denmark, Belgium, Netherlands** — these are essentially split between native-language English speakers and Arab diaspora. This is a major caveat for any "Western" group analysis.

---

## 4. Iran Blame — Country Breakdown

### Overall: 15,265 tweets blame Iran (31.1% of all tweets)

### Top 15 countries blaming Iran (excluding Unknown):

| Country | Iran-Blame Tweets | Rate (% of country's tweets) |
|---------|-------------------|------------------------------|
| Saudi Arabia | 1,637 | **68.7%** |
| Lebanon | 857 | 21.2% |
| United States | 701 | 29.0% |
| West Asia (region) | 549 | 42.3% |
| United Kingdom | 407 | 25.1% |
| Kuwait | 290 | **70.2%** |
| Iraq | 289 | **51.3%** |
| Egypt | 198 | 39.3% |
| Yemen | 189 | **67.7%** |
| India | 179 | 30.9% |
| Israel | 170 | 29.4% |
| Germany | 160 | **44.7%** |
| Canada | 148 | 28.8% |
| Europe (region) | 148 | 26.8% |
| UAE | 134 | 37.4% |

### Disproportionate Iran-blamers (by rate, min 20 tweets):

| Country | Total | Iran-Blame | Rate |
|---------|-------|-----------|------|
| **Tunisia** | 91 | 65 | **71.4%** |
| **Kuwait** | 413 | 290 | **70.2%** |
| **Saudi Arabia** | 2,384 | 1,637 | **68.7%** |
| **Yemen** | 279 | 189 | **67.7%** |
| **Oman** | 108 | 73 | **67.6%** |
| **Morocco** | 125 | 80 | **64.0%** |
| **Bahrain** | 39 | 24 | **61.5%** |
| Malaysia | 37 | 22 | 59.5% |
| **Algeria** | 118 | 67 | **56.8%** |
| **Iraq** | 563 | 289 | **51.3%** |
| Libya | 52 | 26 | 50.0% |
| Denmark | 33 | 16 | 48.5% |
| **Syria** | 150 | 70 | **46.7%** |
| **Germany** | 358 | 160 | **44.7%** |

### Is Iran-blame driven by "shah-sympathizing Iranian diaspora"?

**No. Emphatically not.**

The data shows zero Farsi-language tweets in the entire dataset, and only 13 tweets from Iran itself. The Iran-blame narrative is overwhelmingly driven by:

1. **Sunni Arab states** — Saudi Arabia, Kuwait, Yemen, Oman, Bahrain, Tunisia, Morocco, Algeria all blame Iran at 55-71% rates. This is a **Sunni geopolitical grievance** against Iranian expansion, not an Iranian diaspora phenomenon.

2. **Arab diaspora in Western countries** — The high Iran-blame rates from Germany (44.7%), Sweden (31.3%), Netherlands (39.8%), Denmark (48.5%) are largely Arabic-language tweets. Breakdown of Iran-blaming tweets from Western countries by language:
   - Germany: 78% Arabic, 22% English
   - Sweden: 68% Arabic, 32% English
   - France: 64% Arabic, 36% English
   - Belgium: 67% Arabic, 33% English
   - Denmark: **94% Arabic**, 6% English
   - Netherlands: 54% Arabic, 46% English
   - Canada: 46% Arabic, 54% English

3. **English-language Iran-blame from US/UK** — In the US (566 English, 135 Arabic) and UK (337 English, 70 Arabic), Iran-blame is primarily English-language. This likely reflects mainstream Western media framing rather than diaspora activity.

### Gulf countries' blame patterns in detail:

| Gulf Country | Iran Blame Rate | Hezbollah | Israel | Dominant Stance |
|-------------|----------------|-----------|--------|----------------|
| Kuwait | **70.2%** | 30.3% | 17.2% | anti_war (34.4%) |
| Saudi Arabia | **68.7%** | 29.6% | 18.7% | anti_war (34.2%) |
| Yemen | **67.7%** | 24.0% | 30.5% | unclear/pro_resistance |
| Oman | **67.6%** | 15.7% | 29.6% | — |
| Bahrain | **61.5%** | 25.6% | 25.6% | — |
| Qatar | 36.7% | 18.1% | **44.3%** | — |
| UAE | 37.4% | 17.0% | 22.9% | analytical (32.7%) |

Saudi/Kuwait/Yemen/Oman/Bahrain: strongly anti-Iran. Qatar and UAE: more balanced, with Qatar tilting toward Israel-blame.

---

## 5. Stance Breakdown by Key Country

| Country | Analytical | Anti-War | Pro-Resistance | Pro-Israel | Unclear |
|---------|-----------|----------|----------------|------------|---------|
| Lebanon | **53.6%** | 17.9% | 9.9% | 3.1% | 14.6% |
| United States | 34.1% | 21.1% | 10.5% | **16.0%** | 17.3% |
| Saudi Arabia | 18.2% | **34.2%** | 17.5% | 5.2% | 23.9% |
| United Kingdom | 30.2% | **26.4%** | 11.9% | 12.2% | 17.6% |
| Israel | **52.1%** | 12.1% | 2.8% | **20.4%** | 11.6% |
| Iraq | 27.4% | 21.3% | **23.8%** | 2.7% | 23.6% |
| India | **61.3%** | 14.5% | 9.7% | 6.6% | 7.1% |
| Pakistan | **62.6%** | 14.8% | 10.2% | 3.6% | 7.7% |
| Egypt | 37.5% | 22.4% | 18.7% | 1.8% | 18.7% |
| Ireland | 10.5% | **40.6%** | 13.3% | 9.8% | 24.5% |
| Tunisia | 22.0% | 14.3% | **48.4%** | 2.2% | 13.2% |
| Yemen | 15.4% | 22.2% | **27.2%** | 6.1% | 28.0% |
| Germany | 22.6% | 26.0% | 17.9% | 10.3% | 21.8% |

Notable patterns:
- **Lebanon** is overwhelmingly analytical (53.6%) — they're living it
- **Ireland** is the most anti-war Western country (40.6%) with the highest Israel-blame rate (69.2%) among Western nations — consistent with Irish political sympathy for occupied peoples
- **Tunisia** is the most pro-resistance (48.4%) and highest Iran-blame rate (71.4%) — a unique combination suggesting anti-Iran but pro-Palestinian resistance framing
- **Iraq** has the highest pro-resistance stance (23.8%) among major Arab countries
- **US** has the highest pro-Israel rate (16.0%) among non-Israel countries
- **India/Pakistan** are overwhelmingly analytical (61-63%), acting as distant observers

---

## Summary for Maddy

1. **"Arab diaspora" = mostly Saudi Arabia** (42% of the group), followed by Iraq, Egypt, and the Gulf states. The Gulf bloc collectively dominates.

2. **"Western" = US + UK** (54% of the group). But Germany/France/Sweden/Netherlands/Belgium/Denmark have 40-65% Arabic-language tweets, meaning they're really mixed native + Arab diaspora.

3. **Iran-blame is NOT driven by Iranian diaspora** (zero Farsi tweets, only 13 tweets from Iran). It's driven by Sunni Arab populations — Gulf states at 60-70% rates, and Arab diaspora in Europe writing in Arabic.

4. **The most disproportionate Iran-blamers** are Gulf Arab states (Kuwait, Saudi, Yemen, Oman) and North African states (Tunisia, Morocco, Algeria). In Western countries, Iran-blame from Germany/Denmark/Sweden/Belgium is predominantly Arabic-language — i.e., Arab diaspora, not native populations.
