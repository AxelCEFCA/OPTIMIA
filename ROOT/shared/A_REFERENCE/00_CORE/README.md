# 00_CORE — the constitution of the memory [BASE]

> **What question does it answer?** *"What is this memory, what laws govern it, and how do I read the
> rest?"* This is the meta-layer: it contains the rules of the system, never business content.
>
> This memory exists so that both **people** and **AI agents** have the organisation's whole context —
> its what/why/how/who/where/when/how-much — in one navigable place; `00_CORE` holds the laws that keep
> that context single-homed, consistent and safe to load.

## The 5W2H spine in one screen

```
00_CORE     (meta)        rules, schema, catalogues, governance, profile
10_WHAT     What?         definition (systems, data models, catalogues)
20_WHY      Why?          purpose (the deep "why"), decisions
30_HOW      How?          playbooks, procedures, processes, policies
40_WHO      Who?          roles, people, teams, partners, suppliers, agents
50_WHERE    Where?        locations, sites, compute, networks
60_WHEN     When?         planning / future / cadence (the "should")
70_HOWMUCH  How much?     cost, effort, magnitude
00_WORK     (work)        Inbox / Outbox / Flow (expedientes)          [B_OPERATIONS]
10_STATUS   (status)      Now + Daily/Weekly/Monthly/Yearly rollups    [B_OPERATIONS]
```

## What lives in CORE (01–09)

| Folder | Role |
|--------|------|
| `00_CORE` | This constitution + index of the rules. |
| `01_CORE_Schema` | The formal model: 10 buckets, the X0..X9 numbering rule, the page anatomy. |
| `02_CORE_Templates` | Blank memory-page templates (ADR, record, ticket). |
| `03_CORE_Rules` | How to fill/place each bucket: routing algorithm + 100 criteria + conflict closure. |
| `04_CORE_Governance` | The hard laws P1–P8, SEAL, RAG-EXIT, REDACTION, promotion, intake, human-in-the-loop. |
| `05_CORE_Glossary` | Canonical glossary + the single CODE_CATALOG (4-letter codes). |
| `06_CORE_Control` | The machine control-plane: ownership, router, RAG manifest, path aliases. |
| `07_CORE_Index` | Spec + generator of `index.html` (human) and `index.json` (machine). |
| `08_CORE_Profile` | **The swappable instance profile** — the one place that changes per organisation. |
| `09_CORE_Flow` | The raw → processed → recorded → sealed information-flow definition. |

## The three laws you must never break

1. **Canonical home + facets (P1).** One thing, one home (single-writer); every other dimension is a
   read-only pointer. Never copy across buckets.
2. **Entity ≠ Work ≠ Event (master rule).** An entity's identity lives in its thematic home (even with
   live state); its tasks → WORK; its events/state/evidence → STATUS; linked by id / `correlation_id`.
3. **Speak by role, never by person.** PII lives only in `43_WHO_People/_restricted`, gated and no-RAG.

## License & attribution

This is an **OPTIMIA-type structured memory**, released under the **MIT License** (see `ROOT/LICENSE`). If
you reuse the idea/architecture, please cite CEFCA's SPIE 2026 (Copenhagen) OPTIMIA papers and link the
project's GitHub. Full declaration, citation and the plain-language **no-warranty** clause:
[`LICENSE_AND_ATTRIBUTION.md`](LICENSE_AND_ATTRIBUTION.md). The agent-mirror & consolidation model is in [`AGENT_CONSOLIDATION.md`](AGENT_CONSOLIDATION.md).

## What does NOT go here

- Any business content (a system, a person, a purchase) → its W home.
- The instance's concrete configuration → `08_CORE_Profile` (CORE holds the *generic* rules).

## Mark
[BASE] — base folder of the CORE family (the memory's own meta-rules).
