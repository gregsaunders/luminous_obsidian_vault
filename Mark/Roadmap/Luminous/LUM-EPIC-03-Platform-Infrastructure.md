# EPIC-03: Platform Infrastructure

**Status:** 🟡 Partial
**Priority:** High
**Owner:** Greg
**Target:** Q2 2026 (Before Pilot)

**Dependencies:**
- ⭐ **Foundational:** Mostly independent - enables EPIC-01
- 🔗 **Related:** EPIC-02 Feature 2.1 (audit trail covers biosensor data)

---

## Vision

Customers are provisioned efficiently, stay informed through notifications, and all data changes are auditable for regulatory compliance.

---

## User Stories

- As a **Luminous admin**, I can create customer teams and invite users without developer involvement
- As a **customer**, I receive notifications when new results are available so I don't have to check manually
- As a **regulator**, I can request an audit trail of all data changes to verify data integrity
- As a **customer manager**, I can download PDF reports to share with stakeholders who don't have platform access

---

## Context

Core platform capabilities that support the customer experience: user management, notifications, and audit trails for regulatory compliance. Much of this infrastructure exists in the platform; it needs configuration and extension for Luminous use cases.

---

## Features

### Feature 3.1: Customer User Provisioning
**Status:** 🟡 Partial (framework exists)
**Priority:** High
**Dependencies:** None (foundational, enables EPIC-01 Feature 1.1)

#### Outcome
A Luminous admin can create customer teams and invite users through a self-service workflow.

#### What Success Looks Like
- Admin creates new customer team from admin panel
- Enters customer info, clicks "Create"
- Invites users by email address
- Users receive invitation, set password, gain access
- No developer involvement required

#### Scope: Owned Files
- `apps/platform_groups/luminous/admin/` (customer admin UI)

#### Out of Scope (Frozen)
- `square_head/apps/teams/` - Multi-tenancy framework (core)
- `square_head/apps/users/` - User management (core)
- `square_head/apps/authentication/` - Auth flows (core)

#### Tasks
- [ ] Customer team creation workflow
- [ ] Admin UI for creating customer teams
- [ ] User invitation email flow
- [ ] Role definitions (viewer, admin, API access)
- [ ] API key generation for integrations

---

### Feature 3.2: Notification System
**Status:** 🟡 Partial (in-app only - email not implemented)
**Priority:** Medium (post-pilot - in-app sufficient for MVP)
**Dependencies:** Feature 3.1 (users must exist to notify), EPIC-02 Feature 2.2 (results must exist to trigger alerts)

#### Outcome
Customers are automatically notified when new results are available or when thresholds are breached.

#### What Success Looks Like
- Customer logs in, sees notification badge
- Clicks to see "New results available for Site A"
- If NA exceeds threshold, sees alert notification
- (Post-pilot) Receives email for critical alerts

#### Context
MVP uses in-app notifications only. Email/push delivery is post-pilot work.

#### Scope: Owned Files
- `apps/platform_groups/luminous/notifications/` (Luminous-specific triggers)

#### Out of Scope (Frozen)
- `square_head/apps/notifications/` (core notification framework)

#### Tasks

**MVP (In-App Only):**
- [ ] In-app notification on new results available
- [ ] Threshold configuration per customer
- [ ] In-app notification on threshold breach

**Post-Pilot (Email/Push):**
- [ ] Email notification delivery
- [ ] Push notification support
- [ ] Notification preferences (opt-in/out)

**Note:** See [SQH-EPIC-08 Tech Debt](../SquareHead/SQH-EPIC-08-Tech-Debt.md) for platform-level notification work.

---

### Feature 3.3: Audit Trail (Glass Box)
**Status:** 🟡 Partial (TerminusDB has capability)
**Priority:** Medium
**Dependencies:** EPIC-02 Feature 2.1 (data model to audit)

#### Outcome
A regulator or auditor can request a complete history of all data changes for any biosensor record.

#### What Success Looks Like
- Auditor requests history for a specific sample
- System shows every change: who, what, when
- Export as CSV/PDF for compliance documentation
- Data cannot be altered retroactively without trace

#### Context
TerminusDB provides built-in versioning. This feature configures it for Luminous data and exposes the audit trail to users.

#### Scope: Owned Files
- `apps/platform_groups/luminous/audit/` (audit views and exports)

#### Tasks
- [ ] Configure TerminusDB versioning for biosensor data
- [ ] Query interface for audit history
- [ ] "Who changed what when" reporting
- [ ] Export audit log for regulators
- [ ] Retention policy definition
- [ ] Regulatory audit dashboard (visual chain: Field Scan → Lab Receipt → Plate Reader → Platform Ingestion)

---

### Feature 3.4: PDF Report Generation
**Status:** 🔴 Not Started
**Priority:** Medium
**Dependencies:** EPIC-01 Features 1.2, 1.3 (charts/views to include in PDF), EPIC-02 Features 2.1-2.3 (data to report on)

#### Outcome
A customer can download a professional PDF report to share with stakeholders who don't have platform access.

#### What Success Looks Like
- Customer clicks "Generate Report" in dashboard
- Selects date range and locations to include
- Downloads PDF with summary, trends, and data table
- Report is branded and professional-looking
- Can be attached to regulatory filings

#### Scope: Owned Files
- `apps/platform_groups/luminous/reports/` (report generation)
- `apps/platform_groups/luminous/templates/pdf/` (report templates)

#### Tasks
- [ ] Define report template (summary, trends, data table)
- [ ] PDF generation library integration
- [ ] Include charts/visualizations in PDF
- [ ] On-demand generation from dashboard
- [ ] AER compliance report template (regulator-ready format with data provenance)
- [ ] Indigenous community report template (visual, accessible, plain language)
- [ ] (Future) Scheduled report emails

---

### Feature 3.5: API Documentation
**Status:** 🟡 Partial
**Priority:** Medium
**Dependencies:** EPIC-02 Features 2.2, 2.3 (APIs must exist to document)

#### Outcome
A customer's developer can integrate with Luminous APIs using clear, accurate documentation.

#### What Success Looks Like
- Developer visits API docs page
- Sees all available endpoints with descriptions
- Can try endpoints interactively
- Copy-paste example code works
- Rate limits and auth are clearly documented

#### Context
drf-spectacular provides OpenAPI generation. This feature ensures Luminous endpoints are well-documented.

#### Scope: Owned Files
- `apps/platform_groups/luminous/api/` (docstrings and schema)
- `docs/api/luminous/` (additional documentation)

#### Tasks
- [ ] OpenAPI/Swagger spec for Luminous endpoints
- [ ] Authentication documentation
- [ ] Example code snippets
- [ ] Rate limiting documentation

---

## References

- [Technology Requirements](../../03-OPERATING-MODEL/03-Technology-Requirements.md)
- [SquareHead Platform Backlog](../SquareHead/SQH-00-Backlog-Index.md)
- [SQH-EPIC-08 Tech Debt](../SquareHead/SQH-EPIC-08-Tech-Debt.md) - Notification delivery work
- Teams app: `square_head/apps/teams/`
- Notifications app: `square_head/apps/notifications/`
- API app: `square_head/apps/api/`
