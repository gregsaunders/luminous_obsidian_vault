# EPIC-12: Tech Debt

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

### Feature 12.1: Email Notification Delivery
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

### Feature 12.2: Push Notification Support
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

### Feature 12.3: Test Coverage Gaps
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

### Feature 12.4: Support Ticket System
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

### Feature 12.5: Group Chat UI Integration
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
| Task escalation | `apps/workflows/tasks.py` | Tracked in EPIC-05 |
| CDC secret resolution | `apps/cdc/services/connector_config_builders.py` | Tracked in EPIC-06 |
| BPMN role extraction | `apps/workflows/engine.py` | Tracked in EPIC-05 |
| Per-model Qdrant | `apps/documents/graph/search_service.py` | Tracked in EPIC-08 |
| Notification auto-retry | `apps/notifications/` | Part of 12.1/12.2 |
