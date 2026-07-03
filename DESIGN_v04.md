# MemoryTemplate5W2H — v04 design note (agent mirror + consolidation)

**Date:** 2026-07-01 · **Base:** `260701_MemoryTemplate5W2H_v03`

v04 leaves `shared/` and `03_WORK_Flow` unchanged and adds the **agent-mirror & consolidation** model,
plus the corrected license/attribution (real repo, no harness tools).

## 1. Agent mirror = particularised copy of the shared structure
- Each agent has a **private mirror** `agents/<id>/` with the **same three chambers and 5W2H spine** as
  `shared/`, at the agent's scale.
- `agents/agent01/` is the **prototype**. A new agent = **copy** the prototype + **particularise**: fill
  `_self.md` (role, scope, functions), keep only the `03_WORK_Flow` themes and W-detail relevant to its
  function, add its own skills/tools/services, and register it in `06_CORE_Control/ownership.yaml` +
  `41_WHO_Roles`. Same shape → many specific particularisations.
- Single-writer + facets (P1) unchanged: the agent owns everything under `agents/<id>/`; the canonical
  homes stay in `shared/` and are referenced as read-only facets.

## 2. Consolidation strategy (agent → shared)
The problem: keep the **shared** status current with what each sub-agent (managing a particular area) does,
without duplicating detail.

The strategy:
- Each agent keeps its own STATUS cascade (Now → Daily → Weekly → Monthly → Yearly).
- On a **configurable cadence** (`08_CORE_Profile.agents.consolidation.cadence`, e.g. Monthly and/or
  Yearly), the agent's period rollup is **consolidated into the shared STATUS rollup of the same period**.
- The shared `12_STATUS_Daily`..`15_STATUS_Yearly` **aggregate one summary block per agent**, each ending
  `[Source: agents/<id>/B_OPERATIONS/…]` — a **summary + pointer**, never a copy (P1).
- The merge is a **promotion handshake** approved by the shared-STATUS owner
  (`agents.consolidation.approver`, default `role:leadership`) — human-in-the-loop.
- Optionally, approved reference knowledge (closed expedientes, decisions) also promotes to shared
  `A_REFERENCE` via the same handshake (`also_promote_approved_reference`).

```
agent (area) rollups: 11_Now -> 12_Daily -> 13_Weekly -> 14_Monthly -> 15_Yearly
   -> [cadence: Monthly/Yearly]  promotion handshake (owner approves)
      -> shared 14_STATUS_Monthly / 15_STATUS_Yearly  (one summary block per agent + [Source:])
```

## 3. Where it is defined (consistency)
| File | Change |
|------|--------|
| `agents/agent01/README.md` | rewritten: similar-to-shared, replicate + particularise per function, consolidation |
| `00_CORE/AGENT_CONSOLIDATION.md` | **new** — the full model + flow + config |
| `08_CORE_Profile/_PROFILE_TEMPLATE.yaml` + `_PROFILE_EXAMPLE.yaml` | **new** `agents:` block (prototype + consolidation) |
| `04_CORE_Governance/GOVERNANCE.md` | promotion section: periodic agent-consolidation bullet |
| `B_OPERATIONS/10_STATUS/README.md` | note: rollups aggregate one summary block per agent |
| `00_CORE/README.md` | pointer to `AGENT_CONSOLIDATION.md` |
| portals + `ARCHITECTURE.md` | version bumped V03 → V04 |

## 4. License/attribution correction (carried into v04)
`00_CORE/LICENSE_AND_ATTRIBUTION.md`, `ROOT/LICENSE` and `ARCHITECTURE.md` now link the real repository
<https://github.com/AxelCEFCA/OPTIMIA> (cited in the SPIE 2026 papers), state the memory structure is
**independent of any agent harness**, and drop the third-party tool references. The corrected files were
edited in v03 and inherited here.
