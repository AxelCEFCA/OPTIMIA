# 03_WORK_Flow - the expediente flow (thematic, numbered)

> **5W2H - WORK ->** Where the actual case-work lives. Expediente **types** are organised into a **numbered, thematic taxonomy**: the tens digit is a super-theme **band**, so related workflows have adjacent suffix numbers. Inside each type, one folder per **expediente** (a case file that gathers all its artefacts, e.g. `260701_MinorContractLab_V01/`).

> **This is a GENERAL OPTIMIA template.** The theme folders below are a broad default for an organisation that operates astrophysical observatories. **Every organisation must adapt this directory carefully to its own use case** - add, remove, rename or renumber themes *within their band* so that related workflows keep adjacent suffix numbers (administration stays in `10`-`19`).

> **If you are an AI agent performing the initial configuration of this memory:** do **not** accept these defaults blindly. Ask the organisation's managers all the relevant questions - which areas, departments, committees, standing groups and recurring case (expediente) types they actually handle, and how they want them grouped - so that you leave this `03_WORK_Flow` area well organised and tailored to the final organisation's real needs **before** creating any expediente. Record the agreed taxonomy in `08_CORE_Profile.enums.expediente_types`.

## Structure
```
03_WORK_Flow/
  NN_Theme/                       a numbered theme (band by tens digit; see below)
    yymmdd_SubjectInPascalCase_V01/  one expediente (opening date + PascalCase subject + version; see NAMING.md)
      _expediente.html            cover: id, type, estado, ambito, timeline
      yymmdd_KIND_Detail.ext      the expediente's artefacts
```
> Expediente folder naming (`yymmdd_SubjectInPascalCase_V01/`, subject in PascalCase, `_V01` version bumped for later similar-subject expedientes) is defined in `03_CORE_Rules/NAMING.md`.

## Numbering bands (related themes stay adjacent)
- **00-09** general / cross-cutting.
- **10-19** administration, governance & compliance.
- **20-29** scientific.
- **30-39** engineering & technical.
- **40-49** outreach & external relations.
- **50+** free for organisation-specific super-themes.
Gaps between numbers are intentional room to insert new themes without renumbering neighbours.

## Expediente lifecycle (state = metadata, not folder)
Each expediente carries its state in its `_expediente.html` cover: `OPEN -> IN_PROGRESS -> WAITING -> RESOLVED -> CLOSED` (or `REJECTED`). The state machine is defined in `33_HOW_Processes`; closing an expediente emits a line to `12_STATUS_Daily`. Archiving is a **state flag** (`CLOSED`), not a move (R4). File-naming: `03_CORE_Rules/NAMING.md`.

## Default themes (configurable in `08_CORE_Profile.enums.expediente_types`)

**00-09 - General / cross-cutting**
- `00_General` - General / cross-cutting or not-yet-classified expedientes (a catch-all before a theme is chosen).

**10-19 - Administration, Governance & Compliance**
- `10_Governance` - Governance bodies & strategic decisions (board / council / faculty / committees), minutes, resolutions.
- `11_RulesAndRegulations` - Internal rules, policies and the applicable regulatory framework (as living dossiers).
- `12_ArtificialIntelligenceCommittee` - AI committee & AI governance: AI risk, AI-Act/AESIA conformity, model approvals, OPTIMIA oversight.
- `13_ComplianceAndCybersecurity` - ENS / NIS2 / ISO 27001 / GDPR compliance, security audits, hardening, access control.
- `14_ContractsAndTenders` - Tenders, framework agreements and major service contracts.
- `15_Purchases` - Procurement / minor contracts (quotes, offers, justification memo, purchasing-platform form).
- `16_GrantsAndFunding` - Funding calls, grant applications and management of funded projects.
- `17_HumanResources` - Hiring, evaluations, training, onboarding / offboarding, students / interns.
- `18_SafetyRiskPrevention` - Occupational-risk prevention (PRL), safety plans, drills and emergencies.

**20-29 - Scientific**
- `20_ScientificArea` - Scientific area coordination & strategy (research lines, science policy, the science area as an actor).
- `21_ScientificOperation` - Science operations: telescope operation, observing runs, night reports, science verification.
- `22_ObservingPrograms` - Time allocation (TAC), surveys, observing programmes and open time.
- `23_ScientificDataProcess` - Data reduction pipelines, processing and the scientific data archive.
- `24_DataReleasesAndPublications` - Data releases and scientific / technical publications and proceedings.

**30-39 - Engineering & Technical**
- `30_Engineering` - Engineering area coordination & technical strategy (the engineering department as an actor).
- `31_Projects` - Engineering & science projects (design / development / upgrade).
- `32_Developments` - Developments, R&D, prototypes and in-house software/tools (incl. the AI platform).
- `33_EngineeringChanges` - Engineering change requests, configuration changes and upgrades.
- `34_CommissioningAndAcceptance` - Commissioning, acceptance tests, first light and hand-over.
- `35_Maintenance` - Preventive / corrective maintenance work orders and calibration.
- `36_Incidents` - Infrastructure / instrument / cyber incidents and their post-mortems.
- `37_FacilitiesAndSite` - Site infrastructure works (power, HVAC, water, roads, buildings, plant).
- `38_ITandOT` - IT / network / control-systems (OT) changes and operations.

**40-49 - Outreach & External Relations**
- `40_OutreachArea` - Outreach / education / dissemination area coordination (the outreach centre as an actor).
- `41_EventsAndOutreach` - Conferences, workshops, eclipses, open days, visits and dissemination activities.
- `42_WorkingGroups` - Standing working groups and external networks (safety, engineering, coordination bodies, inter-observatory groups).

**Status.** Empty in the template. Populate when this organisation is configured (`08_CORE_Profile` + `C_OPERATIONAL_KIT/_SKILLS/CONFIG_QUESTIONS.md`).
