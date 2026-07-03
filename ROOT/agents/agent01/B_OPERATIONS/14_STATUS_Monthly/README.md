# 14_STATUS_Monthly - Monthly state rollup

> **5W2H - STATUS ->** At the end of each monthly, a single HTML consolidates the most relevant of the period (facts, decisions, incidents, deliveries, KPIs, what changed).

**Naming.** `yymm_STATUS_Monthly.html`  (e.g. `2607_STATUS_Monthly.html`).

**Regime.** Append-only while the monthly is open; **sealed (WORM)** once it closes (at end of month). Each rollup links its sources with `[Source: ...]` and points at the finer-grained rollups it summarises.

**Status.** Empty in the template. Populate when this organisation is configured (`08_CORE_Profile` + `C_OPERATIONAL_KIT/_SKILLS/CONFIG_QUESTIONS.md`).
