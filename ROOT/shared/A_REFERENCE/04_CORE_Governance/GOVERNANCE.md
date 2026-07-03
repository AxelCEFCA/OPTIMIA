---
id: Governance
home: shared/A_REFERENCE/04_CORE_Governance
owner: role:leadership
status: approved
sensitivity: internal
twin: META
---

# 04_CORE_Governance — the hard laws of the memory

> **What question does it answer?** *"Which rules cannot be broken, who may write what, and how are
> things sealed, promoted and anonymised?"* This is the constitution of the system.

## What goes here
- The laws **P1–P8**.
- The **writing** rules (single-writer, coarse-lock).
- The **SEAL**, **RAG-EXIT**, **REDACTION (GDPR)**, **promotion** and **intake** processes.
- The **human-in-the-loop** principle.

## What does NOT go here
- The concrete configuration (who owns what) → `06_CORE_Control/ownership.yaml`.
- The concrete RAG corpus → `06_CORE_Control/rag_manifest.yaml`.

---

## The laws P1–P8

### P1 — Canonical home + facets (the mother law)
Every item has **ONE home** (single-writer). Its other dimensions are **read-only facets** in the
frontmatter (pointers). What **happens/changes** lives in `00_WORK` (in progress) or `10_STATUS`
(occurred/current), with a stable id + facets. **No content is duplicated across buckets: cross-links
are POINTERS.**

> Canonical example — a decision: the **why** lives in `28_WHY_Decisions/<Decision>.md`; the **dated
> fact** in `12_STATUS_Daily/decisions/<date>_<Decision>.md`; the **evidence** in
> `03_WORK_Flow/...`. Three faces, zero duplication.

### P2 — Two sinks
`00_CORE` = rules/catalogues · `10_STATUS` = facts/evidence. Every datum eventually drains into one or
the other; nothing sits in limbo.

### P3 — WHEN = should, STATUS = is/was
`60_WHEN` holds plans/cadences (what *should* happen). `10_STATUS` holds what *happened/is*. A plan
**does not move** when its date passes: it **emits** a fact in STATUS and remains in WHEN.

### P4 — Immutability per subdirectory
`11_STATUS_Now` {mutable} · `12_STATUS_Daily` (and Weekly/Monthly/Yearly) {append-only, sealed on close} · sealed evidence is WORM **in place** (immutable Inbox originals, sealed expediente artefacts, closed rollups) · archiving is a **state flag** (R4).

### P5 — One CODE_CATALOG
A single 4-letter code catalogue in `05_CORE_Glossary` (facet `what|where`, building prefix). WHAT/WHERE
are **projections** of the catalogue, not parallel sources.

### P6 — Migration = indirection
Moving something is done with `PATH_ALIASES` in `06_CORE_Control`, **never** by rewriting sealed evidence.
IDs are stable and not derived from the path.

### P7 — Generated dual index
`index.html` (human) + `index.json` (machine), **both generated**; never hand-edited. A gate fails if the
committed index does not match the regenerated one.

### P8 — Twins as a facet
PHYS/OPER/ORG/META **retired as an axis**; kept as the optional `twin:` facet.

---

## Writing: single-writer at a time (coarse-lock)
- Each canonical home has **one owner** (a role) that may rewrite its *Compiled Truth*.
- Concurrency is handled with a **coarse lock**: the whole file/home is locked while a writer works;
  there is no line-level merge on Compiled Truth.
- **Teams** (`03_WORK_Flow`): the multi-writer exception, with **claim-then-lock** — a member
  claims the item, locks it, writes and releases.

## SEAL (sealing to evidence)
- Evidence is **sealed in place** (v02): a received original in `01_WORK_Inbox`, a sent message in `02_WORK_Outbox/5_SENT`, a decisive artefact inside its expediente in `03_WORK_Flow`, or a closed period rollup in `1X_STATUS`. Mark it `immutable: true` with `sealed_from: <path>@<git-sha>`; a heavy copy of deliverables goes to `_OUTPUT`.
- Once sealed it is **WORM**: never rewritten. Any later change is modelled with a new fact/alias (P6),
  not by editing the seal.

## RAG-EXIT (what enters the retrieval corpus)
- **Corpus = `status: approved` AND NOT `superseded`.**
- **Always excluded**: `43_WHO_People` (PII), anything tagged `sensitivity: restricted`, items flagged `ARCHIVED`/superseded, and `11_STATUS_Now` (mutable, unstable). Operating detail in `06_CORE_Control/rag_manifest.yaml`.

## REDACTION (GDPR / anonymisation)
- Before any output to a **public cloud**, data passes through **anonymisation**: PII is redacted and
  people are replaced by **roles**.
- Speak **by role, never by person** in all publishable content.
- Real people only in `43_WHO_People/_restricted` with `sensitivity: pii`.

## Promotion (handshake)
- An agent's work is **promoted** from its workspace (an expediente in `03_WORK_Flow`, or a draft within it) to the shared shelf via a **handshake** declaring the `target:` canonical home.
- It is a **handshake**: the agent proposes → **human-in-the-loop** review → on approval, the content
  lands in its W home and the event is chronicled in `12_STATUS_Daily`.
- **Periodic agent consolidation:** on a configured cadence (`08_CORE_Profile.agents.consolidation.cadence`, e.g. monthly/yearly) each agent's period STATUS rollup is consolidated — as a **summary + pointer** — into the **shared** STATUS rollup of the same period, via the same handshake. See `00_CORE/AGENT_CONSOLIDATION.md`.

## Intake (fan-out)
- Everything that enters (`01_WORK_Inbox`) is **classified at intake** and routed to an expediente type in `03_WORK_Flow`, generating W-bucket facets (see `06_CORE_Control/router_rules.yaml`).
- A raw item is **never discarded**: low confidence → quarantine, not deletion.

## Human-in-the-loop
- No **publication** and no **action on systems** is executed without human review.
- **Hard boundary**: the AI is *advise-only* over the organisation's control systems — it never writes
  to them. Declare those systems in `08_CORE_Profile.boundaries`.
