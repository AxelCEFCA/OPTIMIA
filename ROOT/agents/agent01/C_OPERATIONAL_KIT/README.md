# C_OPERATIONAL_KIT - agent operational kit [agent01]

> My own operating kit. Same four parts as the shared `C_OPERATIONAL_KIT`, at my scale.
> Model: **inherit the shared kit by default, extend it with what is mine.**

- `_SKILLS/`    - my specialised skills (built from the shared defaults for my scope).
- `_TOOLS/`     - my own scripts; by default I reuse `shared/C_OPERATIONAL_KIT/_TOOLS`.
- `_RESOURCES/` - my own assets; by default I reference `shared/C_OPERATIONAL_KIT/_RESOURCES`.
- `_SERVICES/`  - the services (skills / MCP) I have available and am subscribed to.

**Rule:** I never duplicate the shared kit; I point to it and only add what is specific to me.
Capability resolution is **agent-first, then shared**: if a skill/tool/service exists here it wins; otherwise I fall back to the shared kit.

**Status.** Skeleton only in the template.
