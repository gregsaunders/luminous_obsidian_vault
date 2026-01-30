---
linear_id: TBD
linear_url: TBD
---

# EPIC-07: Treatment Intelligence

**Linear:** TBD
**Status:** 🔴 Not Started
**Priority:** High
**Owner:** TBD
**Target:** Q3 2026 (Post-Pilot Iteration)

**Dependencies:**
- **Blocked by:** LUM-EPIC-01 (Data Ingestion) - biosensor results must exist
- **Blocked by:** LUM-EPIC-02 Feature 2.4 (Query Services) - historical data access
- **Related:** LUM-EPIC-03 Feature 3.6 (Correlation View) - visualization of recommendations
- **Platform:** SQH-EPIC-06 (Anomaly Detection Service) - alerting infrastructure

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

## Features

### Feature 7.1: Treatment Performance Metrics
**Linear:** TBD
**Status:** 🔴 Not Started
**Priority:** Critical
**Dependencies:** LUM-EPIC-02 Features 2.1-2.3 (data must exist to analyze)

#### Outcome
Operations managers can see treatment effectiveness metrics for each cell, enabling comparison and informed routing decisions.

#### What Success Looks Like
- Manager views dashboard showing effectiveness by cell
- Each cell displays: removal efficiency, throughput, cost per unit treated
- Can filter by time period (week, month, season)
- Can compare current performance to historical baseline
- Trends are visible - improving vs declining performance

#### Scope: Owned Files
- `apps/platform_groups/luminous/models/treatment_metrics.py`
- `apps/platform_groups/luminous/services/metrics_calculator.py`
- `apps/platform_groups/luminous/api/metrics.py`

#### Tasks
- [ ] Define treatment effectiveness metrics (removal efficiency formula, throughput calculation)
- [ ] Create TreatmentMetric model (cell, period, metrics)
- [ ] Build metrics calculation service (aggregate from biosensor results)
- [ ] Create API endpoints for metrics retrieval
- [ ] Define baseline calculation methodology
- [ ] Historical comparison logic (current vs. same period last year)

---

### Feature 7.2: Cell Routing Recommendations
**Linear:** TBD
**Status:** 🔴 Not Started
**Priority:** High
**Dependencies:** Feature 7.1 (performance metrics must exist)

#### Outcome
Operators receive recommendations for which cells to route flow to based on current conditions and historical performance.

#### What Success Looks Like
- Operator views current conditions (temperature, flow rate, recent toxicity)
- System displays recommended routing with confidence level
- Recommendation includes rationale ("Cell 3 performed 26% better under similar conditions in August 2025")
- Operator can accept, modify, or dismiss recommendation
- System tracks which recommendations were followed

#### Scope: Owned Files
- `apps/platform_groups/luminous/services/routing_recommender.py`
- `apps/platform_groups/luminous/models/recommendation.py`

#### Tasks
- [ ] Define conditions that affect cell performance (temperature, flow rate, time of year)
- [ ] Build condition-matching logic (find similar historical periods)
- [ ] Create recommendation model (recommendation, confidence, rationale, status)
- [ ] Build routing recommendation service
- [ ] API endpoint for current recommendations
- [ ] Recommendation acceptance/dismissal tracking

---

### Feature 7.3: Seasonal Strategy Optimizer
**Linear:** TBD
**Status:** 🔴 Not Started
**Priority:** High
**Dependencies:** Feature 7.1 (performance metrics), LUM-EPIC-02 Feature 2.4 (weather data)

#### Outcome
Operations managers can see temperature-based recommendations for treatment season start/end rather than relying on calendar dates.

#### What Success Looks Like
- Manager views seasonal analysis dashboard
- System shows temperature thresholds where treatment effectiveness drops
- Recommendation: "Based on current forecast, extend operation 2 weeks beyond calendar shutdown"
- Historical comparison: "Last year's early shutdown cost an estimated $X in lost treatment capacity"
- Can model scenarios: "What if we operate until temperature drops below Y?"

#### Scope: Owned Files
- `apps/platform_groups/luminous/services/seasonal_analyzer.py`
- `apps/platform_groups/luminous/models/seasonal_strategy.py`

#### Tasks
- [ ] Identify temperature thresholds from historical data (when does effectiveness drop?)
- [ ] Build seasonal analysis service
- [ ] Integrate weather forecast data for projections
- [ ] Calculate value of extended operation (days × throughput × cost)
- [ ] Create scenario modeling capability
- [ ] Seasonal recommendation generation

---

### Feature 7.4: Intervention Outcome Tracking
**Linear:** TBD
**Status:** 🔴 Not Started
**Priority:** Critical
**Dependencies:** Feature 7.2 (recommendations to track)

#### Outcome
The system learns from operator actions by tracking what interventions were made and whether they achieved the desired outcome.

#### What Success Looks Like
- Operator logs an intervention: "Increased flow to Cell 3 to 650 m³/hr at 14:30"
- System automatically captures before/after metrics
- After sufficient time, system calculates intervention effectiveness
- Future recommendations incorporate this learning
- Operations manager can review intervention history and outcomes

#### What This Is NOT
- Not a replacement for SCADA or operational control systems
- Not automated control - operators make and execute decisions
- Not real-time process control

#### Scope: Owned Files
- `apps/platform_groups/luminous/models/intervention.py`
- `apps/platform_groups/luminous/services/intervention_tracker.py`
- `apps/platform_groups/luminous/services/outcome_analyzer.py`

#### Tasks
- [ ] Create Intervention model (action, timestamp, operator, conditions_before)
- [ ] Build intervention logging API
- [ ] Automatic before/after metric capture
- [ ] Outcome calculation service (compare expected vs actual)
- [ ] Feedback loop to recommendation engine
- [ ] Intervention effectiveness reporting

---

### Feature 7.5: Prescriptive Alerts
**Linear:** TBD
**Status:** 🔴 Not Started
**Priority:** Medium
**Dependencies:** Features 7.1, 7.2, 7.4, SQH-EPIC-06 (Anomaly Detection Service)

#### Outcome
Operators receive proactive recommendations when conditions suggest an action should be taken, rather than only reacting to problems.

#### What Success Looks Like
- Operator receives alert: "Flow rate in Cell 3 should be increased based on current conditions"
- Alert includes: recommended action, confidence level, expected benefit, similar past events
- Operator can view supporting evidence before acting
- Alerts respect notification preferences (don't spam)
- Alert history shows which were acted on and outcomes

#### Scope: Owned Files
- `apps/platform_groups/luminous/services/prescriptive_alerts.py`
- `apps/platform_groups/luminous/notifications/` (Luminous-specific alert triggers)

#### Tasks
- [ ] Define alert conditions (when to recommend action vs. wait)
- [ ] Build prescriptive alert service
- [ ] Integrate with platform notification system
- [ ] Confidence scoring for recommendations
- [ ] Similar event retrieval for supporting evidence
- [ ] Alert effectiveness tracking

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
- [LUM-EPIC-01: Data Ingestion](LUM-EPIC-01-Data-Ingestion.md) - Data foundation
- [LUM-EPIC-03: Customer Dashboard](LUM-EPIC-03-Customer-Dashboard.md) - Visualization
- [SQH-EPIC-06: AI Services](../SquareHead/SQH-EPIC-06-AI-Services.md) - Anomaly detection platform capability
