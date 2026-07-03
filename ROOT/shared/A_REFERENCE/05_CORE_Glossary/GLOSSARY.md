---
id: Glossary
home: shared/A_REFERENCE/05_CORE_Glossary
owner: role:leadership
status: approved
sensitivity: internal
twin: META
---

# 05_CORE_Glossary — canonical terms of the memory system

> **What question does it answer?** *"What do the words this memory uses mean?"* This is the glossary of
> the **system's own** vocabulary. The business vocabulary (closed catalogues) lives in
> `15_WHAT_Catalogs`; the 4-letter code namespace lives in [`CODE_CATALOG.md`](CODE_CATALOG.md).

## Core terms

| Term | Meaning |
|------|---------|
| **5W2H** | The organising axis: What / Why / How / Who / Where / When + How-much. |
| **Bucket / family** | One of the 10 top numeric groups (`00_CORE` … `10_STATUS`). |
| **Canonical home (P1)** | The single folder where an item's identity is written; one owner (single-writer). |
| **Facet** | A read-only pointer in the frontmatter to one of the item's other dimensions. No copying. |
| **Chamber** | A first-level grouping: `A_REFERENCE`, `B_OPERATIONS`, `C_OPERATIONAL_KIT`. Navigation, not address. |
| **Compiled Truth** | The current curated state of a page; rewritable only by the owner. |
| **Timeline** | The append-only log section of a page; each line cites `[Source: …]`. |
| **SEAL / WORM** | Sealing a datum into `03_WORK_Flow` as immutable (write-once-read-many). |
| **RAG-EXIT** | The rule for what enters the retrieval corpus: `approved AND NOT superseded`, minus exclusions. |
| **REDACTION** | Anonymisation: replace people with roles before any public-cloud output. |
| **Promotion** | The handshake that moves an agent's content from `00_WORK` to a shared canonical home. |
| **correlation_id** | A stable `yymmdd-NN` id threading every page generated from one intake. |
| **twin** | Optional `PHYS/OPER/ORG/META` label (the retired "digital twin" axis kept as a facet). |
| **Entity ≠ Work ≠ Event** | The master rule: identity → its W home; tasks → WORK; events/state → STATUS. |
| **CODE_CATALOG** | The single source of 4-letter codes, with `facet: what|where` (see `CODE_CATALOG.md`). |

## What does NOT go here
- Business taxonomies (request types, channels, trackers) → `15_WHAT_Catalogs`.
- Definitions of business *things* (a system, a service) → `10_WHAT`.

> Tip: an organisation often also needs a **domain glossary** (its own jargon). Put that in
> `35_HOW_KnowledgeBase` or `15_WHAT_Catalogs`; keep this file for the memory system's own terms.
