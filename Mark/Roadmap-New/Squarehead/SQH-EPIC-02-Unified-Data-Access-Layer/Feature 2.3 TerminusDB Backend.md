---
status: "Not Started"
priority: "High"
assigned: ""
dependencies:
  - "[[Feature 2.2 Storage Backend Protocol]]"
linear_id: ""
---

# Feature 2.3: TerminusDB Backend

## Outcome

Existing TerminusDB logic extracted into a backend implementing the protocol.

## What Success Looks Like

- All existing TerminusDB operations work through new backend
- No behavior changes for existing models
- Code is cleaner with clear abstraction boundary
- Backend passes all existing tests

## Scope: Owned Files

- `apps/platform_groups/backends/terminusdb.py` - **NEW**

## Requirements

- `TerminusDBBackend` class implements `StorageBackendProtocol`
- Existing `dao.pool.get_client()` patterns are wrapped
- Tenant context uses existing `client.connect(db=tenant_id)` mechanism
- Queries use `client.query_document()` for list/search operations
- Document operations use `client.get_document()`, `insert_document()`, etc.
