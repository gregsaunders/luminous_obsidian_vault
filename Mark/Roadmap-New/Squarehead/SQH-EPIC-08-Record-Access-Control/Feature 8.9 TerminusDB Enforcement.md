---
status: "Not Started"
priority: "High"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 8.9: TerminusDB Enforcement

## Outcome

TerminusDB operations always validate team access, including Platform Group records.

## What Success Looks Like

- All TerminusDB operations require `team_id`
- Operations fail closed when context is missing
- System context allows background tasks to operate
- Access denials are logged for audit

## Scope: Owned Files

- `apps/documents/graph/operations.py` - DocumentGraphAPI
- `apps/platform_groups/record_service.py` - PlatformGroupRecordService

## Requirements

**DocumentGraphAPI:**

- `team_id` parameter is REQUIRED (not optional)
- `user_id` parameter is available for record-level checks (optional for system context)
- Operations fail closed: return None/empty if team_id is missing
- Access denials are logged for audit

**System Context (for background tasks):**

Background tasks (CDC sync, projections, scheduled jobs) run without a logged-in user. They must not break when `user_id` is None.

- `SystemContext` class represents system-level operations
- `SystemContext` bypasses ownership checks but still requires `team_id`
- Celery tasks use `SystemContext` instead of user context
- All system-context operations are logged for audit trail
- Example usage:
  ```python
  # In Celery task
  context = SystemContext(team_id=team_id, task_name="projection_sync")
  service.list(team_id=team_id, context=context)  # Bypasses ownership, respects team
  ```

**PlatformGroupRecordService:**

- `user_id` and `team_id` parameters are available on `get()`, `list()`, `search()` methods
- WOQL conditions in `list()` enforce ownership/assignment filtering:
  ```python
  # Example: Add ownership filter to WOQL query
  woql_query = WOQL().woql_and(
      WOQL().triple("v:Doc", "rdf:type", f"@schema:{model_name}"),
      WOQL().triple("v:Doc", "team_id", team_id),
      WOQL().woql_or(
          WOQL().triple("v:Doc", "owned_by", user_id),
          WOQL().triple("v:Doc", "assigned_to", user_id),
      )
  )
  ```
- WOQL conditions in `search()` enforce access filtering
- Post-fetch filtering fallback is available for complex ABAC conditions
- `list_for_user(user, team, ...)` wrapper method applies policies automatically
