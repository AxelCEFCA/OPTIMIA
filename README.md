# 5W2H Memory Template — V04

**Date:** 2026-07-01 · **Kind:** generic, reusable **template** · **Base:** `260701_MemoryTemplate5W2H_v03`

> Same three chambers and laws as v03. **v04 adds the agent-mirror & consolidation model** and carries the
> corrected license/attribution. Everything else is inherited verbatim from v03.

## What v04 adds

### 1. Agent mirror = a particularised copy of the shared structure
`ROOT/agents/agent01/README.md` now states clearly that each agent's private memory is a structure
**similar to the shared memory** (`ROOT/shared/`) — the same three chambers and 5W2H spine — that is
**replicated for every agent created** and **particularised** to the **functions that agent performs**
(its own `_self.md`, only the `03_WORK_Flow` themes and skills it needs). `agent01` is the **prototype**;
each real agent is a specific particularisation of it.

### 2. Periodic consolidation into the shared memory (the strategy)
Each agent manages a **particular area** and keeps its own STATUS rollups. On a **configurable cadence**
(set in `08_CORE_Profile.agents.consolidation.cadence`, e.g. **Monthly** and/or **Yearly**), each agent's
period rollup (`14_STATUS_Monthly` / `15_STATUS_Yearly`) is **consolidated — as a summary + pointer (P1,
no copy) — into the shared STATUS rollup of the same period**, via the promotion handshake (human-in-the-
loop). The shared `10_STATUS` thus stays continuously updated with what the sub-agents have done.
- Full model: `ROOT/shared/A_REFERENCE/00_CORE/AGENT_CONSOLIDATION.md`.
- Config block: `08_CORE_Profile.agents` (in `_PROFILE_TEMPLATE.yaml` / `_PROFILE_EXAMPLE.yaml`).
- Cross-referenced in `04_CORE_Governance` (promotion) and `B_OPERATIONS/10_STATUS/README.md`.

### 3. License & attribution correction (from v03)
`00_CORE/LICENSE_AND_ATTRIBUTION.md` and `ROOT/LICENSE` now link the **real OPTIMIA repository**
<https://github.com/AxelCEFCA/OPTIMIA> (cited in the SPIE 2026 papers as *"OPTIMIA: generic memory concept
and multi-agent operations framework"*), state that **the memory structure is independent of any agent
harness/runtime**, and no longer reference any third-party harness tool. MIT license + plain-language
no-warranty clause unchanged.

## Build (reproducible; UTF-8, no BOM)
1. `python build_template_v04.py` — copies v03 `ROOT/`, rewrites the agent prototype README, adds
   `00_CORE/AGENT_CONSOLIDATION.md`, appends the `agents:` profile block, notes it in GOVERNANCE and the
   shared STATUS README, bumps version strings to V04, regenerates `_TREE.txt`.
2. `python ROOT/shared/C_OPERATIONAL_KIT/_TOOLS/gen_index.py` — regenerates each chamber's index (P7).

See `DESIGN_v04.md` for the model and the config. The earlier redesigns are documented in the v02
(Inbox/Outbox/Flow + periodic STATUS) and v03 (numbered thematic Flow) folders.

## Deploy
As before: `START_HERE.md` → `CONFIG_QUESTIONS.md` interview → `08_CORE_Profile/<org_id>.yaml` (now also
the `agents.consolidation` cadence) → project consequences → specialise skills → tailor `03_WORK_Flow`.
Then create the agents by copying and particularising `agents/agent01/`.
