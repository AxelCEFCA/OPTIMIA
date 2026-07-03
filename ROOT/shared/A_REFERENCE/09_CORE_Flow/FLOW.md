---
id: Flow
home: shared/A_REFERENCE/09_CORE_Flow
owner: role:leadership
status: approved
sensitivity: internal
twin: META
---

# 09_CORE_Flow — from raw to sealed, in 5 steps

> **What question does it answer?** *"What happens to a datum from the moment it arrives until it is
> recorded and sealed?"* It is the master procedure for the data lifecycle.

## What goes here
- The **raw → processed → recorded → sealed** procedure, in 5 steps.
- Where each artefact lands at each step.

## What does NOT go here
- The rules of who owns what → `06_CORE_Control/ownership.yaml`.
- The laws that underpin it (P1–P8) → `04_CORE_Governance`.

---

## The flow in 5 steps (v02)

### Step 1 — A message ARRIVES in the Inbox
Every incoming message (any channel) is written as one **immutable** file in `01_WORK_Inbox`, named
`yymmdd_hhmmss_CHANNEL_SenderId_Subject.html`. It is **never discarded** (intake law).

### Step 2 — Intake classification (an action, not a folder)
At intake the message is classified by request type (`06_CORE_Control/router_rules.yaml`) and a
`correlation_id` is minted. It is routed to the right expediente **type** in `03_WORK_Flow` (opening a new
expediente or updating an existing one). Low confidence → it stays in the Inbox flagged for human triage.

### Step 3 — Work happens in the expediente (03_WORK_Flow)
The agent works the case inside `03_WORK_Flow/NN_Theme/<yymmdd_SubjectInPascalCase_V01>/`: it gathers artefacts
(quotes, minutes, reports, offers…) and updates the `_expediente.html` cover, whose **state** advances
OPEN→IN_PROGRESS→WAITING→RESOLVED→CLOSED (or REJECTED). Canonical business content is written/updated in
its W home (P1); the expediente holds **facets** (supplier→46, cost→72, system→13, location→51), not copies.

### Step 4 — Evidence is SEALED in place; outgoing goes through the Outbox
Decisive artefacts are sealed **in place** (`immutable: true`, `sealed_from: …`): the Inbox original, the
sealed artefact inside the expediente, and — for anything sent — the message in `02_WORK_Outbox`
(`1_PROPOSED→…→5_SENT`, human-in-the-loop) with a heavy copy in `_OUTPUT`. Nothing is rewritten.

### Step 5 — The fact is emitted to STATUS; knowledge is promoted
When the expediente closes it **emits a fact** into `12_STATUS_Daily` (append-only; the canonical dated
log), which is later consolidated into `13_STATUS_Weekly` → `14_STATUS_Monthly` → `15_STATUS_Yearly`.
`11_STATUS_Now` reflects only what is still live. If the work produced content for the shared shelf, it is
**promoted** to `A_REFERENCE` via a **handshake** (human review) declaring its `target:` home; on approval
the index generator (`07_CORE_Index`) regenerates `index.html` + `index.json` (P7).

---

## Artefact journey summary

```
01_WORK_Inbox (message, immutable)
   -> [classify at intake + correlation_id]
      -> 03_WORK_Flow/<Type>/<expediente>   (work; state in _expediente.html; W-home facets)
         -> seal in place (Inbox original / expediente artefact / 02_WORK_Outbox 5_SENT + _OUTPUT)
            -> on close: emit fact -> 12_STATUS_Daily -> 13_Weekly -> 14_Monthly -> 15_Yearly
               -> (if shared knowledge) promotion handshake -> A_REFERENCE -> index regenerated
```

**Invariant:** at no step is content duplicated between buckets; each hop leaves **pointers** (facets,
`correlation_id`, sources). The received message is never lost; sealed evidence is never rewritten.
