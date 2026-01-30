---
status: "Not Started"
priority: "Medium"
assigned: ""
dependencies:
  - "[[Feature 2.4 PostgreSQL Backend]]"
linear_id: ""
---

# Feature 2.6: PostgreSQL Query Service

## Outcome

Advanced PostgreSQL queries for reporting and analytics (NOT part of unified CRUD).

## What Success Looks Like

- Developer can run GROUP BY queries for analytics
- Multi-table JOINs work for reporting
- Window functions enable advanced analytics
- Raw SQL is available with safety checks

## Scope: Owned Files

- `apps/platform_groups/query_services/__init__.py` - **NEW**
- `apps/platform_groups/query_services/postgresql.py` - **NEW**

## Requirements

- `PostgreSQLQueryService` class provides advanced query capabilities
- `aggregate()` method executes GROUP BY queries with metrics
- `join_query()` method executes multi-table JOINs
- `window_functions()` method supports analytics with window functions
- `raw_sql()` method executes parameterized SQL with safety checks

## Example Usage

```python
pg_query = PostgreSQLQueryService()
summary = pg_query.aggregate("tenant-123", "lab", "AppLabResult",
    group_by=["test_type", "month"],
    metrics={"count": "COUNT(*)", "avg_value": "AVG(value)"}
)
```
