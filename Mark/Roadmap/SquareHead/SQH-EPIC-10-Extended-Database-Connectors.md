# EPIC-10: Extended Database Connectors

**Status:** 🔴 Not Started
**Priority:** Low
**Owner:** TBD

---

## Vision

The CDC pipeline supports a wide variety of database sources beyond PostgreSQL and MySQL, enabling data mirroring from diverse enterprise systems.

---

## User Stories

- As a **data engineer**, I can configure CDC connectors for Oracle databases to mirror enterprise data
- As a **data engineer**, I can configure CDC connectors for MongoDB to capture document changes
- As a **data engineer**, I can configure CDC connectors for SQL Server to mirror Windows-ecosystem databases

---

## Context

The core CDC pipeline (EPIC-04) supports PostgreSQL and MySQL. This EPIC extends database support to additional platforms as customer requirements emerge.

**Current Support (EPIC-04):**
- PostgreSQL (production-ready)
- MySQL (production-ready)

**Potential Future Support (this EPIC):**
- Oracle
- MongoDB
- SQL Server
- MariaDB
- Others as needed

---

## Features

### Feature 10.1: Oracle Connector
**Status:** 🔴 Not Started
**Priority:** Low

#### Outcome
CDC pipeline can capture changes from Oracle databases.

#### Scope: Owned Files
- `apps/cdc/connectors/oracle.py`

#### Tasks
- [ ] Debezium Oracle connector configuration
- [ ] Oracle-specific schema mapping
- [ ] LogMiner vs XStream evaluation
- [ ] Testing with Oracle XE

---

### Feature 10.2: MongoDB Connector
**Status:** 🔴 Not Started
**Priority:** Low

#### Outcome
CDC pipeline can capture changes from MongoDB databases.

#### Scope: Owned Files
- `apps/cdc/connectors/mongodb.py`

#### Tasks
- [ ] Debezium MongoDB connector configuration
- [ ] Document-to-relational mapping strategy
- [ ] Change stream handling
- [ ] Testing with MongoDB Community

---

### Feature 10.3: SQL Server Connector
**Status:** 🔴 Not Started
**Priority:** Low

#### Outcome
CDC pipeline can capture changes from Microsoft SQL Server databases.

#### Scope: Owned Files
- `apps/cdc/connectors/sqlserver.py`

#### Tasks
- [ ] Debezium SQL Server connector configuration
- [ ] SQL Server CDC feature enablement docs
- [ ] Testing with SQL Server Express

---

## Key Files

- `apps/cdc/connectors/` - Database-specific connector implementations
- `apps/cdc/services/connector_config_builders.py` - Connector configuration

---

## References

- [SQH-EPIC-04: CDC Pipeline](SQH-EPIC-04-CDC-Pipeline.md) - Core CDC infrastructure
- Debezium Connectors: https://debezium.io/documentation/reference/stable/connectors/
