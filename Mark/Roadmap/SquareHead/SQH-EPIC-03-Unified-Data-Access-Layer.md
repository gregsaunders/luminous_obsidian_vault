---
linear_id: SQU-40
linear_url: https://linear.app/squarehead/issue/SQU-40
---

# EPIC-03: Unified Data Access Layer

**Linear:** [SQU-40](https://linear.app/squarehead/issue/SQU-40)
**Status:** 🔴 Not Started
**Priority:** High (Prerequisite for PostgreSQL-backed Platform Group models)
**Owner:** TBD

---

## Vision

Platform Group models can declare their storage backend (TerminusDB or PostgreSQL), with unified CRUD operations, consistent access control, and backend-specific query services for advanced operations.

---

## User Stories

- As a **platform developer**, I can define a model that stores data in PostgreSQL for efficient reporting on millions of rows
- As a **platform developer**, I can use the same `PlatformGroupRecordService` API regardless of where data is stored
- As a **data analyst**, I can run SQL aggregations on PostgreSQL-backed models for reporting
- As a **workflow developer**, I can traverse graph relationships in TerminusDB-backed models

---

## Context

### Problem Statement

Currently, all Platform Group data is stored in TerminusDB. While TerminusDB excels at graph relationships and schema-typed documents, some use cases require efficient relational queries:

- **Luminous lab results**: Millions of rows, need efficient aggregations
- **Time-series data**: Need table partitioning for performance
- **Reporting**: SQL JOINs and GROUP BY are more natural than WOQL

### PostgreSQL Usage: Two Distinct Roles

SquareHead uses PostgreSQL in **two different ways**:

| PostgreSQL Role | ORM | Database | Data Type | Access Control |
|-----------------|-----|----------|-----------|----------------|
| **Platform Config** | Django ORM | Shared `confluent` DB | Users, Tenants, Teams, CDC configs, Permissions | Django QuerySet `.filter()` |
| **Customer Data** (This EPIC) | SQLAlchemy | Per-tenant `sqh_tenant_{slug}` | High-volume Platform Group models | SQL WHERE via `AccessContext` |

**Key distinction:**
- Django ORM is **only** for platform configuration—not customer/tenant business data
- Customer data in PostgreSQL uses **separate per-tenant databases** accessed via SQLAlchemy
- This EPIC adds the infrastructure to support PostgreSQL as a Platform Group storage backend

### Design Decision: Unified CRUD Only

After evaluating options, we chose to unify only basic CRUD operations:

| Approach | Pros | Cons |
|----------|------|------|
| ~~Fully Unified ORM~~ | Single API for everything | Leaky abstraction, can't expose SQL JOINs or WOQL traversals |
| **Unified CRUD Only** | Consistent basic operations, backend-specific power features | Two APIs to learn |
| ~~Completely Separate~~ | Full power of each backend | Duplicated access control, inconsistent patterns |

**Result:** Basic CRUD is unified; advanced queries use backend-specific services.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    PlatformGroupRecordService                        │
│  (Unified CRUD: get, list, search, create, update, delete)          │
└─────────────────────┬───────────────────────────────────────────────┘
                      │
        ┌─────────────┴─────────────┐
        │                           │
        ▼                           ▼
┌───────────────────┐     ┌───────────────────┐
│  TerminusDBBackend │     │ PostgreSQLBackend  │
│  (graph data)      │     │ (high-volume data) │
└─────────┬──────────┘     └─────────┬──────────┘
          │                          │
          ▼                          ▼
┌───────────────────┐     ┌───────────────────┐
│ TerminusDB        │     │ Per-Tenant        │
│ (per-tenant DB)   │     │ PostgreSQL        │
│                   │     │ sqh_tenant_{slug} │
└───────────────────┘     └───────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│            BACKEND-SPECIFIC SERVICES (Advanced Queries)              │
├─────────────────────────────┬───────────────────────────────────────┤
│   PostgreSQLQueryService    │     TerminusDBQueryService            │
│   - aggregate()             │     - traverse()                      │
│   - join_query()            │     - woql_query()                    │
│   - window_functions()      │     - path_query()                    │
│   - raw_sql()               │     - subgraph()                      │
└─────────────────────────────┴───────────────────────────────────────┘
```

---

## Features

### Feature 3.1: Storage Configuration
**Status:** 🔴 Not Started
**Priority:** High

#### Outcome
Models can declare their storage backend via a `_storage` class attribute.

#### Scope: Owned Files
- `apps/platform_groups/storage.py` - **NEW**

#### Tasks

- [ ] `StorageBackend` enum (TERMINUSDB, POSTGRESQL)
- [ ] `StorageConfig` dataclass with:
  - `backend: StorageBackend`
  - `table_name: str | None` (for PostgreSQL)
  - `high_volume: bool` (optimization hint)
  - `partition_by: str | None` (PostgreSQL partitioning)
- [ ] Factory methods: `StorageConfig.terminusdb()`, `StorageConfig.postgresql()`
- [ ] Default: TerminusDB (existing models unchanged)

#### Model Declaration Example

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

---

### Feature 3.2: Storage Backend Protocol
**Status:** 🔴 Not Started
**Priority:** High

#### Outcome
A common interface for storage backends enabling consistent CRUD operations.

#### Scope: Owned Files
- `apps/platform_groups/backends/__init__.py` - **NEW**
- `apps/platform_groups/backends/protocol.py` - **NEW**

#### Tasks

- [ ] `StorageBackendProtocol` with methods:
  - `get(tenant_id, model_class, record_id) -> dict | None`
  - `list(tenant_id, model_class, filters, limit, skip, order_by) -> list[dict]`
  - `search(tenant_id, model_class, query, search_fields, limit) -> list[dict]`
  - `count(tenant_id, model_class, filters) -> int`
  - `create(tenant_id, model_class, data) -> dict`
  - `update(tenant_id, model_class, record_id, data) -> dict`
  - `delete(tenant_id, model_class, record_id) -> bool`
  - `batch_create(tenant_id, model_class, records) -> list[dict]`
- [ ] All methods return `dict` for consistency with existing code
- [ ] Use `@runtime_checkable` for Protocol

---

### Feature 3.3: TerminusDB Backend
**Status:** 🔴 Not Started
**Priority:** High

#### Outcome
Existing TerminusDB logic extracted into a backend implementing the protocol.

#### Scope: Owned Files
- `apps/platform_groups/backends/terminusdb.py` - **NEW**

#### Tasks

- [ ] `TerminusDBBackend` class implementing `StorageBackendProtocol`
- [ ] Wrap existing `dao.pool.get_client()` patterns
- [ ] Use existing tenant context (`client.connect(db=tenant_id)`)
- [ ] Query via `client.query_document()` for list/search
- [ ] Document operations via `client.get_document()`, `insert_document()`, etc.

---

### Feature 3.4: PostgreSQL Backend
**Status:** 🔴 Not Started
**Priority:** High

#### Outcome
Per-tenant PostgreSQL databases with SQLAlchemy for high-volume Platform Group models.

#### Scope: Owned Files
- `apps/platform_groups/backends/postgresql.py` - **NEW**

#### Tasks

**Tenant Database Manager:**
- [ ] `TenantDatabaseManager` class for per-tenant connections
- [ ] Database naming: `sqh_tenant_{tenant_slug}`
- [ ] `get_engine(tenant_id)` - SQLAlchemy engine per tenant (cached)
- [ ] `ensure_database_exists(tenant_id)` - Create DB if not exists

**PostgreSQL Backend:**
- [ ] `PostgreSQLBackend` implementing `StorageBackendProtocol`
- [ ] `_get_table(tenant_id, model_class)` - Build SQLAlchemy Table from model
- [ ] Type mapping from Pydantic annotations to SQLAlchemy columns
- [ ] Lazy table creation from model definitions
- [ ] SQL operations: SELECT, INSERT, UPDATE, DELETE with parameterization

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

---

### Feature 3.5: Service Refactoring
**Status:** 🔴 Not Started
**Priority:** High

#### Outcome
`PlatformGroupRecordService` routes to appropriate backend based on model configuration.

#### Scope: Owned Files
- `apps/platform_groups/record_service.py` - Modify

#### Tasks

- [ ] Add `_backends` dict mapping `StorageBackend` -> implementation
- [ ] Add `_get_model_class(group_slug, model_name)` method
- [ ] Add `_get_backend(model_class)` method
- [ ] Update CRUD methods to:
  1. Load model class via loader
  2. Get backend from model's `_storage` config
  3. Delegate to backend
  4. Keep existing hook invocations
  5. Keep existing projection triggering

#### Code Pattern

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

---

### Feature 3.6: PostgreSQL Query Service
**Status:** 🔴 Not Started
**Priority:** Medium

#### Outcome
Advanced PostgreSQL queries for reporting and analytics (NOT part of unified CRUD).

#### Scope: Owned Files
- `apps/platform_groups/query_services/__init__.py` - **NEW**
- `apps/platform_groups/query_services/postgresql.py` - **NEW**

#### Tasks

- [ ] `PostgreSQLQueryService` class
- [ ] `aggregate(tenant_id, group_slug, model_name, group_by, metrics)` - GROUP BY queries
- [ ] `join_query(tenant_id, tables, join_conditions, select)` - Multi-table JOINs
- [ ] `window_functions(tenant_id, ...)` - Window functions for analytics
- [ ] `raw_sql(tenant_id, sql, params)` - Parameterized raw SQL (with safety checks)

#### Example Usage

```python
pg_query = PostgreSQLQueryService()
summary = pg_query.aggregate("tenant-123", "lab", "AppLabResult",
    group_by=["test_type", "month"],
    metrics={"count": "COUNT(*)", "avg_value": "AVG(value)"}
)
```

---

### Feature 3.7: TerminusDB Query Service
**Status:** 🔴 Not Started
**Priority:** Medium

#### Outcome
Advanced TerminusDB queries for graph traversals (NOT part of unified CRUD).

#### Scope: Owned Files
- `apps/platform_groups/query_services/terminusdb.py` - **NEW**

#### Tasks

- [ ] `TerminusDBQueryService` class
- [ ] `traverse(tenant_id, group_slug, model_name, start_id, path, max_depth)` - Relationship traversal
- [ ] `woql_query(tenant_id, woql)` - Raw WOQL execution
- [ ] `path_query(tenant_id, start_id, end_id)` - Find paths between nodes
- [ ] `subgraph(tenant_id, root_id, depth)` - Extract subgraph

#### Example Usage

```python
terminus_query = TerminusDBQueryService()
related = terminus_query.traverse("tenant-123", "crm", "AppCRMAccount",
    start_id="Account/acme-123",
    path="contacts/opportunities",  # Account -> Contacts -> Opportunities
    max_depth=2
)
```

---

### Feature 3.8: Access Control Integration
**Status:** 🔴 Not Started
**Priority:** High
**Depends On:** [EPIC-04](SQH-EPIC-04-Record-Access-Control.md)

#### Outcome
Access control (RBAC, Ownership, ABAC) works consistently across both backends.

#### Scope: Owned Files
- `apps/platform_groups/backends/protocol.py` - Extend
- `apps/platform_groups/backends/terminusdb.py` - Add access filtering
- `apps/platform_groups/backends/postgresql.py` - Add access filtering

#### Tasks

- [ ] Add `AccessContext` parameter to backend protocol methods
- [ ] `AccessContext` includes: user_id, team_id, permissions, attribute_conditions
- [ ] TerminusDB: Inject WOQL conditions for ownership/ABAC filtering
- [ ] PostgreSQL: Convert AccessContext to SQL WHERE clauses
- [ ] Unified `build_access_context(user, tenant, permission)` service (from EPIC-11)

---

### Feature 3.9: ISON Output Formatting for AI Context
**Linear:** [SQU-55](https://linear.app/squarehead/issue/SQU-55)
**Status:** 🔴 Not Started
**Priority:** Low

#### Outcome
Query results from PostgreSQL, TerminusDB, and hybrid search can be formatted as ISON for token-efficient injection into LLM context.

#### Rationale
- Large result sets (100s-1000s of rows) consume significant context tokens
- ISON provides 30-70% token reduction over JSON
- Tabular format aligns well with query results
- LLM reads the data; doesn't need to generate it (accuracy less critical than for output)

#### Example
```
# JSON (verbose) - 89 tokens
[{"id": "123", "name": "Acme Corp", "status": "active"}, {"id": "456", "name": "Globex", "status": "inactive"}]

# ISON (compact) - ~40 tokens
@accounts
| id  | name      | status
| 123 | Acme Corp | active
| 456 | Globex    | inactive
```

#### Scope: Owned Files
- `apps/platform_groups/query_services/formatters/__init__.py` - **NEW**
- `apps/platform_groups/query_services/formatters/ison.py` - **NEW**
- `apps/platform_groups/query_services/postgresql.py` - Extend
- `apps/platform_groups/query_services/terminusdb.py` - Extend

#### Tasks
- [ ] Add `output_format` parameter to query services (json, ison)
- [ ] Implement ISON serializer for tabular results
- [ ] Add ISON formatting to PostgreSQLQueryService
- [ ] Add ISON formatting to TerminusDBQueryService
- [ ] Document usage patterns for AI context injection

#### References
- [ISON Official Site](https://www.ison.dev/)
- [ISON GitHub](https://github.com/maheshvaikri-code/ison)

---

## Implementation Order

| Phase | Features | Rationale |
|-------|----------|-----------|
| **Phase 1** | 3.1, 3.2 | Foundation: StorageConfig + Protocol |
| **Phase 2** | 3.3 | Extract existing TerminusDB logic |
| **Phase 3** | 3.4 | Add PostgreSQL backend |
| **Phase 4** | 3.5 | Refactor service to route by backend |
| **Phase 5** | 3.6, 3.7 | Backend-specific query services |
| **Phase 6** | 3.8 | Access control integration (with EPIC-04) |
| **Phase 7** | 3.9 | ISON formatting for AI context (optional) |

Existing models continue to work without changes (default = TerminusDB).

---

## Key Files

**Storage Configuration:**
- `apps/platform_groups/storage.py` - **NEW** StorageBackend enum, StorageConfig

**Backend Layer:**
- `apps/platform_groups/backends/__init__.py` - **NEW** Package init
- `apps/platform_groups/backends/protocol.py` - **NEW** StorageBackendProtocol
- `apps/platform_groups/backends/terminusdb.py` - **NEW** TerminusDB backend
- `apps/platform_groups/backends/postgresql.py` - **NEW** PostgreSQL backend + TenantDatabaseManager

**Query Services:**
- `apps/platform_groups/query_services/__init__.py` - **NEW** Package init
- `apps/platform_groups/query_services/postgresql.py` - **NEW** SQL aggregations, JOINs
- `apps/platform_groups/query_services/terminusdb.py` - **NEW** Graph traversals, WOQL
- `apps/platform_groups/query_services/formatters/` - **NEW** Output formatters (JSON, ISON)

**Service Layer:**
- `apps/platform_groups/record_service.py` - Refactor to route by backend
- `apps/platform_groups/loader.py` - Read `_storage` attribute

---

## Key Implementation Details

### Projection Compatibility
Both backends trigger the same projection pipeline:
- Model's `_document_projection` config is read regardless of backend
- Projection fetches record from whichever backend stores it
- Same flow to Qdrant/Meilisearch for search indexing

### Hook Compatibility
Hooks work identically for both backends:
- `validate_or_raise()` - Called before create/update
- `before_create/update/delete()` - Transform data
- `after_create/update/delete()` - Side effects
- Hooks receive same `HookContext` regardless of backend

### Per-Tenant Database Provisioning
- Extend existing tenant provisioning pipeline
- Create PostgreSQL database when tenant is created
- Tables created lazily when models with `postgresql` backend are accessed
- Connection pooling: SQLAlchemy engine per tenant, cached in `TenantDatabaseManager._engines`

---

## Dependencies

**Depends On:**
- [EPIC-01](SQH-EPIC-01-Platform-Groups.md) - Platform Group framework (complete)

**Related To:**
- [EPIC-04](SQH-EPIC-04-Record-Access-Control.md) - Access control integration (Feature 3.8)

**Used By:**
- [LUM-EPIC-02](../Luminous/LUM-EPIC-02-Luminous-Platform-Group.md) - Luminous lab results (PostgreSQL backend)

---

## References

- `apps/platform_groups/record_service.py` - Current service to refactor
- `apps/platform_groups/protocols.py` - Existing protocol patterns
- `apps/documents/graph/dao.py` - TerminusDB patterns to wrap
- `apps/platform_groups/hooks.py` - Hook system (unchanged)
- `apps/platform_groups/loader.py` - Model loading
