---
status: "Not Started"
priority: "Medium"
assigned: ""
dependencies:
  - "[[Feature 1.1 MCP Server Foundation]]"
linear_id: ""
---

# Feature 1.4: Document Tools

## Outcome

AI clients can list, read, and get details about documents.

## What Success Looks Like

- AI can enumerate available documents
- AI can retrieve document content and metadata
- AI can access document chunks for detailed analysis
- Operations are properly scoped to tenant

## Scope: Owned Files

- `mcp_server/tools/documents.py`

## Requirements

- `list_documents` tool with parameters:
  - `limit`: Maximum results, 1-100 (default 20)
  - `offset`: Pagination offset (default 0)
  - `sort_by`: One of "created_at", "updated_at", "title" (default "updated_at")
  - `sort_order`: One of "asc", "desc" (default "desc")
- `get_document` tool with parameters:
  - `document_id`: Document ID (required)
- `get_document_content` tool with parameters:
  - `document_id`: Document ID (required)
  - Returns full document text
- `get_document_chunks` tool with parameters:
  - `document_id`: Document ID (required)
  - Returns list of chunks with chunk ID, text, and position
- All operations scoped to authenticated user's tenant
