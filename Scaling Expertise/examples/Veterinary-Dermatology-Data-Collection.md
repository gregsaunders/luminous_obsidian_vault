# Veterinary Dermatology - AI Medical Record Automation Data Collection

**Purpose:** Gather the minimum information needed to build AI prompts that generate 98% accurate medical records with minimal editing required.

**Time to complete:** 60-90 minutes total (can be done in multiple sessions)

**For:** Tara (Veterinary Dermatologist)

---

## PART 1: DOCUMENT INVENTORY (15 minutes)

**Instructions:** List every type of document you write regularly. For each, estimate how often and how long.

| Document Type | How Often? | Time to Write | Pain Level (1-10) | Priority to Automate |
|--------------|------------|---------------|-------------------|---------------------|
| Example: Treatment plan for pet owner | 8-12/week | 45 min | 8 | HIGH |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

**Frequency options:** Daily, 2-3x/week, Weekly, 2-3x/month, Monthly, Rarely

**Priority options:** HIGH (automate first), MEDIUM (automate later), LOW (not worth it)

---

## PART 2: WORKFLOW MAPPING (20 minutes)

**Instructions:** For your TOP 3 most painful document types, describe the current process.

### Document Type #1: ____________________

**When do you write this?**
- [ ] During the appointment
- [ ] Immediately after the appointment
- [ ] End of day batch
- [ ] Between appointments
- [ ] At home after hours

**What information do you already have in your head when you start writing?**
(Check all that apply)
- [ ] Diagnosis
- [ ] Diagnostic test results
- [ ] Treatment protocol
- [ ] Medication details (drug names, dosages, frequencies)
- [ ] Prognosis
- [ ] Cost estimate
- [ ] Home care instructions
- [ ] Follow-up timeline
- [ ] Client concerns/questions addressed
- [ ] Other: _______________

**What slows you down when writing this?**
(Check all that apply)
- [ ] Formatting (making it look professional)
- [ ] Finding the right words for client to understand
- [ ] Remembering all the details to include
- [ ] Adjusting tone (not too clinical, not too casual)
- [ ] Looking up medication names/dosages to confirm
- [ ] Including all required compliance language
- [ ] Making it persuasive/educational without being salesy
- [ ] Typing speed
- [ ] Organizing information logically
- [ ] Other: _______________

**Who reads this document?**
- [ ] Pet owner (needs layperson language)
- [ ] Referring veterinarian (wants technical detail)
- [ ] Insurance company (needs specific format/codes)
- [ ] Your medical record/legal documentation
- [ ] Other: _______________

**Current workflow time breakdown:**
- Thinking/deciding what to say: _____ minutes
- Actually writing/typing: _____ minutes
- Formatting/polishing: _____ minutes
- **Total time: _____ minutes**

---

### Document Type #2: ____________________

*(Repeat same questions as above)*

**When do you write this?**
- [ ] During the appointment
- [ ] Immediately after the appointment
- [ ] End of day batch
- [ ] Between appointments
- [ ] At home after hours

**What information do you already have in your head when you start writing?**
- [ ] Diagnosis
- [ ] Diagnostic test results
- [ ] Treatment protocol
- [ ] Medication details
- [ ] Prognosis
- [ ] Cost estimate
- [ ] Home care instructions
- [ ] Follow-up timeline
- [ ] Client concerns addressed
- [ ] Other: _______________

**What slows you down?**
- [ ] Formatting
- [ ] Translation to accessible language
- [ ] Remembering details
- [ ] Tone adjustment
- [ ] Looking up details
- [ ] Compliance language
- [ ] Persuasion/education
- [ ] Typing speed
- [ ] Organization
- [ ] Other: _______________

**Who reads this?**
- [ ] Pet owner
- [ ] Referring veterinarian
- [ ] Insurance company
- [ ] Medical record
- [ ] Other: _______________

**Time breakdown:**
- Thinking: _____ min
- Writing: _____ min
- Formatting: _____ min
- **Total: _____ min**

---

### Document Type #3: ____________________

*(Repeat same questions)*

**When do you write this?**
- [ ] During appointment
- [ ] After appointment
- [ ] End of day
- [ ] Between appointments
- [ ] After hours

**What information do you already have?**
- [ ] Diagnosis
- [ ] Test results
- [ ] Treatment protocol
- [ ] Medications
- [ ] Prognosis
- [ ] Costs
- [ ] Home care
- [ ] Follow-up
- [ ] Client concerns
- [ ] Other: _______________

**What slows you down?**
- [ ] Formatting
- [ ] Language translation
- [ ] Remembering details
- [ ] Tone
- [ ] Looking up info
- [ ] Compliance
- [ ] Persuasion
- [ ] Typing
- [ ] Organization
- [ ] Other: _______________

**Who reads this?**
- [ ] Pet owner
- [ ] Referring vet
- [ ] Insurance
- [ ] Medical record
- [ ] Other: _______________

**Time:**
- Thinking: _____ min
- Writing: _____ min
- Formatting: _____ min
- **Total: _____ min**

---

## PART 3: SAMPLE DOCUMENTS (10 minutes to gather)

**Instructions:** Please provide 3-5 REAL examples of each document type you want to automate. De-identify patient/client information.

**What I need:**
- [ ] 3-5 examples of Document Type #1
- [ ] 3-5 examples of Document Type #2
- [ ] 3-5 examples of Document Type #3

**How to provide:**
- Copy-paste into separate files named: `Sample-TreatmentPlan-01.md`, `Sample-TreatmentPlan-02.md`, etc.
- Or export from EzyVet and provide PDFs/Word docs

**Why we need this:** AI learns your writing style, tone, structure, and what information you always include. This makes output 80% accurate instead of 50% accurate.

---

## PART 4: DOMAIN EXPERTISE MAPPING (30 minutes)

**Instructions:** For your most common conditions, provide the "standard approach" you use. This becomes the AI's knowledge base.

### TOP 10 CONDITIONS YOU TREAT

List your 10 most frequent dermatology conditions:

1. _____________________
2. _____________________
3. _____________________
4. _____________________
5. _____________________
6. _____________________
7. _____________________
8. _____________________
9. _____________________
10. _____________________

---

### CONDITION TEMPLATE (Complete for top 5 conditions)

**Condition:** _____________________ (e.g., Atopic Dermatitis)

**Typical presentation / How it usually presents:**
(1-2 sentences, how you explain it)
- Example: "Chronic itching, usually affecting face, feet, armpits, and belly. Often seasonal at first, becomes year-round."

**Your typical diagnostic workup:**
(Bulleted list of tests/diagnostics you usually run)
- Example:
  - Physical exam + dermatology exam
  - Rule out other causes (flea control, food trial, skin scraping)
  - Intradermal or serum allergy testing
  - May include cytology if secondary infection

**Your standard treatment protocol:**
(What you typically prescribe/recommend)
- Example:
  - Immunotherapy (allergy shots or sublingual drops) - long-term solution
  - Symptom management: Apoquel or Cytopoint for itch control
  - Treat secondary infections if present
  - Bathing protocol with medicated shampoo
  - Home environment modifications

**Common medications you prescribe for this condition:**
(Drug name, typical dosage range, frequency, duration)
- Example:
  - Apoquel: 0.4-0.6 mg/kg PO BID for 14 days, then SID
  - Cytopoint: 2 mg/kg SQ, every 4-8 weeks
  - Cephalexin: 15-30 mg/kg PO BID for 3-4 weeks (if secondary infection)

**Realistic prognosis / What you tell clients to expect:**
(1-2 sentences)
- Example: "This is a lifelong condition we manage, not cure. Most dogs do very well with consistent treatment, but it requires ongoing commitment."

**Key client education points / What you always explain:**
(2-4 bullet points of what clients need to understand)
- Example:
  - This is allergies - like people with hay fever, it's chronic
  - Treatment controls symptoms but doesn't cure
  - Flare-ups can happen; we adjust treatment as needed
  - Compliance with bathing and medication is critical

**Typical follow-up schedule:**
- Example: Recheck in 2-4 weeks, then every 3-6 months once stable

**Estimated investment range:**
- Example: Initial workup: $800-1,500; Ongoing management: $100-300/month

---

**Repeat the above template for your top 5 conditions.**

*(The AI will use this to generate accurate, condition-specific treatment plans)*

---

## PART 5: "ALWAYS INCLUDE" CHECKLISTS (15 minutes)

**Instructions:** For each document type, what MUST always be included? This becomes the AI's checklist.

### For Document Type #1: ____________________

**Required elements (check all that must be in every document):**

- [ ] Patient signalment (species, breed, age, sex, weight)
- [ ] Chief complaint / Reason for visit
- [ ] Diagnosis (medical term)
- [ ] Diagnosis explained in layperson terms
- [ ] Diagnostic tests performed and results
- [ ] Treatment plan overview
- [ ] Specific medications (name, dose, frequency, duration)
- [ ] Home care instructions
- [ ] What to monitor at home
- [ ] When to call/return if problems
- [ ] Prognosis / realistic expectations
- [ ] Follow-up schedule
- [ ] Cost estimate / investment
- [ ] Alternative options considered
- [ ] Risks/side effects to monitor
- [ ] Client questions addressed
- [ ] Consent language (if applicable)
- [ ] VCPR documentation (if applicable)
- [ ] Other: _____________________

**Tone requirements:**
- [ ] Professional but warm
- [ ] Educational, not condescending
- [ ] Empathetic to client concerns
- [ ] Realistic, not overly optimistic
- [ ] Reassuring but honest
- [ ] Other: _____________________

**Format requirements:**
- [ ] Specific length: _______ pages/words
- [ ] Sections/headers required
- [ ] Must fit EzyVet template format
- [ ] Must be printable/email-friendly
- [ ] Other: _____________________

**Compliance/Legal must-haves:**
- [ ] VCPR statement
- [ ] Informed consent language for certain treatments
- [ ] Controlled substance documentation (if applicable)
- [ ] State board requirements: _____________________
- [ ] Other: _____________________

---

### For Document Type #2: ____________________

*(Repeat checklist format above)*

**Required elements:**
- [ ] *(Same list as above, check applicable items)*

**Tone requirements:**
- [ ] *(Adjust based on audience - e.g., referring vet wants technical language)*

**Format requirements:**
- [ ] *(Specific to this document type)*

**Compliance requirements:**
- [ ] *(Specific to this document type)*

---

### For Document Type #3: ____________________

*(Repeat checklist format)*

---

## PART 6: INPUT CAPTURE PREFERENCES (5 minutes)

**Instructions:** How do you prefer to capture information to feed the AI?

**During/after an appointment, what's FASTEST for you?**

**Option A: Voice Notes**
- You record 2-3 minute voice memo with findings
- AI transcribes and structures it
- **Pros:** Fastest input (talk is faster than typing)
- **Cons:** Requires transcription step, may need quiet space

**Option B: Bullet Point Typing**
- You type quick bullets on laptop/tablet
- Just facts, no formatting needed
- **Pros:** Already typed, structured
- **Cons:** Slower than talking if you're not a fast typer

**Option C: Fill-in-the-Blank Template**
- Pre-made form with fields to fill
- Example: "Diagnosis: ___ | Meds: ___ | Prognosis: ___"
- **Pros:** Ensures you don't forget anything
- **Cons:** Can feel rigid/constraining

**Option D: Photos + Brief Captions**
- Take photos, add short voice/text notes
- AI generates documentation from visual + notes
- **Pros:** Great for dermatology (visual specialty)
- **Cons:** Requires photo organization

**Option E: Hybrid**
- Describe your preferred combination

**Your preference (rank 1-5, with 1 = most preferred):**
- Voice notes: _____
- Bullet typing: _____
- Fill-in template: _____
- Photos + captions: _____
- Hybrid: _____ (describe: ___________________)

**Where are you when you need to capture this?**
- [ ] Exam room with client present
- [ ] Exam room after client leaves
- [ ] Office/desk area
- [ ] Between exam rooms
- [ ] At home after hours

**What device are you using?**
- [ ] Desktop computer (clinic)
- [ ] Laptop
- [ ] Tablet (iPad, etc.)
- [ ] Phone
- [ ] Multiple devices

**How much time can you realistically spend on input capture per patient?**
- [ ] 1-2 minutes (need this FAST)
- [ ] 3-5 minutes (reasonable)
- [ ] 5-10 minutes (prefer thoroughness)
- [ ] 10+ minutes (quality over speed)

---

## PART 7: SUCCESS CRITERIA (5 minutes)

**Instructions:** How will we know this is working?

**What does "98% accurate" mean to you?**
(What are the 1-2 things you'll ALWAYS need to edit, vs. what should AI get right?)

Things I expect to always edit manually:
- _____________________
- _____________________

Things AI must get right or it's not trustworthy:
- _____________________
- _____________________
- _____________________

**Time savings goal:**

Current weekly time on medical records: _____ hours

Acceptable weekly time after AI: _____ hours

Time savings goal: _____ hours/week

**Volume goal:**

- [ ] I want to see MORE patients (use saved time for revenue)
- [ ] I want to maintain current volume but leave on time (quality of life)
- [ ] I want BETTER documentation quality (risk reduction, client satisfaction)
- [ ] Combination: _____________________

**Deal-breakers (what would make you stop using this):**
- [ ] Takes longer to edit than to write from scratch
- [ ] Output is too generic/doesn't sound like me
- [ ] Misses critical clinical information
- [ ] Creates compliance/legal risk
- [ ] Too many steps/clicks to use
- [ ] Doesn't integrate with EzyVet
- [ ] Other: _____________________

**Success looks like:**
(Describe in your own words what success looks like 3 months from now)

_____________________________________________________________________________________

_____________________________________________________________________________________

---

## SUBMISSION CHECKLIST

Before sending this back, make sure you've completed:

- [ ] Part 1: Document Inventory (table filled out)
- [ ] Part 2: Workflow Mapping (top 3 document types)
- [ ] Part 3: Gathered 3-5 sample documents for each type
- [ ] Part 4: Domain expertise for top 5 conditions
- [ ] Part 5: "Always Include" checklists for top 3 document types
- [ ] Part 6: Input capture preferences
- [ ] Part 7: Success criteria defined

---

## NOTES / ADDITIONAL CONTEXT

Use this space for anything else that would help us build better prompts:

_____________________________________________________________________________________

_____________________________________________________________________________________

_____________________________________________________________________________________

---

**Next Steps After Submission:**

1. Jeff reviews your responses
2. We build first AI prompt for highest-priority document type
3. You test with 3-5 real cases
4. We refine based on what you edit
5. Scale to full implementation

**Expected timeline:** First working prompt in 3-5 days after receiving this completed form.
