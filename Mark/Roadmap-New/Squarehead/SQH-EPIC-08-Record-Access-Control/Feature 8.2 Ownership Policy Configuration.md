---
status: "Not Started"
priority: "High"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 8.2: Ownership Policy Configuration

## Outcome

Team admins can define ownership-based visibility policies that determine which records users can see based on their relationship to the record (owner, assignee, etc.).

## What Success Looks Like

- Team admins can configure one of four ownership policies
- Default behavior (TEAM_WIDE) maintains current functionality
- Policy changes take effect immediately
- Users see only records matching their policy relationship

## Scope: Owned Files

- `apps/teams/access_policies.py` - Policy definitions
- `apps/teams/models.py` - Policy storage

## Requirements

**Ownership Policy Model:**

- `OwnershipPolicy` model supports four policy types:
  - `TEAM_WIDE` - All team members see all records (current behavior, no ownership check)
  - `OWNER_ONLY` - Users see only records where `owned_by = user`
  - `ASSIGNED_ONLY` - Users see records where `owned_by = user` OR `user IN assigned_to`
  - `HIERARCHICAL` - Managers see subordinates' records (requires org hierarchy)
- Policies are attached per team (not per-Platform-Group)
- Default policy is TEAM_WIDE (maintains current behavior)

**Ownership Evaluation:**

- `OwnershipEvaluator` class evaluates ownership-based filtering
- `WOQLOwnershipFilter` builds WOQL query conditions from policy:
  ```python
  # Example: ASSIGNED_ONLY policy generates this WOQL fragment
  WOQL().woql_or(
      WOQL().triple("v:Doc", "owned_by", user_id),
      WOQL().triple("v:Doc", "assigned_to", user_id),
  )
  ```
- `QuerySetOwnershipFilter` handles Django models (PostgreSQL only)
- Ownership checks integrate with RBAC permission checks
