---
status: "Not Started"
priority: "Critical"
assigned: ""
dependencies:
  - "Feature 1.1"
linear_id: "SQU-18"
---

# Feature 1.2: Lab Results Upload Pipeline

**Linear:** [SQU-18](https://linear.app/squarehead/issue/SQU-18)

**Used By:**
- [[../LUM-EPIC-03-Customer-Dashboard/Feature 3.2 Summary View|LUM-EPIC-03 Feature 3.2]] - Summary View
- [[../LUM-EPIC-03-Customer-Dashboard/Feature 3.5 Data Table & Export|LUM-EPIC-03 Feature 3.5]] - Data Table & Export
- [[../LUM-EPIC-04-Platform-Infrastructure/Feature 4.2 Notification System|LUM-EPIC-04 Feature 4.2]] - Notification System
- [[../LUM-EPIC-04-Platform-Infrastructure/Feature 4.4 PDF Report Generation|LUM-EPIC-04 Feature 4.4]] - PDF Reports
- [[../LUM-EPIC-04-Platform-Infrastructure/Feature 4.5 API Documentation|LUM-EPIC-04 Feature 4.5]] - API Documentation

---

## Outcome

Lab technician can upload plate reader export files and see results in the system within minutes.

---

## What Success Looks Like

- Technician exports CSV from plate reader
- Uploads via web interface
- Sees confirmation with row count
- If errors, gets clear message about which rows/columns failed
- Cannot accidentally re-upload same file
- Results appear in dashboard immediately

---

## Context

Currently, plate reader results are exported as CSV/Excel and manually copied into spreadsheets. This is slow and error-prone.

---

## Constraints

- Must handle files up to 10MB
- Must validate all required columns before accepting
- Must prevent duplicate uploads (same data, different filename)

---

## Platform Capabilities (Reuse)

Luminous leverages existing SquareHead infrastructure for upload validation:
- **BulkJobService** (`apps/documents/api/jobs.py`) - Error tracking, progress events
- **HTTP 207 Multi-Status** - Partial success handling pattern
- **ConsistencyRun** - Post-upload validation tracking

No new validation workflow needed - configure existing patterns for biosensor data.

---

## Scope: Owned Files

- `apps/platform_groups/luminous/api/`
- `apps/platform_groups/luminous/services/upload.py`

---

## Requirements

- PerkinElmer Victor plate reader files (.xls/.txt) are parsed natively
- CSV upload API endpoint accepts fallback formats
- File validation checks required columns and data types before import
- Duplicate detection prevents re-uploading the same data
- Data is parsed and transformed to match the data model
- Records are stored with audit trail (who uploaded, when)
- Upload status and errors are returned to the user immediately

**Reference:** `square_head/apps/documents/` has file upload infrastructure
