---
status: "Not Started"
priority: "Critical"
assigned: ""
dependencies:
  - "SQH-EPIC-02 (Unified Data Access Layer)"
linear_id: "TBD"
---

# Feature 2.0: Core Data Model (PostgreSQL Schema)

**Linear:** TBD

---

## Outcome

A normalized, partitioned PostgreSQL schema stores 6M+ measurements with sub-second query performance, accessible to all tenants via a shared reference database.

---

## What Success Looks Like

- Station, SampleEvent, Measurement tables deployed to shared reference database
- Parameter, Method, QualityFlag reference tables populated with canonical values
- Query for "all phosphorus measurements at station X in 2024" returns in <500ms
- Multi-tenant access works without data duplication

---

## Context

The data model follows the universal hierarchy identified in research:

```
Station (geographic point)
  └── SampleEvent (collection at date/time/depth)
      └── Measurement (parameter value + quality metadata)
          ├── Parameter (what was measured)
          └── Method (how it was measured)
```

---

## Scope: Owned Files

- `apps/platform_groups/luminous/models/water_quality/`
- Database migrations for shared reference schema

---

## Tasks

- [ ] Define Django models for Station, SampleEvent, Measurement
- [ ] Define reference tables: Parameter, Method, QualityFlag
- [ ] Configure PostgreSQL table partitioning by sample_date (yearly)
- [ ] Add PostGIS extension and GiST indexes for spatial queries
- [ ] Implement JSONB column for source-specific metadata
- [ ] Configure shared reference database access (cross-tenant read)
- [ ] Set up access control: public read, admin-only write
