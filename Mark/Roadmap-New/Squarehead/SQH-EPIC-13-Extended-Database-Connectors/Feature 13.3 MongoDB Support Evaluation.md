---
status: "Not Started"
priority: "Low"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 13.3: MongoDB Support Evaluation

## Outcome

Decision documented on whether MongoDB CDC makes sense for our architecture.

## What Success Looks Like

- Architectural differences are documented
- Recommendation is made: implement, defer, or out-of-scope
- If implementing: design document-to-table mapping strategy

## Context

MongoDB is fundamentally different from relational databases:
- No schema/tables/columns - uses collections and documents
- Debezium MongoDB connector has different configuration model
- Our discovery logic is table-based (SQLAlchemy)
- May need separate code paths rather than plugin pattern

## Scope: Owned Files

- `docs/cdc/mongodb-evaluation.md`

## Requirements

- Evaluate if MongoDB CDC fits our use cases
- Document architectural differences
- Recommend: implement, defer, or out-of-scope
- If implementing: design document-to-table mapping strategy
