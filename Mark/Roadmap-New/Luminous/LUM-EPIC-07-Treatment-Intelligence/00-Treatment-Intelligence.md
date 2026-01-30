---
status: "Not Started"
priority: "High"
epic_id: "LUM-EPIC-07"
linear_id: "TBD"
linear_url: "TBD"
---

# EPIC-07: Treatment Intelligence

**Linear:** TBD
**Owner:** TBD
**Target:** Q3 2026 (Post-Pilot Iteration)

---

## Vision

Operators receive data-driven recommendations for treatment optimization, enabling them to maximize remediation effectiveness with existing infrastructure and extend the treatment season based on conditions rather than calendar dates.

---

## User Stories

- As a **site operator**, I can see which treatment cells are performing best under current conditions so I can route flow to maximize effectiveness
- As an **operations manager**, I can compare treatment effectiveness across different operational parameters so I can optimize our strategy
- As a **site operator**, I can record what actions I took in response to conditions so the system learns what works
- As an **environmental analyst**, I can see recommended flow rates based on historical performance so I can make informed decisions
- As an **operations manager**, I can see when temperature-based shutdown should occur instead of relying on calendar dates so I can extend the treatment season

---

## Context

The Kearl retrospective analysis demonstrated significant value from treatment optimization:
- **Seasonal Strategy**: Temperature-based shutdown (vs. calendar) enables 3 weeks additional treatment ($104k/year)
- **Spatial Routing**: Routing flow to high-performing cells yields 26% capacity increase ($78k/year)

Currently, operators make these decisions based on experience and intuition. This EPIC transforms high-frequency biosensor data into actionable recommendations that compound as more data accumulates.

---

## Dependencies

- **Blocked by:** LUM-EPIC-01 (Data Ingestion) - biosensor results must exist
- **Blocked by:** LUM-EPIC-02 Feature 2.4 (Query Services) - historical data access
- **Related:** LUM-EPIC-03 Feature 3.6 (Correlation View) - visualization of recommendations
- **Platform:** SQH-EPIC-06 (Anomaly Detection Service) - alerting infrastructure

---

## Features

- [[Feature 7.1 Treatment Performance Metrics]]
- [[Feature 7.2 Cell Routing Recommendations]]
- [[Feature 7.3 Seasonal Strategy Optimizer]]
- [[Feature 7.4 Intervention Outcome Tracking]]
- [[Feature 7.5 Prescriptive Alerts]]

---

## Data Model Overview

```
TreatmentMetric
├── cell_id
├── period_start / period_end
├── removal_efficiency
├── throughput
├── cost_per_unit
└── conditions (temperature, flow_rate)

Recommendation
├── type (routing, seasonal, intervention)
├── recommended_action
├── confidence_score
├── rationale
├── similar_events[]
├── status (pending, accepted, dismissed)
└── outcome (if tracked)

Intervention
├── operator
├── timestamp
├── action_taken
├── conditions_before
├── conditions_after (captured automatically)
├── expected_outcome
└── actual_outcome
```

---

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Recommendation acceptance rate | >50% | Accepted / Total recommendations |
| Intervention outcome improvement | Positive trend | Before vs after metrics |
| Extended treatment season | +2-3 weeks vs calendar | Actual vs calendar shutdown |
| Routing optimization lift | +15% throughput | High-performer routing vs uniform |

---

## Implementation Phases

### Phase 1: Foundation (Post-Pilot)
**Features:** 7.1, 7.4
**Focus:** Metrics and learning infrastructure

Build the metrics calculation and intervention tracking foundation. This enables data collection even before recommendations are automated.

### Phase 2: Recommendations
**Features:** 7.2, 7.3
**Focus:** Routing and seasonal intelligence

Add recommendation capabilities once sufficient historical data exists for pattern matching.

### Phase 3: Proactive
**Feature:** 7.5
**Focus:** Prescriptive alerting

Enable proactive recommendations once the feedback loop validates that recommendations improve outcomes.

---

## References

- [Squarehead Foundry Storyline](../Squarehead-Foundry-Storyline.md) - Outcome 2: Treatment Optimization
- [[../LUM-EPIC-01-Data-Ingestion/00-Data-Ingestion|LUM-EPIC-01: Data Ingestion]] - Data foundation
- [[../LUM-EPIC-03-Customer-Dashboard/00-Customer-Dashboard|LUM-EPIC-03: Customer Dashboard]] - Visualization
- [[../Squarehead/SQH-EPIC-06-AI-Services/00-AI-Services|SQH-EPIC-06: AI Services]] - Anomaly detection platform capability
