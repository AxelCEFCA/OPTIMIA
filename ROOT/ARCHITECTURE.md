# ARCHITECTURE — Generic 5W2H Memory Template V04

**Project:** OPTIMIA — Generic 5W2H Memory Template, version **V04**
**Root:** the repository `ROOT/` (this template)
**Project / owner:** CEFCA (Centro de Estudios de Física del Cosmos de Aragón) — OPTIMIA project · 2026 · (MIT, © Axel Yanes Díaz — see `ROOT/LICENSE`)
**Language:** English (generic, organisation-agnostic)
**Status:** Reusable, unconfigured template (a blank skeleton adapted per organisation)

> This document is a reference to the *whole* architecture: its philosophy, its three chambers, the 5W2H
> spine, the operational model, the hard laws, the page anatomy, the information flow, the operating kit,
> the customisation lifecycle, the reproducible build, and the versioning history. It synthesises the
> canonical sources under `ROOT/shared/` (`START_HERE.md`, the `A_REFERENCE/00_CORE` files, and the
> `B_OPERATIONS/03_WORK_Flow` README) — it does not replace them.

---

## Table of contents

1. [Overview & philosophy](#1-overview--philosophy)
2. [The three chambers](#2-the-three-chambers)
3. [The 5W2H spine (A_REFERENCE)](#3-the-5w2h-spine-a_reference)
4. [B_OPERATIONS — the now (v02/v03 model)](#4-b_operations--the-now-v02v03-model)
5. [The hard laws P1–P8 and the operating principles](#5-the-hard-laws-p1p8-and-the-operating-principles)
6. [Page anatomy & format policy](#6-page-anatomy--format-policy)
7. [The information flow (raw → sealed)](#7-the-information-flow-raw--sealed)
8. [The operating kit (C_OPERATIONAL_KIT) & the agent mirror](#8-the-operating-kit-c_operational_kit--the-agent-mirror)
9. [Configuration & customisation lifecycle](#9-configuration--customisation-lifecycle)
10. [Reproducible build & versioning](#10-reproducible-build--versioning)
11. [License & attribution](#11-license--attribution)

---

## 1. Overview & philosophy

### 1.1 What an OPTIMIA-type structured memory is

An **OPTIMIA-type structured memory** is a file-system-shaped, human-and-machine-readable knowledge base
that is deliberately organised so that **every piece of information has exactly one obvious home**. It is
not a database and not a wiki: it is a *disciplined filesystem* of lightweight HTML/Markdown pages, each
carrying structured frontmatter, governed by a small set of non-negotiable laws. Its purpose is to be the
**shared long-term memory** of an organisation *and* the operating substrate its AI agents read from and
write to.

It serves two audiences at once:

- **Humans** — who navigate it through generated `index.html` landing pages ("three doors": REFERENCE,
  OPERATIONS, KIT) and read the pages directly.
- **AI agents** — who load the generated `index.json`, apply the routing algorithm to classify incoming
  information, work cases, and propose promotions of new knowledge — always under human review.

The template ships **blank and generic**: nothing here names a real organisation, person, system or
vendor. It becomes a specific organisation's memory only after it is **configured** (see §9).

**Conceived for observatories, applicable to any organisation.** The project was originally designed for
entities that **build and operate astrophysical observatories** — that heritage shows only in the *default*
`03_WORK_Flow` themes and a few examples. The architecture itself (the 5W2H spine, the laws, the runtime
model) is **domain-agnostic**, and the default configuration is **deliberately open and general** so that
**any type of organisation** — research centre, hospital, factory, agency, NGO, software team — can adopt
it and, during configuration, re-label/prune/extend the themes to its own reality. Only the profile and the
`03_WORK_Flow` taxonomy change; the skeleton and the laws stay the same.

### 1.2 Why 5W2H

The backbone is the classic **5W2H** interrogative frame — *What, Why, How, Who, Where, When, How much* —
used as the **primary axis of classification**. Any descriptive fact answers one of these questions best,
so 5W2H gives a small, exhaustive, mutually intelligible set of top-level "families" that both a person
and an agent can reason about without training. To this descriptive spine the template adds two runtime
families — **WORK** (the in-progress) and **STATUS** (the is/was) — yielding **10 buckets** in total.

| Question | Family | Holds |
|----------|--------|-------|
| (meta) | `00_CORE` | Rules, schema, catalogues, governance, profile |
| What? | `10_WHAT` | Definition / identity (systems, data models, catalogues) |
| Why? | `20_WHY` | Purpose, mission, decisions (the deep "why") |
| How? | `30_HOW` | Playbooks, procedures, processes, policies |
| Who? | `40_WHO` | Roles, people, teams, partners, suppliers, agents |
| Where? | `50_WHERE` | Locations, sites, compute, networks |
| When? | `60_WHEN` | Planning / future / cadence (the "should") |
| How much? | `70_HOWMUCH` | Cost, effort, magnitude, risk |
| (work) | `00_WORK` | Inbox / Outbox / Flow — daily work in progress |
| (status) | `10_STATUS` | Now + periodic rollups — the "is/was" |

### 1.3 The core intuition: one home + facets

The single idea that makes the whole system coherent is **P1 — canonical home + facets**: a thing lives
in exactly one place (single-writer), and all its other dimensions are recorded as **read-only pointers**
(facets) in that page's frontmatter. A purchase is *cost* (`72`), involves a *supplier* (`46`), follows a
*procedure* (`32`), and produces *evidence* (`03_WORK_Flow`) — but the content is never copied; the faces
are just links. This removes duplication, contradiction and "which copy is right?" ambiguity by
construction.

### 1.4 Why this matters for AI agents (giving them the organisation's context)

This is the whole point. An LLM agent arrives with **zero knowledge of the organisation** — it does not
know its mission, its roles, its systems, its procedures, its suppliers, its plans, its budgets or its
history. This memory is the **single, navigable place that holds all of that context** so the agent can
act as an informed member of the organisation instead of guessing.

The 5W2H structure is what makes that context *loadable and trustworthy*:

- **`A_REFERENCE` (00–79) is the agent's ground truth** — the curated, slow-changing description of *what*
  exists, *why*, *how* it works, *who* is involved, *where*, *when* and *how much*. To give an agent
  context is, concretely, to let it retrieve the right A_REFERENCE pages.
- **The generated `index.json` is the agent's map** and the **routing algorithm** (`03_CORE_Rules`) tells
  it exactly where any new fact belongs, so it files things back consistently instead of inventing places.
- **RAG-EXIT (§5.2) is the context filter**: it selects exactly the `approved`, non-PII, non-superseded
  subset the agent may load — so the agent is grounded on *vetted* organisational knowledge, never on raw
  PII or stale drafts.
- **Roles-not-persons + human-in-the-loop** keep that context safe to use and safe to publish.
- **Per-agent mirrors + consolidation** (`agents/`, `00_CORE/AGENT_CONSOLIDATION.md`) mean each agent gets
  its own **scaled copy of this context** for its area and feeds its summaries back, so the shared context
  keeps growing with what the agents learn.

In one line: **5W2H is a discipline for turning an organisation's scattered knowledge into a single
context an AI agent (and a human) can load, trust, extend and hand off** — the reason the whole template
exists.

---

## 2. The three chambers

The memory is split into three top-level chambers under `ROOT/shared/`, plus a private per-agent mirror
under `ROOT/agents/`.

```
ROOT/
├── LICENSE                       MIT license (CEFCA / OPTIMIA, 2026)
├── _TREE.txt                     generated full-tree snapshot
├── shared/                       the shared memory (all three chambers)
│   ├── index.html                navigable landing page (three doors)
│   ├── START_HERE.md             first file any agent/person reads
│   ├── A_REFERENCE/              [CONTENT] the permanent MODEL — you CONSULT it
│   ├── B_OPERATIONS/             [CONTENT] the NOW — you WORK in it
│   └── C_OPERATIONAL_KIT/        [INFRASTRUCTURE] how you operate & produce
└── agents/
    └── agent01/                  an agent's private mirror (copy & rename per agent)
        ├── A_REFERENCE/  B_OPERATIONS/  C_OPERATIONAL_KIT/  README.md
```

| Chamber | Nature | Change rate | Format | One-line role |
|---------|--------|-------------|--------|----------------|
| **A_REFERENCE** | Content — the descriptive model | Slow, curated | Lightweight HTML | The permanent model you *consult* |
| **B_OPERATIONS** | Content — the runtime | Fast, live | Lightweight HTML (heavy in `_OUTPUT`) | The *now* you *work* in |
| **C_OPERATIONAL_KIT** | Infrastructure — the operating kit | Permanent | Markdown (skills), Python (tools) | *How* you operate and produce |

- **A_REFERENCE** is the **stable retrieval corpus**: curated, slow-changing descriptive knowledge,
  numbered **00–79** across 8 families. You look things up here; you rarely change it, and only through
  the promotion handshake.
- **B_OPERATIONS** is the **runtime**: incoming/outgoing messages, live case-work (expedientes) and the
  chronicle of what happened. It is numbered **00–19** (WORK `0X` + STATUS `1X`) plus `_OUTPUT`.
- **C_OPERATIONAL_KIT** is **permanent infrastructure** that *serves* the other two but is not itself
  5W2H content: the skills that describe how to operate, the brand resources, the production tools, and
  the service registry.

Each chamber has its own generated `index.html` (+ `index.json`) and its numbering is **independent** —
so zones are always referred to by their **full name** (`03_WORK_Flow`, `12_STATUS_Daily`), never by
number alone (the number `12` means `12_WHAT_OrgStructure` in A but `12_STATUS_Daily` in B).

---

## 3. The 5W2H spine (A_REFERENCE)

A_REFERENCE contains **8 families** — `00_CORE` plus the seven interrogatives — each a base folder `NN0`
with up to nine derivatives `NN1..NN9`.

### 3.1 The X0..X9 derivative rule

Inside each family the numbering is systematic:

- `NN0` — the family **base folder**; it carries the README that explains how to read its derivatives.
- `NN1..NN8` — **stable subcategories**, each with a fixed meaning declared in the profile.
- `NN9` — by convention **Reserved** (or the last subcategory); it never moves and carries a
  `RESERVED: what will go here` note, leaving room to grow without renumbering neighbours.

Example (`40_WHO`): `41_WHO_Roles`, `42_WHO_Org`, `43_WHO_People`, … `49_WHO_Agents`; `40_WHO/README.md`
explains the family.

### 3.2 `00_CORE` — the constitution (00–09)

`00_CORE` holds the memory's own meta-rules; it never holds business content.

| Folder | Role |
|--------|------|
| `00_CORE` | The constitution + index of the rules (this family's base). |
| `01_CORE_Schema` | The formal model: 10 buckets, the X0..X9 rule, the page anatomy, the `twin` facet, node types. |
| `02_CORE_Templates` | Blank **memory-page** moulds (ADR, record, ticket) — vs `38_HOW_Templates` (business output). |
| `03_CORE_Rules` | How to fill/place each bucket: routing algorithm + the 100 folder criteria + naming + conflict closure. |
| `04_CORE_Governance` | The hard laws P1–P8, SEAL, RAG-EXIT, REDACTION, promotion, intake, human-in-the-loop. |
| `05_CORE_Glossary` | Canonical glossary + the single **CODE_CATALOG** (4-letter codes; facet `what`/`where`). |
| `06_CORE_Control` | The machine control-plane: `ownership.yaml`, `router_rules.yaml`, `rag_manifest.yaml`, `PATH_ALIASES`. |
| `07_CORE_Index` | Spec + generator of `index.html` (human) and `index.json` (machine). |
| `08_CORE_Profile` | **The swappable instance profile** — the one place that changes per organisation. |
| `09_CORE_Flow` | The raw → processed → recorded → sealed information-flow definition. |

### 3.3 The seven interrogative families (10–79)

Each family answers one question; the derivatives split it by a units-digit criterion. The most important
disambiguations (from `ClassificationCriteria.md`) are shown per family.

**`10_WHAT` — definition (what it is), static and timeless**
`11_WHAT_Root` (what the entity is) · `12_WHAT_OrgStructure` (org chart as a model) · `13_WHAT_SystemTree`
(tree of systems, identity) · `14_WHAT_DataModel` (entity schema, not instances) · `15_WHAT_Catalogs`
(closed business taxonomies) · `16_WHAT_Services` · `17_WHAT_Assets` (asset classes) · `18_WHAT_Standards`
(specs that define) · `19_WHAT_Reserved`.

**`20_WHY` — purpose/justification (timeless); the dated fact goes to STATUS**
`21_WHY_Purpose` · `22_WHY_Mission` · `23_WHY_Vision` · `24_WHY_Values` · `25_WHY_Principles`
(roles-not-persons, HITL, control-systems boundary) · `26_WHY_Objectives` (OKR) · `27_WHY_ValueProposition`
· `28_WHY_Decisions` (rationale/ADR — the *why*, linked to the dated fact in `12_STATUS_Daily`) ·
`29_WHY_Impact`.

**`30_HOW` — operation (how), timeless; execution goes to WORK**
`31_HOW_Playbooks` (end-to-end) · `32_HOW_Procedures` (step-by-step SOP) · `33_HOW_Processes` (state
machines — the *definition* of a lifecycle) · `34_HOW_Methods` · `35_HOW_KnowledgeBase` (model cards,
binding regulations, FAQ/RAG) · `36_HOW_Integrations` (connectors, gateway, anonymisation) ·
`37_HOW_Policies` (RBAC, requires_confirmation) · `38_HOW_Templates` (business output moulds) ·
`39_HOW_Automations` (what the router / scheduled jobs do).

**`40_WHO` — entities**
`41_WHO_Roles` (RACI) · `42_WHO_Org` (units/departments) · `43_WHO_People` (**real people, PII,
RESTRICTED, no-RAG — the only place PII may live**) · `44_WHO_Teams` · `45_WHO_Partners` ·
`46_WHO_Suppliers` · `47_WHO_Contacts` (distribution lists) · `48_WHO_Stakeholders` · `49_WHO_Agents`
(AI agents as entities).

**`50_WHERE` — location/context**
`51_WHERE_LocationTree` (physical locations, building prefix) · `52_WHERE_Sites` · `53_WHERE_Compute`
(cloud/on-prem/HPC) · `54_WHERE_Networks` · `55_WHERE_Field` (office vs field) · `56_WHERE_Zones`
(security/TLP zones) · `57_WHERE_External` (third-party premises) · `58/59_WHERE_Reserved`.

**`60_WHEN` — planning/future (the "should"); if it passed, it emits a fact to STATUS**
`61_WHEN_Calendar` (CalDAV) · `62_WHEN_Schedule` (person×day / shifts) · `63_WHEN_Cadences` (recurring
rhythms) · `64_WHEN_OnCall` · `65_WHEN_Milestones` (deadlines, tenders) · `66_WHEN_Triggers` ·
`67_WHEN_Roadmap` (phases) · `68/69_WHEN_Reserved`.

**`70_HOWMUCH` — cost/effort/magnitude**
`71_HOWMUCH_Budget` (planned) · `72_HOWMUCH_Procurement` (master purchase file) · `73_HOWMUCH_Costs`
(actual) · `74_HOWMUCH_Effort` (capacity, plan-vs-reported hours) · `75_HOWMUCH_Metrics` (KPIs) ·
`76_HOWMUCH_Resources` (quantities: licenses, quotas) · `77_HOWMUCH_Risks` (severity×likelihood) ·
`78/79_HOWMUCH_Reserved`.

---

## 4. B_OPERATIONS — the now (v02/v03 model)

B_OPERATIONS is the runtime. It has two families — **`00_WORK`** (`0X`) and **`10_STATUS`** (`1X`) — plus
`_OUTPUT` for heavy deliverables.

```
B_OPERATIONS/
├── 00_WORK/
│   ├── 01_WORK_Inbox/      all incoming messages, every channel (immutable)
│   ├── 02_WORK_Outbox/     all outgoing messages, human-approved
│   ├── 03_WORK_Flow/       the expediente flow, by NUMBERED THEME
│   └── 04_WORK_Reserved … 09_WORK_Reserved
├── 10_STATUS/
│   ├── 11_STATUS_Now/      live state (mutable)
│   ├── 12_STATUS_Daily/    end-of-day rollup + canonical dated-fact log
│   ├── 13_STATUS_Weekly/   14_STATUS_Monthly/  15_STATUS_Yearly/   (rollups)
│   └── 16_STATUS_Reserved … 19_STATUS_Reserved
└── _OUTPUT/                heavy generated deliverables (PDF, embedded HTML)
```

### 4.1 `01_WORK_Inbox` — all incoming (the input sink)

Every incoming message, on **every channel**, is written as **one immutable HTML file**. It is never
discarded (intake law): low-confidence items stay here flagged for human triage. `01_WORK_Inbox` is
**symmetric** to `02_WORK_Outbox`.

- **Naming:** `yymmdd_hhmmss_CHANNEL_SenderId_Subject.html`
- `CHANNEL` — a closed catalogue in `08_CORE_Profile.enums.channels` (default
  `EMAIL WHATSAPP TELEGRAM PHONE VIDEOCONF INPERSON`), optionally glued to the receiving account
  (`EMAILops` = the EMAIL account *ops*).
- `SenderId` — short id of the sender + their org (`acmeco`).
- `Subject` — CamelCase, no spaces/accents.
- **Example:** `260701_102311_EMAILops_acmeco_RequestQuoteRenewal.html`

### 4.2 `02_WORK_Outbox` — all outgoing (the output sink, human-approved)

Every outgoing message passes through **approval states encoded as subfolders**. On SEND, a heavy copy
goes to `_OUTPUT`; the sent file stays as the record.

```
1_PROPOSED  →  2_EDITING  →  3_APPROVED  →  5_SENT
                                   └────────→  4_DISCARDED
```

- **Naming:** `yymmdd_hhmmss_CHANNEL_RecipientId_Subject.html` (advances through the state subfolders).
- Nothing is sent without human review (human-in-the-loop).

### 4.3 `03_WORK_Flow` — the expediente flow (numbered thematic taxonomy)

This is where **the actual case-work lives**. It is a **numbered, thematic taxonomy** of expediente
**types**: the **tens digit is a super-theme band**, so related workflows keep adjacent suffix numbers,
and gaps are deliberate room to grow without renumbering. Inside each theme, each **expediente is a
directory** gathering all its artefacts.

```
03_WORK_Flow/
  NN_Theme/                                a numbered theme (band by tens digit)
    yymmdd_SubjectInPascalCase_V01/        one expediente (a case-file directory)
      _expediente.html                     cover: id, type, estado, ambito, timeline
      yymmdd_KIND_Detail.ext               the expediente's artefacts
```

**Numbering bands (related themes stay adjacent):**

| Band | Super-theme |
|------|-------------|
| `00–09` | General / cross-cutting |
| `10–19` | Administration, Governance & Compliance |
| `20–29` | Scientific |
| `30–39` | Engineering & Technical |
| `40–49` | Outreach & External Relations |
| `50+` | Free for organisation-specific super-themes |

**The 27 default themes** (shipped; each organisation adapts them within their band):

- **00–09 General** — `00_General`.
- **10–19 Administration, Governance & Compliance** — `10_Governance` · `11_RulesAndRegulations` ·
  `12_ArtificialIntelligenceCommittee` · `13_ComplianceAndCybersecurity` · `14_ContractsAndTenders` ·
  `15_Purchases` · `16_GrantsAndFunding` · `17_HumanResources` · `18_SafetyRiskPrevention`.
- **20–29 Scientific** — `20_ScientificArea` · `21_ScientificOperation` · `22_ObservingPrograms` ·
  `23_ScientificDataProcess` · `24_DataReleasesAndPublications`.
- **30–39 Engineering & Technical** — `30_Engineering` · `31_Projects` · `32_Developments` ·
  `33_EngineeringChanges` · `34_CommissioningAndAcceptance` · `35_Maintenance` · `36_Incidents` ·
  `37_FacilitiesAndSite` · `38_ITandOT`.
- **40–49 Outreach & External Relations** — `40_OutreachArea` · `41_EventsAndOutreach` · `42_WorkingGroups`.

> **Adaptation is mandatory.** These themes are a broad default for an organisation that operates
> astrophysical observatories. Every organisation must tailor `03_WORK_Flow` — add, remove, rename or
> renumber themes *within their band* — and record the agreed taxonomy in
> `08_CORE_Profile.enums.expediente_types` **before** creating any expediente.

#### 4.3.1 Expediente directory naming (v03, authoritative)

Every expediente is a **directory** placed inside one of the numbered theme folders. Its name is:

```
yymmdd_SubjectInPascalCase_V01
```

- **`yymmdd`** — the expediente's **opening date** (year, month, day, two digits each).
- **`SubjectInPascalCase`** — the subject with **each word's first letter uppercased**, no spaces, no
  accents, no hyphens/underscores inside the subject.
  *e.g.* the subject "solicita librar mañana" becomes `SolicitaLibrarManana`.
- **`_V01`** — a two-digit **version suffix**. Bump to `_V02`, `_V03`… if, some time later, a **new**
  expediente arises on a **similar/related subject**, so similar subjects are versioned instead of
  colliding.

**Full example:** `260701_SolicitudLibrarManana_V01`

> This v03 rule **replaces** the earlier `yymmdd_ShortName/` wording used in v02/v03 drafts.

#### 4.3.2 The `_expediente.html` cover and artefacts

- **Cover — `_expediente.html`:** metadata `id`, `type`, `estado`, `ambito`, `timeline`.
- **State (`estado`)** advances **`OPEN → IN_PROGRESS → WAITING → RESOLVED → CLOSED`** (or **`REJECTED`**).
  The state machine itself is *defined* in `33_HOW_Processes`.
- **State is metadata on the cover — do not encode it in the folder name and do not move the folder.**
  Archiving is a state flag (`CLOSED`), not a move (law R4).
- **Artefacts inside:** `yymmdd_KIND_Detail.ext` — e.g. `260602_OFERTA_Integra.pdf`.
- Canonical business content is written/updated in its W home (P1); the expediente holds **facets**
  (supplier→`46`, cost→`72`, system→`13`, location→`51`), not copies. Closing an expediente **emits a
  line** to `12_STATUS_Daily`.

This single bucket absorbs everything the old v01 model spread across request/triage/pipeline/
coordination/drafts/promotion/processed flows.

### 4.4 `10_STATUS` — Now + periodic rollups (the "is/was")

STATUS records what happened and what is currently true. Each sub-bucket has its own mutability regime.

| Bucket | Regime | File | Example |
|--------|--------|------|---------|
| `11_STATUS_Now` | **mutable** — live state; open incidents live here | single `Now.html` | `Now.html` |
| `12_STATUS_Daily` | **append-only, sealed on close** — canonical dated-fact log | `yymmdd_STATUS_Daily.html` | `260701_STATUS_Daily.html` |
| `13_STATUS_Weekly` | append-only, sealed on close | `yyWww_STATUS_Weekly.html` (ISO week) | `26W27_STATUS_Weekly.html` |
| `14_STATUS_Monthly` | append-only, sealed on close | `yymm_STATUS_Monthly.html` | `2607_STATUS_Monthly.html` |
| `15_STATUS_Yearly` | append-only, sealed on close | `yyyy_STATUS_Yearly.html` | `2026_STATUS_Yearly.html` |

`12_STATUS_Daily` is the **canonical dated log**; it consolidates upward into Weekly → Monthly → Yearly,
each rollup linking its sources with `[Source: …]` and pointing at the finer-grained rollups it
summarises. Reserved buckets `16–19` re-home former v01 functions on demand (16≈Archive-as-flag,
17≈Audit-folded-into-rollups; evidence is sealed in place, PII stays in `43_WHO_People/_restricted`, live
health is part of `11_STATUS_Now`).

### 4.5 `_OUTPUT` — heavy deliverables

`_OUTPUT` holds **heavy, self-contained generated deliverables** (PDF and base64-embedded HTML), organised
by date/type (default `yymmdd_<Type>_<slug>.(pdf|html)`, configurable in `08_CORE_Profile.output.naming`).
It lives in OPERATIONS because it is operational/generated, not permanent infrastructure. If a deliverable
is evidence, a **stub + pointer** is left in `03_WORK_Flow`.

---

## 5. The hard laws P1–P8 and the operating principles

### 5.1 The laws (the constitution)

| Law | Name | What it enforces |
|-----|------|------------------|
| **P1** | **Canonical home + facets** *(the mother law)* | One home per item (single-writer); other dimensions are **read-only pointer facets** in frontmatter. **No content is duplicated across buckets — cross-links are pointers.** |
| **P2** | **Two sinks** | `00_CORE` = rules/catalogues · `10_STATUS` = facts/evidence. Every datum eventually drains into one or the other; nothing sits in limbo. |
| **P3** | **WHEN = should, STATUS = is/was** | `60_WHEN` holds plans/cadences; `10_STATUS` holds what happened. A plan **does not move** when its date passes — it **emits** a fact to STATUS and remains in WHEN. |
| **P4** | **Immutability per subdirectory** | `11_STATUS_Now` mutable · `12/13/14/15_STATUS` append-only & sealed on close · sealed evidence is WORM in place · archiving is a state flag (R4). |
| **P5** | **One CODE_CATALOG** | A single 4-letter code catalogue in `05_CORE_Glossary`. WHAT/WHERE are **projections** of it, not parallel sources. |
| **P6** | **Migration = indirection** | Moving something uses `PATH_ALIASES` in `06_CORE_Control`, **never** by rewriting sealed evidence. IDs are stable, not derived from the path. |
| **P7** | **Generated dual index** | `index.html` (human) + `index.json` (machine) are **both generated**, never hand-edited. A gate fails if the committed index ≠ the regenerated one. |
| **P8** | **Twins as a facet** | PHYS/OPER/ORG/META is retired as a structural axis; kept only as the optional `twin:` frontmatter facet. |

**Master rule (dominates the regime): Entity ≠ Work ≠ Event.** Every long-lived entity keeps its master
identity record in its thematic zone (one home, even with live state); its **tasks** → WORK; its
**events/state/evidence** → STATUS; stitched by `id` / `correlation_id`. The WORK/STATUS regime does not
apply to the master record. A closure set of 16 rules (R1–R16) resolves all-pairs conflicts (e.g. R3
sensitivity is an access facet not a home; R4 archive is a state; R6 decision = rationale in `28` + dated
fact in `12_STATUS_Daily`; R7 document-by-lifecycle; R10 memory ≠ data lake).

### 5.2 The operating principles

- **Roles, not persons.** All publishable content speaks by **role**; real people (PII) live only in
  `43_WHO_People/_restricted`, gated and excluded from RAG.
- **Human-in-the-loop.** No publication and no action on systems is executed without human review.
- **Advise-only over control systems (hard boundary).** The AI is *advise-only* over the organisation's
  control systems — it never writes to them. Those systems are declared in `08_CORE_Profile.boundaries`.
- **SEAL / WORM evidence in place.** Decisive artefacts are sealed **in place** (`immutable: true`,
  `sealed_from: <path>@<git-sha>`): the Inbox original, the artefact inside its expediente, the sent
  message in `02_WORK_Outbox/5_SENT`, a closed rollup. Once sealed they are WORM — never rewritten; later
  changes are modelled with a new fact/alias (P6), never by editing the seal.
- **RAG-EXIT (what enters the retrieval corpus).** Corpus = `status: approved` **AND NOT** `superseded`.
  **Always excluded:** `43_WHO_People` (PII), anything `sensitivity: restricted`, `ARCHIVED`/superseded
  items, and `11_STATUS_Now` (mutable). Operating detail in `06_CORE_Control/rag_manifest.yaml`.
- **Redaction (GDPR / anonymisation).** Before any output to a public cloud, PII is redacted and people
  are replaced by roles.
- **Single-writer (coarse-lock).** Each canonical home has one owner-role that may rewrite its *Compiled
  Truth*; the whole home is locked while a writer works. `03_WORK_Flow` teams are the multi-writer
  exception, with **claim-then-lock**.
- **Promotion is a handshake.** Work is promoted from an expediente to the shared shelf by declaring a
  `target:` home → human review → on approval it lands in its W home and the event is chronicled in
  `12_STATUS_Daily`.
- **Intake fan-out.** Everything entering `01_WORK_Inbox` is classified at intake and routed; a raw item
  is never discarded — low confidence → quarantine (flagged), not deletion.

---

## 6. Page anatomy & format policy

### 6.1 Page anatomy

Every memory `.md`/HTML page has **frontmatter** + two sections:

```
---
id: <ConceptOrCode>
home: shared/<bucket>/<id>            # canonical path (P1)
owner: role:<role>                     # a ROLE, never a person
status: draft|approved|superseded
sensitivity: public|internal|pii|restricted
twin: PHYS|OPER|ORG|META               # optional facet (P8)
# W facets (read-only pointers, as applicable):
what:  13_WHAT_SystemTree/<CODE>
where: 51_WHERE_LocationTree/<CODE>
who:   role:<role>
when:  65_WHEN_Milestones/<id>
howmuch: 72_HOWMUCH_Procurement/<file-id>
correlation_id: yymmdd-NN
sources: [shared/B_OPERATIONS/03_WORK_Flow/...]
---
## Compiled Truth   (rewritable ONLY by the owner; the curated current state)
...
---
## Timeline         (append-only; each line ends with [Source: <path>])
- <date>  ...  [Source: shared/B_OPERATIONS/03_WORK_Flow/...]
```

- **Compiled Truth** — the *current* curated state; rewritten **only by the home's owner**.
- **Timeline** — **append-only**; each line cites its source with `[Source: <path>]`.
- **W facets** — read-only pointers that declare the item's other faces without copying content.

**Immutable pages** (a sealed Inbox original, a sealed expediente artefact, a closed rollup) have **no
Compiled Truth** — they are only *captured* — and add `immutable: true` + `sealed_from: <path>@<git-sha>`.

**Node types.** Canonical page (W families, owner-rewritable) · Expediente (cover holds state, advances
OPEN..CLOSED) · Fact/rollup (STATUS, append-only, sealed on close) · Evidence (WORM in place) · Now/incident
(`11_STATUS_Now`, mutable until closed) · README (prose) · Config (YAML).

### 6.2 Format policy (cross-cutting)

| Where | Format | Images |
|-------|--------|--------|
| **Working dirs** (A_REFERENCE + B_OPERATIONS) | **Lightweight HTML** | **Referenced** → point to `C_OPERATIONAL_KIT/_RESOURCES/`; never embedded |
| **`C_OPERATIONAL_KIT/_SKILLS/`** | **Markdown (.md)** | — |
| **`B_OPERATIONS/_OUTPUT/`** (deliverables) | **Heavy**: PDF and **embedded HTML** | **Embedded (base64)** → self-contained for sending (chat/email) |

Work stays light and navigable (one logo set in `_RESOURCES`, referenced by pointer); only when you must
**deliver/send** do you generate heavy, self-contained copies in `_OUTPUT` using the `_TOOLS`.

---

## 7. The information flow (raw → sealed)

The master data lifecycle, in five steps:

```
Step 1  A message ARRIVES        → 01_WORK_Inbox : one IMMUTABLE file
        (any channel)              yymmdd_hhmmss_CHANNEL_SenderId_Subject.html  (never discarded)
             │
Step 2  CLASSIFY at intake       → router_rules.yaml decides the request type; a correlation_id is minted;
        (an action, not a folder)  routed to a theme in 03_WORK_Flow (new or existing expediente).
             │                     Low confidence → stays in Inbox, flagged for human triage.
             ▼
Step 3  WORK in the expediente   → 03_WORK_Flow/NN_Theme/yymmdd_SubjectInPascalCase_V01/
                                     gather artefacts; advance _expediente.html state OPEN→…→CLOSED;
                                     write canonical content in its W home (P1); expediente keeps FACETS.
             │
Step 4  SEAL in place            → immutable:true + sealed_from:<path>@<sha> on the Inbox original,
        + emit outgoing            the decisive expediente artefact, and any sent message
                                     (02_WORK_Outbox 1_PROPOSED→…→5_SENT + heavy copy in _OUTPUT).
             │                     Nothing is rewritten.
             ▼
Step 5  EMIT the fact to STATUS  → on close, a line → 12_STATUS_Daily (canonical dated log)
        + PROMOTE knowledge        → consolidated into 13_Weekly → 14_Monthly → 15_Yearly;
                                     11_STATUS_Now reflects only what is still live.
                                     If it produced shared knowledge → PROMOTION HANDSHAKE (human review,
                                     declaring target: home) → A_REFERENCE → index regenerated (P7).
```

**Invariant:** at no step is content duplicated between buckets — each hop leaves **pointers** (facets,
`correlation_id`, sources). The received message is never lost; sealed evidence is never rewritten.

**Worked example (a purchase, from the conflict-closure rules):** the request arrives in `01_WORK_Inbox` →
an expediente opens in `03_WORK_Flow/15_Purchases/260701_…_V01/` → the master purchase file (amount,
status) is the canonical home `72_HOWMUCH_Procurement`, with facets to supplier (`46`), procedure (`32`) →
the invoice is sealed inside the expediente → on close a fact is emitted to `12_STATUS_Daily`.

---

## 8. The operating kit (C_OPERATIONAL_KIT) & the agent mirror

C_OPERATIONAL_KIT is permanent infrastructure that serves the two content chambers but is **not** 5W2H
content (it is a separate N1 branch that precedes thematic classification).

```
C_OPERATIONAL_KIT/
├── _SKILLS/       (Markdown)  how to operate everything + default skills + onboarding
│     README.md · START_HERE-equivalent · CONFIG_QUESTIONS.md · skill_use_structure.md ·
│     skill_generate_your_skills.md · skill_official_documents.md
├── _RESOURCES/    logos / images / brand assets (REFERENCED from work, never embedded)
├── _TOOLS/        (Python) production utilities
│     embed_images.py · html2pdf.py · md2pdf.py · gen_index.py · README.md
└── _SERVICES/     the capability registry: skills & MCP servers agents can call
      services.yaml (machine registry, ships EMPTY) · _SERVICE_TEMPLATE.md · example_* cards
```

- **`_SKILLS/` (Markdown)** — how to operate the structure: the default skills and onboarding. Generic and
  **adaptable** per organisation (ask the particularities with `CONFIG_QUESTIONS.md`, then specialise).
- **`_RESOURCES/`** — logos/images/brand assets. **Referenced** from working documents, not embedded; only
  `_OUTPUT` embeds them (base64) for self-contained delivery.
- **`_TOOLS/` (Python)** — the canonical home of production scripts. Check here **before writing a new
  one**:
  - `embed_images.py` — referenced images → embedded base64.
  - `html2pdf.py` — self-contained HTML → PDF.
  - `md2pdf.py` — Markdown → PDF.
  - `gen_index.py` — regenerate each chamber's `index.html` + `index.json` (P7).
- **`_SERVICES/`** — the **capability registry**: one card per available **skill** or **MCP server** an
  agent can call, plus the machine registry `services.yaml`. It describes *what can be called and how* (an
  `mcp` service often *implements* a `36_HOW_Integrations` business integration). It ships **empty** (only
  illustrative example cards); real services are registered on configuration. Secrets are never stored
  here — only which auth is required.

**Production pipeline (work → deliverable):**

```
working doc (lightweight HTML, logo referenced in _RESOURCES)
    │  _TOOLS/embed_images.py     (referenced → embedded base64)
    ▼
self-contained HTML  ──  _TOOLS/html2pdf.py  ──►  PDF
    │
    ▼
B_OPERATIONS/_OUTPUT/  (organised by date/type — the final heavy deliverable)
    │
    └─ if it is evidence → stub + pointer in 03_WORK_Flow
```

### 8.1 The agent mirror model

An example agent's **private mirror** lives in `agents/agent01/` (copy it and rename it to your agent id).
**Each agent mirrors all three chambers at its own scale — including its own `C_OPERATIONAL_KIT/`**: it
inherits the shared kit and extends it with its own skills/tools/resources/services. The structure is
**scale-invariant**: the shared shelf and every agent mirror obey the same laws and the same folder model,
so `agent01/A_REFERENCE`, `agent01/B_OPERATIONS`, `agent01/C_OPERATIONAL_KIT` are identical in shape to the
shared ones.

---

## 9. Configuration & customisation lifecycle

The template ships **unconfigured on purpose**. The golden rule is: **do not assume the particularities —
ask them.** The lifecycle is **interview → profile → project → specialise**:

1. **Interview.** Ask the organisation's particularities with
   `C_OPERATIONAL_KIT/_SKILLS/CONFIG_QUESTIONS.md` — name, logos, colours, how logos sit on official
   documents, output formats, channels, language, roles, naming/codes, and — critically — which **areas,
   departments, committees, standing groups and recurring expediente types** they actually handle and how
   to group them.
2. **Profile.** Write the answers into the **instance profile**
   `A_REFERENCE/08_CORE_Profile/<org_id>.yaml` (start from `_PROFILE_TEMPLATE.yaml`). **This is the only
   place that changes when adapting the template to a different organisation.**
3. **Project.** Project the consequences of the profile onto the control-plane and the working folders
   (enums, router rules, ownership).
4. **Specialise.** Generate the organisation's own skills from the defaults, following
   `skill_generate_your_skills.md`, and register real capabilities in `_SERVICES/services.yaml`.

> **Strong note — you must tailor `03_WORK_Flow`.** The 27 default themes are a broad default for an
> observatory operator. If you are an AI agent doing the initial configuration, **do not accept them
> blindly**: ask the managers which themes they need and how to band them, leave the `03_WORK_Flow` area
> well-organised, and record the agreed taxonomy in `08_CORE_Profile.enums.expediente_types` **before
> creating any expediente**.

---

## 10. Reproducible build & versioning

### 10.1 Reproducible build (UTF-8, no BOM)

```
1)  python build_template_v03.py
       copies v02 ROOT/, rebuilds 03_WORK_Flow (shared + agent mirror) with the numbered themes,
       patches references that named old type folders (profile enums, router_rules.yaml, FLOW.md,
       ClassificationCriteria.md, NAMING.md), bumps version strings, and regenerates _TREE.txt.

2)  python build_template_v04.py
       copies v03 ROOT/, rewrites the agent prototype README, adds 00_CORE/AGENT_CONSOLIDATION.md,
       appends the agents: profile block, notes it in GOVERNANCE and the shared STATUS README,
       bumps version strings to V04, regenerates _TREE.txt.

3)  python ROOT/shared/C_OPERATIONAL_KIT/_TOOLS/gen_index.py
       regenerates each chamber's index.html + index.json  (law P7).
```

The build is reproducible and idempotent; each `DESIGN_v0N.md` documents that version's change (v03 =
theme placement and the v02→v03 mapping; v04 = the agent mirror + consolidation model).

### 10.2 Versioning (the model's evolution)

| Version | Shape of the runtime |
|---------|----------------------|
| **v01** | **Flat** work model (separate request / triage / pipeline / coordination / drafts / promotion / processed flows). |
| **v02** | Runtime consolidated into **Inbox / Outbox / Flow** + **periodic STATUS** (Now + Daily/Weekly/Monthly/Yearly). Introduced the P1–P8 laws, page anatomy, seal-in-place, and NAMING per bucket. |
| **v03** | Same three chambers and laws as v02; **changes only the contents of `03_WORK_Flow`**: expediente types reorganised into a **numbered thematic taxonomy** (banded by tens digit) with nine themes added, and the authoritative expediente-directory naming `yymmdd_SubjectInPascalCase_V01`. |
| **v04** | Same three chambers and laws as v03; adds the **per-agent private mirror** `agents/<id>/` (prototype `agent01`, replicated and particularised per agent's functions) and the **periodic consolidation** of each agent's STATUS rollup into the shared STATUS (summary + pointer, P1, human-in-the-loop, on a cadence configured in `08_CORE_Profile.agents.consolidation`). Also carries the corrected license/attribution (real repository, harness-independent). |

Each version is built on the previous one and inherits everything it does not change verbatim: v03 on v02
(only `03_WORK_Flow`), v04 on v03 (adds the agent mirror + consolidation). The v02 folder documents the
B_OPERATIONS redesign that first introduced Inbox/Outbox/Flow + periodic STATUS.

---

## 11. License & attribution

- **License:** MIT — see `ROOT/LICENSE`. Copyright (c) 2026 Axel Yanes Díaz / CEFCA (Centro de Estudios de
  Física del Cosmos de Aragón) — OPTIMIA project.
- **Repository:** <https://github.com/AxelCEFCA/OPTIMIA> — the OPTIMIA memory structure, **independent of
  any agent harness or runtime**. Link this repository when you reuse the architecture.
- **Citation:** if you use this template, cite **CEFCA's SPIE 2026 (Copenhagen)** OPTIMIA papers (lead:
  A. Yanes-Díaz, AS113) and the repository above.
- **Full attribution & citation detail:** see `00_CORE/LICENSE_AND_ATTRIBUTION.md`.

---

*Document generated for the Generic 5W2H Memory Template V04 · OPTIMIA / CEFCA · 2026. It synthesises the
canonical sources under `ROOT/shared/` and must stay consistent with them; on any discrepancy, the
`00_CORE` files (`SCHEMA.md`, `GOVERNANCE.md`, `RULES.md`, `ClassificationCriteria.md`, `NAMING.md`,
`FLOW.md`) and the `03_WORK_Flow/README.md` prevail.*
