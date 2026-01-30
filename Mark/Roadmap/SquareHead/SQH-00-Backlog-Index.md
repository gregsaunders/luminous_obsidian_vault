---
linear_project: SquareHead Platform
linear_url: https://linear.app/squarehead/project/squarehead-platform-b6e6ffab
---

# SquareHead Platform Backlog

**Last Updated:** 2026-01-27
**Scope:** Core platform infrastructure and capabilities

---

## Demo Critical Path

MCP Server (SQH-01) is the primary demo interface for Q2 2026 pilot via Claude Cowork.

See [Master Index](../00-Master-Index.md) for the full demo strategy and execution phases.

---

## Epic Overview

EPICs are numbered by execution priority for Q2 2026 pilot.

| Epic | Linear | Status | Phase | Summary |
|------|--------|--------|-------|---------|
| [SQH-EPIC-01: MCP Server](SQH-EPIC-01-MCP-Server.md) | TBD | 🔴 Not Started | 0-1 | Model Context Protocol for AI integration - **Demo Interface** |
| [SQH-EPIC-02: Unified Data Access Layer](SQH-EPIC-02-Unified-Data-Access-Layer.md) | [SQU-40](https://linear.app/squarehead/issue/SQU-40) | 🔴 Not Started | 1 | PostgreSQL backend for water quality data |
| [SQH-EPIC-03: Platform Groups](SQH-EPIC-03-Platform-Groups.md) | [SQU-38](https://linear.app/squarehead/issue/SQU-38) | 🟡 Partial | 0 | Modular app extensibility system |
| [SQH-EPIC-04: UI Kit and Platform UX](SQH-EPIC-04-Base-UI-Kit.md) | [SQU-39](https://linear.app/squarehead/issue/SQU-39) | 🟡 Partial | 2+ | Component library + 3-pane application shell |
| [SQH-EPIC-05: Workflow Engine](SQH-EPIC-05-Workflow-Engine.md) | [SQU-43](https://linear.app/squarehead/issue/SQU-43) | 🟡 Partial | 2+ | BPMN workflows with AI agents |
| [SQH-EPIC-06: AI Services](SQH-EPIC-06-AI-Services.md) | [SQU-47](https://linear.app/squarehead/issue/SQU-47) | 🟡 Partial | 1 | RAG for MCP, Modal-hosted AI models |
| [SQH-EPIC-07: CDC Pipeline](SQH-EPIC-07-CDC-Pipeline.md) | [SQU-44](https://linear.app/squarehead/issue/SQU-44) | 🟡 Partial | 2+ | Change data capture |
| [SQH-EPIC-08: Record-Level Access Control](SQH-EPIC-08-Record-Access-Control.md) | [SQU-41](https://linear.app/squarehead/issue/SQU-41) | 🔴 Not Started | 2+ | Record ownership, ACLs, audit logging |
| [SQH-EPIC-09: Object Storage Migration](SQH-EPIC-09-Object-Storage-Migration.md) | [SQU-42](https://linear.app/squarehead/issue/SQU-42) | 🔴 Not Started | 3+ | Replace MinIO with license-compliant storage |
| [SQH-EPIC-10: AI-Generated UI](SQH-EPIC-10-AI-Generated-UI.md) | [SQU-45](https://linear.app/squarehead/issue/SQU-45) | 🔴 Not Started | 3+ | ISON-based composable UI for agents |
| [SQH-EPIC-11: Frontend Apps](SQH-EPIC-11-Frontend-Apps.md) | [SQU-48](https://linear.app/squarehead/issue/SQU-48) | 🟡 Partial | 2 | Flutter & React apps, chat interface |
| [SQH-EPIC-12: Document Management](SQH-EPIC-12-Document-Management.md) | [SQU-46](https://linear.app/squarehead/issue/SQU-46) | 🟢 Complete | - | Document processing & search |
| [SQH-EPIC-13: Extended Database Support](SQH-EPIC-13-Extended-Database-Connectors.md) | [SQU-49](https://linear.app/squarehead/issue/SQU-49) | 🔴 Not Started | 3+ | ConfigBuilder layer for Oracle, MongoDB |
| [SQH-EPIC-14: Tech Debt](SQH-EPIC-14-Tech-Debt.md) | [SQU-50](https://linear.app/squarehead/issue/SQU-50) | Ongoing | - | Outstanding TODOs |

### Renumbering Reference

| New # | Old # | EPIC Name |
|-------|-------|-----------|
| SQH-01 | SQH-14 | MCP Server |
| SQH-02 | SQH-03 | Unified Data Access Layer |
| SQH-03 | SQH-01 | Platform Groups |
| SQH-04 | SQH-02 | UI Kit & Platform UX |
| SQH-05 | SQH-06 | Workflow Engine |
| SQH-06 | SQH-10 | AI Services |
| SQH-07 | SQH-07 | CDC Pipeline |
| SQH-08 | SQH-04 | Record Access Control |
| SQH-09 | SQH-05 | Object Storage Migration |
| SQH-10 | SQH-08 | AI-Generated UI |
| SQH-11 | SQH-11 | Frontend Apps |
| SQH-12 | SQH-09 | Document Management |
| SQH-13 | SQH-12 | Extended Database Support |
| SQH-14 | SQH-13 | Tech Debt |

---

## Status Legend

| Status | Meaning |
|--------|---------|
| 🔴 Not Started | Work has not begun |
| 🟡 Partial | Framework exists, features incomplete |
| 🟢 Complete | Production-ready |

---

## Phase Context

| Phase | Meaning |
|-------|---------|
| **0** | MCP + Scaffolding Foundation |
| **1** | Data Infrastructure |
| **2** | Water Quality + Demo Polish |
| **2+** | Post-demo, pre-pilot |
| **3+** | Post-pilot |

---

## Dependency Map

![[assets/cross-area-dependencies.svg]]

---

## Key Directories

| Directory | Purpose |
|-----------|---------|
| `mcp/` | MCP server (EPIC-01) |
| `apps/platform_groups/` | Modular app system (CRM reference) |
| `apps/workflows/` | BPMN workflow engine |
| `apps/cdc/` | Change data capture |
| `apps/documents/` | Document processing |
| `apps/ai/` | AI usage tracking |
| `apps/notifications/` | Notification framework |
| `frontend/flutter/packages/ui/` | Base UI Kit (EPIC-04) |
| `frontend/flutter/` | Flutter client apps |
| `frontend/react/` | React graph visualizer |
| `modal_apps/` | Self-hosted AI models |

---

## Tech Stack Reference

- **Backend:** Django 5.2, DRF
- **Databases:** PostgreSQL, TerminusDB (graph), Qdrant (vector), Meilisearch (search)
- **Storage:** MinIO (S3-compatible) - *migrating, see EPIC-09*
- **Queue:** Redis + Celery
- **Frontend:** Flutter (desktop/mobile/web), React
- **AI:** OpenAI APIs + Modal (Granite, Qwen2.5 variants)
- **Workflows:** BPMN + DMN + LangGraph + DBOS
- **Observability:** OpenTelemetry, Prometheus, Loki, Grafana
- **AI Integration:** MCP (Model Context Protocol) for external AI clients
