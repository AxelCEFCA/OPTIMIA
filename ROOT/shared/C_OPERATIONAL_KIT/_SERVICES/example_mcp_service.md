---
# ILLUSTRATIVE EXAMPLE (MCP service) - delete or replace on configuration.
id: task-manager
kind: mcp
status: planned
owner: role:operations
summary: "Read and update work items in the organisation's task manager over MCP."
transport: stdio
endpoint: "<command to launch the MCP server>"
tools: [list_tasks, get_task, update_task]
auth: api_key
scopes: [tasks:read, tasks:write]
requires_confirmation: true
implements: 36_HOW_Integrations
---

# Task manager (example MCP service)

## Purpose
Bridges the agent to the organisation's task/work-tracking system through an MCP server, so the agent can
read the queue and (with approval) update items. This is the typical shape of an `mcp` service card; a real
deployment fills the `endpoint` and the tool list from the chosen MCP server.

## How to use
Connect to the MCP server declared in the frontmatter, then call its tools. Example: to advance a ticket,
read it with `get_task`, then call `update_task` — which `requires_confirmation` (a human approves the write
before it is sent).

## Interface
| Tool | Input | Output |
|------|-------|--------|
| `list_tasks` | filter (status, assignee, …) | list of task summaries |
| `get_task` | `task_id` | the task detail |
| `update_task` | `task_id`, fields | the updated task (write — needs confirmation) |

## Auth & config
Needs an `api_key` with scopes `tasks:read`, `tasks:write`. The **key lives in the deployment secret
store**, never in this card or in the memory. Configure the launch `endpoint`/`transport` per the chosen
server.

## Limits
The authoritative source of task state is the external system (declare it in
`08_CORE_Profile.integrations`); the memory mirrors, it does not override. Writes are human-in-the-loop
(`requires_confirmation: true`). Never write to systems listed in `08_CORE_Profile.boundaries.never_write`.

## Source
An MCP server package (name + version, to be chosen). The business integration it fulfils is described in
`A_REFERENCE/36_HOW_Integrations`.
