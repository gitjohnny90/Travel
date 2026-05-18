#!/usr/bin/env python3
"""Kiwi Tequila flight search.

Usage:
  ./tools/kiwi.py search --from LAX --to NRT --date 2026-08-15 [--return 2026-08-29]
                         [--adults 2] [--cabin M] [--max-stops 1]
                         [--currency USD] [--limit 10] [--json]

Cabin: M=economy, W=premium economy, C=business, F=first.
Dates: YYYY-MM-DD. Add --flex-days N to widen the window by ±N days on each side.

Docs: https://tequila.kiwi.com/portal/docs/tequila_api/search_api
"""
from __future__ import annotations
import argparse
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from _env import require  # noqa: E402

API = "https://api.tequila.kiwi.com/v2/search"


def kiwi_date(s: str) -> str:
    return datetime.strptime(s, "%Y-%m-%d").strftime("%d/%m/%Y")


def shift(s: str, days: int) -> str:
    return (datetime.strptime(s, "%Y-%m-%d") + timedelta(days=days)).strftime("%Y-%m-%d")


def search(args: argparse.Namespace) -> dict:
    flex = args.flex_days
    date_from = shift(args.date_, -flex) if flex else args.date_
    date_to = shift(args.date_, flex) if flex else args.date_
    params = {
        "fly_from": args.from_,
        "fly_to": args.to,
        "date_from": kiwi_date(date_from),
        "date_to": kiwi_date(date_to),
        "adults": args.adults,
        "selected_cabins": args.cabin,
        "max_stopovers": args.max_stops,
        "curr": args.currency,
        "limit": args.limit,
        "sort": "price",
    }
    if args.return_:
        r_from = shift(args.return_, -flex) if flex else args.return_
        r_to = shift(args.return_, flex) if flex else args.return_
        params["return_from"] = kiwi_date(r_from)
        params["return_to"] = kiwi_date(r_to)
    url = f"{API}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"apikey": require("KIWI_API_KEY")})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def fmt(data: dict, currency: str) -> str:
    rows = data.get("data", [])
    if not rows:
        return "No flights found."
    out = [f"Found {len(rows)} options (cheapest first):\n"]
    for i, f in enumerate(rows, 1):
        legs = " → ".join(
            f"{r['cityFrom']}({r['flyFrom']})→{r['cityTo']}({r['flyTo']}) "
            f"{r['local_departure'][:16].replace('T',' ')} {r['airline']}{r['flight_no']}"
            for r in f["route"]
        )
        stops = len(f["route"]) - 1
        dur_h = f["duration"]["total"] // 3600
        dur_m = (f["duration"]["total"] % 3600) // 60
        out.append(
            f"{i}. {f['price']:>6.0f} {currency}  {stops} stop(s)  "
            f"{dur_h}h{dur_m:02d}m\n   {legs}\n   booking: {f['deep_link']}"
        )
    return "\n".join(out)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search")
    s.add_argument("--from", dest="from_", required=True, help="IATA origin (or comma list)")
    s.add_argument("--to", required=True, help="IATA destination (or comma list)")
    s.add_argument("--date", dest="date_", required=True, help="Outbound YYYY-MM-DD")
    s.add_argument("--return", dest="return_", default=None, help="Return YYYY-MM-DD (omit for one-way)")
    s.add_argument("--flex-days", type=int, default=0, help="±N day window on each leg")
    s.add_argument("--adults", type=int, default=1)
    s.add_argument("--cabin", default="M", choices=["M", "W", "C", "F"])
    s.add_argument("--max-stops", type=int, default=2)
    s.add_argument("--currency", default="USD")
    s.add_argument("--limit", type=int, default=10)
    s.add_argument("--json", action="store_true", help="Print raw JSON")
    args = p.parse_args()

    data = search(args)
    if args.json:
        print(json.dumps(data, indent=2))
    else:
        print(fmt(data, args.currency))
    return 0


if __name__ == "__main__":
    sys.exit(main())
