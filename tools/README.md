# tools/

Thin CLI wrappers around travel APIs. Python 3 stdlib only — no install step.

## Setup

1. `cp .env.example .env`
2. Fill in `KIWI_API_KEY` and `GOOGLE_MAPS_API_KEY`.
3. `chmod +x tools/*.py` (optional).

## Quick reference

```bash
# Flights — cheapest LAX→NRT roundtrip with ±3 day flex
./tools/kiwi.py search --from LAX --to NRT --date 2026-08-15 --return 2026-08-29 --flex-days 3

# Multi-airport origin
./tools/kiwi.py search --from LAX,BUR,LGB --to HND,NRT --date 2026-08-15

# Places near a city
./tools/maps.py places "best ramen" --near "Shibuya, Tokyo"

# Full details on a place (use id from places output)
./tools/maps.py details ChIJ...

# Walking time between two stops
./tools/maps.py directions "Senso-ji Temple" "Tokyo Skytree" --mode walking

# Geocode
./tools/maps.py geocode "Eiffel Tower"
```

Add `--json` to any command for raw output.

## API key sources

- **Kiwi Tequila**: https://tequila.kiwi.com/portal — register, free dev tier.
- **Google Maps**: https://console.cloud.google.com/ — create a project, enable Places API (New), Directions API, Geocoding API on one key. Free tier covers personal use.
