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

Use the `google-maps` MCP (requires `GOOGLE_MAPS_API_KEY`):
- `maps_search_places` — confirm an anchor exists, get rating, open-now status, place id.
- `maps_place_details` — full opening hours, website, phone, reviews.
- `maps_directions` — walking / transit / driving time between consecutive stops.
- `maps_distance_matrix` — many-to-many timings when ordering a day's stops.
- `maps_geocode` — resolve a name to coordinates.

Verify travel times rather than estimating — LLM-guessed durations skew optimistic. Without the MCP: WebFetch Google Maps URLs and note that times are estimates.

## Lodging

If the user wants help shortlisting stays:
- `airbnb` MCP — `airbnb_search` then `airbnb_listing_details` on the shortlist.
- For hotels, WebFetch Booking.com and one or two direct chain sites; record the date checked.

## Budget math

Use the `currency` MCP for any cross-currency totals — `convert_currency_latest` for single sums, `get_latest_exchange_rates` when rolling up a day or trip. Don't ask the user to do FX math.

## Rain-day / contingency

For each day with outdoor anchors, list one indoor backup at the bottom of that day.

## Output

Update the trip file in-place. Don't re-paste the full itinerary into chat unless asked — instead summarize what changed and where to look.
