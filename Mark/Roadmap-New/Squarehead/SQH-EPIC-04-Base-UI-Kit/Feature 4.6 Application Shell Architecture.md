---
status: "Not Started"
priority: "High"
assigned: ""
dependencies: []
linear_id: ""
---

# Feature 4.6: Application Shell Architecture

## Outcome

All SquareHead applications share a unified 3-pane layout architecture that provides a consistent, AI-native user experience.

## What Success Looks Like

- User opens desktop app and sees the unified shell with header bar, icon rail, and content panes
- Header bar provides global navigation: hamburger menu, context-aware menus, search, notifications, user profile
- Icon rail shows installed apps; hamburger toggles to expanded drawer with app names
- App content pane renders forms, lists, and detail views from Platform Groups
- Chat pane shows AI agent conversation or home screen with quick access and conversation starters
- Artifacts pane displays agent-generated content (charts, previews, documents)
- Panels resize smoothly and remember user preferences
- Mobile users get the same functionality with adaptive drawer/bottom sheet navigation

## Context

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

**Used By:**
- [[../SQH-EPIC-11-Frontend-Apps/00-Frontend-Apps|SQH-EPIC-11]] - Desktop, Mobile, Web apps
- [[../SQH-EPIC-10-AI-Generated-UI/00-AI-Generated-UI|SQH-EPIC-10]] Feature 10.4 - Ephemeral UI Lifecycle (artifacts pane)

## Scope: Owned Files

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

## Requirements

**Core Shell:**
- 3-pane layout scaffold widget provides the overall structure
- Collapsible panels animate smoothly when expanding/collapsing
- Panel states persist across sessions (collapsed/expanded remembered)
- Panel borders are drag-resizable

**Header Bar:**
- Header bar spans full width in fixed position
- Hamburger menu button toggles icon rail / expanded drawer
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
- Breadcrumb navigation shows hierarchy
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
- **Menu system:** Hierarchical - menu bar changes based on current app context
- **Keyboard navigation:** Standard keyboard navigation (Tab, Arrow keys, Enter, Escape)
- **Touch gestures:** None for now - standard touch interactions only
- **Platform Group customization:** Platform Groups register app icons via manifest; shell displays icons, Platform Groups own app content
- **Chat home screen:** Displayed when no active conversation; includes quick access icons and conversation starters to guide users
