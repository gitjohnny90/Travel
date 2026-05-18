#!/usr/bin/env python3
"""Google Maps lookups: places, details, directions, geocoding.

Usage:
  ./tools/maps.py places "best ramen in shibuya" [--near "Shibuya, Tokyo"] [--limit 10]
  ./tools/maps.py details PLACE_ID
  ./tools/maps.py directions "origin" "destination" [--mode walking|transit|driving|bicycling]
  ./tools/maps.py geocode "address or place name"

Add --json to any command for raw output.

Required APIs on the same key:
  - Places API (New)
  - Directions API
  - Geocoding API
"""
from __future__ import annotations
import argparse
import json
import sys
import urllib.parse
import urllib.request

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from _env import require  # noqa: E402

PLACES = "https://places.googleapis.com/v1/places:searchText"
PLACE_DETAILS = "https://places.googleapis.com/v1/places/"
DIRECTIONS = "https://maps.googleapis.com/maps/api/directions/json"
GEOCODE = "https://maps.googleapis.com/maps/api/geocode/json"


def _post(url: str, body: dict, fields: str) -> dict:
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode(),
        headers={
            "Content-Type": "application/json",
            "X-Goog-Api-Key": require("GOOGLE_MAPS_API_KEY"),
            "X-Goog-FieldMask": fields,
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def _get(url: str, params: dict) -> dict:
    params = {**params, "key": require("GOOGLE_MAPS_API_KEY")}
    req = urllib.request.Request(f"{url}?{urllib.parse.urlencode(params)}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def _get_place(place_id: str, fields: str) -> dict:
    req = urllib.request.Request(
        f"{PLACE_DETAILS}{urllib.parse.quote(place_id)}",
        headers={
            "X-Goog-Api-Key": require("GOOGLE_MAPS_API_KEY"),
            "X-Goog-FieldMask": fields,
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def cmd_places(args) -> dict:
    body = {"textQuery": args.query, "pageSize": args.limit}
    if args.near:
        body["locationBias"] = {"circle": {"center": _resolve_center(args.near), "radius": 5000.0}}
    fields = (
        "places.id,places.displayName,places.formattedAddress,places.rating,"
        "places.userRatingCount,places.priceLevel,places.types,"
        "places.currentOpeningHours.openNow,places.googleMapsUri"
    )
    return _post(PLACES, body, fields)


def _resolve_center(text: str) -> dict:
    g = _get(GEOCODE, {"address": text})
    if not g.get("results"):
        raise SystemExit(f"Could not geocode: {text}")
    loc = g["results"][0]["geometry"]["location"]
    return {"latitude": loc["lat"], "longitude": loc["lng"]}


def cmd_details(args) -> dict:
    fields = (
        "id,displayName,formattedAddress,rating,userRatingCount,priceLevel,"
        "regularOpeningHours,currentOpeningHours,websiteUri,nationalPhoneNumber,"
        "googleMapsUri,editorialSummary,reviews"
    )
    return _get_place(args.place_id, fields)


def cmd_directions(args) -> dict:
    return _get(DIRECTIONS, {"origin": args.origin, "destination": args.destination, "mode": args.mode})


def cmd_geocode(args) -> dict:
    return _get(GEOCODE, {"address": args.address})


def fmt_places(data: dict) -> str:
    places = data.get("places", [])
    if not places:
        return "No places found."
    out = []
    for p in places:
        name = p.get("displayName", {}).get("text", "?")
        rating = p.get("rating", "—")
        count = p.get("userRatingCount", 0)
        open_now = p.get("currentOpeningHours", {}).get("openNow")
        open_str = "OPEN" if open_now else "CLOSED" if open_now is False else "?"
        out.append(
            f"- {name}  ★{rating} ({count})  [{open_str}]\n"
            f"  {p.get('formattedAddress', '')}\n"
            f"  {p.get('googleMapsUri', '')}  id={p.get('id', '')}"
        )
    return "\n".join(out)


def fmt_directions(data: dict) -> str:
    routes = data.get("routes", [])
    if not routes:
        return f"No route. status={data.get('status')}"
    leg = routes[0]["legs"][0]
    return (
        f"{leg['start_address']} → {leg['end_address']}\n"
        f"  Distance: {leg['distance']['text']}\n"
        f"  Duration: {leg['duration']['text']}"
    )


def fmt_geocode(data: dict) -> str:
    if not data.get("results"):
        return f"No match. status={data.get('status')}"
    r = data["results"][0]
    loc = r["geometry"]["location"]
    return f"{r['formatted_address']}\n  lat={loc['lat']} lng={loc['lng']}"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--json", action="store_true", help="Print raw JSON instead of summary")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("places")
    sp.add_argument("query")
    sp.add_argument("--near", help="Bias to a city/area (geocoded first)")
    sp.add_argument("--limit", type=int, default=10)

    sd = sub.add_parser("details")
    sd.add_argument("place_id")

    sr = sub.add_parser("directions")
    sr.add_argument("origin")
    sr.add_argument("destination")
    sr.add_argument("--mode", default="walking", choices=["walking", "driving", "transit", "bicycling"])

    sg = sub.add_parser("geocode")
    sg.add_argument("address")

    args = p.parse_args()
    fn = {"places": cmd_places, "details": cmd_details, "directions": cmd_directions, "geocode": cmd_geocode}[args.cmd]
    data = fn(args)

    if args.json:
        print(json.dumps(data, indent=2))
        return 0
    if args.cmd == "places":
        print(fmt_places(data))
    elif args.cmd == "directions":
        print(fmt_directions(data))
    elif args.cmd == "geocode":
        print(fmt_geocode(data))
    else:
        print(json.dumps(data, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
