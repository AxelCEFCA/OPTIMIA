# Default skill · Process a transcription (speech-to-text intake)

**Goal:** turn a raw **transcription** (speech-to-text, dictation, meeting notes) sitting in the Inbox
into a corrected, sensible processed page — repairing the errors the recogniser made against what the
project *knows*, and flagging what still cannot be reconciled so a human reviews it.

> This skill is a **specialisation of [`skill_process_raw_intake.md`](skill_process_raw_intake.md)**. A
> transcription is just one kind of raw intake, so it follows all the ordinary intake steps and **adds one
> extra pass**: a **CORRECTION pass** that leans on project knowledge. Read the parent skill first; this
> page only describes the delta.

## 1. Inherit the raw-intake steps

Do everything [`skill_process_raw_intake.md`](skill_process_raw_intake.md) says, unchanged:

1. The original file is already in `B_OPERATIONS/01_WORK_Inbox`, named
   `yymmdd_hhmmss_CHANNEL_SenderId_Subject.html` — **immutable evidence, sealed in place**. Never edit it.
2. Classify it with `../../A_REFERENCE/06_CORE_Control/router_rules.yaml` and follow the flow in
   `../../A_REFERENCE/09_CORE_Flow/FLOW.md`.
3. Open or attach the matching **expediente** under `B_OPERATIONS/03_WORK_Flow/NN_Theme/`
   (`yymmdd_SubjectInPascalCase_V01`, `_expediente.html` cover + artefacts named `yymmdd_KIND_Detail.ext`,
   per `../../A_REFERENCE/03_CORE_Rules/NAMING.md`).
4. Write the **processed page**, keeping `[Source:]` pointed at the original Inbox transcription.

Then, **before** you consider the processed page final, run the correction pass below.

## 2. The CORRECTION pass — reconcile against project knowledge

Speech-to-text mangles exactly the words this project cares about most: acronyms, product/system names,
domain jargon, and people. Go through the transcription and, for **every uncertain term**, cross-check it:

1. **Against the project glossary** — `../../A_REFERENCE/05_CORE_Glossary/GLOSSARY.md` (canonical terms)
   and the 4-letter **`../../A_REFERENCE/05_CORE_Glossary/CODE_CATALOG.md`** (the code namespace).
2. **Against the section's known entities** — the related **W home** for the topic (e.g. a system in
   `10_WHAT`, a role in `40_WHO`, a place in `50_WHERE`) and the reference knowledge in
   `../../A_REFERENCE/35_HOW_KnowledgeBase`.

Apply the fix to the **canonical form**:

- **Garbled acronym → its catalogued code.** If the recogniser wrote a plausible-sounding but non-existent
  acronym, and a near-neighbour exists in `CODE_CATALOG.md`, correct it to that 4-letter code.
- **Mis-heard term → the known project term.** Replace a phonetic approximation with the glossary's
  canonical wording (e.g. an everyday word the ASR substituted for a piece of project jargon that *sounds*
  like it).
- **Homophones and names → disambiguate with context.** Use the surrounding topic and the section's known
  entities to pick the right member of a homophone pair. Where a **personal name** was transcribed, do not
  keep it: replace it with the **ROLE** (roles-not-persons), consistent with the glossary/`40_WHO`.

Only correct where project knowledge gives you a **confident** target. Do not "improve" wording that is
already fine, and do not guess a code that is not in the catalogue — an unresolved term is a FLAG (§4),
not a free invention.

## 3. Write the corrected, sensible processed page

The processed page should read as something that **makes sense given what the project knows** — canonical
terms, real codes, roles instead of names. Rules that still hold:

- **`[Source:]` stays on the original transcription.** The processed page is a corrected *reading* of that
  evidence; the pointer must remain to the raw Inbox file so the chain is auditable.
- **The original transcription stays immutable in `01_WORK_Inbox`.** You corrected the *derived* page, not
  the evidence. The raw errors remain visible in the sealed original — that is deliberate.
- Follow Law **P1**: one canonical home + read-only facets, no duplication. The corrected page lives with
  its expediente; it points to glossary/code entries, it does not copy them.

## 4. FLAG what cannot be reconciled

Anything that **still does not fit** the glossary, the code catalogue, or the section's known
entities after the correction pass is **not silently dropped** and **not force-fitted**. It is written
down for a human, verbatim enough that someone can act on it. Two complementary places:

- **In the processed page:** keep the uncertain span and mark the line **`[REVIEW]`**, with the original
  ASR text preserved (e.g. `... the [REVIEW: heard "acme-din", no matching code] system ...`) so the
  reviewer sees both what was heard and why it could not be resolved.
- **Next to the expediente:** drop a small **to-clarify / needs-review** stub artefact inside the
  expediente directory (a `yymmdd_REVIEW_Detail` note) listing each unresolved term, the raw transcription
  span, and your best guess if any. This is a **human-in-the-loop** hand-off: nothing derived from an
  unresolved term gets published until a human confirms it.

Never delete an unresolvable term to make the page look clean — an un-flagged omission is worse than a
visible `[REVIEW]`.

## 5. Iteration — revisit flags when the glossary grows

The glossary and code catalogue are living. When someone **extends** `05_CORE_Glossary` (a new canonical
term, a new 4-letter code) or `35_HOW_KnowledgeBase` gains an entity that was missing before,
**previously-flagged items can be resolved**:

1. Re-scan open `[REVIEW]` marks and `REVIEW` stubs for terms the new glossary entry now explains.
2. Correct the processed page (canonical form, role, or code) and clear the flag — again keeping
   `[Source:]` on the untouched original.
3. Leave a timeline line recording the reconciliation, so the correction is itself auditable.

This way early transcriptions improve automatically as project knowledge matures, without ever touching the
sealed evidence.

## See also
- `../../A_REFERENCE/05_CORE_Glossary/` — `GLOSSARY.md` (canonical terms) + `CODE_CATALOG.md` (4-letter
  codes); the authority you correct **to**.
- `../../A_REFERENCE/35_HOW_KnowledgeBase` — reference knowledge / known entities for
  disambiguation.
- [`skill_process_raw_intake.md`](skill_process_raw_intake.md) — the general intake skill this one
  specialises.
