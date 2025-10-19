---
tags: [prompts, healthcare, medical, veterinary]
created: 2025-10-19
---


# Healthcare Prompts

These prompts help healthcare professionals scale their clinical documentation.

**Critical:** Always verify clinical accuracy, patient safety, and treatment appropriateness. **Use HIPAA-compliant systems only.**


## Family Physician - SOAP Notes

**Use case:** Patient visit documentation for medical records and insurance.

```markdown
I'm a family physician documenting a patient visit. This needs SOAP note format for insurance purposes.

Patient Information:
[Age, gender, relevant medical history]

Chief Complaint:
[Why they came in today]

Subjective Notes:
[Patient's description of symptoms, timeline, what makes it better/worse]

Objective Findings:
[Vitals, exam findings, test results]

Assessment:
[Your diagnosis or differential]

Plan:
[Treatment, prescriptions, follow-up, patient education provided]

Make this complete and insurance-friendly while staying clinically accurate. Include relevant ICD-10 codes.

Tone: clinical, precise, thorough.

Structure: standard SOAP format.
```

**What you own:** Diagnosis, treatment decisions, clinical judgment, patient safety, prescription decisions

**What AI handles:** SOAP format structure, insurance-friendly language, complete documentation

**Critical verification:**

- [ ] Diagnosis clinically accurate
- [ ] Treatment appropriate for this patient
- [ ] Drug interactions checked
- [ ] Dosages correct
- [ ] Patient-specific history accurate
- [ ] ICD-10 codes appropriate

**Important:** Use HIPAA-compliant AI systems only.

---


## Dentist - Treatment Plan Letter

**Use case:** Treatment plan explanations for patients.

```markdown
I'm a dentist writing a treatment plan letter to a patient.

Patient Situation:
[Current oral health status]

Issues Identified:
[Cavities, gum disease, other problems and their severity]

Recommended Treatment Sequence:
[What needs to happen, in what order, and why]

What Happens If Untreated:
[Consequences of delaying care]

Investment and Options:
[Cost, insurance coverage, payment plans if applicable]

Explain the sequence and why each step matters. Address cost concerns by explaining outcomes.

Tone: caring, educational, not judgmental.

Structure: current situation, recommended treatment with rationale, timeline, investment, next steps.
```

**What you own:** Clinical diagnosis, treatment planning, timeline recommendations

**What AI handles:** Patient education, treatment sequence explanation, accessible language

**Critical verification:**

- [ ] Treatment plan clinically appropriate
- [ ] Sequence makes clinical sense
- [ ] Costs match your pricing
- [ ] Insurance information accurate
- [ ] Timeline realistic

---


## Veterinarian - Surgery Recommendation

**Use case:** Surgery recommendation letters for pet owners.

```markdown
I'm a veterinarian writing a surgery recommendation letter for a pet owner.

Pet Information:
[Species, breed, age, relevant history]

Diagnosis:
[What's wrong, how you diagnosed it]

Recommended Treatment:
[Surgery type, why you recommend it over alternatives]

Recovery Timeline:
[What to expect post-surgery, restrictions, follow-up]

Prognosis:
[Expected outcome with vs. without surgery]

Investment:
[Cost range, what's included]

Explain this honestly including risks. Address cost concerns by explaining long-term outcomes.

Tone: compassionate, thorough, realistic.

Structure: diagnosis, recommendation with rationale, recovery, prognosis, alternatives, investment.
```

**What you own:** Medical diagnosis, surgical recommendation, risk assessment, prognosis

**What AI handles:** Client communication, accessible medical explanation, cost discussion framework

**Critical verification:**

- [ ] Diagnosis accurate
- [ ] Surgical recommendation appropriate
- [ ] Risks explained honestly
- [ ] Prognosis realistic
- [ ] Cost estimate matches your pricing
- [ ] Alternative options presented fairly

**Extension for Dermatology Specialist:**

For veterinary dermatologists creating treatment plans for chronic skin conditions:

**Adapt this prompt by:**

- Adding photo documentation section
- Emphasizing ongoing management vs. one-time procedure
- Including detailed home care instructions
- Addressing medication schedules and follow-up timelines
- Creating separate versions for pet owners vs. referring veterinarians

See the [[skill-analysis-prompt]] and [[reference-review-prompt]] for complete example of building a veterinary dermatology automation.
