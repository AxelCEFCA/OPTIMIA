# 40_WHO - Entities [BASE]

> **5W2H - WHO:** Who is involved? Every actor: roles, units, people, teams, partners, suppliers, contacts, stakeholders, agents.

## What goes here
- **Roles** (RACI) and **organisational units**.
- **People** (PII, restricted), **teams**, **partners**, **suppliers**, **contacts**, **stakeholders**.
- **AI agents** as entities (synthetic principals).

## What does NOT go here
- The abstract org *model* -> `12_WHAT_OrgStructure`.
- Why a stakeholder matters -> `27_WHY_ValueProposition`.
- What an agent *does* -> `39_HOW_Automations`.
- **PII lives ONLY in `43_WHO_People/_restricted`** (no-RAG, gated).

## How to read the derivatives (laws)
1. **Canonical home + facets (P1)**: each thing has ONE home here; its other dimensions are read-only `facet:` pointers in the frontmatter, never copies.
2. **One catalogue (P5)**: the 4-letter code namespace lives in `05_CORE_Glossary`; trees here are *projections* of it.
3. **Plans emit facts (P3)**: lifecycle events are pointed at `12_STATUS_Daily`, not transcribed here.
4. **Generated index (P7)**: `index.html` / `index.json` are generated, not hand-edited.

## Derivatives
- `41_WHO_Roles` - Roles & responsibilities (RACI); roles-not-persons.
- `42_WHO_Org` - Units / departments.
- `43_WHO_People` - Real people / PII. RESTRICTED, no-RAG.
- `44_WHO_Teams` - Teams / working groups (cross-cutting).
- `45_WHO_Partners` - Partners / collaborations.
- `46_WHO_Suppliers` - Commercial suppliers / vendors.
- `47_WHO_Contacts` - Contact / distribution lists.
- `48_WHO_Stakeholders` - Stakeholder register (the entity).
- `49_WHO_Agents` - AI agents as entities.

## Mark
[BASE] - base folder of the WHO family (5W2H spine).
