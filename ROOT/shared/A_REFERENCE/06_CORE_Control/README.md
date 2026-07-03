# 06_CORE_Control — the machine control-plane

> **What question does it answer?** *"Who owns what, how is intake routed, what enters the RAG corpus,
> and how are moves aliased?"* This is the **executable** counterpart of `04_CORE_Governance` (which
> states the same laws in prose).

## Files

| File | Purpose | Law |
|------|---------|-----|
| `ownership.yaml` | One owner role per canonical home (single-writer). Agent self-entries + what they may propose. | P1 |
| `router_rules.yaml` | Fan-out rules applied at intake (`01_WORK_Inbox`): request type → homes generated; mints `correlation_id`. | intake |
| `rag_manifest.yaml` | What enters the retrieval corpus: `approved AND NOT superseded`, with mandatory exclusions (PII, restricted, archive, now). | RAG-EXIT |
| `PATH_ALIASES.yaml` | Migration = indirection: when a home moves, alias it here; sealed evidence is never rewritten. | P6 |

## What does NOT go here

- The laws in prose (the *why*) → `04_CORE_Governance`.
- The instance identity (name, logos, enums) → `08_CORE_Profile`.
- Secrets/credentials → the deployment secret store, never here.

> In the template these YAMLs carry generic placeholders. Filling them is part of configuration:
> replace the example roles and request types with the organisation's real ones (CONFIG blocks F and G).
