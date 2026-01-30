---
status: "In Progress"
priority: "Medium"
assigned: ""
dependencies:
  - "Feature 4.1"
  - "LUM-EPIC-01 Feature 1.2"
linear_id: "SQU-23"
---

# Feature 4.2: Notification System

**Linear:** [SQU-23](https://linear.app/squarehead/issue/SQU-23)
**Status Note:** In-app only - email not implemented
**Priority Note:** Post-pilot - in-app sufficient for MVP

---

## Outcome

Customers are automatically notified when new results are available or when thresholds are breached.

---

## What Success Looks Like

- Customer logs in, sees notification badge
- Clicks to see "New results available for Site A"
- If NA exceeds threshold, sees alert notification
- (Post-pilot) Receives email for critical alerts

---

## Context

MVP uses in-app notifications only. Email/push delivery is post-pilot work.

---

## Scope: Owned Files

- `apps/platform_groups/luminous/notifications/` (Luminous-specific triggers)

## Out of Scope (Frozen)

- `square_head/apps/notifications/` (core notification framework)

---

## Requirements

### MVP (In-App Only)

- Users see in-app notifications when new results are available
- Each customer can configure their own alert thresholds
- In-app alerts appear when thresholds are breached

### Post-Pilot (Email/Push)

- Notifications can be delivered via email
- Push notification delivery is available
- Users can opt in/out of notification channels

**Note:** See [[../Squarehead/SQH-EPIC-14-Tech-Debt/00-Tech-Debt|SQH-EPIC-14 Tech Debt]] for platform-level notification work.
