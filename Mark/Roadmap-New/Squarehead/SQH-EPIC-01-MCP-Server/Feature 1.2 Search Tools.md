---
status: "Not Started"
priority: "High"
assigned: ""
dependencies:
  - "[[Feature 1.1 MCP Server Foundation]]"
linear_id: ""
---

# Feature 1.2: Search Tools

## Outcome

AI clients can search documents using Square Head's hybrid search capabilities.

## What Success Looks Like

- Claude Code can invoke `search_documents` tool
- Search results are relevant and formatted for LLM consumption
- Different search types (hybrid, semantic, keyword) work correctly
- Results are properly scoped to authenticated user's tenant

## Scope: Owned Files

- `mcp_server/tools/search.py`

## Requirements

- `search_documents` tool with parameters:
  - `query`: Natural language search query (required)
  - `limit`: Maximum results, 1-100 (default 10)
  - `search_type`: One of "hybrid", "semantic", or "keyword" (default "hybrid")
  - `expand_chunks`: Boolean to include matching text chunks in results
- Results include: document ID, title, summary, relevance score, and optionally matching chunks with highlights
- All searches scoped to the authenticated user's tenant
- Results formatted for LLM consumption (concise, structured)
