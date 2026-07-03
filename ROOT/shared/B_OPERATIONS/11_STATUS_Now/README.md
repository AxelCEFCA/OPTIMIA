# 11_STATUS_Now - live state {mutable}

> **5W2H - STATUS ->** The current live state of the organisation, **updated through the day** as events happen (an open incident, a system alarm, a decision taken, a message that changes things).

**Naming.** A single rolling page `Now.html` that the agent rewrites as the state changes (mutable). Open incidents live here until closed.

**Flow.** At the end of the day, the relevant lines of `Now.html` are consolidated into `12_STATUS_Daily/yymmdd_STATUS_Daily.html` (append-only history); `Now.html` then reflects only what is still live.

**Excluded from RAG** (mutable, unstable). Empty in the template. Populate when this organisation is configured (`08_CORE_Profile` + `C_OPERATIONAL_KIT/_SKILLS/CONFIG_QUESTIONS.md`).
