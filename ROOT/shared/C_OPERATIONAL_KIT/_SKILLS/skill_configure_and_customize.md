# Default skill · Configure and customise a fresh deployment

**Goal:** turn a freshly copied **Generic 5W2H Memory Template V03** into a memory configured for **one
real organisation** — its entity, branding, documents, channels, roles, codes and, above all, its
**03_WORK_Flow themes** — without breaking the fixed spine.

> This is the skill you run **once**, at deployment time, before anyone starts operating. When you finish,
> the memory is no longer "generic": it knows who it belongs to. Everything specific lands in the
> **instance profile** (`08_CORE_Profile`); the 100-folder spine stays untouched.

## 0. The FIRST rule: interview, do not assume

**Do NOT accept the defaults blindly.** The template ships with sensible defaults (channels, expediente
types, states, roles) so it *runs*, but those defaults describe a generic observatory-style entity, not
**this** organisation. Before you generate, rename or delete anything:

1. **Interview the organisation's managers** with
   [`CONFIG_QUESTIONS.md`](CONFIG_QUESTIONS.md), blocks **A–H**. Ask in blocks, not all at once: A–B–C
   first (what you need to produce the first official document), D–H when they are needed.
2. **Assume nothing** — the logo, colours, naming, output formats, channels, roles, codes and language
   all change from one organisation to another.
3. **Especially tailor the `03_WORK_Flow` themes** (block G) to the organisation's **real** areas,
   departments, committees, standing groups and case-types. Do not keep a theme the organisation does not
   have, and do not force its work into a theme that does not fit.
4. Write every answer straight into the profile. If a person is named, it goes to the restricted lane
   (`43_WHO_People/_restricted`) — **never inline**, only the role stays in the open text.

If an answer is missing, **ask for it**; do not invent it — leave the `<PLACEHOLDER>` and flag it.

## 1. Configure the profile (`08_CORE_Profile`)

Copy the template and fill it in — this is the **only** file that distinguishes this organisation from
any other:

```
A_REFERENCE/08_CORE_Profile/_PROFILE_TEMPLATE.yaml   →   08_CORE_Profile/<org_id>.yaml
```

Replace every `<PLACEHOLDER>` and **leave the `spine:` block untouched**. Fill, block by block, from the
interview:

| Block | Profile keys | From CONFIG |
|-------|--------------|-------------|
| Entity | `profile.id/name/short/type/language/description/date_today` | A |
| Branding | `branding.logos/placement/colors/typefaces` | B |
| Documents | `documents.types/tone` | C |
| Output | `output.formats/naming/organize_by` | D |
| Channels & integrations | `channels`, `integrations` (which system is *authoritative* for which datum) | E |
| Roles, governance, privacy, boundaries | `roles`, `governance.promotion_approver`, `privacy`, `boundaries.never_write` | F |
| Domain codes & enums | `domain_codes.what/where`, `enums.*` | G |
| Cadence | `cadence` | H |

Two `enums` fields carry the taxonomy decisions and deserve care:
- `enums.channels` — the intake catalogue for Inbox/Outbox (default
  `EMAIL WHATSAPP TELEGRAM PHONE VIDEOCONF INPERSON`; rename/extend).
- **`enums.expediente_types`** — the agreed **03_WORK_Flow** taxonomy (see §3). This is where the
  organisation's real themes are recorded, as the single source of truth for the flow folders.

## 2. Project the profile onto the structure

The profile is the source; a few places are its **projections**. After filling the profile, materialise:

- **Roles** → `40_WHO/41_WHO_Roles` (one card per role, **by role never by person**) and the ownership map
  in `06_CORE_Control/ownership.yaml` (who owns/approves each home).
- **Closed catalogues** (request types, states, channels, on-call/shift labels) → `10_WHAT/15_WHAT_Catalogs`,
  mirroring the profile `enums`.
- **Codes** (4-letter `what`/`where` namespace) → project into
  `05_CORE_Glossary/CODE_CATALOG.md` (which codes are systems, which are locations).
- **Logos** → drop the real files into `C_OPERATIONAL_KIT/_RESOURCES/logos/` and record their placement
  (which, order, position, size, co-branding) in `branding.placement`.

**Do not duplicate:** these projections point back to the profile; the profile stays authoritative.

## 3. Customise `03_WORK_Flow` (the theme taxonomy)

`B_OPERATIONS/03_WORK_Flow` holds the expedientes, one **numbered thematic folder** per theme. The
tens digit is a **band**, so related things stay adjacent — keep the bands:

| Band | Meaning |
|------|---------|
| `00–09` | general / cross-cutting |
| `10–19` | administration · governance · compliance |
| `20–29` | scientific |
| `30–39` | engineering & technical |
| `40–49` | outreach & external |

The 27 default themes (e.g. `10_Governance`, `14_ContractsAndTenders`, `15_Purchases`,
`20_ScientificArea`, `31_Projects`, `36_Incidents`, `41_EventsAndOutreach`) are a **starting point**.
Now adapt them to the real organisation:

- **Add** a theme the organisation has and the defaults miss (give it the next free number in its band).
- **Remove** a theme the organisation does not have.
- **Rename** a theme to the organisation's own wording (keep PascalCase, no spaces/accents).
- **Renumber** within the band so numbers stay ordered and meaningful.

Whatever you agree, **keep it inside the right band** and **record the final list** in
`08_CORE_Profile.enums.expediente_types`. The folders under `03_WORK_Flow` and that enum must match.

## 4. Specialise the skills

The default skills are generic on purpose. Once the profile is filled:

1. **Specialise** `skill_use_structure.md` and `skill_official_documents.md`, making them concrete with
   the profile data (the real logos and their placement, the real document types, the real tone).
2. **Add one skill per real workflow.** For each recurring flow the organisation named in block G
   (procurement, incidents, weekly planning, observing programs…), write a skill anchored to the real
   `NN_Theme/` folder it uses. See [`skill_generate_your_skills.md`](skill_generate_your_skills.md).
3. **Save** shared skills here in `_SKILLS/`; save an agent's own skills under its mirror
   `agents/<id>/C_OPERATIONAL_KIT/_SKILLS/`.

## 5. Expediente naming convention (state it, enforce it)

Every expediente is a **directory** placed inside one of the numbered thematic folders `NN_Theme/` under
`B_OPERATIONS/03_WORK_Flow`. The directory name format is:

```
yymmdd_SubjectInPascalCase_V01
```

- **`yymmdd`** — the expediente **opening date** (year, month, day, two digits each).
- **`SubjectInPascalCase`** — the subject with **each word's first letter uppercased**, no spaces, no
  accents, no hyphens/underscores inside the subject. E.g. the subject *"solicita librar mañana"* becomes
  `SolicitaLibrarManana`.
- **`_V01`** — a two-digit **version** suffix. Bump to `_V02`, `_V03`… when, some time later, a **new**
  expediente arises on a **similar/related** subject, so similar subjects are **versioned** instead of
  colliding.

**Full example:** `260701_SolicitudLibrarManana_V01`.

Inside the expediente directory:
- a cover page **`_expediente.html`** — metadata `id, type, estado (OPEN..CLOSED/REJECTED), ambito,
  timeline`;
- the artefacts, named `yymmdd_KIND_Detail.ext` (e.g. `260602_OFERTA_Integra.pdf`).

State is **metadata on the cover**, not in the folder name — do not move or rename the folder to encode
state. The authoritative rule lives in
[`../../A_REFERENCE/03_CORE_Rules/NAMING.md`](../../A_REFERENCE/03_CORE_Rules/NAMING.md); point every
operator there.

## 6. Finish checklist — what "configured" means

You are done when you have produced (mirrors the closing section of `CONFIG_QUESTIONS.md`):

1. A **filled `08_CORE_Profile`** — no `<PLACEHOLDER>` left that the organisation actually uses.
2. The real **logos in `_RESOURCES/logos/`** and their placement recorded in the profile.
3. The **closed catalogues** (request types, states, channels…) declared in `15_WHAT_Catalogs` and the
   profile `enums`.
4. The **roles** in `41_WHO_Roles` and the **ownership** map in `06_CORE_Control/ownership.yaml`.
5. The **`03_WORK_Flow` themes** adapted within their bands and matching
   `08_CORE_Profile.enums.expediente_types`.
6. **Specialised skills** (from `skill_generate_your_skills.md`) for this organisation's real flows.

If you have all six, the memory is configured and you can start operating. If any input is missing,
**ask for it** — do not invent it; leave the field as `<PLACEHOLDER>` and flag it.

## Hard laws to honour throughout

- **P1 — one canonical home** + read-only facets (pointers). No duplication: link, don't copy.
- **Roles, not persons** (except the restricted lane `43_WHO_People`).
- **Human-in-the-loop:** nothing leaves the Outbox without human approval.
- **Generated indexes (P7):** rebuild with `_TOOLS/gen_index.py`; don't hand-edit indexes.
- **SEAL/WORM evidence in place:** rollups and sent items are sealed once closed.
- **RAG-EXIT:** only approved, not-superseded, PII-excluded content is exportable.
