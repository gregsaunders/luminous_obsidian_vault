---
status: "Not Started"
priority: "High"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 8.8: Meilisearch Team Filtering

## Outcome

Meilisearch documents include team_id and filterable attributes.

## What Success Looks Like

- All indexed documents include `team_id`
- Ownership fields are added to documents
- CDC access control fields are included
- Team filter is required on all searches

## Scope: Owned Files

- `apps/documents/indexing/` - Document creation
- Search service Meilisearch integration

## Requirements

- All indexed documents include `team_id`
- Ownership fields are added to documents
- CDC access control fields are included
- Filterable attributes are configured in index settings
- Team filter is required on all searches
