---
status: "Not Started"
priority: "High"
assigned: ""
dependencies: []
linear_id: "SQU-51"
---

# Feature 10.1: UI Schema Vocabulary

## Outcome

A defined JSON Schema vocabulary for UI components that works with the existing form system and is optimized for LLM generation.

## What Success Looks Like

- JSON Schema conventions documented for forms, fields, layouts
- Schema covers: text, number, date, enum, reference, array, object
- Layout hints (col-span) expressible via `x-ui-*` extensions
- Validation rules expressible in standard JSON Schema format
- Example prompts that reliably produce valid schemas

## Context

Example Schema:
```json
{
  "type": "object",
  "title": "Contact Form",
  "properties": {
    "name": {
      "type": "string",
      "title": "Name",
      "x-ui-col-span": 6
    },
    "email": {
      "type": "string",
      "format": "email",
      "title": "Email",
      "x-ui-col-span": 6
    },
    "phone": {
      "type": "string",
      "title": "Phone",
      "x-ui-col-span": 6
    },
    "status": {
      "type": "string",
      "enum": ["active", "inactive", "lead"],
      "title": "Status",
      "x-ui-col-span": 6
    },
    "notes": {
      "type": "string",
      "title": "Notes",
      "x-ui-col-span": 12,
      "x-ui-widget": "textarea"
    }
  },
  "required": ["name", "email"]
}
```

## Scope: Owned Files

- `docs/ai-ui/schema-vocabulary.md`
- `docs/ai-ui/examples/`

## Requirements

- JSON Schema conventions for form fields are documented
- `x-ui-*` extension vocabulary (col-span, widget, sections) is defined
- Type mappings to Flutter widgets are documented
- Example schemas demonstrate common patterns
- Example prompts reliably produce valid schemas
- Validation rule patterns are documented
