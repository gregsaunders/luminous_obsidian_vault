---
status: "Not Started"
priority: "Medium"
assigned: ""
dependencies:
  - "[[Feature 2.3 TerminusDB Backend]]"
linear_id: ""
---

# Feature 2.7: TerminusDB Query Service

## Outcome

Advanced TerminusDB queries for graph traversals (NOT part of unified CRUD).

## What Success Looks Like

- Developer can traverse relationship paths
- WOQL queries are available for complex graph operations
- Path finding works between entities
- Subgraph extraction is supported

## Scope: Owned Files

- `apps/platform_groups/query_services/terminusdb.py` - **NEW**

## Requirements

- `TerminusDBQueryService` class provides graph query capabilities
- `traverse()` method follows relationship paths between nodes
- `woql_query()` method executes raw WOQL queries
- `path_query()` method finds paths between two nodes
- `subgraph()` method extracts a subgraph from a root node

## Example Usage

```python
terminus_query = TerminusDBQueryService()
related = terminus_query.traverse("tenant-123", "crm", "AppCRMAccount",
    start_id="Account/acme-123",
    path="contacts/opportunities",  # Account -> Contacts -> Opportunities
    max_depth=2
)
```
