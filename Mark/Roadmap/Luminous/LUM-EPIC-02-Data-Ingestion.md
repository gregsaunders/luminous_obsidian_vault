---
linear_id: SQU-6
linear_url: https://linear.app/squarehead/issue/SQU-6/epic-02-data-ingestion
---

# EPIC-02: Data Ingestion

**Linear:** [SQU-6](https://linear.app/squarehead/issue/SQU-6)
**Status:** 🔴 Not Started
**Priority:** Critical
**Owner:** Greg
**Target:** Q2 2026 (Before Pilot)

**Dependencies:**
- ⭐ **Foundational:** This EPIC enables EPIC-01 and EPIC-03
- 🔗 **Related:** EPIC-04 Feature 4.1 (field metadata flows into Feature 2.3)
- 🔗 **Platform:** [SQH-EPIC-01 Platform Groups](../SquareHead/SQH-EPIC-01-Platform-Groups.md)

---

## Vision

Lab technicians and field operators can submit biosensor data and sample metadata into the platform, with automatic linking and traceability from field collection to lab analysis.

---

## User Stories

- As a **lab technician**, I can upload plate reader results so that data enters the system without manual data entry
- As a **field operator**, I can record sample metadata at collection time so that results are linked to their source
- As an **analyst**, I can see the complete chain from field sample to lab result so that I can trust data provenance
- As a **data manager**, I can identify orphaned or unlinked records so that data quality issues are surfaced

---

## Context

Currently, lab results are exported from plate readers as Excel files and manually processed. Field metadata is recorded on paper or in separate systems. Linking samples to results requires manual barcode matching, which is error-prone and time-consuming.

This is the data foundation - nothing else works until data flows into the platform.

---

## Features

### Feature 2.0: Luminous Platform Group Scaffolding
**Linear:** [SQU-16](https://linear.app/squarehead/issue/SQU-16)
**Status:** 🔴 Not Started
**Priority:** Critical
**Dependencies:** None (foundational - blocks all other features)

#### Outcome
A tenant administrator can install the Luminous platform group and see it available in their workspace.

#### What Success Looks Like
- Admin navigates to platform group catalog
- Selects "Luminous" and installs it
- Luminous appears in navigation
- No data yet, but structure is ready

#### Scope: Owned Files
- `apps/platform_groups/luminous/`

#### Tasks
- [ ] Create `apps/platform_groups/luminous/` directory structure
- [ ] Write initial `manifest.yaml` with core models
- [ ] Create `ui_hints.yaml` skeleton
- [ ] Create `relationship_types.yaml` for sample/result linking
- [ ] Set up `workflows/` directory for future agents
- [ ] Register Luminous in platform group catalog
- [ ] Barcode pre-registration workflow (barcodes active in system before kit shipment)
- [ ] Kit batch tracking (link barcodes to kit preparation batch)
- [ ] Luminous test fixtures (`apps/platform_groups/luminous/tests/conftest.py`)
- [ ] E2E test command (`apps/platform_groups/management/commands/e2e_luminous.py`)
- [ ] Test data seeding script (realistic sample/result data)

**Reference:** `apps/platform_groups/crm/` for structure and patterns

---

### Feature 2.1: Biosensor Results Data Model
**Linear:** [SQU-17](https://linear.app/squarehead/issue/SQU-17)
**Status:** 🔴 Not Started
**Priority:** Critical
**Dependencies:** Feature 2.0 (Platform Group scaffolding)
**Used By:**
- [LUM-EPIC-01 Feature 1.2](LUM-EPIC-01-Customer-Dashboard.md) - Summary View
- [LUM-EPIC-01 Feature 1.3](LUM-EPIC-01-Customer-Dashboard.md) - Trend Charts
- [LUM-EPIC-01 Feature 1.5](LUM-EPIC-01-Customer-Dashboard.md) - Data Table & Export
- [LUM-EPIC-03 Feature 3.3](LUM-EPIC-03-Platform-Infrastructure.md) - Audit Trail
- [LUM-EPIC-03 Feature 3.4](LUM-EPIC-03-Platform-Infrastructure.md) - PDF Reports

#### Outcome
The system can store and retrieve biosensor plate reader results with all required fields for analysis.

#### What Success Looks Like
- A biosensor result record includes all fields needed for downstream analysis
- Data model supports all three panel types (atuA, marR, 3680)
- QC status can be tracked per result
- Data dictionary is documented for future developers

#### Context
Biosensor panels detect different types of naphthenic acids (NAs):
- **atuA** - Detects acyclic NAs
- **marR** - Detects complex/aromatic NAs
- **3680** - Detects classic NA structures

#### Scope: Owned Files
- `apps/platform_groups/luminous/manifest.yaml`
- `apps/platform_groups/luminous/models/`

#### Tasks
- [ ] Define data model in `manifest.yaml`:
  - Sample ID (barcode)
  - Panel type (atuA, marR, 3680)
  - Raw fluorescence readings
  - Calculated NA concentration
  - Detection timestamp
  - Lab technician ID
  - QC status (pass/fail)
- [ ] Create TerminusDB DocumentTemplate classes in `models/`
- [ ] Add model to `manifest.yaml` models list
- [ ] Document data dictionary

---

### Feature 2.2: Lab Results Upload Pipeline
**Linear:** [SQU-18](https://linear.app/squarehead/issue/SQU-18)
**Status:** 🔴 Not Started
**Priority:** Critical
**Dependencies:** Feature 2.1 (data model must exist first)
**Used By:**
- [LUM-EPIC-01 Feature 1.2](LUM-EPIC-01-Customer-Dashboard.md) - Summary View
- [LUM-EPIC-01 Feature 1.5](LUM-EPIC-01-Customer-Dashboard.md) - Data Table & Export
- [LUM-EPIC-03 Feature 3.2](LUM-EPIC-03-Platform-Infrastructure.md) - Notification System
- [LUM-EPIC-03 Feature 3.4](LUM-EPIC-03-Platform-Infrastructure.md) - PDF Reports
- [LUM-EPIC-03 Feature 3.5](LUM-EPIC-03-Platform-Infrastructure.md) - API Documentation

#### Outcome
Lab technician can upload plate reader export files and see results in the system within minutes.

#### What Success Looks Like
- Technician exports CSV from plate reader
- Uploads via web interface
- Sees confirmation with row count
- If errors, gets clear message about which rows/columns failed
- Cannot accidentally re-upload same file
- Results appear in dashboard immediately

#### Context
Currently, plate reader results are exported as CSV/Excel and manually copied into spreadsheets. This is slow and error-prone.

#### Constraints
- Must handle files up to 10MB
- Must validate all required columns before accepting
- Must prevent duplicate uploads (same data, different filename)

#### Platform Capabilities (Reuse)
Luminous leverages existing SquareHead infrastructure for upload validation:
- **BulkJobService** (`apps/documents/api/jobs.py`) - Error tracking, progress events
- **HTTP 207 Multi-Status** - Partial success handling pattern
- **ConsistencyRun** - Post-upload validation tracking

No new validation workflow needed - configure existing patterns for biosensor data.

#### Scope: Owned Files
- `apps/platform_groups/luminous/api/`
- `apps/platform_groups/luminous/services/upload.py`

#### Tasks
- [ ] Plate reader raw file parser (PerkinElmer Victor .xls/.txt native format)
- [ ] CSV upload API endpoint (fallback for other formats)
- [ ] File validation (required columns, data types)
- [ ] Duplicate detection (prevent re-upload)
- [ ] Parse and transform to data model
- [ ] Store in database with audit trail
- [ ] Return upload status/errors to user

**Reference:** `square_head/apps/documents/` has file upload infrastructure

---

### Feature 2.3: Sample Metadata Linkage
**Linear:** [SQU-19](https://linear.app/squarehead/issue/SQU-19)
**Status:** 🔴 Not Started
**Priority:** Critical
**Dependencies:** Feature 2.1 (data model), Feature 2.2 (results exist to link), EPIC-04 Feature 4.1 (field metadata source)
**Used By:**
- [LUM-EPIC-01 Feature 1.2](LUM-EPIC-01-Customer-Dashboard.md) - Summary View
- [LUM-EPIC-01 Feature 1.4](LUM-EPIC-01-Customer-Dashboard.md) - Spatial View
- [LUM-EPIC-01 Feature 1.5](LUM-EPIC-01-Customer-Dashboard.md) - Data Table & Export
- [LUM-EPIC-03 Feature 3.4](LUM-EPIC-03-Platform-Infrastructure.md) - PDF Reports
- [LUM-EPIC-03 Feature 3.5](LUM-EPIC-03-Platform-Infrastructure.md) - API Documentation

#### Outcome
An analyst can trace any lab result back to its field collection context (who collected it, where, when, under what conditions).

#### What Success Looks Like
- Analyst views a biosensor result
- Clicks to see linked sample metadata
- Sees collection date, location, collector, field conditions
- If no metadata linked, sees "unlinked" status with action to link
- System prevents linking to wrong barcode

#### Context
Lab results arrive with barcode IDs. Field metadata (from EPIC-04) also has barcode IDs. This feature joins them so analysts can see the full picture.

#### Scope: Owned Files
- `apps/platform_groups/luminous/models/sample.py`
- `apps/platform_groups/luminous/api/linkage.py`
- `apps/platform_groups/luminous/relationship_types.yaml`

#### Tasks
- [ ] Sample metadata schema:
  - Barcode ID
  - Collection date/time
  - Location (name, GPS if available)
  - Collector name
  - Field conditions (weather, notes)
  - Sample type
- [ ] API endpoint for metadata submission
- [ ] Barcode validation (exists, not already linked)
- [ ] Link sample → result in database
- [ ] Handle orphaned results (result without sample metadata)
- [ ] Fulcrum webhook receiver endpoint
- [ ] Fulcrum sync schedule (polling fallback if webhook fails)
- [ ] Sync error handling and retry logic
- [ ] Duplicate detection for re-synced records
- [ ] Conflict resolution (field update after lab result linked)

---

### Feature 2.4: Contextual Data Integration
**Linear:** [SQU-20](https://linear.app/squarehead/issue/SQU-20)
**Status:** 🔴 Not Started
**Priority:** High
**Dependencies:** Feature 2.3 (samples must exist to attach contextual data)
**Used By:**
- [LUM-EPIC-01 Feature 1.6](LUM-EPIC-01-Customer-Dashboard.md) - Correlation View

#### Outcome
An analyst can view weather and environmental conditions alongside biosensor results to identify correlations.

#### What Success Looks Like
- Analyst views sample results
- Sees weather data for that date/location (temperature, precipitation, wind)
- Can filter or sort by weather conditions
- System automatically fetches historical weather for sample dates

#### Context
NA concentrations may correlate with weather events (rain runoff, temperature changes). Having this data alongside results enables correlation analysis.

The **Relational Context Engine** is an existing SquareHead platform capability. This feature focuses on:
1. **Ingesting** contextual data (weather, SCADA, dosing) into the platform
2. **Configuring** how that data relates to samples in the Context Engine
3. The correlation logic itself already exists - we configure it for Luminous relationships

#### Constraints
- Must work with historical data (samples may be weeks old before upload)
- Weather API rate limits and costs to consider

#### Scope: Owned Files
- `apps/platform_groups/luminous/services/weather.py`
- `apps/platform_groups/luminous/models/contextual.py`

#### Tasks
- [ ] Weather data integration
  - Environment Canada API or similar
  - Temperature, precipitation, wind
  - Historical data fetch for sample dates
- [ ] Contextual data schema in database
- [ ] Link contextual data to samples by date/location
- [ ] Auto-correlation reports (temperature vs. NA concentration, precipitation vs. toxicity)
- [ ] Pattern detection alerts (notify when significant correlation discovered)
- [ ] (Future) SCADA integration framework
- [ ] (Future) Dosing data integration

---

### Feature 2.5: Analysis Script Automation
**Linear:** [SQU-21](https://linear.app/squarehead/issue/SQU-21)
**Status:** 🔴 Not Started
**Priority:** Medium
**Dependencies:** Feature 2.2 (upload pipeline to integrate with)

#### Outcome
Lab technician uploads raw plate reader data and receives analyzed results automatically, without manual Excel processing.

#### What Success Looks Like
- Technician uploads raw fluorescence data
- System applies standard calculations (currently done in Excel)
- QC checks run automatically (flag outliers, failed controls)
- Results appear as "pass" or "needs review"
- Technician spends minutes instead of hours on analysis

#### Context
Currently, Greg runs Excel macros to transform raw fluorescence readings into NA concentrations. This is time-consuming and creates a single point of failure.

#### Scope: Owned Files
- `apps/platform_groups/luminous/services/analysis.py`
- `apps/platform_groups/luminous/services/qc.py`

#### Tasks
- [ ] Document current Excel analysis workflow
- [ ] Port calculations to Python/R
- [ ] Automated QC checks
- [ ] Validation rules before data acceptance
- [ ] Integration with upload pipeline

---

## Data Flow Diagram

```
Field                    Lab                      Platform
─────                    ───                      ────────
Sample collected    →    Sample received     →    Metadata uploaded
  ↓                        ↓                         ↓
Barcode scanned     →    Plate reader run    →    Results uploaded
  ↓                        ↓                         ↓
Metadata captured   →    CSV exported        →    Barcode linked
                                                     ↓
                                              Dashboard displays
```

---

## References

- [Technology Requirements - Data Ingestion Section](../../03-OPERATING-MODEL/03-Technology-Requirements.md)
- [Platform Groups Architecture](../SquareHead/SQH-EPIC-01-Platform-Groups.md)
- CRM manifest.yaml reference: `square_head/apps/platform_groups/crm/manifest.yaml`
- CRM PATTERNS.md: `square_head/apps/platform_groups/crm/PATTERNS.md`
- Existing document processing: `square_head/apps/documents/`
