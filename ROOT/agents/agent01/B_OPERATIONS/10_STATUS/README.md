# 10_STATUS - Status [BASE]

> **5W2H - STATUS:** Now + history (is/was). The live state plus periodic rollups that consolidate the most relevant of each period (day / week / month / year).

## What goes here
- `11_STATUS_Now` - {mutable} the live state, updated by the day's events.
- `12_STATUS_Daily` / `13_STATUS_Weekly` / `14_STATUS_Monthly` / `15_STATUS_Yearly` - the period rollups, each sealed when its period closes.
- `16_STATUS_Reserved` .. `19_STATUS_Reserved` - **reserved**.

## What does NOT go here
- The plan / the 'should' -> `60_WHEN`.
- The identity of a thing -> its WHAT/WHO home.
- Live in-progress work -> `00_WORK`.

## v02 note (vs v01)
In v02 STATUS is the **time cascade** Now -> Daily -> Weekly -> Monthly -> Yearly. The old Chronicle/Evidence/Health/Restricted/Archive/Audit are re-homed (Daily is the canonical dated-fact log; evidence is sealed in place; PII stays in `43_WHO_People/_restricted`; archive is a state flag; audit knobs stay in `06_CORE_Control`). See `INCONSISTENCIES_v02.md`. Slots `16`-`19` are reserved.

## Mutability (P4)
`11_STATUS_Now` {mutable} · `12`-`15` {append-only within the period, sealed/WORM once the period closes}.

## Derivatives
- `11_STATUS_Now` - live state (mutable).
- `12_STATUS_Daily` - end-of-day rollup.
- `13_STATUS_Weekly` - end-of-week rollup.
- `14_STATUS_Monthly` - end-of-month rollup.
- `15_STATUS_Yearly` - end-of-year rollup.
- `16_STATUS_Reserved` .. `19_STATUS_Reserved` - reserved.

## Mark
[BASE] - base folder of the STATUS family (5W2H spine).
