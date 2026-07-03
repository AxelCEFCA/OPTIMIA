# _SKILLS — the default skill base (generic & adaptable)

**Format:** Markdown (`.md`). **Nature:** instructions for operating the structure, not business
content. **State:** a generic template that each organisation **adapts**.

## What this is

When an agent reads the memory for the first time ([`../../START_HERE.md`](../../START_HERE.md)), it
arrives here. This folder holds the **default skills** (the base capabilities every agent on this
memory needs) and the **instructions for the agent to generate its own**, adapted to the organisation
and its concrete use case.

## Default skills

| Skill | What for |
|-------|----------|
| [`skill_use_structure.md`](skill_use_structure.md) | How to use the whole directory structure and locate anything (takes you to the `index` and the classification rules). |
| [`skill_official_documents.md`](skill_official_documents.md) | How to produce the organisation's official documents: use the logos in `_RESOURCES`, place them as agreed, and generate the deliverable in `B_OPERATIONS/_OUTPUT` with the tools in `_TOOLS`. |
| [`skill_generate_your_skills.md`](skill_generate_your_skills.md) | How the agent **generates its own skills** from this base — and why the FIRST step is to ask the organisation's particularities. |
| [`skill_configure_and_customize.md`](skill_configure_and_customize.md) | How to **configure & customise a fresh deployment**: interview first, fill `08_CORE_Profile`, project roles/catalogues/codes/logos, adapt the `03_WORK_Flow` themes, and apply the expediente naming convention. |
| [`skill_process_raw_intake.md`](skill_process_raw_intake.md) | The **general methodology** for any raw Inbox file: receive → classify → extract to its canonical home → name → seal the origin (WORM) → emit a STATUS fact. The per-file version of the `09_CORE_Flow` lifecycle. |
| [`skill_process_transcriptions.md`](skill_process_transcriptions.md) | A **specialisation** of `skill_process_raw_intake.md` for speech-to-text files: it inherits every intake step and adds a **correction pass** that reconciles garbled terms against the glossary/codes/entities and `[REVIEW]`-flags what it cannot resolve. |
| [`skill_critical_review.md`](skill_critical_review.md) | The skeptical **QA / red-team audit**: hunt contradictions, P1 duplication, dangling links, stale-not-archived, PII, glossary/code and naming/profile violations (incl. skill conflicts), and emit a severity-ranked findings list for a human — advise-only, never fixes in place. |
| [`CONFIG_QUESTIONS.md`](CONFIG_QUESTIONS.md) | The **particularities questionnaire** to ask when adapting the template (the answers go into `08_CORE_Profile`). |

> **Skill boundaries at a glance.** `skill_use_structure` = navigate & place; `skill_official_documents` = produce & deliver branded deliverables; `skill_configure_and_customize` = one-time deployment setup; `skill_generate_your_skills` = spawn org-specific skills from this base; `skill_process_raw_intake` = the **parent** intake pipeline and `skill_process_transcriptions` its **child** (transcription-only correction delta — not a duplicate); `skill_critical_review` = the coherence audit that checks the *output* of all the above. Each owns a distinct scope and cross-references the others rather than repeating them.

## Principle

These skills are **generic on purpose**. They do not describe "what this organisation is like"; they
describe "how to operate ANY organisation built on this structure". The specific part lives in the
**instance profile** [`../../A_REFERENCE/08_CORE_Profile`](../../A_REFERENCE/08_CORE_Profile/), which the
agent fills in after asking (see `CONFIG_QUESTIONS.md`).

> When you specialise these defaults for a real organisation, keep the generic copies here and write the
> concrete ones either here (if shared by the whole organisation) or in your agent mirror
> `agents/<id>/` (if they are yours).

## See also
A skill is one kind of **service**. The unified registry of everything an agent can call — these skills
**and** the available **MCP servers** — is [`../_SERVICES/`](../_SERVICES/README.md) (with a card per
service and a machine `services.yaml`). Use `_SKILLS` for the skill *bodies*; use `_SERVICES` to *discover*
what is callable and how.
