---
linear_id: SQU-50
linear_url: https://linear.app/squarehead/issue/SQU-50
---

# EPIC-14: Tech Debt

**Linear:** [SQU-50](https://linear.app/squarehead/issue/SQU-50)
**Status:** Ongoing
**Priority:** Medium
**Owner:** TBD

---

## Vision

Technical debt is tracked, prioritized, and systematically addressed to maintain platform quality and developer productivity.

---

## User Stories

- As a **developer**, I can find and address TODOs without them getting lost
- As a **product owner**, I can see technical debt and make informed prioritization decisions
- As a **customer**, I receive email notifications when enabled (post-pilot)

---

## Context

Outstanding TODOs and incomplete features found throughout the codebase. This EPIC tracks them for visibility and prioritization.

---

## Features

### Feature 14.1: Email Notification Delivery
**Status:** Not Implemented
**Impact:** Medium (post-pilot per user decision)

#### Outcome
Users receive email notifications for important events.

#### Context
The notification framework exists (`apps/notifications/`) with in-app working. Email delivery not implemented.

#### Scope: Owned Files
- `apps/notifications/delivery/email.py`

#### Tasks
- [ ] Email delivery infrastructure
- [ ] Enable NotificationPreference `email_enabled` field
- [ ] Email templates

---

### Feature 14.2: Push Notification Support
**Status:** Not Implemented
**Impact:** Low

#### Outcome
Users receive push notifications on mobile devices.

#### Scope: Owned Files
- `apps/notifications/delivery/push.py`

#### Tasks
- [ ] Push notification infrastructure
- [ ] Mobile app integration

---

### Feature 14.3: Test Coverage Gaps
**Status:** Ongoing

#### Outcome
Critical paths have adequate test coverage.

#### Areas needing coverage:
- Dashboard functionality
- Email/push notification delivery
- End-to-end workflow escalation
- Some Modal AI service endpoints

#### Tasks
- [ ] Identify critical paths without tests
- [ ] Write tests for dashboard functionality
- [ ] Write tests for workflow escalation

---

### Feature 14.4: Support Ticket System
**Status:** Stub Only

#### Outcome
Users can submit support tickets and track their status.

#### Context
`apps/support/` has forms and views but no models for ticket tracking.

#### Scope: Owned Files
- `apps/support/models.py`
- `apps/support/views.py`

#### Tasks
- [ ] Define ticket data model
- [ ] Implement ticket creation flow
- [ ] Implement ticket status tracking

---

### Feature 14.5: Group Chat UI Integration
**Status:** Minimal

#### Outcome
Users can chat in groups with real-time updates.

#### Context
WebSocket consumer exists (`apps/group_chat/`) but minimal UI integration.

#### Scope: Owned Files
- `apps/group_chat/`
- `frontend/flutter/packages/chat/`

#### Tasks
- [ ] Flutter chat UI component
- [ ] WebSocket integration in UI

---

## Code Locations (TODOs)

| Item | File | Notes |
|------|------|-------|
| Task escalation | `apps/workflows/tasks.py` | Tracked in EPIC-06 |
| CDC secret resolution | `apps/cdc/services/connector_config_builders.py` | Tracked in EPIC-07 |
| BPMN role extraction | `apps/workflows/engine.py` | Tracked in EPIC-06 |
| Per-model Qdrant | `apps/documents/graph/search_service.py` | Tracked in EPIC-09 |
| Notification auto-retry | `apps/notifications/` | Part of 13.1/13.2 |
