---
status: "Not Started"
priority: "High"
epic_id: "SQH-EPIC-01"
linear_id: "TBD"
linear_url: "TBD"
---

# EPIC-01: MCP Server (Model Context Protocol)

## Vision

External AI applications (Claude Code, Claude Desktop, third-party agents) can securely access Square Head's document search, RAG chat, and knowledge graph through the Model Context Protocol, enabling AI-powered workflows over enterprise data.

## User Stories

- As a **developer using Claude Code**, I can search my team's documents semantically without leaving my IDE
- As a **Claude Cowork user**, I can ask questions about my company documents and get cited answers
- As an **AI agent builder**, I can integrate Square Head's search and RAG capabilities into custom workflows
- As an **admin**, I can control which users and applications have access to MCP tools via OAuth scopes
- As a **security officer**, I can audit all AI tool invocations through existing observability infrastructure

## Context

### What is MCP?

The [Model Context Protocol](https://modelcontextprotocol.io/) is an open standard that enables AI applications to connect to external data sources and tools. MCP provides:

- **Tools**: Functions the AI can call (search, query, create)
- **Resources**: Data the AI can read (documents, configs)
- **Prompts**: Pre-built prompt templates

### Why MCP for Square Head?

Square Head already has powerful capabilities that are valuable to AI agents:
- **Hybrid Search**: Semantic + keyword search across documents
- **RAG Chat**: Question-answering with source citations
- **Knowledge Graph**: Entity relationships in TerminusDB
- **Platform Groups**: Structured business data defined by the tenant (contacts, companies, deals, or any custom groups)

MCP exposes these capabilities to any MCP-compatible client without building custom integrations for each. Platform Group tools are generic and work with any group type—the specific groups available depend on the tenant's configuration.

## Key Decisions

### Server Architecture

**Options:**
1. **Standalone process** (Recommended) - Separate MCP server that imports Django services directly. Native MCP protocol handling, clean separation, but requires separate deployment.
2. **Embedded in Django** - MCP endpoints within Django. Single deployment, but requires implementing MCP protocol manually with DRF overhead.

### OAuth Provider

**Options:**
1. **django-oauth-toolkit** (Recommended) - Mature, well-documented Django integration
2. **Authlib** - More flexible but more setup required
3. **External provider** (Auth0, Keycloak) - If already in use elsewhere

## Features

- [[Feature 1.1 MCP Server Foundation]]
- [[Feature 1.2 Search Tools]]
- [[Feature 1.3 RAG Chat Tools]]
- [[Feature 1.4 Document Tools]]
- [[Feature 1.5 Document Resources]]
- [[Feature 1.6 Knowledge Graph Tools]]
- [[Feature 1.7 Platform Group Tools]]
- [[Feature 1.8 OAuth 2.1 Authorization]]
- [[Feature 1.9 Prompt Templates]]
- [[Feature 1.10 Observability Integration]]
- [[Feature 1.11 Deployment Configuration]]

## Implementation Order

| Phase | Features | Rationale |
|-------|----------|-----------|
| **Phase 1** | 1.1, 1.2 | Foundation + Search (core value, can test locally without OAuth) |
| **Phase 2** | 1.3 | RAG Chat (high value for AI workflows) |
| **Phase 3** | 1.8, 1.11 | OAuth + Deployment (production readiness) |
| **Phase 4** | 1.4, 1.5 | Document tools + resources |
| **Phase 5** | 1.7 | Platform Group tools (requires SQH-02 complete) |
| **Phase 6** | 1.10 | Observability |
| **Phase 7** | 1.6, 1.9 | Graph tools + prompts |

> **Note:** Phases 1-4 can proceed independently of SQH-02 (Unified Data Access Layer). Phase 5 requires SQH-02 to query PostgreSQL-backed Platform Groups like Luminous biosensor data.

## Security Considerations

- OAuth 2.1 with PKCE required for all public clients
- Scope-based tool access control enforced at the MCP server layer
- All queries scoped to authenticated user's tenant (team_slug from token)
- Rate limiting at nginx layer (requests per minute per client)
- Audit logging of all tool invocations with user context
- Access tokens expire after 1 hour
- Refresh tokens expire after 30 days
- No tool accepts raw SQL or arbitrary code execution

## Dependencies

**Depends On:**
- [[../SQH-EPIC-12-Document-Management/00-Document-Management|SQH-EPIC-12]] - Document search/processing (complete)
- [[../SQH-EPIC-06-AI-Services/00-AI-Services|SQH-EPIC-06]] - RAG chat service (complete)
- [[../SQH-EPIC-02-Unified-Data-Access-Layer/00-Unified-Data-Access-Layer|SQH-EPIC-02]] - Unified Data Access Layer (for Feature 1.7 Platform Group Tools)

**Related To:**
- [[../SQH-EPIC-08-Record-Access-Control/00-Record-Access-Control|SQH-EPIC-08]] - Access control patterns

## References

- [MCP Specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [FastMCP](https://github.com/jlowin/fastmcp) - Higher-level Python framework for building MCP servers (recommended for rapid development)
- [RFC 9728 - OAuth Protected Resource Metadata](https://datatracker.ietf.org/doc/html/rfc9728)
