---
status: "Not Started"
priority: "Medium"
assigned: ""
dependencies:
  - "[[Feature 4.6 Application Shell Architecture]]"
linear_id: ""
---

# Feature 4.9: Hierarchical Prompt Shortcuts

## Outcome

Users can quickly access AI agent actions through a drill-down shortcut system that replaces static conversation starters.

## What Success Looks Like

- User sees category tiles on chat home screen (Dashboard, Invoices, Search, Reports)
- Tapping a category reveals specific action shortcuts
- Tapping an action populates the chat input with a prompt template
- Placeholders in prompts (`{customer}`, `{date}`) are highlighted and editable
- Users can pin frequently-used shortcuts to "My Shortcuts" section
- Organization admins can define org-wide shortcuts visible to all members

## Context

Inspired by Claude Cowork's hierarchical shortcut system. Short, actionable labels replace long-winded prompt suggestions. Users build muscle memory for common workflows.

## Data Model

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

## Ownership Rules

- **System shortcuts**: Pre-seeded, read-only, always visible
- **Organization shortcuts**: Created by admins, visible to all org members
- **User shortcuts**: Created by user, only visible to that user
- **Override behavior**: User can hide org shortcuts or create personal versions

## Scope: Owned Files

- `frontend/flutter/packages/ui/lib/components/prompt_shortcuts/`
- `frontend/flutter/packages/ui/lib/components/prompt_shortcuts/prompt_shortcut_grid.dart`
- `frontend/flutter/packages/ui/lib/components/prompt_shortcuts/shortcut_category_card.dart`
- `frontend/flutter/packages/ui/lib/components/prompt_shortcuts/shortcut_action_card.dart`
- `frontend/flutter/packages/ui/lib/components/prompt_shortcuts/prompt_input_field.dart`
- `frontend/flutter/packages/ui/lib/components/prompt_shortcuts/pinned_shortcuts_row.dart`
- `apps/desktop/lib/features/chat/data/models/prompt_shortcut.dart`
- `apps/desktop/lib/features/chat/data/repositories/shortcut_repository.dart`

## Requirements

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
