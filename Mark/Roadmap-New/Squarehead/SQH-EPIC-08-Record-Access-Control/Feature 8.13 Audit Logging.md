---
status: "Not Started"
priority: "Medium"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 8.13: Audit Logging

## Outcome

Security-relevant actions are logged for compliance and debugging.

## What Success Looks Like

- Security events are captured and stored
- Logs are queryable by actor, target, and date
- Retention policy is configurable
- CSV export available for compliance reports

## Scope: Owned Files

- `apps/audit/models.py`
- `apps/audit/middleware.py`

## Requirements

**Audit Log Model:**

- `AuditLog` model stores action, actor, target, timestamp, and metadata
- Logs are indexed for efficient querying by actor, target, and date range
- Retention policy is configurable

**Event Capture:**

- Record access logging is available (configurable, off by default)
- Record modifications are logged
- Permission changes are logged
- Failed access attempts are logged
- Agent data access is logged

**Query Interface:**

- API endpoint provides audit log retrieval (admin only)
- Logs are filterable by actor, action type, and date range
- CSV export is available for compliance reports
