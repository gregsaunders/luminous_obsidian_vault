---
linear_id: SQU-44
linear_url: https://linear.app/squarehead/issue/SQU-44
---

# EPIC-07: CDC Pipeline

**Linear:** [SQU-44](https://linear.app/squarehead/issue/SQU-44)
**Status:** 🟡 Partial
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

**What exists:** Full connector lifecycle, Kafka integration, snapshot assembly, PostgreSQL/MySQL/SQL Server support

**What's needed:** Processing profiles, secret resolution (Vault), documentation

---

## Features

### Feature 7.1: Processing Profiles
**Status:** 🔴 Not Started
**Priority:** High

#### Outcome
An operator can configure how different document types are processed through the pipeline.

#### Context
Not all CDC-sourced documents benefit from the same processing. Transactional records (orders, invoices) are structured data best indexed for lookup. Knowledge documents (articles, manuals) benefit from chunking and semantic embeddings.

#### What Success Looks Like
- Operator configures `processing_profile` per `ConnectorTableConfig`
- Transactional tables skip chunking/embedding, go straight to search index
- Knowledge tables get full processing (chunk + embed + index)
- Archive tables are stored only, no processing
- Cost savings from skipping unnecessary embedding API calls

#### Processing Profile Options

| Profile | Chunk | Embed | Index | Use Case |
|---------|-------|-------|-------|----------|
| `full` | ✅ | ✅ | ✅ | Knowledge docs, manuals, articles |
| `index_only` | ❌ | ❌ | ✅ | Transactional records, structured data |
| `archive` | ❌ | ❌ | ❌ | Audit logs, historical snapshots |

#### Scope: Owned Files
- `apps/cdc/models.py` - Add `processing_profile` field to `ConnectorTableConfig`
- `apps/documents/tasks.py` - Route based on profile in `process_object_created_graph`
- `apps/documents/models.py` - Add profile to `StorageBucket` or metadata

#### Tasks
- [ ] Add `ProcessingProfile` enum (full, index_only, archive)
- [ ] Add `processing_profile` field to `ConnectorTableConfig`
- [ ] Modify pipeline routing in `process_object_created_graph` to check profile
- [ ] Skip chunking/embedding for `index_only` profile
- [ ] Skip all processing for `archive` profile
- [ ] API endpoint to configure profile per table
- [ ] Documentation for profile selection guidelines

---

### Feature 7.2: Secret Resolution

#### Outcome
Database credentials are securely managed through Vault, not stored in connector configs.

#### Scope: Owned Files
- `apps/cdc/services/connector_config_builders.py`
- `apps/cdc/services/vault.py`

#### Tasks
- [ ] Vault integration for database credentials
- [ ] Secure credential injection

---

### Feature 7.3: CDC Documentation

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

---

## References

- [SQH-EPIC-13: Extended Database Support](SQH-EPIC-13-Extended-Database-Connectors.md) - Oracle, MongoDB, SQL Server support
