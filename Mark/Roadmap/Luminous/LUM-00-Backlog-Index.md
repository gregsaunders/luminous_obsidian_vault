---
linear_project: Luminous
linear_url: https://linear.app/squarehead/project/luminous-9a90903f56ff
---

# Luminous Product Backlog

**Last Updated:** 2026-01-08
**Target Milestone:** Q2 2026 - CNRL Pilot Ready
**Architecture:** Luminous is built as a [Platform Group](../SquareHead/SQH-EPIC-01-Platform-Groups.md)

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

See [Master Index](../00-Master-Index.md) for cross-area dependency map.

---

## Epic Overview

| Epic | Linear | Status | Priority | Description |
|------|--------|--------|----------|-------------|
| [LUM-EPIC-01: Customer Dashboard](LUM-EPIC-01-Customer-Dashboard.md) | [SQU-5](https://linear.app/squarehead/issue/SQU-5) | 🔴 Not Started | Critical | Customer-facing dashboard for biosensor results |
| [LUM-EPIC-02: Data Ingestion](LUM-EPIC-02-Data-Ingestion.md) | [SQU-6](https://linear.app/squarehead/issue/SQU-6) | 🔴 Not Started | Critical | Biosensor results, sample metadata, contextual data |
| [LUM-EPIC-03: Platform Infrastructure](LUM-EPIC-03-Platform-Infrastructure.md) | [SQU-7](https://linear.app/squarehead/issue/SQU-7) | 🟡 Partial | High | User provisioning, audit trail, notifications |
| [LUM-EPIC-04: Field Operations](LUM-EPIC-04-Field-Operations.md) | [SQU-8](https://linear.app/squarehead/issue/SQU-8) | 🔴 Not Started | High | Sample metadata capture from field |
| [LUM-EPIC-05: Observability & Docs](LUM-EPIC-05-Observability-Docs.md) | [SQU-9](https://linear.app/squarehead/issue/SQU-9) | 🟡 Partial | Medium | Documentation, AI services, monitoring |

---

## Priority Legend

| Priority | Meaning |
|----------|---------|
| **Critical** | Must complete before pilot launch |
| **High** | Significantly improves pilot readiness |
| **Medium** | Can build during or after pilot |
---

## Dependency Map

![[assets/luminous-dependency-map.svg]]

### Key Blockers

| Blocker                             | Blocks                                 | Owner | Status         |
| ----------------------------------- | -------------------------------------- | ----- | -------------- |
| Luminous Platform Group scaffolding | All EPIC features                      | TBD   | 🔴 Not Started |
| EPIC-02 Features 2.1-2.3            | EPIC-01, EPIC-03 notifications/reports | Greg  | 🔴 Not Started |

### Pending Decisions

| Decision | Options | Blocks | Owner |
|----------|---------|--------|-------|
| Dashboard Tech | Metabase / Retool / Custom Flutter | EPIC-01 all features | TBD |

See [LUM-EPIC-01 Technology Decision](LUM-EPIC-01-Customer-Dashboard.md#technology-decision) for detailed options.

## Status Legend

| Status | Meaning |
|--------|---------|
| 🔴 Not Started | Work has not begun |
| 🟡 Partial / In Progress | Some work complete or actively being worked |
| 🟢 Complete | All features delivered |

---

## Critical Path Summary

The following features are **blockers** for the Q2 2026 pilot:

1. **Customer Dashboard MVP** (EPIC-01)
   - Authentication, results visualization, trend charts, data export

2. **Biosensor Results Ingestion** (EPIC-02)
   - Data model, CSV upload, barcode linkage

3. **Sample Metadata Linkage** (EPIC-02)
   - Field metadata → lab results connection

---

## Platform Context

**Tech Stack:**
- Backend: Django 5.2, Django REST Framework
- Databases: PostgreSQL, TerminusDB (graph), Qdrant (vector), Meilisearch
- Frontend: Flutter (desktop/mobile/web)
- AI: OpenAI + Modal (self-hosted Granite, Qwen)

**Key Source Directories:**
- `square_head/apps/` - Django applications
- `square_head/frontend/flutter/` - Client apps
- `square_head/docs/` - MkDocs documentation

---

## Related Documents

- [Master Index](../00-Master-Index.md) - Cross-area overview
- [SquareHead Platform Backlog](../SquareHead/SQH-00-Backlog-Index.md)
- [Technology Requirements](../../03-OPERATING-MODEL/03-Technology-Requirements.md)
- [Pilot Readiness Scorecard](../../03-OPERATING-MODEL/04-Pilot-Readiness-Scorecard.md)
- [Pilot Deliverables Framework](../../03-OPERATING-MODEL/05-Pilot-Deliverables-Framework.md)
- [CRM Reference Implementation](../../../../square_head/apps/platform_groups/crm/) - Pattern reference
