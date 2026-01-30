---
status: "Not Started"
priority: "Medium"
assigned: ""
dependencies:
  - "Feature 1.2"
linear_id: "SQU-21"
---

# Feature 1.5: Analysis Script Automation

**Linear:** [SQU-21](https://linear.app/squarehead/issue/SQU-21)

---

## Outcome

Lab technician uploads raw plate reader data and receives analyzed results automatically, without manual Excel processing.

---

## What Success Looks Like

- Technician uploads raw fluorescence data
- System applies standard calculations (currently done in Excel)
- QC checks run automatically (flag outliers, failed controls)
- Results appear as "pass" or "needs review"
- Technician spends minutes instead of hours on analysis

---

## Context

Currently, Greg runs Excel macros to transform raw fluorescence readings into NA concentrations. This is time-consuming and creates a single point of failure.

---

## Scope: Owned Files

- `apps/platform_groups/luminous/services/analysis.py`
- `apps/platform_groups/luminous/services/qc.py`

---

## Requirements

- Current Excel analysis workflow is documented for reference
- Calculations are ported from Excel macros to Python/R
- QC checks run automatically on uploaded data
- Validation rules are enforced before data is accepted
- Analysis is integrated with the upload pipeline (results processed on upload)
