# EPIC-01: Customer Dashboard

**Status:** 🔴 Not Started
**Priority:** Critical
**Owner:** Greg
**Target:** Q2 2026 (Before Pilot)

---

## Business Value

Customers need a way to view their biosensor monitoring results. Without a dashboard, there's no way to deliver the core value proposition: "24-72 hour turnaround on NA monitoring with trend visualization."

**Key Outcome:** Customers can log in and see their NA monitoring data with actionable insights.

---

## Features

### Feature 1.1: User Authentication
**Status:** 🟡 Partial (platform has auth, needs customer provisioning)
**Priority:** Critical

Enable customers to log in and access their team's data.

**Tasks:**
- [ ] Customer team creation workflow
- [ ] Customer user invitation flow
- [ ] Role-based access (viewer vs admin)
- [ ] Password reset flow for customers

**Existing Code:** `square_head/apps/users/`, `square_head/apps/teams/`

---

### Feature 1.2: Summary View
**Status:** 🔴 Not Started
**Priority:** Critical

Dashboard landing page showing latest results at a glance.

**Tasks:**
- [ ] Latest NA reading per sample location
- [ ] Status indicators (normal/elevated/critical thresholds)
- [ ] Last sample date per location
- [ ] Quick stats (total samples, average NA level)

---

### Feature 1.3: Trend Charts
**Status:** 🔴 Not Started
**Priority:** Critical

Visualize NA levels over time to identify patterns.

**Tasks:**
- [ ] Time-series chart component
- [ ] Date range selector
- [ ] Filter by sample location
- [ ] Filter by biosensor panel (atuA, marR, 3680)
- [ ] Export chart as image

---

### Feature 1.4: Spatial View
**Status:** 🔴 Not Started
**Priority:** High

Show results by sample location (map or location grid).

**Tasks:**
- [ ] Location metadata display
- [ ] Results grouped by location
- [ ] Visual indicator of NA levels per location
- [ ] (Optional) Map integration if GPS coordinates available

---

### Feature 1.5: Data Table & Export
**Status:** 🔴 Not Started
**Priority:** Critical

Raw data access with filtering and export.

**Tasks:**
- [ ] Sortable/filterable data table
- [ ] Column selection
- [ ] CSV export
- [ ] Date range filtering

---

### Feature 1.6: Correlation View
**Status:** 🔴 Not Started
**Priority:** High

Show NA levels alongside contextual factors (weather, dosing).

**Tasks:**
- [ ] Multi-axis chart (NA + temperature, precipitation)
- [ ] Correlation indicators
- [ ] Contextual data overlay

**Dependencies:** EPIC-02 Feature 2.3 (Contextual Data Integration)

---

## Technology Decision

**Options:**
1. **Metabase** - Off-the-shelf BI tool, fast to deploy, limited customization
2. **Retool** - Low-code platform, faster than custom, moderate flexibility
3. **Custom (Flutter/React)** - Full control, more effort, fits existing stack

**Recommendation:** TBD (Greg to evaluate)

---

## References

- [Technology Requirements - Dashboard Section](../03-OPERATING-MODEL/03-Technology-Requirements.md)
- [Pilot Deliverables Framework](../03-OPERATING-MODEL/05-Pilot-Deliverables-Framework.md)
- Existing admin dashboard: `square_head/apps/dashboard/`
