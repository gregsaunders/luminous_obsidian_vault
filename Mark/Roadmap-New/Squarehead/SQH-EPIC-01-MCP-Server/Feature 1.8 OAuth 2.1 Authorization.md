---
status: "Not Started"
priority: "High"
assigned: ""
dependencies:
  - "[[Feature 1.1 MCP Server Foundation]]"
linear_id: ""
---

# Feature 1.8: OAuth 2.1 Authorization

## Outcome

MCP clients authenticate via OAuth 2.1 with scoped access tokens.

## What Success Looks Like

- Claude Desktop can authenticate via OAuth flow
- Access tokens properly scope tool access
- Token introspection validates requests
- Application registration UI exists for clients

## Scope: Owned Files

- `apps/oauth/` - OAuth provider implementation
- `mcp_server/auth.py` - Token validation

## Requirements

- OAuth 2.1 authorization server endpoints:
  - `/oauth/authorize/` - Authorization endpoint
  - `/oauth/token/` - Token endpoint
  - `/oauth/introspect/` - Token introspection endpoint
- PKCE required for public clients (Claude Desktop, Claude Code)
- Supported scopes:
  - `mcp:read` - Grants access to: search_documents, list_documents, get_document, get_document_content, get_document_chunks, all document resources
  - `mcp:chat` - Grants access to: ask_documents
  - `mcp:graph` - Grants access to: get_entity, get_relationships, traverse_graph
  - `mcp:groups` - Grants access to: list_platform_groups, search_platform_group, get_platform_group_record, list_platform_group_records, aggregate_platform_group
  - `mcp:write` - Reserved for future document and record creation/update tools
  - `mcp:admin` - Grants access to all tools plus configuration endpoints
- Access tokens include user_id and team_slug for tenant routing
- Access token expiration: 1 hour
- Refresh token expiration: 30 days
- RFC 9728 Protected Resource Metadata at `/.well-known/oauth-protected-resource`
- Application registration UI for creating MCP client credentials
