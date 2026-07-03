---
id: IndexSpec
home: shared/A_REFERENCE/07_CORE_Index
owner: role:leadership
status: approved
sensitivity: internal
twin: META
---

# 07_CORE_Index — index spec & generator (P7)

> **What question does it answer?** *"How are the human and machine indexes produced, and what must they
> contain?"* Both `index.html` (human) and `index.json` (machine) are **generated**, never hand-edited.

## What goes here
- The **spec** of the two indexes and the **generator** that builds them from the pages' frontmatter.
- The **gate**: a check that fails if a committed index does not match the regenerated one.

## What does NOT go here
- The generated indexes themselves (those live at each chamber root: `A_REFERENCE/index.html` +
  `index.json`, `B_OPERATIONS/index.html` + `index.json`, `C_OPERATIONAL_KIT/index.html`).

## index.json (machine site-map)
```
{
  "chamber": "A_REFERENCE",
  "generated_by": "07_CORE_Index",
  "folders": [
    { "name": "13_WHAT_SystemTree", "kind": "derivative", "family": "WHAT", "summary": "..." }
  ]
}
```
- It is the agent's site-map / RAG index. It passes the **same anti-PII gate** (it must not leak the
  contents of `43_WHO_People`).

## index.html (human landing)
- A navigable rendering of the same data: the chamber's folders grouped by family, each linking to its
  README. Lightweight HTML, images referenced.

## Rules
- **Generated, not edited** (P7). Regenerate after any structural change or promotion.
- The seed indexes shipped in the template are placeholders; replace them by running the generator once
  the instance is configured.
