---
status: "Not Started"
priority: "High"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 8.5: CDC Field Indexing

## Outcome

CDC-mirrored records include designated fields in search indexes for filtering.

## What Success Looks Like

- Configured fields are extracted during CDC assembly
- Fields appear in Qdrant payloads for filtering
- Fields appear in Meilisearch documents for filtering
- Field names are validated against source schema

## Scope: Owned Files

- `apps/cdc/models.py` - ConnectorTableConfig.field_mapping usage
- `apps/documents/graph/consistency.py` - Qdrant payload creation
- `apps/cdc/assembly/` - Field extraction during assembly

## Requirements

**Connector Configuration:**

- `field_mapping` schema defines access control fields:
  ```json
  {
    "access_control_fields": ["invoice_type", "department"],
    "index_for_search": ["invoice_type", "status"]
  }
  ```
- Field names are validated against source schema

**Indexing Pipeline:**

- Access control fields are extracted during CDC assembly
- Fields are included in Qdrant payloads during chunk indexing
- Fields are included in Meilisearch documents
