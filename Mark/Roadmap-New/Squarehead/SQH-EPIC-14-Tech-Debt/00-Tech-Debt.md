---
status: "In Progress"
priority: "Medium"
epic_id: "SQH-EPIC-14"
linear_id: "SQU-50"
linear_url: "https://linear.app/squarehead/issue/SQU-50"
---

# EPIC-14: Tech Debt

## Vision

Technical debt is tracked, prioritized, and systematically addressed to maintain platform quality and developer productivity.

## User Stories

- As a **developer**, I can find and address TODOs without them getting lost
- As a **product owner**, I can see technical debt and make informed prioritization decisions
- As a **customer**, I receive email notifications when enabled (post-pilot)

## Context

Outstanding TODOs and incomplete features found throughout the codebase. This EPIC tracks them for visibility and prioritization.

## Features

- [[Feature 14.1 Email Notification Delivery]]
- [[Feature 14.2 Push Notification Support]]
- [[Feature 14.3 Test Coverage Gaps]]
- [[Feature 14.4 Support Ticket System]]
- [[Feature 14.5 Group Chat UI Integration]]

## Code Locations (TODOs)

| Item | File | Notes |
|------|------|-------|
| Task escalation | `apps/workflows/tasks.py` | Tracked in EPIC-06 |
| CDC secret resolution | `apps/cdc/services/connector_config_builders.py` | Tracked in EPIC-07 |
| BPMN role extraction | `apps/workflows/engine.py` | Tracked in EPIC-06 |
| Per-model Qdrant | `apps/documents/graph/search_service.py` | Tracked in EPIC-09 |
| Notification auto-retry | `apps/notifications/` | Part of 14.1/14.2 |
