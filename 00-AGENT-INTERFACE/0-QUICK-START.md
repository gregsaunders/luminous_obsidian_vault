# Agent Interface: Quick Start Guide

**Purpose:** This folder is your "Control Center" for working with the AI Agent.

## 1. How to Start a Session
**Goal:** Align the agent with your business strategy immediately.
*   **Action:** Tell the agent:
    > "Read the `4-Context-Index.md` file and confirm you are ready."
*   **Why:** This loads all your Master Context files (Strategy, Tone, Fundraising) in one shot.

## 2. How to Assign Deep Work (The "Ticket" System)
**Goal:** Assign complex tasks (research, drafting, analysis) without long chats.
*   **Step 1:** Go to `1-New-Tickets/`.
*   **Step 2:** Duplicate `TEMPLATE-Task-Ticket.md`.
*   **Step 3:** Rename it (e.g., `competitor-analysis.md`) and fill in the details.
*   **Step 4:** Tell the agent:
    > "Execute the ticket in `1-New-Tickets/competitor-analysis.md`."

## 3. How to End a Session
**Goal:** Save your progress so the agent "remembers" next time.
*   **Action:** Tell the agent:
    > "Session complete. Create a log in `2-Session-Memory/` using the Session Log template."

## 4. Quick Tools (Templates)
Located in `3-Prompt-Templates/`. Use these for specific recurring checks.
*   **Tone Check:** "Run the `TEMPLATE-Tone-Check.md` on this text."
*   **Conflict Resolution:** "I found a conflict. Use `TEMPLATE-Context-Conflict-Resolution.md` to fix it."
*   **Health Check:** "Run the `TEMPLATE-Master-Context-Health-Check.md`."

## Folder Structure
*   `0-QUICK-START.md` (This file)
*   `1-New-Tickets/` (Your Inbox for Agent tasks)
*   `2-Session-Memory/` (The Agent's Memory)
*   `3-Prompt-Templates/` (Reusable tools)
*   `4-Context-Index.md` (The Map of your Strategy)
