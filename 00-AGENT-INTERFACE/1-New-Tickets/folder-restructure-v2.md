# File System Restructuring Proposal

## The Goal
Simplify the directory structure to reduce cognitive load, eliminate redundancy (e.g., "Where does this file go?"), and ensure the AI has a clear "Master Context" for decision-making.

## 1. The Strategy: "4 Pillars + Archive"
We will consolidate everything into **4 Active Pillars** and **1 Archive**.

### ✅ The 4 Active Pillars
1.  **`00-AGENT-INTERFACE`** (The Brain) - *No changes needed.*
2.  **`01-OPERATIONS`** (The Action) - Daily execution, meetings, outreach.
3.  **`02-STRATEGY`** (The Plan) - Fundraising, partnerships, legal, and **Master Context**.
4.  **`03-PRODUCTS`** (The Output) - Squarehead Foundry, Luminous Services (Proposals, Deliverables).
5.  **`04-KNOWLEDGE`** (The Library) - Technical docs, market research, regulatory specs.

---

## 2. Proposed Changes (The "Clean Up")

### 🗑️ Folders to Deprecate (Move contents -> Then Archive)
These folders create confusion and should be emptied and deleted/archived:
*   `02-COMPANY-ASSETS` (Legacy structure)
*   `03-DEVELOPMENT` (Legacy structure)
*   `Business Development` (Root folder -> Move to `01-OPERATIONS`)
*   `Grant Funding` (Root folder -> Move to `02-STRATEGY`)
*   `Infrastructure` (Root folder -> Move to `04-KNOWLEDGE`)
*   `Journal` (Root folder -> Move to `01-OPERATIONS`)
*   `Market Research` (Root folder -> Move to `04-KNOWLEDGE`)
*   `Meetings` (Root folder -> Move to `01-OPERATIONS`)
*   `Repo Prompt` (Root folder -> Move to `99-ARCHIVE`)

### 📂 The New Tree Structure

```text
/Luminous
├── 00-AGENT-INTERFACE/       (Brain)
│   ├── 4-Context-Index.md    (Updated Map)
│   └── ...
├── 01-OPERATIONS/            (Action)
│   ├── 1-Journal/            (Daily Logs)
│   ├── 2-Business-Dev/       (Prospects, Outreach)
│   └── 3-Meetings/           (Notes by Date/Company)
├── 02-STRATEGY/              (Plan)
│   ├── 0-MASTER-CONTEXT/     (The "Single Source of Truth")
│   ├── 1-Fundraising/        (Investors, Grants, Decks)
│   ├── 2-Partnerships/       (CDL, Associations, Stakeholders)
│   └── 3-Legal/              (Agreements, IP)
├── 03-PRODUCTS/              (Output)
│   ├── 0-Brand-Identity/     (Style Guide, Assets)
│   ├── 1-Luminous-Services/  (Service Offerings, Website Reference)
│   └── 2-Squarehead-Foundry/ (Product Specs, Pilot Proposals)
├── 04-KNOWLEDGE/             (Library)
│   ├── 1-Technical-Docs/     (Internal Papers, NAFC Workshop)
│   ├── 2-Regulatory/         (AER, OSMWSC)
│   └── 3-Market-Research/    (Competitors, Industry Reports)
└── 99-ARCHIVE/               (Old)
    ├── Legacy-Company-Assets/
    ├── Legacy-Development/
    └── ...
```

### 📍 Your Specific Files: Where They Go
Here is the mapping for the items you flagged (Nothing is deleted):

| Source File/Folder | New Destination | Why? |
| :--- | :--- | :--- |
| `02-COMPANY-ASSETS/brand-identity/_STYLE-GUIDE.md` | `03-PRODUCTS/0-Brand-Identity/` | It's a core asset for building products. |
| `02-COMPANY-ASSETS/legal/Agreements` | `02-STRATEGY/3-Legal/Agreements` | Consolidates strict legal docs. |
| `02-COMPANY-ASSETS/marketing/Website-Redesign...` | `03-PRODUCTS/1-Luminous-Services/Website/` | Active reference for the redesign project. |
| `02-COMPANY-ASSETS/presentations/Internal Papers` | `04-KNOWLEDGE/1-Technical-Docs/Internal-Papers/` | Central library for technical reference. |
| `02-COMPANY-ASSETS/stakeholders` | `02-STRATEGY/2-Partnerships/Stakeholders/` | Groups people strategy together. |
| `02-STRATEGY/2-Fundraising/Grants` | *No Change* (`02-STRATEGY/1-Fundraising/`) | Stays in Strategy. |
| `02-STRATEGY/3-Partnerships` | *No Change* (`02-STRATEGY/2-Partnerships/`) | Stays in Strategy. |
| `03-DEVELOPMENT/NAFC Workshop` | `04-KNOWLEDGE/1-Technical-Docs/NAFC-Workshop/` | Technical reference material. |
| `04-KNOWLEDGE` | *No Change* | Stays as the Knowledge Base. |
| `99-ARCHIVE` | *No Change* | Stays as Archive (We only add to it). |

---

## 3. Maintenance Rules (How to Keep it Clean)

1.  **The "Active vs. Static" Rule:**
    *   If you are *working on it this week*, it lives in `01-OPERATIONS` or `03-PRODUCTS`.
    *   If it is *finished reference material*, it moves to `04-KNOWLEDGE` or `99-ARCHIVE`.

2.  **The "One Home" Rule:**
    *   Never duplicate files. If a file applies to multiple places (e.g., a contract for a pilot), put it in `03-PRODUCTS` (Project file) and link to it from `02-STRATEGY` (Legal).

3.  **The "Inbox Zero" Rule for Root:**
    *   Do not create folders in the Root context. The AI should aggressively suggest moving any Root files to `00-AGENT-INTERFACE/1-New-Tickets` or `01-OPERATIONS/1-Journal` during Weekly Cleanup.

---

## 4. Migration Strategy

**Option A: The "AI Turnkey" (Recommended)**
I (Agntigravity) will:
1.  Create the new directory skeleton in `04-KNOWLEDGE` and `01-OPERATIONS`.
2.  Move the files from the identified "Deprecate" folders to their new homes.
3.  Move the "Deprecate" empty folders to `99-ARCHIVE`.
4.  Update `4-Context-Index.md` with the new paths.

**Option B: Manual Control**
You verify this plan, and manually move the files yourself to ensure "mental mapping" of where things are.

**Recommendation:** Let me do Option A. It is tedious work perfect for an agent. I will generate a log of every file moved so you can review it.
