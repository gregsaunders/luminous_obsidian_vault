---
status: "Not Started"
priority: "Medium"
assigned: ""
dependencies:
  - "Feature 2.4"
  - "SQH-EPIC-04 Feature 4.4"
  - "SQH-EPIC-04 Feature 4.7"
  - "SQH-EPIC-04 Feature 4.8"
linear_id: "TBD"
---

# Feature 2.6: Water Quality Dashboard Views

**Linear:** TBD

**Used By:**
- [[../LUM-EPIC-03-Customer-Dashboard/00-Customer-Dashboard|LUM-EPIC-03 Customer Dashboard]] - embedded widget

---

## Outcome

Environmental analysts access water quality visualizations through both an embedded Customer Dashboard widget and standalone deep-dive views.

---

## What Success Looks Like

- Customer Dashboard shows "Compare with Regional Data" widget linking biosensor results to regional context
- Analyst views display station map with color-coded data availability
- Parameter picker allows hierarchical selection by category
- Detection limit values display with distinct visual treatment
- Saved views enable reproducible analyses

---

## Context

This feature focuses on **Luminous-specific UI configuration**, not generic chart/table components (those come from SQH-EPIC-04).

### Embedded Widget (in LUM-EPIC-03 Customer Dashboard)
- "Compare with Regional Data" summary showing biosensor results vs regional averages
- Quick link to analyst views for deep-dive

### Standalone Analyst Views
- Station map with GeoJSON layer (consumes platform Map Component)
- Parameter picker with hierarchical categories (Major Ions, Trace Metals, Nutrients, etc.)
- Detection limit display conventions (symbol, color, tooltip for "<DL" values)
- Quality flag legend with severity color scheme
- Saved view definitions for common analyses

---

## Scope: Owned Files

- `apps/platform_groups/luminous/ui_hints.yaml` (water quality views)
- `frontend/flutter/packages/luminous/lib/features/water_quality/`

---

## Tasks

- [ ] Design "Compare with Regional Data" embedded widget for Customer Dashboard
- [ ] Implement station map configuration with GeoJSON data source
- [ ] Build hierarchical parameter picker component
- [ ] Define detection limit display conventions (visual treatment for "<DL")
- [ ] Create quality flag legend component with severity colors
- [ ] Implement saved view persistence (user preferences)
- [ ] Create pre-configured views: compliance, trend analysis, cross-station comparison

**NOT in scope** (use platform components from SQH-EPIC-04):
- Chart widgets (line, bar, time-series) - Feature 4.4
- Data table component - Feature 4.7
- Map component - Feature 4.8
- Export functionality - Feature 4.7
