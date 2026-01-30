---
status: "Not Started"
priority: "Critical"
assigned: ""
dependencies:
  - "Feature 1.0"
linear_id: "SQU-17"
---

# Feature 1.1: Biosensor Results Data Model

**Linear:** [SQU-17](https://linear.app/squarehead/issue/SQU-17)

**Used By:**
- [[../LUM-EPIC-03-Customer-Dashboard/Feature 3.2 Summary View|LUM-EPIC-03 Feature 3.2]] - Summary View
- [[../LUM-EPIC-03-Customer-Dashboard/Feature 3.3 Trend Charts|LUM-EPIC-03 Feature 3.3]] - Trend Charts
- [[../LUM-EPIC-03-Customer-Dashboard/Feature 3.5 Data Table & Export|LUM-EPIC-03 Feature 3.5]] - Data Table & Export
- [[../LUM-EPIC-04-Platform-Infrastructure/Feature 4.3 Audit Trail (Glass Box)|LUM-EPIC-04 Feature 4.3]] - Audit Trail
- [[../LUM-EPIC-04-Platform-Infrastructure/Feature 4.4 PDF Report Generation|LUM-EPIC-04 Feature 4.4]] - PDF Reports

---

## Outcome

The system can store and retrieve biosensor plate reader results with all required fields for analysis.

---

## What Success Looks Like

- A biosensor result record includes all fields needed for downstream analysis
- Data model supports all three panel types (atuA, marR, 3680)
- QC status can be tracked per result
- Data dictionary is documented for future developers

---

## Context

Biosensor panels detect different types of naphthenic acids (NAs):
- **atuA** - Detects acyclic NAs
- **marR** - Detects complex/aromatic NAs
- **3680** - Detects classic NA structures

---

## Scope: Owned Files

- `apps/platform_groups/luminous/manifest.yaml`
- `apps/platform_groups/luminous/models/`

---

## Requirements

- Data model in `manifest.yaml` includes:
  - Sample ID (barcode)
  - Panel type (atuA, marR, 3680)
  - Raw fluorescence readings
  - Calculated NA concentration
  - Detection timestamp
  - Lab technician ID
  - QC status (pass/fail)
- TerminusDB DocumentTemplate classes are defined in `models/`
- Model is registered in `manifest.yaml` models list
- Data dictionary is documented for all fields
