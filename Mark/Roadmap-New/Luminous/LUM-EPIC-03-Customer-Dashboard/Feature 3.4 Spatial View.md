---
status: "Not Started"
priority: "High"
assigned: ""
dependencies:
  - "Feature 3.2"
  - "LUM-EPIC-01 Feature 1.3"
linear_id: "SQU-13"
---

# Feature 3.4: Spatial View

**Linear:** [SQU-13](https://linear.app/squarehead/issue/SQU-13)

---

## Outcome

A customer can see results organized by physical location to understand spatial patterns in NA levels.

---

## What Success Looks Like

- Customer views a list or map of sampling locations
- Each location shows current status and latest reading
- Can drill down into any location to see details
- Spatial patterns become visible (e.g., higher NA near certain areas)

---

## Scope: Owned Files

- `apps/platform_groups/luminous/ui_hints.yaml` (spatial view config)
- `apps/platform_groups/luminous/views/spatial.py`

---

## Requirements

- Location metadata (name, coordinates, site type) is displayed for each sampling point
- Results are organized and grouped by physical location
- NA levels show visual indicators (color/size) per location
- Map view shows sampling points when GPS coordinates are available (optional)
