---
status: "In Progress"
priority: "Medium"
assigned: ""
dependencies: []
linear_id: "SQU-33"
---

# Feature 6.1: Platform Monitoring Dashboard

**Linear:** [SQU-33](https://linear.app/squarehead/issue/SQU-33)
**Status Note:** Infrastructure exists

---

## Outcome

An operator can see Luminous platform health at a glance and get alerted to issues.

---

## What Success Looks Like

- Operator opens Grafana, sees Luminous dashboard
- Key metrics visible: API latency, error rate, queue depth
- Alerts fire when thresholds breached
- Can drill down to identify root cause

---

## Context

Infrastructure exists (OpenTelemetry, Prometheus, Loki, Grafana). This feature adds Luminous-specific dashboards.

---

## Scope: Owned Files

- `square_head/observability/dashboards/luminous.json`

---

## Requirements

- Grafana dashboard displays Luminous-specific metrics in one view
- API response times are monitored with visible latency graphs
- Error rate alerts fire when thresholds are breached
- Database query performance is tracked and visible
- Celery queue depth is monitored with alerts for backlogs
