---
linear_id: TBD
linear_url: TBD
---

# EPIC-01: MCP Server (Model Context Protocol)

**Linear:** TBD
**Status:** Not Started
**Priority:** High
**Owner:** TBD

---

## Vision

External AI applications (Claude Code, Claude Desktop, third-party agents) can securely access Square Head's document search, RAG chat, and knowledge graph through the Model Context Protocol, enabling AI-powered workflows over enterprise data.

---

## User Stories

- As a **developer using Claude Code**, I can search my team's documents semantically without leaving my IDE
- As a **Claude Cowork user**, I can ask questions about my company documents and get cited answers
- As an **AI agent builder**, I can integrate Square Head's search and RAG capabilities into custom workflows
- As an **admin**, I can control which users and applications have access to MCP tools via OAuth scopes
- As a **security officer**, I can audit all AI tool invocations through existing observability infrastructure

---

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

---

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

---

## Features

### Feature 1.1: MCP Server Foundation

**Priority:** High

#### Outcome
A running MCP server that exposes Square Head tools to MCP clients over the streamable-http transport.

#### Requirements
- Server can bootstrap Django ORM and settings
- Server can import and call SearchService, RAGService, and DocumentGraphAPI
- Server exposes MCP protocol endpoints
- Server runs as a containerized service alongside Django
- Health check endpoint for orchestration
- Local development command (Makefile target)

---

### Feature 1.2: Search Tools

**Priority:** High

#### Outcome
AI clients can search documents using Square Head's hybrid search capabilities.

#### Requirements
- `search_documents` tool with parameters:
  - `query`: Natural language search query (required)
  - `limit`: Maximum results, 1-100 (default 10)
  - `search_type`: One of "hybrid", "semantic", or "keyword" (default "hybrid")
  - `expand_chunks`: Boolean to include matching text chunks in results
- Results include: document ID, title, summary, relevance score, and optionally matching chunks with highlights
- All searches scoped to the authenticated user's tenant
- Results formatted for LLM consumption (concise, structured)

---

### Feature 1.3: RAG Chat Tools

**Priority:** High

#### Outcome
AI clients can ask questions and get answers grounded in documents with citations.

#### Requirements
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

---

### Feature 1.4: Document Tools

**Priority:** Medium

#### Outcome
AI clients can list, read, and get details about documents.

#### Requirements
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

---

### Feature 1.5: Document Resources

**Priority:** Medium

#### Outcome
Documents exposed as MCP resources that clients can read directly.

#### Requirements
- `document://{document_id}` resource returns document content as text
- `document://{document_id}/metadata` resource returns JSON with title, created_at, updated_at, size, chunk_count
- `document://{document_id}/chunks` resource returns JSON array of chunks
- Resource templates registered for dynamic URI resolution
- All resources scoped to authenticated user's tenant

---

### Feature 1.6: Knowledge Graph Tools

**Priority:** Low

#### Outcome
AI clients can query the knowledge graph for entity relationships.

#### Requirements
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

---

### Feature 1.7: Platform Group Tools

**Priority:** Medium
**Depends On:** [SQH-EPIC-02](SQH-EPIC-02-Unified-Data-Access-Layer.md) - Unified Data Access Layer (for PostgreSQL-backed groups)

#### Outcome
AI clients can query and search records within any Platform Group configured by the tenant, regardless of storage backend (TerminusDB or PostgreSQL).

#### Requirements
- `list_platform_groups` tool with no required parameters:
  - Returns list of available platform groups for the tenant with group name, display name, description, and record count
- `search_platform_group` tool with parameters:
  - `group_name`: Platform group name (required)
  - `query`: Search query string (required)
  - `limit`: Maximum results, 1-100 (default 20)
  - `filters`: Optional key-value filters on record fields
  - Returns list of matching records with ID and field values
- `get_platform_group_record` tool with parameters:
  - `group_name`: Platform group name (required)
  - `record_id`: Record ID (required)
  - Returns full record with all fields
- `list_platform_group_records` tool with parameters:
  - `group_name`: Platform group name (required)
  - `limit`: Maximum results, 1-100 (default 20)
  - `offset`: Pagination offset (default 0)
  - `sort_by`: Field name to sort by (optional)
  - `sort_order`: One of "asc", "desc" (default "desc")
  - Returns list of records with ID and field values
- `aggregate_platform_group` tool with parameters:
  - `group_name`: Platform group name (required)
  - `aggregations`: List of aggregation specs, each containing:
    - `field`: Field to aggregate (required)
    - `function`: One of "count", "sum", "avg", "min", "max" (required)
    - `alias`: Name for result column (optional)
  - `group_by`: List of fields to group by (optional)
  - `filters`: Optional key-value filters on record fields
  - `time_bucket`: For time-series grouping - one of "hour", "day", "week", "month", "quarter", "year" (optional)
  - `limit`: Maximum groups returned, 1-1000 (default 100)
  - Returns list of aggregation results with group keys and computed values
- CRUD tools (`list_platform_groups`, `search_platform_group`, `get_platform_group_record`, `list_platform_group_records`) are generic and work with any platform group type (TerminusDB or PostgreSQL-backed)
- `aggregate_platform_group` requires PostgreSQL-backed groups (uses SQL aggregation via `PostgreSQLQueryService.aggregate()` for efficiency)
- TerminusDB-backed groups use Feature 1.6 (Knowledge Graph Tools) for relationship traversal instead of SQL aggregations
- Routes queries through `PlatformGroupRecordService` which handles backend abstraction
- Field names and types are determined by the group's schema
- All operations scoped to authenticated user's tenant

---

### Feature 1.8: OAuth 2.1 Authorization

**Priority:** High

#### Outcome
MCP clients authenticate via OAuth 2.1 with scoped access tokens.

#### Requirements
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

---

### Feature 1.9: Prompt Templates

**Priority:** Low

#### Outcome
Pre-built MCP prompts for common workflows.

#### Requirements
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

---

### Feature 1.10: Observability Integration

**Priority:** Medium

#### Outcome
MCP tool invocations are traced and logged through existing OpenTelemetry infrastructure.

#### Requirements
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

---

### Feature 1.11: Deployment Configuration

**Priority:** High

#### Outcome
MCP server deployable alongside Django in production.

#### Requirements
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

---

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

---

## Security Considerations

- OAuth 2.1 with PKCE required for all public clients
- Scope-based tool access control enforced at the MCP server layer
- All queries scoped to authenticated user's tenant (team_slug from token)
- Rate limiting at nginx layer (requests per minute per client)
- Audit logging of all tool invocations with user context
- Access tokens expire after 1 hour
- Refresh tokens expire after 30 days
- No tool accepts raw SQL or arbitrary code execution

---

## Dependencies

**Depends On:**
- [SQH-EPIC-12](SQH-EPIC-12-Document-Management.md) - Document search/processing (complete)
- [SQH-EPIC-06](SQH-EPIC-06-AI-Services.md) - RAG chat service (complete)
- [SQH-EPIC-02](SQH-EPIC-02-Unified-Data-Access-Layer.md) - Unified Data Access Layer (for Feature 1.7 Platform Group Tools)

**Related To:**
- [SQH-EPIC-08](SQH-EPIC-08-Record-Access-Control.md) - Access control patterns

---

## References

- [MCP Specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [FastMCP](https://github.com/jlowin/fastmcp) - Higher-level Python framework for building MCP servers (recommended for rapid development)
- [RFC 9728 - OAuth Protected Resource Metadata](https://datatracker.ietf.org/doc/html/rfc9728)
