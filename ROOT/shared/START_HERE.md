# START HERE — the first file an agent reads

> You are an agent (or a person) opening this memory for the **first time**. Read this whole file
> before touching anything. It tells you what this is, how it is used, and — above all — **what you
> must do first** to make it serve *your* organisation.

## 0. What this is in one line

This is a **blank, generic 5W2H memory template**. It is the same structure for any organisation; it
becomes *yours* only after you **configure it** by asking the questions in this kit and writing the
answers into the instance profile. Nothing here names a real organisation, person, system or vendor —
that is on purpose.

**Its job** is to give **you — an AI agent (or a person) — the whole organisation's context** (its
identity, roles, procedures, systems, locations, plans, costs and history) in one navigable place, so you
can act as an informed member of the organisation instead of guessing. Everything below is how that
context is organised, kept true, and handed to each agent.

> **Conceived for observatories, applicable to any organisation.** This template was originally designed
> for entities that **build and operate astrophysical observatories** (its default `03_WORK_Flow` themes
> reflect that world). But **it is perfectly applicable to any kind of organisation**: the 5W2H spine, the
> laws and the operating model are domain-agnostic, and the default configuration is **deliberately open
> and general** — a starting point you re-label, prune and extend during configuration (§2). A hospital, a
> factory, an NGO or a software team can adopt it just as well; only the profile and the `03_WORK_Flow`
> themes change.

## 1. The shape: three chambers

```
shared/
├── index.html                 ← navigable landing page (start here to LOOK)
├── START_HERE.md              ← this file
│
├── A_REFERENCE/               ← [CONTENT] the permanent MODEL (00–79). You CONSULT it. Lightweight HTML.
│     00_CORE · 10_WHAT · 20_WHY · 30_HOW · 40_WHO · 50_WHERE · 60_WHEN · 70_HOWMUCH
├── B_OPERATIONS/              ← [CONTENT] the NOW (00–19). You WORK in it. Lightweight HTML.
│     0X_WORK (01_Inbox · 02_Outbox · 03_Flow=expedientes) · 1X_STATUS (Now + Daily/Weekly/Monthly/Yearly) · _OUTPUT/
└── C_OPERATIONAL_KIT/         ← [INFRASTRUCTURE] how you operate & produce. Permanent.
      _SKILLS/      (Markdown) how to operate everything + default skills + onboarding, adaptable.
      _RESOURCES/   logos / images / brand assets (REFERENCED, not embedded).
      _TOOLS/       utilities (Python): embed images, HTML→PDF, MD→PDF, regenerate the index…
      _SERVICES/    the capability registry: which skills & MCP servers are available, and how to call each.
```

- **A_REFERENCE** = the descriptive model (what / why / how / who / where / when-plan / how-much).
  Curated, slow-changing, the stable retrieval corpus. Numbered **00–79** (8 families).
- **B_OPERATIONS** = the runtime. **WORK** (`0X`): `01_WORK_Inbox` (all incoming messages, every channel), `02_WORK_Outbox` (all outgoing, human-approved), `03_WORK_Flow` (the **expediente** flow, one subfolder per expediente type), `04`-`09` reserved. **STATUS** (`1X`): `11_STATUS_Now` (live) + `12`-`15` Daily/Weekly/Monthly/Yearly rollups, `16`-`19` reserved. File-naming per bucket is in `A_REFERENCE/03_CORE_Rules/NAMING.md`.
- **C_OPERATIONAL_KIT** = the operating kit (skills, resources, tools). Permanent infrastructure.
- An example agent's private mirror lives in `agents/agent01/` (copy it, rename it to your agent id). Each
  agent mirrors all three chambers at its scale — **including its own `C_OPERATIONAL_KIT/`** (it inherits the
  shared kit and extends it with its own skills/tools/resources/services).

## 2. The FIRST thing you must do (do not skip)

Because this is a **generic template**, it is *unconfigured*. Before you generate anything:

1. **Ask the organisation's particularities.** The questionnaire is
   [`C_OPERATIONAL_KIT/_SKILLS/CONFIG_QUESTIONS.md`](C_OPERATIONAL_KIT/_SKILLS/CONFIG_QUESTIONS.md)
   (name, logos, colours, how logos sit on official documents, output formats, channels, language,
   roles, naming/codes…).
2. **Write the answers into the instance profile**
   [`A_REFERENCE/08_CORE_Profile`](A_REFERENCE/08_CORE_Profile/) — the **only** place that changes when
   you adapt the template to a different organisation. Start from
   [`_PROFILE_TEMPLATE.yaml`](A_REFERENCE/08_CORE_Profile/_PROFILE_TEMPLATE.yaml).
3. **Generate your own skills** from the defaults, following
   [`C_OPERATIONAL_KIT/_SKILLS/skill_generate_your_skills.md`](C_OPERATIONAL_KIT/_SKILLS/skill_generate_your_skills.md).

> Golden rule: **do not assume the particularities — ask them.** What ships here is an adaptable
> skeleton, not your organisation's final configuration.

## 3. The reading order (so this template is self-sufficient)

If you read these files in order, you have everything you need to configure the memory and start working:

1. **`START_HERE.md`** (this file) — the map and the first task.
2. **`C_OPERATIONAL_KIT/_SKILLS/README.md`** — what the default skills are.
3. **`C_OPERATIONAL_KIT/_SKILLS/skill_use_structure.md`** — how to find/place any piece of information.
4. **`C_OPERATIONAL_KIT/_SKILLS/CONFIG_QUESTIONS.md`** — the questions to ask the organisation.
5. **`A_REFERENCE/08_CORE_Profile/_PROFILE_TEMPLATE.yaml`** — where the answers go.
6. **`C_OPERATIONAL_KIT/_SKILLS/skill_generate_your_skills.md`** — how to specialise the skills.
7. **`C_OPERATIONAL_KIT/_SKILLS/skill_official_documents.md`** — how to produce official documents.
8. **`A_REFERENCE/03_CORE_Rules/ClassificationCriteria.md`** — the full routing rules (reference); **`NAMING.md`** — the file-naming convention for each B_OPERATIONS bucket.
9. **`A_REFERENCE/04_CORE_Governance/GOVERNANCE.md`** — the hard laws (P1–P8, SEAL, RAG, redaction).
10. **`A_REFERENCE/09_CORE_Flow/FLOW.md`** — the raw→sealed information flow.

## 4. How to find / place anything (the short version)

- **To look** → [`index.html`](index.html) (three doors: REFERENCE, OPERATIONS, KIT) and each chamber's
  index (`A_REFERENCE/index.html`, `B_OPERATIONS/index.html`, `C_OPERATIONAL_KIT/index.html`).
- **To classify (where does this go?)** → the routing algorithm in
  [`A_REFERENCE/03_CORE_Rules`](A_REFERENCE/03_CORE_Rules/). In one breath: a **raw** file → `B_OPERATIONS/01_WORK_Inbox`;
  a **memory rule** → `A_REFERENCE/00_CORE`; something that **happens/is worked** → `B_OPERATIONS`
  (WORK/STATUS); **descriptive knowledge** → the right W in `A_REFERENCE`; an **asset/tool/skill** →
  `C_OPERATIONAL_KIT`; a **heavy generated deliverable** → `B_OPERATIONS/_OUTPUT`.
- **Golden rule of placement:** each thing has **one canonical home** (single-writer) + **N read-only
  facets** (pointers) in its frontmatter. Never copy across buckets; link.

## 5. Format policy (cross-cutting — important)

| Where | Format | Images |
|-------|--------|--------|
| **Working dirs** (A_REFERENCE + B_OPERATIONS) | **lightweight HTML** | **referenced** (point to `C_OPERATIONAL_KIT/_RESOURCES/`), never embedded |
| **`C_OPERATIONAL_KIT/_SKILLS/`** | **Markdown (.md)** | — |
| **`B_OPERATIONS/_OUTPUT/`** (deliverables) | **heavy**: PDF and **embedded HTML** | **embedded** (base64) → self-contained for sending (chat/email) |

**Why:** work stays light and navigable (referenced images, one logo set in `_RESOURCES`); only when you
must **deliver/send** do you generate heavy self-contained copies in `B_OPERATIONS/_OUTPUT`, using the
tools in `C_OPERATIONAL_KIT/_TOOLS`.

## 6. The production pipeline (work → deliverable)

```
working document (lightweight HTML, logo referenced in C_OPERATIONAL_KIT/_RESOURCES)
        │  _TOOLS/embed_images.py   (referenced → embedded base64)
        ▼
self-contained HTML  ──  _TOOLS/html2pdf.py  ──►  PDF
        │
        ▼
B_OPERATIONS/_OUTPUT/  (organised by date/type: the final, heavy deliverable)
        │
        └─ if it is evidence → stub + pointer in B_OPERATIONS/03_WORK_Flow
```

> Tool detail: [`C_OPERATIONAL_KIT/_TOOLS/README.md`](C_OPERATIONAL_KIT/_TOOLS/README.md) ·
> assets: [`C_OPERATIONAL_KIT/_RESOURCES/README.md`](C_OPERATIONAL_KIT/_RESOURCES/README.md) ·
> output: [`B_OPERATIONS/_OUTPUT/README.md`](B_OPERATIONS/_OUTPUT/README.md).
