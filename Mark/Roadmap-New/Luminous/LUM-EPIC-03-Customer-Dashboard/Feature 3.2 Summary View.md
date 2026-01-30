---
status: "Not Started"
priority: "Critical"
assigned: ""
dependencies:
  - "LUM-EPIC-01 Feature 1.1"
  - "LUM-EPIC-01 Feature 1.2"
  - "LUM-EPIC-01 Feature 1.3"
linear_id: "SQU-11"
---

# Feature 3.2: Summary View

**Linear:** [SQU-11](https://linear.app/squarehead/issue/SQU-11)

**Used By:**
- [[../LUM-EPIC-04-Platform-Infrastructure/Feature 4.4 PDF Report Generation|LUM-EPIC-04 Feature 4.4]] - PDF Reports

---

## Outcome

A customer can see an at-a-glance overview of their NA monitoring status across all sites.

---

## What Success Looks Like

- Customer logs in, immediately sees current status
- Each location shows latest reading with color-coded status (green/yellow/red)
- Can tell at a glance if any site needs attention
- Quick stats show total samples and trends

---

## Scope: Owned Files

- `apps/platform_groups/luminous/ui_hints.yaml` (summary view config)
- `apps/platform_groups/luminous/views/summary.py`

---

## Requirements

- Each sample location displays its most recent NA reading
- Status indicators show color-coded thresholds (green=normal, yellow=elevated, red=critical)
- Last sample date is visible for each location
- Summary statistics show total sample count and average NA level across all sites
