# Travel Repo

Personal travel planning workspace. Used to research destinations, hunt cheap flights, build itineraries, and store trip plans.

## At session start

1. Read `preferences.md` before asking the user setup questions (home airports, loyalty programs, dietary needs, budget norms — assume they apply unless overridden).
2. If the user names a destination or date, check `trips/` for an existing file before starting fresh.

## Layout

- `preferences.md` — user's standing travel preferences. Read on every session.
- `trips/<destination>-<YYYY-MM>.md` — one file per trip. Append research, fare quotes, itinerary, booking confirmations.
- `templates/itinerary.md` — copy this when starting a new trip.
- `.mcp.json` — MCP servers wired in (see below).
- `.env` (gitignored) — API keys. Copy from `.env.example`, then `set -a; source .env; set +a` before launching Claude Code so MCPs see the vars.
- `.claude/skills/` — playbooks I follow automatically when a matching task comes up:
  - `flight-search` — hunting cheap fares
  - `trip-plan` — building day-by-day itineraries
  - `destination-research` — finding things to do
  - `points-miles` — award-flight searches

## MCP tools available

- **kiwi** (`search-flight`) — hosted at mcp.kiwi.com, no key. Round-trip / one-way, ±3-day flex, multi-pax, cabin class, returns booking links.
- **airbnb** (`airbnb_search`, `airbnb_listing_details`) — no key. Scrapes Airbnb; respects robots.txt.
- **currency** (`convert_currency_latest`, `convert_currency_specific_date`, `get_latest_exchange_rates`, `get_historical_exchange_rates`, `get_supported_currencies`) — no key. Frankfurter / ECB rates; runs locally via `uvx`.
- **google-maps** (`maps_search_places`, `maps_place_details`, `maps_directions`, `maps_geocode`, `maps_distance_matrix`, `maps_search_nearby`, plus composite tools like `maps_plan_route`) — needs `GOOGLE_MAPS_API_KEY`.

## House rules

- Quote prices with the currency and the date checked — fares move fast.
- For flight prices: start with the `kiwi` MCP, then cross-check on Google Flights and at least one airline-direct site. Call out uncertainty when scraping.
- Never claim a flight is booked. I can draft, search, and compare — booking happens in the airline/OTA.
- Store booking confirmations (PNR, ticket numbers) in the trip file under a `## Bookings` section.
