---
id: AgentConsolidation
home: shared/A_REFERENCE/00_CORE/AGENT_CONSOLIDATION
owner: role:leadership
status: approved
sensitivity: internal
twin: META
---
# AGENT_CONSOLIDATION — agent mirrors and how their information reaches the shared memory

> **What question does it answer?** *"How is the memory replicated for each agent, and how does each
> agent's particular information periodically become part of the shared memory?"*

## 1. One shape, many particularisations
- The memory has a **shared** part (`shared/`) and one **private mirror per agent** (`agents/<id>/`).
- Every agent mirror has the **same three chambers and the same 5W2H spine** as `shared/`, but **at the
  agent's scale** and **particularised** to the functions that agent performs.
- `agents/agent01/` is the **prototype**: a new agent is created by **copying** it and **particularising**
  it (its `_self.md`, its `03_WORK_Flow` themes, its skills), then registering it in
  `06_CORE_Control/ownership.yaml` and `41_WHO_Roles`. All agents share the shape; each is a specific
  particularisation.

## 2. Single-writer + facets (P1) still holds
- Each agent is the **sole owner** of everything under `agents/<id>/` (`owner: role:<id>`).
- The canonical homes stay in `shared/`; the agent's pages point at them as **read-only facets**. The agent
  never rewrites a shared home directly — it **proposes** (handshake).

## 3. Periodic consolidation into the shared STATUS (the strategy)
Each agent manages a **particular area** and keeps its own STATUS rollups (Now → Daily → Weekly → Monthly →
Yearly). To keep the **shared** status current with what every sub-agent has done:

- **Cadence (configurable):** set at deployment in `08_CORE_Profile.agents.consolidation.cadence` — e.g.
  **Monthly** and/or **Yearly** (an organisation may choose weekly, monthly, yearly, or several).
- **What is consolidated:** each agent's **period rollup** (`14_STATUS_Monthly` / `15_STATUS_Yearly` of the
  agent) — a concise summary of the most relevant of that period for its area.
- **Where it lands:** the **shared** STATUS rollup of the **same period**
  (`shared/B_OPERATIONS/14_STATUS_Monthly` / `15_STATUS_Yearly`), which **aggregates one summary block per
  agent**.
- **How (no duplication, P1):** the shared rollup holds a **summary + pointer**; each block ends
  `[Source: agents/<id>/B_OPERATIONS/14_STATUS_Monthly/…]`. The detail stays in the agent; only the summary
  is aggregated.
- **Approval (human-in-the-loop):** the consolidation is a **promotion handshake** — the agent proposes its
  period summary; the **owner of the shared STATUS** (`agents.consolidation.approver`, default
  `role:leadership`) reviews and merges. Nobody writes another's home without acknowledgement.
- **Optional knowledge promotion:** approved reference knowledge (a closed expediente's outcome, a decision)
  may also be promoted to the shared `A_REFERENCE` via the same handshake, if
  `agents.consolidation.also_promote_approved_reference` is set.

## 4. Flow
```
agent (particular area)  keeps its own rollups:  11_Now -> 12_Daily -> 13_Weekly -> 14_Monthly -> 15_Yearly
        |  at the configured cadence (e.g. Monthly / Yearly)
        v
   promotion handshake  (agent proposes its period summary; shared-STATUS owner approves)
        v
shared/B_OPERATIONS/14_STATUS_Monthly (or 15_STATUS_Yearly)  <- aggregates one summary block per agent
        |   each block: <agent summary>  [Source: agents/<id>/B_OPERATIONS/14_STATUS_Monthly/...]
        v
   the shared status stays continuously updated with the sub-agents' work (no duplication of detail)
```

## 5. Configuration (`08_CORE_Profile.agents`)
```yaml
agents:
  prototype: agents/agent01
  consolidation:
    cadence: [Monthly, Yearly]     # which agent STATUS rollups feed the shared STATUS
    into: 10_STATUS                # shared STATUS family (12_Daily..15_Yearly)
    mode: summary_with_pointer     # merge a summary + [Source: agents/<id>/...] (P1, no copy)
    approver: role:leadership      # human-in-the-loop merge into shared
    also_promote_approved_reference: true
```

## See also
`agents/agent01/README.md` (the prototype mirror) · `04_CORE_Governance` (the promotion handshake) ·
`09_CORE_Flow` (the raw->sealed flow) · `08_CORE_Profile` (the `agents` block) ·
`B_OPERATIONS/10_STATUS` (the shared rollups that aggregate the agents' summaries).

## Mark
[META] — CORE meta-declaration of the agent-mirror and consolidation model.
