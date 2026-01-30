---
linear_id: SQU-5
linear_url: https://linear.app/squarehead/issue/SQU-5/epic-01-customer-dashboard
---

# EPIC-03: Customer Dashboard

**Linear:** [SQU-5](https://linear.app/squarehead/issue/SQU-5)
**Status:** 🔴 Not Started
**Priority:** Critical
**Owner:** Greg
**Target:** Q2 2026 (Before Pilot)

**Dependencies:**
- ⛔ **Blocked by:** Luminous Platform Group scaffolding (LUM-EPIC-01 Feature 1.0)
- ⛔ **Blocked by:** LUM-EPIC-01 Features 1.1-1.3 (no data to display without ingestion pipeline)
- 🔗 **Related:** LUM-EPIC-04 Feature 4.1 (Customer User Provisioning)
- 🔗 **Platform:** [SQH-EPIC-03 Platform Groups](../SquareHead/SQH-EPIC-03-Platform-Groups.md)

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

## Features

### Feature 3.1: User Authentication
**Linear:** [SQU-10](https://linear.app/squarehead/issue/SQU-10)
**Status:** 🟡 Partial (platform has auth, needs customer provisioning)
**Priority:** Critical
**Dependencies:** LUM-EPIC-04 Feature 4.1 (Customer User Provisioning)

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

#### Requirements
- Customer teams can be created and configured for Luminous access
- New users receive email invitations and can set their own passwords
- Viewer role sees data; admin role can invite users and configure settings
- Users can reset forgotten passwords without contacting support

**Existing Code:** `square_head/apps/users/`, `square_head/apps/teams/`

---

### Feature 3.2: Summary View
**Linear:** [SQU-11](https://linear.app/squarehead/issue/SQU-11)
**Status:** 🔴 Not Started
**Priority:** Critical
**Dependencies:** LUM-EPIC-01 Features 1.1, 1.2, 1.3 (data model, upload pipeline, sample linkage)
**Used By:**
- [LUM-EPIC-04 Feature 4.4](LUM-EPIC-04-Platform-Infrastructure.md) - PDF Reports

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

#### Requirements
- Each sample location displays its most recent NA reading
- Status indicators show color-coded thresholds (green=normal, yellow=elevated, red=critical)
- Last sample date is visible for each location
- Summary statistics show total sample count and average NA level across all sites

---

### Feature 3.3: Trend Charts
**Linear:** [SQU-12](https://linear.app/squarehead/issue/SQU-12)
**Status:** 🔴 Not Started
**Priority:** Critical
**Dependencies:** Feature 3.2 (Summary View), LUM-EPIC-01 Feature 1.1 (data model with timestamps)
**Used By:**
- [LUM-EPIC-04 Feature 4.4](LUM-EPIC-04-Platform-Infrastructure.md) - PDF Reports

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

#### Requirements
- Time-series chart displays NA concentration over time
- Users can select custom date ranges for analysis
- Results can be filtered by sample location
- Results can be filtered by biosensor panel type (atuA, marR, 3680)
- Charts can be exported as images for inclusion in reports

---

### Feature 3.4: Spatial View
**Linear:** [SQU-13](https://linear.app/squarehead/issue/SQU-13)
**Status:** 🔴 Not Started
**Priority:** High
**Dependencies:** Feature 3.2 (Summary View), LUM-EPIC-01 Feature 1.3 (sample metadata with GPS)

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

#### Requirements
- Location metadata (name, coordinates, site type) is displayed for each sampling point
- Results are organized and grouped by physical location
- NA levels show visual indicators (color/size) per location
- Map view shows sampling points when GPS coordinates are available (optional)

---

### Feature 3.5: Data Table & Export
**Linear:** [SQU-14](https://linear.app/squarehead/issue/SQU-14)
**Status:** 🔴 Not Started
**Priority:** Critical
**Dependencies:** LUM-EPIC-01 Features 1.1, 1.2, 1.3 (data to display)

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

#### Requirements
- Data table supports sorting and filtering on any column
- Users can show/hide columns to customize their view
- Filtered data can be exported to CSV format
- Data can be filtered by date range

---

### Feature 3.6: Correlation View
**Linear:** [SQU-15](https://linear.app/squarehead/issue/SQU-15)
**Status:** 🔴 Not Started
**Priority:** High
**Dependencies:** Feature 3.3 (Trend Charts), LUM-EPIC-01 Feature 1.4 (Contextual Data Integration)

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

#### Requirements
- Relational Context Engine is configured for Luminous data relationships
- Multi-axis chart displays NA levels alongside environmental factors (temperature, precipitation)
- Correlation strength is indicated visually when patterns exist
- Contextual data (weather, operational events) can be overlaid on trend charts

---

### Feature 3.7: Community Dashboard
**Linear:** TBD
**Status:** 🔴 Not Started
**Priority:** High
**Dependencies:** Features 3.2, 3.3 (data views to simplify)

#### Outcome
Indigenous communities and public stakeholders can view water quality status in plain language without technical expertise.

#### What Success Looks Like
- Community member visits public dashboard (no login required for public view)
- Sees simple status indicators: Safe / Monitoring / Concern
- Plain-language explanations: "Water quality is within normal range" vs technical metrics
- Can view trends without needing to interpret complex charts
- Educational content explains what is being measured and why it matters
- Available in multiple languages (English, French, Indigenous languages as needed)

#### Context
The Foundry storyline promises "simplified plain-language views for communities." This serves the transparency goal of building trust with stakeholders who have waited decades for progress on tailings remediation.

#### Scope: Owned Files
- `apps/platform_groups/luminous/views/community.py`
- `apps/platform_groups/luminous/templates/community/`
- `apps/platform_groups/luminous/ui_hints.yaml` (community view config)

#### Requirements
- Status thresholds are defined for Safe/Monitoring/Concern levels
- Each status level has plain-language explanations that non-technical users understand
- Trend visualization uses simple indicators (up/down/stable arrows) instead of complex charts
- Educational content explains what NA monitoring measures and why it matters
- All components meet WCAG 2.1 AA accessibility standards
- Multi-language support is available (English, French, Indigenous languages)
- Public users can view the community dashboard without authentication

---

### Feature 3.8: Operator Annotation System
**Linear:** TBD
**Status:** 🔴 Not Started
**Priority:** Medium
**Dependencies:** Features 3.2, 3.3 (data to annotate)
**Used By:**
- [LUM-EPIC-07 Feature 7.4](LUM-EPIC-07-Treatment-Intelligence.md) - Intervention Outcome Tracking

#### Outcome
Operators can capture institutional knowledge by annotating events, samples, and trends with notes about what happened and what actions were taken.

#### What Success Looks Like
- Operator views a spike in toxicity readings
- Clicks to add annotation: "Spike caused by heavy rainfall runoff. Increased flow to Cell 3, resolved within 48 hours."
- Annotation is permanently linked to that data point/period
- Future operators viewing similar conditions see the annotation
- Search finds past annotations matching current conditions
- Knowledge compounds over time rather than being lost to turnover

#### Context
The Foundry storyline emphasizes that "institutional knowledge remains trapped in PDF reports and spreadsheets. Personnel turnover means hard-won lessons get lost." This feature captures operator knowledge directly in the system.

#### Scope: Owned Files
- `apps/platform_groups/luminous/models/annotation.py`
- `apps/platform_groups/luminous/api/annotations.py`
- `apps/platform_groups/luminous/services/annotation_search.py`

#### Requirements
- Annotation model stores target type, target ID, content, operator, and timestamp
- Annotations can be created directly from any dashboard view
- Annotations are linked to samples, results, time periods, and events
- Tags categorize annotations by type: cause, action, outcome
- Search finds past annotations matching keywords or criteria
- "Similar situation" suggestions appear when viewing anomalies
- Annotation visibility can be set to team-only or public

---

## Technology Decision

**Status:** ⚠️ DECISION NEEDED - Blocks all EPIC-01 features

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
- Dashboard components need building (see [SQH-EPIC-04 Feature 4.4](../SquareHead/SQH-EPIC-04-Base-UI-Kit.md))

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
