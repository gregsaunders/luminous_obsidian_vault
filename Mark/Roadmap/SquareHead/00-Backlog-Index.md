# SquareHead Platform Backlog

**Last Updated:** 2026-01-05
**Scope:** Core platform infrastructure and capabilities

---

## Epic Overview

| Epic | Status | Priority | Summary |
|------|--------|----------|---------|
| [EPIC-01: Platform Groups](EPIC-01-Platform-Groups.md) | 🟡 Partial | High | Modular app extensibility system |
| [EPIC-02: Base UI Kit](EPIC-02-Base-UI-Kit.md) | 🟡 Partial | High | Shared Flutter component library (Layer 1) |
| [EPIC-03: Workflow Engine](EPIC-03-Workflow-Engine.md) | 🟡 Partial | High | BPMN workflows with AI agents |
| [EPIC-04: CDC Pipeline](EPIC-04-CDC-Pipeline.md) | 🟢 Complete | Medium | Change data capture |
| [EPIC-05: Document Management](EPIC-05-Document-Management.md) | 🟢 Complete | Low | Document processing & search |
| [EPIC-06: AI Services](EPIC-06-AI-Services.md) | 🟡 Partial | Medium | Modal-hosted AI models |
| [EPIC-07: Frontend Apps](EPIC-07-Frontend-Apps.md) | 🟡 Partial | Medium | Flutter & React apps |
| [EPIC-08: Tech Debt](EPIC-08-Tech-Debt.md) | Ongoing | Medium | Outstanding TODOs |

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

```
┌─────────────────────────────────────────────────────────────────┐
│  FOUNDATIONAL (High Priority)                                  │
│                                                                 │
│  ┌──────────────────┐   ┌──────────────────┐                   │
│  │ EPIC-01         │   │ EPIC-02         │                   │
│  │ Platform Groups │   │ Base UI Kit     │                   │
│  │ (modular apps)  │   │ (Layer 1 UI)    │                   │
│  └────────┬─────────┘   └────────┬─────────┘                   │
│           │                      │                              │
│           └──────────┬───────────┘                              │
│                      │                                          │
│                      ▼                                          │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ EPIC-03: Workflow Engine                                │   │
│  │ (uses Platform Groups for workflow definitions)         │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  INFRASTRUCTURE (Medium Priority)                              │
│                                                                 │
│  ┌──────────────────┐   ┌──────────────────┐                   │
│  │ EPIC-04         │   │ EPIC-05         │                   │
│  │ CDC Pipeline    │   │ Document Mgmt   │                   │
│  │ (complete)      │   │ (complete)      │                   │
│  └──────────────────┘   └──────────────────┘                   │
│                                                                 │
│  ┌──────────────────┐   ┌──────────────────┐                   │
│  │ EPIC-06         │   │ EPIC-07         │                   │
│  │ AI Services     │   │ Frontend Apps   │                   │
│  │                 │   │ (uses EPIC-02)  │                   │
│  └──────────────────┘   └──────────────────┘                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  ONGOING                                                        │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ EPIC-08: Tech Debt                                      │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

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
