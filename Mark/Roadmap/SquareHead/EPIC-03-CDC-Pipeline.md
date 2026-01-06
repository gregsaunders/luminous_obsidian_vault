# EPIC-03: CDC Pipeline

**Status:** 🟢 Complete
**Priority:** Medium
**Owner:** TBD

---

## Vision

External database changes are captured in real-time and mirrored into the platform for unified data access.

---

## User Stories

- As a **data engineer**, I can configure CDC connectors to mirror external databases
- As an **analyst**, I can query mirrored data without accessing source systems
- As an **ops engineer**, I can securely manage database credentials through Vault

---

## Context

Debezium-based Change Data Capture pipeline for database mirroring. Production-ready with 15+ models.

**What exists:** Full connector lifecycle, Kafka integration, snapshot assembly, PostgreSQL/MySQL support

**What's needed:** Secret resolution (Vault), Oracle/MongoDB support, documentation

---

## Features

### Feature 3.1: Secret Resolution

#### Outcome
Database credentials are securely managed through Vault, not stored in connector configs.

#### Scope: Owned Files
- `apps/cdc/services/connector_config_builders.py`
- `apps/cdc/services/vault.py`

#### Tasks
- [ ] Vault integration for database credentials
- [ ] Secure credential injection

---

### Feature 3.2: Oracle/MongoDB Support

#### Outcome
CDC connectors support Oracle and MongoDB databases.

#### Scope: Owned Files
- `apps/cdc/connectors/oracle.py`
- `apps/cdc/connectors/mongodb.py`

#### Tasks
- [ ] Oracle connector implementation
- [ ] MongoDB connector implementation

**Note:** Not critical for Luminous pilot

---

### Feature 3.3: CDC Documentation

#### Outcome
An operator can configure and troubleshoot CDC connectors following documentation.

#### Scope: Owned Files
- `docs/cdc/`

#### Tasks
- [ ] Architecture overview
- [ ] Connector configuration guide
- [ ] Troubleshooting runbook

---

## Key Files

- `apps/cdc/models.py` - CDCConnector, DatabaseConnection, etc.
- `apps/cdc/services/` - Connector configuration
- `apps/cdc/assembly/snapshot.py` - Snapshot assembly
- `apps/cdc/tasks.py` - Celery tasks
