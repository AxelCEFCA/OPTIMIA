# Agent `agent01` — private memory mirror (the prototype for every agent)

## What this is
This directory is an example agent's **private memory**. Its structure is **similar to the shared memory**
in [`../../shared/`](../../shared/) — the same three chambers and the same 5W2H spine — but **at the
agent's own scale** and **particularised to what the agent does**.

`agent01` is the **prototype**. Every agent that is created **starts from a copy of this same structure**
and is then **particularised**: it keeps only the files, `03_WORK_Flow` themes and skills that correspond
to the **functions that agent will perform**, fills its `_self.md`, and is registered as an owner/role. So
all agents share the same shape, but each one is a **specific particularisation** of it (different scope,
different themes, different skills).

## How to create a new agent (particularise this prototype)
1. **Copy** `agents/agent01/` and **rename** it to the new agent id → `agents/<id>/`.
2. **Fill** `A_REFERENCE/00_CORE/_self.md`: the agent's role, scope, the **functions it performs**, its
   limits, and what it may read/write.
3. **Particularise the mirror**: keep only the `03_WORK_Flow` themes and the W-family detail relevant to
   its function; add its own skills/tools/services under its `C_OPERATIONAL_KIT/`.
4. **Register it**: add `agents/<id>` to `shared/A_REFERENCE/06_CORE_Control/ownership.yaml` (owners +
   a `self_entries` block) and add its role to `shared/A_REFERENCE/41_WHO_Roles`.

## The three directions of information
1. **READ from shared (read-only):** the canonical W descriptions and homes (P1) live in `shared/`. The
   agent consults them and points at them as **read-only facets**; it never rewrites them.
2. **WRITE its own detail (single-writer):** everything under `agents/<id>/…` has `owner: role:<id>`. Here
   the agent is sole owner — its Inbox, its expedientes (in the themes it manages,
   `03_WORK_Flow/NN_Theme/yymmdd_SubjectInPascalCase_V01/`), its own STATUS (Now + Daily/Weekly/Monthly/
   Yearly rollups), and its private view of each W.
3. **CONSOLIDATE up to shared (periodic promotion):** on a configured cadence (see below), the agent's
   period STATUS summaries are **promoted and merged into the shared STATUS**, so `shared/` stays updated
   with what every sub-agent has done. What goes up is a **summary + pointer** to the agent's home
   (P1 — never a copy).

## Periodic consolidation into the shared memory  ← the key strategy
Each agent manages a **particular area** and keeps its own STATUS rollups. On a cadence configured at setup
time in `shared/A_REFERENCE/08_CORE_Profile` (`agents.consolidation.cadence`, e.g. **Monthly** and/or
**Yearly**), each agent's period rollup (its `14_STATUS_Monthly` / `15_STATUS_Yearly`) is **consolidated
into the shared STATUS rollup of the same period**: the shared `shared/B_OPERATIONS/14_STATUS_Monthly` /
`15_STATUS_Yearly` **aggregates one summary block per agent**, each ending with
`[Source: agents/<id>/B_OPERATIONS/14_STATUS_Monthly/…]`. The merge is a **handshake** approved by the
shared-STATUS owner (human-in-the-loop). This way the **shared status is continuously fed by the
sub-agents** that manage the particular areas, without duplicating their detail. Full model:
[`shared/A_REFERENCE/00_CORE/AGENT_CONSOLIDATION.md`](../../shared/A_REFERENCE/00_CORE/AGENT_CONSOLIDATION.md).

## Its own operational kit
The agent also has its **own `C_OPERATIONAL_KIT/`** (the same four parts, at its scale). It **inherits the
shared kit and extends it** with what is its own; capability resolution is **agent-first, then shared**. It
never duplicates the shared kit — it points to it.

## Tree (at `agent01` scale)
```
agents/agent01/
├── README.md                      (this file)
├── A_REFERENCE/
│   ├── 00_CORE/_self.md           the agent profile (role, scope, functions, limits, read/write)
│   └── 10_WHAT … 70_HOWMUCH/README.md   the agent's private view of each W family
├── B_OPERATIONS/
│   ├── 00_WORK/  01_WORK_Inbox · 02_WORK_Outbox · 03_WORK_Flow/NN_Theme · 04-09 reserved
│   └── 10_STATUS/ 11_Now · 12_Daily · 13_Weekly · 14_Monthly · 15_Yearly · 16-19 reserved
└── C_OPERATIONAL_KIT/             the agent's own kit (inherit shared + extend)
      _SKILLS/ · _TOOLS/ · _RESOURCES/ · _SERVICES/
```

## Mark
[5W2H-mirror] — the prototype private mirror; same shape as `shared/`, particularised per agent, and
consolidated into the shared STATUS on a configured cadence.
