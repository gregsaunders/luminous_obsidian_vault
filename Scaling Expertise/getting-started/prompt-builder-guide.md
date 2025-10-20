---
tags: [meta-prompt, prompt-building, how-to]
created: 2025-10-19
---


# Prompt Builder Guide

## Purpose

This guide helps you build new domain-specific prompts using the universal framework. Use when you need to create automation for a role not covered in the existing prompt library.

## The Universal Formula

Every effective expertise-scaling prompt has these four elements:

### 1. Your Role

Who you are professionally. This sets context for the AI about expertise level and perspective.

**Example:** "I'm a veterinary dermatologist with 12 years of experience..."

### 2. Your Audience

Who will read this deliverable. This shapes tone, technical level, and what to emphasize.

**Example:** "...writing a treatment plan for a pet owner who's concerned about costs..."

### 3. Your Goal

What you're trying to accomplish with this document.

**Example:** "...to explain a complex diagnostic process and treatment options in accessible language..."

### 4. Your Constraints

Formatting, tone, length, what to include/exclude, special requirements.

**Example:** "...keeping it under 2 pages, reassuring but honest about prognosis, include cost estimates."

## How to Build a New Prompt

### Step 1: Review Similar Prompts

Look at existing prompts in related domains. For a veterinary dermatologist, review:

- Base vet template (in healthcare-prompts)
- Dentist (similar treatment planning structure)
- Family Physician (clinical documentation approach)

### Step 2: Identify Your Specific Bottleneck

Ask yourself: "What takes me hours to write but minutes to know?"

For a vet dermatologist, this might be:

- Detailed skin condition diagnosis letters to referring vets
- Treatment plans for complex allergy cases
- Follow-up progress reports with photo documentation
- Client education materials about chronic conditions

### Step 3: Map the Four Elements

**Role:** Veterinary dermatologist, your experience level, specialty focus

**Audience Options:**

- Pet owners (accessible language, emphasize outcomes and costs)
- Referring veterinarians (technical detail, differential diagnoses)
- Insurance companies (medical necessity justification)

**Goal Examples:**

- Explain diagnosis and treatment plan
- Document progress for referring vet
- Justify medical necessity for insurance
- Educate about ongoing management

**Constraints Examples:**

- Professional but compassionate tone
- Include photos/diagrams descriptions
- Cost-conscious without compromising care
- Evidence-based treatment rationale


### Step 4: Add Your Raw Expertise Section

This is where you'll dump your actual knowledge for each case:

```
Patient Information:
[Species, breed, age, history]

Presenting Complaint:
[What the owner reported, duration]

Clinical Findings:
[Your physical exam, skin scraping results, etc.]

Diagnosis:
[Your professional assessment]

Recommended Treatment Protocol:
[Medications, frequency, duration, follow-up plan]

Prognosis & Expected Timeline:
[Realistic outcomes, when they'll see improvement]
```

### Step 5: Specify Output Format

Tell the AI what structure you want:

"Structure: clinical summary, diagnosis explanation, treatment protocol, home care instructions, follow-up plan, cost estimate."

## Complete Example: Veterinary Dermatologist

```markdown
I'm a veterinary dermatologist writing a comprehensive treatment plan for a pet owner.

Patient Information:
[Species, breed, age, relevant history]

Presenting Complaint:
[Chief complaint, duration, previous treatments tried]

Your Clinical Findings:
[Physical exam findings, diagnostic test results, skin scrapings, cultures, etc.]

Diagnosis:
[Your professional assessment, differential diagnoses considered]

Treatment Protocol:
[Medications, topical treatments, dietary changes, environmental modifications]

Expected Timeline:
[When they should see improvement, follow-up schedule]

Cost Estimate:
[Breakdown of treatment costs, ongoing management expenses]

Write a detailed treatment plan in language a pet owner can understand. Explain the condition, why this treatment approach, what to expect, and how to manage at home. Address cost concerns by explaining long-term value.

Tone: compassionate, educational, realistic about timeline.

Structure: condition explanation, treatment protocol with rationale, home care instructions, expected timeline, cost breakdown, follow-up plan.
```

## Testing Your New Prompt

1. **First test:** Use it with a recent real case. Does it get you 80% there?
2. **Adjust:** Refine based on what was missing or excessive
3. **Second test:** Try a different case type. Does it still work?
4. **Iterate:** Add constraints or examples where AI struggles
5. **Document:** Save the refined version to your prompt library

## Common Issues & Fixes

**Too generic?** → Add more specific constraints about tone, structure, or domain requirements

**AI adds fluff?** → Add constraint: "Be direct and concise. No generic statements."

**Wrong technical level?** → Be more specific about audience expertise level

**Missing key elements?** → Add them to your "Structure:" specification

**Too long?** → Add word/page count constraint
