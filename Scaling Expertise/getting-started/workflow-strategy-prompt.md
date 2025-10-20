---
tags: [meta-prompt, implementation, workflow-design]
created: 2025-10-19
---
# Workflow Strategy Prompt

## Purpose

After building a prompt, use this to design the complete workflow for scaling your expertise. This turns a prompt into a systematic process.

## When to Use This

- You have a working prompt and want to implement it systematically
- You need to train someone else on the workflow
- You want to optimize the iteration and review process
- You're planning how this fits into your existing work

## The Strategy Prompt

```markdown
I need help designing an implementation workflow for scaling [ROLE] expertise using AI.

Context:
[Brief description of the role and what you're automating]

Current Bottleneck:
[The specific task you're addressing]

Prompt Created:
[Paste or link to the prompt you built]

Help me design:

## 1. Input Workflow

How should I capture my expertise for each case?

Consider:
- When in my process do I have the information needed?
- What's the fastest capture method? (voice notes, bullet points, photos, etc.)
- What's the minimum information the AI needs?
- What can I capture during the work vs. after?

Recommend:
- Optimal capture moment in my workflow
- Best capture method for this role
- Template/checklist for inputs

## 2. Iteration Pattern

How should I refine outputs efficiently?

Consider:
- What typically needs adjustment? (tone, length, technical detail, etc.)
- Common patterns in my revisions
- How many iterations until acceptable?

Recommend:
- Pre-built refinement prompts for common adjustments
- Checklist of what to review first
- When to start over vs. iterate

## 3. Verification Checklist

What must I personally verify before sending?

Based on this domain, create a checklist for:
- Technical accuracy items
- Compliance/legal requirements
- Professional judgment points
- Client-specific details
- Safety or risk items

## 4. Time Allocation

How should I budget time for this workflow?

Estimate:
- Input capture: X minutes
- Initial AI generation: X minutes (including wait time)
- Review and iteration: X minutes
- Final verification: X minutes
- Total time vs. old workflow time

## 5. Integration Points

How does this fit my existing workflow?

Consider:
- What triggers the need for this deliverable?
- What tools/systems am I already using?
- Who else touches this process?
- What happens with the output?

Recommend:
- Where this fits in my current process
- Any tools/templates to prepare in advance
- Handoff procedures if applicable

## 6. Scaling Plan

How do I ramp from first test to full implementation?

Create a 4-week plan:
- Week 1: Test with how many cases? What to learn?
- Week 2: Refine based on learnings, expand volume
- Week 3: Full implementation on this task type
- Week 4: Measure impact, identify next automation opportunity

## 7. Quality Metrics

How do I know this is working?

Define:
- Time savings per deliverable
- Quality indicators (client feedback, revision rate, accuracy)
- Volume increase capacity
- Stress/workload reduction indicators
```


## Example Output Structure

When you run this prompt, the AI will provide:

**1. Input Workflow Design**

"After the exam, while the client checks out, spend 3 minutes recording voice notes: diagnosis, key findings, treatment protocol, prognosis. Include any photo references."

**2. Iteration Pattern**

"Common adjustments:
- First review: Check technical accuracy and add pricing
- Second review: Adjust tone if too clinical or too casual
- Third review: Verify timeline expectations are realistic"

**3. Verification Checklist**

- [ ] Drug names, dosages, and frequencies correct
- [ ] Prognosis is realistic
- [ ] Cost estimate matches your pricing
- [ ] Follow-up timeline specified
- [ ] Home care instructions are safe and clear

**4. Time Allocation**

- Input capture: 3 min
- AI generation: 2 min
- Review iteration: 8 min
- Final verification: 5 min
- **Total: 18 minutes vs. 60 minutes previously = 3.3x faster**

**5. Integration Points**

"Capture notes right after exam while client is checking out. Have your prompt ready on a second monitor. Generate while doing final exam room cleanup."

**6. Scaling Plan**

- Week 1: Use for 3 complex cases, note adjustments needed
- Week 2: Refine prompt, use for 6-8 cases
- Week 3: Use for all new cases requiring treatment plans
- Week 4: Measure time savings, plan to expand to referral letters

**7. Quality Metrics**

- Treatment plan completion time drops to 15-20 minutes
- Client comprehension improves (fewer follow-up calls)
- Can handle 2-3 more cases per day
- Leave clinic on time


## Optimizing Over Time

After 2-4 weeks of using the workflow:

**What to Track:**

- Which parts of the prompt consistently need editing
- What verification catches most often
- Where you're spending review time
- Patterns in iterations

**Common Optimizations:**

- Tighten the prompt - Add common constraints you keep adding manually
- Expand verification checklist - Add items you kept catching
- Batch processing - Can you generate multiple at once?
- Pre-built variations - Create sub-prompts for common case types
