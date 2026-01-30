---
status: "Not Started"
priority: "High"
assigned: ""
dependencies:
  - "Feature 9.1 Technology Evaluation Spike"
  - "Feature 9.2 Storage Abstraction Layer"
linear_id: ""
---

# Feature 9.3: Auth Service Migration

## Outcome

User/group/policy management works with new storage solution.

## What Success Looks Like

- Multi-tenancy preserved (bucket-per-team isolation)
- User credentials work for their team's buckets only
- Policy enforcement is equivalent to current MinIO setup
- No regression in access control

## Scope: Owned Files

- `apps/users/minio_service.py` → `apps/users/storage_auth_service.py`
- `apps/teams/storage_provisioning.py` (new)

## Requirements

- Audit current MinIO policy patterns
- Design application-layer auth model (if Option A)
- Migrate user provisioning logic
- Migrate group/team provisioning logic
- Migrate bucket policy logic
- Update team creation signals
- Integration tests for multi-tenancy
