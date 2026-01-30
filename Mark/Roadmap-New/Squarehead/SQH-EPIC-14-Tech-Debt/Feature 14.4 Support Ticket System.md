---
status: "Not Started"
priority: "Low"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 14.4: Support Ticket System

## Outcome

Users can submit support tickets and track their status.

## What Success Looks Like

- Users can create support tickets
- Ticket status is trackable
- Support team can manage tickets

## Context

`apps/support/` has forms and views but no models for ticket tracking.

## Scope: Owned Files

- `apps/support/models.py`
- `apps/support/views.py`

## Requirements

- Define ticket data model
- Implement ticket creation flow
- Implement ticket status tracking
