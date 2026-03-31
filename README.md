# Lebanon Faultlines

**Discourse analysis of ~49,000 tweets about the 2024 Lebanon-Israel conflict, examining blame attribution patterns across three geographic audiences.**

A scrollytelling data visualization built for Maddalena Luberti's UCL masters application in international policy.

Live site: [maddalenaluberti.github.io/lebanon-faultlines](https://maddalenaluberti.github.io/lebanon-faultlines/)

---

## Research Question

**"Who gets scapegoated?"** This project investigates how three distinct geographic audiences assign blame during the 2024 Lebanon-Israel escalation.

### Key Findings

| Audience | Primary blame target | Framing |
|---|---|---|
| **Lebanese accounts** | Own political system (Hezbollah, sectarian elites) | Domestic structural critique |
| **Arab diaspora accounts** | Iran | Proxy war framing |
| **Western accounts** | Israel | International law framing |

A critical secondary finding: during escalation periods, structural critique collapses. All three groups converge on blaming immediate military actors, abandoning the more nuanced systemic critiques they otherwise sustain.

## Dataset

| Metric | Value |
|---|---|
| Total tweets collected | 49,149 |
| Valid after cleaning | 48,407 |
| English / Arabic | 69.4% / 30.6% |
| Tweets with identifiable location | 44.9% |
| Countries represented | 150 |

**Location groups** (tweets with geographic attribution):
- Lebanon: 4,048
- Arab diaspora: 5,729
- Western: 7,427

## Data Pipeline

The analysis follows a five-stage pipeline. Each stage can be run independently given the output of the previous stage.

```
collect_tweets.py / collect_v2.py    (1) Twitter API collection
        │
        ▼
    clean_spam.py                    (2) Spam removal & deduplication
        │
        ▼
    fast_enrich.py                   (3) User location enrichment
        │
        ▼
   classify_blame.py                 (4) GPT-4o-mini blame classification
        │
        ▼
   blame_crosstabs.json              (5) Cross-tabulation for visualization
```

1. **Collection** -- Tweets gathered via Twitter/X API (v1 and v2) using multiple search queries in English and Arabic.
2. **Cleaning** -- Spam removal and deduplication reduces the corpus from 49,149 to 48,407 valid tweets.
3. **Enrichment** -- User profile location fields are geocoded and mapped to country/region groups.
4. **Classification** -- OpenAI GPT-4o-mini batch API classifies each tweet for blame target, stance, and geographic attribution.
5. **Analysis** -- Cross-tabulation of blame by audience, stance analysis, and temporal pattern extraction.

## Website

The visualization is a single-page scrollytelling site with the following sections:

**Header** -- Intro -- Methodology -- Blame Attribution Chart -- Stance Analysis -- Timeline -- Discussion -- Coda

Built with SvelteKit (static adapter for SSG), using inline SVG charts and CSS scroll-driven animations. The tone is academic and neutral, appropriate for a university application context.

### Build and Deploy

```bash
cd website
npm install
npm run build
```

Built files output to `website/build/`. For GitHub Pages deployment, copy the contents of `build/` to the repository root and push to the main branch. GitHub Pages serves from the root of the main branch.

For local development:

```bash
cd website
npm run dev
```

## Repository Structure

```
/                              GitHub Pages serves from repo root
├── README.md
├── index.html                 Built site entry point
├── _app/                      Built SvelteKit assets
├── robots.txt
├── .nojekyll
│
├── website/                   SvelteKit source
│   ├── src/
│   │   └── routes/
│   │       ├── +page.svelte          Main page (content + visualizations)
│   │       ├── +layout.svelte        Layout wrapper
│   │       └── +layout.ts            Prerender config
│   ├── static/
│   ├── package.json
│   ├── svelte.config.js
│   ├── vite.config.ts
│   └── tsconfig.json
│
├── scripts/                   Data collection & analysis
│   ├── collect_tweets.py              Twitter API v1 collection
│   ├── collect_v2.py                  Twitter API v2 collection
│   ├── clean_spam.py                  Spam removal & deduplication
│   ├── classify_blame.py             GPT-4o-mini blame classification
│   ├── fast_enrich.py                 User location enrichment
│   └── classify_requirements.txt      Python dependencies
│
├── analysis/                  Research documentation
│   ├── BLAME_ANALYSIS.md              Core blame attribution findings
│   ├── COUNTRY_BREAKDOWN.md           Geographic audience analysis
│   ├── LORIENT_TIMELINE.md            Fact-checked timeline (L'Orient Today)
│   ├── QUOTE_DETAILS.md              Notable quote metadata
│   ├── RESEARCH_ANGLES.md             Initial research directions
│   ├── DISPLACEMENT_RESEARCH.md       Displacement narrative analysis
│   ├── DISPLACEMENT_FRAMING_ANALYSIS.md
│   ├── SPIKE_ANALYSIS.md             Temporal spike analysis
│   ├── SPAM_ANALYSIS.md              Spam patterns documentation
│   ├── STATS.md                       Dataset statistics
│   ├── WEBSITE_STACK.md              Tech stack decisions
│   └── cleaning_report.txt            Data cleaning log
│
└── data/
    └── blame_crosstabs.json           Cross-tabulation data for visualizations
```

## Data Files Not in This Repository

The raw tweet JSONL files exceed GitHub's size limits. The following files can be regenerated by running the pipeline scripts in order (collect, clean, enrich, classify):

- `all_tweets_classified.jsonl` -- All 48,407 classified tweets with blame targets, stance, and location
- `all_tweets_cleaned.jsonl` -- Cleaned tweets before classification
- `all_tweets_merged.jsonl` -- Raw merged collection
- Various query-specific collection files (`tweets_english.jsonl`, `v2_tweets_*.jsonl`, etc.)

## Technologies

| Layer | Stack |
|---|---|
| Data collection | Python, Twitter/X API (v1 + v2) |
| Classification | OpenAI GPT-4o-mini (batch API) |
| Website | SvelteKit, inline SVG charts, CSS animations |
| Hosting | GitHub Pages |

## Credits

Website and data analysis by hezb (AI assistant) with direction from Elio and Maddy. March 2026.
