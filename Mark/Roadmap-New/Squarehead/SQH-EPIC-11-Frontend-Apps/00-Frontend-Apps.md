---
status: "In Progress"
priority: "Medium"
epic_id: "SQH-EPIC-11"
linear_id: "SQU-48"
linear_url: "https://linear.app/squarehead/issue/SQU-48"
---

# EPIC-11: Frontend Apps

## Vision

Users can access the platform through native desktop, mobile, and web applications with consistent UX and dynamic form capabilities.

## User Stories

- As a **desktop user**, I can work offline and sync when connected
- As a **developer**, I can render dynamic forms from JSON schema using documented patterns
- As a **user**, I can visualize graph data relationships interactively

## Context

Flutter monorepo for desktop/mobile/web apps, plus React graph visualizer. Dynamic form system works; some features incomplete.

**What exists:** Flutter monorepo (Melos), apps (desktop, mobile, web), packages (core, ui, workflows), Material 3 theming, React graph visualizer

**What's needed:** Documentation, desktop sync completion, maintenance, web modernization

## Dependencies

- [[../SQH-EPIC-04-Base-UI-Kit/00-Base-UI-Kit|SQH-EPIC-04: Base UI Kit]] for shared components

## Features

- [[Feature 11.1 Flutter Dynamic Forms Documentation]]
- [[Feature 11.2 Desktop Sync Completion]]
- [[Feature 11.3 React Graph Visualizer Maintenance]]
- [[Feature 11.4 Web App Modernization]]

## Key Files

- `frontend/flutter/apps/desktop/` - Desktop app
- `frontend/flutter/apps/mobile/` - Mobile app
- `frontend/flutter/apps/web_app/` - Web app
- `frontend/flutter/packages/workflows/` - Form rendering
- `frontend/flutter/packages/ui/` - Theme/components (see EPIC-02)
- `frontend/react/graph-visualizer/` - React graph viz
