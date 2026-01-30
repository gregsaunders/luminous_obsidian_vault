---
status: "Not Started"
priority: "High"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 8.6: ABAC Evaluator

## Outcome

Attribute conditions from the user's permissions are evaluated at query time to filter results. Works alongside RBAC and Ownership checks.

## What Success Looks Like

- User attribute conditions are extracted from permissions
- Conditions are pushed to storage layer where possible
- Fallback to post-query filtering for complex conditions
- Performance is optimized for common patterns

## Scope: Owned Files

- `apps/documents/access_control.py` - Extend with ABAC

## Requirements

- `ABACEvaluator` class handles condition evaluation
- `get_user_conditions(user, permission)` extracts conditions from granted permissions

**Storage-Native Filtering (preferred - push to database):**

- `WOQLConditionBuilder` converts `AttributeCondition` to WOQL filters:
  ```python
  # AttributeCondition(field="invoice_type", operator="in", values=["vendor_bill"])
  # Generates:
  WOQL().woql_or(
      WOQL().triple("v:Doc", "invoice_type", "vendor_bill"),
  )
  ```
- Qdrant filters are built from user's attribute conditions
- Meilisearch filters are built from conditions

**Post-Query Filtering (fallback only):**

- Python-based filtering is available for complex conditions that can't be pushed to storage
- Warning is logged when falling back to post-query filtering (performance concern)
- Documentation specifies which condition types require fallback
