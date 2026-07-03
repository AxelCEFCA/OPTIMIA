# 00_WORK - Work [BASE]

> **5W2H - WORK:** Live, in-progress work (mutable, stateful). Two message trays and one expediente flow. When an expediente closes it EMITS a fact to STATUS (the day's rollup).

## What goes here
- `01_WORK_Inbox` - **all** received messages, from every channel (one immutable file per message).
- `02_WORK_Outbox` - **all** outgoing messages, under human approval (state = subfolder).
- `03_WORK_Flow` - the **expediente flow**: one subdirectory per expediente **type**, and inside each, one folder per expediente (a case file with all its artefacts together).
- `04_WORK_Reserved` .. `09_WORK_Reserved` - **reserved** slots (see below).

## What does NOT go here
- Finished periodic state / sealed rollups -> `10_STATUS`.
- The process *definition* (the expediente state machine) -> `33_HOW_Processes`.
- Heavy generated deliverables -> `B_OPERATIONS/_OUTPUT`.

## v02 note (vs v01)
In v02 the intake/triage/pipeline/coordination/drafts/promotion/processed folders (old `03`-`09`) are **absorbed into the expediente flow**: each expediente carries its own state and artefacts. The freed slots `04`-`09` are **reserved**. Triage becomes an action at Inbox intake; the ticket lifecycle becomes expediente metadata; promotion to `A_REFERENCE` is a handshake from the expediente. See `09_CORE_Flow` and `INCONSISTENCIES_v02.md`.

## How to read the derivatives (laws)
1. **Canonical home + facets (P1)**: each thing has ONE home; other dimensions are read-only facets.
2. **Plans emit facts (P3)**: when an expediente closes, it emits a line into the day's rollup (`12_STATUS_Daily`).
3. **Generated index (P7)**: `index.html` / `index.json` are generated, not hand-edited.

## Derivatives
- `01_WORK_Inbox` - all received messages (every channel).
- `02_WORK_Outbox` - all outgoing messages (human approval).
- `03_WORK_Flow` - the expediente flow (types -> expedientes).
- `04_WORK_Reserved` .. `09_WORK_Reserved` - reserved.

## Mark
[BASE] - base folder of the WORK family (5W2H spine).
