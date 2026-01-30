---
status: "Not Started"
priority: "Critical"
epic_id: "LUM-EPIC-03"
linear_id: "SQU-5"
linear_url: "https://linear.app/squarehead/issue/SQU-5/epic-01-customer-dashboard"
---

# EPIC-03: Customer Dashboard

**Linear:** [SQU-5](https://linear.app/squarehead/issue/SQU-5)
**Owner:** Greg
**Target:** Q2 2026 (Before Pilot)

---

## Vision

Customers can log in and see their NA monitoring data with actionable insights, enabling them to make informed decisions about their environmental monitoring programs.

---

## User Stories

- As a **customer manager**, I can see the latest NA readings across all my sites so I know where to focus attention
- As a **site operator**, I can view trends at my location over time so I can identify patterns and anomalies
- As an **environmental analyst**, I can export raw data for my own analysis and reporting
- As a **regulatory compliance officer**, I can generate reports to satisfy audit requirements
- As a **community member**, I can view water quality status in plain language so I can understand if the water is safe
- As a **site operator**, I can annotate events with what I observed and what actions I took so future operators can learn from my experience

---

## Context

Customers need a way to view their biosensor monitoring results. Without a dashboard, there's no way to deliver the core value proposition: "24-72 hour turnaround on NA monitoring with trend visualization."

---

## Dependencies

- **Blocked by:** Luminous Platform Group scaffolding (LUM-EPIC-01 Feature 1.0)
- **Blocked by:** LUM-EPIC-01 Features 1.1-1.3 (no data to display without ingestion pipeline)
- **Related:** LUM-EPIC-04 Feature 4.1 (Customer User Provisioning)
- **Platform:** [[../Squarehead/SQH-EPIC-03-Platform-Groups/00-Platform-Groups|SQH-EPIC-03 Platform Groups]]

---

## Features

- [[Feature 3.1 User Authentication]]
- [[Feature 3.2 Summary View]]
- [[Feature 3.3 Trend Charts]]
- [[Feature 3.4 Spatial View]]
- [[Feature 3.5 Data Table & Export]]
- [[Feature 3.6 Correlation View]]
- [[Feature 3.7 Community Dashboard]]
- [[Feature 3.8 Operator Annotation System]]

---

## Technology Decision

**Status:** DECISION NEEDED - Blocks all EPIC-01 features

### Option A: Metabase (Embedded Analytics)

| Aspect | Details |
|--------|---------|
| **What it is** | Open-source BI tool, SQL-based dashboards |
| **Deployment** | Self-hosted or cloud (~$85/month) |
| **Dev effort** | Small - SQL queries + drag-and-drop |
| **Customization** | Limited - works within Metabase paradigms |
| **Integration** | Embedded iframes, separate auth |

**Pros:**
- Fast to deploy (Effort: Small)
- Good for pilot validation - learn what customers want
- Non-developers can modify dashboards

**Cons:**
- Separate system from main platform
- Limited customization for biosensor-specific views
- Dual auth complexity (platform + Metabase)

---

### Option B: Retool (Low-Code Internal Tools)

| Aspect | Details |
|--------|---------|
| **What it is** | Low-code platform for internal tools |
| **Deployment** | Cloud (~$10-50/user/month) |
| **Dev effort** | Small-Medium - drag-and-drop + JS |
| **Customization** | Medium - flexible within Retool |
| **Integration** | API-first, custom auth possible |

**Pros:**
- Fast iteration (Effort: Small)
- Can connect directly to APIs
- Good for CRUD operations

**Cons:**
- Vendor lock-in, subscription cost
- Not designed for customer-facing dashboards
- Another system to maintain

---

### Option C: Custom Flutter + Platform Groups (ui_hints.yaml)

| Aspect | Details |
|--------|---------|
| **What it is** | Native Flutter app using Platform Groups dynamic UI |
| **Deployment** | Web/Desktop/Mobile via existing Flutter infrastructure |
| **Dev effort** | Medium-Large |
| **Customization** | Full - complete control |
| **Integration** | Native - same codebase as platform |

**Pros:**
- Fully integrated with platform architecture
- Reusable patterns from CRM reference
- AI can generate/modify ui_hints.yaml
- Native desktop/mobile apps possible
- No vendor dependency

**Cons:**
- More upfront development
- Requires Flutter expertise
- Dashboard components need building (see [[../Squarehead/SQH-EPIC-04-Base-UI-Kit/Feature 4.4 Dashboard Components|SQH-EPIC-04 Feature 4.4]])

**If chosen, views would be defined in `ui_hints.yaml`:**

```yaml
models:
  LuminousBiosensorResult:
    display_name: "Biosensor Result"
    list_columns: [sample_id, panel_type, na_concentration, detection_date]
    detail_sections:
      - title: "Result Details"
        fields: [na_concentration, qc_status, lab_tech]
      - title: "Sample Info"
        fields: [sample_location, collection_date]
```

---

### Recommendation

Per [Technology Requirements](../../03-OPERATING-MODEL/03-Technology-Requirements.md):

> Use **Metabase or Retool** for pilot to validate what customers want. Build custom dashboard after pilot feedback.

**Questions to answer:**
1. Is speed-to-pilot more important than long-term architecture?
2. How much customization do we need for biosensor-specific visualizations?
3. Do we want native desktop/mobile apps or web-only?
4. Are we comfortable with the dual-auth complexity of embedded analytics?

---

### Dashboard Technology Spike

**Status:** Not Started
**Priority:** Critical
**Effort:** Small (timeboxed)

#### Outcome
Team has made an informed decision on dashboard technology with a working proof-of-concept.

#### Requirements
- Metabase is set up with sample biosensor data for evaluation
- Retool is set up with sample biosensor data for evaluation
- Minimal Flutter dashboard view is built using ui_hints.yaml pattern
- Pros/cons documented from hands-on evaluation of each option
- Team decision meeting held and approach committed

---

## References

- [Technology Requirements - Dashboard Section](../../03-OPERATING-MODEL/03-Technology-Requirements.md)
- [Pilot Deliverables Framework](../../03-OPERATING-MODEL/05-Pilot-Deliverables-Framework.md)
- [Platform Groups Architecture](../SquareHead/SQH-EPIC-03-Platform-Groups.md)
- CRM ui_hints.yaml reference: `square_head/apps/platform_groups/crm/ui_hints.yaml`
- Flutter workflow forms: `square_head/frontend/flutter/packages/workflows/`
