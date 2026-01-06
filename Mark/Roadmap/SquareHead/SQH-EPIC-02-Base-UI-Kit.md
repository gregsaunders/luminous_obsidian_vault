# EPIC-02: Base UI Kit

**Status:** 🟡 Partial
**Priority:** Medium
**Owner:** TBD

---

## Vision

All Flutter applications share a consistent, accessible component library with Material 3 theming, enabling rapid UI development while maintaining design consistency.

---

## User Stories

- As a **Flutter developer**, I can build UIs using documented, reusable components without reinventing common patterns
- As a **designer**, I can define theme tokens that apply consistently across all apps
- As a **user**, I experience consistent interactions and visual design across desktop, mobile, and web
- As an **LLM agent**, I can generate UI code using well-documented component patterns

---

## Context

The Base UI Kit is the foundation layer (Layer 1) in the three-tier UI architecture:

1. **Layer 1: Base UI Kit** (this epic) - Core components shared across all apps
2. **Layer 2: Platform Group Extensions** - Product-specific widgets (Luminous, CRM)
3. **Layer 3: Tenant Customizations** - Customer branding and preferences

**What exists:** Material 3 theming, basic components in `frontend/flutter/packages/ui/`

**What's needed:** Component documentation, accessibility audit, design tokens, component catalog

---

## Features

### Feature 2.1: Component Library Documentation

#### Outcome
A Flutter developer can discover and use all available UI components through browsable documentation.

#### What Success Looks Like
- Developer opens component catalog
- Sees all available components with examples
- Copies code snippets that work immediately
- Understands component props and variants

#### Scope: Owned Files
- `frontend/flutter/packages/ui/README.md`
- `frontend/flutter/packages/ui/doc/`

#### Tasks
- [ ] Catalog all existing components
- [ ] Create usage examples for each
- [ ] Document component API (props, callbacks)
- [ ] Add visual examples/screenshots

---

### Feature 2.2: Design Tokens System

#### Outcome
Theme values (colors, spacing, typography) are defined as tokens that can be customized per tenant.

#### What Success Looks Like
- Developer references tokens instead of hardcoded values
- Changing a token value updates all usages
- Tenants can override brand colors without code changes
- Dark mode works by switching token sets

#### Scope: Owned Files
- `frontend/flutter/packages/ui/lib/tokens/`
- `frontend/flutter/packages/ui/lib/theme/`

#### Tasks
- [ ] Define token categories (color, spacing, typography, elevation)
- [ ] Create token override mechanism
- [ ] Document token usage patterns
- [ ] Implement dark mode token set

---

### Feature 2.3: Accessibility Compliance

#### Outcome
All base components meet WCAG 2.1 AA accessibility requirements.

#### What Success Looks Like
- Components have proper semantic labels
- Color contrast meets minimums
- Keyboard navigation works
- Screen readers announce components correctly

#### Scope: Owned Files
- `frontend/flutter/packages/ui/lib/`

#### Tasks
- [ ] Audit existing components for a11y
- [ ] Add semantic labels where missing
- [ ] Fix color contrast issues
- [ ] Test with screen readers
- [ ] Document a11y requirements for new components

---

### Feature 2.4: Dashboard Components

#### Outcome
Reusable chart and dashboard components are available for analytics views.

#### What Success Looks Like
- Developer can add line/bar/pie charts with minimal code
- Charts are responsive and handle loading states
- KPI cards display metrics consistently
- Data tables support sorting/filtering

#### Context
These components will be used by the Luminous Customer Dashboard and other analytics views across Platform Groups.

#### Scope: Owned Files
- `frontend/flutter/packages/ui/lib/components/charts/`
- `frontend/flutter/packages/ui/lib/components/dashboard/`

#### Tasks
- [ ] Line chart component
- [ ] Bar chart component
- [ ] KPI card component
- [ ] Data table with sorting/filtering
- [ ] Chart loading/empty states

---

### Feature 2.5: Component Storybook/Catalog App

#### Outcome
A standalone app showcases all components for browsing and testing.

#### What Success Looks Like
- Run catalog app locally
- Browse components by category
- See live examples with different props
- Test responsive behavior

#### Scope: Owned Files
- `frontend/flutter/apps/ui_catalog/`

#### Tasks
- [ ] Create catalog app scaffold
- [ ] Add component pages
- [ ] Interactive prop controls
- [ ] Responsive preview modes

---

## Key Files

- `frontend/flutter/packages/ui/` - Base UI Kit package
- `frontend/flutter/packages/ui/lib/theme/` - Material 3 theming
- `frontend/flutter/packages/ui/lib/components/` - Reusable components

---

## References

- [CONTRIBUTING.md - LLM-Parallel Development](../../../square_head/CONTRIBUTING.md)
- [SQH-EPIC-07: Frontend Apps](SQH-EPIC-07-Frontend-Apps.md) - Apps that consume this kit
- [LUM-EPIC-01: Customer Dashboard](../Luminous/LUM-EPIC-01-Customer-Dashboard.md) - May depend on Feature 2.4
- Flutter packages: `frontend/flutter/packages/`
