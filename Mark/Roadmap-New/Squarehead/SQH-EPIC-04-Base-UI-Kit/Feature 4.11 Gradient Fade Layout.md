---
status: "Not Started"
priority: "Low"
assigned: ""
dependencies:
  - "[[Feature 4.6 Application Shell Architecture]]"
  - "[[Feature 4.10 Agent Progress Panel]]"
linear_id: ""
---

# Feature 4.11: Gradient Fade Layout

## Outcome

When an artifact opens full-width, the right panel compresses with a gradient fade effect hinting at more content.

## What Success Looks Like

- User opens artifact - right panel smoothly compresses to ~80px
- Right edge of compressed panel shows content fading to transparent
- User sees partial "PROGRESS", "ARTIFACTS", "CONTEXT" headers through fade
- Hovering/tapping faded area slides panel out to full width
- Clicking outside or swiping left slides panel back with fade
- Animation is smooth (300ms easing)

## Context

Inspired by Claude Cowork's right panel behavior. The gradient fade hints "there's more here" without harsh cutoffs.

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

## Pane States

```dart
enum RightPaneState {
  expanded,   // Full 280px width
  faded,      // ~80px with gradient fade
  collapsed,  // Hidden (mobile)
}
```

## Scope: Owned Files

- `frontend/flutter/packages/ui/lib/layout/pane_controller.dart`
- `frontend/flutter/packages/ui/lib/layout/faded_pane_wrapper.dart`
- `frontend/flutter/packages/ui/lib/layout/app_layout.dart`

## Requirements

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

## Flutter Implementation Note

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
