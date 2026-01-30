---
linear_project: Luminous
linear_url: https://linear.app/squarehead/project/luminous-9a90903f56ff
---

# Luminous Product Backlog

**Last Updated:** 2026-01-27
**Target Milestone:** Q2 2026 - CNRL Pilot Ready
**Architecture:** Luminous is built as a [Platform Group](../SquareHead/SQH-EPIC-03-Platform-Groups.md)

---

## Demo Strategy

The Q2 2026 pilot demo uses **Claude Cowork + MCP Server** as the primary interface.

See [Master Index](../00-Master-Index.md) for the full demo strategy and execution phases.

---

## Platform Group Dependency

Luminous depends on the Square Head Platform Groups system. All features are implemented within:

```
apps/platform_groups/luminous/
├── manifest.yaml           # Data models (Sample, Result, Location)
├── ui_hints.yaml          # Dashboard view configuration
├── relationship_types.yaml # Sample → Result → Location links
└── workflows/             # Analysis automation agents
```

---

## Epic Overview

EPICs are numbered by execution priority for Q2 2026 pilot.

| Epic | Linear | Status | Phase | Description |
|------|--------|--------|-------|-------------|
| [LUM-EPIC-01: Data Ingestion](LUM-EPIC-01-Data-Ingestion.md) | [SQU-6](https://linear.app/squarehead/issue/SQU-6) | 🔴 Not Started | 0-1 | Platform Group scaffolding + biosensor data model |
| [LUM-EPIC-02: Unified Water Quality Data Model](LUM-EPIC-02-Unified-Water-Quality-Data-Model.md) | TBD | 🔴 Not Started | 1-2 | PostgreSQL-backed water quality data for cross-source analysis |
| [LUM-EPIC-03: Customer Dashboard](LUM-EPIC-03-Customer-Dashboard.md) | [SQU-5](https://linear.app/squarehead/issue/SQU-5) | 🔴 Not Started | 2-3 | Customer-facing dashboard (after UX foundation) |
| [LUM-EPIC-04: Platform Infrastructure](LUM-EPIC-04-Platform-Infrastructure.md) | [SQU-7](https://linear.app/squarehead/issue/SQU-7) | 🟡 Partial | 2 | User provisioning, audit trail, notifications |
| [LUM-EPIC-05: Field Operations](LUM-EPIC-05-Field-Operations.md) | [SQU-8](https://linear.app/squarehead/issue/SQU-8) | 🔴 Not Started | 3 | Sample metadata capture from field |
| [LUM-EPIC-06: Observability & Docs](LUM-EPIC-06-Observability-Docs.md) | [SQU-9](https://linear.app/squarehead/issue/SQU-9) | 🟡 Partial | 2-3 | Documentation, AI services, monitoring |
| [LUM-EPIC-07: Treatment Intelligence](LUM-EPIC-07-Treatment-Intelligence.md) | TBD | 🔴 Not Started | Post-Pilot | Treatment optimization recommendations |

### Renumbering Reference

| New # | Old # | EPIC Name |
|-------|-------|-----------|
| LUM-01 | LUM-02 | Data Ingestion (incl. scaffolding) |
| LUM-02 | LUM-06 | Unified Water Quality Data Model |
| LUM-03 | LUM-01 | Customer Dashboard |
| LUM-04 | LUM-03 | Platform Infrastructure |
| LUM-05 | LUM-04 | Field Operations |
| LUM-06 | LUM-05 | Observability & Docs |
| LUM-07 | LUM-07 | Treatment Intelligence |

---

## Phase Context

| Phase | Meaning |
|-------|---------|
| **0** | MCP + Scaffolding Foundation |
| **1** | Data Infrastructure |
| **2** | Water Quality + Demo Polish |
| **3** | Pilot Readiness |
| **Post-Pilot** | Q3 2026+ |

---

## Dependency Map

![[assets/luminous-dependency-map.svg]]

### Key Blockers

| Blocker | Blocks | Owner | Status |
|---------|--------|-------|--------|
| MCP Server Foundation (SQH-01) | Demo interface | TBD | 🔴 Not Started |
| Luminous Platform Group scaffolding (LUM-01 Feature 1.0) | All EPIC features | TBD | 🔴 Not Started |
| LUM-01 Features 1.1-1.3 (Data model + ingestion) | LUM-03, LUM-04 notifications/reports | Greg | 🔴 Not Started |
| SQH-02 (Unified Data Access) | LUM-02 (Water Quality Data Model) | TBD | 🔴 Not Started |
| SQH-04 Map Component | LUM-02 Feature 2.6 (Dashboard Views) | TBD | 🔴 Not Started |

### Dashboard Tech Decision: RESOLVED

**Decision:** Claude Cowork + MCP Server is the demo interface. Flutter native app follows later.

This eliminates the Metabase/Retool/Custom Flutter decision for the pilot demo phase.

---

## Status Legend

| Status | Meaning |
|--------|---------|
| 🔴 Not Started | Work has not begun |
| 🟡 Partial / In Progress | Some work complete or actively being worked |
| 🟢 Complete | All features delivered |

---

## Critical Path Summary

The following features are **blockers** for the Q2 2026 pilot:

1. **MCP Server Foundation** (SQH-01)
   - Demo interface via Claude Cowork

2. **Platform Group Scaffolding + Biosensor Data** (LUM-01)
   - Luminous Platform Group creation, data model, CSV upload, barcode linkage

3. **Unified Water Quality Data Model** (LUM-02)
   - PostgreSQL schema, ETL pipelines, query services for 4 regional data sources
   - Blocked by: SQH-02 (Unified Data Access Layer)

4. **User Provisioning** (LUM-04)
   - Multi-tenant support for pilot customers

---

## Post-Pilot Intelligence Layer

The following supports the "Foundry" vision of actionable intelligence (Q3 2026+):

1. **Treatment Intelligence** (LUM-07)
   - Performance metrics, routing recommendations, seasonal optimization
   - Depends on: LUM-01 (data foundation), LUM-02 (historical data)

2. **Community Dashboard** (LUM-03 Feature 3.7)
   - Plain-language views for Indigenous communities and public stakeholders

3. **Operator Annotations** (LUM-03 Feature 3.8)
   - Institutional knowledge capture for compounding learning

4. **Anomaly Detection** (Platform: SQH-06 Feature 6.4)
   - Reusable baseline and deviation detection service

---

## Platform Context

**Tech Stack:**
- Backend: Django 5.2, Django REST Framework
- Databases: PostgreSQL, TerminusDB (graph), Qdrant (vector), Meilisearch
- Frontend: Flutter (desktop/mobile/web)
- AI: OpenAI + Modal (self-hosted Granite, Qwen)
- Demo Interface: MCP Server + Claude Cowork

**Key Source Directories:**
- `square_head/apps/` - Django applications
- `square_head/frontend/flutter/` - Client apps
- `square_head/docs/` - MkDocs documentation
- `square_head/mcp/` - MCP server

---

## Related Documents

- [Master Index](../00-Master-Index.md) - Cross-area overview
- [SquareHead Platform Backlog](../SquareHead/SQH-00-Backlog-Index.md)
- [Technology Requirements](../../03-OPERATING-MODEL/03-Technology-Requirements.md)
- [Pilot Readiness Scorecard](../../03-OPERATING-MODEL/04-Pilot-Readiness-Scorecard.md)
- [Pilot Deliverables Framework](../../03-OPERATING-MODEL/05-Pilot-Deliverables-Framework.md)
- [CRM Reference Implementation](../../../../square_head/apps/platform_groups/crm/) - Pattern reference
