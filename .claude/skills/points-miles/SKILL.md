---
name: points-miles
description: Use when the user wants to book with points/miles, evaluate an award redemption, or decide cash vs. points. Triggers on "use my points", "award flight", "miles for", "is this a good redemption", "transfer partners".
---

# Points & miles playbook

## Pull from `preferences.md`

- Airline loyalty balances + status
- Hotel loyalty balances + status
- Transferable currencies: Chase UR, Amex MR, Capital One miles, Bilt, Citi TY, Capital One, Marriott
- Status that affects award availability (e.g. Lifetime Platinum)

## Award search order

1. Identify the **route** and **dates**.
2. Identify which alliance(s) serve the route:
   - Star Alliance — United, Lufthansa, ANA, Air Canada, Avianca, Turkish, Singapore, Thai…
   - oneworld — AA, BA, Iberia, Cathay, Qatar, JAL, Qantas, Finnair, Alaska (partner)
   - SkyTeam — Delta, Air France/KLM, Korean, Virgin Atlantic (partner), ITA
   - Non-aligned but valuable partners: Virgin Atlantic, Alaska, Aeroplan, Air France/KLM Flying Blue
3. **Search the cheapest mileage program for that route**, not the airline you'd fly:
   - Star Alliance long-haul biz: Aeroplan, ANA, Turkish, Avianca LifeMiles
   - oneworld long-haul biz: Alaska, BA Avios (short-haul), Qatar Avios, Cathay Asia Miles
   - SkyTeam: Flying Blue Promo Rewards, Virgin Atlantic (Delta/ANA partner sweet spots)
4. Cross-reference what **transferable currency** can reach that program.

## Tools to suggest

- **seats.aero** (subscription) — multi-program award search, the single best tool
- **point.me** — similar
- **ExpertFlyer** — fare class / award availability
- Each airline's own award search for confirmation before transferring points

## "Good redemption" math

Compute: `cents per point (cpp) = (cash price − taxes/fees on award) / points used`

Rules of thumb:
- Economy short-haul: 1.2–1.5 cpp is fine
- Long-haul business: 4–8 cpp is the target
- Long-haul first: 6–12 cpp
- Below floor = pay cash and keep points

## Critical warnings

- **Never transfer points speculatively** — confirm award space is bookable in the partner program first.
- **Phantom availability** — some search tools show space that doesn't actually price out. Call the program if needed.
- **Fuel surcharges** vary wildly by partner (BA/LH high, Aeroplan/AS low). Factor into cpp.
- **Cancellation rules** differ by program, not by operating carrier.

## Output

Show top 3 options as:
```
Option 1: {points program} — {N} miles + ${fees} → {cpp} cpp
  Operating: {carrier} {route}
  Award space confirmed via: {source, date}
  Transfer from: {currency} → {program} ({ratio})
```
