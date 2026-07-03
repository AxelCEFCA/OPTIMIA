---
id: Naming
home: shared/A_REFERENCE/03_CORE_Rules/NAMING
owner: role:leadership
status: approved
sensitivity: internal
twin: META
---
# NAMING - file-naming convention per B_OPERATIONS bucket (v03)

> **What question does it answer?** *"What do I call the file I am about to create, in each working
> bucket?"* One convention per bucket, so names are self-describing and sortable.

## 01_WORK_Inbox - received messages
`yymmdd_hhmmss_CHANNEL_SenderId_Subject.html`
- `yymmdd_hhmmss` - date and time of reception.
- `CHANNEL` - intake channel (closed catalogue in `08_CORE_Profile.enums.channels`; default
  `EMAIL WHATSAPP TELEGRAM PHONE VIDEOCONF INPERSON`), optionally glued to the receiving account
  (`EMAILops` = the EMAIL account *ops*).
- `SenderId` - short id of who sent it + their org (`acmeco`).
- `Subject` - CamelCase, no spaces/accents.
- Example: `260701_102311_EMAILops_acmeco_RequestQuoteRenewal.html`.
- One file per message; **immutable** once written.

## 02_WORK_Outbox - sent messages
`yymmdd_hhmmss_CHANNEL_RecipientId_Subject.html`, advancing through the state subfolders
`1_PROPOSED -> 2_EDITING -> 3_APPROVED -> 5_SENT` (or `4_DISCARDED`).

## 03_WORK_Flow - expedientes
- Type subfolder: one of the numbered themes (`15_Purchases`, `36_Incidents`, ... - banded, see `03_WORK_Flow/README.md`).
- Expediente folder: `yymmdd_SubjectInPascalCase_V01/`.
  - `yymmdd` - the expediente opening date (year, month, day, 2 digits each).
  - `SubjectInPascalCase` - the subject with each word's first letter uppercased, no spaces, no accents, no hyphens/underscores inside the subject (e.g. "solicita librar mañana" -> `SolicitaLibrarManana`).
  - `_V01` - two-digit version suffix; bump to `_V02`, `_V03`... if a later expediente arises on a similar/related subject, so similar subjects are versioned instead of colliding.
  - Full example: `260701_SolicitudLibrarManana_V01`.
- Cover page: `_expediente.html` - metadata `id, type, estado (OPEN..CLOSED/REJECTED), ambito, timeline`.
- Artefacts inside: `yymmdd_KIND_Detail.ext` (e.g. `260602_OFERTA_Integra.pdf`).
- State is metadata on the cover; **do not** encode state in the folder name (do not move the folder).

## 1X_STATUS - live state + periodic rollups
| Bucket | File | Example |
|--------|------|---------|
| `11_STATUS_Now` | a single mutable `Now.html` | `Now.html` |
| `12_STATUS_Daily` | `yymmdd_STATUS_Daily.html` | `260701_STATUS_Daily.html` |
| `13_STATUS_Weekly` | `yyWww_STATUS_Weekly.html` (ISO week) | `26W27_STATUS_Weekly.html` |
| `14_STATUS_Monthly` | `yymm_STATUS_Monthly.html` | `2607_STATUS_Monthly.html` |
| `15_STATUS_Yearly` | `yyyy_STATUS_Yearly.html` | `2026_STATUS_Yearly.html` |

Each rollup is append-only while its period is open and **sealed (WORM)** once it closes; it links its
sources with `[Source: ...]` and points at the finer-grained rollups it summarises.

## _OUTPUT - heavy deliverables
Keep the organisation's output convention (declared in `08_CORE_Profile.output.naming`); by default
`yymmdd_<Type>_<slug>.(pdf|html)` organised by date or type.

---
## Timeline
- 2026-07-01  Naming convention per B_OPERATIONS bucket defined (v02).  [Source: 260701_PropuestaTemplate5W2H_v02.txt]
- 2026-07-01  Expediente folder naming set to `yymmdd_SubjectInPascalCase_V01` (v03).  [Source: user directive]
