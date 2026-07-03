# _SERVICES — the capability registry (skills & MCP)

**What this is.** A single, discoverable **catalogue of the capabilities available to the agents** of this
memory. Every entry is one **service**, described as one of two kinds:

- **`skill`** — an instruction-based capability (a procedure the agent follows). The service card points at
  the skill body in [`../_SKILLS/`](../_SKILLS/README.md).
- **`mcp`** — a **Model Context Protocol** server: an external process that exposes *tools*, *resources*
  and/or *prompts* the agent can call over MCP. The service card documents the server and its interface.

**Why it exists (and why separate from the rest of the kit).** An agent needs one place to answer *"what can
I call, and how?"*. This registry is that place. It does **not** replace the other kit folders — it indexes
them and adds the external ones:

| Folder | Answers | Relationship to `_SERVICES` |
|--------|---------|------------------------------|
| `_SKILLS/` | "how do I do this myself?" (instructions) | a `skill` service points here for its body |
| `_TOOLS/` | "what local script do I run?" | a tool may be wrapped as a `skill` service entry |
| `_SERVICES/` | **"what capabilities exist and how do I call them?"** | the unified discovery index (this folder) |
| `36_HOW_Integrations` | "how does the org connect to system X?" | an `mcp` service often *implements* one of these integrations |

So: `_SKILLS` and `_TOOLS` are *bodies*; `36_HOW_Integrations` is *business connection knowledge*;
`_SERVICES` is the **agent-facing index of callable capabilities** (local skills + remote MCP servers).

## What goes here
- One **service card** per available capability (`<service-id>.md`), following
  [`_SERVICE_TEMPLATE.md`](_SERVICE_TEMPLATE.md).
- A machine-readable registry [`services.yaml`](services.yaml) (the index an agent loads at startup).

## What does NOT go here
- The skill instructions themselves → `../_SKILLS/`.
- Local scripts → `../_TOOLS/`.
- Secrets / API keys / tokens → the deployment secret store, **never** here (cards declare *that* auth is
  needed and *which* scopes, never the credential).

## How an agent uses a service
1. **Discover.** Load `services.yaml` (or browse the cards) to see what is available and its `status`.
2. **Read the card.** It states the purpose, how to invoke it, the interface (skill steps, or MCP tools +
   inputs/outputs), the auth/config needed, the limits, and whether it `requires_confirmation`.
3. **Call it.**
   - `skill` → open and follow the referenced `_SKILLS/…` file.
   - `mcp` → connect to the declared MCP server and call its tools (respecting `requires_confirmation` and
     the human-in-the-loop and anonymisation laws in `04_CORE_Governance`).
4. **Trace.** A call that changes state or sends something leaves its evidence in `B_OPERATIONS` per the
   normal flow (e.g. an outgoing message in `02_WORK_Outbox`, evidence sealed in `03_WORK_Flow`).

## The service card schema (summary)
Frontmatter: `id`, `kind: skill|mcp`, `status: available|planned|deprecated`, `owner`, `auth`, `scopes`,
`requires_confirmation`, and for MCP `endpoint`/`transport`. Body: **Purpose · How to use · Interface ·
Auth & config · Limits · Source**. Full schema in [`_SERVICE_TEMPLATE.md`](_SERVICE_TEMPLATE.md).

## Configuring this registry (per organisation)
The template ships **empty** (one template + two illustrative example cards). During onboarding
(`CONFIG_QUESTIONS.md`, block E) register the **real** services:
- the organisation's **MCP servers** (task manager, calendar, file store, search, ticketing…), one card each;
- the **skills** the agents are allowed to use, one card each (pointing at `_SKILLS/…`).
Then list them all in `services.yaml`. Agents inherit this shared registry; an agent's own
`agents/<id>/C_OPERATIONAL_KIT/_SERVICES/` scopes it to what that agent is subscribed to / authorised for.

> Example cards in this folder (`example_skill_service.md`, `example_mcp_service.md`) are **illustrative
> placeholders** — delete or replace them when you configure the real services.
