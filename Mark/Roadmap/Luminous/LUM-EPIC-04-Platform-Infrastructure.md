---
linear_id: SQU-7
linear_url: https://linear.app/squarehead/issue/SQU-7/epic-03-platform-infrastructure
---

# EPIC-04: Platform Infrastructure

**Linear:** [SQU-7](https://linear.app/squarehead/issue/SQU-7)
**Status:** 🟡 Partial
**Priority:** High
**Owner:** Greg
**Target:** Q2 2026 (Before Pilot)

**Dependencies:**
- ⭐ **Foundational:** Mostly independent - enables LUM-EPIC-01
- 🔗 **Related:** LUM-EPIC-01 Feature 1.1 (audit trail covers biosensor data)

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

### Feature 4.1: Customer User Provisioning
**Linear:** [SQU-22](https://linear.app/squarehead/issue/SQU-22)
**Status:** 🟡 Partial (framework exists)
**Priority:** High
**Dependencies:** None (foundational, enables LUM-EPIC-01 Feature 1.1)
**Used By:**
- [LUM-EPIC-03 Feature 3.1](LUM-EPIC-03-Customer-Dashboard.md) - User Authentication
- [LUM-EPIC-05 Feature 5.3](LUM-EPIC-05-Field-Operations.md) - Sample Kit Management

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

#### Requirements
- Customer teams can be created through a self-service workflow
- Admin UI allows creating and managing customer teams without developer help
- User invitations are sent via email with account setup instructions
- Roles are defined: viewer (read-only), admin (manage users), API access (integration)
- API keys can be generated for customer integrations

#### Platform Capabilities (Reuse)
Luminous leverages existing SquareHead team management:
- **RBAC** (`apps/teams/roles.py`) - Admin/Editor/Viewer roles ready to use
- **Invitations** (`apps/teams/invitations.py`) - Email invite flow implemented
- **Auto-provisioning** (`apps/teams/signals.py`) - Storage auto-created on team setup

**Luminous-Specific Requirements:**
- Customer onboarding checklist documents the provisioning process
- Welcome email uses Luminous-branded template
- New customers can configure their alert thresholds during setup

---

### Feature 4.2: Notification System
**Linear:** [SQU-23](https://linear.app/squarehead/issue/SQU-23)
**Status:** 🟡 Partial (in-app only - email not implemented)
**Priority:** Medium (post-pilot - in-app sufficient for MVP)
**Dependencies:** Feature 4.1 (users must exist to notify), LUM-EPIC-01 Feature 1.2 (results must exist to trigger alerts)

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

#### Requirements

**MVP (In-App Only):**
- Users see in-app notifications when new results are available
- Each customer can configure their own alert thresholds
- In-app alerts appear when thresholds are breached

**Post-Pilot (Email/Push):**
- Notifications can be delivered via email
- Push notification delivery is available
- Users can opt in/out of notification channels

**Note:** See [SQH-EPIC-13 Tech Debt](../SquareHead/SQH-EPIC-13-Tech-Debt.md) for platform-level notification work.

---

### Feature 4.3: Audit Trail (Glass Box)
**Linear:** [SQU-24](https://linear.app/squarehead/issue/SQU-24)
**Status:** 🟡 Partial (TerminusDB has capability)
**Priority:** Medium
**Dependencies:** LUM-EPIC-01 Feature 1.1 (data model to audit)

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

#### Requirements
- TerminusDB versioning is configured for all biosensor data
- Query interface allows retrieving audit history for any record
- Reports show "who changed what when" for any data point
- Audit logs can be exported for regulator review (CSV/PDF)
- Data retention policy is defined and enforced
- Regulatory audit dashboard visualizes full chain: Field Scan → Lab Receipt → Plate Reader → Platform Ingestion

---

### Feature 4.4: PDF Report Generation
**Linear:** [SQU-25](https://linear.app/squarehead/issue/SQU-25)
**Status:** 🔴 Not Started
**Priority:** Medium
**Dependencies:** LUM-EPIC-01 Features 1.2, 1.3 (charts/views to include in PDF), LUM-EPIC-01 Features 1.1-1.3 (data to report on)

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

#### Requirements
- Report template includes summary, trends, and data table sections
- PDF generation produces downloadable documents
- Charts and visualizations are rendered in PDF output
- Reports can be generated on-demand from the dashboard
- AER compliance template is regulator-ready with data provenance
- Indigenous community template is visual, accessible, and uses plain language

#### Future Scope
- Scheduled report emails

---

### Feature 4.5: API Documentation
**Linear:** [SQU-26](https://linear.app/squarehead/issue/SQU-26)
**Status:** 🟡 Partial
**Priority:** Medium
**Dependencies:** LUM-EPIC-01 Features 1.2, 1.3 (APIs must exist to document)

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

#### Requirements
- OpenAPI/Swagger spec is generated for all Luminous endpoints
- Authentication is documented with examples
- Code snippets demonstrate common integrations
- Rate limits are documented with error handling guidance

---

### Feature 4.6: Pilot UAT Process
**Linear:** [SQU-27](https://linear.app/squarehead/issue/SQU-27)
**Status:** 🔴 Not Started
**Priority:** High
**Dependencies:** EPIC-01, EPIC-02, EPIC-04 (features to test)

#### Outcome
CNRL validates the system meets their needs before go-live, with documented sign-off.

#### What Success Looks Like
- UAT test plan created with CNRL
- Test scenarios cover all critical workflows
- CNRL executes tests with Luminous support
- Issues tracked and resolved
- Formal sign-off before production launch

#### Requirements
- UAT test plan documents all scenarios and acceptance criteria
- Test environment is provisioned using existing E2E patterns
- CNRL receives UAT training session before testing
- Issues discovered during UAT are tracked to resolution
- Sign-off checklist and approval workflow documents formal acceptance

---

## References

- [Technology Requirements](../../03-OPERATING-MODEL/03-Technology-Requirements.md)
- [SquareHead Platform Backlog](../SquareHead/SQH-00-Backlog-Index.md)
- [SQH-EPIC-13 Tech Debt](../SquareHead/SQH-EPIC-13-Tech-Debt.md) - Notification delivery work
- Teams app: `square_head/apps/teams/`
- Notifications app: `square_head/apps/notifications/`
- API app: `square_head/apps/api/`
