# 13_STATUS_Weekly - Weekly state rollup

> **5W2H - STATUS ->** At the end of each weekly, a single HTML consolidates the most relevant of the period (facts, decisions, incidents, deliveries, KPIs, what changed).

**Naming.** `yyWww_STATUS_Weekly.html`  (e.g. `26W27_STATUS_Weekly.html`).

**Regime.** Append-only while the weekly is open; **sealed (WORM)** once it closes (at end of ISO week). Each rollup links its sources with `[Source: ...]` and points at the finer-grained rollups it summarises.

**Status.** Empty in the template. Populate when this organisation is configured (`08_CORE_Profile` + `C_OPERATIONAL_KIT/_SKILLS/CONFIG_QUESTIONS.md`).
