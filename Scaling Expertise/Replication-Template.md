# Scaling Expertise: Replication Template
**How to build AI documentation automation for ANY expertise-based professional**

**Based on:** Veterinary Dermatology case study (Dr. Tara Dixon)
**Framework source:** `Scaling Expertise/core-concepts/`
**Use this template for:** Attorneys, doctors, consultants, contractors, accountants, architects, engineers, or any professional where expertise time << documentation time

---

## The Universal Problem Pattern

**Every expertise-based professional hits this bottleneck:**

1. **Expertise is fast** (diagnosis, decision-making, problem-solving: 15-30 min)
2. **Documentation is slow** (writing, formatting, translating expertise: 30-90 min)
3. **Bottleneck ratio: 2:1 to 6:1** (documentation takes 2-6x longer than expertise)

**Result:** Professional works unpaid hours documenting expertise, or turns down work because documentation doesn't scale.

**Solution:** AI handles the 80% (structure, translation, formatting), professional handles the 20% (expertise, judgment, verification).

---

## The 5 Design Principles (Non-Negotiable)

### 1. Keep It Simple
- No complex tools, integrations, or workflows
- 3-step process: Input → AI generates → Professional refines
- Copy-paste is fine if it saves 70% of the time

### 2. Mirror Existing Workflow
- Don't redesign how they work
- Slot AI into the gap between expertise and documentation
- They keep using their existing tools (practice management software, Word, etc.)

### 3. Match Their Expertise
- AI must sound like THEM, not generic/textbook
- Requires domain-specific context (their protocols, terminology, structure)
- 5-10 sample documents are critical to capture their voice

### 4. Absolutely Simple to Use
- If it takes more than 3 steps, they won't use it
- No new software to learn
- No APIs, no integrations (at least initially)

### 5. Professional Maintains Control
- They ALWAYS review and approve output
- AI is a "junior associate" that drafts, professional verifies
- Quality control lives with the professional

---

## 7-Step Replication Process

### Step 1: Validate the Bottleneck (15-30 min interview)

**Questions to ask:**

**Time burden:**
- How many hours per week do you spend on documentation/deliverables?
- How much of that is unpaid or after-hours work?
- What percentage of your week is documentation vs. actual expertise work?

**Expertise vs. documentation ratio:**
- How long does it take you to diagnose/decide/solve the problem? (expertise time)
- How long does it take to document that expertise? (writing time)
- Ratio should be 2:1 or higher to be worth automating

**Pain level:**
- On a scale of 1-10, how painful is the documentation burden?
- Do you turn down work because of documentation limits?
- Do you work unpaid hours to keep up with documentation?

**If pain level < 7, or ratio < 2:1, this may not be worth automating.**

---

### Step 2: Collect Sample Documents (Most Critical Step)

**What you need:**
- 5-10 examples of their ACTUAL work (not templates, not examples from the internet)
- Must be real documents they've written
- De-identify client/patient information
- Mix of document types if they write multiple kinds

**Why this matters:**
- AI learns their voice, tone, structure
- Identifies patterns (what they always include, how they organize)
- Reveals domain-specific terminology and abbreviations
- Shows what "good" looks like to them

**How to get samples:**
- "Send me 5-10 recent [reports/letters/records] with names removed"
- "Export from [their software] as PDF or Word"
- "I need to see your actual writing to build prompts that sound like you"

**Red flag:** If they won't provide samples, you can't build accurate prompts. Stop here.

---

### Step 3: Analyze Patterns (1-2 hours)

**Read through samples and document:**

**Structure:**
- What sections do they always include?
- What order? (e.g., History → Findings → Assessment → Plan)
- Bullets vs. paragraphs?
- Headers/formatting?

**Tone:**
- Formal vs. conversational?
- Technical vs. accessible?
- Terse vs. detailed?
- Writing for who? (clients, professionals, courts, insurance, etc.)

**Content:**
- What information is always present?
- What varies case-to-case?
- Common phrases or language patterns?
- Abbreviations or jargon they use?

**Domain expertise:**
- What protocols, procedures, or methodologies appear repeatedly?
- What are their "go-to" recommendations or solutions?
- What do they explain to every client/customer?

**Length:**
- Average word count?
- Range (shortest to longest)?

**Create a summary:** "This professional writes [length] [tone] documents in [structure] format for [audience], always including [X, Y, Z], using [terminology/abbreviations]."

---

### Step 4: Map Document Types by Time Burden (30 min)

**List every type of document they write regularly:**

For each, estimate:
- **Frequency:** Daily, weekly, monthly?
- **Time to write:** X minutes per document
- **Pain level:** 1-10 (how much they hate writing it)
- **Weekly burden:** Frequency × Time = Hours per week

**Prioritize by impact:**
- **Priority 1:** Highest frequency × highest time = most hours saved
- **Priority 2:** High pain level (even if less frequent)
- **Priority 3:** Client-facing (improves service quality)

**Calculate potential ROI:**
- Time to write manually: X min
- Target time with AI: Y min (usually 20-30% of original)
- Savings per document: X - Y
- Weekly savings: (X - Y) × frequency

**Start with the document type that saves the most hours per week.**

---

### Step 5: Build Context File (2-3 hours)

**Use the template:** `Vet-Dermatology-Context-File.md`

**Adapt sections:**

**Header:**
- Professional's name, title, specialty
- Practice/firm/company context
- Purpose of file

**Design Principles:**
- Copy the 5 principles (same for every professional)

**The Problem:**
- Their specific time burden
- Bottleneck ratio
- Target outcome

**Document Types:**
- List in priority order
- Time burden and savings estimate for each

**Writing Style:**
- Structure, tone, length (from your analysis)
- Key elements always included
- Abbreviations/terminology

**Domain Expertise:**
- Common protocols, procedures, methodologies
- Standard recommendations or solutions
- Client education themes (what they always explain)

**Sample References:**
- Link to sample documents
- Categorize by type

**AI Prompt Requirements:**
- What must be included for accuracy
- What professional must always verify
- 80-20 rule (AI does 80%, professional refines 20%)

**Success Metrics:**
- Adoption (do they use it?)
- Time savings per document
- Quality indicators
- Weekly time reclaimed

---

### Step 6: Build Prompts (30-60 min per prompt)

**Use the 4-part formula:**

```markdown
I'm a [ROLE] creating a [DELIVERABLE].

Audience: [WHO READS THIS AND WHY]

Goal: [WHAT YOU'RE TRYING TO ACCOMPLISH]

Constraints: [TONE, FORMAT, LENGTH, REQUIREMENTS]

---

[DOMAIN-SPECIFIC CONTEXT]
- Common protocols/procedures
- Standard terminology
- Required elements

---

## Input Fields:

[List the information professional will provide]

---

## Output Structure:

[Exact format matching their samples]

---

## Example Output:

[Use one of their actual documents as the example]
```

**Customize with:**
- Their structure (from samples)
- Their tone (clinical, formal, conversational, etc.)
- Their domain expertise (protocols, terminology)
- Their required elements (what they always include)
- One of their actual documents as the example

**Test immediately:**
- Get details for 1 real case (not from samples)
- Run through prompt
- Send output to professional
- Ask: "What would you change?"
- Refine prompt based on their edits

---

### Step 7: Deploy & Measure (Ongoing)

**Week 1-2: Testing Phase**
- Professional uses prompt for 3-5 cases
- Track what they edit every time
- Update prompt to address common edits
- Measure time: before vs. after

**Week 3-4: Scaling Phase**
- Professional uses for ALL instances of this document type
- Monitor adoption (are they actually using it?)
- Measure weekly time savings
- Gather feedback

**Month 2: Expand**
- If first prompt is working (80%+ adoption), build second document type
- Repeat testing process
- Track cumulative time savings

**Month 3: Optimize**
- Refine prompts based on usage patterns
- Build remaining document types (if applicable)
- Calculate total ROI
- Decide what to do with reclaimed time (more clients? better service? life balance?)

**Success = They use it every time without you reminding them**

---

## Continuous Improvement (Phase 2+ ONLY)

**⚠️ CRITICAL WARNING: Do NOT add continuous improvement mechanisms until Month 2+**

**Why:** The biggest failure mode is adding optimization tools before the professional has adopted the basic workflow. Get them using it consistently for 30 days FIRST. Then, and only then, add simple continuous improvement mechanisms.

**Rule:** If it requires them to do anything new (new tools, new workflows), you're over-engineering. Stop.

---

### When to Add Continuous Improvement

**Wait until:**
- ✅ They've used the prompt 20+ times
- ✅ Adoption rate is 80%+ (they use it most of the time)
- ✅ They see clear time savings and value
- ✅ Habit is formed (it's now their default workflow)

**Don't add if:**
- ❌ Still in first month of usage
- ❌ Adoption is inconsistent
- ❌ They're still learning the basic workflow
- ❌ It requires new tools or steps

---

### Simple Continuous Improvement Mechanisms (Post-Adoption)

**These are acceptable ONLY if they're simple and optional:**

### 1. Edit Log (Track Common Patterns)

**Purpose:** Identify what the professional consistently changes so you can refine prompts monthly.

**How it works:**
```markdown
## What I Edited This Week (Quick Running Log)

Case 1 (Dermatology recheck):
- Changed: Added specific dosage for patient weight (12kg)
- Changed: Adjusted recheck timeline from 2 weeks to 3 weeks

Case 2 (New allergy case):
- Changed: Added client concern about cost
- Changed: Expanded explanation of food trial requirements

Case 3 (Ear flush procedure):
- Changed: Added detail about bulla flushing technique
- No other changes

Pattern noticed: I always need to verify/adjust dosages for patient weight
```

**Implementation:**
- Professional keeps running note in Google Doc, Notes app, or text file
- Takes 30 seconds per case to jot down what they changed
- You review monthly and refine prompts based on patterns

**Payoff:**
- Prompts improve from 80% → 85% → 90% accurate over time
- Less editing required for professional

**Test:** If they stop logging after 2 weeks, drop it. Not worth the friction.

---

### 2. Domain Knowledge Snippets (Add New Protocols)

**Purpose:** Keep AI current as professional adopts new treatments, procedures, or methodologies.

**How it works:**
```markdown
## New Treatment Protocol (Quick Update)

Medication: Zenrelia (lokivetmab biosimilar)
Use case: Atopic dermatitis (alternative to Cytopoint)
Dosing: 2 mg/kg SQ, every 4-8 weeks
Notes: Works as well as Cytopoint, sometimes better tolerated

→ Add to prompt's medication database
```

**Implementation:**
- When professional adopts a new protocol, they send you 1-2 sentence update
- Takes 2 minutes to write
- You add it to context file and update prompt

**Payoff:**
- AI suggests current treatments, not outdated ones
- Professional doesn't have to manually add new meds to every output

**Frequency:** As needed (maybe 1-2 updates per quarter)

---

### 3. Prompt Version Control (Track What Works)

**Purpose:** Maintain history of prompt improvements so you can roll back if new version is worse.

**How it works:**
```markdown
## Prompt Evolution Log (Maintained by You, Not Professional)

Version 1.0 (Week 1):
- Generic structure based on samples
- Accuracy: ~60% (lots of editing needed)

Version 1.1 (Week 2):
- Added professional's common medications with dosing
- Added cytology reporting format
- Accuracy: ~75%

Version 1.2 (Week 3):
- Refined tone based on edit patterns (less verbose)
- Added recheck timelines by condition
- Accuracy: ~85%

Version 2.0 (Month 2):
- Added new medication (Zenrelia)
- Updated ear flush procedure details
- Current accuracy: ~90%

Next planned update: Add treatment plan templates for top 5 conditions
```

**Implementation:**
- YOU maintain this, not the professional
- Takes 5 minutes when you update a prompt
- Lets you track what improvements actually worked

**Payoff:**
- Can revert to previous version if update makes things worse
- Documents what changes increased accuracy

---

### 4. Quarterly Refinement Session (Optional)

**Purpose:** Structured review of prompt performance and updates.

**How it works:**
- Every 3 months, 30-minute call with professional
- Review: What are you still editing consistently?
- Discuss: Any new protocols, procedures, or patterns?
- Update: Refine prompts based on discussion
- Measure: Time savings, adoption rate, quality

**Implementation:**
- Schedule quarterly (not monthly - too frequent)
- Professional brings list of common edits
- You update prompts live or shortly after

**Payoff:**
- Keeps prompts current without constant updates
- Catches drift (their style evolves, prompts should too)

---

### What NOT to Add (Over-Engineering Red Flags)

**❌ Complex documentation systems:**
- Notion databases with tagging and categories
- Sophisticated knowledge management platforms
- Multi-tool ecosystems

**❌ Automated workflow tracking:**
- API integrations to their practice software
- Real-time dashboards and analytics
- Automated prompt refinement pipelines

**❌ AI training pipelines:**
- Fine-tuning custom models
- RAG (Retrieval-Augmented Generation) systems
- Vector databases for domain knowledge

**❌ New software requirements:**
- "Download this app to log edits"
- "Use this Chrome extension for prompt management"
- "Set up this automation platform"

**Why these fail:** Too much overhead. Professional stops using it.

**The test:** If it requires them to learn a new tool or change their workflow, don't add it.

---

### Continuous Improvement Checklist

**Before adding ANY continuous improvement mechanism, ask:**

- [ ] Has the professional used the basic workflow for 30+ days?
- [ ] Is adoption rate 80%+ (they use it most of the time)?
- [ ] Does this improvement require less than 2 minutes per case?
- [ ] Can they do it in a tool they already use (Notes, Google Docs, email)?
- [ ] If they stop doing it, does the system still work fine?

**If any answer is NO, don't add it yet.**

---

## Common Failure Modes (and How to Avoid Them)

### Failure: Professional stops using it after Week 1
**Causes:**
- Output is too generic (didn't use their samples to match voice)
- Takes too long to edit (prompt needs refinement)
- Workflow is too complex (simplify to 3 steps)
- They don't see time savings (set realistic expectations)

**Fix:** Ask "Why aren't you using it?" and address that specific issue.

### Failure: Output requires as much editing as writing from scratch
**Causes:**
- Prompt lacks domain-specific context (add their protocols, terminology)
- Prompt is too vague (be more specific about structure and content)
- Not using their samples as examples (AI needs to see what "good" looks like)

**Fix:** Refine prompt with their common protocols, use their actual document as example in prompt.

### Failure: Professional doesn't trust the output
**Causes:**
- AI hallucinated clinical/technical information (prompt should flag for verification)
- Output had factual errors (prompt needs constraints: "only use information provided")
- Professional expects 100% accuracy (set expectation: AI drafts 80%, they refine 20%)

**Fix:** Add verification checklist, set 80-20 expectation, never let AI guess facts.

### Failure: Adoption is inconsistent (uses it sometimes, not always)
**Causes:**
- Workflow friction (too many steps, too complicated)
- Faster to write short cases manually (that's fine - use AI for complex cases only)
- Forgot it exists (need to build habit)

**Fix:** Simplify workflow, make it default process, track usage for 30 days to build habit.

### Failure: Added continuous improvement too early
**Causes:**
- Professional still learning basic workflow, can't handle additional steps
- Edit logging feels like extra work before habit is formed
- Optimization tools added before adoption is proven

**Fix:** Remove all continuous improvement mechanisms, get back to basic 3-step workflow, wait until Month 2+ to re-introduce simple improvements.

---

## Time Investment vs. ROI

**Upfront time investment:**
- Step 1 (Validate): 30 min
- Step 2 (Collect samples): 15 min (from professional)
- Step 3 (Analyze): 1-2 hours (your time)
- Step 4 (Map documents): 30 min
- Step 5 (Context file): 2-3 hours (your time)
- Step 6 (Build prompts): 1-2 hours per prompt
- Step 7 (Test & refine): 2-3 iterations, 1-2 hours

**Total: ~8-12 hours of work (mostly your time, ~1 hour from professional)**

**Payback period:**
- If saving 2 hours/week: Payback in 4-6 weeks
- If saving 5 hours/week: Payback in 1.5-2.5 weeks
- **ROI compounds every week after payback**

**Annual ROI (if saving 3 hours/week):**
- 3 hours/week × 50 weeks = 150 hours reclaimed
- At $200/hour professional rate = $30,000 in capacity
- Or: 150 hours of life balance (4 weeks of vacation)

---

## Document Types Across Professions

**This framework has been applied successfully to:**

### Legal
- Discovery responses
- Client letters
- Contract summaries
- Legal memoranda

### Medical
- Patient chart notes (SOAP notes)
- Treatment plans
- Insurance letters
- Referral summaries

### Veterinary
- Medical records (SOAP notes)
- Treatment plans for pet owners
- Referral updates to other vets
- Surgical procedure notes

### Trades/Contracting
- Project estimates
- Change orders
- Inspection reports
- Client proposals

### Consulting
- Client reports
- Executive summaries
- Recommendations decks
- Status updates

### Real Estate
- Listing descriptions
- Market analysis (CMA) narratives
- Client communications
- Offer summaries

### Engineering
- Design documents (RFCs)
- Technical specifications
- Code review summaries
- Architecture decision records

### Accounting/Finance
- Client reports
- Tax strategy letters
- Financial statement narratives
- Audit findings

**Universal pattern:** Expertise time << Documentation time = Automation opportunity

---

## Key Success Factors

**1. Professional commitment:**
- Willing to provide 5-10 sample documents
- Willing to test 3-5 times and provide feedback
- Invests 1-2 hours total over 2-3 weeks

**2. Clear bottleneck:**
- Documentation takes 2x+ longer than expertise
- 2+ hours per week spent on documentation
- Pain level 7+ out of 10

**3. Consistent patterns:**
- Professional has a "style" that can be captured
- Common protocols, procedures, or approaches
- Clear structure to documents

**4. Simple workflow:**
- 3 steps maximum
- No new tools to learn
- Fits into existing process

**5. Iteration mindset:**
- Expect first output to need refinement
- Willing to test 3-5 times before perfect
- Continuous improvement (update prompts as practice evolves)

**6. Patience before optimization:**
- Don't add continuous improvement until Month 2+
- Focus on adoption first, optimization second
- Keep it simple until habit is formed

---

## Implementation Timeline

### Month 1: Deploy & Adopt
**Goal:** They use it every time
**Focus:** Basic 3-step workflow only
**Metrics:** Adoption rate (% of cases where they use it)
**Don't add:** Any continuous improvement mechanisms

### Month 2: Refine & Expand
**Goal:** Improve accuracy, add second document type
**Focus:** Refine first prompt based on edit patterns
**Metrics:** Time savings per document, accuracy improvements
**Can add:** Simple edit logging (if they want to)

### Month 3+: Optimize & Scale
**Goal:** Build remaining document types, fine-tune all prompts
**Focus:** Complete automation of top 3-5 document types
**Metrics:** Total weekly time savings, ROI calculation
**Can add:** Domain knowledge updates, quarterly refinement sessions

---

## Next Steps

1. **Identify professional with documentation bottleneck** (2+ hours/week, pain level 7+)
2. **Collect 5-10 sample documents** (their actual work)
3. **Copy this template** and adapt to their domain
4. **Build context file** using Vet-Dermatology-Context-File.md as model
5. **Create first prompt** for highest-impact document type
6. **Test with 3-5 real cases** and refine
7. **Deploy and measure** adoption and time savings
8. **Wait until Month 2+** before adding any continuous improvement

**Goal:** 70-80% time reduction on documentation, professional gets their life back.

---

## Resources

**Framework documentation:**
- `Scaling Expertise/core-concepts/01-introduction.md` - The expertise scaling problem
- `Scaling Expertise/core-concepts/02-framework-principles.md` - Four principles
- `Scaling Expertise/core-concepts/03-implementation-guide.md` - Five-step implementation
- `Scaling Expertise/core-concepts/04-domain-examples.md` - Cross-industry examples

**Case study:**
- `Scaling Expertise/examples/Vet-Dermatology-Context-File.md` - Complete veterinary dermatology example
- `Scaling Expertise/examples/Vet Record Examples.md` - Sample medical records

**Prompts library:**
- `Scaling Expertise/prompts/healthcare-prompts.md` - Healthcare examples
- Add additional industry prompts as built

---

**This template is a proven system. Follow the steps, don't over-engineer, keep it simple, and any expertise-based professional can reclaim 2-5 hours per week.**
