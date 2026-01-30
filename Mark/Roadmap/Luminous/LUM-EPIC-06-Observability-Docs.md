---
linear_id: SQU-9
linear_url: https://linear.app/squarehead/issue/SQU-9/epic-05-observability-and-docs
---

# EPIC-06: Observability & Documentation

**Linear:** [SQU-9](https://linear.app/squarehead/issue/SQU-9)
**Status:** 🟡 Partial
**Priority:** Medium
**Owner:** Greg
**Target:** Ongoing / During Pilot

**Dependencies:**
- 🟢 **Independent:** Can progress in parallel with other EPICs
- 🔗 **Related:** All EPICs (documentation covers entire platform)

---

## Vision

The team can monitor platform health in real-time and new contributors can onboard quickly with clear documentation.

---

## User Stories

- As an **operator**, I can see platform health at a glance so I can respond to issues before customers notice
- As a **new developer**, I can set up my local environment and understand the architecture within a day
- As a **on-call engineer**, I have runbooks for common issues so I can resolve incidents quickly
- As a **team lead**, I can point new team members to documentation instead of explaining things repeatedly

---

## Context

Platform observability ensures reliability during pilot operations. Documentation enables team scaling and knowledge transfer. These are not blockers for pilot launch but significantly improve operational readiness.

---

## Features

### Feature 6.1: Platform Monitoring Dashboard
**Linear:** [SQU-33](https://linear.app/squarehead/issue/SQU-33)
**Status:** 🟡 Partial (infrastructure exists)
**Priority:** Medium
**Dependencies:** None (infrastructure exists, just needs Luminous-specific dashboards)

#### Outcome
An operator can see Luminous platform health at a glance and get alerted to issues.

#### What Success Looks Like
- Operator opens Grafana, sees Luminous dashboard
- Key metrics visible: API latency, error rate, queue depth
- Alerts fire when thresholds breached
- Can drill down to identify root cause

#### Context
Infrastructure exists (OpenTelemetry, Prometheus, Loki, Grafana). This feature adds Luminous-specific dashboards.

#### Scope: Owned Files
- `square_head/observability/dashboards/luminous.json`

#### Requirements
- Grafana dashboard displays Luminous-specific metrics in one view
- API response times are monitored with visible latency graphs
- Error rate alerts fire when thresholds are breached
- Database query performance is tracked and visible
- Celery queue depth is monitored with alerts for backlogs

---

### Feature 6.2: Luminous AI Usage Patterns
**Linear:** [SQU-34](https://linear.app/squarehead/issue/SQU-34)
**Status:** 🔴 Not Started
**Priority:** Medium
**Dependencies:** SQH-EPIC-06 Feature 6.1 (core AI docs)

#### Outcome
A Luminous developer knows how to use AI services for Luminous-specific tasks.

#### What Success Looks Like
- Developer finds Luminous-specific prompt templates
- Knows which model to use for biosensor analysis tasks
- Can configure Luminous agent workflows

#### Context
Core AI Services documentation is owned by SQH-EPIC-06. This feature documents Luminous-specific usage patterns only.

#### Scope: Owned Files
- `apps/platform_groups/luminous/docs/ai-usage.md`

#### Requirements
- Luminous-specific prompt templates are documented with examples
- Agent configuration for biosensor workflows is explained
- Model selection guidance helps developers choose the right model for Luminous tasks

---

### Feature 6.3: Developer Onboarding Guide
**Linear:** [SQU-35](https://linear.app/squarehead/issue/SQU-35)
**Status:** 🟡 Partial
**Priority:** Medium
**Dependencies:** None (can start now, update as architecture evolves)

#### Outcome
A new developer can set up their environment and make their first contribution within one day.

#### What Success Looks Like
- New dev follows setup guide, gets local env running
- Reads architecture overview, understands system structure
- Finds cookbook for common tasks
- Knows where to look when stuck

#### Scope: Owned Files
- `square_head/docs/` (MkDocs documentation)
- `square_head/CONTRIBUTING.md`

#### Requirements
- Local development setup guide gets new devs running in under an hour
- Architecture overview document explains system structure and data flow
- Key design decisions log captures the "why" behind major choices
- Common tasks cookbook provides copy-paste solutions for frequent operations
- Troubleshooting guide addresses common environment and runtime issues

---

### Feature 6.4: Flutter Client Documentation
**Linear:** [SQU-36](https://linear.app/squarehead/issue/SQU-36)
**Status:** 🟡 Partial
**Priority:** Medium
**Dependencies:** None

#### Outcome
A Flutter developer can understand the client architecture and contribute to any of the apps.

#### What Success Looks Like
- Developer reads docs, understands monorepo structure
- Knows how packages relate to each other
- Can build and run any app locally
- Understands release process

#### Scope: Owned Files
- `square_head/frontend/flutter/README.md`
- `square_head/frontend/flutter/docs/`

#### Requirements
- Desktop app architecture is documented with component diagrams
- Mobile app architecture is documented with platform-specific details
- Shared packages documentation explains dependencies and usage patterns
- Build and release process is documented end-to-end

**Reference:** `square_head/frontend/flutter/`

---

### Feature 6.5: Runbook for Operations
**Linear:** [SQU-37](https://linear.app/squarehead/issue/SQU-37)
**Status:** 🔴 Not Started
**Priority:** Low
**Dependencies:** Features 6.1 (monitoring must exist to write runbooks about)

#### Outcome
An on-call engineer can resolve common issues quickly using documented playbooks.

#### What Success Looks Like
- Alert fires, on-call looks up runbook
- Runbook has step-by-step resolution
- Escalation path is clear if runbook doesn't help
- Recovery procedures prevent data loss

#### Scope: Owned Files
- `docs/operations/runbooks/`

#### Requirements
- Incident response process is documented with roles and responsibilities
- Common issue playbooks provide step-by-step resolution for known problems
- Escalation procedures clearly define when and how to escalate
- Backup and recovery procedures document data protection and restoration

---

## References

- Existing docs: `square_head/docs/`
- Modal apps: `square_head/modal_apps/`
- Flutter apps: `square_head/frontend/flutter/`
- Observability: OpenTelemetry, Prometheus, Loki, Grafana stack
