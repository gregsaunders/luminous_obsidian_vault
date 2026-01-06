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
Reusable chart and dashboard components are available for analytics views, including advanced correlation visualization for time-series data with event overlays.

#### What Success Looks Like
- Developer can add line/bar/pie charts with minimal code
- Charts are responsive and handle loading states
- KPI cards display metrics consistently
- Data tables support sorting/filtering
- Analyst can view multiple data series on shared timeline with event annotations
- Correlations between metrics and events are visually apparent

#### Context
These components will be used by the Luminous Customer Dashboard and other analytics views across Platform Groups. The correlation visualization requirements are driven by biosensor monitoring use cases where NA concentrations must be analyzed alongside operational events (water intake, dosing) and environmental factors (temperature, precipitation).

**Used By:**
- [LUM-EPIC-01 Feature 1.3](../Luminous/LUM-EPIC-01-Customer-Dashboard.md) - Trend Charts
- [LUM-EPIC-01 Feature 1.6](../Luminous/LUM-EPIC-01-Customer-Dashboard.md) - Correlation View
- [SQH-EPIC-09 Feature 9.4](SQH-EPIC-09-AI-Generated-UI.md) - Composable UI Components

#### Technology Options

| Option | Pros | Cons |
|--------|------|------|
| **fl_chart** | Pure Dart, good community, free | Limited advanced features, no multi-axis native support |
| **syncfusion_flutter_charts** | Feature-rich, multi-axis, annotations built-in | Commercial license (~$995/dev/year) |
| **graphic** | Declarative grammar of graphics, flexible | Steeper learning curve, less community |
| **Custom Canvas** | Full control, no dependencies | Significant dev effort, maintenance burden |

**Decision needed:** Evaluate options during implementation spike.

#### Scope: Owned Files
- `frontend/flutter/packages/ui/lib/components/charts/`
- `frontend/flutter/packages/ui/lib/components/dashboard/`

#### Tasks

**Basic Charts:**
- [x] KPI/Stat card component (exists: `stat_card.dart`)
- [ ] Line chart component
- [ ] Bar chart component
- [ ] Pie/donut chart component
- [ ] Chart loading/empty/error states

**Advanced Time Series:**
- [ ] Multi-axis time series component (primary Y-axis + secondary Y-axis for different units)
- [ ] Event annotation layer (vertical markers with labels for operational events)
- [ ] Threshold/reference line support (horizontal lines for alert levels)
- [ ] Correlation highlight bands (shaded regions showing correlation periods)
- [ ] Interactive zoom/pan with date range selection
- [ ] Unified tooltip showing all series values at hovered timestamp

**Data Tables:**
- [ ] Data table with sorting/filtering
- [ ] Column visibility toggle
- [ ] Export to CSV

**Technology Spike:**
- [ ] Evaluate fl_chart for basic charting needs
- [ ] Evaluate syncfusion_flutter_charts for advanced features
- [ ] Prototype multi-axis chart with event annotations
- [ ] Document library recommendation with trade-offs

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
