---
linear_id: SQU-40
linear_url: https://linear.app/squarehead/issue/SQU-40
---

# EPIC-02: Unified Data Access Layer

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

### Feature 2.1: Storage Configuration
**Status:** 🔴 Not Started
**Priority:** High

#### Outcome
Models can declare their storage backend via a `_storage` class attribute.

#### Scope: Owned Files
- `apps/platform_groups/storage.py` - **NEW**

#### Requirements

- `StorageBackend` enum defines TERMINUSDB and POSTGRESQL options
- `StorageConfig` dataclass includes:
  - `backend: StorageBackend`
  - `table_name: str | None` (for PostgreSQL)
  - `high_volume: bool` (optimization hint)
  - `partition_by: str | None` (PostgreSQL partitioning)
- Factory methods `StorageConfig.terminusdb()` and `StorageConfig.postgresql()` are available
- Default backend is TerminusDB (existing models work unchanged)

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

### Feature 2.2: Storage Backend Protocol
**Status:** 🔴 Not Started
**Priority:** High

#### Outcome
A common interface for storage backends enabling consistent CRUD operations.

#### Scope: Owned Files
- `apps/platform_groups/backends/__init__.py` - **NEW**
- `apps/platform_groups/backends/protocol.py` - **NEW**

#### Requirements

- `StorageBackendProtocol` defines methods:
  - `get(tenant_id, model_class, record_id) -> dict | None`
  - `list(tenant_id, model_class, filters, limit, skip, order_by) -> list[dict]`
  - `search(tenant_id, model_class, query, search_fields, limit) -> list[dict]`
  - `count(tenant_id, model_class, filters) -> int`
  - `create(tenant_id, model_class, data) -> dict`
  - `update(tenant_id, model_class, record_id, data) -> dict`
  - `delete(tenant_id, model_class, record_id) -> bool`
  - `batch_create(tenant_id, model_class, records) -> list[dict]`
- All methods return `dict` for consistency with existing code
- Protocol uses `@runtime_checkable` decorator

---

### Feature 2.3: TerminusDB Backend
**Status:** 🔴 Not Started
**Priority:** High

#### Outcome
Existing TerminusDB logic extracted into a backend implementing the protocol.

#### Scope: Owned Files
- `apps/platform_groups/backends/terminusdb.py` - **NEW**

#### Requirements

- `TerminusDBBackend` class implements `StorageBackendProtocol`
- Existing `dao.pool.get_client()` patterns are wrapped
- Tenant context uses existing `client.connect(db=tenant_id)` mechanism
- Queries use `client.query_document()` for list/search operations
- Document operations use `client.get_document()`, `insert_document()`, etc.

---

### Feature 2.4: PostgreSQL Backend
**Status:** 🔴 Not Started
**Priority:** High

#### Outcome
Per-tenant PostgreSQL databases with SQLAlchemy for high-volume Platform Group models.

#### Scope: Owned Files
- `apps/platform_groups/backends/postgresql.py` - **NEW**

#### Requirements

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

---

### Feature 2.5: Service Refactoring
**Status:** 🔴 Not Started
**Priority:** High

#### Outcome
`PlatformGroupRecordService` routes to appropriate backend based on model configuration.

#### Scope: Owned Files
- `apps/platform_groups/record_service.py` - Modify

#### Requirements

- `_backends` dict maps `StorageBackend` enum to implementation instances
- `_get_model_class(group_slug, model_name)` method resolves model class
- `_get_backend(model_class)` method returns appropriate backend
- CRUD methods:
  1. Load model class via loader
  2. Get backend from model's `_storage` config
  3. Delegate to backend for storage operations
  4. Existing hook invocations are preserved
  5. Existing projection triggering is preserved

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

### Feature 2.6: PostgreSQL Query Service
**Status:** 🔴 Not Started
**Priority:** Medium

#### Outcome
Advanced PostgreSQL queries for reporting and analytics (NOT part of unified CRUD).

#### Scope: Owned Files
- `apps/platform_groups/query_services/__init__.py` - **NEW**
- `apps/platform_groups/query_services/postgresql.py` - **NEW**

#### Requirements

- `PostgreSQLQueryService` class provides advanced query capabilities
- `aggregate()` method executes GROUP BY queries with metrics
- `join_query()` method executes multi-table JOINs
- `window_functions()` method supports analytics with window functions
- `raw_sql()` method executes parameterized SQL with safety checks

#### Example Usage

```python
pg_query = PostgreSQLQueryService()
summary = pg_query.aggregate("tenant-123", "lab", "AppLabResult",
    group_by=["test_type", "month"],
    metrics={"count": "COUNT(*)", "avg_value": "AVG(value)"}
)
```

---

### Feature 2.7: TerminusDB Query Service
**Status:** 🔴 Not Started
**Priority:** Medium

#### Outcome
Advanced TerminusDB queries for graph traversals (NOT part of unified CRUD).

#### Scope: Owned Files
- `apps/platform_groups/query_services/terminusdb.py` - **NEW**

#### Requirements

- `TerminusDBQueryService` class provides graph query capabilities
- `traverse()` method follows relationship paths between nodes
- `woql_query()` method executes raw WOQL queries
- `path_query()` method finds paths between two nodes
- `subgraph()` method extracts a subgraph from a root node

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

### Feature 2.8: Access Control Integration
**Status:** 🔴 Not Started
**Priority:** High (Post-Demo)
**Depends On:** [EPIC-08](SQH-EPIC-08-Record-Access-Control.md)

> **Demo Scope:** This feature is post-demo. For demo, we rely on `TeamScopedPermission` for tenant isolation. Record-level access control (RBAC, Ownership, ABAC) will be added after pilot.

#### Outcome
Access control (RBAC, Ownership, ABAC) works consistently across both backends.

#### Scope: Owned Files
- `apps/platform_groups/backends/protocol.py` - Extend
- `apps/platform_groups/backends/terminusdb.py` - Add access filtering
- `apps/platform_groups/backends/postgresql.py` - Add access filtering

#### Requirements

- Backend protocol methods accept `AccessContext` parameter
- `AccessContext` includes: user_id, team_id, permissions, attribute_conditions
- TerminusDB backend injects WOQL conditions for ownership/ABAC filtering
- PostgreSQL backend converts AccessContext to SQL WHERE clauses
- `build_access_context(user, tenant, permission)` service creates context uniformly

---

### Feature 2.9: ISON Output Formatting for AI Context
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

#### Requirements
- Query services accept `output_format` parameter (json, ison)
- ISON serializer formats tabular results compactly
- PostgreSQLQueryService supports ISON output format
- TerminusDBQueryService supports ISON output format
- Usage patterns for AI context injection are documented

#### References
- [ISON Official Site](https://www.ison.dev/)
- [ISON GitHub](https://github.com/maheshvaikri-code/ison)

---

### Feature 2.10: Shared Reference Database
**Linear:** TBD
**Status:** 🔴 Not Started
**Priority:** Medium (Post-Demo)
**Required By:** [LUM-EPIC-02](../Luminous/LUM-EPIC-02-Unified-Water-Quality-Data-Model.md) - Water Quality Data Model (post-demo)

> **Demo Scope:** This feature is post-demo. For demo, water quality reference data can live in tenant database. Shared reference database pattern enables cross-tenant public data but is not required for pilot.

#### Outcome
Platform Group models can be stored in a shared reference database accessible by all tenants for public/common data, avoiding duplication of large datasets across per-tenant databases.

#### Rationale
Some data is inherently shared across all tenants:
- **Water quality reference data**: 6M+ measurements from federal/provincial sources (public)
- **Regulatory thresholds**: CCME guidelines, provincial standards
- **Geographic reference data**: Watershed boundaries, station networks

Duplicating this data per-tenant wastes storage and creates synchronization complexity.

#### What Success Looks Like
- Model declares `_storage = StorageConfig.postgresql(shared=True)`
- Data lives in `sqh_shared_reference` database (not per-tenant)
- All tenants can read shared data via standard query services
- Only admin users can write to shared reference data
- Queries can JOIN shared reference data with tenant-specific data

#### Architecture
```
┌─────────────────────────────────────────────────────────────────────┐
│                    PlatformGroupRecordService                        │
└─────────────────────┬───────────────────────────────────────────────┘
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Per-Tenant   │ │ Per-Tenant   │ │ Shared       │
│ TerminusDB   │ │ PostgreSQL   │ │ PostgreSQL   │
│              │ │ sqh_tenant_* │ │ sqh_shared_  │
│              │ │              │ │ reference    │
└──────────────┘ └──────────────┘ └──────────────┘
                                         │
                                         ▼
                                  Read: All tenants
                                  Write: Admin only
```

#### Scope: Owned Files
- `apps/platform_groups/storage.py` - Extend StorageConfig
- `apps/platform_groups/backends/postgresql.py` - Add shared DB routing

#### Requirements

**StorageConfig Extension:**
- `StorageConfig.postgresql()` accepts `shared: bool = False` parameter
- `SHARED_REFERENCE_DB_NAME = "sqh_shared_reference"` constant is defined
- Validation enforces `shared=True` only for `StorageBackend.POSTGRESQL`

**Database Routing:**
- `TenantDatabaseManager.get_engine()` returns shared engine when `shared=True`
- Shared database is created during platform initialization (not per-tenant)
- Connection pool is shared across all tenants for reference DB

**Access Control:**
- All authenticated users can read shared data (tenant context not required)
- Write operations require `shared_reference:write` permission (admin only)
- AccessContext includes `is_shared_reference` flag for permission checks

**Cross-Database Queries:**
- `PostgreSQLQueryService.join_shared()` JOINs tenant data with shared reference
- Implementation uses PostgreSQL foreign data wrapper or application-level join
- Performance implications of cross-DB queries are documented

**Extensions for Shared DB:**
- `ensure_shared_database_exists()` creates shared DB with required extensions
- PostGIS extension is enabled for spatial queries on shared reference data
- pg_trgm extension is enabled for fuzzy text search on parameter names

#### Model Declaration Example

```python
from apps.platform_groups.storage import StorageConfig

# Shared reference data - accessible by all tenants
class AppWaterQualityStation(DocumentTemplate):
    _storage = StorageConfig.postgresql(
        shared=True,           # Lives in sqh_shared_reference
        partition_by=None,     # No partitioning for reference data
    )
    station_code: str
    name: str
    latitude: float
    longitude: float
    ...

# Per-tenant data - isolated per customer
class AppTenantSampleAnnotation(DocumentTemplate):
    _storage = StorageConfig.postgresql(
        shared=False,          # Lives in sqh_tenant_{slug}
        high_volume=True,
    )
    station_id: str           # References shared station
    tenant_notes: str
    ...
```

#### Query Example

```python
pg_query = PostgreSQLQueryService()

# Query shared reference data (no tenant context needed)
stations = pg_query.list_shared("water-quality", "AppWaterQualityStation",
    filters={"water_body": "Athabasca River"}
)

# Join tenant annotations with shared stations
annotated = pg_query.join_shared("tenant-123",
    tenant_model=("water-quality", "AppTenantSampleAnnotation"),
    shared_model=("water-quality", "AppWaterQualityStation"),
    join_on="station_id",
    select=["station.name", "annotation.tenant_notes"]
)
```

---

## Implementation Order

| Phase | Features | Rationale |
|-------|----------|-----------|
| **Phase 1** | 2.1, 2.2 | Foundation: StorageConfig + Protocol |
| **Phase 2** | 2.3 | Extract existing TerminusDB logic |
| **Phase 3** | 2.4 | Add PostgreSQL backend (with PostGIS support) |
| **Phase 4** | 2.5 | Refactor service to route by backend |
| **Phase 5** | 2.6, 2.7 | Backend-specific query services |
| **Phase 6** | 2.8 | Access control integration (with EPIC-04) |
| **Phase 7** | 2.9 | ISON formatting for AI context (optional) |
| **Phase 8** | 2.10 | Shared reference database for cross-tenant public data |

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
- [EPIC-03](SQH-EPIC-03-Platform-Groups.md) - Platform Group framework (complete)

**Related To:**
- [EPIC-08](SQH-EPIC-08-Record-Access-Control.md) - Access control integration (Feature 2.8)

**Used By:**
- [SQH-EPIC-01](SQH-EPIC-01-MCP-Server.md) - MCP Server Feature 1.7 (Platform Group Tools need to query PostgreSQL-backed groups)
- [LUM-EPIC-01](../Luminous/LUM-EPIC-01-Data-Ingestion.md) - Luminous lab results (PostgreSQL backend)
- [LUM-EPIC-02](../Luminous/LUM-EPIC-02-Unified-Water-Quality-Data-Model.md) - Water quality data model (shared reference DB, PostGIS)

---

## References

- `apps/platform_groups/record_service.py` - Current service to refactor
- `apps/platform_groups/protocols.py` - Existing protocol patterns
- `apps/documents/graph/dao.py` - TerminusDB patterns to wrap
- `apps/platform_groups/hooks.py` - Hook system (unchanged)
- `apps/platform_groups/loader.py` - Model loading
