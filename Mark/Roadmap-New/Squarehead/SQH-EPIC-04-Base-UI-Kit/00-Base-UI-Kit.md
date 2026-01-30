---
status: "In Progress"
priority: "High"
epic_id: "SQH-EPIC-04"
linear_id: "SQU-39"
linear_url: "https://linear.app/squarehead/issue/SQU-39"
---

# EPIC-04: UI Kit and Platform UX

## Vision

All Flutter applications share a consistent, accessible component library and a unified application shell architecture, enabling rapid UI development while maintaining design consistency and a coherent user experience across desktop, mobile, and web.

## User Stories

- As a **Flutter developer**, I can build UIs using documented, reusable components without reinventing common patterns
- As a **designer**, I can define theme tokens that apply consistently across all apps
- As a **user**, I experience consistent interactions and visual design across desktop, mobile, and web
- As a **user**, I can interact with AI agents in a central chat pane while viewing generated artifacts in a side panel
- As a **user on mobile**, I can access the same functionality with panels collapsing into a drawer-based navigation

## Context

This EPIC covers both the **component library** and the **application shell architecture** - together they form the foundation layer (Layer 1) in the three-tier UI architecture:

1. **Layer 1: UI Kit + Platform UX** (this epic) - Core components AND application shell shared across all apps
2. **Layer 2: Platform Group Extensions** - Product-specific widgets (Luminous, CRM)
3. **Layer 3: Tenant Customizations** - Customer branding and preferences

**What exists:** Material 3 theming, basic components in `frontend/flutter/packages/ui/`

**What's needed:** Component documentation, accessibility audit, design tokens, component catalog, application shell architecture

## Features

- [[Feature 4.1 Component Library Documentation]]
- [[Feature 4.2 Design Tokens System]]
- [[Feature 4.3 Accessibility Compliance]]
- [[Feature 4.4 Dashboard Components]]
- [[Feature 4.5 Component Storybook]]
- [[Feature 4.6 Application Shell Architecture]]
- [[Feature 4.7 List Table Component]]
- [[Feature 4.8 Map Component]]
- [[Feature 4.9 Hierarchical Prompt Shortcuts]]
- [[Feature 4.10 Agent Progress Panel]]
- [[Feature 4.11 Gradient Fade Layout]]

## Key Files

- `frontend/flutter/packages/ui/` - Base UI Kit package
- `frontend/flutter/packages/ui/lib/theme/` - Material 3 theming
- `frontend/flutter/packages/ui/lib/components/` - Reusable components
- `frontend/flutter/packages/ui/lib/components/data_table/` - List/Table component
- `frontend/flutter/packages/ui/lib/components/map/` - Map component
- `frontend/flutter/packages/ui/lib/shell/` - Application shell architecture
- `frontend/flutter/packages/ui/lib/components/prompt_shortcuts/` - Hierarchical prompt shortcuts
- `frontend/flutter/packages/ui/lib/components/agent_panel/` - Agent progress panel
- `frontend/flutter/packages/ui/lib/layout/` - Pane layout and fade effects

## Dependencies

**Depends On:** None (foundation layer)

**Used By:**
- [[../SQH-EPIC-11-Frontend-Apps/00-Frontend-Apps|SQH-EPIC-11]] - Desktop, Mobile, Web apps
- [[../SQH-EPIC-10-AI-Generated-UI/00-AI-Generated-UI|SQH-EPIC-10]] - Composable UI Components
- [[../../Luminous/LUM-EPIC-03-Customer-Dashboard/00-Customer-Dashboard|LUM-EPIC-03]] - Trend Charts and Correlation View

## References

- [CONTRIBUTING.md - LLM-Parallel Development](../../../square_head/CONTRIBUTING.md)
- [[SQH-EPIC-11-Frontend-Apps]] - Apps that consume this kit
- [[LUM-EPIC-03-Customer-Dashboard]] - May depend on Feature 4.4
- [[../../Luminous/LUM-EPIC-02-Unified-Water-Quality-Data-Model/00-Unified-Water-Quality-Data-Model|LUM-EPIC-02]] - Depends on Feature 4.8 (Map Component)
- Flutter packages: `frontend/flutter/packages/`
