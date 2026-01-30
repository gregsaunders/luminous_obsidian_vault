---
status: "Not Started"
priority: "High"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 8.7: Qdrant Team + Attribute Filtering

## Outcome

Qdrant payloads include team_id and configurable fields for filtering.

## What Success Looks Like

- All Qdrant payloads include `team_id`
- Ownership fields are included in payloads
- CDC access control fields are included
- Search filtering by team and attributes works correctly
- Migration completes without data loss

## Scope: Owned Files

- `apps/documents/graph/consistency.py` - Payload creation
- `apps/documents/vector_store/qdrant_store.py` - Search filtering

## Requirements

**Payload Extension:**

- All Qdrant payloads include `team_id`
- Ownership fields (`owned_by`, `created_by`) are added to payloads
- CDC access control fields from `field_mapping` are included
- Filterable fields are configured in index settings

**Search Filtering:**

- `team_id` filter is required on all searches
- Attribute filters from user permissions are optionally applied
- Filters are combined efficiently

**Migration (Required):**

Qdrant does not support updating payloads in place. New fields require re-ingesting all vectors.

- Migration script re-indexes all existing documents with new payload fields
- Migration runs BEFORE enabling team_id filtering (otherwise old records disappear from search)
- Impact is full re-index of all vectors (pre-production, acceptable)
- `team_id` backfill logic looks up team from document's bucket or TerminusDB record
