---
linear_id: SQU-39
linear_url: https://linear.app/squarehead/issue/SQU-39
---

# EPIC-04: UI Kit and Platform UX

**Linear:** [SQU-39](https://linear.app/squarehead/issue/SQU-39)
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

### Feature 4.1: Component Library Documentation

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

#### Requirements
- All existing components are cataloged with descriptions
- Each component has working usage examples
- Component APIs are documented: props, callbacks, and usage patterns
- Visual examples/screenshots show component variants and states

---

### Feature 4.2: Design Tokens System

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

#### Requirements
- Token categories are defined: color, spacing, typography, elevation
- Token override mechanism allows tenants to customize values
- Token usage patterns are documented with examples
- Dark mode token set enables theme switching

---

### Feature 4.3: Accessibility Compliance

#### Outcome
All base components meet WCAG 2.1 AA accessibility requirements.

#### What Success Looks Like
- Components have proper semantic labels
- Color contrast meets minimums
- Keyboard navigation works
- Screen readers announce components correctly

#### Scope: Owned Files
- `frontend/flutter/packages/ui/lib/`

#### Requirements
- Existing components are audited for accessibility compliance
- Semantic labels are present on all interactive elements
- Color contrast meets WCAG 2.1 AA minimums
- Components are tested with screen readers and work correctly
- Accessibility requirements are documented for new component development

---

### Feature 4.4: Dashboard Components

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
- [LUM-EPIC-03 Feature 3.3](../Luminous/LUM-EPIC-03-Customer-Dashboard.md) - Trend Charts
- [LUM-EPIC-03 Feature 3.6](../Luminous/LUM-EPIC-03-Customer-Dashboard.md) - Correlation View
- [SQH-EPIC-10 Feature 10.3](SQH-EPIC-10-AI-Generated-UI.md) - Composable UI Components

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

#### Requirements

**Basic Charts:**
- KPI/Stat card component displays metrics (exists: `stat_card.dart`) ✓
- Line chart component renders time-series data
- Bar chart component displays categorical comparisons
- Pie/donut chart component shows proportional data
- All charts handle loading, empty, and error states gracefully

**Advanced Time Series:**
- Multi-axis chart supports primary and secondary Y-axes with different units
- Event annotation layer displays vertical markers with labels for operational events
- Threshold/reference lines show horizontal alert level indicators
- Correlation highlight bands shade regions showing correlation periods
- Interactive zoom/pan allows date range selection
- Unified tooltip displays all series values at hovered timestamp

**Technology Spike:**
- fl_chart is evaluated for basic charting needs
- syncfusion_flutter_charts is evaluated for advanced features
- Multi-axis chart with event annotations is prototyped
- Library recommendation is documented with trade-offs

---

### Feature 4.5: Component Storybook/Catalog App

#### Outcome
A standalone app showcases all components for browsing and testing.

#### What Success Looks Like
- Run catalog app locally
- Browse components by category
- See live examples with different props
- Test responsive behavior

#### Scope: Owned Files
- `frontend/flutter/apps/ui_catalog/`

#### Requirements
- Catalog app scaffold is created and runnable
- Each component has its own browsable page
- Interactive controls allow changing props and seeing results live
- Responsive preview modes show components at different viewport sizes

---

### Feature 4.6: Application Shell Architecture
**Status:** 🔴 Not Started
**Priority:** High

#### Outcome
All SquareHead applications share a unified 3-pane layout architecture that provides a consistent, AI-native user experience.

#### What Success Looks Like
- User opens desktop app and sees the unified shell with header bar, icon rail, and content panes
- Header bar provides global navigation: hamburger menu, context-aware menus, search, notifications, user profile
- Icon rail shows installed apps; hamburger toggles to expanded drawer with app names
- App content pane renders forms, lists, and detail views from Platform Groups
- Chat pane shows AI agent conversation or home screen with quick access and conversation starters
- Artifacts pane displays agent-generated content (charts, previews, documents)
- Panels resize smoothly and remember user preferences
- Mobile users get the same functionality with adaptive drawer/bottom sheet navigation

#### Context
This is the foundational UX pattern for all SquareHead applications. The architecture is inspired by modern AI-native interfaces where conversation and artifacts coexist.

```
┌──────────────────────────────────────────────────────────────────────┐
│ ☰  SquareHead   │ Invoices │ Bills │ Ledger │  🔍 Search  │ 🔔 👤   │
├────┬─────────────────────────┬─────────────────┬─────────────────────┤
│    │                         │                 │                     │
│ 📊 │      APP CONTENT        │      CHAT       │     ARTIFACTS       │
│ 💰 │   (forms, lists,        │  (conversation  │   (charts, docs,    │
│ 🧪 │    detail views)        │   or home       │    previews)        │
│ 📋 │                         │   screen)       │                     │
│    │                         │                 │   opens on demand   │
│ ⚙️ │                         │                 │                     │
└────┴─────────────────────────┴─────────────────┴─────────────────────┘
 Rail        App Pane              Chat Pane         Artifacts Pane
```

**Key Concepts**
![[assets/three-pane-shell-mockup-v2b-annotated.svg]]
*Annotated version highlighting the core interaction model: (1) App-context aware chat - the agent sees what you're working on and can reference it in conversation, (2) Artifacts pane opens on demand - generated content like charts and previews appear when the agent creates them, (3) Bidirectional context flow - the chat references form data while generating artifacts that relate to the current task.*


**Used By:**
- [SQH-EPIC-11](SQH-EPIC-11-Frontend-Apps.md) - Desktop, Mobile, Web apps
- [SQH-EPIC-10 Feature 10.4](SQH-EPIC-10-AI-Generated-UI.md) - Ephemeral UI Lifecycle (artifacts pane)

#### Scope: Owned Files
- `frontend/flutter/packages/ui/lib/shell/`
- `frontend/flutter/packages/ui/lib/shell/three_pane_layout.dart`
- `frontend/flutter/packages/ui/lib/shell/header_bar.dart`
- `frontend/flutter/packages/ui/lib/shell/icon_rail.dart`
- `frontend/flutter/packages/ui/lib/shell/app_drawer.dart`
- `frontend/flutter/packages/ui/lib/shell/app_content_pane.dart`
- `frontend/flutter/packages/ui/lib/shell/chat_pane.dart`
- `frontend/flutter/packages/ui/lib/shell/chat_home_screen.dart`
- `frontend/flutter/packages/ui/lib/shell/artifacts_pane.dart`
- `frontend/flutter/packages/ui/lib/shell/collapsible_panel.dart`
- `frontend/flutter/packages/ui/lib/components/search_bar.dart`
- `frontend/flutter/packages/ui/lib/components/notification_icon.dart`
- `frontend/flutter/packages/ui/lib/components/user_menu.dart`
- `frontend/flutter/packages/ui/lib/components/dropdown_menu.dart`

#### Requirements

**Core Shell:**
- 3-pane layout scaffold widget provides the overall structure
- Collapsible panels animate smoothly when expanding/collapsing
- Panel states persist across sessions (collapsed/expanded remembered)
- Panel borders are drag-resizable

**Header Bar:**
- Header bar spans full width in fixed position
- Hamburger menu button toggles icon rail ↔ expanded drawer
- App logo and title are displayed
- Context-aware menu bar shows dropdowns for current app
- Menu items have hover states and dropdowns position correctly
- Global search bar is accessible from header
- Search results appear in popover/dropdown
- Notification icon shows badge count
- Notification dropdown lists recent notifications
- User profile button shows avatar
- User dropdown menu provides profile, settings, logout options

**Icon Rail + App Drawer:**
- Icon rail is a thin strip, always visible on desktop
- App icons show tooltips on hover
- App icons support badge indicators (notifications, status)
- Active app is visually highlighted
- Hamburger toggle expands rail to full drawer
- Expanded drawer shows icon + app name + description
- Settings icon appears at bottom of rail
- Collapse/expand animates smoothly

**App Content Pane:**
- App content container renders Platform Group UI
- Action bar is sticky with title and action buttons
- Breadcrumb navigation shows hierarchy (e.g., Invoices > INV-2026-0042 > Edit)
- Breadcrumb segments are clickable for quick navigation
- Deep hierarchies truncate with ellipsis
- Home/root icon appears at breadcrumb start
- Tab bar supports multi-view navigation with close buttons
- Active tab is visually indicated
- Tab overflow menu appears when too many tabs
- Tabs can be drag-reordered
- Open tabs persist per app
- Tab limit is enforced with user notification
- Form rendering uses WorkflowFormRenderer
- List/table and detail views render in designated areas
- Scroll behavior keeps action bar sticky
- Loading, empty, and error states are handled

**Chat Pane:**
- Chat conversation container displays messages
- Agent and user message bubbles are visually distinct
- Message timestamps are displayed
- Typing indicator shows when agent is responding
- User input area includes send button
- Attachment button allows file picker access
- Chat home screen shows when no conversation is active:
  - Welcome message with personalized greeting
  - Quick Access grid provides fast app navigation
  - "Try Asking" section shows conversation starters
  - Conversation starter cards are clickable to send

**Artifacts Pane:**
- Artifact container widget displays generated content
- Pane auto-opens when agent generates artifacts
- Multiple artifacts appear as tabs/stack
- Artifact tab bar includes close buttons
- Close/minimize behavior works consistently
- Collapsed state shows thin strip indicator
- Expand arrow/button restores full pane

**Responsive Behavior:**
- Mobile: Icon rail becomes drawer-based navigation
- Mobile: Artifacts appear as bottom sheet
- Mobile: Chat is primary view, app content in drawer
- Tablet: 2-pane mode (app + chat) with artifacts as overlay
- Breakpoints: mobile < 600, tablet < 1024, desktop >= 1024

**Design Decisions:**
- **Menu system:** Hierarchical - menu bar changes based on current app context (e.g., Accounting App shows invoices, bills, general ledger; root shows system-wide menu)
- **Keyboard navigation:** Standard keyboard navigation (Tab, Arrow keys, Enter, Escape)
- **Touch gestures:** None for now - standard touch interactions only
- **Platform Group customization:** Platform Groups register app icons via manifest; shell displays icons, Platform Groups own app content
- **Chat home screen:** Displayed when no active conversation; includes quick access icons and conversation starters to guide users

#### Visual Design

**Active Conversation with Artifacts**
![[assets/three-pane-shell-mockup-v2.svg]]
*Full 3-pane layout showing an invoice form in the app pane, an active agent conversation in the chat pane, and generated artifacts (chart + invoice preview) in the right pane. Demonstrates the complete workflow where an agent assists with creating an invoice while surfacing relevant context.*


**Blank Chat Home Screen (Artifacts Collapsed)**
![[assets/three-pane-shell-mockup-v3-blank.svg]]
*Initial state when no conversation is active. The artifacts pane collapses to a thin strip. The chat area displays a home screen with quick-access app icons and conversation starters to help users begin interacting with the AI agent.*

**Form + Chat with Tabs and Breadcrumbs (Artifacts Collapsed)**
![[assets/three-pane-shell-mockup-v4-form-and-chat.svg]]
*Working state showing the full App Content Pane navigation stack: tab bar at top (with "All Invoices" and "INV-2026-0042" tabs), breadcrumb trail below (Home › Invoices › INV-2026-0042), and the action bar with context-specific buttons. Equal-width panes allow users to work on app content while having the agent ready to assist.*

**Hierarchical Menu Hover State**
![[assets/three-pane-shell-mockup-v5-menu-hover.svg]]
*Demonstrates the hierarchical menu system. When the user hovers over "Invoices" in the menu bar, a dropdown appears with contextual options (All Invoices, New Invoice, Sent, Pending, Settings). Menu items change based on the currently active app.*

---

### Feature 4.7: List/Table Component
**Status:** 🔴 Not Started
**Priority:** High

#### Outcome
A comprehensive, reusable list/table component that Platform Groups use to display tabular data with full user customization.

#### What Success Looks Like
- Developer renders a data table by passing columns and data
- User can hide/show columns via column visibility menu
- User preferences persist across sessions
- Tables handle large datasets efficiently with virtualization
- Sorting, filtering, and selection work consistently across all tables

#### Context
This is a foundational UI component used across all Platform Groups for displaying lists of records (invoices, customers, sensor readings, etc.). The shell's App Content Pane renders this component.

**Used By:**
- All Platform Groups displaying record lists
- [SQH-EPIC-10 Feature 10.3](SQH-EPIC-10-AI-Generated-UI.md) - AI-generated table views

#### Scope: Owned Files
- `frontend/flutter/packages/ui/lib/components/data_table/`
- `frontend/flutter/packages/ui/lib/components/data_table/data_table.dart`
- `frontend/flutter/packages/ui/lib/components/data_table/column_visibility_menu.dart`
- `frontend/flutter/packages/ui/lib/components/data_table/table_header.dart`
- `frontend/flutter/packages/ui/lib/components/data_table/table_row.dart`

#### Requirements

**Core Table:**
- Data table component accepts typed column definitions
- Column headers display labels and sort indicators
- Table rows render cells with appropriate formatting
- Loading state shows skeleton rows
- Empty state displays customizable message
- Error state offers retry action

**Column Management:**
- Column visibility toggle menu allows hiding/showing columns
- Column visibility preferences persist per-table and per-user
- Column borders are draggable for resizing
- Columns can be reordered via drag-and-drop
- Column widths respect minimum/maximum constraints
- Columns can be pinned (frozen) left or right

**Sorting & Filtering:**
- Single-column sort activates on header click
- Multi-column sort activates on shift+click
- Sort indicators show ascending/descending state
- Column filter popover appears on filter icon click
- Text filters support: contains, starts with, equals
- Numeric filters support: greater than, less than, between
- Date filters support: before, after, range
- Active filters show indicator on column header

**Row Selection:**
- Single-select mode behaves like radio buttons
- Multi-select mode adds checkbox column
- Select all / deselect all works correctly
- Selection callback provides selected row data
- Rows highlight on hover
- Selected rows show distinct styling

**Performance:**
- Virtualized scrolling handles large datasets efficiently
- Lazy loading / infinite scroll loads data as needed
- Re-renders are optimized on data changes

**Export:**
- Visible data can be exported to CSV
- Selected rows can be exported to CSV
- Selected rows can be copied to clipboard

---

### Feature 4.8: Map Component
**Linear:** TBD
**Status:** 🔴 Not Started
**Priority:** High
**Required By:** [LUM-EPIC-02](../Luminous/LUM-EPIC-02-Unified-Water-Quality-Data-Model.md) - Water Quality Dashboard Views

#### Outcome
A reusable map component for displaying geographic data with markers, layers, and interactive features.

#### What Success Looks Like
- Developer can add a map widget with minimal code
- Map supports marker layers from GeoJSON data sources
- Users can pan, zoom, and click markers to see details
- Map handles loading states and error conditions gracefully
- Works across desktop, mobile, and web platforms

#### Context
Geographic visualization is needed across multiple Platform Groups:
- **Luminous**: Water quality monitoring station locations
- **Operations**: Asset locations, service territories
- **Field Services**: Work order locations, route planning

This is a platform-level component to avoid duplicating map implementations.

**Used By:**
- [LUM-EPIC-02 Feature 2.6](../Luminous/LUM-EPIC-02-Unified-Water-Quality-Data-Model.md) - Station map visualization

#### Technology Options

| Option | Pros | Cons |
|--------|------|------|
| **flutter_map** | Open source, Leaflet-based, active community | Requires tile provider setup |
| **google_maps_flutter** | Feature-rich, familiar UX | API key required, usage costs |
| **mapbox_gl** | Beautiful styling, offline support | API key required, commercial license |

**Recommendation:** Start with `flutter_map` + OpenStreetMap tiles for cost-free development; evaluate Mapbox for production if styling needs exceed OSM capabilities.

#### Scope: Owned Files
- `frontend/flutter/packages/ui/lib/components/map/`
- `frontend/flutter/packages/ui/lib/components/map/map_widget.dart`
- `frontend/flutter/packages/ui/lib/components/map/map_marker.dart`
- `frontend/flutter/packages/ui/lib/components/map/map_layer.dart`
- `frontend/flutter/packages/ui/lib/components/map/map_controls.dart`
- `frontend/flutter/packages/ui/lib/components/map/geojson_layer.dart`

#### Requirements

**Core Map:**
- Map widget accepts configurable tile provider
- Initial center/zoom can be set via props or auto-fits to markers
- Pan and zoom interactions work with mouse, touch, and scroll
- Loading state shows placeholder while tiles load
- Error state displays when tile loading fails

**Markers:**
- Marker component accepts customizable icons
- Dense point data clusters automatically
- Marker popup/tooltip appears on tap
- Selected markers show highlighted state
- Markers can bind arbitrary data for popup display

**Layers:**
- GeoJSON layer renders polygon/line/point data
- Layer toggle controls show/hide individual layers
- Layers are styleable (fill color, stroke, opacity)
- Choropleth coloring reflects data values
- Layer legend component explains symbology

**Controls:**
- Zoom in/out buttons are accessible
- Fit-to-bounds button resets view to show all data
- Layer switcher panel manages layer visibility
- Scale bar shows distance reference
- Attribution displays tile provider credits

**Data Integration:**
- GeoJSON data sources bind to layers
- Markers update dynamically without full re-render
- Markers can be filtered by data attributes
- Bounds-based loading fetches only visible area data

**Responsive Behavior:**
- Mobile touch gestures work (pinch zoom, two-finger pan)
- Controls are compact on mobile viewport
- Full-screen toggle expands map to fill screen

---

### Feature 4.9: Hierarchical Prompt Shortcuts
**Status:** 🔴 Not Started
**Priority:** Medium

#### Outcome
Users can quickly access AI agent actions through a drill-down shortcut system that replaces static conversation starters.

#### What Success Looks Like
- User sees category tiles on chat home screen (Dashboard, Invoices, Search, Reports)
- Tapping a category reveals specific action shortcuts
- Tapping an action populates the chat input with a prompt template
- Placeholders in prompts (`{customer}`, `{date}`) are highlighted and editable
- Users can pin frequently-used shortcuts to "My Shortcuts" section
- Organization admins can define org-wide shortcuts visible to all members

#### Context
Inspired by Claude Cowork's hierarchical shortcut system. Short, actionable labels replace long-winded prompt suggestions. Users build muscle memory for common workflows.

**Visual Reference:**
![[assets/three-pane-shell-mockup-v6-shortcuts.svg]]
*Shortcut drill-down flow: (1) Category grid on home screen, (2) Action cards within category, (3) Prompt template with editable placeholders.*

#### Scope: Owned Files
- `frontend/flutter/packages/ui/lib/components/prompt_shortcuts/`
- `frontend/flutter/packages/ui/lib/components/prompt_shortcuts/prompt_shortcut_grid.dart`
- `frontend/flutter/packages/ui/lib/components/prompt_shortcuts/shortcut_category_card.dart`
- `frontend/flutter/packages/ui/lib/components/prompt_shortcuts/shortcut_action_card.dart`
- `frontend/flutter/packages/ui/lib/components/prompt_shortcuts/prompt_input_field.dart`
- `frontend/flutter/packages/ui/lib/components/prompt_shortcuts/pinned_shortcuts_row.dart`
- `apps/desktop/lib/features/chat/data/models/prompt_shortcut.dart`
- `apps/desktop/lib/features/chat/data/repositories/shortcut_repository.dart`

#### Data Model
```dart
class PromptShortcut {
  final String id;
  final String icon;           // Emoji or icon name
  final String label;          // Short label (max ~20 chars)
  final String? description;   // Subtitle text
  final String? promptTemplate; // null = has children
  final List<PromptShortcut>? children;
  final ShortcutScope scope;   // user | organization | system
  final String? ownerId;       // userId or orgId
  final int sortOrder;
}

enum ShortcutScope { user, organization, system }
```

#### Ownership Rules
- **System shortcuts**: Pre-seeded, read-only, always visible
- **Organization shortcuts**: Created by admins, visible to all org members
- **User shortcuts**: Created by user, only visible to that user
- **Override behavior**: User can hide org shortcuts or create personal versions

#### Requirements

**Data Layer:**
- PromptShortcut data model is stored in Drift table
- ShortcutRepository provides CRUD operations
- System default shortcuts are seeded in migration
- API allows organization shortcut management (admin only)

**UI Components:**
- PromptShortcutGrid widget animates drill-down into categories
- ShortcutCategoryCard displays icon + label + description as tile
- ShortcutActionCard shows action tile with prompt preview
- PromptInputField highlights placeholders for editing
- PinnedShortcutsRow displays user's pinned items
- Back navigation returns from category to grid

**User Features:**
- Long-press on shortcut shows "Pin to my shortcuts" action
- Pinned shortcuts section appears at top of home screen
- Pinned shortcuts can be removed
- Pinned shortcuts can be reordered via drag-and-drop

**Admin Features:**
- Organization shortcut management screen is accessible to admins
- Admins can create, edit, and delete organization shortcuts
- Preview shows how shortcuts appear to organization members

---

### Feature 4.10: Agent Progress Panel
**Status:** 🔴 Not Started
**Priority:** Medium

#### Outcome
The artifacts pane evolves into a three-section panel showing Progress, Artifacts, and Context for the current conversation.

#### What Success Looks Like
- User sees Progress section with agent's task breakdown as it unfolds
- Completed steps show checkmarks, current step shows spinner, pending show empty circles
- Artifacts section lists all generated outputs with thumbnails and pin buttons
- Context section shows documents/data pulled into the conversation with relevance scores
- Progress persists when revisiting old conversations
- User can pin any artifact to Dashboard, Chat Shortcuts, Files, or Organization

#### Context
Inspired by Claude Cowork's right panel. Provides transparency into agent actions and quick access to generated content.

**Visual Reference:**
![[assets/three-pane-shell-mockup-v7-right-pane.svg]]
*Enhanced right pane with collapsible Progress, Artifacts, and Context sections.*

#### Scope: Owned Files
- `frontend/flutter/packages/ui/lib/components/agent_panel/`
- `frontend/flutter/packages/ui/lib/components/agent_panel/agent_progress_panel.dart`
- `frontend/flutter/packages/ui/lib/components/agent_panel/progress_tracker.dart`
- `frontend/flutter/packages/ui/lib/components/agent_panel/progress_item.dart`
- `frontend/flutter/packages/ui/lib/components/agent_panel/artifact_list.dart`
- `frontend/flutter/packages/ui/lib/components/agent_panel/artifact_card.dart`
- `frontend/flutter/packages/ui/lib/components/agent_panel/context_list.dart`
- `frontend/flutter/packages/ui/lib/components/agent_panel/context_item.dart`
- `frontend/flutter/packages/ui/lib/components/agent_panel/pin_destination_dialog.dart`

#### Data Models
```dart
class AgentProgress {
  final String id;
  final String conversationId;
  final String label;
  final AgentProgressStatus status;
  final DateTime? startedAt;
  final DateTime? completedAt;
  final List<AgentProgress>? subTasks;
}

enum AgentProgressStatus { pending, inProgress, completed, failed }

class ConversationArtifact {
  final String id;
  final String conversationId;
  final String title;
  final ArtifactType type;  // chart, table, document, form, preview
  final String? thumbnailUrl;
  final dynamic content;
  final DateTime createdAt;
}

class ContextSource {
  final String id;
  final String conversationId;
  final String name;
  final String sourceType;  // document, database, api
  final double relevanceScore;
  final String? previewText;
}
```

#### Requirements

**Progress Section:**
- AgentProgressPanel container has three collapsible sections
- ProgressTracker widget updates live as agent works
- ProgressItem shows status icon (✓ ● ○) and label
- Progress persists to conversation record
- Status transitions animate smoothly

**Artifacts Section:**
- ArtifactList scrolls through generated content cards
- ArtifactCard shows thumbnail, title, type badge, timestamp
- Pin button on artifact cards allows saving
- PinDestinationDialog offers options: Dashboard, Chat Shortcuts, Files, Organization
- Tapping artifact opens full view

**Context Section:**
- ContextList shows source items used in conversation
- ContextItem displays name, type icon, relevance percentage
- Sources link to original document/record
- Sources connect to existing RAG document_sources from chat

**Persistence:**
- Progress steps are stored in conversation record
- Artifacts are linked to conversation
- Progress and artifacts load when opening old conversations

---

### Feature 4.11: Gradient Fade Layout
**Status:** 🔴 Not Started
**Priority:** Low

#### Outcome
When an artifact opens full-width, the right panel compresses with a gradient fade effect hinting at more content.

#### What Success Looks Like
- User opens artifact → right panel smoothly compresses to ~80px
- Right edge of compressed panel shows content fading to transparent
- User sees partial "PROGRESS", "ARTIFACTS", "CONTEXT" headers through fade
- Hovering/tapping faded area slides panel out to full width
- Clicking outside or swiping left slides panel back with fade
- Animation is smooth (300ms easing)

#### Context
Inspired by Claude Cowork's right panel behavior. The gradient fade hints "there's more here" without harsh cutoffs.

**Visual Reference:**
![[assets/three-pane-shell-mockup-v8-artifact-fade.svg]]
*Artifact expanded with right panel in gradient fade state.*

```
┌────────────────────────────────────┬─────────░░░
│                                    │ PROGRE ░░░
│     FULL ARTIFACT VIEW             │ ──────░░░
│                                    │ ✓ Fetc░░░
│                                    │ ● Gene░░░
│                                    ├─────────░░░
│                                    │ ARTIFA░░░
└────────────────────────────────────┴─────────░░░
                                      ↑ gradient fade
```

#### Scope: Owned Files
- `frontend/flutter/packages/ui/lib/layout/pane_controller.dart`
- `frontend/flutter/packages/ui/lib/layout/faded_pane_wrapper.dart`
- `frontend/flutter/packages/ui/lib/layout/app_layout.dart`

#### Pane States
```dart
enum RightPaneState {
  expanded,   // Full 280px width
  faded,      // ~80px with gradient fade
  collapsed,  // Hidden (mobile)
}
```

#### Requirements

**Layout:**
- PaneController manages pane states
- Artifact open/close events are tracked
- Right pane auto-fades when artifact opens
- Right pane auto-expands when artifact closes

**Animation:**
- FadedPaneWrapper widget applies ShaderMask gradient
- Width changes animate over 300ms with ease-out
- Gradient fades content to transparent at edge

**Interaction:**
- Hovering faded area slides pane out to full width (temporary)
- Tapping faded area on touch devices slides pane out
- Clicking outside or swiping left slides pane back to faded
- Escape key closes artifact and restores full panel

**Responsive:**
- Desktop (>1400px): All panes visible, fade activates on artifact open
- Tablet (900-1400px): Fade behavior is active
- Mobile (<900px): Panel fully collapses (no fade effect)

#### Flutter Implementation Note
```dart
ShaderMask(
  shaderCallback: (bounds) => LinearGradient(
    begin: Alignment.centerLeft,
    end: Alignment.centerRight,
    colors: [Colors.white, Colors.transparent],
    stops: [0.6, 1.0],
  ).createShader(bounds),
  blendMode: BlendMode.dstIn,
  child: rightPaneContent,
)
```

---

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

---

## References

- [CONTRIBUTING.md - LLM-Parallel Development](../../../square_head/CONTRIBUTING.md)
- [SQH-EPIC-11: Frontend Apps](SQH-EPIC-11-Frontend-Apps.md) - Apps that consume this kit
- [LUM-EPIC-03: Customer Dashboard](../Luminous/LUM-EPIC-03-Customer-Dashboard.md) - May depend on Feature 4.4
- [LUM-EPIC-02: Water Quality Data Model](../Luminous/LUM-EPIC-02-Unified-Water-Quality-Data-Model.md) - Depends on Feature 4.8 (Map Component)
- Flutter packages: `frontend/flutter/packages/`
