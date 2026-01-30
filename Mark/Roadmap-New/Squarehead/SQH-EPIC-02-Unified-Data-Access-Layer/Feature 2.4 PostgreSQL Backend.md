---
status: "Not Started"
priority: "High"
assigned: ""
dependencies:
  - "[[Feature 2.2 Storage Backend Protocol]]"
linear_id: ""
---

# Feature 2.4: PostgreSQL Backend

## Outcome

Per-tenant PostgreSQL databases with SQLAlchemy for high-volume Platform Group models.

## What Success Looks Like

- Models can declare PostgreSQL storage
- Tenant databases are created automatically
- Tables are created lazily from model schemas
- CRUD operations work identically to TerminusDB backend

## Scope: Owned Files

- `apps/platform_groups/backends/postgresql.py` - **NEW**

## Requirements

**Tenant Database Manager:**
- `TenantDatabaseManager` class manages per-tenant database connections
- Databases are named `sqh_tenant_{tenant_slug}`
- `get_engine(tenant_id)` returns cached SQLAlchemy engine per tenant
- `ensure_database_exists(tenant_id)` creates database if it doesn't exist
- `ensure_extension(tenant_id, extension_name)` enables PostgreSQL extensions (e.g., PostGIS)

**PostgreSQL Backend:**
- `PostgreSQLBackend` class implements `StorageBackendProtocol`
- `_get_table(tenant_id, model_class)` builds SQLAlchemy Table from model
- Pydantic type annotations map to SQLAlchemy column types
- Tables are created lazily when models are first accessed
- SQL operations (SELECT, INSERT, UPDATE, DELETE) use parameterized queries

**Type Mapping:**

| Pydantic | SQLAlchemy |
|----------|------------|
| `str` | `String` |
| `int` | `Integer` |
| `float` | `Float` |
| `bool` | `Boolean` |
| `datetime` | `DateTime` |
| `Optional[T]` | `T` (nullable) |
| `Set[str]` | `ARRAY(String)` |
