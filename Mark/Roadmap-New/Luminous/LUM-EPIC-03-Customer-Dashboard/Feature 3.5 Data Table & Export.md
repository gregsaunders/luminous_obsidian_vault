---
status: "Not Started"
priority: "Critical"
assigned: ""
dependencies:
  - "LUM-EPIC-01 Feature 1.1"
  - "LUM-EPIC-01 Feature 1.2"
  - "LUM-EPIC-01 Feature 1.3"
linear_id: "SQU-14"
---

# Feature 3.5: Data Table & Export

**Linear:** [SQU-14](https://linear.app/squarehead/issue/SQU-14)

---

## Outcome

A customer can access raw data, filter it, and export it for their own analysis or reporting.

---

## What Success Looks Like

- Customer navigates to data table view
- Can sort and filter by any column
- Can select which columns to display
- Can export filtered results to CSV
- Exported data is complete and accurate for regulatory reporting

---

## Scope: Owned Files

- `apps/platform_groups/luminous/ui_hints.yaml` (table config)
- `apps/platform_groups/luminous/api/export.py`

---

## Requirements

- Data table supports sorting and filtering on any column
- Users can show/hide columns to customize their view
- Filtered data can be exported to CSV format
- Data can be filtered by date range
