---
status: "Not Started"
priority: "Critical"
epic_id: "LUM-EPIC-02"
linear_id: "TBD"
linear_url: "TBD"
---

# EPIC-02: Unified Water Quality Data Model

**Linear:** TBD
**Owner:** TBD
**Target:** Q2 2026 (Before Pilot)

---

## Vision

Environmental analysts can query water quality measurements across four federal/provincial data sources through a unified interface, with automatic parameter aliasing, unit normalization, and statistically rigorous detection limit handling - reducing time-to-analysis from weeks to hours.

---

## User Stories

- As a **data analyst**, I can compare phosphorus concentrations across all monitoring stations in a watershed over 10 years, regardless of which agency collected the samples
- As a **field technician**, I can submit new sample results with confidence that the system correctly maps lab codes to standard parameters
- As an **environmental manager**, I can demonstrate compliance by tracing any measurement back to its original source with full provenance
- As a **regulator**, I can verify that reported summaries accurately reflect underlying measurements, including proper handling of non-detect values

---

## Context

Environmental monitoring programs generate water quality data from diverse sources, each with their own naming conventions, units, and quality flag systems:

| Source | Characteristics | Volume |
|--------|-----------------|--------|
| Federal Mainstem | Long-term river monitoring, standardized parameters | ~2M measurements |
| Provincial Surface Water | Tributary and lake monitoring, provincial codes | ~2.5M measurements |
| Wetland Monitoring | Research-focused, specialized parameters | ~500K measurements |
| JOSM Groundwater | Joint Oil Sands Monitoring, regulatory focus | ~1M measurements |

**Key Technical Challenges:**

1. **Parameter Aliasing**: Same chemical has different codes across agencies (e.g., TP, T-P, PHOSPHORUS_TOTAL)
2. **Unit Normalization**: Measurements arrive in mg/L, ug/L, ppm, ppb
3. **Detection Limits**: ~15% of measurements are "non-detects" requiring specialized statistical handling
4. **Quality Flags**: Each source uses different flag systems to indicate sample integrity
5. **Volume**: 6M+ measurements require PostgreSQL-specific optimizations (partitioning, indexing)

### Architectural Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| **Data Tenancy** | Shared Reference DB | 6M+ public records live in shared database, not duplicated per-tenant |
| **Spatial Queries** | PostGIS | GiST indexes for station location queries |
| **Bulk Loading** | PostgreSQL COPY | Standard ORM too slow for 6M rows |
| **AI Integration** | ISON formatting | Efficient LLM context for query results |

**Reference:** [v2-Luminous-Unified-Water-Quality-Data-Model.md](../../Research/v2-Luminous-Unified-Water-Quality-Data-Model.md)

---

## Dependencies

- **Blocking:** [[../Squarehead/SQH-EPIC-02-Unified-Data-Access-Layer/00-Unified-Data-Access-Layer|SQH-EPIC-02 Unified Data Access Layer]] - PostgreSQL backend (F2.1, F2.4)
- **Related:** [[../LUM-EPIC-03-Customer-Dashboard/00-Customer-Dashboard|LUM-EPIC-03 Customer Dashboard]] - embedded widget integration (post-demo)
- **Related:** [[../LUM-EPIC-01-Data-Ingestion/00-Data-Ingestion|LUM-EPIC-01 Data Ingestion]] - ETL patterns reference
- **Platform (Post-Demo):** [[../Squarehead/SQH-EPIC-04-Base-UI-Kit/Feature 4.8 Map Component|SQH-EPIC-04 Feature 4.8]] - Map Component for station visualization
- **Platform (Post-Demo):** [[../Squarehead/SQH-EPIC-04-Base-UI-Kit/00-Base-UI-Kit|SQH-EPIC-04 Features 4.4, 4.7]] - chart widgets and data tables

> **Demo Scope:** For the Q2 demo, water quality data lives in the **tenant database** (not shared reference DB). Claude Cowork generates visualizations via MCP artifacts. The Shared Reference Database pattern (SQH-02 F2.10) and UI Kit (SQH-04) are post-demo scope.

---

## Features

- [[Feature 2.0 Core Data Model (PostgreSQL Schema)]]
- [[Feature 2.1 Parameter Aliasing & Unit Normalization]]
- [[Feature 2.2 Detection Limit Handling]]
- [[Feature 2.3 ETL Pipelines (4 Data Sources)]]
- [[Feature 2.4 Query Services & Time-Series Analysis]]
- [[Feature 2.5 Quality Flag Interpretation]]
- [[Feature 2.6 Water Quality Dashboard Views]]

---

## Implementation Phases

### Phase 1: Foundation
**Features:** 2.0, 2.1
**Focus:** Schema + aliasing

Establish the PostgreSQL schema and parameter aliasing system. Enables schema validation and performance testing with synthetic data.

**Exit Criteria:**
- Schema deployed to development environment
- Multi-tenant shared reference DB access verified
- Parameter alias API functional
- Basic query performance benchmarks established

### Phase 2: Data Loading
**Features:** 2.3
**Focus:** ETL pipelines

Build ETL pipelines starting with Federal Mainstem (most standardized), then progressively add sources.

**Exit Criteria:**
- All four sources successfully loaded to development
- Validation reports show <1% quarantine rate
- Incremental load tested with simulated updates
- Initial 6M row load completes in <1 hour

### Phase 3: Query Services
**Features:** 2.2, 2.4
**Focus:** Detection limits + queries

Implement query service layer with detection limit handling. Real data enables meaningful performance optimization.

**Exit Criteria:**
- All query endpoints functional
- Performance targets met with production-scale data
- Detection limit methods validated against known datasets
- ISON formatting verified with AI agent tests

### Phase 4: Integration
**Features:** 2.5, 2.6
**Focus:** Flags + dashboard views

Add quality flag interpretation and integrate with dashboard. Focus on user experience refinement.

**Exit Criteria:**
- Dashboard widgets rendering water quality data
- Quality flags displayed with interpretations
- Embedded widget functional in Customer Dashboard
- User acceptance testing complete

---

## Data Flow Diagram

```
Data Sources                    ETL Layer                     Unified Model
─────────────                   ─────────                     ─────────────
Federal API        →  federal.py   →  ┐
Provincial CSV     →  provincial.py →  ├──→  Station
Wetland Export     →  wetland.py   →  │     SampleEvent
JOSM Submission    →  josm.py      →  ┘     Measurement
                                              ↓
                        ┌─────────────────────┼─────────────────────┐
                        ↓                     ↓                     ↓
                   Query Services      Dashboard Views         AI Agents
                   (time-series,       (maps, charts,         (ISON format)
                    statistics)         tables)
```

---

## Platform Dependencies

This epic requires updates to other epics before full implementation:

| Epic | Required Update | Status |
|------|-----------------|--------|
| SQH-EPIC-02 | Add "Shared Reference Database" pattern for cross-tenant public data | Pending |
| SQH-EPIC-02 | Ensure PostGIS extension activation in database provisioning | Pending |
| SQH-EPIC-04 | Map Component (Feature 4.8) for station visualization | Added |

---

## Open Questions

These questions should be resolved when developers are assigned to this epic:

### Data Refresh & Synchronization
1. **ETL refresh frequency** - Is this a one-time historical load or ongoing sync with federal/provincial sources? What is the refresh cadence?
2. **Source update detection** - How do we detect when source datasets are updated? Pull-based polling or notification-based?
3. **Retroactive corrections** - How do we handle corrections to historical data from source agencies?

### Parameter Governance
4. **Parameter alias governance** - Who approves new mappings when unknown parameter codes appear? What is the review workflow?
5. **Alias confidence thresholds** - At what confidence level do we auto-approve vs require human review?
6. **New parameter discovery** - What happens when a completely new parameter appears that has no canonical mapping?

### Statistical Methods
7. **Detection limit method selection** - Who decides which statistical method (DL/2, Kaplan-Meier, etc.) for regulatory reports? Is it configurable per-report or system-wide default?
8. **Method documentation** - How do we document which method was used for audit/reproducibility purposes?

### Data Quality
9. **Cross-source validation** - How do we handle conflicting measurements from different sources at the same station/time?
10. **Quality flag harmonization** - When sources use different severity classifications, who decides the mapping?

### Performance
11. **Query performance benchmarks** - What are the acceptable latency targets for different query types (time-series, cross-station, aggregations)?
12. **Partitioning strategy validation** - How do we validate that yearly partitioning is the right choice vs monthly or by data source?

### Database Architecture
13. **Shared Reference DB vs Tenant DB** - Should water quality data live in a shared reference database (cross-tenant, single copy of public data) or tenant database (per-tenant copy)? For demo, tenant DB is acceptable. Evaluate trade-offs during implementation:
    - Shared: Single source of truth, no duplication, but requires F2.10 infrastructure
    - Tenant: Simpler isolation, works with current infrastructure, but data duplication
14. **ETL database portability** - Validate that ETL pipelines work identically against both database types via StorageConfig abstraction. ETL code must not hard-code database targets.

---

## References

- [v2-Luminous-Unified-Water-Quality-Data-Model.md](../../Research/v2-Luminous-Unified-Water-Quality-Data-Model.md) - Data model research
- [v1-Unified-Water-Quality-Data-Model.md](../../Research/v1-Unified-Water-Quality-Data-Model.md) - Initial analysis
- [[../Squarehead/SQH-EPIC-02-Unified-Data-Access-Layer/00-Unified-Data-Access-Layer|SQH-EPIC-02-Unified-Data-Access-Layer]] - PostgreSQL backend
- [[../Squarehead/SQH-EPIC-04-Base-UI-Kit/00-Base-UI-Kit|SQH-EPIC-04-Base-UI-Kit]] - Platform UI components
- CRM Reference Implementation: `square_head/apps/platform_groups/crm/`
