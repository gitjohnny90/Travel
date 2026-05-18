---
name: trip-plan
description: Use when the user wants to build or refine a day-by-day itinerary, structure a trip, or turn research into a plan. Triggers on "plan my trip", "itinerary for X", "what should we do in N days", "build me a day-by-day".
---

# Trip planning playbook

## Setup

1. If a `trips/<destination>-<YYYY-MM>.md` exists, open it and continue. Otherwise copy `templates/itinerary.md` to that path.
2. Fill in header (travelers, dates, origin, budget) from `preferences.md` + the user's message.
3. Establish the **vibe** before scheduling — packed vs. balanced vs. slow. Default to the user's preference.

## Building the day-by-day

For each day:
- Pick an **anchor** (one must-do thing, usually morning).
- Add a **secondary** within walking distance or one transit hop.
- Leave evenings looser unless something requires a reservation.
- Verify travel times **between** consecutive activities — if >45 min, you've overpacked the day.
- Note opening hours and weekday closures for each anchor. Many museums close one weekday.
- Group by neighborhood, not by theme — minimize transit.

## Reservations to flag upfront

Mark these in "Reservations needed in advance":
- Big-name restaurants (often 30–60 days out)
- Timed-entry museums / palaces / tower tickets
- Day trips that sell out (cooking classes, certain hikes, ferry tickets in season)
- Internal flights or trains with surge pricing
- Activities with weather alternates

## Map verification

If a Google Maps MCP is available, use it to:
- Confirm each place exists and pull current opening hours / ratings
- Get walking + transit time between consecutive stops
- Identify a nearby cheap lunch when a gap appears

Without it: use WebFetch on Google Maps URLs, note that times are estimates.

## Rain-day / contingency

For each day with outdoor anchors, list one indoor backup at the bottom of that day.

## Output

Update the trip file in-place. Don't re-paste the full itinerary into chat unless asked — instead summarize what changed and where to look.
