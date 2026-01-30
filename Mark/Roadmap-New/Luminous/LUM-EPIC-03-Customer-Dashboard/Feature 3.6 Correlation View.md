---
status: "Not Started"
priority: "High"
assigned: ""
dependencies:
  - "Feature 3.3"
  - "LUM-EPIC-01 Feature 1.4"
linear_id: "SQU-15"
---

# Feature 3.6: Correlation View

**Linear:** [SQU-15](https://linear.app/squarehead/issue/SQU-15)

---

## Outcome

An analyst can view NA levels alongside environmental factors to identify correlations and potential causes.

---

## What Success Looks Like

- Analyst views NA trend chart
- Can overlay weather data (temperature, precipitation)
- Can see if NA spikes correlate with rain events
- Insights help explain anomalies and inform operational decisions

---

## Context

The correlation capability is powered by the **Relational Context Engine** - an existing SquareHead platform feature. This feature configures and exposes that capability for the Luminous use case, rather than building correlation logic from scratch.

---

## Scope: Owned Files

- `apps/platform_groups/luminous/ui_hints.yaml` (correlation view config)
- `apps/platform_groups/luminous/views/correlation.py`

---

## Requirements

- Relational Context Engine is configured for Luminous data relationships
- Multi-axis chart displays NA levels alongside environmental factors (temperature, precipitation)
- Correlation strength is indicated visually when patterns exist
- Contextual data (weather, operational events) can be overlaid on trend charts
