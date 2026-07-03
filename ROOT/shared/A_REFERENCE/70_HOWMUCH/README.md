# 70_HOWMUCH - Cost, effort, magnitude [BASE]

> **5W2H - HOWMUCH:** How much? The quantitative face of any topic: budget, procurement, costs, effort, metrics, resources, risks.

## What goes here
- **Budgets** (planned) and **costs** (actual/estimated).
- The master **procurement** file, **effort/capacity**, **metrics/KPIs**, **resource** quantities, **risk** registers.

## What does NOT go here
- The supplier entity -> `46_WHO_Suppliers`; the procedure -> `32_HOW_Procedures`; the invoice -> `03_WORK_Flow`.
- Live health figures -> `11_STATUS_Now`; the qualitative objective -> `26_WHY_Objectives`.

## How to read the derivatives (laws)
1. **Canonical home + facets (P1)**: each thing has ONE home here; its other dimensions are read-only `facet:` pointers in the frontmatter, never copies.
2. **One catalogue (P5)**: the 4-letter code namespace lives in `05_CORE_Glossary`; trees here are *projections* of it.
3. **Plans emit facts (P3)**: lifecycle events are pointed at `12_STATUS_Daily`, not transcribed here.
4. **Generated index (P7)**: `index.html` / `index.json` are generated, not hand-edited.

## Derivatives
- `71_HOWMUCH_Budget` - Budgets / planned amounts.
- `72_HOWMUCH_Procurement` - The master procurement file (amount/status of a purchase).
- `73_HOWMUCH_Costs` - Actual costs / estimates.
- `74_HOWMUCH_Effort` - Effort / capacity, planned-vs-reported.
- `75_HOWMUCH_Metrics` - KPIs / sizing figures.
- `76_HOWMUCH_Resources` - Quantities (licenses, quotas, headcount).
- `77_HOWMUCH_Risks` - Risk = severity x likelihood.
- `78_HOWMUCH_Reserved` - reserved.
- `79_HOWMUCH_Reserved` - reserved.

## Mark
[BASE] - base folder of the HOWMUCH family (5W2H spine).
