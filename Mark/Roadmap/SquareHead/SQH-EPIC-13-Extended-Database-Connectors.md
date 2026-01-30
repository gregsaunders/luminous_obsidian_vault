---
linear_id: SQU-49
linear_url: https://linear.app/squarehead/issue/SQU-49
---

# EPIC-13: Extended Database Support

**Linear:** [SQU-49](https://linear.app/squarehead/issue/SQU-49)
**Status:** Not Started
**Priority:** Low
**Owner:** TBD

---

## Vision

The CDC pipeline configuration layer supports additional Debezium-compatible databases, enabling data mirroring from diverse enterprise systems with minimal code changes.

---

## User Stories

- As a **data engineer**, I can configure CDC connectors for Oracle databases by selecting the Oracle engine
- As a **data engineer**, I can configure CDC connectors for MongoDB to capture document changes
- As a **data engineer**, I can use the existing SQL Server support that's already implemented

---

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

---

## Features

### Feature 13.1: SQL Server Documentation
**Status:** Partial (code exists, docs missing)
**Priority:** Low

#### Outcome
SQL Server CDC support is documented and tested.

#### Context
`SQLServerConfigBuilder` already exists in the codebase. This feature adds documentation and validation.

#### Scope: Owned Files
- `docs/cdc/sqlserver.md`
- `apps/cdc/tests/test_sqlserver_config.py`

#### Tasks
- [ ] Document SQL Server CDC setup requirements
- [ ] Add integration test with SQL Server container
- [ ] Update EPIC-07 documentation to reflect SQL Server support

---

### Feature 13.2: Oracle ConfigBuilder
**Status:** Not Started
**Priority:** Low

#### Outcome
Data engineers can configure CDC connectors for Oracle databases.

#### Context
Debezium supports Oracle via LogMiner or XStream. We need to add:
- `OracleConfigBuilder` class with Oracle-specific Debezium parameters
- SQLAlchemy Oracle URL creation (`oracle+oracledb://`)
- Oracle read-only enforcement SQL

#### Scope: Owned Files
- `apps/cdc/services/connector_config_builders.py` - Add `OracleConfigBuilder`
- `apps/cdc/discovery/runner.py` - Add Oracle URL + read-only SQL
- `apps/cdc/tests/test_oracle_config.py`

#### Tasks
- [ ] Create `OracleConfigBuilder` extending `DebeziumConfigBuilder`
- [ ] Add Oracle-specific config fields (LogMiner vs XStream, mining strategy)
- [ ] Add SQLAlchemy Oracle URL creation in discovery runner
- [ ] Add Oracle read-only enforcement SQL
- [ ] Register in `CONFIG_BUILDERS` dict
- [ ] Add unit tests

#### References
- [Debezium Oracle Connector](https://debezium.io/documentation/reference/stable/connectors/oracle.html)

---

### Feature 13.3: MongoDB Support Evaluation
**Status:** Not Started
**Priority:** Low

#### Outcome
Decision documented on whether MongoDB CDC makes sense for our architecture.

#### Context
MongoDB is fundamentally different from relational databases:
- No schema/tables/columns - uses collections and documents
- Debezium MongoDB connector has different configuration model
- Our discovery logic is table-based (SQLAlchemy)
- May need separate code paths rather than plugin pattern

#### Scope: Owned Files
- `docs/cdc/mongodb-evaluation.md`

#### Tasks
- [ ] Evaluate if MongoDB CDC fits our use cases
- [ ] Document architectural differences
- [ ] Recommend: implement, defer, or out-of-scope
- [ ] If implementing: design document-to-table mapping strategy

---

## Key Files

- `apps/cdc/services/connector_config_builders.py` - ConfigBuilder classes + registry
- `apps/cdc/discovery/runner.py` - Schema discovery with SQLAlchemy
- `apps/cdc/models.py` - `DatabaseEngine` and `DebeziumPlugin` enums (Oracle/MongoDB already defined)

---

## References

- [SQH-EPIC-07: CDC Pipeline](SQH-EPIC-07-CDC-Pipeline.md) - Core CDC infrastructure
- [Debezium Source Connectors](https://debezium.io/documentation/reference/stable/connectors/index.html)
- [Debezium Oracle Connector](https://debezium.io/documentation/reference/stable/connectors/oracle.html)
- [Debezium MongoDB Connector](https://debezium.io/documentation/reference/stable/connectors/mongodb.html)
