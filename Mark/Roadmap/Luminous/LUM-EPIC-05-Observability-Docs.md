# EPIC-05: Observability & Documentation

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

### Feature 5.1: Platform Monitoring Dashboard
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

#### Tasks
- [ ] Grafana dashboard for Luminous-specific metrics
- [ ] API response time monitoring
- [ ] Error rate alerting
- [ ] Database query performance
- [ ] Celery queue depth monitoring

---

### Feature 5.2: Luminous AI Usage Patterns
**Status:** 🔴 Not Started
**Priority:** Medium
**Dependencies:** SquareHead EPIC-10 Feature 10.1 (core AI docs)

#### Outcome
A Luminous developer knows how to use AI services for Luminous-specific tasks.

#### What Success Looks Like
- Developer finds Luminous-specific prompt templates
- Knows which model to use for biosensor analysis tasks
- Can configure Luminous agent workflows

#### Context
Core AI Services documentation is owned by SquareHead EPIC-10. This feature documents Luminous-specific usage patterns only.

#### Scope: Owned Files
- `apps/platform_groups/luminous/docs/ai-usage.md`

#### Tasks
- [ ] Luminous-specific prompt templates
- [ ] Agent configuration for biosensor workflows
- [ ] Model selection guidance for Luminous tasks

---

### Feature 5.3: Developer Onboarding Guide
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

#### Tasks
- [ ] Local development setup guide
- [ ] Architecture overview document
- [ ] Key design decisions log
- [ ] Common tasks cookbook
- [ ] Troubleshooting guide

---

### Feature 5.4: Flutter Client Documentation
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

#### Tasks
- [ ] Desktop app architecture
- [ ] Mobile app architecture
- [ ] Shared packages documentation
- [ ] Build and release process

**Reference:** `square_head/frontend/flutter/`

---

### Feature 5.5: Runbook for Operations
**Status:** 🔴 Not Started
**Priority:** Low
**Dependencies:** Features 5.1 (monitoring must exist to write runbooks about)

#### Outcome
An on-call engineer can resolve common issues quickly using documented playbooks.

#### What Success Looks Like
- Alert fires, on-call looks up runbook
- Runbook has step-by-step resolution
- Escalation path is clear if runbook doesn't help
- Recovery procedures prevent data loss

#### Scope: Owned Files
- `docs/operations/runbooks/`

#### Tasks
- [ ] Incident response process
- [ ] Common issue playbooks
- [ ] Escalation procedures
- [ ] Backup and recovery procedures

---

## References

- Existing docs: `square_head/docs/`
- Modal apps: `square_head/modal_apps/`
- Flutter apps: `square_head/frontend/flutter/`
- Observability: OpenTelemetry, Prometheus, Loki, Grafana stack
