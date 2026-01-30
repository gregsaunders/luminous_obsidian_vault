---
status: "Not Started"
priority: "Medium"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 12.1: Per-Model Qdrant Collections

## Outcome

Different document types are stored in separate Qdrant collections for better organization and performance.

## What Success Looks Like

- Each document type has its own Qdrant collection
- Collection management API works correctly
- Search performance improves for type-specific queries

## Scope: Owned Files

- `apps/documents/graph/search_service.py`

## Requirements

- Separate collections for different document types
- Collection management API
