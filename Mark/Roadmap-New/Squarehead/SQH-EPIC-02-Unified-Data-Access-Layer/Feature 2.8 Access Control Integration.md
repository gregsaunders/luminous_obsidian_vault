---
status: "Not Started"
priority: "High"
assigned: ""
dependencies:
  - "[[Feature 2.3 TerminusDB Backend]]"
  - "[[Feature 2.4 PostgreSQL Backend]]"
  - "[[../SQH-EPIC-08-Record-Access-Control/00-Record-Access-Control|SQH-EPIC-08]]"
linear_id: ""
---

# Feature 2.8: Access Control Integration

> **Demo Scope:** This feature is post-demo. For demo, we rely on `TeamScopedPermission` for tenant isolation. Record-level access control (RBAC, Ownership, ABAC) will be added after pilot.

## Outcome

Access control (RBAC, Ownership, ABAC) works consistently across both backends.

## What Success Looks Like

- Access rules apply identically regardless of storage backend
- TerminusDB queries inject WOQL conditions
- PostgreSQL queries inject WHERE clauses
- AccessContext is created uniformly

## Scope: Owned Files

- `apps/platform_groups/backends/protocol.py` - Extend
- `apps/platform_groups/backends/terminusdb.py` - Add access filtering
- `apps/platform_groups/backends/postgresql.py` - Add access filtering

## Requirements

- Backend protocol methods accept `AccessContext` parameter
- `AccessContext` includes: user_id, team_id, permissions, attribute_conditions
- TerminusDB backend injects WOQL conditions for ownership/ABAC filtering
- PostgreSQL backend converts AccessContext to SQL WHERE clauses
- `build_access_context(user, tenant, permission)` service creates context uniformly
