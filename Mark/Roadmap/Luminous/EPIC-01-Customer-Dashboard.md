# EPIC-01: Customer Dashboard

**Status:** 🔴 Not Started
**Priority:** Critical
**Owner:** Greg
**Target:** Q2 2026 (Before Pilot)

**Dependencies:**
- ⛔ **Blocked by:** Luminous Platform Group scaffolding (EPIC-02 Feature 2.0)
- ⛔ **Blocked by:** EPIC-02 Features 2.1-2.3 (no data to display without ingestion pipeline)
- 🔗 **Related:** EPIC-03 Feature 3.1 (Customer User Provisioning)
- 🔗 **Platform:** [SquareHead EPIC-01 Platform Groups](../SquareHead/EPIC-01-Platform-Groups.md)

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

Currently, results are delivered via email or manual reports. This is slow, doesn't scale, and doesn't allow customers to explore their data.

---

## Features

### Feature 1.1: User Authentication
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
**Status:** 🔴 Not Started
**Priority:** Critical
**Dependencies:** EPIC-02 Features 2.1, 2.2, 2.3 (data model, upload pipeline, sample linkage)

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
**Status:** 🔴 Not Started
**Priority:** Critical
**Dependencies:** Feature 1.2 (Summary View), EPIC-02 Feature 2.1 (data model with timestamps)

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

#### Scope: Owned Files
- `apps/platform_groups/luminous/ui_hints.yaml` (correlation view config)
- `apps/platform_groups/luminous/views/correlation.py`

#### Tasks
- [ ] Multi-axis chart (NA + temperature, precipitation)
- [ ] Correlation indicators
- [ ] Contextual data overlay

---

## Technology Approach

The dashboard will be built using **Flutter + Platform Groups (ui_hints.yaml)**, consistent with the existing platform architecture.

**Why Flutter + ui_hints.yaml:**
- Fully integrated with platform architecture
- Reusable patterns from CRM reference implementation
- AI can generate/modify ui_hints.yaml configurations
- Native desktop/mobile/web apps from single codebase
- No vendor dependency or dual-auth complexity

**Implementation approach:**

Views are defined declaratively in `ui_hints.yaml`:

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

**Dependencies:**
- Dashboard chart components from [SquareHead EPIC-02 Feature 2.4](../SquareHead/EPIC-02-Base-UI-Kit.md)
- Platform Groups loader from [SquareHead EPIC-01](../SquareHead/EPIC-01-Platform-Groups.md)

---

## References

- [Technology Requirements - Dashboard Section](../../03-OPERATING-MODEL/03-Technology-Requirements.md)
- [Pilot Deliverables Framework](../../03-OPERATING-MODEL/05-Pilot-Deliverables-Framework.md)
- [Platform Groups Architecture](../SquareHead/EPIC-01-Platform-Groups.md)
- CRM ui_hints.yaml reference: `square_head/apps/platform_groups/crm/ui_hints.yaml`
- Flutter workflow forms: `square_head/frontend/flutter/packages/workflows/`
