---
status: "Not Started"
priority: "Critical"
assigned: ""
dependencies:
  - "Feature 3.2"
  - "LUM-EPIC-01 Feature 1.1"
linear_id: "SQU-12"
---

# Feature 3.3: Trend Charts

**Linear:** [SQU-12](https://linear.app/squarehead/issue/SQU-12)

**Used By:**
- [[../LUM-EPIC-04-Platform-Infrastructure/Feature 4.4 PDF Report Generation|LUM-EPIC-04 Feature 4.4]] - PDF Reports

---

## Outcome

A customer can visualize NA levels over time to identify patterns, anomalies, and seasonal trends.

---

## What Success Looks Like

- Customer selects a location and date range
- Sees a clear time-series chart of NA levels
- Can compare different panel types (atuA, marR, 3680)
- Can export chart as image for reports

---

## Scope: Owned Files

- `apps/platform_groups/luminous/ui_hints.yaml` (chart config)
- `apps/platform_groups/luminous/views/trends.py`

---

## Requirements

- Time-series chart displays NA concentration over time
- Users can select custom date ranges for analysis
- Results can be filtered by sample location
- Results can be filtered by biosensor panel type (atuA, marR, 3680)
- Charts can be exported as images for inclusion in reports
