---
tags: [meta-prompt, research, prompt-library]
created: 2025-10-19
---


# Reference Review Prompt


## Purpose

Use this to have Claude Code (or any AI) search the prompt library and identify the most relevant examples for building a new automation. This saves you from reading all 27+ prompts manually.


## When to Use This

- You're building a new domain prompt and want relevant examples
- You need inspiration from similar roles
- You want to understand pattern variations across industries
- You're comparing approaches before building


## The Review Prompt

```markdown
I'm building an AI automation prompt for [ROLE/SPECIALTY].

Search the prompt library and identify the 3-5 most relevant existing prompts that would inform this build.

Role/Specialty Details:
[Describe the role, what they do, who they serve]

Key Characteristics:
- Deliverable type: [report, estimate, plan, letter, etc.]
- Audience: [technical/non-technical, client/internal, etc.]
- Tone requirements: [professional, reassuring, technical, etc.]
- Documentation complexity: [simple/complex]

For each relevant prompt identified:

1. **Why it's relevant**
   - What makes this a good reference point

2. **Key elements to borrow**
   - Specific prompt structure, constraints, or approaches

3. **What to adapt**
   - How the domain difference affects the prompt

4. **Verification differences**
   - What this domain checks vs. the reference domain

Then recommend:
- Which prompt to use as the primary template
- What elements from other prompts to incorporate
- What new elements this domain needs that aren't in existing prompts

Available prompt categories to search:
- tech-product-prompts - Engineering, product, technical roles
- sales-marketing-prompts - GTM, customer-facing roles
- finance-legal-prompts - Financial, legal documentation
- healthcare-prompts - Medical, veterinary, healthcare
- trades-home-services-prompts - Contractors, tradespeople
- personal-services-prompts - Service providers, consultants
```


## Example: Veterinary Dermatology Specialist

```markdown
I'm building an AI automation prompt for a Veterinary Dermatology Specialist.

Search the prompt library and identify the 3-5 most relevant existing prompts for this build.

Role/Specialty Details:
Specialty veterinarian focused on diagnosing and treating complex skin conditions, allergies, and dermatological diseases in pets. Creates detailed treatment plans for pet owners and referral letters to general practice vets. Deals with chronic conditions requiring ongoing management.

Key Characteristics:
- Deliverable type: Treatment plans, diagnostic letters, progress reports
- Audience: Pet owners (non-technical, emotionally invested, cost-conscious) and referring vets (technical, wants detail)
- Tone requirements: Compassionate, educational, realistic about outcomes and costs
- Documentation complexity: Complex (clinical findings + owner education + cost justification + photos)
```


### Expected AI Response

**Most Relevant Prompts:**

**1. Veterinarian - Surgery Recommendation** (healthcare-prompts)

*Why it's relevant:*
Same domain (veterinary medicine), similar audience (pet owners), addresses cost concerns, explains medical decisions in accessible language.

*Key elements to borrow:*
- Structure for explaining diagnosis to pet owners
- Tone that's compassionate but realistic about prognosis
- Cost discussion framework
- Recovery/timeline expectations section

*What to adapt:*
- Surgery is one-time event; dermatology often involves chronic management
- Need more emphasis on ongoing protocols vs. one procedure
- Include home care instructions more prominently
- Add photo documentation discussion

*Verification differences:*
- Dermatology checks: drug interactions, allergy testing accuracy, realistic timeline
- Surgery checks: immediate risks, anesthesia protocols

**2. Dentist - Treatment Plan Letter** (healthcare-prompts)

*Why it's relevant:*
Similar multi-phase treatment planning, client education about "why this approach", explaining sequential treatments.

*Key elements to borrow:*
- Structure for treatment sequences ("first we do X, then Y")
- Explaining why cheaper alternatives don't work long-term
- Educational tone without being condescending

**3. Family Physician - SOAP Notes** (healthcare-prompts)

*Why it's relevant:*
Clinical documentation structure, diagnostic process, treatment plans.

*Key elements to borrow:*
- SOAP note structure for internal documentation
- Clinical precision in findings and assessment
- Insurance-friendly language patterns

**4. HVAC Contractor - Estimate** (trades-home-services-prompts)

*Why it's relevant:*
Explaining technical problems to non-technical audience, addressing cost concerns, building trust through education.

*Key elements to borrow:*
- "Here's the problem, here's why, here's the solution" structure
- Cost justification without being defensive
- Reassuring educational tone

**Primary Template Recommendation:**

Use healthcare-prompts Veterinarian as base template - same domain, similar audience.

**Elements to Incorporate:**

- Treatment sequencing structure from Dentist
- Educational tone from HVAC Contractor
- Clinical documentation precision from Family Physician

**New Elements Needed:**

- Photo documentation description (not in base prompts)
- Chronic condition management emphasis (ongoing vs. one-time)
- Multiple audience variations (owner vs. referring vet letters)
- Dermatology-specific verification items


## Using the Results

After getting this analysis:

1. **Open the recommended prompts** - Review the specific examples identified
2. **Note the patterns** - What's consistent across similar domains
3. **Identify gaps** - What this role needs that isn't covered
4. **Build your prompt** - Using [[prompt-builder-guide]] with these insights
5. **Test and iterate** - Start with the closest match, then adapt


## Advanced Usage


### For Complex Roles

If your role has multiple deliverable types:

```markdown
I'm building automations for a [ROLE] who creates three different deliverable types:

1. [Deliverable A] - for [audience X]
2. [Deliverable B] - for [audience Y]
3. [Deliverable C] - for [audience Z]

For each deliverable type, identify the most relevant reference prompts.
```


### For Hybrid Roles

If combining multiple domains:

```markdown
I'm building a prompt for a [ROLE] that combines [Domain A] and [Domain B] responsibilities.

Example: A technical sales engineer who both creates technical documentation AND customer-facing proposals.

Identify relevant prompts from each domain and explain how to merge them effectively.
```
