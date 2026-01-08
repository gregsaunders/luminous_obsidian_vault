# EPIC-09: AI Services

**Status:** 🟡 Partial
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

---

## Context

Modal-hosted self-hosted AI models. Services deployed and functional; need documentation and cost visibility.

**What exists:**
- 5 Modal services: chat (Granite), embeddings (Qwen), code (Qwen), vision (Qwen), reasoning (Qwen)
- OpenTelemetry tracing, AI usage tracking

**What's needed:** Documentation, cost monitoring, model selection guidelines

---

## Features

### Feature 9.1: AI Services Documentation

#### Outcome
A developer can understand and use AI services without asking for help.

#### Scope: Owned Files
- `docs/ai-services/`

#### Tasks
- [ ] Architecture overview
- [ ] Service catalog with capabilities
- [ ] Deployment and scaling procedures

---

### Feature 9.2: Cost Monitoring Dashboard

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

### Feature 9.3: Model Selection Guidelines

#### Outcome
A developer knows which model to use for which task without trial and error.

#### Scope: Owned Files
- `docs/ai-services/model-selection.md`

#### Tasks
- [ ] Which model for which task
- [ ] Performance vs cost tradeoffs
- [ ] Context length considerations

---

## Key Files

- `modal_apps/chat_service.py` - IBM Granite 4.0 Micro (A10G)
- `modal_apps/embedding_service.py` - Qwen3-Embedding 0.6B (T4)
- `modal_apps/code_service.py` - Qwen2.5-Coder 7B (A10G)
- `modal_apps/vision_service.py` - Qwen2.5-VL 7B (A10G)
- `modal_apps/reasoning_service.py` - Qwen3 4B (A10G)
- `modal_apps/otel_bootstrap.py` - Observability
- `apps/ai/models.py` - AIUsageLog
