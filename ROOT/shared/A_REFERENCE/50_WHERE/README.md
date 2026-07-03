# 50_WHERE - Location & context [BASE]

> **5W2H - WHERE:** Where? Physical locations, sites, compute environments, networks, work context, zones.

## What goes here
- The **LocationTree** (buildings/sites), projected from the CODE_CATALOG.
- **Sites/campuses**, **compute environments** (cloud / on-prem / HPC), **networks**.
- **Work context** (office vs field) and **security/access zones**.

## What does NOT go here
- The system that sits there -> `13_WHAT_SystemTree` (here only a `where:` facet).
- The work itself -> `00_WORK`; the access policy -> `37_HOW_Policies`.

## How to read the derivatives (laws)
1. **Canonical home + facets (P1)**: each thing has ONE home here; its other dimensions are read-only `facet:` pointers in the frontmatter, never copies.
2. **One catalogue (P5)**: the 4-letter code namespace lives in `05_CORE_Glossary`; trees here are *projections* of it.
3. **Plans emit facts (P3)**: lifecycle events are pointed at `12_STATUS_Daily`, not transcribed here.
4. **Generated index (P7)**: `index.html` / `index.json` are generated, not hand-edited.

## Derivatives
- `51_WHERE_LocationTree` - Physical locations (buildings/sites tree).
- `52_WHERE_Sites` - Sites / campuses (macro).
- `53_WHERE_Compute` - Compute environments (where data runs).
- `54_WHERE_Networks` - Network topology / segments.
- `55_WHERE_Field` - Work context: office vs field/on-site.
- `56_WHERE_Zones` - Security / access zones, TLP.
- `57_WHERE_External` - Third-party premises.
- `58_WHERE_Reserved` - reserved.
- `59_WHERE_Reserved` - reserved.

## Mark
[BASE] - base folder of the WHERE family (5W2H spine).
