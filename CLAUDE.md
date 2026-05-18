# Travel Repo

Personal travel planning workspace. Used to research destinations, hunt cheap flights, build itineraries, and store trip plans.

## At session start

1. Read `preferences.md` before asking the user setup questions (home airports, loyalty programs, dietary needs, budget norms — assume they apply unless overridden).
2. If the user names a destination or date, check `trips/` for an existing file before starting fresh.

## Layout

- `preferences.md` — user's standing travel preferences. Read on every session.
- `trips/<destination>-<YYYY-MM>.md` — one file per trip. Append research, fare quotes, itinerary, booking confirmations.
- `templates/itinerary.md` — copy this when starting a new trip.
- `tools/kiwi.py` — Kiwi Tequila flight search CLI. See `tools/README.md`.
- `tools/maps.py` — Google Maps places / details / directions / geocode CLI.
- `.env` (gitignored) — API keys. Copy from `.env.example`.
- `.claude/skills/` — playbooks I follow automatically when a matching task comes up:
  - `flight-search` — hunting cheap fares
  - `trip-plan` — building day-by-day itineraries
  - `destination-research` — finding things to do
  - `points-miles` — award-flight searches

## House rules

- Quote prices with the currency and the date checked — fares move fast.
- For flight prices: prefer a flights API (Kiwi/Duffel/Amadeus) when configured. Otherwise scrape with WebFetch and call out the uncertainty.
- Never claim a flight is booked. I can draft, search, and compare — booking happens in the airline/OTA.
- Store booking confirmations (PNR, ticket numbers) in the trip file under a `## Bookings` section.
