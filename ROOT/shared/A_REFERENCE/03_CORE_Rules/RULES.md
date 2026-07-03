---
id: Rules
home: shared/A_REFERENCE/03_CORE_Rules
owner: role:leadership
status: approved
sensitivity: internal
twin: META
---

# 03_CORE_Rules — how to fill and place each bucket

> **What question does it answer?** *"Given a piece of information, where does it go and how do I write
> it?"* The full algorithm and the per-folder criteria are in
> [`ClassificationCriteria.md`](ClassificationCriteria.md); this file is the orientation + the writing
> conventions.

## Where to put things
Use the routing algorithm in `ClassificationCriteria.md` (apply in order; first match wins), then the
per-folder criterion (units digit). Master rule: **one canonical home + facets**; **Entity ≠ Work ≠
Event**.

## Naming conventions
- **Folders:** `NN_BUCKET_Concept` in English PascalCase (e.g. `13_WHAT_SystemTree`). The **full name is
  the address**; the chamber (A/B/C) is only the aisle.
- **Pages:** `id` in PascalCase or a domain code; file dated artefacts `yyMMdd_Name`.
- **Language:** folder/concept names are always English; page *content* may be in the organisation's
  language (declared in `08_CORE_Profile.language`).

## Writing conventions
- **Page anatomy** (see `01_CORE_Schema`): frontmatter + `Compiled Truth` (owner-rewritable) +
  `Timeline` (append-only, each line `[Source:]`).
- **Append-only** zones (`12_STATUS_Daily` and the Weekly/Monthly/Yearly rollups) are never rewritten once their period closes; you add lines/rollups.
- **Sealed** artefacts (immutable Inbox originals, sealed expediente artefacts, closed rollups) are WORM; you never edit, you point.
- **File naming** per B_OPERATIONS bucket is defined in [`NAMING.md`](NAMING.md).
- **Roles, not persons**, everywhere except `43_WHO_People/_restricted`.

## What does NOT go here
- The authority of who-owns-what (the *law*) → `04_CORE_Governance`; the executable config → `06_CORE_Control`.
- The instance specifics (real catalogues, codes) → `08_CORE_Profile` + the relevant W home.
