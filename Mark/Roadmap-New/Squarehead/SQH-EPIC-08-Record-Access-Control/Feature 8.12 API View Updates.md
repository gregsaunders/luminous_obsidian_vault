---
status: "Not Started"
priority: "Medium"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 8.12: API View Updates

## Outcome

All API views pass user and team context through to services.

## What Success Looks Like

- Search views pass user and team context
- REST views use DocumentAccessControl for filtering
- Graph views include team filters in queries
- Bulk views validate per-record access
- 404 vs 403 handling prevents information leakage

## Scope: Owned Files

- `apps/documents/api/search_views.py`
- `apps/documents/api/rest_views.py`
- `apps/documents/api/graph_views.py`
- `apps/documents/api/bulk_views.py`

## Requirements

- Search views pass `request.user` and `request.team` to SearchService
- REST views use DocumentAccessControl for filtering
- Graph views include team filters in WOQL queries
- Bulk views validate per-record access
- 404 vs 403 response handling prevents info leakage
