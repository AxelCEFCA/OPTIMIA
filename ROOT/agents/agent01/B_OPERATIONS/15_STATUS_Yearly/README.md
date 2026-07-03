# 15_STATUS_Yearly - Yearly state rollup

> **5W2H - STATUS ->** At the end of each yearly, a single HTML consolidates the most relevant of the period (facts, decisions, incidents, deliveries, KPIs, what changed).

**Naming.** `yyyy_STATUS_Yearly.html`  (e.g. `2026_STATUS_Yearly.html`).

**Regime.** Append-only while the yearly is open; **sealed (WORM)** once it closes (at end of year). Each rollup links its sources with `[Source: ...]` and points at the finer-grained rollups it summarises.

**Status.** Empty in the template. Populate when this organisation is configured (`08_CORE_Profile` + `C_OPERATIONAL_KIT/_SKILLS/CONFIG_QUESTIONS.md`).
