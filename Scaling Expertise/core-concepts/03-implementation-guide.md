---
tags: [core-concepts, implementation, how-to]
created: 2025-10-19
---


# How to Actually Do This: Five-Step Implementation

The framework is universal. The implementation is domain-specific. Here's how to start.


## Step One: Pick Your Bottleneck

Identify the one repetitive task where you spend hours translating expertise into deliverables.


### Common Candidates

**Legal:** Discovery responses, client letters, contract summaries

**Medical:** Patient documentation, insurance letters, treatment plans

**Trades:** Estimates and change orders, project proposals

**Ecommerce:** Product descriptions, customer service responses

**Real estate:** Listings and CMAs, market analysis reports

**Engineering:** Design docs and RFCs, technical specifications

**Consulting:** Client reports and proposals, executive summaries


### Selection Criteria

Choose the task you do weekly that:

1. Takes 2+ hours to document
2. Takes under 30 minutes to think through
3. Doesn't require your highest-level expertise to document
4. Has a clear audience and format
5. Would free significant time if automated

**Pro tip:** Start with something you do at least weekly. The ROI compounds faster with frequent tasks.


## Step Two: Learn the Context Formula

AI needs four things to produce professional output: your role, your audience, your goal, and your constraints.


### The Template

```
I'm a [ROLE] [creating/writing/drafting] a [DELIVERABLE].

Audience: [WHO READS THIS AND WHY]

Goal: [WHAT YOU'RE TRYING TO ACCOMPLISH]

Constraints: [TONE, FORMAT, LENGTH, SPECIAL REQUIREMENTS]

[YOUR RAW EXPERTISE/INPUTS]

[OUTPUT STRUCTURE SPECIFICATION]
```


### Examples by Domain

**Family law attorney:**

```
I'm a family law attorney drafting a response to discovery interrogatories.

Audience: Opposing counsel and potentially a judge

Goal: Answer these questions while protecting privilege and avoiding unnecessary admissions

Constraints: Tone should be formal and cautious. Use proper legal citation format.

[Notes on each interrogatory - what to admit, deny, object to, and why]

Structure: Standard interrogatory response format with objections listed first, then substantive responses.
```

**Family physician:**

```
I'm a family physician documenting a patient visit.

Audience: Insurance company and future care providers

Goal: Complete SOAP note that meets insurance requirements

Constraints: Clinically accurate, follows SOAP format, insurance-friendly language

Patient: 45-year-old with Type 2 diabetes, follow-up visit

[Visit notes - complaints, findings, assessment, plan]

Structure: Standard SOAP format with relevant ICD-10 codes.
```

**General contractor:**

```
I'm a general contractor writing an estimate for a kitchen remodel.

Audience: Homeowner who is price-sensitive but values quality

Goal: Explain why certain choices—structural work, permits, quality materials—are necessary investments, not upsells

Constraints: Educational and reassuring tone, not salesy. Address cost concerns directly.

[Job assessment - scope, structural issues, code requirements, material recommendations]

Structure: Project overview, scope of work, why this approach, investment/timeline, payment terms.
```


### Why This Formula Works

Each element serves a purpose:

**Role** → Sets expertise level and perspective

**Audience** → Shapes tone, technical level, what to emphasize

**Goal** → Defines success criteria for the document

**Constraints** → Prevents common AI mistakes (too long, wrong tone, etc.)

**Raw expertise** → Your actual knowledge in fastest format

**Structure** → Ensures professional format


## Step Three: Use the Iteration Pattern

Professional output rarely comes from one prompt. Think of this as a conversation, not a command.


### The Process

1. **Generate first draft** with your initial prompt
2. **Review output** - what's right, what's wrong, what's missing
3. **Refine with specific instructions:**
   - "Make the second paragraph more specific about timeline"
   - "This sounds too salesy, make it more educational"
   - "Include a line about code compliance requirements"
   - "Shorten this by 20% without losing key points"
4. **Repeat** until you hit the 80% threshold
5. **Apply your expertise** to the final 20%


### Common Refinement Patterns

**Too generic?** → "Add specific details about [X], reference the client's situation with [Y]"

**Wrong tone?** → "Make this more [reassuring/technical/direct]. Less [salesy/casual/formal]."

**Too long?** → "Cut this to [X] words. Keep [these key points], remove [generic statements]."

**Missing context?** → "Add a section explaining [why this approach] / [what happens if they don't]"

**Too technical/simple?** → "Explain [technical term] in plain language" or "Add more technical detail"


### Speed Tips

- Save common refinements - You'll use the same ones repeatedly
- Create templates - Standard structures for your frequent documents
- Batch similar tasks - Do all estimates at once, all reports at once
- Time-box iteration - Don't chase perfection, chase "good enough to review"


## Step Four: Know What to Verify

Every domain has critical elements that you must check yourself. AI can draft, but you're still the professional.


### Universal Verification Items

- Factual accuracy for this specific case/client
- Professional judgment decisions are correct
- Numbers, dates, names are accurate
- Tone is appropriate for this relationship
- Nothing confidential or privileged is exposed


### Domain-Specific Checks

**Legal work:**

- Privilege issues—nothing protected revealed
- Jurisdiction-specific rules followed
- Case citations are real and relevant
- Strategy decisions align with client interests

**Medical work:**

- Diagnosis accuracy
- Treatment appropriateness for this patient
- Drug interactions and dosages
- Patient-specific history considered

**Trades:**

- Code compliance for this jurisdiction
- Safety requirements included
- Pricing matches your actual costs/margins
- Site-specific conditions addressed

**Engineering:**

- Technical accuracy
- Security implications considered
- Performance claims realistic
- Operational concerns addressed


### Creating Your Checklist

1. Track what you fix - Note what you change in the first 10 outputs
2. Identify patterns - What do you always need to adjust?
3. Build your list - Create a checklist of must-verify items
4. Refine your prompt - If you're always fixing the same thing, add it as a constraint
5. Update regularly - Add new items as you discover them


## Step Five: Start Small, Then Scale

Don't try to automate everything at once. Build confidence with one workflow.


### Week 1-2: Single Task, Low Stakes

- Choose one deliverable type you do frequently
- Use AI for 3-5 examples this week
- Track time: Before vs. after for each one
- Note issues: What needs adjustment?
- Refine prompt: Improve based on learnings

**Example:** HVAC contractor uses AI for estimates only. Completes 10 estimates in week 1-2. Notes that AI always needs pricing adjusted and timeline clarified. Updates prompt.


### Week 3-4: Expand Volume

- Use refined prompt for all instances of this task
- Track metrics: Time saved, quality level, iteration count
- Build confidence: Is output consistently good?
- Calculate ROI: Hours saved × hourly value

**Example:** HVAC contractor now does all estimates with AI. Time per estimate drops from 2.5 hours to 25 minutes. Completes 20 estimates per week instead of 5.


### Month 2: Add Second Task

- Choose next bottleneck from your list
- Apply learnings from first task
- Build second prompt using same framework
- Run same process: Small test, refine, scale


### Month 3: Optimize and Compound

- Refine both workflows based on cumulative learning
- Measure total impact: Hours saved per week/month
- Reinvest time: More clients? Better service? Life balance?
- Plan next automation if applicable


### Scaling Decision Tree

After 2-3 months, decide:

**Option A: Take on more volume** → More clients, more projects, higher revenue

**Option B: Improve quality** → Better deliverables, happier clients, higher retention

**Option C: Reclaim time** → Leave on time, reduce stress, better life balance

**Option D: Some combination** → 50% more volume + leave 1 hour earlier

All are valid. You choose based on your goals.


## Measuring Success

Track these metrics for the first 3 months:

**Time Metrics:**

- Time per deliverable (before vs. after)
- Total documentation time per week
- Hours freed up per week

**Volume Metrics:**

- Deliverables completed per week (before vs. after)
- Capacity increase (clients/projects/cases)
- Response time improvement

**Quality Metrics:**

- Revision rate (how often you need to redo)
- Client/stakeholder feedback
- Error rate in final deliverables

**Business Impact:**

- Revenue change (if taking more volume)
- Client retention (if improving quality)
- Stress/workload (if reclaiming time)
