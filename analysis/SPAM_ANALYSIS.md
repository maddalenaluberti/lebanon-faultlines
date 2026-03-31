# Spam & Data Quality Analysis

Dataset: 50,811 tweets | 30,277 unique users

## High Confidence Spam (remove regardless of analysis direction)

| Category | Count | % |
|---|---|---|
| @grok AI bot replies | 1,234 | 2.4% |
| Sectarian spam (@alhasany_news, @LgmanHkeem) | 388 | 0.8% |
| Automated accounts (isAutomated=true) | 40 | 0.1% |
| **Total definite removals** | **~1,662** | **3.3%** |

## Medium Confidence (depends on research goals)

| Category | Count | % |
|---|---|---|
| Hashtag-heavy (5+ tags) | 2,453 | 4.8% |
| Exact duplicate texts (excess copies) | 422 | 0.8% |
| Very short tweets (<20 chars) | 1,013 | 2.0% |
| Link-only tweets | 27 | 0.1% |

## Notes

- Dataset is ~89.5% clean after all flags
- Top news accounts (thisislebnews, sawtkellebnen, etc.) are legit but may skew organic discourse analysis
- No language contamination — clean EN/AR split
- Grok removal is highest single impact action (1,234 AI-generated replies)
