---
status: "Not Started"
priority: "Medium"
assigned: ""
dependencies:
  - "[[Feature 1.1 MCP Server Foundation]]"
  - "[[../SQH-EPIC-02-Unified-Data-Access-Layer/00-Unified-Data-Access-Layer|SQH-EPIC-02]]"
linear_id: ""
---

# Feature 1.7: Platform Group Tools

## Outcome

AI clients can query and search records within any Platform Group configured by the tenant, regardless of storage backend (TerminusDB or PostgreSQL).

## What Success Looks Like

- AI can list available platform groups
- AI can search and filter records within groups
- AI can retrieve individual records
- AI can aggregate data for reporting
- Operations work consistently across storage backends

## Scope: Owned Files

- `mcp_server/tools/platform_groups.py`

## Requirements

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
