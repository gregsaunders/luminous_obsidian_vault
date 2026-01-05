# Square Head Platform Backlog

**Last Updated:** 2026-01-05
**Target Milestone:** Q2 2026 - CNRL Pilot Ready

---

## Epic Overview

| Epic | Status | Priority | Description |
|------|--------|----------|-------------|
| [EPIC-01: Customer Dashboard](EPIC-01-Customer-Dashboard.md) | 🔴 Not Started | Critical | Customer-facing dashboard for biosensor results |
| [EPIC-02: Data Ingestion](EPIC-02-Data-Ingestion.md) | 🔴 Not Started | Critical | Biosensor results, sample metadata, contextual data |
| [EPIC-03: Platform Infrastructure](EPIC-03-Platform-Infrastructure.md) | 🟡 Partial | High | User provisioning, audit trail, notifications |
| [EPIC-04: Field Operations](EPIC-04-Field-Operations.md) | 🔴 Not Started | High | Sample metadata capture from field |
| [EPIC-05: Observability & Docs](EPIC-05-Observability-Docs.md) | 🟡 Partial | Medium | Documentation, AI services, monitoring |

---

## Priority Legend

| Priority | Meaning |
|----------|---------|
| **Critical** | Must complete before pilot launch |
| **High** | Significantly improves pilot readiness |
| **Medium** | Can build during or after pilot |
---

## Dependency Map

```
┌───────────────────────────────────────────────────────────────────┐
│  FOUNDATIONAL (No Blockers - Start First)                       │
│  ┌──────────────────────┐   ┌──────────────────────┐              │
│  │ EPIC-02 Data       │   │ EPIC-04 Field Ops  │              │
│  │ Ingestion          │   │ (Feature 4.1 only) │              │
│  │ Features 2.1-2.3   │   │                    │              │
│  └──────────┬───────────┘   └──────────┬───────────┘              │
│             │                      │                          │
│             └───────────┬──────────┘                          │
│                       ▼                                        │
│  ┌─────────────────────────────────────────────────┐            │
│  │ EPIC-02 Feature 2.3: Sample Metadata Linkage  │            │
│  │ (joins field data + lab results)              │            │
│  └────────────────────────┬────────────────────────┘            │
│                         │                                     │
└─────────────────────────┼─────────────────────────────────────────┘
                          ▼
┌───────────────────────────────────────────────────────────────────┐
│  DEPENDENT (Blocked Until Data Exists)                          │
│                                                                 │
│  ┌──────────────────────┐                                       │
│  │ ⚠️  DECISION NEEDED │  ← Blocks all EPIC-01 work            │
│  │ Dashboard Tech     │                                        │
│  │ (Metabase/Retool/  │                                        │
│  │  Custom Flutter)   │                                        │
│  └──────────┬───────────┘                                       │
│             │                                                   │
│             ▼                                                   │
│  ┌──────────────────────┐   ┌──────────────────────┐              │
│  │ EPIC-01 Dashboard  │   │ EPIC-03 Platform   │              │
│  │ (all features)     │   │ (notifications,    │              │
│  │                    │   │  PDF reports)      │              │
│  └──────────────────────┘   └──────────────────────┘              │
│                                                                 │
└───────────────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────────────┐
│  PARALLEL (Can Progress Anytime)                                │
│  ┌─────────────────────────────────────────────────┐            │
│  │ EPIC-05 Observability & Docs                  │            │
│  │ EPIC-03 Feature 3.1 (User Provisioning)       │            │
│  └─────────────────────────────────────────────────┘            │
└───────────────────────────────────────────────────────────────────┘
```

### Key Blockers

| Blocker | Blocks | Owner | Status |
|---------|--------|-------|--------|
| Dashboard Tech Decision | All EPIC-01 work | Greg | ⚠️ Pending |
| EPIC-02 Features 2.1-2.3 | EPIC-01, EPIC-03 notifications/reports | Greg | 🔴 Not Started |

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

- [Technology Requirements](../03-OPERATING-MODEL/03-Technology-Requirements.md)
- [Pilot Readiness Scorecard](../03-OPERATING-MODEL/04-Pilot-Readiness-Scorecard.md)
- [Pilot Deliverables Framework](../03-OPERATING-MODEL/05-Pilot-Deliverables-Framework.md)
