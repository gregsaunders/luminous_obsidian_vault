---
status: "Not Started"
priority: "High"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 8.4: ABAC Condition Model

## Outcome

RBAC permissions can include attribute conditions that filter records by field values. This extends the existing permission system without replacing it.

## What Success Looks Like

- Permissions can have optional attribute conditions
- Conditions are evaluated at query time
- Admin UI allows defining conditions
- Condition fields are validated against source schema

## Scope: Owned Files

- `apps/platform_groups/permissions.py` - Permission model extension

## Requirements

**Attribute Condition Model:**

- `AttributeCondition` dataclass contains field, operator, and values:
  ```python
  @dataclass(frozen=True)
  class AttributeCondition:
      field: str           # "invoice_type"
      operator: str        # "equals", "in", "not_in", "contains"
      values: list[str]    # ["vendor_bill"]
  ```
- Supported operators are: `equals`, `not_equals`, `in`, `not_in`, `contains`

**Permission Grant with Conditions:**

- `TenantGroupPermissionGrant.attribute_conditions` JSON field is available (optional)
- When conditions are present, ABAC filtering applies *in addition to* RBAC check
- Admin-only UI allows defining conditions
- Condition fields are validated against source schema
