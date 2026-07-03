# 10_WHAT - Definition [BASE]

> **5W2H - WHAT:** What exists? The identity, structure and catalogues of the things this memory knows.

## What goes here
- Stable **definitions**: the canonical record of each thing the system recognises (a system, a data entity, a closed catalogue).
- **Structure / taxonomy**: the `SystemTree`, projected from the CODE_CATALOG (see `05_CORE_Glossary`).
- **Closed catalogues**: enumerations of valid values (request types, channels, trackers).
- **Data models**: the shape (fields) of business entities.

## What does NOT go here
- What **happens or changes** -> `00_WORK` (in progress) or `10_STATUS` (occurred/current). No dated facts here.
- The **WHY** (purpose, decisions) -> `20_WHY`.
- The **HOW it works** (playbooks, procedures) -> `30_HOW`.
- **WHO** (roles, people, suppliers) -> `40_WHO`; here only referenced as `who:` facets.
- **WHERE** (physical locations) -> `50_WHERE`; here only `where:` facets.
- **Amounts / costs** -> `70_HOWMUCH`. A system record points at an amount, it does not copy it.

## How to read the derivatives (laws)
1. **Canonical home + facets (P1)**: each thing has ONE home here; its other dimensions are read-only `facet:` pointers in the frontmatter, never copies.
2. **One catalogue (P5)**: the 4-letter code namespace lives in `05_CORE_Glossary`; trees here are *projections* of it.
3. **Plans emit facts (P3)**: lifecycle events are pointed at `12_STATUS_Daily`, not transcribed here.
4. **Generated index (P7)**: `index.html` / `index.json` are generated, not hand-edited.

## Derivatives
- `11_WHAT_Root` - What the entity itself is, at the top level (the organisation/program this memory serves).
- `12_WHAT_OrgStructure` - The org chart as a model/structure (boxes and reporting lines).
- `13_WHAT_SystemTree` - The tree of systems/products the entity owns (functional identity).
- `14_WHAT_DataModel` - The schema of business entities (the shape of a 'request', a ticket, an incident).
- `15_WHAT_Catalogs` - Closed taxonomies / controlled vocabularies of the business.
- `16_WHAT_Services` - The catalogue of services/products the entity delivers.
- `17_WHAT_Assets` - Classes of assets / instruments / equipment.
- `18_WHAT_Standards` - External/internal specs that DEFINE (norms, formats).
- `19_WHAT_Reserved` - reserved.

## Mark
[BASE] - base folder of the WHAT family (5W2H spine).
