---
status: "In Progress"
priority: "Medium"
epic_id: "SQH-EPIC-07"
linear_id: "SQU-44"
linear_url: "https://linear.app/squarehead/issue/SQU-44"
---

# EPIC-07: CDC Pipeline

## Vision

External database changes are captured in real-time and mirrored into the platform for unified data access.

## User Stories

- As a **data engineer**, I can configure CDC connectors to mirror external databases
- As an **analyst**, I can query mirrored data without accessing source systems
- As an **ops engineer**, I can securely manage database credentials through Vault

## Context

Debezium-based Change Data Capture pipeline for database mirroring. Production-ready with 15+ models.

**What exists:** Full connector lifecycle, Kafka integration, snapshot assembly, PostgreSQL/MySQL/SQL Server support

**What's needed:** Processing profiles, secret resolution (Vault), documentation

## Features

- [[Feature 7.1 Processing Profiles]]
- [[Feature 7.2 Secret Resolution]]
- [[Feature 7.3 CDC Documentation]]

## Key Files

- `apps/cdc/models.py` - CDCConnector, DatabaseConnection, etc.
- `apps/cdc/services/` - Connector configuration
- `apps/cdc/assembly/snapshot.py` - Snapshot assembly
- `apps/cdc/tasks.py` - Celery tasks

## Dependencies

**Depends On:** None (core platform capability)

**Related To:**
- [[SQH-EPIC-13-Extended-Database-Connectors]] - Oracle, MongoDB, SQL Server support
