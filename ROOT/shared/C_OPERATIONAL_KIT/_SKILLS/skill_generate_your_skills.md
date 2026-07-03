# Default skill · Generate your own skills

**Goal:** that each agent, starting from this generic base, builds the set of skills **adapted to its
organisation and concrete use case**.

## The correct order (do not invert it)

1. **FIRST, ask.** Before generating any skill, gather the organisation's **particularities** with
   [`CONFIG_QUESTIONS.md`](CONFIG_QUESTIONS.md). Assume nothing: the logo, the colours, the naming, the
   output formats, the channels and the language all change from one organisation to another.
2. **Configure the profile.** Write the answers into
   [`../../A_REFERENCE/08_CORE_Profile`](../../A_REFERENCE/08_CORE_Profile/), starting from
   [`_PROFILE_TEMPLATE.yaml`](../../A_REFERENCE/08_CORE_Profile/_PROFILE_TEMPLATE.yaml). That is the only
   place that distinguishes this organisation from any other; the rest of the structure is common.
3. **Specialise the default skills.** Take `skill_use_structure.md` and `skill_official_documents.md`
   and rewrite them **making them concrete** with the profile data (the real logos, their placement, the
   document types this organisation produces, its tone…).
4. **Add use-case skills.** If the organisation has specific flows (procurement, incidents, weekly
   planning…), create one skill per flow, anchored to the real folders.
5. **Save your skills.** Generated skills live in your space:
   - if **shared** by the whole organisation → `_SKILLS/` (this folder);
   - if **yours** (your agent's) → the `_SKILLS/` of your private mirror `agents/<id>/`.

## What NOT to do

- **Do not** hard-code particularities into the common structure: they go in the **profile**.
- **Do not** duplicate: a skill references the folders and tools, it does not copy them.
- **Do not** skip step 1. The template is meant to be reused; without asking, you would be configuring
  it blind.

## Result

A **minimal, specific** set of skills: "how I use this structure in MY organisation", "how I make MY
organisation's official documents with MY logos", and one skill per own flow. All resting on this
generic base and on the profile.
