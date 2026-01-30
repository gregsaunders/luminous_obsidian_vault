---
status: "Not Started"
priority: "Low"
epic_id: "SQH-EPIC-13"
linear_id: "SQU-49"
linear_url: "https://linear.app/squarehead/issue/SQU-49"
---

# EPIC-13: Extended Database Support

## Vision

The CDC pipeline configuration layer supports additional Debezium-compatible databases, enabling data mirroring from diverse enterprise systems with minimal code changes.

## User Stories

- As a **data engineer**, I can configure CDC connectors for Oracle databases by selecting the Oracle engine
- As a **data engineer**, I can configure CDC connectors for MongoDB to capture document changes
- As a **data engineer**, I can use the existing SQL Server support that's already implemented

## Context

**Debezium already supports these databases** - we don't build connectors, we configure them.

Debezium provides production-ready connectors for:
- PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, MongoDB, Db2, Cassandra, Spanner, Vitess, Informix

Our CDC pipeline wraps Debezium with a configuration layer that handles:
1. **ConfigBuilders** - Generate Debezium JSON config with database-specific parameters
2. **Schema Discovery** - SQLAlchemy-based introspection with database-specific URLs
3. **Read-only enforcement** - Database-specific SQL syntax

**Current Implementation Status:**

| Database | ConfigBuilder | Discovery URL | Read-only SQL | Status |
|----------|--------------|---------------|---------------|--------|
| PostgreSQL | Yes | Yes | Yes | Production |
| MySQL | Yes | Yes | Yes | Production |
| SQL Server | Yes | Yes | Yes | **Implemented** (undocumented) |
| Oracle | No | No | No | Needs config layer |
| MongoDB | No | N/A | N/A | Different architecture |

**Key Insight:** SQL Server is already implemented in `connector_config_builders.py` but wasn't documented in EPIC-04.

## Features

- [[Feature 13.1 SQL Server Documentation]]
- [[Feature 13.2 Oracle ConfigBuilder]]
- [[Feature 13.3 MongoDB Support Evaluation]]

## Key Files

- `apps/cdc/services/connector_config_builders.py` - ConfigBuilder classes + registry
- `apps/cdc/discovery/runner.py` - Schema discovery with SQLAlchemy
- `apps/cdc/models.py` - `DatabaseEngine` and `DebeziumPlugin` enums (Oracle/MongoDB already defined)

## References

- [SQH-EPIC-07: CDC Pipeline](SQH-EPIC-07-CDC-Pipeline.md) - Core CDC infrastructure
- [Debezium Source Connectors](https://debezium.io/documentation/reference/stable/connectors/index.html)
- [Debezium Oracle Connector](https://debezium.io/documentation/reference/stable/connectors/oracle.html)
- [Debezium MongoDB Connector](https://debezium.io/documentation/reference/stable/connectors/mongodb.html)
