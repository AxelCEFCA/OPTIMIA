---
id: Templates
home: shared/A_REFERENCE/02_CORE_Templates
owner: role:leadership
status: approved
sensitivity: internal
twin: META
---

# 02_CORE_Templates — blank memory-page moulds

> **What question does it answer?** *"What does a well-formed memory page look like for each node type?"*
> These are the moulds for **memory pages**. The moulds for the organisation's **business documents**
> (email, report, minutes) live in `38_HOW_Templates`.

Copy a block, fill it, drop it in the right canonical home.

## Canonical page (a thing in a W family)
```
---
id: <ConceptOrCode>
home: shared/A_REFERENCE/<bucket>/<id>
owner: role:<role>
status: draft
sensitivity: internal
twin: <PHYS|OPER|ORG|META>
# facets (read-only pointers), as applicable:
where: 51_WHERE_LocationTree/<CODE>
who: role:<role>
---
## Compiled Truth
<the current curated state, written by the owner>

## Timeline
- <date>  <what happened>  [Source: <path>]
```

## Decision record (ADR) — lives in `28_WHY_Decisions`
```
---
id: <DecisionName>
home: shared/A_REFERENCE/28_WHY_Decisions/<DecisionName>
owner: role:<role>
status: approved
correlation_id: <yymmdd-NN>
---
## Compiled Truth
**Context.** <what forced a decision>
**Decision.** <what was decided>
**Rationale.** <why — the argument>
**Consequences.** <trade-offs>
> The dated FACT of deciding is in 12_STATUS_Daily (pointer, not duplicated).
```

## Ticket — lives in `03_WORK_Flow/<state>`
```
---
id: <yymmdd_TicketName>
home: shared/B_OPERATIONS/03_WORK_Flow/<state>/<id>
owner: role:<role>
status: <QUEUE|WORK|WAIT|VERIFY|DONE>
correlation_id: <yymmdd-NN>
---
## Compiled state
<what is being done, current step, blockers>

## Timeline
- <date>  <state change>  [Source: <path>]
```

## Evidence stub — lives in `03_WORK_Flow`
```
---
id: <yymmdd_Artefact>
home: shared/B_OPERATIONS/03_WORK_Flow/<id>
immutable: true
sealed_from: <path>@<git-sha>
sensitivity: internal
---
<short description + pointer to the blob; the binary lives in _OUTPUT or an attachment store>
```
