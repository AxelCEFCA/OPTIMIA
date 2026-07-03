---
# Service card schema. Copy this file to "<service-id>.md" and fill it in.
id: "<service-id>"                 # kebab-case, unique in the registry
kind: "<skill|mcp>"                # skill = instruction body in _SKILLS ; mcp = external MCP server
status: "<available|planned|deprecated>"
owner: "role:<role>"               # who is responsible for this service
summary: "<one line: what capability this provides>"
# --- only for kind: skill ---
skill_ref: "<../_SKILLS/skill_xxx.md>"     # the instruction body this service exposes
# --- only for kind: mcp ---
transport: "<stdio|http|sse>"      # how the MCP server is reached
endpoint: "<command or URL>"       # e.g. "npx -y some-mcp-server"  or  "https://host/mcp"
tools: []                          # [tool_name, ...] the MCP server exposes
# --- common ---
auth: "<none|api_key|oauth|token>" # WHICH kind of auth (never the secret itself)
scopes: []                         # permissions this service needs
requires_confirmation: <true|false># must a human approve each call? (human-in-the-loop)
---

# <Service name>

## Purpose
<What capability this service provides, in one or two sentences, and when an agent should reach for it.>

## How to use
<For a `skill`: "follow `skill_ref`". For an `mcp`: how to connect and which tool to call for the common
task, with a concrete example call.>

## Interface
<For a `skill`: the inputs it needs and the artefact it produces. For an `mcp`: each tool with its inputs
and outputs.>

| Tool / step | Input | Output |
|-------------|-------|--------|
| `<name>` | `<...>` | `<...>` |

## Auth & config
<What credential/scope is required (named, not the value), where it is configured, and any rate limits.
Secrets live in the deployment secret store, never in this card.>

## Limits
<What it must NOT do; whether it is advise-only; `requires_confirmation` behaviour; the
public-cloud/anonymisation rule if it sends data outward.>

## Source
<Where it is defined: the `_SKILLS/…` file, or the MCP server package/repo and version. For MCP that
implements a business integration, link the matching `36_HOW_Integrations` page.>
