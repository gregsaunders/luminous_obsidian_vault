---
status: "In Progress"
priority: "Medium"
epic_id: "SQH-EPIC-06"
linear_id: "SQU-47"
linear_url: "https://linear.app/squarehead/issue/SQU-47"
---

# EPIC-06: AI Services

## Vision

Developers can leverage self-hosted AI models for chat, embeddings, code, vision, and reasoning without external API dependencies.

## User Stories

- As a **developer**, I can call AI services for various tasks using consistent APIs
- As an **ops engineer**, I can monitor AI service costs and usage
- As a **new developer**, I can choose the right model for my task based on documented guidelines
- As a **Platform Group developer**, I can configure anomaly detection for my domain metrics so the system alerts when values deviate from normal

## Context

Modal-hosted self-hosted AI models. Services deployed and functional; need documentation and cost visibility.

**What exists:**
- 5 Modal services: chat (Granite), embeddings (Qwen), code (Qwen), vision (Qwen), reasoning (Qwen)
- OpenTelemetry tracing, AI usage tracking

**What's needed:** Documentation, cost monitoring, model selection guidelines

## Features

- [[Feature 6.1 AI Services Documentation]]
- [[Feature 6.2 Cost Monitoring Dashboard]]
- [[Feature 6.3 Model Selection Guidelines]]
- [[Feature 6.4 Anomaly Detection Service]]

## Key Files

- `modal_apps/chat_service.py` - IBM Granite 4.0 Micro (A10G)
- `modal_apps/embedding_service.py` - Qwen3-Embedding 0.6B (T4)
- `modal_apps/code_service.py` - Qwen2.5-Coder 7B (A10G)
- `modal_apps/vision_service.py` - Qwen2.5-VL 7B (A10G)
- `modal_apps/reasoning_service.py` - Qwen3 4B (A10G)
- `modal_apps/otel_bootstrap.py` - Observability
- `apps/ai/models.py` - AIUsageLog

## Dependencies

**Depends On:** None (core platform capability)

**Used By:**
- [[SQH-EPIC-01-MCP-Server]] - RAG chat service
- [[LUM-EPIC-07-Treatment-Intelligence]] - Anomaly detection for biosensor data
