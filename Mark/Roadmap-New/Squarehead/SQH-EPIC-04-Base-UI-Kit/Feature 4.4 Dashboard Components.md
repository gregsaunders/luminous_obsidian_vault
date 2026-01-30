---
status: "Not Started"
priority: "High"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 4.4: Dashboard Components

## Outcome

Reusable chart and dashboard components are available for analytics views, including advanced correlation visualization for time-series data with event overlays.

## What Success Looks Like

- Developer can add line/bar/pie charts with minimal code
- Charts are responsive and handle loading states
- KPI cards display metrics consistently
- Data tables support sorting/filtering
- Analyst can view multiple data series on shared timeline with event annotations
- Correlations between metrics and events are visually apparent

## Context

These components will be used by the Luminous Customer Dashboard and other analytics views across Platform Groups. The correlation visualization requirements are driven by biosensor monitoring use cases where NA concentrations must be analyzed alongside operational events (water intake, dosing) and environmental factors (temperature, precipitation).

**Used By:**
- [[../../Luminous/LUM-EPIC-03-Customer-Dashboard/00-Customer-Dashboard|LUM-EPIC-03]] Feature 3.3 - Trend Charts
- [[../../Luminous/LUM-EPIC-03-Customer-Dashboard/00-Customer-Dashboard|LUM-EPIC-03]] Feature 3.6 - Correlation View
- [[../SQH-EPIC-10-AI-Generated-UI/00-AI-Generated-UI|SQH-EPIC-10]] Feature 10.3 - Composable UI Components

## Technology Options

| Option | Pros | Cons |
|--------|------|------|
| **fl_chart** | Pure Dart, good community, free | Limited advanced features, no multi-axis native support |
| **syncfusion_flutter_charts** | Feature-rich, multi-axis, annotations built-in | Commercial license (~$995/dev/year) |
| **graphic** | Declarative grammar of graphics, flexible | Steeper learning curve, less community |
| **Custom Canvas** | Full control, no dependencies | Significant dev effort, maintenance burden |

**Decision needed:** Evaluate options during implementation spike.

## Scope: Owned Files

- `frontend/flutter/packages/ui/lib/components/charts/`
- `frontend/flutter/packages/ui/lib/components/dashboard/`

## Requirements

**Basic Charts:**
- KPI/Stat card component displays metrics (exists: `stat_card.dart`)
- Line chart component renders time-series data
- Bar chart component displays categorical comparisons
- Pie/donut chart component shows proportional data
- All charts handle loading, empty, and error states gracefully

**Advanced Time Series:**
- Multi-axis chart supports primary and secondary Y-axes with different units
- Event annotation layer displays vertical markers with labels for operational events
- Threshold/reference lines show horizontal alert level indicators
- Correlation highlight bands shade regions showing correlation periods
- Interactive zoom/pan allows date range selection
- Unified tooltip displays all series values at hovered timestamp

**Technology Spike:**
- fl_chart is evaluated for basic charting needs
- syncfusion_flutter_charts is evaluated for advanced features
- Multi-axis chart with event annotations is prototyped
- Library recommendation is documented with trade-offs
