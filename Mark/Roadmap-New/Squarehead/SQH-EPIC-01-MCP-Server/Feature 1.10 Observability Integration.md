---
status: "Not Started"
priority: "Medium"
assigned: ""
dependencies:
  - "[[Feature 1.1 MCP Server Foundation]]"
linear_id: ""
---

# Feature 1.10: Observability Integration

## Outcome

MCP tool invocations are traced and logged through existing OpenTelemetry infrastructure.

## What Success Looks Like

- Tool invocations appear in tracing dashboards
- Errors are captured with context
- Metrics enable performance monitoring
- Correlation IDs link logs across services

## Scope: Owned Files

- `mcp_server/telemetry.py`

## Requirements

- OpenTelemetry SDK initialized in MCP server (same configuration as Django and Celery)
- Each tool invocation creates a trace span with:
  - Tool name
  - User ID
  - Team slug
  - Duration
  - Success/failure status
  - Error message (if failed)
- Trace context propagated to SearchService, RAGService, and DocumentGraphAPI calls
- Correlation IDs in logs match trace IDs
- Metrics exported:
  - `mcp.tool.invocations` counter by tool name, status
  - `mcp.tool.duration` histogram by tool name
