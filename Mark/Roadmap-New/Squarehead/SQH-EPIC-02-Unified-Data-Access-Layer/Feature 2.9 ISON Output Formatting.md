---
status: "Not Started"
priority: "Low"
assigned: ""
dependencies:
  - "[[Feature 2.6 PostgreSQL Query Service]]"
  - "[[Feature 2.7 TerminusDB Query Service]]"
linear_id: "SQU-55"
---

# Feature 2.9: ISON Output Formatting for AI Context

## Outcome

Query results from PostgreSQL, TerminusDB, and hybrid search can be formatted as ISON for token-efficient injection into LLM context.

## What Success Looks Like

- Large result sets consume fewer tokens
- Tabular format is readable by LLMs
- Formatting is opt-in via parameter
- 30-70% token reduction achieved

## Context

- Large result sets (100s-1000s of rows) consume significant context tokens
- ISON provides 30-70% token reduction over JSON
- Tabular format aligns well with query results
- LLM reads the data; doesn't need to generate it (accuracy less critical than for output)

## Example

```
# JSON (verbose) - 89 tokens
[{"id": "123", "name": "Acme Corp", "status": "active"}, {"id": "456", "name": "Globex", "status": "inactive"}]

# ISON (compact) - ~40 tokens
@accounts
| id  | name      | status
| 123 | Acme Corp | active
| 456 | Globex    | inactive
```

## Scope: Owned Files

- `apps/platform_groups/query_services/formatters/__init__.py` - **NEW**
- `apps/platform_groups/query_services/formatters/ison.py` - **NEW**
- `apps/platform_groups/query_services/postgresql.py` - Extend
- `apps/platform_groups/query_services/terminusdb.py` - Extend

## Requirements

- Query services accept `output_format` parameter (json, ison)
- ISON serializer formats tabular results compactly
- PostgreSQLQueryService supports ISON output format
- TerminusDBQueryService supports ISON output format
- Usage patterns for AI context injection are documented

## References

- [ISON Official Site](https://www.ison.dev/)
- [ISON GitHub](https://github.com/maheshvaikri-code/ison)
