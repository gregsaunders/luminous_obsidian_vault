# EPIC-03: Platform Infrastructure

**Status:** 🟡 Partial
**Priority:** High
**Owner:** Greg
**Target:** Q2 2026 (Before Pilot)

**Dependencies:**
- ⭐ **Foundational:** Mostly independent - enables EPIC-01
- 🔗 **Related:** EPIC-02 Feature 2.1 (audit trail covers biosensor data)

---

## Business Value

Core platform capabilities that support the customer experience: user management, notifications, and audit trails for regulatory compliance. Much of this infrastructure exists in the platform; it needs configuration and extension for Luminous use cases.

**Key Outcome:** Customers are provisioned, notified of results, and all data changes are auditable.

---

## Features

### Feature 3.1: Customer User Provisioning
**Status:** 🟡 Partial (framework exists)
**Priority:** High
**Dependencies:** None (foundational, enables EPIC-01 Feature 1.1)

Configure customer access to the platform.

**Tasks:**
- [ ] Customer team creation workflow
- [ ] Admin UI for creating customer teams
- [ ] User invitation email flow
- [ ] Role definitions (viewer, admin, API access)
- [ ] API key generation for integrations

**Existing Code:**
- `square_head/apps/teams/` - Multi-tenancy framework
- `square_head/apps/users/` - User management
- `square_head/apps/authentication/` - Auth flows

---

### Feature 3.2: Notification System
**Status:** 🟡 Partial (framework exists)
**Priority:** High
**Dependencies:** Feature 3.1 (users must exist to notify), EPIC-02 Feature 2.2 (results must exist to trigger alerts)

Alert customers when events occur.

**Tasks:**
- [ ] Email notification on new results available
- [ ] Threshold configuration per customer
- [ ] Email notification on threshold breach
- [ ] Notification preferences (opt-in/out)
- [ ] (Future) SMS notifications

**Existing Code:** `square_head/apps/notifications/`

---

### Feature 3.3: Audit Trail (Glass Box)
**Status:** 🟡 Partial (TerminusDB has capability)
**Priority:** Medium
**Dependencies:** EPIC-02 Feature 2.1 (data model to audit)

Immutable record of all data changes for regulatory compliance.

**Tasks:**
- [ ] Configure TerminusDB versioning for biosensor data
- [ ] Query interface for audit history
- [ ] "Who changed what when" reporting
- [ ] Export audit log for regulators
- [ ] Retention policy definition

**Existing:** TerminusDB provides built-in versioning; needs configuration for this use case.

---

### Feature 3.4: PDF Report Generation
**Status:** 🔴 Not Started
**Priority:** Medium
**Dependencies:** EPIC-01 Features 1.2, 1.3 (charts/views to include in PDF), EPIC-02 Features 2.1-2.3 (data to report on)

Generate downloadable PDF summaries for customers.

**Tasks:**
- [ ] Define report template (summary, trends, data table)
- [ ] PDF generation library integration
- [ ] Include charts/visualizations in PDF
- [ ] On-demand generation from dashboard
- [ ] (Future) Scheduled report emails

---

### Feature 3.5: API Documentation
**Status:** 🟡 Partial
**Priority:** Medium
**Dependencies:** EPIC-02 Features 2.2, 2.3 (APIs must exist to document)

Document APIs for customer integrations.

**Tasks:**
- [ ] OpenAPI/Swagger spec for Luminous endpoints
- [ ] Authentication documentation
- [ ] Example code snippets
- [ ] Rate limiting documentation

**Existing:** drf-spectacular provides OpenAPI generation

---

## References

- [Technology Requirements](../03-OPERATING-MODEL/03-Technology-Requirements.md)
- Teams app: `square_head/apps/teams/`
- Notifications app: `square_head/apps/notifications/`
- API app: `square_head/apps/api/`
