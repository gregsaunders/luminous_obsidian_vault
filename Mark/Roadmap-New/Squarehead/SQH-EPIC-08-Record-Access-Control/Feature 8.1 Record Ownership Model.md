---
status: "Not Started"
priority: "High"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 8.1: Record Ownership Model

## Outcome

Every record has an owner and optional assignees, enabling ownership-based filtering.

## What Success Looks Like

- All Platform Group records have ownership fields (`created_by`, `owned_by`, `assigned_to`)
- Ownership fields are automatically populated on record creation
- Ownership can be transferred via API
- Bulk reassignment is available for organizational changes

## Context

Platform Group records are stored in TerminusDB, not Django ORM. A Django mixin cannot add fields to TerminusDB documents. Instead, ownership fields must be injected during schema loading.

## Scope: Owned Files

- `apps/platform_groups/loader.py` - Manifest loader (inject ownership fields)
- `apps/platform_groups/record_service.py` - Auto-populate created_by on create
- `apps/platform_groups/models.py` - Django mixin (for PostgreSQL models only)

## Requirements

**Schema-Level Ownership Fields:**

- Ownership fields (`created_by`, `owned_by`, `assigned_to`) are injected into `ManifestModel` objects within `loader.py` before TerminusDB schema generation
- In-memory model representation is modified after loading from `manifest.yaml`
- Ownership field types are defined in base schema (user reference fields)
- `created_by` is auto-populated in `PlatformGroupRecordService.create()` from `HookContext.user_id`
- `assigned_to` supports multiple assignees as array field
- Migration note: pre-production, no data migration needed

**Django Model Ownership (PostgreSQL-backed models only):**

- `OwnedModelMixin` provides ownership fields for Django models (CDC configs, Teams, etc.)
- This mixin is NOT used for Platform Group records

**Ownership Transfer:**

- API endpoint transfers ownership via `PlatformGroupRecordService.update()`
- Bulk ownership reassignment is available via WOQL update query
- Ownership transfer permission is checked before allowing transfer
