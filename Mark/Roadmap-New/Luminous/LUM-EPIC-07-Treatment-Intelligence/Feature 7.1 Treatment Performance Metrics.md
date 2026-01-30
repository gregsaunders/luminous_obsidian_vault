---
status: "Not Started"
priority: "Critical"
assigned: ""
dependencies:
  - "LUM-EPIC-02 Features 2.1-2.3"
linear_id: "TBD"
---

# Feature 7.1: Treatment Performance Metrics

**Linear:** TBD

---

## Outcome

Operations managers can see treatment effectiveness metrics for each cell, enabling comparison and informed routing decisions.

---

## What Success Looks Like

- Manager views dashboard showing effectiveness by cell
- Each cell displays: removal efficiency, throughput, cost per unit treated
- Can filter by time period (week, month, season)
- Can compare current performance to historical baseline
- Trends are visible - improving vs declining performance

---

## Scope: Owned Files

- `apps/platform_groups/luminous/models/treatment_metrics.py`
- `apps/platform_groups/luminous/services/metrics_calculator.py`
- `apps/platform_groups/luminous/api/metrics.py`

---

## Tasks

- [ ] Define treatment effectiveness metrics (removal efficiency formula, throughput calculation)
- [ ] Create TreatmentMetric model (cell, period, metrics)
- [ ] Build metrics calculation service (aggregate from biosensor results)
- [ ] Create API endpoints for metrics retrieval
- [ ] Define baseline calculation methodology
- [ ] Historical comparison logic (current vs. same period last year)
