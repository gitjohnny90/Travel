# Travel Repo

Personal travel planning workspace. Used to research destinations, hunt cheap flights, build itineraries, and store trip plans.

## At session start

1. Read `preferences.md` before asking the user setup questions (home airports, loyalty programs, dietary needs, budget norms — assume they apply unless overridden).
2. If the user names a destination or date, check `trips/` for an existing file before starting fresh.
3. If the `kiwi` MCP exposes `mcp__kiwi__authenticate` (rather than `search-flight`), the OAuth token has expired or never been issued — kick off the flow: call `authenticate`, hand the URL to the user, then `complete_authentication` with the callback URL they paste back. One-time per token lifetime.

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

- **kiwi** (`search-flight`) — hosted at mcp.kiwi.com. Requires one-time OAuth per session (see "At session start" step 3). Round-trip / one-way, ±3-day flex, multi-pax, cabin class, returns booking links.
- **airbnb** (`airbnb_search`, `airbnb_listing_details`) — no key. Scrapes Airbnb; respects robots.txt.
- **currency** (`convert_currency_latest`, `convert_currency_specific_date`, `get_latest_exchange_rates`, `get_historical_exchange_rates`, `get_supported_currencies`) — no key. Frankfurter / ECB rates; runs locally via `uvx`.
- **google-maps** (`maps_search_places`, `maps_place_details`, `maps_directions`, `maps_geocode`, `maps_distance_matrix`, `maps_search_nearby`, plus composite tools like `maps_plan_route`) — needs `GOOGLE_MAPS_API_KEY`.

## House rules

- Quote prices with the currency and the date checked — fares move fast.
- For flight prices: start with the `kiwi` MCP, then cross-check on Google Flights and at least one airline-direct site. Call out uncertainty when scraping.
- Never claim a flight is booked. I can draft, search, and compare — booking happens in the airline/OTA.
- Store booking confirmations (PNR, ticket numbers) in the trip file under a `## Bookings` section.

## Deferred work (not yet started)

Stuff explored in research and intentionally postponed — pick up here next time the user wants to invest in the workspace:

- **Phase 2 — Patterns lifted from [borski/travel-hacking-toolkit](https://github.com/borski/travel-hacking-toolkit):**
  - `data/` directory with curated JSON ground truth (transfer-partners, sweet-spots, points-valuations). LLM can't be trusted to remember these.
  - `fallback-and-resilience` reference skill auto-loaded on flight queries.
  - Playwright/Patchright MCP for browser-automation fallback on sites with no API (Southwest, airline portals, Chase/Amex travel).
  - "No questions, just act" pre-output gate.
- **Phase 3 — Sub-agent restructure of `trip-plan`:** convert into a synthesizer that launches parallel sub-agents (flight-researcher, hotel-researcher, food-explorer, logistics, budget). Independently converged on by borski, ErlebnisW, squid-club.
- **Known dead/closed APIs (don't retry):** Kiwi Tequila self-serve (portal closed to new signups, Apr 2026); Amadeus self-service developer portal (sunsetting July 17, 2026); wesbos currency MCP endpoint (HTTP 403).
