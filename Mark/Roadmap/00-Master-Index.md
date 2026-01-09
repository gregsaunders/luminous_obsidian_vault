# Square Head Platform - Master Roadmap Index

**Last Updated:** 2026-01-08

---

## Project Tracking

This roadmap is tracked in **Linear**: [Squarehead Workspace](https://linear.app/squarehead)

| Project | Linear | EPICs |
|---------|--------|-------|
| [Luminous](Luminous/LUM-00-Backlog-Index.md) | [Luminous Project](https://linear.app/squarehead/project/luminous-9a90903f56ff) | 5 EPICs (SQU-5 to SQU-9) |
| [SquareHead](SquareHead/SQH-00-Backlog-Index.md) | [SquareHead Platform Project](https://linear.app/squarehead/project/squarehead-platform-b6e6ffab) | 13 EPICs (SQU-38 to SQU-50) |

---

## Cross-Area Dependencies

![[assets/master-cross-area-dependencies.svg]]

---

## Key Blockers

| Blocker | Blocks | Status |
|---------|--------|--------|
| **Luminous Platform Group scaffolding** | All Luminous EPICs | Not Started |
| Dashboard tech decision resolved | - | Platform Group + Flutter |

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
