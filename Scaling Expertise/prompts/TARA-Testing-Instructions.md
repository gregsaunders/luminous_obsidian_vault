# Testing Instructions: Tara's Medical Record Prompts

**Created:** January 21, 2025
**Prompts built:**
1. New Dermatology Case Record
2. General Physical Exam Record

**Goal:** Test both prompts with real cases, refine based on Tara's edits, deploy when 80%+ accurate

---

## TESTING WORKFLOW

### Phase 1: Initial Test (This Week)

**For EACH prompt, we need 1 test case:**

#### Test Case 1: New Dermatology Case
**What we need from Tara:**
- Details of ONE recent dermatology case (not from the samples)
- Preferably a case she hasn't written up yet, OR
- A case where she can compare AI output to what she actually wrote

**Tara provides:**
- Patient info (species, breed, age, sex, weight)
- Presenting complaint
- History (duration, previous treatments, areas affected, etc.)
- Exam findings (ears, skin, cytology results)
- Diagnosis
- Treatment plan she prescribed
- Medications prescribed

**Time from Tara: 5 minutes to provide details**

#### Test Case 2: General Physical Exam
**What we need from Tara:**
- Details of ONE recent general case (wellness, pre-surgical, or general medicine)
- NOT a dermatology case

**Tara provides:**
- Patient info
- Reason for visit
- System-by-system exam findings (can use "WNL" for normal systems)
- Assessment
- Plan
- Medications (if any)

**Time from Tara: 5 minutes to provide details**

---

### Phase 2: Generate & Review (Same Day)

**What happens:**
1. Jeff sends test case details to Claude (me)
2. I run each case through the appropriate prompt
3. I send AI-generated output back to Jeff
4. Jeff forwards to Tara for review

**What Tara does:**
1. Read the AI-generated record
2. Edit it as if preparing to paste into EzyVet
3. **Track ALL edits** - what she changed and why
4. Send edited version back with notes

**Questions for Tara to answer:**
- What did you change?
- What was wrong or missing?
- What was surprisingly good?
- How long did it take you to review and edit?
- Would you use this in real workflow?

**Time from Tara: 10-15 minutes per prompt** (review, edit, provide feedback)

---

### Phase 3: Refine Prompts (Next Day)

**What Jeff + Claude do:**
1. Review Tara's edits
2. Identify patterns:
   - What did she change every time?
   - What did AI get wrong?
   - What did AI miss?
3. Update prompts to address these issues
4. Document changes in prompt version notes

**Time: 30-60 minutes (Jeff + Claude)**

---

### Phase 4: Second Round Testing (End of Week)

**Repeat with 2-3 more cases per prompt:**
- Use refined prompts
- Track if edits are decreasing
- Measure: Time to review, number of changes, accuracy improvement

**Goal: 80-90% accuracy by end of second round**

---

## SUCCESS METRICS

### Accuracy
**Track for each test case:**
- % of output that's usable without editing
- Number of factual errors (should be ZERO - AI shouldn't hallucinate)
- Number of style/tone edits needed
- Number of missing elements

**Target: 80%+ accurate (meaning Tara edits <20% of content)**

### Time Savings
**Track for each case:**
- Time to provide input: X minutes
- Time to review/edit AI output: Y minutes
- Total: X + Y minutes
- Compare to: Time to write from scratch (baseline)

**Target:**
- New Derm Case: 30-45 min → 10-12 min (70-75% time savings)
- General PE: 20-30 min → 8-10 min (60-70% time savings)

### Usability
**Ask Tara after each test:**
- Was it faster than writing from scratch? (Yes/No)
- Would you use this in real workflow? (Yes/No)
- What would make this more useful?

**Target: "Yes" to both questions by end of Phase 4**

---

## SAMPLE TEST CASE FORMAT

### Example: What Tara Sends for Derm Case

```
Patient: Max, 5yo M/N Golden Retriever, 32kg

Presenting complaint: Chronic itching, recurrent ear infections

History:
- Year-round pruritus affecting face, paws, belly
- Gets ear infections every 2-3 months
- On flea prevention (Nexgard)
- Fed Purina Pro Plan Chicken
- Has tried Benadryl (didn't help much)
- O wants long-term solution

Exam findings:
Ears: Both ears erythematous, malodorous discharge
  Cytology: cocci 3+, yeast 2+

Skin: Ventral abdomen and axillae erythematous, lichenified
  Interdigital spaces: erythema, some alopecia from licking
  Cytology: cocci 2+, yeast 1+

Pruritus score: 7/10 in exam room

Diagnosis: Canine atopic dermatitis with secondary bacterial/yeast infections

Plan:
1. Treat infections first
   - Cephalexin 500mg (15mg/kg) 1 tab BID x 4 weeks
   - Ketoconazole 200mg 1.5 tabs SID x 3 weeks
   - Mometamax 0.5ml AU BID x 2 weeks

2. Long-term allergy control
   - Start Apoquel 16mg BID x 14 days then SID
   - Douxo Pyo shampoo 2x weekly x 4 weeks then 1x weekly

3. Recheck in 3-4 weeks

Prescriptions: Cephalexin, Ketoconazole, Mometamax, Apoquel, Douxo Pyo Shampoo
```

**That's it. Bullet points, quick details. Tara doesn't need to format it nicely.**

---

## TESTING SCHEDULE

### Week 1: Initial Testing
- **Monday:** Build prompts (DONE)
- **Tuesday:** Get 2 test cases from Tara (1 derm, 1 general)
- **Wednesday:** Run through prompts, send outputs to Tara
- **Thursday:** Tara reviews, sends back edits
- **Friday:** Refine prompts based on feedback

### Week 2: Expanded Testing
- **Monday-Wednesday:** Tara uses refined prompts for 2-3 real cases each
- **Thursday:** Review results, calculate time savings
- **Friday:** Final refinements, create "Production Version 1.0"

### Week 3: Real-World Deployment
- **Tara uses prompts for ALL applicable cases this week**
- Track adoption rate (does she actually use them?)
- Track time savings
- Gather feedback

### Week 4: Optimization
- Review what she's still editing consistently
- Update prompts to Version 1.1
- Measure total time reclaimed
- Decide: Build next document type (discharge instructions, referral letters)?

---

## REFINEMENT TRACKING TEMPLATE

### Test Case #1: [Type] - [Date]

**AI Output Accuracy:**
- Correct: 85%
- Style/tone edits needed: 10%
- Missing information: 5%
- Factual errors: 0%

**Tara's Edits:**
1. Changed dosage from general to patient-specific (expected)
2. Added detail about owner concern re: cost (AI didn't know this)
3. Adjusted tone in plan section (too clinical, not warm enough)

**Time:**
- Input: 3 min
- Review/edit: 9 min
- Total: 12 min
- Baseline (from scratch): 35 min
- **Savings: 23 min (66%)**

**Tara's Feedback:**
"Pretty good! I just had to adjust dosages and add a bit more about what I told the owner. Way faster than writing from scratch."

**Changes to Make:**
- Add reminder to verify dosages
- Add field for "owner concerns discussed"
- Adjust tone in plan section (more conversational)

---

## RED FLAGS (When to Stop and Reassess)

**Stop testing and reassess if:**
- ❌ Accuracy is <70% after 3 test cases
- ❌ Tara says "This takes longer than writing myself"
- ❌ AI hallucinates clinical information (makes up facts)
- ❌ Tara doesn't trust the output
- ❌ Takes more than 15 min to review/edit

**What to do:**
1. Ask Tara: "What's the biggest problem?"
2. Fix that ONE thing
3. Test again
4. Don't add more features - simplify instead

---

## COMMUNICATION WITH TARA

### Initial Request (for test cases):

"Hi Tara,

I've built the first two medical record prompts based on your samples:
1. New Dermatology Case
2. General Physical Exam

To test them, I need details for 2 recent cases (one of each type). Can you send me:

**Case 1 (Derm):** Patient info, presenting complaint, history, exam findings, diagnosis, treatment plan
**Case 2 (General):** Patient info, reason for visit, system-by-system findings, assessment, plan

Just bullets/shorthand is fine - takes about 5 minutes per case.

I'll run them through the prompts and send you the AI-generated records to review. You tell me what needs changing.

Thanks!"

### After Sending AI Output:

"Hi Tara,

Here are the AI-generated records for the 2 test cases you sent.

Please:
1. Read through each one
2. Edit it like you're preparing to paste into EzyVet
3. Track what you changed and why
4. Let me know:
   - How long did review/editing take?
   - Is this faster than writing from scratch?
   - Would you actually use this?

Thanks for testing!"

---

## NEXT STEPS AFTER SUCCESSFUL TESTING

**If both prompts achieve 80%+ accuracy and Tara says "yes, I'd use these":**

1. **Deploy for real-world use** (Week 3)
2. **Measure actual time savings** over 1 week
3. **Refine** based on real usage patterns
4. **Build next prompt** (Client Discharge Instructions or Referral Letters)
5. **Repeat process** for additional document types

**Target: Month 2, Tara has 3-5 working prompts saving 2-5 hours/week**

---

## FILES CREATED

1. ✅ `TARA-Prompt-1-New-Dermatology-Case.md`
2. ✅ `TARA-Prompt-2-General-Physical-Exam.md`
3. ✅ `TARA-Testing-Instructions.md` (this file)

**Location:** `Scaling Expertise/prompts/`

**Ready to test? Send this file to Jeff, he coordinates with Tara for test cases.**
