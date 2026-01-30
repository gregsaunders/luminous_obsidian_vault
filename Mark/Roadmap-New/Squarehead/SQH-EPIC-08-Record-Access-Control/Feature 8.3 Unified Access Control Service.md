---
status: "Not Started"
priority: "High"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 8.3: Unified Access Control Service

## Outcome

A centralized service that combines RBAC, Ownership, and ABAC checks across all storage systems.

## What Success Looks Like

- Single service handles all access control decisions
- Consistent behavior across storage backends
- Performance is optimized with caching
- Clear API for permission checks and record filtering

## Scope: Owned Files

- `apps/documents/access_control.py` - **CREATE** new file

## Requirements

- `AccessControlService` class holds user + team context
- `check_access(user, permission, record)` performs combined RBAC + Ownership + ABAC check
- `filter_records(records, user, permission)` provides batch filtering for lists
- Service integrates with `OwnershipPolicy` and `AttributeCondition`
- Caching layer improves performance for permission and policy lookups
