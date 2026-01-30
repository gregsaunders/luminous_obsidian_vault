---
status: "In Progress"
priority: "Critical"
assigned: ""
dependencies:
  - "LUM-EPIC-04 Feature 4.1"
linear_id: "SQU-10"
---

# Feature 3.1: User Authentication

**Linear:** [SQU-10](https://linear.app/squarehead/issue/SQU-10)
**Status Note:** Platform has auth, needs customer provisioning

---

## Outcome

A customer user can log in with their credentials and access only their team's data.

---

## What Success Looks Like

- Customer receives invitation email, sets password
- Logs in and sees only their organization's data
- Admin users can invite new team members
- Users who forget passwords can reset them without support

---

## Scope: Owned Files

- `apps/platform_groups/luminous/` (customer-specific auth config)

## Out of Scope (Frozen)

- `square_head/apps/users/` (core platform)
- `square_head/apps/teams/` (core platform)
- `square_head/apps/authentication/` (core platform)

---

## Requirements

- Customer teams can be created and configured for Luminous access
- New users receive email invitations and can set their own passwords
- Viewer role sees data; admin role can invite users and configure settings
- Users can reset forgotten passwords without contacting support

**Existing Code:** `square_head/apps/users/`, `square_head/apps/teams/`
