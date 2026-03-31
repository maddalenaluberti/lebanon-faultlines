# Displacement Framing Analysis

**Dataset:** 12,338 displacement-related tweets (filtered from 48,407 total)
**Method:** Keyword filtering (Arabic + English displacement/evacuation/shelter/sectarian terms), then classified via Qwen2.5-7B-Instruct for framing categories.
**Categories are non-mutually exclusive** — a single tweet can carry multiple framings.

---

## Overall Distribution

### All framings (non-mutually exclusive)

| Category | Count | % of displacement tweets |
|---|---|---|
| **Sectarian** | 6,577 | 53.3% |
| **Securitisation** | 4,859 | 39.4% |
| **Exclusionary** | 3,780 | 30.6% |
| **Informational** | 3,087 | 25.0% |
| **Solidarity** | 2,928 | 23.7% |
| **Fitna** | 653 | 5.3% |
| **Burden** | 440 | 3.6% |

### Primary framing

| Category | Count | % |
|---|---|---|
| **Sectarian** | 4,332 | 35.1% |
| **Securitisation** | 2,850 | 23.1% |
| **Informational** | 2,197 | 17.8% |
| **Exclusionary** | 1,553 | 12.6% |
| **Solidarity** | 976 | 7.9% |
| **Fitna** | 350 | 2.8% |
| **Burden** | 80 | 0.6% |

---

## Geographic Breakdown

### Framing by geographic group (% of each group's displacement tweets)

| Category | Lebanon (1,472) | Arab countries (2,349) | Western (1,442) | All |
|---|---|---|---|---|
| **Sectarian** | 43.4% | 69.6% | 51.1% | 53.3% |
| **Securitisation** | 36.8% | 38.4% | 44.7% | 39.4% |
| **Exclusionary** | 20.2% | 42.8% | 30.8% | 30.6% |
| **Informational** | 32.0% | 13.7% | 23.5% | 25.0% |
| **Solidarity** | 26.6% | 15.4% | 26.3% | 23.7% |
| **Fitna** | 6.4% | 5.0% | 5.4% | 5.3% |
| **Burden** | 3.0% | 2.3% | 4.2% | 3.6% |

### Key patterns by geography

**Lebanese accounts (1,472 tweets)**
- Most balanced distribution of any group — no single framing exceeds 43%
- Highest informational rate (32%) — Lebanese accounts are the most likely to report displacement as fact
- Highest solidarity rate (26.6%) — empathy and mutual aid framing
- Lowest exclusionary rate (20.2%) — those closest to the crisis are least hostile
- Highest fitna rate (6.4%) — Lebanese are most likely to explicitly name civil war risk
- Burden framing (3%) — surprisingly low, despite being the ones bearing the resource strain

**Arab-majority country accounts (2,349 tweets)**
- Sectarian framing dominates at 69.6% — far higher than any other group
- Exclusionary rhetoric at 42.8% — more than double Lebanon's rate
- Lowest solidarity (15.4%) and informational (13.7%) rates
- The sectarian lens is overwhelmingly Sunni-framed, driven by Gulf accounts

**Western accounts (1,442 tweets)**
- Highest securitisation rate (44.7%) — framing displacement through a security lens
- Sectarian at 51.1% — high but significantly lower than Arab group
- Solidarity (26.3%) comparable to Lebanon
- Exclusionary (30.8%) — between Lebanon and Arab rates

---

## Language Patterns

### Framing by language (all tweets)

| Category | Arabic (6,157) | English (6,181) |
|---|---|---|
| **Sectarian** | 57.3% | 49.3% |
| **Securitisation** | 41.1% | 37.7% |
| **Exclusionary** | 34.4% | 26.8% |
| **Informational** | 20.1% | 30.0% |
| **Solidarity** | 20.0% | 27.4% |
| **Fitna** | 6.7% | 3.9% |
| **Burden** | 2.8% | 4.3% |

### Key language patterns

- Arabic-language tweets are more sectarian (+8pp), more exclusionary (+7.6pp), and more likely to reference fitna (+2.8pp)
- English-language tweets are more informational (+10pp), more solidarity-oriented (+7.4pp)
- This mirrors the broader finding: Arabic discourse is more internally focused (community tensions, sect dynamics), English discourse is more externally framed (humanitarian, security)

### Lebanese tweets by language

| Category | Lebanese Arabic (1,346) | Lebanese English (126) |
|---|---|---|
| **Sectarian** | 42.7% | 50.8% |
| **Securitisation** | 37.6% | 28.6% |
| **Solidarity** | 26.3% | 30.2% |
| **Informational** | 31.5% | 37.3% |
| **Exclusionary** | 19.6% | 27.0% |
| **Fitna** | 6.8% | 2.4% |

Notable: Lebanese English-language tweets are *more* sectarian (50.8%) than Lebanese Arabic tweets (42.7%). This may reflect that English-speaking Lebanese accounts are addressing an international audience and framing local dynamics in sectarian terms for external consumption, while Arabic-speaking Lebanese accounts discuss displacement in more practical, informational terms.

---

## Notable Patterns and Correlations

1. **Proximity reduces hostility**: Lebanese accounts — the people actually hosting the displaced — have the lowest exclusionary rate (20.2%) of any group. Arab-majority country accounts, geographically removed, have more than double (42.8%). Distance correlates with dehumanisation.

2. **Sectarian framing is the dominant lens everywhere, but its character differs**:
   - In Lebanon: sectarian framing often comes with solidarity or fitna concern — "we are different sects but must hold together" or "this displacement risks tearing us apart"
   - In Gulf states: sectarian framing is more hostile — framing Shia displacement as a consequence of Iran/Hezbollah's actions, with less empathy
   - In the West: sectarian framing is more analytical — explaining Lebanon's sectarian system to an outside audience

3. **Burden framing is almost absent (3.6%)**: Despite the enormous material strain of 816K+ displaced, almost nobody frames displacement primarily as an economic or resource burden. It's overwhelmingly discussed in sectarian, security, or humanitarian terms. This suggests the discourse is political, not pragmatic.

4. **Fitna (civil war risk) is a distinctly Lebanese concern**: At 6.4%, it's small overall but highest among Lebanese accounts. Tweets referencing fitna often come from politically engaged accounts warning that the displacement could be exploited to create internal conflict — a concern grounded in Lebanon's civil war history.

5. **The exclusionary-solidarity divide maps onto the blame attribution findings**: Accounts that blame Iran/Hezbollah are significantly more likely to frame displacement with exclusionary rhetoric. Accounts that blame Israel are more likely to use solidarity framing. The blame lens predicts the displacement lens.

---

## Representative Examples

### 1. Solidarity — Lebanese Druze voice
> "I'm a Druze born, raised, and living in Lebanon, son of a former PSP militant who fought alongside the PLO during the Israeli siege of Beirut in 1982. Today, my old man and I both agree that we have nothing to do with Islam's holy war against the Jews. We want to live in peace."

@seasidedruze · English · Lebanon · 636 followers · 36,907 views
[View tweet](https://x.com/seasidedruze/status/2033256746618077445)
Framings: sectarian + solidarity. A Lebanese Druze account simultaneously names the sectarian dynamic and distances from it. War-weary, not hostile.

### 2. Sectarian — Lebanese Christian nostalgia
> "This is Lebanon when Christians and Sunnis were the majority. Before Nasser and his projects with Palestinian camps. Before Khomeini's revolution and Iranian turbans. This was neutral Lebanon, the Switzerland of the East."

@RaymondFHakim · Arabic · Lebanon · 183K followers · 386,821 views
[View tweet](https://x.com/RaymondFHakim/status/2034413577369465151)
Framings: sectarian + solidarity. The most-viewed Lebanese displacement tweet. Nostalgia for a pre-Shia-ascendancy Lebanon. Frames current displacement as consequence of historical sectarian shifts.

### 3. Fitna warning — Lebanese political figure
> "Mahmoud Qomati's threats of overthrowing the state internally: 1) Does not help the displaced but rather scares people and obstructs their reception. 2) Amounts to a call for internal fitna while Lebanon needs the utmost solidarity. 3) Is absurd because any sect's power in Lebanon stops at the boundary of the other sect."

@FaresSouaid · Arabic · Lebanon · 20,590 views
[View tweet](https://x.com/FaresSouaid/status/2033724221843546541)
Framings: solidarity + fitna. A Lebanese political voice warning that Hezbollah's internal threats risk turning displacement into civil conflict.

### 4. Exclusionary — Gulf Arab framing
> "In the coming days, southern Lebanon will be controlled. Anyone who wants used household furniture, I'll give 50% off — fridges, washing machines, bedrooms, kitchens, whatever you want, write in the comments. 90% discount for Syrians because Hezbollah looted their homes in the war."

@mosha3324 · Arabic · Unknown · 247,252 views
[View tweet](https://x.com/mosha3324/status/2033975993279336733)
Framings: exclusionary + solidarity. Mocking tone, treating displacement as a commercial opportunity. Dehumanising, but high engagement.

### 5. Burden + securitisation — Lebanese account
> "Unpopular opinion: The rockets being fired in this war from Lebanon at Israel have zero effect on the entity. They go down, have a glass of whisky in the shelter, come out and continue their night normally. The negatives are only on us: the people exposed, after these strikes, end up in the streets, underground, or terrified."

@sarkiss18 · Arabic · Lebanon · 33,892 views
[View tweet](https://x.com/sarkiss18/status/2034379244566933519)
Framings: solidarity + burden + securitisation. A Lebanese voice framing displacement as the direct cost of Hezbollah's military strategy — the displaced pay the price for rockets that achieve nothing.

---

## Summary for Maddy

The displacement discourse is overwhelmingly sectarian (53%) and securitised (39%), not humanitarian. The people actually living with the displaced (Lebanese accounts) are the most balanced and least hostile. The further away you are, the more exclusionary and sectarian the framing becomes. Solidarity exists (24%) but is outweighed by hostile framing in every geographic group except Lebanon itself.

The most striking finding: **burden framing barely registers (3.6%)**. Nobody is talking about shelter capacity, food, or infrastructure strain. The conversation is about identity — who the displaced are, what sect they belong to, what threat they pose, whether they brought this on themselves. The material reality of displacement is almost invisible in the discourse.
