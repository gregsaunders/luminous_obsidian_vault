---
status: "Not Started"
priority: "High"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 8.10: SearchService Integration

## Outcome

SearchService requires team context and applies access control to all searches.

## What Success Looks Like

- All search methods require `team_id` parameter
- Optional user context enables record-level filtering
- ABAC filters are applied to search results
- All callers pass team context

## Scope: Owned Files

- `apps/documents/graph/search_service.py`
- `apps/documents/api/services.py`

## Requirements

- All search methods require `team_id` parameter
- Optional `user_id` is available for record-level filtering
- Optional `access_control: DocumentAccessControl` parameter is supported
- ABAC filters are applied before returning results
- All callers pass team context
