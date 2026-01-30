---
status: "Not Started"
priority: "Low"
assigned: ""
dependencies:
  - "[[Feature 1.2 Search Tools]]"
  - "[[Feature 1.3 RAG Chat Tools]]"
  - "[[Feature 1.4 Document Tools]]"
linear_id: ""
---

# Feature 1.9: Prompt Templates

## Outcome

Pre-built MCP prompts for common workflows.

## What Success Looks Like

- AI clients can use pre-built prompts for common tasks
- Prompts chain multiple tools effectively
- Prompts are documented and discoverable

## Scope: Owned Files

- `mcp_server/prompts/`

## Requirements

- `search_and_summarize` prompt:
  - Input: search query
  - Workflow: search documents, synthesize top results into summary
- `document_qa` prompt:
  - Input: document ID, question
  - Workflow: retrieve document, answer question with citations
- `compare_documents` prompt:
  - Input: list of document IDs
  - Workflow: retrieve documents, compare and contrast key points
- `extract_entities` prompt:
  - Input: document ID
  - Workflow: retrieve document, extract named entities and relationships
