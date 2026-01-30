---
status: "Not Started"
priority: "Medium"
assigned: ""
dependencies:
  - "[[Feature 4.6 Application Shell Architecture]]"
linear_id: ""
---

# Feature 4.10: Agent Progress Panel

## Outcome

The artifacts pane evolves into a three-section panel showing Progress, Artifacts, and Context for the current conversation.

## What Success Looks Like

- User sees Progress section with agent's task breakdown as it unfolds
- Completed steps show checkmarks, current step shows spinner, pending show empty circles
- Artifacts section lists all generated outputs with thumbnails and pin buttons
- Context section shows documents/data pulled into the conversation with relevance scores
- Progress persists when revisiting old conversations
- User can pin any artifact to Dashboard, Chat Shortcuts, Files, or Organization

## Context

Inspired by Claude Cowork's right panel. Provides transparency into agent actions and quick access to generated content.

## Data Models

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

## Scope: Owned Files

- `frontend/flutter/packages/ui/lib/components/agent_panel/`
- `frontend/flutter/packages/ui/lib/components/agent_panel/agent_progress_panel.dart`
- `frontend/flutter/packages/ui/lib/components/agent_panel/progress_tracker.dart`
- `frontend/flutter/packages/ui/lib/components/agent_panel/progress_item.dart`
- `frontend/flutter/packages/ui/lib/components/agent_panel/artifact_list.dart`
- `frontend/flutter/packages/ui/lib/components/agent_panel/artifact_card.dart`
- `frontend/flutter/packages/ui/lib/components/agent_panel/context_list.dart`
- `frontend/flutter/packages/ui/lib/components/agent_panel/context_item.dart`
- `frontend/flutter/packages/ui/lib/components/agent_panel/pin_destination_dialog.dart`

## Requirements

**Progress Section:**
- AgentProgressPanel container has three collapsible sections
- ProgressTracker widget updates live as agent works
- ProgressItem shows status icon and label
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
