---
status: "Not Started"
priority: "High"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 7.2: Secret Resolution

## Outcome

Database credentials are securely managed through Vault, not stored in connector configs.

## What Success Looks Like

- Credentials are stored in Vault, not in database
- Connector configs reference Vault paths
- Credentials are injected at runtime
- Rotation is possible without config changes

## Scope: Owned Files

- `apps/cdc/services/connector_config_builders.py`
- `apps/cdc/services/vault.py`

## Requirements

- Vault integration for database credentials
- Secure credential injection
