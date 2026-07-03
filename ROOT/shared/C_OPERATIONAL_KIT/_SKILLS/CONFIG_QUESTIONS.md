# CONFIG · Particularities to ask, to adapt the template

This is the **first** thing an agent must ask when deploying the structure in an organisation. Every
answer maps to a field in the instance profile `A_REFERENCE/08_CORE_Profile/_PROFILE_TEMPLATE.yaml`.
Until this is done, the template is **unconfigured**.

> How to use it: ask in **blocks**, not all at once. Start with A–B–C (what you need to produce the first
> official document) and leave D–H for when they are needed. For every answer, write it into the profile
> and, if it is sensitive (people), into the restricted lane — never inline.

---

## A · Entity identity → `profile.entity`
- Official name and short name / acronym.
- Type of organisation (this defines the "profile": company, observatory, hospital, NGO, agency, lab…).
- Working language(s) and the language of official documents.
- A one-line description of what the organisation does (feeds `11_WHAT_Root` and `22_WHY_Mission`).

## B · Visual identity → `_RESOURCES/logos` + `profile.branding`
- Which **logos** exist (entity, program, department, funders…). Formats (SVG/PNG) and variants
  (colour / mono / negative).
- **Placement on official documents:** which logos, in what order, in what position (header/footer),
  size, margins. Co-branding (several logos together)? Usage rules / clear space?
- Corporate colours and typefaces.

## C · Official documents → `38_HOW_Templates` + `profile.documents`
- Document types the entity produces (report, minutes, memo, record card, email, note…).
- Existing templates and their layout (header, institutional footer, numbering).
- Tone and register (form of address: formal/informal? singular/plural?).

## D · Formats & output → format policy + `B_OPERATIONS/_OUTPUT` + `profile.output`
- Usual delivery format: PDF? Embedded HTML for chat/email? Both?
- File-naming conventions for output and how to organise `_OUTPUT` (by date, by type…).

## E · Channels, tools & services → `_TOOLS`, `_SERVICES`, `36_HOW_Integrations` + `profile.integrations`, `profile.channels`
- Channels by which information enters/leaves (email, messaging, task manager…).
- External systems to integrate (project/work manager, procurement platform, calendar…) and which is
  **authoritative** for which datum.
- Existing in-house tools/scripts that should go into `_TOOLS`.
- **Available capabilities/services → `_SERVICES`:** which **MCP servers** the agents may use (task
  manager, calendar, file store, search, ticketing…) — with their tools, transport and required auth — and
  which **skills** the agents may call. Register one card per capability and list them in
  `_SERVICES/services.yaml` (declare which credential/scope each needs — never the secret itself).

## F · People, roles & governance → `40_WHO`, `profile.roles`, `profile.governance`, `profile.privacy`
- The organisation's roles (for `40_WHO`) — **by role, not by person**.
- Who approves what (write governance: what moves from OPERATIONS to REFERENCE by promotion).
- Personal-data / restricted-access policy (PII lives only in `43_WHO_People/_restricted`; sensitive operational items are tagged `sensitivity: restricted` in place).
- Any **control systems** the AI must never write to (advise-only boundary) → `profile.boundaries`.

## G · Naming & domain particularities → `05_CORE_Glossary` (CODE_CATALOG), `15_WHAT_Catalogs`, `profile.domain_codes`, `profile.enums`
- Own codes (systems, locations, projects), naming conventions, closed catalogues
  (request types, states, channels, on-call/shift labels).
- The 4-letter code namespace (if any): which codes are `what` (systems) and which are `where` (locations).
- The **intake channels** for `01_WORK_Inbox` (default `EMAIL WHATSAPP TELEGRAM PHONE VIDEOCONF INPERSON`) and the **expediente types** for `03_WORK_Flow` (default set in `_PROFILE_TEMPLATE.yaml`).
- The **expediente states** (default `OPEN..CLOSED/REJECTED`) and the **STATUS periods** (`Now/Daily/Weekly/Monthly/Yearly`). File-naming per bucket → `03_CORE_Rules/NAMING.md`.
- Any specific workflow that deserves its own skill.

## H · Cadence & time → `60_WHEN`, `profile.cadence`
- Recurring rhythms (daily/weekly/monthly cycles, day/night, planning day).
- On-call / shift model, if any (labels, rotation, fairness window).

---

## What you must have produced when you finish

By the end of this questionnaire you should have:

1. A **filled `08_CORE_Profile`** (no `<PLACEHOLDER>` left that the organisation actually uses).
2. The real **logos in `_RESOURCES/logos/`** and their placement recorded in the profile.
3. The **closed catalogues** (request types, states, channels…) declared in `15_WHAT_Catalogs` and the
   profile `enums`.
4. The **roles** in `41_WHO_Roles` and the **ownership** map in `06_CORE_Control/ownership.yaml`.
5. **Specialised skills** (from `skill_generate_your_skills.md`) for this organisation's real flows.

If you have all five, the memory is configured and you can start operating. If any input is missing,
**ask for it** — do not invent it; leave the field as `<PLACEHOLDER>` and flag it.
