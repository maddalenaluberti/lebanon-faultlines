# Scrollytelling Website — Tech Stack

## Stack (same as The Pudding + Reuters Graphics)

- **Framework**: SvelteKit with static adapter
- **Scrollytelling**: Scrollama + GSAP ScrollTrigger for animations
- **Charts**: D3.js via Layer Cake (+ d3-sankey for alluvial diagrams)
- **Maps**: MapLibre GL JS (free, open-source Mapbox fork)
- **i18n/RTL**: svelte-i18n with derived RTL store for Arabic support
- **Deployment**: Netlify or GitHub Pages

## Starter

```bash
npx degit the-pudding/svelte-starter lebanon-story
```

## Three Acts → Components

### Act 1: Displacement Map
- MapLibre GL JS with vector tiles
- Animated displacement flow arrows
- Sectarian geography overlay (Shia/Sunni/Maronite/Druze regions)
- Data: UNHCR/OCHA displacement figures, IDF evacuation zones

### Act 2: Blame Attribution
- Alluvial/Sankey diagram: group → blame target flows
- Stacked bar charts: blame by location × language
- Highlighted example tweets (bilingual)
- Data: classifier output from 49K tweets

### Act 3: Temporal Shift
- Timeline chart with annotated events
- Language shift visualization (Arabic → English)
- Before/after blame comparison
- Data: timestamps + classifier output

## References
- [The Pudding Starter](https://github.com/the-pudding/svelte-starter)
- [Reuters Svelte Components](https://reuters-graphics.github.io/graphics-svelte-components/)
- [Layer Cake](https://layercake.graphics/)
- [MapLibre GL JS](https://github.com/maplibre/maplibre-gl-js)
