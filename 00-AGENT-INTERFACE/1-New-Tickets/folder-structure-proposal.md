# Proposal: Luminous File System Redesign

## The Goal
Create a structure that is **logical for humans** (Squarehead Foundry vs. Luminous) and **navigable for AI** (clear context paths).

## The Core Concept: 4 Pillars
We move from a "Folder Dump" to a "Functional Hierarchy".

### 1. `01-OPERATIONS` (The Daily Grind)
*   **Focus:** Execution, Meetings, Outreach, Active Deals.
*   **Changes:**
    *   Rename `01-ACTIVE-BUSINESS` -> `01-OPERATIONS`.
    *   **New:** Create `2-Business-Development` folder.
        *   `Prospects/` (CNRL, Suncor - Active Operator targets).
        *   `Outreach/` (General networking).

### 2. `02-STRATEGY` (The Business Engine)
*   **Focus:** Fundraising, Partnerships, Legal, Master Context.
*   **Changes:**
    *   **New:** Create `2-Fundraising` folder.
        *   `Investors/` (VCs, Angels, Pitch Decks).
        *   `Grants/` (Alberta Innovates, ERA, Non-dilutive).
    *   Move `03-DEVELOPMENT/partnerships` (CDL) to `3-Partnerships`.
    *   **New:** Create `0-MASTER-CONTEXT` folder for the "Source of Truth" files.

### 3. `03-PRODUCTS` (The Offerings)
*   **Focus:** Defining what we sell.
*   **Changes:**
    *   Create `1-Luminous-Services` (Biosensors, Consulting).
    *   Create `2-Squarehead-Foundry` (The Platform - formerly Confluent).
    *   Move `02-COMPANY-ASSETS/strategy-development/operational-intelligence` into `Squarehead-Foundry`.

### 4. `04-KNOWLEDGE` (The Library)
*   **Focus:** Reference material, Regulatory, Technical Docs.
*   **Changes:**
    *   Move `02-COMPANY-ASSETS/technical-docs` here.
    *   Move `02-COMPANY-ASSETS/regulatory` here.

## AI Navigation Strategy
To make this "AI Navigable" without admin burden:

1.  **The Router:** We keep `00-AGENT-INTERFACE/4-Context-Index.md` updated as the absolute map.
2.  **The "Context Link" Block:**
    *   We add a standard block to the bottom of every active project file:
    ```markdown
    ---
    **AI Context:**
    - Strategy: [[MASTER-CONTEXT.md]]
    - Product: [[Squarehead-Foundry-Specs.md]]
    ---
    ```
    *   This uses Obsidian wikilinks `[[]]`, which both you and I can follow.

## Proposed Migration Map

| Current Location | New Location |
| :--- | :--- |
| `01-ACTIVE-BUSINESS/` | `01-OPERATIONS/` |
| `02-COMPANY-ASSETS/fundraising/` | `02-STRATEGY/2-Fundraising/` |
| `03-DEVELOPMENT/partnerships/` | `02-STRATEGY/3-Partnerships/` |
| `02-COMPANY-ASSETS/strategy-development/` | `03-PRODUCTS/2-Squarehead-Foundry/` |
| `02-COMPANY-ASSETS/technical-docs/` | `04-KNOWLEDGE/1-Technical-Docs/` |

## Decision Required
Do you approve this structure? If yes, I will execute the moves and update the Context Index.
