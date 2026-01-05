# EPIC-02: Data Ingestion

**Status:** 🔴 Not Started
**Priority:** Critical
**Owner:** Greg
**Target:** Q2 2026 (Before Pilot)

**Dependencies:**
- ⭐ **Foundational:** No external blockers - this EPIC enables EPIC-01 and EPIC-03
- 🔗 **Related:** EPIC-04 Feature 4.1 (field metadata flows into Feature 2.3)

---

## Business Value

The platform needs to receive and store biosensor results from the lab, link them to sample metadata from the field, and integrate contextual data for correlation analysis. This is the data foundation for everything else.

**Key Outcome:** Lab results flow into the platform and are linked to field samples with full traceability.

---

## Features

### Feature 2.1: Biosensor Results Data Model
**Status:** 🔴 Not Started
**Priority:** Critical
**Dependencies:** None (foundational)

Define the schema for storing biosensor plate reader results.

**Tasks:**
- [ ] Define data model for biosensor results
  - Sample ID (barcode)
  - Panel type (atuA, marR, 3680)
  - Raw fluorescence readings
  - Calculated NA concentration
  - Detection timestamp
  - Lab technician ID
  - QC status (pass/fail)
- [ ] Create TerminusDB schema
- [ ] Create PostgreSQL tables if needed for fast queries
- [ ] Document data dictionary

**Biosensor Panels:**
- **atuA** - Detects acyclic NAs
- **marR** - Detects complex/aromatic NAs
- **3680** - Detects classic NA structures

---

### Feature 2.2: Lab Results Upload Pipeline
**Status:** 🔴 Not Started
**Priority:** Critical
**Dependencies:** Feature 2.1 (data model must exist first)

Ingest CSV/Excel files from the plate reader.

**Tasks:**
- [ ] CSV upload API endpoint
- [ ] File validation (required columns, data types)
- [ ] Duplicate detection (prevent re-upload)
- [ ] Parse and transform to data model
- [ ] Store in database with audit trail
- [ ] Return upload status/errors to user

**Existing Patterns:** `square_head/apps/documents/` has file upload infrastructure

---

### Feature 2.3: Sample Metadata Linkage
**Status:** 🔴 Not Started
**Priority:** Critical
**Dependencies:** Feature 2.1 (data model), Feature 2.2 (results exist to link), EPIC-04 Feature 4.1 (field metadata source)

Link lab results to field sample metadata via barcode.

**Tasks:**
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

---

### Feature 2.4: Contextual Data Integration
**Status:** 🔴 Not Started
**Priority:** High
**Dependencies:** Feature 2.3 (samples must exist to attach contextual data)

Integrate external data sources for correlation analysis.

**Tasks:**
- [ ] Weather data integration
  - Environment Canada API or similar
  - Temperature, precipitation, wind
  - Historical data fetch for sample dates
- [ ] Contextual data schema in database
- [ ] Link contextual data to samples by date/location
- [ ] (Future) SCADA integration framework
- [ ] (Future) Dosing data integration

---

### Feature 2.5: Analysis Script Automation
**Status:** 🔴 Not Started
**Priority:** Medium
**Dependencies:** Feature 2.2 (upload pipeline to integrate with)

Automate the Excel-based analysis currently done manually.

**Tasks:**
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

- [Technology Requirements - Data Ingestion Section](../03-OPERATING-MODEL/03-Technology-Requirements.md)
- Existing document processing: `square_head/apps/documents/`
- CDC patterns: `square_head/apps/cdc/`
