---
status: "Not Started"
priority: "Medium"
assigned: ""
dependencies:
  - "[[Feature 1.1 MCP Server Foundation]]"
linear_id: ""
---

# Feature 1.5: Document Resources

## Outcome

Documents exposed as MCP resources that clients can read directly.

## What Success Looks Like

- AI can access documents via URI scheme
- Metadata and chunks available as separate resources
- Resource templates enable dynamic URI resolution

## Scope: Owned Files

- `mcp_server/resources/documents.py`

## Requirements

- `document://{document_id}` resource returns document content as text
- `document://{document_id}/metadata` resource returns JSON with title, created_at, updated_at, size, chunk_count
- `document://{document_id}/chunks` resource returns JSON array of chunks
- Resource templates registered for dynamic URI resolution
- All resources scoped to authenticated user's tenant
