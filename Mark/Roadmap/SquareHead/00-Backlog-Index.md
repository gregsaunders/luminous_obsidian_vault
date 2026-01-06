# SquareHead Platform Backlog

**Last Updated:** 2026-01-05
**Scope:** Core platform infrastructure and capabilities

---

## Epic Overview

| Epic | Status | Priority | Summary |
|------|--------|----------|---------|
| [EPIC-01: Platform Groups](EPIC-01-Platform-Groups.md) | 🟡 Partial | High | Modular app extensibility system |
| [EPIC-02: Workflow Engine](EPIC-02-Workflow-Engine.md) | 🟡 Partial | High | BPMN workflows with AI agents |
| [EPIC-03: CDC Pipeline](EPIC-03-CDC-Pipeline.md) | 🟢 Complete | Medium | Change data capture |
| [EPIC-04: Document Management](EPIC-04-Document-Management.md) | 🟢 Complete | Low | Document processing & search |
| [EPIC-05: AI Services](EPIC-05-AI-Services.md) | 🟡 Partial | Medium | Modal-hosted AI models |
| [EPIC-06: Frontend Apps](EPIC-06-Frontend-Apps.md) | 🟡 Partial | Medium | Flutter & React apps |
| [EPIC-07: Tech Debt](EPIC-07-Tech-Debt.md) | Ongoing | Medium | Outstanding TODOs |

---

## Status Legend

| Status | Meaning |
|--------|---------|
| 🔴 Not Started | Work has not begun |
| 🟡 Partial | Framework exists, features incomplete |
| 🟢 Complete | Production-ready |

---

## Priority Context

| Priority | Meaning |
|----------|---------|
| **High** | Directly needed for Luminous product |
| **Medium** | Platform capability, not urgent for pilot |
| **Low** | Nice to have, no current dependency |

---

## Key Directories

| Directory | Purpose |
|-----------|---------|
| `apps/platform_groups/` | Modular app system (CRM reference) |
| `apps/workflows/` | BPMN workflow engine |
| `apps/cdc/` | Change data capture |
| `apps/documents/` | Document processing |
| `apps/ai/` | AI usage tracking |
| `apps/notifications/` | Notification framework |
| `frontend/flutter/` | Flutter client apps |
| `frontend/react/` | React graph visualizer |
| `modal_apps/` | Self-hosted AI models |

---

## Tech Stack Reference

- **Backend:** Django 5.2, DRF
- **Databases:** PostgreSQL, TerminusDB (graph), Qdrant (vector), Meilisearch (search)
- **Storage:** MinIO (S3-compatible)
- **Queue:** Redis + Celery
- **Frontend:** Flutter (desktop/mobile/web), React
- **AI:** OpenAI APIs + Modal (Granite, Qwen2.5 variants)
- **Workflows:** BPMN + DMN + LangGraph + DBOS
- **Observability:** OpenTelemetry, Prometheus, Loki, Grafana
