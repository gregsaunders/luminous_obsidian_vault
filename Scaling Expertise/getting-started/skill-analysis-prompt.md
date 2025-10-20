---
tags: [meta-prompt, analysis, bottleneck-identification]
created: 2025-10-19
---
# Skill Analysis Prompt

## Purpose

Use this prompt to analyze any professional role and identify where AI can scale expertise. This is your starting point before building automation.

## When to Use This

- You want to scale a new role not in the prompt library
- You're unsure which tasks should be automated
- You need to articulate the bottleneck to others
- You're consulting with someone about their scaling opportunities

## The Analysis Prompt

```markdown
I need help analyzing the [ROLE] workflow to identify documentation bottlenecks where AI can scale expertise.

Role Description:
[Brief description of the professional role - what they do, who they serve]

Typical Work Activities:
[List the main tasks this role performs daily/weekly]

Current Workflow for Key Deliverables:
[For each major deliverable type, describe:
- How long the thinking/diagnosis takes
- How long the documentation takes
- Who reads the deliverable
- What format it requires]

Help me identify:

1. **The Bottleneck Tasks**
- Which deliverables take hours to write but minutes to know?
- Where is documentation time disproportionate to expertise time?
- What prevents taking on more clients/projects?

2. **The Expertise vs. Translation Ratio**
- For each bottleneck task, what's the ratio of thinking time to writing time?
- What makes the writing slow? (Format complexity? Technical translation? Length?)

3. **What Must Stay Human**
- What requires professional judgment that cannot be delegated?
- What decisions need this person's expertise specifically?
- What quality control must they personally verify?

4. **Quick Wins**
- Which task, if automated first, would have biggest impact?
- What's the simplest prompt to start with?
- What can be tested this week?

Based on the four principles, analyze this role and recommend:
- The #1 bottleneck to automate first
- Draft prompt structure following the 4-part formula (role, audience, goal, constraints)
- What this person should still own vs. what AI handles
- Expected time savings and scaling multiple
```

## Example: Veterinary Dermatologist

```markdown
I need help analyzing a Veterinary Dermatologist's workflow to identify documentation bottlenecks.

Role Description:
Specialty veterinarian focused on diagnosing and treating complex skin conditions, allergies, and dermatological diseases in pets. Sees referred cases from general practice vets and directly from pet owners. Mix of acute issues and chronic condition management.

Typical Work Activities:
- Patient examinations and diagnostic workups (skin scrapings, cultures, biopsies)
- Developing treatment protocols for complex cases
- Follow-up appointments to assess treatment progress
- Communication with referring veterinarians
- Client education about chronic conditions
- Photo documentation of conditions and progress

Current Workflow for Key Deliverables:

**Treatment Plans for Pet Owners:**
- Diagnosis/thinking time: 15-20 minutes during exam
- Documentation time: 45-60 minutes after
- Reader: Pet owner (needs accessible language)
- Format: 2-3 page letter explaining condition, treatment, costs, timeline

**Referral Letters to General Practice Vets:**
- Diagnosis/thinking time: Same as above (already done)
- Documentation time: 30-40 minutes
- Reader: Referring veterinarian (wants technical detail)
- Format: Professional letter with clinical findings, diagnosis, treatment protocol

[Continue with analysis questions...]
```

## What You'll Learn

After running this analysis, you'll have:
1. Clear bottleneck identification
2. Scaling potential (5-20x improvement)
3. Starting point (which prompt to build first)
4. ROI estimate (hours saved per week/month)
5. Implementation priority

## Next Steps

After completing this analysis:
1. Review similar prompts using reference-review-prompt
2. Build your first prompt following prompt-builder-guide
3. Plan implementation using workflow-strategy-prompt
4. Start small - test with one real case before scaling
