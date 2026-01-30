---
status: "Not Started"
priority: "Medium"
assigned: ""
dependencies:
  - "[[Feature 2.4 PostgreSQL Backend]]"
linear_id: ""
---

# Feature 2.10: Shared Reference Database

> **Demo Scope:** This feature is post-demo. For demo, water quality reference data can live in tenant database. Shared reference database pattern enables cross-tenant public data but is not required for pilot.

**Required By:** [[../../Luminous/LUM-EPIC-02-Unified-Water-Quality-Data-Model/00-Unified-Water-Quality-Data-Model|LUM-EPIC-02]] - Water Quality Data Model (post-demo)

## Outcome

Platform Group models can be stored in a shared reference database accessible by all tenants for public/common data, avoiding duplication of large datasets across per-tenant databases.

## What Success Looks Like

- Model declares `_storage = StorageConfig.postgresql(shared=True)`
- Data lives in `sqh_shared_reference` database (not per-tenant)
- All tenants can read shared data via standard query services
- Only admin users can write to shared reference data
- Queries can JOIN shared reference data with tenant-specific data

## Context

Some data is inherently shared across all tenants:
- **Water quality reference data**: 6M+ measurements from federal/provincial sources (public)
- **Regulatory thresholds**: CCME guidelines, provincial standards
- **Geographic reference data**: Watershed boundaries, station networks

Duplicating this data per-tenant wastes storage and creates synchronization complexity.

## Architecture

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

## Scope: Owned Files

- `apps/platform_groups/storage.py` - Extend StorageConfig
- `apps/platform_groups/backends/postgresql.py` - Add shared DB routing

## Requirements

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

## Model Declaration Example

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

## Query Example

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
