---
linear_id: SQU-47
linear_url: https://linear.app/squarehead/issue/SQU-47
---

# EPIC-06: AI Services

**Linear:** [SQU-47](https://linear.app/squarehead/issue/SQU-47)
**Status:** Partial
**Priority:** Medium
**Owner:** TBD

---

## Vision

Developers can leverage self-hosted AI models for chat, embeddings, code, vision, and reasoning without external API dependencies.

---

## User Stories

- As a **developer**, I can call AI services for various tasks using consistent APIs
- As an **ops engineer**, I can monitor AI service costs and usage
- As a **new developer**, I can choose the right model for my task based on documented guidelines
- As a **Platform Group developer**, I can configure anomaly detection for my domain metrics so the system alerts when values deviate from normal

---

## Context

Modal-hosted self-hosted AI models. Services deployed and functional; need documentation and cost visibility.

**What exists:**
- 5 Modal services: chat (Granite), embeddings (Qwen), code (Qwen), vision (Qwen), reasoning (Qwen)
- OpenTelemetry tracing, AI usage tracking

**What's needed:** Documentation, cost monitoring, model selection guidelines

---

## Features

### Feature 6.1: AI Services Documentation

#### Outcome
A developer can understand and use AI services without asking for help.

#### Scope: Owned Files
- `docs/ai-services/`

#### Tasks
- [ ] Architecture overview
- [ ] Service catalog with capabilities
- [ ] Deployment and scaling procedures

---

### Feature 6.2: Cost Monitoring Dashboard

#### Outcome
Team can see AI service usage and costs, with alerts for budget overruns.

#### Scope: Owned Files
- `square_head/observability/dashboards/ai-costs.json`
- `apps/ai/reports/`

#### Tasks
- [ ] Usage tracking visualization
- [ ] Cost allocation by team
- [ ] Budget alerts

---

### Feature 6.3: Model Selection Guidelines

#### Outcome
A developer knows which model to use for which task without trial and error.

#### Scope: Owned Files
- `docs/ai-services/model-selection.md`

#### Tasks
- [ ] Which model for which task
- [ ] Performance vs cost tradeoffs
- [ ] Context length considerations

---

### Feature 6.4: Anomaly Detection Service
**Linear:** TBD
**Status:** 🔴 Not Started
**Priority:** High
**Dependencies:** None (standalone platform capability)
**Used By:**
- [LUM-EPIC-07 Feature 7.5](../Luminous/LUM-EPIC-07-Treatment-Intelligence.md) - Prescriptive Alerts
- [LUM-EPIC-04 Feature 4.2](../Luminous/LUM-EPIC-04-Platform-Infrastructure.md) - Notification System

#### Outcome
Platform Groups can detect when metrics deviate from established baselines, enabling proactive alerting across any domain.

#### What Success Looks Like
- Developer configures anomaly detection for a metric (e.g., biosensor NA concentration, sales pipeline value)
- System establishes baseline from historical data
- When new data arrives, system evaluates against baseline
- Anomalies trigger alerts with severity scores and context
- False positive rate is low enough that operators trust the alerts

#### Context
Anomaly detection is a cross-cutting concern. Luminous needs it for biosensor results, CRM could use it for sales anomalies, and future Platform Groups will benefit. Building this as a platform capability avoids duplicate implementations.

#### Scope: Owned Files
- `apps/ai/anomaly/`
- `apps/ai/anomaly/baseline.py`
- `apps/ai/anomaly/detectors.py`
- `apps/ai/anomaly/service.py`

#### Tasks
- [ ] Define AnomalyDetectionConfig model (metric, baseline_period, sensitivity, alert_threshold)
- [ ] Implement baseline calculation from historical data (rolling window, seasonal adjustment)
- [ ] Implement statistical detectors:
  - Z-score detector (deviation from mean)
  - Modified Z-score (robust to outliers)
  - IQR-based detector (interquartile range)
- [ ] Multi-variate correlation detection (when combinations of metrics are anomalous together)
- [ ] Severity scoring (how anomalous is this? minor/moderate/severe)
- [ ] Integration with notification system (feed anomalies into alerts)
- [ ] Anomaly history tracking (for analysis and tuning)
- [ ] Configuration API for Platform Groups to register metrics

---

## Key Files

- `modal_apps/chat_service.py` - IBM Granite 4.0 Micro (A10G)
- `modal_apps/embedding_service.py` - Qwen3-Embedding 0.6B (T4)
- `modal_apps/code_service.py` - Qwen2.5-Coder 7B (A10G)
- `modal_apps/vision_service.py` - Qwen2.5-VL 7B (A10G)
- `modal_apps/reasoning_service.py` - Qwen3 4B (A10G)
- `modal_apps/otel_bootstrap.py` - Observability
- `apps/ai/models.py` - AIUsageLog
