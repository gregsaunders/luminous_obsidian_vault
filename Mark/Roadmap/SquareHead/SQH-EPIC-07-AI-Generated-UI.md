# EPIC-07: AI-Generated UI

**Status:** 🔴 Not Started
**Priority:** Medium
**Owner:** TBD

---

## Vision

AI agents can generate composable, ephemeral user interfaces on the fly using an LLM-optimized schema format, enabling dynamic data collection and visualization during agent conversations.

---

## User Stories

- As an **AI agent**, I can generate a form UI with minimal tokens to collect structured input from users
- As a **user**, I see a well-designed form appear inline when an agent needs information from me
- As a **developer**, I can extend the UI vocabulary without modifying the core translation layer
- As an **agent developer**, I can request visualizations (charts, tables) using the same schema format

---

## Context

The platform has a sophisticated JSON Schema-based form system (`WorkflowFormRenderer`) that renders Flutter Material 3 widgets from declarative schemas. However, JSON Schema is verbose and not optimized for LLM generation.

**ISON** (Interchange Simple Object Notation) is a data format designed specifically for LLMs:
- 30-70% fewer tokens than JSON
- Based on tabular/relational patterns from LLM training data
- Multi-language parsers (JS/TS, Python, Rust, C++)
- Schema validation support

This EPIC creates an ISON → JSON Schema translation layer, enabling agents to generate UIs efficiently.

**Architecture:**
```
Agent generates ISON → Translator → JSON Schema → WorkflowFormRenderer → Flutter UI
                                                         ↓
                                               User fills form
                                                         ↓
                                               Data back to agent
```

**References:**
- [ISON Official Site](https://www.ison.dev/)
- [ISON GitHub](https://github.com/maheshvaikri-code/ison)

---

## Features

### Feature 7.1: ISON UI Vocabulary

#### Outcome
A defined ISON vocabulary for UI components that maps to the existing JSON Schema form system.

#### What Success Looks Like
- ISON format documented for forms, fields, layouts
- Vocabulary covers: text, number, date, enum, reference, array, object
- Layout hints (col-span) expressible in ISON
- Validation rules expressible in ISON

#### Example Syntax
```
@form contact
| name:str col=6 req           # String field, 6 columns, required
| email:str[email] col=6 req   # Email format
| phone:str col=6              # Optional
| status:enum(active,inactive,lead) col=6
| account:ref(crm.account) col=6
| notes:str[textarea] col=12
```

#### Scope: Owned Files
- `docs/ai-ui/ison-vocabulary.md`
- `docs/ai-ui/examples/`

#### Tasks
- [ ] Define ISON table format for form fields
- [ ] Map ISON types to JSON Schema types
- [ ] Define layout hint syntax (column spans, sections)
- [ ] Define validation rule syntax
- [ ] Document enum and reference field syntax
- [ ] Create example ISON snippets for common patterns

---

### Feature 7.2: ISON → JSON Schema Translator

#### Outcome
A translation layer converts ISON UI definitions to JSON Schema compatible with WorkflowFormRenderer.

#### What Success Looks Like
- ISON input produces valid JSON Schema output
- All existing field types supported
- Layout hints preserved in x-ui-col-span
- Round-trip validation (ISON → JSON → rendered form)

#### Technology Options

| Option | Pros | Cons |
|--------|------|------|
| **Python (backend)** | Existing ISON parser, server-side validation | Requires API call, latency |
| **Dart (frontend)** | No network latency, offline capable | Need to port/wrap ISON parser |
| **Rust via FFI** | Official ISON parser, performant | FFI complexity |

#### Scope: Owned Files
- `square_head/apps/ai_ui/` (Python backend option)
- `frontend/flutter/packages/ai_ui/` (Dart frontend option)

#### Tasks
- [ ] Evaluate ISON parser options for Flutter/Dart
- [ ] Implement ISON parser integration
- [ ] Build translator: ISON → JSON Schema
- [ ] Add x-ui-* extension mapping
- [ ] Unit tests for translation accuracy
- [ ] Integration test with WorkflowFormRenderer

---

### Feature 7.3: Agent UI Generation API

#### Outcome
Agents can request UI generation through a simple API that returns rendered UI specifications.

#### What Success Looks Like
- Agent sends ISON string, receives UI ready for rendering
- Error handling for invalid ISON
- Schema validation before rendering
- Supports both form input and display-only modes

#### Scope: Owned Files
- `square_head/apps/ai_ui/api/`
- `frontend/flutter/packages/workflows/lib/src/widgets/agent_ui_renderer.dart`

#### Tasks
- [ ] API endpoint: POST /api/v1/ai-ui/generate
- [ ] Request validation
- [ ] Error response format
- [ ] Flutter widget for rendering agent-generated UI
- [ ] Callback mechanism for form submission
- [ ] Display-only mode for visualizations

---

### Feature 7.4: Composable UI Components

#### Outcome
The UI vocabulary includes visualization components beyond forms (charts, tables, cards).

#### What Success Looks Like
- Agent can request a chart with data inline
- Agent can request a data table
- Agent can compose multiple components in a layout
- Components use Base UI Kit (SQH-EPIC-02)

#### Example Syntax
```
@chart line
| title "NA Concentration Over Time"
| x_axis date
| y_axis concentration "mg/L"
@data
| 2024-01-01 12.5
| 2024-01-02 14.2
| 2024-01-03 11.8

@stat_card
| value "1,234"
| label "Total Samples"
| trend "+12%"
| trend_positive true
```

#### Dependencies
- [SQH-EPIC-02 Feature 2.4](SQH-EPIC-02-Base-UI-Kit.md) - Dashboard Components

#### Scope: Owned Files
- `docs/ai-ui/ison-vocabulary.md` (extended)
- `frontend/flutter/packages/ai_ui/lib/src/components/`

#### Tasks
- [ ] Define ISON syntax for chart specification
- [ ] Define ISON syntax for data table
- [ ] Define ISON syntax for stat cards
- [ ] Layout composition (multiple components)
- [ ] Integrate with Base UI Kit chart components

---

### Feature 7.5: Ephemeral UI Lifecycle

#### Outcome
Agent-generated UIs can be created, rendered, collected, and disposed without persisting.

#### What Success Looks Like
- UI appears inline in agent conversation
- User fills form, submits to agent
- Agent receives structured data
- UI can be dismissed or replaced
- No permanent UI artifacts created

#### Scope: Owned Files
- `frontend/flutter/packages/workflows/lib/src/widgets/ephemeral_ui_container.dart`

#### Tasks
- [ ] Ephemeral UI container widget
- [ ] Submission callback to agent
- [ ] Dismissal/replacement handling
- [ ] Animation for appearance/disappearance
- [ ] State cleanup on disposal

---

## Key Files

- `docs/ai-ui/` - ISON vocabulary documentation
- `square_head/apps/ai_ui/` - Backend translation service
- `frontend/flutter/packages/ai_ui/` - Flutter package
- `frontend/flutter/packages/workflows/` - Existing form renderer (dependency)

---

## References

- [SQH-EPIC-02: Base UI Kit](SQH-EPIC-02-Base-UI-Kit.md) - UI components (Feature 7.4 dependency)
- [SQH-EPIC-05: Workflow Engine](SQH-EPIC-05-Workflow-Engine.md) - Agent integration
- [SQH-EPIC-10: Frontend Apps](SQH-EPIC-10-Frontend-Apps.md) - Dynamic forms documentation
- [ISON Official Site](https://www.ison.dev/)
- [ISON GitHub](https://github.com/maheshvaikri-code/ison)
- Existing form system: `frontend/flutter/packages/workflows/lib/src/widgets/forms/`
