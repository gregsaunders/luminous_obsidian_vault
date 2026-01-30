---
status: "Not Started"
priority: "High"
assigned: ""
dependencies:
  - "[[Feature 2.3 TerminusDB Backend]]"
  - "[[Feature 2.4 PostgreSQL Backend]]"
linear_id: ""
---

# Feature 2.5: Service Refactoring

## Outcome

`PlatformGroupRecordService` routes to appropriate backend based on model configuration.

## What Success Looks Like

- Service automatically detects model's storage backend
- CRUD operations delegate to correct backend
- Hooks and projections work identically for both backends
- No changes required for existing code using the service

## Scope: Owned Files

- `apps/platform_groups/record_service.py` - Modify

## Requirements

- `_backends` dict maps `StorageBackend` enum to implementation instances
- `_get_model_class(group_slug, model_name)` method resolves model class
- `_get_backend(model_class)` method returns appropriate backend
- CRUD methods:
  1. Load model class via loader
  2. Get backend from model's `_storage` config
  3. Delegate to backend for storage operations
  4. Existing hook invocations are preserved
  5. Existing projection triggering is preserved

## Code Pattern

```python
class PlatformGroupRecordService:
    def __init__(self):
        self._backends = {
            StorageBackend.TERMINUSDB: TerminusDBBackend(),
            StorageBackend.POSTGRESQL: PostgreSQLBackend(),
        }

    def _get_backend(self, model_class):
        config = getattr(model_class, "_storage", StorageConfig())
        return self._backends[config.backend]

    def list(self, tenant_id, group_slug, model_name, ...):
        model_class = self._get_model_class(group_slug, model_name)
        backend = self._get_backend(model_class)
        return backend.list(tenant_id, model_class, ...)
```
