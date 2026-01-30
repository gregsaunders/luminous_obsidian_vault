# Square Head Platform - Master Roadmap Index

**Last Updated:** 2026-01-27

---

## Project Tracking

This roadmap is tracked in **Linear**: [Squarehead Workspace](https://linear.app/squarehead)

| Project | Linear | EPICs |
|---------|--------|-------|
| [Luminous](Luminous/LUM-00-Backlog-Index.md) | [Luminous Project](https://linear.app/squarehead/project/luminous-9a90903f56ff) | 7 EPICs |
| [SquareHead](SquareHead/SQH-00-Backlog-Index.md) | [SquareHead Platform Project](https://linear.app/squarehead/project/squarehead-platform-b6e6ffab) | 14 EPICs |

---

## Demo Strategy: MCP + Claude Cowork

**Key Strategic Decision:** Claude Cowork via MCP Server is the primary demo interface for Q2 2026 pilot.

### How It Works

1. **MCP Server** provides data access (search, RAG chat, Platform Group queries)
2. **Claude Cowork** renders artifacts (charts, tables, React dashboards) on demand
3. **User iterates** through natural language: "Make it a bar chart" / "Add a filter for Site A"

### Demo Narrative: "The Foundry Experience"

1. **Connect:** User opens Claude Cowork, connects to SquareHead MCP server
2. **Search:** "Find all documents about naphthenic acid monitoring at Mildred Lake"
3. **RAG Q&A:** "What were the NA concentration trends in Q3 2025?"
4. **Platform Group Query:** "Show me the latest biosensor results for Site A"
5. **Dashboard Generation:** "Create a dashboard showing all sites with their current status"
6. **Water Quality Analysis:** "Compare our biosensor readings to the regional water quality baseline"
7. **Insight:** Claude synthesizes data, provides actionable recommendation with visualization

**Key Insight:** MCP Server IS the dashboard backend. Claude Cowork IS the dashboard UI.

### Flutter Native App (Later)

- **Purpose:** Production deployment with native performance
- **Timing:** After demo UX patterns validated through Claude Cowork
- **Interface:** SquareHead Flutter app with embedded chat

---

## Execution Phases

### Phase 0: MCP + Scaffolding Foundation

**Goal:** MCP Server running with basic tools, Luminous Platform Group created

| Work Item | EPIC |
|-----------|------|
| MCP Server Foundation | SQH-01 |
| MCP Search + RAG Tools | SQH-01 |
| Platform Groups docs completion | SQH-03 |
| Luminous Platform Group scaffold | LUM-01 |

**Exit Criteria:** Claude Cowork can search documents and ask questions via MCP

### Phase 1: Data Infrastructure

**Goal:** Build data foundation for water quality demo

| Work Item | EPIC |
|-----------|------|
| MCP Platform Group Tools | SQH-01 |
| MCP OAuth | SQH-01 |
| PostgreSQL backend | SQH-02 |
| Biosensor data model | LUM-01 |
| Data ingestion pipeline | LUM-01 |

**Exit Criteria:** Claude Cowork can query Luminous data and render dashboards

### Phase 2: Water Quality + Demo Polish

**Goal:** Full water quality data model, demo-ready system

| Work Item | EPIC |
|-----------|------|
| Core water quality schema | LUM-02 |
| ETL pipelines (4 sources) | LUM-02 |
| Query services | LUM-02 |
| MCP Observability | SQH-01 |
| User provisioning | LUM-04 |

**Exit Criteria:** Demo: "Query 6M water quality measurements" with 4 regional sources

### Phase 3: Pilot Readiness

**Goal:** Production-ready for CNRL pilot

| Work Item | EPIC |
|-----------|------|
| Flutter native app (optional) | SQH-04/SQH-11 |
| Record access control | SQH-08 |
| Audit logging | LUM-04 |
| Observability | LUM-06 |

---

## Critical Path

### Demo Critical Path (Q2 2026)

![[assets/demo-critical-path.svg]]

**Key Insights:**
1. **Parallel Tracks:** SQH-01 (MCP Server) and SQH-02 (Unified Data Access) can proceed simultaneously
2. **LUM-01 and LUM-02 are independent:** Both need SQH-02, but neither blocks the other
3. **Demo Convergence:** MCP + PostgreSQL (F1.7) requires both MCP Core and Luminous data loaded

### Post-Demo Roadmap

![[assets/post-demo-roadmap.svg]]

---

## Key Blockers

| Blocker | Blocks | Status |
|---------|--------|--------|
| **Unified Data Access Layer (SQH-02 Core)** | LUM-01, LUM-02, MCP F1.7 | Not Started |
| **MCP Server Core (SQH-01 F1.1-1.4)** | Demo (Search + RAG tools) | Not Started |
| **Luminous Data (LUM-01, LUM-02)** | MCP F1.7 (Platform Group Tools) | Blocked by SQH-02 |

> **Note:** SQH-01 (MCP Core) and SQH-02 (Unified Data Access) are independent parallel tracks. LUM-01 and LUM-02 are also independent of each other - both need SQH-02, but neither blocks the other.

### Demo Descoped (Post-Demo)

| Feature | Reason | Workaround |
|---------|--------|------------|
| SQH-02 F2.8 (Access Control) | Requires SQH-08 | Use TeamScopedPermission |
| SQH-02 F2.10 (Shared Reference DB) | Not needed for demo | Water data in tenant DB |
| SQH-04 (UI Kit) | Claude Cowork is demo UI | MCP artifacts for visualizations |
| LUM-03 (Dashboard) | Claude Cowork is demo UI | Post-demo priority |

---

## Milestones

| Milestone                | Target  | Description                      |
| ------------------------ | ------- | -------------------------------- |
| **MVP: Pilot Ready**     | Q2 2026 | CNRL pilot minimum viable        |
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
