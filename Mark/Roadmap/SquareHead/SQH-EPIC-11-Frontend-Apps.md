---
linear_id: SQU-48
linear_url: https://linear.app/squarehead/issue/SQU-48
---

# EPIC-11: Frontend Apps

**Linear:** [SQU-48](https://linear.app/squarehead/issue/SQU-48)
**Status:** Partial
**Priority:** Medium
**Owner:** TBD

---

## Vision

Users can access the platform through native desktop, mobile, and web applications with consistent UX and dynamic form capabilities.

---

## User Stories

- As a **desktop user**, I can work offline and sync when connected
- As a **developer**, I can render dynamic forms from JSON schema using documented patterns
- As a **user**, I can visualize graph data relationships interactively

---

## Context

Flutter monorepo for desktop/mobile/web apps, plus React graph visualizer. Dynamic form system works; some features incomplete.

**What exists:** Flutter monorepo (Melos), apps (desktop, mobile, web), packages (core, ui, workflows), Material 3 theming, React graph visualizer

**What's needed:** Documentation, desktop sync completion, maintenance, web modernization

**Depends on:** [SQH-EPIC-02: Base UI Kit](SQH-EPIC-02-Base-UI-Kit.md) for shared components

---

## Features

### Feature 11.1: Flutter Dynamic Forms Documentation

#### Outcome
A developer can implement dynamic forms following documented patterns.

#### Scope: Owned Files
- `frontend/flutter/packages/workflows/README.md`
- `docs/flutter/dynamic-forms/`

#### Tasks
- [ ] WorkflowFormRenderer usage
- [ ] JSON schema field mapping
- [ ] Conditional logic patterns
- [ ] Grid layout system

---

### Feature 11.2: Desktop Sync Completion

#### Outcome
Desktop app users can work offline and sync files when connected.

#### Scope: Owned Files
- `frontend/flutter/apps/desktop/lib/sync/`

#### Tasks
- [ ] rclone-based file sync
- [ ] Offline capability
- [ ] Conflict resolution

---

### Feature 11.3: React Graph Visualizer Maintenance

#### Outcome
Graph visualizer stays current and integrates well with TerminusDB.

#### Scope: Owned Files
- `frontend/react/graph-visualizer/`

#### Tasks
- [ ] Dependency updates
- [ ] TerminusDB integration improvements

---

### Feature 11.4: Web App Modernization

#### Outcome
Web app performs well and works on mobile browsers.

#### Scope: Owned Files
- `frontend/flutter/apps/web_app/`

#### Tasks
- [ ] Performance optimization
- [ ] Mobile responsiveness

---

## Key Files

- `frontend/flutter/apps/desktop/` - Desktop app
- `frontend/flutter/apps/mobile/` - Mobile app
- `frontend/flutter/apps/web_app/` - Web app
- `frontend/flutter/packages/workflows/` - Form rendering
- `frontend/flutter/packages/ui/` - Theme/components (see EPIC-02)
- `frontend/react/graph-visualizer/` - React graph viz
