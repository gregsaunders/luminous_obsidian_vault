---
status: "Not Started"
priority: "High"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 2.1: Storage Configuration

## Outcome

Models can declare their storage backend via a `_storage` class attribute.

## What Success Looks Like

- Developer can annotate model with `_storage = StorageConfig.postgresql()`
- Existing models without `_storage` default to TerminusDB
- Configuration options support high-volume optimization hints
- PostgreSQL partitioning can be configured

## Scope: Owned Files

- `apps/platform_groups/storage.py` - **NEW**

## Requirements

- `StorageBackend` enum defines TERMINUSDB and POSTGRESQL options
- `StorageConfig` dataclass includes:
  - `backend: StorageBackend`
  - `table_name: str | None` (for PostgreSQL)
  - `high_volume: bool` (optimization hint)
  - `partition_by: str | None` (PostgreSQL partitioning)
- Factory methods `StorageConfig.terminusdb()` and `StorageConfig.postgresql()` are available
- Default backend is TerminusDB (existing models work unchanged)

## Model Declaration Example

```python
from apps.platform_groups.storage import StorageConfig

# TerminusDB (default) - for graph relationships
class AppCRMAccount(DocumentTemplate):
    _storage = StorageConfig.terminusdb()  # Optional, this is default
    ...

# PostgreSQL - for high-volume tabular data
class AppLabResult(DocumentTemplate):
    _storage = StorageConfig.postgresql(high_volume=True, partition_by="created_at")
    ...
```
