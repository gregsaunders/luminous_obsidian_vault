# EPIC-05: Observability & Documentation

**Status:** 🟡 Partial
**Priority:** Medium
**Owner:** Greg
**Target:** Ongoing / During Pilot

**Dependencies:**
- 🟢 **Independent:** Can progress in parallel with other EPICs
- 🔗 **Related:** All EPICs (documentation covers entire platform)

---

## Business Value

Platform observability ensures reliability during pilot operations. Documentation enables team scaling and knowledge transfer. These are not blockers for pilot launch but significantly improve operational readiness.

**Key Outcome:** Team can monitor platform health and onboard new contributors.

---

## Features

### Feature 5.1: Platform Monitoring Dashboard
**Status:** 🟡 Partial (infrastructure exists)
**Priority:** Medium
**Dependencies:** None (infrastructure exists, just needs Luminous-specific dashboards)

Operational dashboard for platform health.

**Tasks:**
- [ ] Grafana dashboard for Luminous-specific metrics
- [ ] API response time monitoring
- [ ] Error rate alerting
- [ ] Database query performance
- [ ] Celery queue depth monitoring

**Existing Infrastructure:**
- OpenTelemetry instrumentation
- Prometheus metrics
- Loki logs
- Grafana dashboards

---

### Feature 5.2: AI Services Documentation
**Status:** 🔴 Not Started
**Priority:** Medium
**Dependencies:** None (can document existing services anytime)

Document the self-hosted AI services for the team.

**Tasks:**
- [ ] Modal services architecture overview
- [ ] Service catalog (Granite, Qwen models)
- [ ] Deployment and scaling procedures
- [ ] Cost monitoring
- [ ] Usage guidelines

**Reference:** `square_head/modal_apps/`

---

### Feature 5.3: Developer Onboarding Guide
**Status:** 🟡 Partial
**Priority:** Medium
**Dependencies:** None (can start now, update as architecture evolves)

Enable new developers to contribute quickly.

**Tasks:**
- [ ] Local development setup guide
- [ ] Architecture overview document
- [ ] Key design decisions log
- [ ] Common tasks cookbook
- [ ] Troubleshooting guide

**Existing:** `square_head/docs/` has MkDocs documentation

---

### Feature 5.4: Flutter Client Documentation
**Status:** 🟡 Partial
**Priority:** Medium
**Dependencies:** EPIC-01 Technology Decision (if custom Flutter dashboard chosen)

Document the Flutter client apps.

**Tasks:**
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

Operational procedures for production issues.

**Tasks:**
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
