---
status: "Not Started"
priority: "Low"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 8.15: Sharing & Explicit Grants

## Outcome

Users can share individual records with specific team members.

## What Success Looks Like

- Users can share records with specific team members
- Share permission levels are configurable
- Expiring shares are supported
- Active shares can be managed (view, revoke)

## Scope: Owned Files

- `apps/platform_groups/sharing.py`

## Requirements

**Share Model:**

- `RecordShare` model stores record, granted_to, permission_level, and expires_at
- Share permission levels are: VIEW, EDIT, FULL
- Expiring shares are supported

**Share UI:**

- Share button is integrated in record detail views
- User picker allows selecting share recipients
- Active shares can be managed (view, revoke)
