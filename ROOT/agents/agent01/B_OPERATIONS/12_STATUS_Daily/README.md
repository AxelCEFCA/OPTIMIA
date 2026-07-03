# 12_STATUS_Daily - Daily state rollup

> **5W2H - STATUS ->** At the end of each daily, a single HTML consolidates the most relevant of the period (facts, decisions, incidents, deliveries, KPIs, what changed).

**Naming.** `yymmdd_STATUS_Daily.html`  (e.g. `260701_STATUS_Daily.html`).

**Regime.** Append-only while the daily is open; **sealed (WORM)** once it closes (at end of day). Each rollup links its sources with `[Source: ...]` and points at the finer-grained rollups it summarises.

**Status.** Empty in the template. Populate when this organisation is configured (`08_CORE_Profile` + `C_OPERATIONAL_KIT/_SKILLS/CONFIG_QUESTIONS.md`).
