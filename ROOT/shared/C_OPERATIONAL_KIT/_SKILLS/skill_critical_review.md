# Default skill · Critically review the memory for coherence

**Goal:** run a skeptical, adversarial QA / red-team pass over the memory (or over a new addition to it)
and prove whether it is **coherent** and **consistent** with the prior/known project information — before
that content is promoted to the shared shelf. You are not here to be helpful to the author; you are here
to **try to break** their claims.

> **Stance:** assume the new content is wrong until it survives scrutiny. **Nothing is "approved" until
> every issue you raise is either resolved or explicitly accepted by a human** (human-in-the-loop, per
> [`../../A_REFERENCE/04_CORE_Governance/GOVERNANCE.md`](../../A_REFERENCE/04_CORE_Governance/GOVERNANCE.md)).
> A clean pass is a *finding of no issues*, not a rubber stamp.

## 1. Purpose & when to run

Run this skill:

- **Before promotion** — as the QA gate on the promotion handshake. An agent proposes content for a
  canonical W home from an expediente in `B_OPERATIONS/03_WORK_Flow`; this review runs *before* the human
  reviewer signs off (see the *Promotion* section of `04_CORE_Governance`).
- **After a batch** — once a run of intake/classification has drained `B_OPERATIONS/01_WORK_Inbox` into
  expedientes and produced STATUS rollups, audit the batch for drift.
- **On demand** — whenever someone doubts a page, or when two pages seem to disagree.

The review **advises only**. It never rewrites the pages it audits and never approves its own findings; it
hands a findings list to a human, exactly as with any publication (human-in-the-loop).

## 2. What it checks (the adversarial checklist)

Work through every item and actively try to find a violation. Cite evidence (file + line/section) for each.

1. **Contradictions between pages** — the same fact stated two ways (a role's owner, a date, a code's
   meaning, a state). Compare the new/target page against every page that touches the same entity.
2. **Duplication that violates P1** — content **copied** into a second home instead of living once in its
   **canonical home** with read-only **facets/pointers** elsewhere. Copied prose, duplicated tables, a
   binary stored twice instead of a stub+pointer. (Law P1, `04_CORE_Governance`.)
3. **Dangling facets/links** — a facet or `[Source:]` pointer that names a canonical home, expediente or
   `_OUTPUT` blob that **does not exist** (or was renamed without a `PATH_ALIASES` entry in
   [`../../A_REFERENCE/06_CORE_Control/PATH_ALIASES.yaml`](../../A_REFERENCE/06_CORE_Control/PATH_ALIASES.yaml)).
4. **Stale / superseded info not archived** — a page presented as current that a later fact overrides,
   without the `superseded`/`ARCHIVED` state flag. Superseded-but-live content silently pollutes the
   RAG-EXIT corpus.
5. **Roles-not-persons violations & stray PII** — a real person named in open text instead of a role, or
   PII anywhere outside the restricted lane
   [`../../A_REFERENCE/43_WHO_People/_restricted`](../../A_REFERENCE/43_WHO_People/_restricted/). Any leak
   here is a hard stop.
6. **Glossary / code consistency** — a term used in a sense that conflicts with
   [`../../A_REFERENCE/05_CORE_Glossary/GLOSSARY.md`](../../A_REFERENCE/05_CORE_Glossary/GLOSSARY.md); a
   4-letter code used, redefined or duplicated in a way that conflicts with the single
   [`../../A_REFERENCE/05_CORE_Glossary/CODE_CATALOG.md`](../../A_REFERENCE/05_CORE_Glossary/CODE_CATALOG.md)
   (one code, one meaning, one `facet: what|where` — law P5).
7. **Naming-convention adherence** — check against
   [`../../A_REFERENCE/03_CORE_Rules/NAMING.md`](../../A_REFERENCE/03_CORE_Rules/NAMING.md):
   Inbox files `yymmdd_hhmmss_CHANNEL_SenderId_Subject.html` (and immutable once written); expediente
   folders `yymmdd_SubjectInPascalCase_V01` with an `_expediente.html` cover and artefacts
   `yymmdd_KIND_Detail.ext`; STATUS rollups named per bucket. State must be **metadata on the cover**, never
   encoded in the folder name.
8. **Consistency with the instance profile** — every organisation-specific claim (channel, role, code,
   expediente theme, tone, boundary) must match
   [`../../A_REFERENCE/08_CORE_Profile`](../../A_REFERENCE/08_CORE_Profile/): e.g. a channel not in
   `enums.channels`, a `03_WORK_Flow` theme not in `enums.expediente_types`, a writer other than the home's
   owner in `06_CORE_Control/ownership.yaml`.
9. **Consistency with prior known facts** — the new addition must not contradict what the memory already
   established. Treat the existing approved content and the user's auto-memory as the baseline.
10. **Skill conflicts** — a new or edited skill that **contradicts**, **redundantly restates** or
    **quietly overrides** an existing one in this `_SKILLS/` folder. Two skills claiming the same folder
    with different rules is a finding.

## 3. How to run it (be adversarial)

1. **Scope** the review: the target page(s) or the batch under audit, plus every page that shares an
   entity, code or theme with it.
2. **Read the evidence, not the summary.** Open the actual files. For sealed evidence (immutable Inbox
   originals, sealed expediente artefacts, closed rollups) confirm nothing has been edited in place — WORM
   is honoured by pointing, never by rewriting.
3. **Compare against the authorities**, in this order:
   - the laws and processes in
     [`../../A_REFERENCE/04_CORE_Governance`](../../A_REFERENCE/04_CORE_Governance/) (P1–P8, SEAL,
     RAG-EXIT, REDACTION, promotion);
   - the placement/writing rules in
     [`../../A_REFERENCE/03_CORE_Rules`](../../A_REFERENCE/03_CORE_Rules/) (`RULES.md`, `NAMING.md`,
     `ClassificationCriteria.md`);
   - the vocabulary and codes in
     [`../../A_REFERENCE/05_CORE_Glossary`](../../A_REFERENCE/05_CORE_Glossary/);
   - the instance specifics in
     [`../../A_REFERENCE/08_CORE_Profile`](../../A_REFERENCE/08_CORE_Profile/);
   - the ownership/routing config in
     [`../../A_REFERENCE/06_CORE_Control`](../../A_REFERENCE/06_CORE_Control/) (`ownership.yaml`,
     `router_rules.yaml`, `rag_manifest.yaml`).
4. **Try to falsify each claim.** Ask: *where would this be wrong?* Chase every pointer to its target.
   Look for the second copy. Look for the older fact that this one silently replaces. Look for the person
   hiding behind a supposedly generic sentence. A claim that survives an honest attempt to break it is the
   only kind you may pass.
5. **Do not fix in place.** This skill produces findings; remediation is a separate, owner-driven edit
   under the single-writer rule.

## 4. Output — a critical findings list

Produce a **findings list**, one row per issue, ranked most-severe first:

| Field | Content |
|-------|---------|
| **Issue** | One sentence: what is inconsistent/incoherent. |
| **Severity** | `BLOCKER` (PII leak, P1 duplication, contradiction of an approved fact, dangling canonical link) · `MAJOR` (stale-not-archived, naming/profile violation, code clash) · `MINOR` (glossary drift, cosmetic). |
| **Evidence** | The exact `file` + line/section on each side of the inconsistency. |
| **Suggested fix** | The smallest change that resolves it (add a facet instead of a copy; archive the superseded page; move the name to the restricted lane; register a `PATH_ALIAS`…). |

Then:

- **Flag every unresolved inconsistency for human review.** The content stays **out of the shared shelf**
  and out of the RAG-EXIT corpus until each finding is resolved or a human **explicitly accepts** it
  (recording the acceptance). No self-approval.
- **Optionally render the report.** Draft it as lightweight HTML (or Markdown) with images referenced from
  `_RESOURCES/`, and — if it is delivered as evidence of the audit — file it as an expediente artefact under
  the relevant `03_WORK_Flow` theme with the usual `_expediente.html` cover, per
  [`skill_official_documents.md`](skill_official_documents.md). Do not embed the findings twice: the
  canonical report is the artefact; STATUS carries a `[Source:]` pointer to it.

## See also

- [`../../A_REFERENCE/04_CORE_Governance`](../../A_REFERENCE/04_CORE_Governance/) — the laws P1–P8,
  SEAL/WORM, RAG-EXIT, REDACTION, promotion, human-in-the-loop (the rules you audit against).
- [`../../A_REFERENCE/03_CORE_Rules`](../../A_REFERENCE/03_CORE_Rules/) — placement and writing conventions,
  `NAMING.md`, `ClassificationCriteria.md`.
- [`../../A_REFERENCE/05_CORE_Glossary`](../../A_REFERENCE/05_CORE_Glossary/) — `GLOSSARY.md` and the single
  `CODE_CATALOG.md`.
- [`../../A_REFERENCE/08_CORE_Profile`](../../A_REFERENCE/08_CORE_Profile/) — the instance profile every
  organisation-specific claim must match.

> Run over the **whole** memory, this is the audit that produces the project's audit report: a systematic,
> skeptical sweep of every home against the laws, the glossary, the profile and the prior known facts —
> reproducible on demand whenever coherence needs to be re-established.
