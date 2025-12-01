# Luminous Prompt Library

**Created:** 2025-10-18
**Purpose:** Copy-paste ready prompts for maximum AI assistant precision and effectiveness
**Organization:** Categorized by function for easy access

---

## Quick Reference Card (Most-Used Prompts)

### Session Start
```
Read the Master Context file and confirm you're ready to work. Flag any contradictions you notice between Master Context and current state.
```

### Session End (Capture & Update)
```
Session complete. Please:
1. Capture today's work in a session file
2. Propose additions to Master Context Section 8 (Continuous Improvement Log)
3. Flag anything we learned that should be integrated
```

### Alignment Check
```
Review [document/message/content] against Master Context tone guidelines and messaging framework. Flag anything that doesn't align with our "humble Canadian confidence" standard.
```

### Quick Tone Check
```
Does this sound authentic for Calgary oil & gas community? Check against Master Context Section 2.3 tone examples.
```

---

## Prompt Categories

### 1. Session Management
[session-management.md](session-management.md) - Start session, end session, context capture, Master Context updates

### 2. Documentation
[documentation.md](documentation.md) - Create documents, streamline content, alignment checks, portfolio selection

### 3. Messaging
[messaging.md](messaging.md) - Tone checks, NA-scoping verification, Q&A generation, cultural fit validation

---

## How to Use This Library

### For Quick Tasks:
Copy the prompt from Quick Reference Card above and paste into Claude Code.

### For Complex Tasks:
1. Navigate to the relevant category file (session-management, documentation, messaging)
2. Find the specific prompt for your need
3. Copy the full prompt template
4. Customize the bracketed [placeholders] with your specific details
5. Paste into Claude Code

### For Custom Prompts:
Add your own prompts to the appropriate category file. Follow the template format:
```
### Prompt Name
**When to Use:** [Situation description]
**What it Does:** [Expected outcome]
**Prompt:**
[Copy-paste ready prompt text]
```

---

## Continuous Improvement

**Missing a prompt you use frequently?** Add it to the appropriate category file.
**Prompt not working well?** Update it and note the change at the bottom of the category file.
**Prompt no longer needed?** Move it to a "Deprecated" section at the bottom with reason why.

---

## Master Context Integration

All prompts in this library assume you're working with the Master Context file. If you're starting fresh or in a new session:

1. **Always start with:** "Read the Master Context file and confirm you're ready"
2. **Then use** category-specific prompts for your task
3. **Always end with:** Session capture and continuous improvement update

This ensures every session builds on previous knowledge and compounds learning over time.

---

**Location:** `00-PROMPT-LIBRARY/` (Root level for easy access)
**Last Updated:** 2025-10-18
**Version:** 1.0 (Initial prompt library, evolves over time)
