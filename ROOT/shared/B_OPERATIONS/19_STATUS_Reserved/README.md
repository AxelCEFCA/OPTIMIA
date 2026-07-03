# 19_STATUS_Reserved

> **Reserved** slot in the STATUS family (spare / future subcategory).

In v01 this number held Chronicle/Evidence/Health/Restricted/Archive/Audit; in v02 those are re-homed (see `10_STATUS/README.md` and `INCONSISTENCIES_v02.md`), so the slot is free. If this organisation needs a dedicated store (e.g. a separate immutable audit log), define it here and declare it in `08_CORE_Profile`. Keep the canonical-home + facets law (P1).
