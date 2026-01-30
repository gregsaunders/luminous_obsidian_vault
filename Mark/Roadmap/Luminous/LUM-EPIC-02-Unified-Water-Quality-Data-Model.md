---
linear_id: TBD
linear_url: TBD
---

# EPIC-02: Unified Water Quality Data Model

**Linear:** TBD
**Status:** 🔴 Not Started
**Priority:** Critical
**Owner:** TBD
**Target:** Q2 2026 (Before Pilot)

**Dependencies:**
- **Blocking:** [SQH-EPIC-02 Unified Data Access Layer](../SquareHead/SQH-EPIC-02-Unified-Data-Access-Layer.md) - PostgreSQL backend (F2.1, F2.4)
- **Related:** [LUM-EPIC-03 Customer Dashboard](LUM-EPIC-03-Customer-Dashboard.md) - embedded widget integration (post-demo)
- **Related:** [LUM-EPIC-01 Data Ingestion](LUM-EPIC-01-Data-Ingestion.md) - ETL patterns reference
- **Platform (Post-Demo):** [SQH-EPIC-04 Feature 4.8](../SquareHead/SQH-EPIC-04-Base-UI-Kit.md) - Map Component for station visualization
- **Platform (Post-Demo):** [SQH-EPIC-04 Features 4.4, 4.7](../SquareHead/SQH-EPIC-04-Base-UI-Kit.md) - chart widgets and data tables

> **Demo Scope:** For the Q2 demo, water quality data lives in the **tenant database** (not shared reference DB). Claude Cowork generates visualizations via MCP artifacts. The Shared Reference Database pattern (SQH-02 F2.10) and UI Kit (SQH-04) are post-demo scope.

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

## Features

### Feature 2.0: Core Data Model (PostgreSQL Schema)
**Linear:** TBD
**Status:** 🔴 Not Started
**Priority:** Critical
**Dependencies:** SQH-EPIC-02 (Unified Data Access Layer)

#### Outcome
A normalized, partitioned PostgreSQL schema stores 6M+ measurements with sub-second query performance, accessible to all tenants via a shared reference database.

#### What Success Looks Like
- Station, SampleEvent, Measurement tables deployed to shared reference database
- Parameter, Method, QualityFlag reference tables populated with canonical values
- Query for "all phosphorus measurements at station X in 2024" returns in <500ms
- Multi-tenant access works without data duplication

#### Context
The data model follows the universal hierarchy identified in research:

```
Station (geographic point)
  └── SampleEvent (collection at date/time/depth)
      └── Measurement (parameter value + quality metadata)
          ├── Parameter (what was measured)
          └── Method (how it was measured)
```

#### Scope: Owned Files
- `apps/platform_groups/luminous/models/water_quality/`
- Database migrations for shared reference schema

#### Tasks
- [ ] Define Django models for Station, SampleEvent, Measurement
- [ ] Define reference tables: Parameter, Method, QualityFlag
- [ ] Configure PostgreSQL table partitioning by sample_date (yearly)
- [ ] Add PostGIS extension and GiST indexes for spatial queries
- [ ] Implement JSONB column for source-specific metadata
- [ ] Configure shared reference database access (cross-tenant read)
- [ ] Set up access control: public read, admin-only write

---

### Feature 2.1: Parameter Aliasing & Unit Normalization
**Linear:** TBD
**Status:** 🔴 Not Started
**Priority:** Critical
**Dependencies:** Feature 2.0 (Core Data Model)
**Used By:**
- Feature 2.3 (ETL Pipelines) - alias resolution during import
- Feature 2.4 (Query Services) - canonical parameter lookup

#### Outcome
Source-specific parameter codes automatically resolve to canonical parameters, and units normalize to standard bases during import and query.

#### What Success Looks Like
- "Calcium Dissolved" (Wetland), "Ca" (JOSM), "Calcium (D-IC)" (Federal) all resolve to canonical "Calcium"
- Query by canonical name returns measurements from all sources
- Unit conversion handles mg/L ↔ ug/L with precision preservation
- Admin can review and approve new alias suggestions

#### Context
The four data sources use different naming conventions for the same parameters. Rather than forcing users to know source-specific codes, the system maps aliases to canonical parameters.

#### Scope: Owned Files
- `apps/platform_groups/luminous/models/water_quality/parameter_alias.py`
- `apps/platform_groups/luminous/services/aliasing.py`

#### Tasks
- [ ] Create ParameterAlias model mapping source codes to canonical parameter IDs
- [ ] Implement unit conversion registry with bidirectional rules
- [ ] Build confidence scoring for alias mappings (exact, synonym, inferred)
- [ ] Create admin interface for alias review/approval workflow
- [ ] Implement audit log for alias changes
- [ ] Seed initial alias mappings from research document tables

---

### Feature 2.2: Detection Limit Handling
**Linear:** TBD
**Status:** 🔴 Not Started
**Priority:** High
**Dependencies:** Feature 2.0 (Core Data Model)
**Used By:**
- Feature 2.4 (Query Services) - statistical calculations
- Feature 2.6 (Dashboard Views) - visual indicators

#### Outcome
Analysts can compute meaningful statistics even when 15-30% of measurements are non-detects, with clear documentation of methods used.

#### What Success Looks Like
- Query for mean concentration includes detection limit handling method in response
- User can select substitution method (DL/2, DL/sqrt(2), Kaplan-Meier) at query time
- Charts visually distinguish detect vs non-detect values
- Percentile estimates account for censoring

#### Context
Environmental data frequently contains "non-detect" values where the true concentration is below the instrument's detection limit. Statistical summaries must handle these appropriately.

#### Scope: Owned Files
- `apps/platform_groups/luminous/services/detection_limits.py`
- `apps/platform_groups/luminous/services/statistics.py`

#### Tasks
- [ ] Implement substitution methods: zero, DL/2, DL, DL/sqrt(2)
- [ ] Implement Maximum Likelihood Estimation for censored data
- [ ] Implement Kaplan-Meier estimation for highly censored datasets
- [ ] Add detection limit method parameter to query endpoints
- [ ] Tag query results with method used for transparency
- [ ] Calculate detection frequency summaries per parameter/station

---

### Feature 2.3: ETL Pipelines (4 Data Sources)
**Linear:** TBD
**Status:** 🔴 Not Started
**Priority:** Critical
**Dependencies:** Features 2.0, 2.1 (schema and aliasing must exist)

#### Outcome
Data stewards can ingest new data releases from all four sources through a consistent interface, with validation feedback and reconciliation reports.

#### What Success Looks Like
- Upload Federal Mainstem CSV → data appears in unified model within minutes
- Validation errors show specific rows/columns that failed
- Duplicate detection prevents accidental re-import
- Pipeline dashboard shows ingestion progress and error counts
- Initial 6M row load completes in reasonable time (<1 hour)

#### Context
Each data source has unique file formats and conventions:
- **Federal Mainstem**: API-based retrieval with pagination
- **Provincial Surface Water**: Annual CSV releases
- **Wetland Monitoring**: Research database exports
- **JOSM Groundwater**: Regulatory submission format

#### Scope: Owned Files
- `apps/platform_groups/luminous/etl/`
- `apps/platform_groups/luminous/etl/federal.py`
- `apps/platform_groups/luminous/etl/provincial.py`
- `apps/platform_groups/luminous/etl/wetland.py`
- `apps/platform_groups/luminous/etl/josm.py`

#### Tasks
- [ ] Create base ETL pipeline class with validation, duplicate detection, error handling
- [ ] Implement Federal Mainstem parser (wide-to-narrow transformation)
- [ ] Implement Provincial Surface Water parser
- [ ] Implement Wetland Monitoring parser
- [ ] Implement JOSM Groundwater parser
- [ ] Use PostgreSQL COPY protocol for bulk loading (6M+ rows)
- [ ] Build quarantine table for records failing validation
- [ ] Create reconciliation reports (source counts vs loaded counts)
- [ ] Implement incremental loading for delta updates
- [ ] Build pipeline status dashboard

---

### Feature 2.4: Query Services & Time-Series Analysis
**Linear:** TBD
**Status:** 🔴 Not Started
**Priority:** High
**Dependencies:** Features 2.2, 2.3 (detection limits and data must exist)
**Used By:**
- Feature 2.6 (Dashboard Views) - data source for visualizations
- SQH-EPIC-06 (AI Services) - agent queries

#### Outcome
The Luminous dashboard and AI agents can query water quality data with responsive performance for common analysis patterns.

#### What Success Looks Like
- Time-series query (single station, single parameter, 10 years) returns in <500ms
- Cross-station query (50 stations, single parameter, current year) returns in <1s
- Statistical summary includes detection limit handling
- AI agents receive ISON-formatted responses for context efficiency

#### Context
Query patterns for water quality analysis:
1. **Time-series**: Parameter values at a station over time
2. **Cross-station**: Compare values across stations at a point in time
3. **Exceedance**: Find measurements exceeding guideline thresholds
4. **Statistical**: Aggregated stats with detection limit handling

#### Scope: Owned Files
- `apps/platform_groups/luminous/api/water_quality/`
- `apps/platform_groups/luminous/services/queries.py`

#### Tasks
- [ ] Implement time-series endpoint with date range filtering
- [ ] Implement cross-station endpoint with spatial filtering
- [ ] Implement exceedance endpoint with configurable thresholds
- [ ] Implement statistical summary endpoint with detection limit methods
- [ ] Create materialized views for common aggregations (monthly means)
- [ ] Add ISON output formatting for AI agent context efficiency
- [ ] Implement query result caching with ETL-triggered invalidation
- [ ] Performance test and optimize against 6M+ row dataset

---

### Feature 2.5: Quality Flag Interpretation
**Linear:** TBD
**Status:** 🔴 Not Started
**Priority:** Medium
**Dependencies:** Feature 2.3 (data with flags must be loaded)
**Used By:**
- Feature 2.6 (Dashboard Views) - flag display and filtering

#### Outcome
Quality flags display as human-readable explanations with consistent severity categorization across all four data sources.

#### What Success Looks Like
- Hovering over a flagged value shows tooltip explaining the flag meaning
- User can filter to exclude "suspect" or "rejected" data
- Flag statistics dashboard shows data quality trends
- Cross-source flags map to common severity levels

#### Context
Each data source uses different quality flag systems:
- **Federal**: L (below MDL), R (below RL), Q + QA codes
- **Provincial/Wetland**: Lab-specific codes (I, K, T, U from AITF; H, ND, NDR from AXYS)
- **JOSM**: Standard environmental (J=estimated, U=non-detect)

#### Scope: Owned Files
- `apps/platform_groups/luminous/models/water_quality/quality_flag.py`
- `apps/platform_groups/luminous/services/flags.py`

#### Tasks
- [ ] Create QualityFlagInterpretation model with source, code, meaning, severity
- [ ] Define severity levels: informational, caution, suspect, rejected
- [ ] Seed interpretation catalog from research document tables
- [ ] Implement API endpoint returning flag meanings for display
- [ ] Add flag severity filtering to query endpoints
- [ ] Create flag statistics dashboard (data quality over time)
- [ ] Document flag harmonization decisions

---

### Feature 2.6: Water Quality Dashboard Views
**Linear:** TBD
**Status:** 🔴 Not Started
**Priority:** Medium
**Dependencies:** Feature 2.4, SQH-EPIC-04 Features 4.4 (charts), 4.7 (tables), 4.8 (map)
**Used By:**
- [LUM-EPIC-03 Customer Dashboard](LUM-EPIC-03-Customer-Dashboard.md) - embedded widget

#### Outcome
Environmental analysts access water quality visualizations through both an embedded Customer Dashboard widget and standalone deep-dive views.

#### What Success Looks Like
- Customer Dashboard shows "Compare with Regional Data" widget linking biosensor results to regional context
- Analyst views display station map with color-coded data availability
- Parameter picker allows hierarchical selection by category
- Detection limit values display with distinct visual treatment
- Saved views enable reproducible analyses

#### Context
This feature focuses on **Luminous-specific UI configuration**, not generic chart/table components (those come from SQH-EPIC-04).

#### Embedded Widget (in LUM-EPIC-03 Customer Dashboard)
- "Compare with Regional Data" summary showing biosensor results vs regional averages
- Quick link to analyst views for deep-dive

#### Standalone Analyst Views
- Station map with GeoJSON layer (consumes platform Map Component)
- Parameter picker with hierarchical categories (Major Ions, Trace Metals, Nutrients, etc.)
- Detection limit display conventions (symbol, color, tooltip for "<DL" values)
- Quality flag legend with severity color scheme
- Saved view definitions for common analyses

#### Scope: Owned Files
- `apps/platform_groups/luminous/ui_hints.yaml` (water quality views)
- `frontend/flutter/packages/luminous/lib/features/water_quality/`

#### Tasks
- [ ] Design "Compare with Regional Data" embedded widget for Customer Dashboard
- [ ] Implement station map configuration with GeoJSON data source
- [ ] Build hierarchical parameter picker component
- [ ] Define detection limit display conventions (visual treatment for "<DL")
- [ ] Create quality flag legend component with severity colors
- [ ] Implement saved view persistence (user preferences)
- [ ] Create pre-configured views: compliance, trend analysis, cross-station comparison

**NOT in scope** (use platform components from SQH-EPIC-04):
- Chart widgets (line, bar, time-series) → Feature 4.4
- Data table component → Feature 4.7
- Map component → Feature 4.8
- Export functionality → Feature 4.7

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
| SQH-EPIC-04 | Map Component (Feature 4.8) for station visualization | ✓ Added |

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
- [SQH-EPIC-02-Unified-Data-Access-Layer.md](../SquareHead/SQH-EPIC-02-Unified-Data-Access-Layer.md) - PostgreSQL backend
- [SQH-EPIC-04-Base-UI-Kit.md](../SquareHead/SQH-EPIC-04-Base-UI-Kit.md) - Platform UI components
- CRM Reference Implementation: `square_head/apps/platform_groups/crm/`
