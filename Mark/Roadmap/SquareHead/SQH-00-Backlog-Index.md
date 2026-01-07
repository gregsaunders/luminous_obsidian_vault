# SquareHead Platform Backlog

**Last Updated:** 2026-01-05
**Scope:** Core platform infrastructure and capabilities

---

## Epic Overview

| Epic | Status | Priority | Summary |
|------|--------|----------|---------|
| [SQH-EPIC-01: Platform Groups](SQH-EPIC-01-Platform-Groups.md) | 🟡 Partial | High | Modular app extensibility system |
| [SQH-EPIC-02: UI Kit and Platform UX](SQH-EPIC-02-Base-UI-Kit.md) | 🟡 Partial | High | Component library + 3-pane application shell |
| [SQH-EPIC-03: Workflow Engine](SQH-EPIC-03-Workflow-Engine.md) | 🟡 Partial | High | BPMN workflows with AI agents |
| [SQH-EPIC-04: CDC Pipeline](SQH-EPIC-04-CDC-Pipeline.md) | 🟡 Partial | Medium | Change data capture |
| [SQH-EPIC-05: Document Management](SQH-EPIC-05-Document-Management.md) | 🟢 Complete | Low | Document processing & search |
| [SQH-EPIC-06: AI Services](SQH-EPIC-06-AI-Services.md) | 🟡 Partial | Medium | Modal-hosted AI models |
| [SQH-EPIC-07: Frontend Apps](SQH-EPIC-07-Frontend-Apps.md) | 🟡 Partial | Medium | Flutter & React apps |
| [SQH-EPIC-08: Tech Debt](SQH-EPIC-08-Tech-Debt.md) | Ongoing | Medium | Outstanding TODOs |
| [SQH-EPIC-09: AI-Generated UI](SQH-EPIC-09-AI-Generated-UI.md) | 🔴 Not Started | Medium | ISON-based composable UI for agents |
| [SQH-EPIC-10: Extended Database Support](SQH-EPIC-10-Extended-Database-Connectors.md) | 🔴 Not Started | Low | ConfigBuilder layer for Oracle, MongoDB |
| [SQH-EPIC-11: Record-Level Access Control](SQH-EPIC-11-Record-Access-Control.md) | 🔴 Not Started | Medium | Record ownership, ACLs, audit logging |

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

## Dependency Map

![[assets/cross-area-dependencies.svg]]

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
| `frontend/flutter/packages/ui/` | Base UI Kit (EPIC-02) |
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
