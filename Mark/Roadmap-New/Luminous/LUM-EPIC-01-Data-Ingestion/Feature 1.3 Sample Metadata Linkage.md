---
status: "Not Started"
priority: "Critical"
assigned: ""
dependencies:
  - "Feature 1.1"
  - "Feature 1.2"
  - "LUM-EPIC-05 Feature 5.1"
linear_id: "SQU-19"
---

# Feature 1.3: Sample Metadata Linkage

**Linear:** [SQU-19](https://linear.app/squarehead/issue/SQU-19)

**Used By:**
- [[../LUM-EPIC-03-Customer-Dashboard/Feature 3.2 Summary View|LUM-EPIC-03 Feature 3.2]] - Summary View
- [[../LUM-EPIC-03-Customer-Dashboard/Feature 3.4 Spatial View|LUM-EPIC-03 Feature 3.4]] - Spatial View
- [[../LUM-EPIC-03-Customer-Dashboard/Feature 3.5 Data Table & Export|LUM-EPIC-03 Feature 3.5]] - Data Table & Export
- [[../LUM-EPIC-04-Platform-Infrastructure/Feature 4.4 PDF Report Generation|LUM-EPIC-04 Feature 4.4]] - PDF Reports
- [[../LUM-EPIC-04-Platform-Infrastructure/Feature 4.5 API Documentation|LUM-EPIC-04 Feature 4.5]] - API Documentation

---

## Outcome

An analyst can trace any lab result back to its field collection context (who collected it, where, when, under what conditions).

---

## What Success Looks Like

- Analyst views a biosensor result
- Clicks to see linked sample metadata
- Sees collection date, location, collector, field conditions
- If no metadata linked, sees "unlinked" status with action to link
- System prevents linking to wrong barcode

---

## Context

Lab results arrive with barcode IDs. Field metadata (from EPIC-04) also has barcode IDs. This feature joins them so analysts can see the full picture.

---

## Scope: Owned Files

- `apps/platform_groups/luminous/models/sample.py`
- `apps/platform_groups/luminous/api/linkage.py`
- `apps/platform_groups/luminous/relationship_types.yaml`

---

## Requirements

- Sample metadata schema includes:
  - Barcode ID
  - Collection date/time
  - Location (name, GPS if available)
  - Collector name
  - Field conditions (weather, notes)
  - Sample type
- API endpoint accepts metadata submissions
- Barcode validation confirms barcode exists and isn't already linked
- Samples are linked to results in the database via barcode
- Orphaned results (result without sample metadata) are identified and surfaced
- Fulcrum webhook receiver endpoint processes field data automatically
- Polling fallback syncs data if webhook fails
- Sync errors are retried with appropriate backoff
- Re-synced records are detected and deduplicated
- Field updates after lab result linkage are handled with conflict resolution
