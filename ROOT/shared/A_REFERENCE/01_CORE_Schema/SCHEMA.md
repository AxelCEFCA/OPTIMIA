---
id: Schema
home: shared/A_REFERENCE/01_CORE_Schema
owner: role:leadership
status: approved
sensitivity: internal
twin: META
---

# 01_CORE_Schema — the model of the memory

> **What question does it answer?** *"How is each page and each bucket structured?"* It is the formal
> contract every `.md` page and every folder must satisfy.

## What goes here
- The definition of the **10 buckets** (the 5W2H spine).
- The **X0..X9 rule** (how derivatives are numbered inside each family).
- The **page anatomy** (frontmatter + Compiled Truth + Timeline).
- The optional **`twin`** facet and the **node types**.

## What does NOT go here
- The concrete fillable templates → `02_CORE_Templates`.
- The rules for *when* to use each bucket → `03_CORE_Rules`.
- The governance laws (P1–P8) → `04_CORE_Governance`.

---

## 1. The 10 buckets (5W2H spine)

```
00_CORE     (meta)        rules, schema, catalogues, governance, profile
10_WHAT     What?         definition (SystemTree)
20_WHY      Why?          purpose (the deep "why")
30_HOW      How?          operation (playbooks/procedures)
40_WHO      Who?          entities (roles/people/teams/partners/suppliers)
50_WHERE    Where?        location (LocationTree)
60_WHEN     When?         planning/future/cadence  (the "should")
70_HOWMUCH  How much?     cost/effort/magnitude
00_WORK     (work)        Inbox / Outbox / Flow (expedientes)   (the "in-progress")
10_STATUS   (status)      Now + Daily/Weekly/Monthly/Yearly rollups (the "is/was")
```

## 2. X0..X9 rule (derivative numbering)

Inside each family `NN0`, derivatives are numbered `NN1`..`NN9`:
- `NN0` = the family **base folder** (carries the rules for reading its derivatives).
- `NN1`..`NN8` = stable subcategories, with a fixed meaning declared in the profile.
- `NN9` = by convention **Reserved** (or the last subcategory); it never moves and carries a
  "RESERVED: what will go here" README.

Example: in `40_WHO`, `41_WHO_Roles`, `42_WHO_Org`, … `49_WHO_Agents`. `40_WHO/README.md` explains how
to read its derivatives.

## 3. Page anatomy

Every memory `.md` page has **frontmatter** + two sections:

```
---
id: <ConceptOrCode>
home: shared/<bucket>/<id>           # canonical path (P1)
owner: role:<role>                    # role, NEVER a person
status: draft|approved|superseded
sensitivity: public|internal|pii|restricted
twin: PHYS|OPER|ORG|META              # optional facet (P8)
# W FACETS (read-only pointers, as applicable):
what: 13_WHAT_SystemTree/<CODE>
where: 51_WHERE_LocationTree/<CODE>
who: role:<role>
when: 65_WHEN_Milestones/<id>
howmuch: 72_HOWMUCH_Procurement/<file-id>
correlation_id: yymmdd-NN
sources: [shared/B_OPERATIONS/03_WORK_Flow/...]
---
## Compiled Truth   (rewritable ONLY by the owner; the curated state)
...
---
## Timeline         (append-only; each line with [Source: <path>])
- <date>  ...  [Source: shared/B_OPERATIONS/03_WORK_Flow/...]
```

- **Compiled Truth**: the *current* curated state. Rewritten **only by the owner** of the home.
- **Timeline**: **append-only**. Each line cites its source with `[Source: <path>]`.
- **W facets** are *read-only* pointers: they declare the item's other faces without copying content.

## 4. Immutable sources (exception)

Sealed evidence pages (an immutable Inbox original, a sealed expediente artefact, a closed period rollup) have **no Compiled Truth**: they are only *captured*. Their frontmatter
includes:

```
immutable: true
sealed_from: <path>@<git-sha>
```

They are WORM (write-once-read-many): sealed and never rewritten (P4, P6).

## 5. The `twin` facet (P8)

The old "digital twins" stop being a structural axis and become an **optional label**:
- `PHYS` — physical reality (hardware, buildings, instruments).
- `OPER` — operation (running processes, shifts).
- `ORG` — organisation (roles, teams, decisions).
- `META` — the memory/system itself.

## 6. Node types

| Type | Lives in | Compiled Truth | Timeline | Mutability |
|------|----------|----------------|----------|------------|
| **Canonical page** | W families (10..70) | yes (owner) | yes (append) | mutable by owner |
| **Expediente** | `03_WORK_Flow/<Type>/<exp>` | cover `_expediente.html` (state) | yes | advances by state (OPEN..CLOSED) |
| **Fact/rollup** | `12_STATUS_Daily` (→ Weekly/Monthly/Yearly) | no (it is the entry) | it is the entry | append-only, sealed on close |
| **Evidence** | sealed in place (Inbox original · expediente artefact · `_OUTPUT`) | no | no | WORM |
| **Now/incident** | `11_STATUS_Now` | yes | yes | mutable until closed |
| **README** | every folder | (n/a, prose) | (n/a) | editable |
| **Config** | `06_CORE_Control`, `08_CORE_Profile` | (n/a, YAML) | (n/a) | editable by owner |
