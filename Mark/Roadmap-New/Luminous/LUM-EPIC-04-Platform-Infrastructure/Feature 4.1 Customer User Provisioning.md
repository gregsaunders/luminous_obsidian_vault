---
status: "In Progress"
priority: "High"
assigned: ""
dependencies: []
linear_id: "SQU-22"
---

# Feature 4.1: Customer User Provisioning

**Linear:** [SQU-22](https://linear.app/squarehead/issue/SQU-22)
**Status Note:** Framework exists

**Used By:**
- [[../LUM-EPIC-03-Customer-Dashboard/Feature 3.1 User Authentication|LUM-EPIC-03 Feature 3.1]] - User Authentication
- [[../LUM-EPIC-05-Field-Operations/Feature 5.3 Sample Kit Management|LUM-EPIC-05 Feature 5.3]] - Sample Kit Management

---

## Outcome

A Luminous admin can create customer teams and invite users through a self-service workflow.

---

## What Success Looks Like

- Admin creates new customer team from admin panel
- Enters customer info, clicks "Create"
- Invites users by email address
- Users receive invitation, set password, gain access
- No developer involvement required

---

## Scope: Owned Files

- `apps/platform_groups/luminous/admin/` (customer admin UI)

## Out of Scope (Frozen)

- `square_head/apps/teams/` - Multi-tenancy framework (core)
- `square_head/apps/users/` - User management (core)
- `square_head/apps/authentication/` - Auth flows (core)

---

## Requirements

- Customer teams can be created through a self-service workflow
- Admin UI allows creating and managing customer teams without developer help
- User invitations are sent via email with account setup instructions
- Roles are defined: viewer (read-only), admin (manage users), API access (integration)
- API keys can be generated for customer integrations

---

## Platform Capabilities (Reuse)

Luminous leverages existing SquareHead team management:
- **RBAC** (`apps/teams/roles.py`) - Admin/Editor/Viewer roles ready to use
- **Invitations** (`apps/teams/invitations.py`) - Email invite flow implemented
- **Auto-provisioning** (`apps/teams/signals.py`) - Storage auto-created on team setup

---

## Luminous-Specific Requirements

- Customer onboarding checklist documents the provisioning process
- Welcome email uses Luminous-branded template
- New customers can configure their alert thresholds during setup
