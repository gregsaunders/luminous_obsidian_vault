---
status: "Not Started"
priority: "High"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 8.11: Agent Tool Enforcement

## Outcome

AI agents operate under the same permission constraints as the user who initiated them.

## What Success Looks Like

- Agents cannot access data outside user's team
- Agents respect attribute-based permissions
- Permission denials are logged
- User context is propagated through all agent operations

## Context

**Current Problem:**
- Agents access data via `hybrid_search` tool without user context
- SearchService has optional team filtering that agents bypass
- HookContext has user_id but tools don't use it
- Result: Agents can see ALL tenant data regardless of user permissions

## Scope: Owned Files

- `apps/workflows/agents/base.py` - BaseAgentTask
- `apps/workflows/agents/tools/search.py` - hybrid_search tool
- `apps/platform_groups/protocols.py` - HookContext

## Requirements

**User Context Propagation:**

- `user` is required in HookContext (not optional)
- `user_permissions: set[str]` is available in HookContext (pre-computed)
- BaseAgentTask requires user in context
- User context is passed from workflow execution to agents

**Tool Permission Enforcement:**

- `@agent_permission_required(permission)` decorator is available for tools
- `hybrid_search` requires and enforces user_id + team_id
- DocumentAccessControl is built from context
- Tool calls are rejected if context is incomplete

**Testing:**

- Agents cannot access data outside user's team
- Agents respect attribute-based permissions
- Permission denials are logged
