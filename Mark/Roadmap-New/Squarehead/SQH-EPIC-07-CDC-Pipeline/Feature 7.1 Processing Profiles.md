---
status: "Not Started"
priority: "High"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 7.1: Processing Profiles

## Outcome

An operator can configure how different document types are processed through the pipeline.

## What Success Looks Like

- Operator configures `processing_profile` per `ConnectorTableConfig`
- Transactional tables skip chunking/embedding, go straight to search index
- Knowledge tables get full processing (chunk + embed + index)
- Archive tables are stored only, no processing
- Cost savings from skipping unnecessary embedding API calls

## Context

Not all CDC-sourced documents benefit from the same processing. Transactional records (orders, invoices) are structured data best indexed for lookup. Knowledge documents (articles, manuals) benefit from chunking and semantic embeddings.

## Processing Profile Options

| Profile | Chunk | Embed | Index | Use Case |
|---------|-------|-------|-------|----------|
| `full` | Yes | Yes | Yes | Knowledge docs, manuals, articles |
| `index_only` | No | No | Yes | Transactional records, structured data |
| `archive` | No | No | No | Audit logs, historical snapshots |

## Scope: Owned Files

- `apps/cdc/models.py` - Add `processing_profile` field to `ConnectorTableConfig`
- `apps/documents/tasks.py` - Route based on profile in `process_object_created_graph`
- `apps/documents/models.py` - Add profile to `StorageBucket` or metadata

## Requirements

- Add `ProcessingProfile` enum (full, index_only, archive)
- Add `processing_profile` field to `ConnectorTableConfig`
- Modify pipeline routing in `process_object_created_graph` to check profile
- Skip chunking/embedding for `index_only` profile
- Skip all processing for `archive` profile
- API endpoint to configure profile per table
- Documentation for profile selection guidelines
