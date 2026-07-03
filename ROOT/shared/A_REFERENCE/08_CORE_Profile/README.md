# 08_CORE_Profile — the swappable instance profile

> **What question does it answer?** *"Which organisation is this, what does it materialise, and with
> what enums does it operate?"*

This is the **only** part of the memory that changes when you reuse the template in a different
organisation. The 5W2H spine, the rules and the laws are common to everyone; **the profile is the
instance**.

## How to configure it

1. Ask the particularities with [`../../C_OPERATIONAL_KIT/_SKILLS/CONFIG_QUESTIONS.md`](../../C_OPERATIONAL_KIT/_SKILLS/CONFIG_QUESTIONS.md).
2. Copy [`_PROFILE_TEMPLATE.yaml`](_PROFILE_TEMPLATE.yaml) to `<your_org_id>.yaml`.
3. Replace every `<PLACEHOLDER>`. **Leave the `spine` and `folders` blocks untouched** — they are the
   fixed structure.
4. Mirror the consequences into the homes they belong to:
   - roles → `41_WHO_Roles` and `06_CORE_Control/ownership.yaml`;
   - closed catalogues / enums → `15_WHAT_Catalogs`;
   - 4-letter codes → `05_CORE_Glossary/CODE_CATALOG.md`;
   - logos → `C_OPERATIONAL_KIT/_RESOURCES/logos/`.

## What does NOT go here

- The structure itself (it is fixed) — it only **declares** it.
- Business content (that lives in its W home) — the profile holds **configuration**, not data.
- Secrets/credentials — those belong to the deployment's secret store, never in the memory.

> Changing organisation = rewriting **this** profile, not the structure. That is the whole point of the
> template.
