---
status: "Not Started"
priority: "High"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 1.1: MCP Server Foundation

## Outcome

A running MCP server that exposes Square Head tools to MCP clients over the streamable-http transport.

## What Success Looks Like

- MCP server process starts and responds to health checks
- Server can bootstrap Django ORM and access Square Head services
- MCP protocol endpoints are functional
- Local development workflow is documented and works

## Scope: Owned Files

- `mcp_server/` - New MCP server package
- `Makefile` - New target for local development

## Requirements

- Server can bootstrap Django ORM and settings
- Server can import and call SearchService, RAGService, and DocumentGraphAPI
- Server exposes MCP protocol endpoints
- Server runs as a containerized service alongside Django
- Health check endpoint for orchestration
- Local development command (Makefile target)
