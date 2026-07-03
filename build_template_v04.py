# -*- coding: utf-8 -*-
"""
build_template_v04.py  --  Generic 5W2H Memory Template, version V04.

v04 adds the AGENT MIRROR + CONSOLIDATION model:
  - agents/agent01/README.md rewritten: the agent memory is a structure SIMILAR to shared/, replicated
    and PARTICULARISED per agent (each agent keeps the files/themes relevant to its function).
  - a strategy for how each agent's particular information PERIODICALLY becomes part of shared/: the
    agent's monthly/yearly STATUS rollups are consolidated (summary + pointer) into the shared STATUS
    rollups of the same period, on a cadence configured in 08_CORE_Profile.
Everything else is inherited verbatim from v03.

Strategy: copytree v03/ROOT -> v04/ROOT ; overwrite the agent README ; add 00_CORE/AGENT_CONSOLIDATION.md ;
append the `agents:` profile block ; note it in GOVERNANCE and the shared STATUS README ; bump versions ;
regenerate _TREE.txt (run gen_index.py afterwards).

UTF-8, no BOM.
"""

import shutil
from pathlib import Path

V03 = Path(r"V:\30_Developments\260701_MemoryTemplate5W2H_v03\ROOT")
DEV = Path(r"V:\30_Developments\260701_MemoryTemplate5W2H_v04")
ROOT = DEV / "ROOT"

misses = []


def sub(path: Path, old: str, new: str, label: str):
    t = path.read_text(encoding="utf-8")
    if old not in t:
        misses.append(f"MISS [{label}] {path.name}")
        return
    path.write_text(t.replace(old, new), encoding="utf-8")
    print(f"  ok  [{label}]")


AGENT_README = r"""# Agent `agent01` — private memory mirror (the prototype for every agent)

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
"""

AGENT_CONSOLIDATION = r"""---
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
"""

PROFILE_AGENTS_BLOCK = """
# ---- Agents & consolidation (v04) --------------------------------------------
# Each agent is a particularised copy of agents/<prototype>. Its periodic STATUS rollups are
# consolidated (summary + pointer, P1) into the SHARED STATUS on the cadence below. See
# A_REFERENCE/00_CORE/AGENT_CONSOLIDATION.md.
agents:
  prototype: agents/agent01
  consolidation:
    cadence: [Monthly, Yearly]     # which agent STATUS rollups feed the shared STATUS (configurable)
    into: 10_STATUS                # shared STATUS family (12_STATUS_Daily .. 15_STATUS_Yearly)
    mode: summary_with_pointer     # merge a summary + [Source: agents/<id>/...] ; never copy detail (P1)
    approver: role:leadership      # human-in-the-loop merge into the shared STATUS
    also_promote_approved_reference: true
"""

PROFILE_EXAMPLE_AGENTS = """
# ---- Agents & consolidation (v04) --------------------------------------------
agents:
  prototype: agents/agent01
  consolidation:
    cadence: [Monthly, Yearly]
    into: 10_STATUS
    mode: summary_with_pointer
    approver: role:leadership
    also_promote_approved_reference: true
"""

if __name__ == "__main__":
    if ROOT.exists():
        shutil.rmtree(ROOT)
    shutil.copytree(V03, ROOT)
    print("copied v03 ROOT -> v04 ROOT")

    SHARED = ROOT / "shared"
    AREF = SHARED / "A_REFERENCE"

    # 1. rewrite the agent prototype README
    (ROOT / "agents" / "agent01" / "README.md").write_text(AGENT_README, encoding="utf-8")
    print("  ok  [agent README rewritten]")

    # 2. new CORE doc
    (AREF / "00_CORE" / "AGENT_CONSOLIDATION.md").write_text(AGENT_CONSOLIDATION, encoding="utf-8")
    print("  ok  [AGENT_CONSOLIDATION.md written]")

    # 3. append the agents block to both profiles (idempotent guard)
    for pf, block in [("_PROFILE_TEMPLATE.yaml", PROFILE_AGENTS_BLOCK),
                      ("_PROFILE_EXAMPLE.yaml", PROFILE_EXAMPLE_AGENTS)]:
        p = AREF / "08_CORE_Profile" / pf
        t = p.read_text(encoding="utf-8")
        if "\nagents:" not in t:
            p.write_text(t.rstrip() + "\n" + block, encoding="utf-8")
            print(f"  ok  [agents block appended to {pf}]")
        else:
            print(f"  (note) agents block already in {pf}")

    # 4. GOVERNANCE: add the periodic agent-consolidation to the Promotion section
    sub(AREF / "04_CORE_Governance" / "GOVERNANCE.md",
        "  lands in its W home and the event is chronicled in `12_STATUS_Daily`.",
        "  lands in its W home and the event is chronicled in `12_STATUS_Daily`.\n"
        "- **Periodic agent consolidation:** on a configured cadence "
        "(`08_CORE_Profile.agents.consolidation.cadence`, e.g. monthly/yearly) each agent's period STATUS "
        "rollup is consolidated — as a **summary + pointer** — into the **shared** STATUS rollup of the same "
        "period, via the same handshake. See `00_CORE/AGENT_CONSOLIDATION.md`.",
        "GOV consolidation")

    # 5. shared STATUS base README: note it aggregates agent summaries
    sub(SHARED / "B_OPERATIONS" / "10_STATUS" / "README.md",
        "## Mutability (P4)",
        "## Agent consolidation (v04)\n"
        "On a configured cadence (`08_CORE_Profile.agents.consolidation.cadence`), the period rollups here "
        "(`12_STATUS_Daily`..`15_STATUS_Yearly`) **aggregate one summary block per agent**, each ending with "
        "`[Source: agents/<id>/B_OPERATIONS/…]`. The shared status is thus continuously fed by the sub-agents "
        "that manage particular areas, without duplicating their detail (P1). See "
        "`A_REFERENCE/00_CORE/AGENT_CONSOLIDATION.md`.\n\n"
        "## Mutability (P4)",
        "STATUS README consolidation")

    # 6. 00_CORE README: list the new CORE doc
    sub(AREF / "00_CORE" / "README.md",
        "[`LICENSE_AND_ATTRIBUTION.md`](LICENSE_AND_ATTRIBUTION.md).",
        "[`LICENSE_AND_ATTRIBUTION.md`](LICENSE_AND_ATTRIBUTION.md). The agent-mirror & consolidation model "
        "is in [`AGENT_CONSOLIDATION.md`](AGENT_CONSOLIDATION.md).",
        "00_CORE README consolidation pointer")

    # 7. version bumps V03 -> V04 in the portals + architecture
    sub(SHARED / "index.html", "<b>This is a blank template (V03).</b>",
        "<b>This is a blank template (V04).</b>", "landing V04")
    sub(SHARED / "index.html", "Generic 5W2H Memory Template · V03 · machine index per chamber",
        "Generic 5W2H Memory Template · V04 · machine index per chamber", "landing footer V04")
    sub(SHARED / "index.html",
        "<code>03_WORK_Flow</code> is a numbered thematic taxonomy (adapt per organisation).",
        "<code>03_WORK_Flow</code> is a numbered thematic taxonomy (adapt per organisation). Each agent has a "
        "private mirror under <code>agents/</code> that consolidates its periodic STATUS into the shared STATUS.",
        "landing v04 note")
    sub(SHARED / "C_OPERATIONAL_KIT" / "index.html",
        "Generic 5W2H Memory Template · V03 ·", "Generic 5W2H Memory Template · V04 ·", "kit index V04")
    sub(ROOT / "ARCHITECTURE.md", "# ARCHITECTURE — Generic 5W2H Memory Template V03",
        "# ARCHITECTURE — Generic 5W2H Memory Template V04", "architecture title V04")

    # 8. regenerate _TREE.txt
    lines = [p.relative_to(ROOT).as_posix() + "/" for p in sorted(ROOT.rglob("*")) if p.is_dir()]
    (ROOT / "_TREE.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("\nMISSES:", len(misses))
    for m in misses:
        print(" ", m)
    print("done.")
