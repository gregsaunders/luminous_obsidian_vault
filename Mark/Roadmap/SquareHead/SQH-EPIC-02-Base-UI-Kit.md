# EPIC-02: UI Kit and Platform UX

**Status:** 🟡 Partial
**Priority:** High
**Owner:** TBD

---

## Vision

All Flutter applications share a consistent, accessible component library and a unified application shell architecture, enabling rapid UI development while maintaining design consistency and a coherent user experience across desktop, mobile, and web.

---

## User Stories

- As a **Flutter developer**, I can build UIs using documented, reusable components without reinventing common patterns
- As a **designer**, I can define theme tokens that apply consistently across all apps
- As a **user**, I experience consistent interactions and visual design across desktop, mobile, and web
- As a **user**, I can interact with AI agents in a central chat pane while viewing generated artifacts in a side panel
- As a **user on mobile**, I can access the same functionality with panels collapsing into a drawer-based navigation

---

## Context

This EPIC covers both the **component library** and the **application shell architecture** - together they form the foundation layer (Layer 1) in the three-tier UI architecture:

1. **Layer 1: UI Kit + Platform UX** (this epic) - Core components AND application shell shared across all apps
2. **Layer 2: Platform Group Extensions** - Product-specific widgets (Luminous, CRM)
3. **Layer 3: Tenant Customizations** - Customer branding and preferences

**What exists:** Material 3 theming, basic components in `frontend/flutter/packages/ui/`

**What's needed:** Component documentation, accessibility audit, design tokens, component catalog, application shell architecture

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

### Feature 2.6: Application Shell Architecture
**Status:** 🔴 Not Started
**Priority:** High

#### Outcome
All SquareHead applications share a unified 3-pane layout architecture that provides a consistent, AI-native user experience.

#### What Success Looks Like
- User opens desktop app and sees the 3-pane layout
- Left pane shows installed apps/modules (collapsible)
- Center pane is the primary interaction area: chat with AI agents + app icons
- Right pane displays artifacts, visualizations, and generated content (collapsible, opens on demand)
- Panels resize smoothly and remember user preferences
- Mobile users get the same experience with panels collapsed into drawer navigation

#### Context
This is the foundational UX pattern for all SquareHead applications. The architecture is inspired by modern AI-native interfaces where conversation and artifacts coexist.

```
┌─────────────┬───────────────────────┬─────────────────┐
│             │                       │                 │
│   APPS      │       CHAT +          │   ARTIFACTS     │
│   (left)    │       APP ICONS       │   (right)       │
│             │       (center)        │                 │
│  collapsible│                       │  collapsible    │
│             │                       │  opens on       │
│             │                       │  demand         │
└─────────────┴───────────────────────┴─────────────────┘
```

**Used By:**
- [SQH-EPIC-07](SQH-EPIC-07-Frontend-Apps.md) - Desktop, Mobile, Web apps
- [SQH-EPIC-09 Feature 9.5](SQH-EPIC-09-AI-Generated-UI.md) - Ephemeral UI Lifecycle (artifacts pane)

#### Scope: Owned Files
- `frontend/flutter/packages/ui/lib/shell/`
- `frontend/flutter/packages/ui/lib/shell/three_pane_layout.dart`
- `frontend/flutter/packages/ui/lib/shell/collapsible_panel.dart`
- `frontend/flutter/packages/ui/lib/shell/artifacts_pane.dart`

#### Tasks

**Core Shell:**
- [ ] 3-pane layout scaffold widget
- [ ] Collapsible panel component with smooth animations
- [ ] Panel state persistence (remember collapsed/expanded)
- [ ] Drag-to-resize panel borders

**Left Pane (Apps):**
- [ ] App list/grid component
- [ ] App icon with badge support
- [ ] Collapse to icon-only rail mode

**Center Pane (Chat + Icons):**
- [ ] Chat conversation container
- [ ] App icon bar/launcher
- [ ] Agent message components
- [ ] User input area

**Right Pane (Artifacts):**
- [ ] Artifact container widget
- [ ] Auto-open when agent generates content
- [ ] Multiple artifact tabs/stack
- [ ] Close/minimize behavior

**Responsive Behavior:**
- [ ] Mobile: Drawer-based navigation (left pane becomes drawer)
- [ ] Mobile: Bottom sheet for artifacts (right pane)
- [ ] Tablet: 2-pane mode (center + right, left as drawer)
- [ ] Breakpoint definitions

**Design Decisions:**
- **Menu system:** Hierarchical - menu bar changes based on current app context (e.g., Accounting App shows invoices, bills, general ledger; root shows system-wide menu)
- **Keyboard navigation:** Standard keyboard navigation (Tab, Arrow keys, Enter, Escape)
- **Touch gestures:** None for now - standard touch interactions only
- **Platform Group customization:** Platform Groups register app icons via manifest; shell displays icons, Platform Groups own app content

**Tasks - Hierarchical Menu:**
- [ ] Menu bar component with context-aware items
- [ ] Root-level system menu (settings, profile, help)
- [ ] App-level menu integration point (apps provide their menu items)
- [ ] Menu state management (track current app context)

#### Visual Design

**Active Conversation with Artifacts**
![[assets/three-pane-shell-mockup-v2.svg]]
*Full 3-pane layout showing an invoice form in the app pane, an active agent conversation in the chat pane, and generated artifacts (chart + invoice preview) in the right pane. Demonstrates the complete workflow where an agent assists with creating an invoice while surfacing relevant context.*

**Blank Chat Home Screen (Artifacts Collapsed)**
![[assets/three-pane-shell-mockup-v3-blank.svg]]
*Initial state when no conversation is active. The artifacts pane collapses to a thin strip. The chat area displays a home screen with quick-access app icons and conversation starters to help users begin interacting with the AI agent.*

**Form + Chat Side-by-Side (Artifacts Collapsed)**
![[assets/three-pane-shell-mockup-v4-form-and-chat.svg]]
*Working state with the invoice form open alongside the chat home screen. Equal-width panes allow users to work on app content while having the agent ready to assist. The artifacts pane remains collapsed until the agent generates content.*

**Hierarchical Menu Hover State**
![[assets/three-pane-shell-mockup-v5-menu-hover.svg]]
*Demonstrates the hierarchical menu system. When the user hovers over "Invoices" in the menu bar, a dropdown appears with contextual options (All Invoices, New Invoice, Sent, Pending, Settings). Menu items change based on the currently active app.*

---

## Key Files

- `frontend/flutter/packages/ui/` - Base UI Kit package
- `frontend/flutter/packages/ui/lib/theme/` - Material 3 theming
- `frontend/flutter/packages/ui/lib/components/` - Reusable components
- `frontend/flutter/packages/ui/lib/shell/` - Application shell architecture

---

## References

- [CONTRIBUTING.md - LLM-Parallel Development](../../../square_head/CONTRIBUTING.md)
- [SQH-EPIC-07: Frontend Apps](SQH-EPIC-07-Frontend-Apps.md) - Apps that consume this kit
- [LUM-EPIC-01: Customer Dashboard](../Luminous/LUM-EPIC-01-Customer-Dashboard.md) - May depend on Feature 2.4
- Flutter packages: `frontend/flutter/packages/`
