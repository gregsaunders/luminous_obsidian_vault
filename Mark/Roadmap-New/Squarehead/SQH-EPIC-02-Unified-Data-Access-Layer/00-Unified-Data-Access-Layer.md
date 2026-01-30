---
status: "Not Started"
priority: "High"
epic_id: "SQH-EPIC-02"
linear_id: "SQU-40"
linear_url: "https://linear.app/squarehead/issue/SQU-40"
---

# EPIC-02: Unified Data Access Layer

## Vision

Platform Group models can declare their storage backend (TerminusDB or PostgreSQL), with unified CRUD operations, consistent access control, and backend-specific query services for advanced operations.

## User Stories

- As a **platform developer**, I can define a model that stores data in PostgreSQL for efficient reporting on millions of rows
- As a **platform developer**, I can use the same `PlatformGroupRecordService` API regardless of where data is stored
- As a **data analyst**, I can run SQL aggregations on PostgreSQL-backed models for reporting
- As a **workflow developer**, I can traverse graph relationships in TerminusDB-backed models

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

## Features

- [[Feature 2.1 Storage Configuration]]
- [[Feature 2.2 Storage Backend Protocol]]
- [[Feature 2.3 TerminusDB Backend]]
- [[Feature 2.4 PostgreSQL Backend]]
- [[Feature 2.5 Service Refactoring]]
- [[Feature 2.6 PostgreSQL Query Service]]
- [[Feature 2.7 TerminusDB Query Service]]
- [[Feature 2.8 Access Control Integration]]
- [[Feature 2.9 ISON Output Formatting]]
- [[Feature 2.10 Shared Reference Database]]

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

## Dependencies

**Depends On:**
- [[../SQH-EPIC-03-Platform-Groups/00-Platform-Groups|SQH-EPIC-03]] - Platform Group framework (complete)

**Related To:**
- [[../SQH-EPIC-08-Record-Access-Control/00-Record-Access-Control|SQH-EPIC-08]] - Access control integration (Feature 2.8)

**Used By:**
- [[../SQH-EPIC-01-MCP-Server/00-MCP-Server|SQH-EPIC-01]] - MCP Server Feature 1.7 (Platform Group Tools need to query PostgreSQL-backed groups)
- [[../../Luminous/LUM-EPIC-01-Data-Ingestion/00-Data-Ingestion|LUM-EPIC-01]] - Luminous lab results (PostgreSQL backend)
- [[../../Luminous/LUM-EPIC-02-Unified-Water-Quality-Data-Model/00-Unified-Water-Quality-Data-Model|LUM-EPIC-02]] - Water quality data model (shared reference DB, PostGIS)

## References

- `apps/platform_groups/record_service.py` - Current service to refactor
- `apps/platform_groups/protocols.py` - Existing protocol patterns
- `apps/documents/graph/dao.py` - TerminusDB patterns to wrap
- `apps/platform_groups/hooks.py` - Hook system (unchanged)
- `apps/platform_groups/loader.py` - Model loading
