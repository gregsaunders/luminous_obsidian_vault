---
status: "Not Started"
priority: "Low"
assigned: ""
dependencies:
  - "[[Feature 1.1 MCP Server Foundation]]"
linear_id: ""
---

# Feature 1.6: Knowledge Graph Tools

## Outcome

AI clients can query the knowledge graph for entity relationships.

## What Success Looks Like

- AI can retrieve entity details
- AI can explore entity relationships
- AI can traverse the graph to discover connections
- Graph queries are tenant-scoped

## Scope: Owned Files

- `mcp_server/tools/graph.py`

## Requirements

- `get_entity` tool with parameters:
  - `entity_id`: Entity ID (required)
  - Returns entity properties and type
- `get_relationships` tool with parameters:
  - `entity_id`: Entity ID (required)
  - `relationship_type`: Optional filter by relationship type
  - `direction`: One of "outgoing", "incoming", "both" (default "both")
  - Returns list of related entities with relationship type and direction
- `traverse_graph` tool with parameters:
  - `start_entity_id`: Starting entity ID (required)
  - `max_hops`: Maximum traversal depth, 1-5 (default 2)
  - `relationship_types`: Optional list of relationship types to follow
  - Returns subgraph of entities and relationships
- All operations scoped to authenticated user's tenant
