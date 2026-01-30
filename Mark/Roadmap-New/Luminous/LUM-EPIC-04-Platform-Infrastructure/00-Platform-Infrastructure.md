---
status: "In Progress"
priority: "High"
epic_id: "LUM-EPIC-04"
linear_id: "SQU-7"
linear_url: "https://linear.app/squarehead/issue/SQU-7/epic-03-platform-infrastructure"
---

# EPIC-04: Platform Infrastructure

**Linear:** [SQU-7](https://linear.app/squarehead/issue/SQU-7)
**Owner:** Greg
**Target:** Q2 2026 (Before Pilot)

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

## Dependencies

- **Foundational:** Mostly independent - enables LUM-EPIC-01
- **Related:** LUM-EPIC-01 Feature 1.1 (audit trail covers biosensor data)

---

## Features

- [[Feature 4.1 Customer User Provisioning]]
- [[Feature 4.2 Notification System]]
- [[Feature 4.3 Audit Trail (Glass Box)]]
- [[Feature 4.4 PDF Report Generation]]
- [[Feature 4.5 API Documentation]]
- [[Feature 4.6 Pilot UAT Process]]

---

## References

- [Technology Requirements](../../03-OPERATING-MODEL/03-Technology-Requirements.md)
- [[../Squarehead/SQH-00-Backlog-Index|SquareHead Platform Backlog]]
- [[../Squarehead/SQH-EPIC-14-Tech-Debt/00-Tech-Debt|SQH-EPIC-14 Tech Debt]] - Notification delivery work
- Teams app: `square_head/apps/teams/`
- Notifications app: `square_head/apps/notifications/`
- API app: `square_head/apps/api/`
