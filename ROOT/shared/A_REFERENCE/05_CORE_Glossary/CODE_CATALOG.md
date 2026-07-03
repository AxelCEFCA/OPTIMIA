---
id: CodeCatalog
home: shared/A_REFERENCE/05_CORE_Glossary/CODE_CATALOG
owner: role:leadership
status: approved
sensitivity: internal
twin: META
---

# CODE_CATALOG — the single 4-letter code namespace (P5)

> **One catalogue, two projections.** All short codes live here once. `13_WHAT_SystemTree` projects the
> `what` codes; `51_WHERE_LocationTree` projects the `where` codes. Neither owns the codes — this file
> does. This prevents a system code and a location code from clashing.

## Format
- A code is **4 letters**, uppercase.
- Each code declares a `facet`: `what` (a system/thing) or `where` (a location).
- Locations may share a **building prefix** (declared in `08_CORE_Profile.domain_codes.building_prefix`).

## Catalogue (fill on configuration)

| Code | facet | Meaning |
|------|-------|---------|
| `<C1>` | what  | `<system / thing>` |
| `<C2>` | what  | `<system / thing>` |
| `<L1>` | where | `<location>` |
| `<L2>` | where | `<location>` |

> Empty in the template. During configuration (CONFIG block G), replace the placeholder rows with the
> organisation's real codes and keep this as the single source of truth. References elsewhere resolve a
> code **through this catalogue**, never by guessing from a path.
