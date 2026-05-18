---
name: flight-search
description: Use when the user wants to find, compare, or price flights. Triggers on "find flights", "cheap flight to X", "fly from A to B", "fare from", "when should I book", "is this a good price". Produces a structured fare comparison, not a single quote.
---

# Flight search playbook

## Inputs to confirm (don't re-ask if in `preferences.md`)

- Origin airport(s) — include nearby airports unless the user said no
- Destination airport(s) — same; include nearby
- Date flexibility: exact / ±1 / ±3 / ±7 / month
- Pax count, cabin, max layover, red-eye OK?
- One-way / roundtrip / multi-city / open-jaw
- Points-eligible? (if yes, also run `points-miles` skill)

## Search order

1. **If a flights API MCP is configured** (Kiwi Tequila, Duffel, Amadeus) — use it first. Run:
   - Exact-date search
   - ±3 day flexible-date matrix
   - Nearby-airport variants
2. **Otherwise** — WebFetch these and call out that prices are approximate:
   - Google Flights (`https://www.google.com/travel/flights`) — best calendar view
   - Kayak — strong for nearby-airport and multi-city
   - Skyscanner — strong for "everywhere" searches
   - The airline direct site for the best one or two options found (cheapest is sometimes only there)
3. Always check **at least one OTA and one airline direct** before recommending.

## Cheap-fare levers to try

- ±3 day shift on each leg
- Nearby airports (origin AND destination)
- Open-jaw (fly into A, out of B)
- Multi-city via a known cheap hub
- Different days of week (Tue/Wed/Sat typically cheapest long-haul)
- Basic economy vs. main cabin — note baggage/seat tradeoffs
- Award availability (handoff to `points-miles`)

## Output format

Quote in this shape:

```
Best fares found ({date checked, currency}):

Option A — $XXX — {carrier} {flight#} {dep→arr} {duration} {stops}
  Outbound: {date, time, route}
  Return:   {date, time, route}
  Cabin: {basic / main}  Bags: {included / extra $X}
  Book at: {airline | OTA + caveats}

Option B — ...

Cheaper if flexible: {date} = ${price}
Nearby-airport win: {airport} = ${price}
```

End with a one-line "is this a good price" verdict using:
- Historical context if known (Google Flights "low/typical/high" or Hopper-style framing)
- The user's stated budget from `preferences.md`

## Pitfalls to call out

- Hidden-city ticketing — mention as an option but warn about airline retaliation
- Basic economy bag/seat costs that flip the ranking
- Long layovers that require a transit visa
- Self-transfer risk on separate tickets (no protection if first leg delays)
- Currency of charge vs. card foreign-transaction fees
