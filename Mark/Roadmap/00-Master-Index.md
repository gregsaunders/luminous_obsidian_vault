# Square Head Platform - Master Roadmap Index

**Last Updated:** 2026-01-05

---

## Areas

| Area | Focus | Status |
|------|-------|--------|
| [Luminous](Luminous/LUM-00-Backlog-Index.md) | Biosensor product for NA monitoring | 5 EPICs |
| [SquareHead](SquareHead/SQH-00-Backlog-Index.md) | Core platform infrastructure | 8 EPICs |

---

## Cross-Area Dependencies

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         SQUAREHEAD PLATFORM                             │
│                                                                         │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐       │
│  │ EPIC-01          │  │ EPIC-02          │  │ EPIC-05          │       │
│  │ Platform Groups  │  │ Workflow Engine  │  │ AI Services      │       │
│  │ (manifest.yaml,  │  │ (BPMN, agents,   │  │ (Modal, Granite, │       │
│  │  ui_hints.yaml)  │  │  DMN decisions)  │  │  Qwen models)    │       │
│  └────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘       │
│           │                     │                     │                 │
│           └─────────────────────┼─────────────────────┘                 │
│                                 │                                       │
└─────────────────────────────────┼───────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                           LUMINOUS PRODUCT                              │
│                                                                         │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │ apps/platform_groups/luminous/                                   │   │
│  │                                                                  │   │
│  │ ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌───────────┐ │   │
│  │ │ manifest    │  │ ui_hints    │  │ workflows/  │  │ relation- │ │   │
│  │ │ .yaml       │  │ .yaml       │  │ agents/     │  │ ship_types│ │   │
│  │ │             │  │             │  │             │  │ .yaml     │ │   │
│  │ │ - Sample    │  │ - Dashboard │  │ - Analysis  │  │           │ │   │
│  │ │ - Result    │  │   views     │  │   agents    │  │ - Sample  │ │   │
│  │ │ - Location  │  │ - Forms     │  │ - QC agents │  │   → Result│ │   │
│  │ │ - Context   │  │ - Charts    │  │             │  │ - Result  │ │   │
│  │ └─────────────┘  └─────────────┘  └─────────────┘  │   → Loc   │ │   │
│  │                                                    └───────────┘ │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  EPIC-01: Dashboard (uses ui_hints.yaml for dynamic UI)                 │
│  EPIC-02: Data Ingestion (defines manifest.yaml models)                 │
│  EPIC-03: Infrastructure (uses platform notifications, auth)            │
│  EPIC-04: Field Ops (metadata capture for sample linkage)               │
│  EPIC-05: Docs (documents platform + product)                           │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Blockers

| Blocker | Blocks | Status |
|---------|--------|--------|
| **Luminous Platform Group scaffolding** | All Luminous EPICs | Not Started |
| Dashboard tech decision resolved | - | Platform Group + Flutter |

---

## GitHub Project Labels

### Area Labels
| Label | Color | Scope |
|-------|-------|-------|
| `area:luminous` | Green | Luminous product features |
| `area:platform` | Blue | Square Head platform |

### Sub-Area Labels
| Label | Color | Area | Purpose |
|-------|-------|------|---------|
| `area:platform-groups` | Light Blue | Platform | Extensibility system |
| `area:workflows` | Light Blue | Platform | BPMN/workflow engine |
| `area:cdc` | Light Blue | Platform | Change data capture |
| `area:documents` | Light Blue | Platform | Document management |
| `area:ai` | Light Blue | Platform | AI/Modal services |
| `area:frontend` | Light Blue | Platform | Flutter/React apps |
| `area:dashboard` | Light Green | Luminous | Customer dashboard |
| `area:ingestion` | Light Green | Luminous | Data ingestion |
| `area:field-ops` | Light Green | Luminous | Field operations |

### Priority & Type Labels
| Label | Color | Purpose |
|-------|-------|---------|
| `priority:critical` | Red | Blockers |
| `priority:high` | Orange | Before pilot |
| `priority:medium` | Yellow | Nice to have |
| `type:feature` | Purple | New functionality |
| `type:bug` | Red | Bug fixes |
| `type:tech-debt` | Brown | Cleanup/refactoring |
| `type:docs` | Gray | Documentation |

---

## Milestones

| Milestone | Target | Description |
|-----------|--------|-------------|
| **MVP: Pilot Ready** | Q2 2026 | CNRL pilot minimum viable |
| **Post-Pilot Iteration** | Q3 2026 | Improvements from pilot feedback |

---

## Architecture Context

**Luminous is built as a Platform Group** on Square Head.

The CRM implementation (`apps/platform_groups/crm/`) serves as a reference example demonstrating:
1. Standalone Catalog Entity pattern
2. Junction Entity with Attributes pattern
3. Parent Entity for M2M pattern
4. Junction with Status pattern
5. TaggedUnion for Polymorphism pattern
6. CoreRelationship Extension pattern

**Key benefit:** AI can generate/modify composable UIs dynamically using the ui_hints pattern.

---

## Quick Links

- [Luminous Backlog](Luminous/LUM-00-Backlog-Index.md)
- [SquareHead Platform Backlog](SquareHead/SQH-00-Backlog-Index.md)
- [CRM Reference Implementation](../../square_head/apps/platform_groups/crm/)
- [Pilot Readiness Scorecard](../03-OPERATING-MODEL/04-Pilot-Readiness-Scorecard.md)
