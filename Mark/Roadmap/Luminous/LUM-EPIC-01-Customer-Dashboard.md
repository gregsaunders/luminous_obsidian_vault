---
linear_id: SQU-5
linear_url: https://linear.app/squarehead/issue/SQU-5/epic-01-customer-dashboard
---

# EPIC-01: Customer Dashboard

**Linear:** [SQU-5](https://linear.app/squarehead/issue/SQU-5)
**Status:** 🔴 Not Started
**Priority:** Critical
**Owner:** Greg
**Target:** Q2 2026 (Before Pilot)

**Dependencies:**
- ⛔ **Blocked by:** Luminous Platform Group scaffolding (EPIC-02 Feature 2.0)
- ⛔ **Blocked by:** EPIC-02 Features 2.1-2.3 (no data to display without ingestion pipeline)
- 🔗 **Related:** EPIC-03 Feature 3.1 (Customer User Provisioning)
- 🔗 **Platform:** [SQH-EPIC-01 Platform Groups](../SquareHead/SQH-EPIC-01-Platform-Groups.md)

---

## Vision

Customers can log in and see their NA monitoring data with actionable insights, enabling them to make informed decisions about their environmental monitoring programs.

---

## User Stories

- As a **customer manager**, I can see the latest NA readings across all my sites so I know where to focus attention
- As a **site operator**, I can view trends at my location over time so I can identify patterns and anomalies
- As an **environmental analyst**, I can export raw data for my own analysis and reporting
- As a **regulatory compliance officer**, I can generate reports to satisfy audit requirements

---

## Context

Customers need a way to view their biosensor monitoring results. Without a dashboard, there's no way to deliver the core value proposition: "24-72 hour turnaround on NA monitoring with trend visualization."

---

## Features

### Feature 1.1: User Authentication
**Linear:** [SQU-10](https://linear.app/squarehead/issue/SQU-10)
**Status:** 🟡 Partial (platform has auth, needs customer provisioning)
**Priority:** Critical
**Dependencies:** EPIC-03 Feature 3.1 (Customer User Provisioning)

#### Outcome
A customer user can log in with their credentials and access only their team's data.

#### What Success Looks Like
- Customer receives invitation email, sets password
- Logs in and sees only their organization's data
- Admin users can invite new team members
- Users who forget passwords can reset them without support

#### Scope: Owned Files
- `apps/platform_groups/luminous/` (customer-specific auth config)

#### Out of Scope (Frozen)
- `square_head/apps/users/` (core platform)
- `square_head/apps/teams/` (core platform)
- `square_head/apps/authentication/` (core platform)

#### Tasks
- [ ] Customer team creation workflow
- [ ] Customer user invitation flow
- [ ] Role-based access (viewer vs admin)
- [ ] Password reset flow for customers

**Existing Code:** `square_head/apps/users/`, `square_head/apps/teams/`

---

### Feature 1.2: Summary View
**Linear:** [SQU-11](https://linear.app/squarehead/issue/SQU-11)
**Status:** 🔴 Not Started
**Priority:** Critical
**Dependencies:** EPIC-02 Features 2.1, 2.2, 2.3 (data model, upload pipeline, sample linkage)
**Used By:**
- [LUM-EPIC-03 Feature 3.4](LUM-EPIC-03-Platform-Infrastructure.md) - PDF Reports

#### Outcome
A customer can see an at-a-glance overview of their NA monitoring status across all sites.

#### What Success Looks Like
- Customer logs in, immediately sees current status
- Each location shows latest reading with color-coded status (green/yellow/red)
- Can tell at a glance if any site needs attention
- Quick stats show total samples and trends

#### Scope: Owned Files
- `apps/platform_groups/luminous/ui_hints.yaml` (summary view config)
- `apps/platform_groups/luminous/views/summary.py`

#### Tasks
- [ ] Latest NA reading per sample location
- [ ] Status indicators (normal/elevated/critical thresholds)
- [ ] Last sample date per location
- [ ] Quick stats (total samples, average NA level)

---

### Feature 1.3: Trend Charts
**Linear:** [SQU-12](https://linear.app/squarehead/issue/SQU-12)
**Status:** 🔴 Not Started
**Priority:** Critical
**Dependencies:** Feature 1.2 (Summary View), EPIC-02 Feature 2.1 (data model with timestamps)
**Used By:**
- [LUM-EPIC-03 Feature 3.4](LUM-EPIC-03-Platform-Infrastructure.md) - PDF Reports

#### Outcome
A customer can visualize NA levels over time to identify patterns, anomalies, and seasonal trends.

#### What Success Looks Like
- Customer selects a location and date range
- Sees a clear time-series chart of NA levels
- Can compare different panel types (atuA, marR, 3680)
- Can export chart as image for reports

#### Scope: Owned Files
- `apps/platform_groups/luminous/ui_hints.yaml` (chart config)
- `apps/platform_groups/luminous/views/trends.py`

#### Tasks
- [ ] Time-series chart component
- [ ] Date range selector
- [ ] Filter by sample location
- [ ] Filter by biosensor panel (atuA, marR, 3680)
- [ ] Export chart as image

---

### Feature 1.4: Spatial View
**Linear:** [SQU-13](https://linear.app/squarehead/issue/SQU-13)
**Status:** 🔴 Not Started
**Priority:** High
**Dependencies:** Feature 1.2 (Summary View), EPIC-02 Feature 2.3 (sample metadata with GPS)

#### Outcome
A customer can see results organized by physical location to understand spatial patterns in NA levels.

#### What Success Looks Like
- Customer views a list or map of sampling locations
- Each location shows current status and latest reading
- Can drill down into any location to see details
- Spatial patterns become visible (e.g., higher NA near certain areas)

#### Scope: Owned Files
- `apps/platform_groups/luminous/ui_hints.yaml` (spatial view config)
- `apps/platform_groups/luminous/views/spatial.py`

#### Tasks
- [ ] Location metadata display
- [ ] Results grouped by location
- [ ] Visual indicator of NA levels per location
- [ ] (Optional) Map integration if GPS coordinates available

---

### Feature 1.5: Data Table & Export
**Linear:** [SQU-14](https://linear.app/squarehead/issue/SQU-14)
**Status:** 🔴 Not Started
**Priority:** Critical
**Dependencies:** EPIC-02 Features 2.1, 2.2, 2.3 (data to display)

#### Outcome
A customer can access raw data, filter it, and export it for their own analysis or reporting.

#### What Success Looks Like
- Customer navigates to data table view
- Can sort and filter by any column
- Can select which columns to display
- Can export filtered results to CSV
- Exported data is complete and accurate for regulatory reporting

#### Scope: Owned Files
- `apps/platform_groups/luminous/ui_hints.yaml` (table config)
- `apps/platform_groups/luminous/api/export.py`

#### Tasks
- [ ] Sortable/filterable data table
- [ ] Column selection
- [ ] CSV export
- [ ] Date range filtering

---

### Feature 1.6: Correlation View
**Linear:** [SQU-15](https://linear.app/squarehead/issue/SQU-15)
**Status:** 🔴 Not Started
**Priority:** High
**Dependencies:** Feature 1.3 (Trend Charts), EPIC-02 Feature 2.4 (Contextual Data Integration)

#### Outcome
An analyst can view NA levels alongside environmental factors to identify correlations and potential causes.

#### What Success Looks Like
- Analyst views NA trend chart
- Can overlay weather data (temperature, precipitation)
- Can see if NA spikes correlate with rain events
- Insights help explain anomalies and inform operational decisions

#### Context
The correlation capability is powered by the **Relational Context Engine** - an existing SquareHead platform feature. This feature configures and exposes that capability for the Luminous use case, rather than building correlation logic from scratch.

#### Scope: Owned Files
- `apps/platform_groups/luminous/ui_hints.yaml` (correlation view config)
- `apps/platform_groups/luminous/views/correlation.py`

#### Tasks
- [ ] Configure Relational Context Engine for Luminous data relationships
- [ ] Multi-axis chart (NA + temperature, precipitation)
- [ ] Correlation indicators
- [ ] Contextual data overlay

---

## Technology Decision

**Status:** ⚠️ DECISION NEEDED - Blocks all EPIC-01 features

### Option A: Metabase (Embedded Analytics)

| Aspect | Details |
|--------|---------|
| **What it is** | Open-source BI tool, SQL-based dashboards |
| **Deployment** | Self-hosted or cloud (~$85/month) |
| **Dev effort** | Low - SQL queries + drag-and-drop |
| **Customization** | Limited - works within Metabase paradigms |
| **Integration** | Embedded iframes, separate auth |

**Pros:**
- Fast to deploy (1-2 weeks)
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
| **Dev effort** | Low-Medium - drag-and-drop + JS |
| **Customization** | Medium - flexible within Retool |
| **Integration** | API-first, custom auth possible |

**Pros:**
- Fast iteration (1-2 weeks)
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
| **Dev effort** | Medium-High (4-8 weeks) |
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
- Dashboard components need building (see [SQH-EPIC-02 Feature 2.4](../SquareHead/SQH-EPIC-02-Base-UI-Kit.md))

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

**Status:** 🔴 Not Started
**Priority:** Critical
**Deadline:** 1 week timeboxed

#### Outcome
Team has made an informed decision on dashboard technology with a working proof-of-concept.

#### Tasks
- [ ] Set up Metabase with sample biosensor data (2 days)
- [ ] Set up Retool with sample biosensor data (2 days)
- [ ] Build minimal Flutter dashboard view with ui_hints.yaml (2 days)
- [ ] Document pros/cons from hands-on evaluation
- [ ] Team decision meeting and commit to approach

---

## References

- [Technology Requirements - Dashboard Section](../../03-OPERATING-MODEL/03-Technology-Requirements.md)
- [Pilot Deliverables Framework](../../03-OPERATING-MODEL/05-Pilot-Deliverables-Framework.md)
- [Platform Groups Architecture](../SquareHead/SQH-EPIC-01-Platform-Groups.md)
- CRM ui_hints.yaml reference: `square_head/apps/platform_groups/crm/ui_hints.yaml`
- Flutter workflow forms: `square_head/frontend/flutter/packages/workflows/`
