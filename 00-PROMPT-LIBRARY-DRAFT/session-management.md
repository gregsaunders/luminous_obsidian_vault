# Session Management Prompts

**Category:** Session Management
**Purpose:** Standardized prompts for starting sessions, ending sessions, capturing context, and updating Master Context

---

## 1. START SESSION (Standard)

### When to Use:
Every time you start a new Claude Code session where you want to maintain continuity with previous work.

### What it Does:
- Loads Master Context into AI's working memory
- Confirms AI has full context before starting work
- Flags any contradictions between Master Context and current state
- Sets foundation for effective session

### Prompt:
```
Read the Master Context file at:
01-ACTIVE-BUSINESS/daily-operations/context-management/Luminous-Master-Context.md

Confirm you're ready to work and flag any contradictions you notice between Master Context and current state.
```

---

## 2. START SESSION (Continuation)

### When to Use:
When continuing from a previous session that ran out of context or was interrupted.

### What it Does:
- Loads Master Context
- References previous session file for immediate continuity
- Provides seamless handoff between sessions

### Prompt:
```
Read the Master Context file and the most recent session file in:
01-ACTIVE-BUSINESS/daily-operations/context-management/session-archives/

I'm continuing from the previous session. Confirm you have context and are ready to pick up where we left off.
```

---

## 3. END SESSION (Capture & Update)

### When to Use:
At the end of every significant work session (document creation, strategic work, problem-solving).

### What it Does:
- Creates comprehensive session capture file
- Proposes additions to Master Context Section 8 (Continuous Improvement Log)
- Documents learnings, decisions, and next steps
- Maintains knowledge continuity for future sessions

### Prompt:
```
Session complete. Please:

1. Create a session capture file in: 01-ACTIVE-BUSINESS/daily-operations/context-management/session-archives/
   - File name: [YYYY-MM-DD-session-topic].md
   - Include: What we worked on, decisions made, files created/modified, key learnings, next steps

2. Propose additions to Master Context Section 8 (Continuous Improvement Log):
   - "Learned Today" entries
   - "Should Add" - missing elements discovered
   - "Should Purge" - obsolete info identified
   - "Should Update" - refinements needed

3. Flag anything critical that should be integrated into core Master Context sections immediately (vs. waiting for monthly review).
```

---

## 4. QUICK SESSION CAPTURE (Tactical Work)

### When to Use:
For shorter, tactical sessions that don't require full strategic documentation (quick edits, minor updates).

### What it Does:
- Creates lightweight session note
- Updates daily log instead of full session file
- Maintains basic continuity without heavy documentation

### Prompt:
```
Quick session wrap-up:
1. Update daily log with today's work
2. List any Master Context updates needed (if any)
3. Note next immediate action
```

---

## 5. MASTER CONTEXT HEALTH CHECK (Monthly Review)

### When to Use:
Monthly or quarterly to keep Master Context lean and current.

### What it Does:
- Reviews Section 8 (Continuous Improvement Log) entries
- Proposes promotions to core sections
- Identifies obsolete content for archiving
- Suggests structural improvements

### Prompt:
```
Perform Master Context health check:

1. Review all entries in Section 8 (Continuous Improvement Log)
2. Propose which items should be:
   - PROMOTED: Integrated into core sections
   - KEPT: Remain in Section 8 for more observation
   - ARCHIVED: Moved to Section 9 (Deprecated) as obsolete

3. Check for:
   - Content that feels stale or outdated
   - Missing context we keep needing
   - Redundant information across sections
   - Structural improvements needed

4. Recommend specific updates to keep Master Context lean and focused (6-8 pages target).
```

---

## 6. EMERGENCY CONTEXT RECOVERY

### When to Use:
When you need to quickly rebuild context after system issues, or when working with an AI that doesn't have session history.

### What it Does:
- Rapid context loading from Master Context + recent sessions
- Gets AI up to speed quickly
- Identifies any critical gaps in understanding

### Prompt:
```
Emergency context recovery needed:

1. Read Master Context file
2. Read the 3 most recent session files in session-archives/
3. Summarize current state, active priorities, and any blockers
4. Confirm you're ready to continue work
5. Flag any context gaps you notice
```

---

## 7. CONTEXT CONFLICT RESOLUTION

### When to Use:
When AI flags contradictions between Master Context and current work, or when you notice Master Context is outdated.

### What it Does:
- Documents the conflict clearly
- Proposes resolution approach
- Updates Master Context with correct information
- Archives outdated info in Section 9 (Deprecated)

### Prompt:
```
Context conflict identified:

Master Context says: [conflicting information]
Current reality is: [actual current state]

Please:
1. Confirm the conflict
2. Propose update to Master Context
3. Archive old information in Section 9 (Deprecated) with explanation
4. Update relevant sections with current information
```

---

## 8. ONBOARD NEW TEAM MEMBER (Future Use)

### When to Use:
When bringing a new team member, consultant, or AI assistant up to speed on Luminous.

### What it Does:
- Provides curated introduction to Luminous context
- Highlights most critical sections of Master Context
- Sets expectations for working style and communication

### Prompt:
```
Onboard new team member to Luminous BioSolutions:

1. Read Master Context file (full read)
2. Provide executive summary covering:
   - What Luminous does (2-3 sentences)
   - Current strategic focus
   - Key messaging framework
   - Tone and communication standards
   - Working preferences
3. Highlight the 5 most critical things they must understand
4. Point to key reference documents in portfolio
```

---

## 9. SESSION HANDOFF (Multi-Person Work)

### When to Use:
When handing off work to another person or AI assistant mid-project.

### What it Does:
- Creates clear handoff documentation
- Documents current state and next steps
- Ensures continuity across team members

### Prompt:
```
Create session handoff for [person/next AI]:

1. Current state: Where we are in the project
2. What we just completed: Summary of today's work
3. Decisions made: Key choices and rationale
4. Next steps: Specific actions needed
5. Context needed: What they should read before continuing
6. Open questions: Anything unresolved or needing decision
```

---

## Continuous Improvement Notes

### Changes Log:
- **2025-10-18:** Initial session management prompts created
- [Future entries as prompts evolve]

### Usage Patterns:
- [Track which prompts get used most frequently]
- [Note which prompts need refinement based on actual use]

### Deprecated Prompts:
- [None yet - will track prompts that stop being useful]
