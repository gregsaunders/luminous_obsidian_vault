---
status: "Not Started"
priority: "High"
assigned: ""
dependencies:
  - "[[Feature 1.1 MCP Server Foundation]]"
linear_id: ""
---

# Feature 1.3: RAG Chat Tools

## Outcome

AI clients can ask questions and get answers grounded in documents with citations.

## What Success Looks Like

- Claude Code can invoke `ask_documents` tool
- Answers are accurate and cite relevant sources
- Multi-turn conversations maintain context
- Confidence indicators help users assess answer quality

## Scope: Owned Files

- `mcp_server/tools/rag.py`

## Requirements

- `ask_documents` tool with parameters:
  - `question`: The question to answer (required)
  - `conversation_id`: Optional ID to continue a multi-turn conversation
  - `max_sources`: Maximum source documents to cite, 1-10 (default 5)
- Response includes:
  - Answer text
  - List of source citations with document ID, title, and relevant excerpt
  - Confidence indicator (high, medium, low)
- Conversation context preserved when conversation_id provided
- All queries scoped to authenticated user's tenant
