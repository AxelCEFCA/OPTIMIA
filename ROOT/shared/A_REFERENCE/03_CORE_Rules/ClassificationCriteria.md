---
id: ClassificationCriteria
home: shared/A_REFERENCE/03_CORE_Rules/ClassificationCriteria
owner: role:leadership
status: approved
sensitivity: internal
twin: META
---
## Compiled Truth — Classification criteria for the 100 folders

Rules to identify **unambiguously** which folder each piece of information goes to.

### Routing algorithm (apply in order; the first that fits decides the zone)
0. **Raw, unprocessed file?** → `01_WORK_Inbox` (the flow then distributes it; see `09_CORE_Flow`).
1. **A rule/META of the memory system itself?** → `0X CORE`.
2. **Does it happen/change, or is it work in progress?** → `0X WORK`.
3. **A consummated fact / current state / evidence?** → `1X STATUS`.
4. **Descriptive knowledge?** pick the W by the question: what→`1X` · why→`2X` · how→`3X` · who→`4X` ·
   where→`5X` · when(plan)→`6X` · how-much→`7X`.
5. Within the zone, the units digit = the criterion of each folder (below).

**Golden rule:** a datum has **one canonical home** (single-writer) + **N read-only facets** in its
frontmatter. If torn between a descriptive W and WORK/STATUS: **if it has an occurrence date or changes
state → WORK/STATUS** (the W only receives a facet).

### 0X CORE — rules of the memory system
- **00_CORE** — constitution and index of rules · NO business content.
- **01_CORE_Schema** — formal model (buckets, signatures, page anatomy) · the grammar, vs 03 (usage).
- **02_CORE_Templates** — memory-PAGE moulds (ADR, record, ticket) · vs 38 (business output).
- **03_CORE_Rules** — how to fill/place (this document), naming, append-only · vs 04 (authority), 06 (config).
- **04_CORE_Governance** — laws in prose (P1, SEAL, RAG-EXIT, REDACTION, promotion) · vs 06 (executable).
- **05_CORE_Glossary** — glossary + single CODE_CATALOG (4 letters, facet what|where) · vs 15 (business).
- **06_CORE_Control** — ownership/router/rag/aliases yaml · vs 04 (prose).
- **07_CORE_Index** — spec/generator of index.html+index.json · NOT the generated index.
- **08_CORE_Profile** — swappable instance profile (the only thing that changes between organisations).
- **09_CORE_Flow** — definition of the raw→processed flow · vs WORK (where it happens).

### 1X WHAT — definition (what it is), static and timeless
- **10_WHAT** — entry + rules 11–19.
- **11_WHAT_Root** — what the entity is · vs 21 (why it exists).
- **12_WHAT_OrgStructure** — org chart as a model · vs 42 (real units).
- **13_WHAT_SystemTree** — tree of systems, identity · vs 51 (where), 11_STATUS_Now/12_STATUS_Daily (state/lifecycle).
- **14_WHAT_DataModel** — entity schema (a "request", a domain object) · vs 15 (values), NOT instances.
- **15_WHAT_Catalogs** — closed business taxonomies (request types, trackers, channels) · vs 05.
- **16_WHAT_Services** — services/products delivered · vs 13/17 (what produces them).
- **17_WHAT_Assets** — asset/instrument classes · vs 13 (functional), 76 (how many), 51 (where).
- **18_WHAT_Standards** — specs that define · vs 32 (procedure), 35 (binding reference).
- **19_WHAT_Reserved** — reserved.

### 2X WHY — purpose/justification (timeless); the dated fact → 12_STATUS_Daily
- **20_WHY** — entry + rules 21–29.
- **21_WHY_Purpose** — ultimate reason for being · vs 22/23.
- **22_WHY_Mission** — what we do (permanent) · vs 26 (time-bound goals).
- **23_WHY_Vision** — undated aspirational future · vs 67 (phased plan).
- **24_WHY_Values** — values/beliefs · vs 25 (operating conduct).
- **25_WHY_Principles** — guiding principles (respect, roles-not-persons, HITL, control-systems boundary) · vs 03/37.
- **26_WHY_Objectives** — qualitative objectives/OKR · vs 75 (KPI), 65 (milestone).
- **27_WHY_ValueProposition** — value proposition + why stakeholders matter · vs 48 (the entity).
- **28_WHY_Decisions** — rationale/ADR (the why) · vs 12_STATUS_Daily (the dated fact). Linked, not duplicated (P1).
- **29_WHY_Impact** — positive impact pursued · vs 26 (goals), 77 (risk).

### 3X HOW — operation (how), timeless; execution → WORK
- **30_HOW** — entry + rules 31–39.
- **31_HOW_Playbooks** — full end-to-end scenario · vs 32 (atomic task).
- **32_HOW_Procedures** — step-by-step SOP · vs 33, 64.
- **33_HOW_Processes** — state machines (request, QUEUE→DONE definition) · vs WORK (instances).
- **34_HOW_Methods** — methodologies (Kanban WIP, service classes) · vs 31.
- **35_HOW_KnowledgeBase** — model cards, binding regulations, FAQs/RAG · vs 18 (spec), 32 (actionable).
- **36_HOW_Integrations** — how to connect (connectors, gateway, anonymisation) · vs 49, 53.
- **37_HOW_Policies** — operating policies (RBAC, requires_confirmation, anonymisation) · vs 25, 04.
- **38_HOW_Templates** — output moulds (email, report, minutes) · vs 02 (memory pages).
- **39_HOW_Automations** — what the router/scheduled jobs do · vs 06 (config), 49 (entity).

### 4X WHO — entities; abstract structure → 12, why it matters → 27
- **40_WHO** — entry + rules 41–49.
- **41_WHO_Roles** — roles/responsibilities (RACI) · vs 43 (person), 12 (structure).
- **42_WHO_Org** — units/departments · vs 44 (cross-cutting team), 12 (model).
- **43_WHO_People** — real people, PII (identity_map), RESTRICTED no-RAG · NO PII outside here.
- **44_WHO_Teams** — teams/groups · vs 42.
- **45_WHO_Partners** — collaborations · vs 46 (supplier), 48 (interested party).
- **46_WHO_Suppliers** — commercial suppliers · vs 72 (the file).
- **47_WHO_Contacts** — mailing/distribution lists · vs 43 (person), 61 (when).
- **48_WHO_Stakeholders** — stakeholder register (entity) · vs 27 (why they matter).
- **49_WHO_Agents** — AI agents as entities (_router, _scheduler, named agents) · vs 39 (what they do).

### 5X WHERE — location/context; the system there → 13
- **50_WHERE** — entry + rules 51–59.
- **51_WHERE_LocationTree** — physical locations (building prefix) · vs 13 (what), 52 (macro site).
- **52_WHERE_Sites** — sites/campuses · vs 51 (detail).
- **53_WHERE_Compute** — compute environments (cloud/on-prem/HPC) · vs 17 (asset), 51 (building).
- **54_WHERE_Networks** — network topology/segments · vs 53 (nodes), 11_STATUS_Now/03_WORK_Flow (network state).
- **55_WHERE_Field** — office vs field as context · vs WORK (the work), 62 (when).
- **56_WHERE_Zones** — security/access/TLP zones · vs 37 (the policy).
- **57_WHERE_External** — third-party premises · vs 45/46 (the entity).
- **58/59_WHERE_Reserved** — reserved.

### 6X WHEN — planning/future (the "should"); if it passed → STATUS. Plans emit facts, they do not move
- **60_WHEN** — entry + rule P3 + rules 61–69.
- **61_WHEN_Calendar** — planned hourly events (CalDAV) · vs 12_STATUS_Daily (what was held), 63 (recurrence).
- **62_WHEN_Schedule** — planned person×day grid / shifts · vs 74 (effort), STATUS (reported).
- **63_WHEN_Cadences** — recurring rhythms (weekly cycle, day/night) · vs 61 (instance).
- **64_WHEN_OnCall** — planned on-call · vs 32 (algorithm), 12_STATUS_Daily (already served).
- **65_WHEN_Milestones** — future milestones/deadlines (stops, tenders) · vs 26 (goal), 67 (phases).
- **66_WHEN_Triggers** — future triggers/conditions · vs 39 (what fires).
- **67_WHEN_Roadmap** — phases MVP/Phase2/Future · vs 23 (undated aspiration).
- **68/69_WHEN_Reserved** — reserved.

### 7X HOWMUCH — cost/effort/magnitude (the quantitative face of any topic)
- **70_HOWMUCH** — entry + rules 71–79.
- **71_HOWMUCH_Budget** — budgets/planned (RAG budget, compute) · vs 73 (actual).
- **72_HOWMUCH_Procurement** — master purchase file (amount/status) · vs 46/32/03_WORK_Flow.
- **73_HOWMUCH_Costs** — actual costs/estimates · vs 72/71.
- **74_HOWMUCH_Effort** — effort/capacity, plan-vs-reported hours · vs 62 (when).
- **75_HOWMUCH_Metrics** — KPIs/sizing · vs 11_STATUS_Now (health), 26 (objective).
- **76_HOWMUCH_Resources** — quantities (licenses, quotas) · vs 17 (class), 53 (where).
- **77_HOWMUCH_Risks** — risk = severity×likelihood · vs 29 (positive impact), 11_STATUS_Now (if it materialises).
- **78/79_HOWMUCH_Reserved** — reserved.

### 0X WORK — live work in transit (mutable, stateful); on completion emits a fact to STATUS (v02)
- **00_WORK** — entry + rules 01_WORK_Inbox–09_WORK_Reserved. **01/02 = the I/O pair** (in/out); **03 = the expediente flow**.
- **01_WORK_Inbox** — ALL received messages, every channel, one **immutable** file each (`yymmdd_hhmmss_CHANNEL_SenderId_Subject.html`). Classification/triage happens here (an action, not a folder): the message is routed to an expediente in 03_WORK_Flow. Low confidence → stays here flagged, never deleted. **Symmetric to 02_WORK_Outbox.**
- **02_WORK_Outbox** — ALL outgoing messages, human approval (state=subfolder: 1_PROPOSED→2_EDITING→3_APPROVED→5_SENT, or 4_DISCARDED). On SEND a heavy copy goes to _OUTPUT; the sent file stays as the record. **Symmetric to 01_WORK_Inbox.**
- **03_WORK_Flow** — the **expediente flow**: one subfolder per expediente **type**, numbered by theme band (e.g. `15_Purchases`, `36_Incidents`, `31_Projects`; admin in `10`-`19`), and inside each, one folder per expediente (a case file with all its artefacts). The expediente **state** (OPEN→IN_PROGRESS→WAITING→RESOLVED→CLOSED, or REJECTED) lives in its `_expediente.html` cover · vs 33_HOW_Processes (the state-machine definition). This one bucket absorbs the v01 request/triage/pipeline/coordination/drafts/promotion/processed flow.
- **04_WORK_Reserved … 09_WORK_Reserved** — reserved (freed by the expediente-flow consolidation).

### 1X STATUS — now + periodic rollups (is/was); regime per folder (v02)
- **10_STATUS** — entry + per-folder regime + rules 11_STATUS_Now–19_STATUS_Reserved.
- **11_STATUS_Now** {mutable} — live state, updated by the day's events; open incidents live here (rolling `Now.html`) · vs 13 (identity), 12_STATUS_Daily (dated).
- **12_STATUS_Daily** {append-only, sealed on close} — the end-of-day rollup and the **canonical dated-fact log** (`yymmdd_STATUS_Daily.html`) · vs 28 (rationale).
- **13_STATUS_Weekly / 14_STATUS_Monthly / 15_STATUS_Yearly** {append-only, sealed on close} — the week/month/year rollups that consolidate the most relevant of each period.
- **16_STATUS_Reserved … 19_STATUS_Reserved** — reserved. They hold the **re-homed** v01 functions, activatable on config: 16≈Archive (now a state flag, R4), 17≈Audit (folded into rollups + 06_CORE_Control), plus Evidence/Restricted/Health — evidence is sealed in place, PII lives in 43_WHO_People/_restricted, live health is part of 11_STATUS_Now.

### Overlaps and conflicts (recommended resolution + motivation)
- **C1 Decision** → dated fact in 12_STATUS_Daily + rationale in 28 (no duplication). *A consummated fact goes to STATUS; the argument is timeless.*
- **C2 Incident** → one id: live in 11_STATUS_Now, worked as an expediente in 03_WORK_Flow/36_Incidents (sealed artefacts + post-mortem in place), fact emitted to 12_STATUS_Daily. *The lifecycle defines the home; stitched by correlation_id.*
- **C3 Risk** → 77 as a magnitude; if it materialises, an incident in 11_STATUS_Now. *Risk = severity×likelihood → HOWMUCH.*
- **C4 Stakeholder** → entity in 48; value relationship in 27. *P1: one entity, one home (WHO).*
- **C5 Compliance** → split: framework 00/25, control 37/32, evidence 03_WORK_Flow, tag `compliance:`. *Not a W; cross-cutting.*
- **C6 Purchase** → master file 72; supplier 46, procedure 32, invoice sealed in the expediente 03_WORK_Flow/15_Purchases, fact in 12_STATUS_Daily. *The file is cost; the invoice is a result.*
- **C7 Model card** → 35 by default (cost→73/75). *Consulted as operating knowledge.*
- **C8 Meeting** → planned 61/63; when held it emits minutes 03_WORK_Flow + event 12_STATUS_Daily. *Plans do not move; they emit facts.*
- **C9 Calendar vs schedule** → hours 61 (CalDAV); shifts 62. *Different granularity/source.*
- **C10 System** → identity 13 (+pointer to 12_STATUS_Daily), state 11_STATUS_Now, lifecycle 12_STATUS_Daily, location facet 51. *One home + facets; single Timeline in 12_STATUS_Daily.*
- **C11 Person/role/contact** → role 41 (shared), person 43 (gated), lists 47. *Roles-not-persons + anti-PII.*
- **C12 Asset** → class 17, system 13, quantity 76, where 51. *Each question, its zone.*
- **C13 Template** → memory page 02; business artefact 38. *Different consumers.*
- **C14 Glossary/codes vs catalogues** → system 05 (single); business 15. *The 4-letter namespace is not split (P5).*
- **C15 Multi-zone raw** → always 01_WORK_Inbox first; after processing it fans out to W + seals to 03_WORK_Flow. *A single flow (09).*

### Conflict closure (after all-pairs adversarial review)

**MASTER RULE — ENTITY ≠ WORK ≠ EVENT (dominates the regime):** every long-lived entity has its
**master identity record** in its **thematic zone** (single home, even with live state); its **tasks** →
WORK; its **events/state/evidence** → STATUS; linked by id/correlation_id. The WORK/STATUS regime does
NOT apply to the master record.

**Revised tree (total and disjoint):** N0 raw→01_WORK_Inbox. N1 (5 exclusive branches): memory-rule→0X ·
bulk-data→OUT (data lake) · work-artefact→WORK · event/state/evidence/document→STATUS ·
master-record/knowledge→N2. N2: identity (actor→WHO / thing→WHAT) or modifier (HOWMUCH>WHEN>WHERE>HOW>WHY).

**16 closure rules:**
- R1 Entity≠Work (overrides the regime). R2 One home+facets (no copying).
- R3 **sensitivity = access facet, NOT a home** (43_WHO_People/_restricted = only the physically isolated PII/raw-evidence store).
- R4 **archive = state** (16_STATUS_Reserved does not break the home; the entity stays with a flag; a tombstone resolves the id).
- R5 **numbers/series → HOWMUCH (75)**; the STATUS regime is for documents/events; 11_STATUS_Now/03_WORK_Flow are views.
- R6 **decision: rationale→28, dated fact→12_STATUS_Daily** (pointer, no duplication).
- R7 **document by lifecycle** (draft 03_WORK_Flow→sealed 03_WORK_Flow→retention 16_STATUS_Reserved); minutes/invoice/contract/post-mortem = master in 03_WORK_Flow.
- R8 **type succession** (does not mutate zone; a successor is born with supersedes/derived_from). R9 versioning = one home + history.
- R10 **memory ≠ data lake** (telemetry/observations OUT; only a snapshot 11_STATUS_Now + def 75 + pointer 53/36).
- R11 **0X vs 3X** (0X=the memory; 3X=the operation; an on-call algorithm→39/32, not 03).
- R12 **actor vs thing (AI)**: acts→49, passive→17, service→16, card→35.
- R13 **regulatory continuum**: memory→0X · axiom→25 · external-defines→18 · to-consult→35 · internal-operates→37 · steps→32.
- R14 **project** → charter in 11_WHAT_Root + project_id threads the facets.
- R15 **assignment/relation** = facet on the more stable side or an event in 12_STATUS_Daily.
- R16 **02 vs 38**: memory pages (02) vs business artefacts (38).

**Guarantee:** the 5 N1 branches are mutually exclusive and the intra-zone discriminators disjoint → every
(entity, piece) has EXACTLY one canonical home; everything else is a facet. Scale-invariant (shared and
agent mirror, identical).

### Operating kit and format policy

Besides the 100 5W2H content folders, the memory has a **third chamber**, `C_OPERATIONAL_KIT/` — the
**operating kit** (production & onboarding infrastructure that serves the other two) — and the generated
**output** in `B_OPERATIONS/_OUTPUT`. These are NOT 5W2H content: they are another N1 branch (like CORE
or "bulk data"), and **precede** thematic classification.

- **`C_OPERATIONAL_KIT/_SKILLS/`** (Markdown) — how to operate the structure: default skills + onboarding
  (`START_HERE.md`). Generic and **adaptable** per organisation (ask the particularities with
  `CONFIG_QUESTIONS.md` → write into `08_CORE_Profile`).
- **`C_OPERATIONAL_KIT/_RESOURCES/`** — logos/images/assets; **referenced** from the work, not embedded.
- **`C_OPERATIONAL_KIT/_TOOLS/`** — utilities (Python): `embed_images`, `html2pdf`, `md2pdf`, `gen_index`… (the
  canonical home of production scripts; check before writing a new one; detailed reference + software
  architecture in its README).
- **`C_OPERATIONAL_KIT/_SERVICES/`** — the **capability registry**: one card per available **skill** or **MCP
  server** the agents can call, plus a machine registry `services.yaml`. Describes *what can be called and
  how*; an `mcp` service often implements a `36_HOW_Integrations` business integration.
- **`B_OPERATIONS/_OUTPUT/`** — **heavy** generated deliverables (PDF, embedded HTML); generated, not
  source. It lives in OPERATIONS because it is operational/generated (not permanent infrastructure).

**Kit/output routing:** asset (logo/image) → `C_OPERATIONAL_KIT/_RESOURCES`? · tool →
`C_OPERATIONAL_KIT/_TOOLS`? · skill/instruction → `C_OPERATIONAL_KIT/_SKILLS`? · callable capability
(skill/MCP) → `C_OPERATIONAL_KIT/_SERVICES`? · heavy generated output → `B_OPERATIONS/_OUTPUT`?

**Format policy (cross-cutting):**
- **Working dirs** (A_REFERENCE + B_OPERATIONS) → **lightweight HTML** with images **referenced** to
  `C_OPERATIONAL_KIT/_RESOURCES` (never embedded).
- **`C_OPERATIONAL_KIT/_SKILLS/`** → **Markdown**.
- **`B_OPERATIONS/_OUTPUT/`** → **heavy**: PDF and **embedded HTML** (base64, self-contained for chat/email).
- **Pipeline:** work (referenced) —`embed_images`→ self-contained —`html2pdf`→ PDF →
  `B_OPERATIONS/_OUTPUT`; if it is evidence, leave a **stub+pointer** in `03_WORK_Flow`.

**Reference note:** because numbering is independent per chamber, zones are named by their **full name**
(`03_WORK_Flow`, `12_STATUS_Daily`), not by number alone: the number repeats across chambers
(`12_WHAT_OrgStructure` in A vs `12_STATUS_Daily` in B).

---
## Timeline
- <date>  Classification criteria for the 100 folders established (canonical home 03_CORE_Rules).  [Source: shared/A_REFERENCE/01_CORE_Schema/SCHEMA.md]
