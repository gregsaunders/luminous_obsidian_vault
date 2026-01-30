---
status: "Not Started"
priority: "High"
assigned: ""
dependencies:
  - "[[Feature 1.1 MCP Server Foundation]]"
  - "[[Feature 1.8 OAuth 2.1 Authorization]]"
linear_id: ""
---

# Feature 1.11: Deployment Configuration

## Outcome

MCP server deployable alongside Django in production.

## What Success Looks Like

- MCP server runs as container alongside Django
- Nginx routes requests correctly
- Health checks enable orchestration
- Environment configuration is documented

## Scope: Owned Files

- `docker/mcp/Dockerfile`
- `docker-compose.yml`
- `nginx/mcp.conf`

## Requirements

- Container image definition for MCP server
- Docker Compose service definition with:
  - Dependency on web, redis, and postgres services
  - Environment variables for OAuth client configuration
  - Health check configuration
- Nginx reverse proxy routing:
  - `/api/*` routes to Django
  - `/mcp/*` routes to MCP server
  - `/oauth/*` routes to Django OAuth endpoints
- Environment variables:
  - `MCP_PORT` - Port for MCP server
  - `MCP_OAUTH_CLIENT_ID` - OAuth client ID for token introspection
  - `MCP_OAUTH_CLIENT_SECRET` - OAuth client secret for token introspection
  - `DJANGO_BASE_URL` - URL of Django server for internal calls
