# PROMPT 2: General Physical Exam Medical Record

**For:** Dr. Tara Dixon - Veterinary Dermatologist (also does general vet work)
**Use case:** Wellness exams, pre-surgical assessments, general medicine cases
**Time target:** 20-30 min → 8-10 min (input 3 min + review 5-7 min)
**Based on:** Records 1, 8, 12 (general cases with full system-by-system PE)

---

## THE PROMPT (Copy everything below this line into AI)

```markdown
I'm a veterinarian (Dr. Tara Dixon, DVM) in Alberta, Canada, documenting a general veterinary case with complete physical examination for the medical record in EzyVet.

**Audience:** Other veterinarians (referring vets, future care providers, internal records)

**Goal:** Create a complete, professional medical record documenting physical examination findings, assessment, and plan for general veterinary cases (wellness, pre-surgical, general medicine).

**Tone:** Clinical, concise, technically accurate. Use veterinary abbreviations freely (WNL, NSF, BID, SID, PO, SQ, IM, etc.). Writing for other vets, not clients.

**Format:** EzyVet medical record format with sections: History/Clinical Record → Physical Exam (complete system-by-system) → Assessment → Plan → Prescription (if applicable)

---

## COMMON ABBREVIATIONS I USE:

- WNL = Within Normal Limits
- NSF = No Significant Findings
- BID = Twice daily
- SID = Once daily
- TID = Three times daily
- PO = By mouth (oral)
- SQ = Subcutaneous
- IM = Intramuscular
- IV = Intravenous
- MM = Mucous membranes
- CRT = Capillary refill time
- TPR = Temperature, Pulse, Respiration
- PE = Physical exam
- O = Owner
- ROM = Range of motion
- BCS = Body condition score

---

## INPUT FIELDS (Tara provides these details):

### Patient Information:
- Species:
- Breed:
- Age:
- Sex:
- Weight:

### Reason for Visit / Clinical Notes:
[Why is patient here? Wellness? Pre-surgical? Specific complaint?]

### History (if relevant):
[Any relevant history for this visit]

### Physical Exam Findings (System-by-System):

**Body Condition Score:** [X/5]

**Pain Score:** [X/24 or "Could not be assessed due to..." or "0/24"]

**Hydration:** [MM moist/dry, skin tent normal/delayed, euhydrated/dehydrated]

**Eyes:** [Corneal and conjunctival examination, pupils, PLR, any abnormalities]

**Ears:** [Bilateral findings, discharge, erythema, any abnormalities. Note if dermatology-related issues]

**Nose:** [Nostrils, nasal planum, air passage]

**Oral Cavity:** [Teeth condition, lacerations, foreign material, gingivitis level if notable]

**Respiratory:** [Lung sounds, respiratory rate/effort, tracheal palpation, cough]

**Cardiovascular:** [Heart sounds, rhythm, peripheral pulses, jugular veins]

**Abdomen:** [Palpation findings - soft/firm, masses, organomegaly, pain, fluid]

**Urogenital:** [Any abnormalities, discharge]

**Neurologic:** [Mentation, cranial nerves, gait, proprioception, nystagmus, facial symmetry]

**Musculoskeletal:** [Gait, ROM, muscle mass, any lameness or pain on manipulation, specific findings]

**Lymph Nodes:** [Peripheral lymph nodes - normal or abnormal]

**Integument:** [Haircoat, masses, skin condition, ectoparasites]

### Assessment:
- Primary diagnosis or reason for visit:
- Any problems identified:
- Differential diagnoses (if applicable):

### Plan:
**Owner discussion:**
[What was discussed with owner]

**Diagnostics/Procedures planned or performed:**
[Vaccines, bloodwork, radiographs, etc.]

**Treatment/Medications:**
[Any medications prescribed or administered]

**Recheck/Follow-up:**
[Timeline or "PRN" or "RTC if concerns"]

### Prescriptions (if applicable):
[List medications with dosing]

---

## OUTPUT STRUCTURE (Match Tara's format exactly):

#### Clinical Record / History Record

[Brief statement of reason for visit and any relevant history]

#### Physical Exam

*Body Condition Score*: X/5

*Pain Score*: X/24 [or qualification if unable to assess]

*Hydration*: [MM moist/normal skin tent/euhydrated OR specific findings]

*Eyes*: [Findings - use "Corneal and conjunctival examination is normal. Pupils are isocoric and pupillary light responses are normal." if WNL, otherwise describe abnormalities]

*Ears*: [Findings - use "Bilaterally normal, no discharge, swelling or erythema externally noted. The patient behaviourally seems to hear normally." if WNL, otherwise describe abnormalities including cytology if performed]

*Nose*: [Findings - use "The nostrils and nasal planum are normal and air passage is normal bilaterally." if WNL]

*Oral cavity*: [Findings - use "Teeth are in good health, no lacerations or foreign material noted in the oral cavity" if WNL, otherwise note gingivitis, dental disease, etc.]

*Respiratory*: [Findings - use "Tracheal and lung sounds are normal bilaterally. Normal respiratory rate and effort. Cough cannot be elicited on tracheal palpation." if WNL]

*Cardiovascular*: [Findings - use "Normal heart sounds bilaterally. Rhythm is regular. Peripheral pulses are strong and synchronous. The jugular veins are normal." if WNL]

*Abdomen*: [Findings - use "Soft on palpation, no masses or organomegaly palpated, no pain appreciated on palpation, no fluid wave noted on palpation" if WNL]

*Urogenital*: [Findings - use "No abnormalities noted" if WNL]

*Neurologic*: [Findings - use "Appropriate mentation, normal cranial nerves. Gait is normal. Normal proprioception x4. No evidence of resting nystagmus or strabismus. Normal facial symmetry" if WNL]

*Musculoskeletal*: [Findings - use "Normal gait x 4 and normal ROM. Muscle mass is appropriate" if WNL, otherwise describe specific findings like lameness, pain, atrophy]

*Lymph nodes*: [Findings - use "All peripheral lymph nodes palpate normally" if WNL]

*Integument*: [Findings - use "Haircoat is healthy, no masses noted on exam or reported by owner, skin appears healthy" if WNL, otherwise describe findings]

#### Assessment

[Primary diagnosis or problem list]
[Any secondary findings or differentials]

#### Plan

[Detailed plan including:
- Owner discussion points
- Procedures performed or planned
- Medications administered or prescribed
- Follow-up timeline]

#### Prescription (if applicable)

**Prescribed By:** Dr. Tara Dixon

[For each medication:]
X x [Medication Name] [Strength]

[DOSING INSTRUCTIONS IN CAPS]. EXP: [MM/YYYY]

---

## EXAMPLE OUTPUT 1 (Based on Record 12 - Lameness case):

#### Clinical Record

Limping on RF started mid Sunday, holding leg up when not using it. if limping has stopped before appointment wont bring it.

#### Physical Exam

*Body Condition Score*: 3.5/5

*Hydration*: MM moist, normal skin tent, assessed hydration - euhydrated

*Eyes*: Corneal and conjunctival examination is normal. Pupils are isocoric and pupillary light responses are normal.

*Ears*: Bilaterally normal, no discharge, swelling or erythema externally noted. The patient behaviourally seems to hear normally.

*Nose*: The nostrils and nasal planum are normal and air passage is normal bilaterally.

*Oral cavity*: **mild gingivitis on back molars,** no lacerations or foreign material noted in the oral cavity

*Respiratory*: Tracheal and lung sounds are normal bilaterally. Normal respiratory rate and effort. Cough cannot be elicited on tracheal palpation.

*Cardiovascular*: Normal heart sounds bilaterally. Rhythm is regular. Peripheral pulses are strong and synchronous. The jugular veins are normal.

*Abdomen*: Soft on palpation, no masses or organomegaly palpated, no pain appreciated on palpation, no fluid wave noted on palpation

*Urogenital*: No abnormalities noted

*Neurologic*: Appropriate mentation, normal cranial nerves. Gait is normal. Normal proprioception x4. No evidence of resting nystagmus or strabismus. Normal facial symmetry

*Musculoskeletal*: Muscle mass is appropriate. **+/- discomfort noted on full extension/flexion of right elbow. Long bones and carpi palpate normally,**

*Lymph nodes*: All peripheral lymph nodes palpate normally

*Integument*: Haircoat is healthy, no masses noted on exam or reported by owner, skin appears healthy

#### Assessment

RF Lameness - suspect traumatic injury/underlying elbow/shoulder OA

Radiographs of forelimbs show bilateral OA in both elbows. Right elbow jt moderately sclerotic, osteophytes present. Long bones normal.

#### Plan

Buprenorphine TGH x 5ds PO
Continue Solensia injs but consider Tramadol if increased pain relief needed for OA pain
Discussed joint supplements - O to consider

#### Prescription

**Prescribed By:** Dr. Tara Dixon

2 x Buprenorphine 0.3mg/mL (per 1.0 mL)

GIVE 0.2ML ORALLY EVERY 12 HOURS FOR 5 DAYS. MAY CAUSE DROWSINESS. EXP: 08/2026

---

## EXAMPLE OUTPUT 2 (Based on Record 8 - Wellness with ear infection found):

#### History Record

**In the event your pet is kept in hospital with us, what is the best number you can be reached at?** 403-352-5537

**History**:
Wellness and vaccines; DHP/Pv, Rabies
O declined Bordetella
Doing well, O has no concerns
Itching a little bit that O has noticed
E/d well
Goes to groomers

#### Physical Exam

*Body Condition Score*: 3/5

*Pain Score*: 0/24

*Hydration*: MM moist, normal skin tent, assessed hydration - euhydrated

*Eyes*: Corneal and conjunctival examination is normal. Pupils are isocoric and pupillary light responses are normal.

*Ears*: **Bilateral erythema, malodorous discharge, pruritus.** The patient behaviourally seems to hear normally. *Cytology: yeast 4+ AU*

*Nose*: The nostrils and nasal planum are normal and air passage is normal bilaterally.

*Oral cavity*: Teeth are in good health, no lacerations or foreign material noted in the oral cavity.

*Respiratory*: Tracheal and lung sounds are normal bilaterally. Normal respiratory rate and effort. Cough cannot be elicited on tracheal palpation.

*Cardiovascular*: Normal heart sounds bilaterally. Rhythm is regular. Peripheral pulses are strong and synchronous. The jugular veins are normal.

*Abdomen*: Soft on palpation, no masses or organomegaly palpated, no pain appreciated on palpation, no fluid wave noted on palpation

*Urogenital*: No abnormalities noted

*Neurologic*: Appropriate mentation, normal cranial nerves. Gait is normal. Normal proprioception x4. No evidence of resting nystagmus or strabismus. Normal facial symmetry

*Musculoskeletal*: Normal gait x 4 and normal ROM. Muscle mass is appropriate

*Lymph nodes*: All peripheral lymph nodes palpate normally

*Integument*: Haircoat is healthy, no masses noted on exam or reported by owner, skin appears healthy

#### Assessment

Bilateral otitis externa - ddx otodectes, food allergy, atopic dermatitis, other
Appears otherwise healthy upon PE today, OK to vaccinate.

#### Plan

**Plan**:
O plans to spay after Spice turns 6 months old
1) DHP/Pv (SQ:RH)
2) Rabies (SQ;Scruff)
3) Strongid PO
4) Microchip administered SQ scruff
5) Mometamax 15g 0.2ml SID AU x 10ds
6) Nexgard 1 tab given in hospital today
7) Recheck ears in 2 weeks

#### Prescription

**Prescribed By:** Dr. Tara Dixon

1 x Nexgard 11.3mg (1.8 - 4.5kg)

GIVE PO IN HOSPITAL EXP: 08/2026

**Prescribed By:** Dr. Tara Dixon

1 x Mometamax 15g

INSTILL 0.2 ML INTO EACH EAR ONCE DAILY FOR 10 DAYS OR UNTIL RECHECK APPOINTMENT. EXP: 10/2026

---

## CRITICAL VERIFICATION CHECKLIST (Tara must verify before pasting into EzyVet):

- [ ] **All exam findings are accurate** (AI only uses what Tara provided, no assumptions)
- [ ] **Abnormal findings are in correct systems** (e.g., ear findings under Ears, not Integument)
- [ ] **"WNL" statements are appropriate** (systems truly normal)
- [ ] **Diagnosis matches exam findings**
- [ ] **Medication dosages are appropriate for patient weight**
- [ ] **Treatment plan makes clinical sense**
- [ ] **Follow-up timeline is appropriate**
- [ ] **No hallucinated information** (AI uses only facts provided)

---

## TIPS FOR EFFICIENT INPUT:

**For "WNL" systems, you can just write:**
- Eyes: WNL
- Ears: WNL
- Cardiovascular: WNL

**AI will expand to full professional language:**
- Eyes: "Corneal and conjunctival examination is normal. Pupils are isocoric and pupillary light responses are normal."

**Only provide detailed input for ABNORMAL findings:**
- Ears: Bilateral erythema, malodorous discharge, cytology shows yeast 4+
- Musculoskeletal: +/- discomfort on RF elbow extension/flexion

**This saves input time while maintaining complete documentation.**

---

## HOW TO USE THIS PROMPT:

### Step 1: Capture Information (3 minutes)
During or after the exam, fill in INPUT FIELDS with:
- Patient info
- Reason for visit
- Exam findings (use "WNL" for normal systems, detail for abnormal)
- Assessment
- Plan

**Format:** Bullets, shorthand, abbreviations are fine. Quick capture.

### Step 2: Generate Draft (30 seconds)
- Copy this entire prompt into AI
- Paste your input details
- Run the prompt

### Step 3: Review and Refine (5-7 minutes)
- Verify exam findings are accurate
- Check that abnormal findings are properly described
- Verify medications and dosages
- Add any patient-specific details AI might have missed

### Step 4: Copy into EzyVet (30 seconds)
- Copy final version
- Paste into EzyVet record
- Sign

**Total time: ~8-10 minutes vs. 20-30 minutes writing from scratch**

---

## NOTES FOR REFINEMENT:

**After using 3-5 times, track:**
- What do you edit every time? → Add to prompt
- What does AI get wrong? → Add constraints
- What takes longest to review? → Simplify that section

**This prompt improves with use. Version 1.0 = 80% accurate. Version 2.0 = 90% accurate.**

---

**END OF PROMPT**
```

---

## USAGE INSTRUCTIONS FOR TARA:

1. Save this file somewhere accessible
2. For general vet cases (wellness, pre-surgical, general medicine), open this file
3. Fill in INPUT FIELDS (3 min) - use "WNL" for normal systems
4. Copy entire prompt + inputs into AI
5. Review/edit output (5-7 min)
6. Paste into EzyVet

**Target: 8-10 minutes instead of 20-30 minutes**

---

## WHEN TO USE WHICH PROMPT:

**Use Prompt 1 (New Derm Case):** Dermatology-focused exam, referred derm cases, initial derm workups

**Use Prompt 2 (General PE):** Wellness exams, pre-surgical assessments, general medicine, non-dermatology cases

**Key difference:** Prompt 1 = focused derm exam. Prompt 2 = complete system-by-system exam.
