# Default skill · Use the directory structure

**Goal:** be able to move around the whole memory and leave every piece of information in its place.

## 1. The mental map (3 layers)

1. **A_REFERENCE (00–79)** — the **permanent model**. What you consult. Changes slowly.
   8 families: `00_CORE` (the memory's own rules), `10_WHAT`, `20_WHY`, `30_HOW`, `40_WHO`, `50_WHERE`,
   `60_WHEN`, `70_HOWMUCH`.
2. **B_OPERATIONS (00–19)** — the **now**. Where you work. Changes constantly.
   2 families: `0X_WORK` = `01_WORK_Inbox` (all incoming, every channel) · `02_WORK_Outbox` (all outgoing) · `03_WORK_Flow` (the expediente flow, one subfolder per type) · `04`-`09` reserved. `1X_STATUS` = `11_STATUS_Now` (live) + `12`-`15` Daily/Weekly/Monthly/Yearly rollups · `16`-`19` reserved. File-naming per bucket in `03_CORE_Rules/NAMING.md`.
3. **The KIT** (`C_OPERATIONAL_KIT`) — cross-cutting infrastructure: `_SKILLS` (this), `_RESOURCES`
   (assets), `_TOOLS` (utilities), `_SERVICES` (registry of available skills & MCP capabilities). The
   heavy generated deliverables live in `B_OPERATIONS/_OUTPUT`. Each agent also has its **own** kit under
   `agents/<id>/C_OPERATIONAL_KIT/` (inherit the shared kit + extend with its own).

## 2. How to locate something

- **To look:** open [`../../index.html`](../../index.html) → pick a chamber → its index lists the folders.
- **To classify (where does this incoming thing go?):** apply the algorithm in
  [`../../A_REFERENCE/03_CORE_Rules`](../../A_REFERENCE/03_CORE_Rules/):
  1. Is it a **raw**, unprocessed file? → `B_OPERATIONS/01_WORK_Inbox`.
  2. Is it a **rule of the memory system** itself? → `A_REFERENCE/00_CORE`.
  3. Is it an **asset** (logo/image), a **tool**, or a **skill**? → the **KIT**.
     Is it a **heavy generated deliverable**? → `B_OPERATIONS/_OUTPUT`.
  4. Does it **happen / change / get worked**? → `B_OPERATIONS` (WORK/STATUS).
  5. Is it **descriptive knowledge**? Pick the W by the question: what→10 · why→20 · how→30 ·
     who→40 · where→50 · when→60 · how-much→70.
- **Master rule:** an entity has **one canonical home** (its identity) + **facets** (pointers) in the
  other dimensions. Do not copy: link.

## 3. Golden rules when writing

- **Format:** working documents in **lightweight HTML with referenced images** (to `_RESOURCES`); never
  embed images in the work (that is only for `_OUTPUT`). Skills are Markdown.
- **Speak by role, never by person** (except the restricted lane `43_WHO_People`).
- **Page anatomy:** `Compiled Truth` (rewritable by the owner) + `Timeline` (append-only, each line with
  `[Source:]`).
- **The full folder name is the address** (`13_WHAT_SystemTree`); the chamber is just the aisle. The same
  number repeats across chambers (`12_WHAT_OrgStructure` in A vs `12_STATUS_Daily` in B), so always
  use the full name in references.

## 4. Full detail

The 100 folders with their discriminating criterion and the conflict closure are in
`../../A_REFERENCE/03_CORE_Rules/ClassificationCriteria.md`. This is the operating summary.
