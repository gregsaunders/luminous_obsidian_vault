---
status: "Not Started"
priority: "High"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 6.4: Anomaly Detection Service

**Used By:**
- [[../../Luminous/LUM-EPIC-07-Treatment-Intelligence/00-Treatment-Intelligence|LUM-EPIC-07]] Feature 7.5 - Prescriptive Alerts
- [[../../Luminous/LUM-EPIC-04-Platform-Infrastructure/00-Platform-Infrastructure|LUM-EPIC-04]] Feature 4.2 - Notification System

## Outcome

Platform Groups can detect when metrics deviate from established baselines, enabling proactive alerting across any domain.

## What Success Looks Like

- Developer configures anomaly detection for a metric (e.g., biosensor NA concentration, sales pipeline value)
- System establishes baseline from historical data
- When new data arrives, system evaluates against baseline
- Anomalies trigger alerts with severity scores and context
- False positive rate is low enough that operators trust the alerts

## Context

Anomaly detection is a cross-cutting concern. Luminous needs it for biosensor results, CRM could use it for sales anomalies, and future Platform Groups will benefit. Building this as a platform capability avoids duplicate implementations.

## Scope: Owned Files

- `apps/ai/anomaly/`
- `apps/ai/anomaly/baseline.py`
- `apps/ai/anomaly/detectors.py`
- `apps/ai/anomaly/service.py`

## Requirements

- Define AnomalyDetectionConfig model (metric, baseline_period, sensitivity, alert_threshold)
- Implement baseline calculation from historical data (rolling window, seasonal adjustment)
- Implement statistical detectors:
  - Z-score detector (deviation from mean)
  - Modified Z-score (robust to outliers)
  - IQR-based detector (interquartile range)
- Multi-variate correlation detection (when combinations of metrics are anomalous together)
- Severity scoring (how anomalous is this? minor/moderate/severe)
- Integration with notification system (feed anomalies into alerts)
- Anomaly history tracking (for analysis and tuning)
- Configuration API for Platform Groups to register metrics
