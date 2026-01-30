---
status: "Not Started"
priority: "High"
assigned: ""
dependencies: []
linear_id: "SQU-28"
---

# Feature 5.1: Sample Metadata Capture App

**Linear:** [SQU-28](https://linear.app/squarehead/issue/SQU-28)

**Used By:**
- [[../LUM-EPIC-01-Data-Ingestion/Feature 1.3 Sample Metadata Linkage|LUM-EPIC-01 Feature 1.3]] - Sample Metadata Linkage

---

## Outcome

A field technician can capture sample metadata on a mobile device at collection time, even without internet connectivity.

---

## What Success Looks Like

- Technician arrives at sampling site
- Opens app, scans barcode on sample container
- App auto-captures GPS and timestamp
- Technician fills in location name, conditions
- Data syncs to platform when connectivity restored
- Metadata appears linked to sample in dashboard

---

## Context

MVP uses Fulcrum (off-the-shelf). Future may use custom Flutter app.

---

## Constraints

- Must work offline (field sites often have no connectivity)
- Must support barcode scanning
- Must auto-capture GPS coordinates

---

## Scope: Owned Files

- `apps/platform_groups/luminous/api/field_sync.py` (API for receiving field data)

---

## Requirements (Fulcrum approach - MVP)

- Fulcrum account is configured and accessible
- Form includes all required fields (see below)
- Barcode scanning captures sample IDs correctly
- GPS coordinates are auto-captured at collection time
- Offline mode is tested and works in areas without connectivity
- Data exports to platform API when connection is available

**Required Fields:**
- Barcode ID (scanned)
- Collection date/time
- Location name
- GPS coordinates (auto-captured)
- Collector name
- Weather conditions (dropdown)
- Sample type
- Notes (optional)
