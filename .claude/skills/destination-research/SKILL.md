---
name: destination-research
description: Use when the user wants to learn about a destination, find things to do, or scope a place before committing. Triggers on "what's there to do in", "is X worth visiting", "tell me about", "best time to visit", "off the beaten path in", "neighborhoods in".
---

# Destination research playbook

## Source priority (best signal first)

1. **Official tourism board** of the country/region — accurate hours, festivals, transit.
2. **Recent Reddit threads** in r/travel, r/solotravel, country-specific subs (r/japantravel, r/portugaltravel, etc.). Filter to last 12 months. Search: `site:reddit.com {destination} {month} trip report`.
3. **Wikitravel / Wikivoyage** — neighborhood breakdowns and "stay safe" sections are reliable.
4. **Recent travel blogs** (last 18 months only — older info on hours/prices is stale). Prefer specific writers over content farms.
5. **Atlas Obscura** for offbeat / quirky.
6. **The Infatuation, Eater, local newspaper food sections** for restaurants.
7. **YouTube** if the user wants a visual feel — but don't waste time transcribing.

## Avoid as primary sources

- TripAdvisor top-10 lists (gamed)
- AI-generated listicles (often hallucinated hours/prices)
- Anything older than 2 years for prices, hours, or "is X still open"

## What to surface

When researching a place, return:
- **Best time to visit**: weather, crowds, prices by month; festivals to chase or avoid
- **Neighborhoods**: 3–5 with one-line character + who they suit
- **Anchors**: the 5–10 things most travelers should see, with a one-line "why" and rough time needed
- **Offbeat picks**: 3–5 things most guides miss
- **Food**: what to eat that's specific to this place; 2–3 specific spots
- **Logistics**: airport options, transit from airport, getting around within
- **Watch-outs**: scams, areas to avoid at night, dress codes, tipping, cash vs. card

## Seasonality reminder

Always cross-check with the trip's dates. "Best of X" lists assume peak season — in shoulder/off-season, anchors may be closed.

## Output

Drop findings into the trip file under a `## Research` section. Use bullets, not paragraphs. Cite sources inline as `({source}, {date})`.
