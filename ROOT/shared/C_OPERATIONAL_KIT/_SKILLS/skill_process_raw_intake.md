# Default skill · Process a raw intake file

**Goal:** take one **raw incoming file** sitting in the Inbox and turn it into recorded, sourced,
correctly-placed knowledge — extract what it says, name and file the extraction in its canonical home, and
leave the origin file **sealed and untouched** as the evidence of record.

> This is the **general methodology** for any incoming RAW FILE, whatever its channel or subject. It is the
> concrete, per-file version of the 5-step lifecycle in
> [`../../A_REFERENCE/09_CORE_Flow/FLOW.md`](../../A_REFERENCE/09_CORE_Flow/FLOW.md). Follow it every time
> something lands in `01_WORK_Inbox`. When in doubt, do less to the original and flag for a human.

## 1. Receive — the raw file is already in the Inbox

The file arrives as **one immutable file** in
[`../../B_OPERATIONS/01_WORK_Inbox`](../../B_OPERATIONS/01_WORK_Inbox/), named per
[`../../A_REFERENCE/03_CORE_Rules/NAMING.md`](../../A_REFERENCE/03_CORE_Rules/NAMING.md):

```
yymmdd_hhmmss_CHANNEL_SenderId_Subject.html
```

- This name is the **address of the evidence**. It is **never rewritten and never deleted** (intake law).
- You do **not** create this file — capture puts it there. Your job starts with a file already present.
- If you must open it, open it **read-only**. Do not edit, re-save, re-encode, or "tidy" the original: any
  change breaks the seal. Treat it as WORM (write-once, read-many) from the first second.

## 2. Classify — what is this, and where does its case live?

Identify the **request type** and route it, using the rules in
[`../../A_REFERENCE/06_CORE_Control/router_rules.yaml`](../../A_REFERENCE/06_CORE_Control/router_rules.yaml)
(purchase, incident, meeting, document, …). Routing lands the work in one **numbered theme** under
[`../../B_OPERATIONS/03_WORK_Flow`](../../B_OPERATIONS/03_WORK_Flow/) (`NN_Theme`, banded):

- **New matter** → open a new expediente directory `yymmdd_SubjectInPascalCase_V01/` in the right theme,
  with an `_expediente.html` cover (`id, type, estado, ambito, timeline`).
- **Continuation of an existing matter** → append to the expediente that already exists (add artefacts,
  advance the cover's state); do not open a duplicate.
- A `correlation_id` (`yymmdd-NN`) is minted at intake and threaded through the expediente and its facts.
- **Low confidence?** Do **not** guess and do **not** delete. Leave the file **flagged in the Inbox** for
  human triage (`default_route: 01_WORK_Inbox`). A wrong route is worse than an un-routed file.

## 3. Extract — write a new lightweight page in its canonical home (P1)

Read the raw content and **transcribe its meaning into a NEW, lightweight page** — never copy the whole
blob into the memory. The extraction is a fresh working document, placed in its **one canonical home**:

- the **expediente** (an artefact / stub inside the `yymmdd_..._V01/` directory), and/or
- the correct **W-family home** for the underlying concept (what→`10_WHAT`, why→`20_WHY`, how→`30_HOW`,
  who→`40_WHO`, where→`50_WHERE`, when→`60_WHEN`, how-much→`70_HOWMUCH`) — reference knowledge in
  [`../../A_REFERENCE/35_HOW_KnowledgeBase`](../../A_REFERENCE/35_HOW_KnowledgeBase/).

Give the page the standard anatomy (see `02_CORE_Templates/TEMPLATE.md`):

- **frontmatter** — `id, home, owner (role:…), status, sensitivity`, plus a `sources:` pointer back to the
  Inbox file (and `correlation_id` when there is one);
- **Compiled Truth** — the current curated state, rewritable by the owner;
- **Timeline** — append-only; **every fact ends with `[Source: <the inbox file path>]`** so the origin is
  always traceable. If a person is named, the name goes only to the restricted lane
  `43_WHO_People/_restricted` — the open text keeps the **role**.

**P1 — one canonical home + read-only facets.** The concept is written **once** in its home; the expediente
and other dimensions hold **facets** (pointers), not copies (supplier→`46`, cost→`72`, system→`13`,
location→`51`).

## 4. Name the extracted file — per NAMING.md

Name what you just wrote by the bucket it lives in
([`../../A_REFERENCE/03_CORE_Rules/NAMING.md`](../../A_REFERENCE/03_CORE_Rules/NAMING.md)):

- **Inside an expediente** → an artefact `yymmdd_KIND_Detail.ext`, where `KIND` is an uppercase kind and
  `Detail` is CamelCase (e.g. `260701_ACTA_ReunionKickoff.html`, `260701_RESUMEN_SolicitudRenovacion.html`).
  The 4-letter/uppercase code vocabulary and the project glossary live in
  [`../../A_REFERENCE/05_CORE_Glossary`](../../A_REFERENCE/05_CORE_Glossary/) (`GLOSSARY.md` +
  `CODE_CATALOG.md`) — reuse an existing code, don't invent a new one.
- **In a W-home** → name the page by its **concept** (the full folder + `id` is the address), not by the
  incoming file's name. The extraction's identity is the *thing it is about*, not *how it arrived*.

## 5. Handle the ORIGIN after processing — move a pointer, keep the bytes

The origin file is the **sealed original (WORM)**: the primary evidence. Once you have extracted from it:

- **By default it STAYS in `01_WORK_Inbox`** as the record. It is **never rewritten and never deleted**.
- **Optionally, place a COPY inside the expediente** as its sealed artefact — an evidence stub with
  `immutable: true` and `sealed_from: <inbox path>` pointing at the original (see the evidence-stub mould in
  `02_CORE_Templates/TEMPLATE.md`). This co-locates the proof with the case without moving the record.
- **Mark it processed** — not by touching the bytes, but with a **facet / pointer** (a processed marker, the
  `correlation_id`, a link to the extraction). The extracted page points **back** to the origin via its
  `sources:`; the origin is pointed **forward** to its extraction.

> **Move vs copy — be precise.** You **copy** the origin only as a sealed artefact if the expediente needs
> the proof beside it. You **never move the original bytes** out of the Inbox and you **never edit** them.
> What "moves" is only a **pointer/marker** (processed-flag, facet, correlation link). Original bytes in;
> pointers out. When you are tempted to "move the file", you are really moving a reference — leave the
> evidence where it was sealed.

## 6. Emit + flag — close the loop

- **On close**, the expediente **emits a fact** into
  [`../../B_OPERATIONS/12_STATUS_Daily`](../../B_OPERATIONS/12_STATUS_Daily/) (append-only; the canonical
  dated log), advancing the cover's `estado`. That daily line is later consolidated up the rollups
  (`13_Weekly → 14_Monthly → 15_Yearly`); `11_STATUS_Now` reflects only what is still live.
- **Flag anything that does not fit** for human review: ambiguous routing, a datum with no obvious home, a
  conflict with existing Compiled Truth, PII, or anything destined to be **published**. Human-in-the-loop is
  mandatory for anything that leaves the memory — never auto-send, never auto-promote.

---

## Flow diagram

```
01_WORK_Inbox : yymmdd_hhmmss_CHANNEL_SenderId_Subject.html   (immutable, sealed original)
    │  read-only
    ▼
[2] classify  →  router_rules.yaml  →  03_WORK_Flow/NN_Theme/
    │                                      ├─ new  : yymmdd_SubjectInPascalCase_V01/ (+ _expediente.html)
    │                                      └─ append to existing expediente
    ▼
[3] extract   →  NEW lightweight page in canonical home (expediente and/or W-home, P1)
    │            frontmatter + Compiled Truth + Timeline; every fact [Source: <inbox path>]
    ▼
[4] name      →  yymmdd_KIND_Detail.ext (artefact)  |  concept-named page (W-home)
    ▼
[5] origin    →  STAYS in Inbox (record)  ·  optional sealed COPY in expediente (sealed_from)
    │            mark processed = move a POINTER, keep the bytes  ·  extraction sources: → origin
    ▼
[6] emit      →  fact into 12_STATUS_Daily (→ Weekly → Monthly → Yearly)  ·  flag misfits for a human
```

**Invariant:** the received file is never lost, never rewritten; nothing is duplicated between buckets —
each hop leaves **pointers** (facets, `correlation_id`, `sources:`).

## See also

- [`../../A_REFERENCE/09_CORE_Flow/FLOW.md`](../../A_REFERENCE/09_CORE_Flow/FLOW.md) — the master
  raw→sealed lifecycle this skill implements per file.
- [`../../A_REFERENCE/03_CORE_Rules/NAMING.md`](../../A_REFERENCE/03_CORE_Rules/NAMING.md) — the naming
  convention for every bucket (Inbox, expediente artefacts, W-home pages, STATUS rollups).
- [`../../A_REFERENCE/06_CORE_Control/router_rules.yaml`](../../A_REFERENCE/06_CORE_Control/router_rules.yaml)
  — the intake classification rules that decide the theme and facets.
- [`skill_process_transcriptions.md`](skill_process_transcriptions.md) — the specialisation of this
  methodology for **transcription** files (meeting/call/audio transcripts) as the raw origin.
