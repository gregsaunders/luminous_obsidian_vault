---
status: "Not Started"
priority: "Low"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 13.2: Oracle ConfigBuilder

## Outcome

Data engineers can configure CDC connectors for Oracle databases.

## What Success Looks Like

- Oracle CDC connectors can be configured via the UI
- LogMiner and XStream modes are supported
- Schema discovery works with Oracle databases
- Read-only enforcement prevents data modifications

## Context

Debezium supports Oracle via LogMiner or XStream. We need to add:
- `OracleConfigBuilder` class with Oracle-specific Debezium parameters
- SQLAlchemy Oracle URL creation (`oracle+oracledb://`)
- Oracle read-only enforcement SQL

## Scope: Owned Files

- `apps/cdc/services/connector_config_builders.py` - Add `OracleConfigBuilder`
- `apps/cdc/discovery/runner.py` - Add Oracle URL + read-only SQL
- `apps/cdc/tests/test_oracle_config.py`

## Requirements

- Create `OracleConfigBuilder` extending `DebeziumConfigBuilder`
- Add Oracle-specific config fields (LogMiner vs XStream, mining strategy)
- Add SQLAlchemy Oracle URL creation in discovery runner
- Add Oracle read-only enforcement SQL
- Register in `CONFIG_BUILDERS` dict
- Add unit tests

## References

- [Debezium Oracle Connector](https://debezium.io/documentation/reference/stable/connectors/oracle.html)
