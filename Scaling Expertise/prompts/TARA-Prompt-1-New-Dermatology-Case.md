# PROMPT 1: New Dermatology Case Medical Record

**For:** Dr. Tara Dixon - Veterinary Dermatologist
**Use case:** Initial dermatology consultation/workup (referred or direct client)
**Time target:** 30-45 min → 10-12 min (input 3 min + review 7-9 min)
**Based on:** Record 4 (Roxy - atopic dermatitis), Vet-Dermatology-Context-File.md

---

## THE PROMPT (Copy everything below this line into AI)

```markdown
I'm a board-certified veterinary dermatologist (Dr. Tara Dixon, DVM) in Alberta, Canada, documenting a new dermatology case for the medical record in EzyVet.

**Audience:** Other veterinarians (referring vets, future care providers, internal records)

**Goal:** Create a complete, professional dermatology case record documenting initial presentation, findings, diagnosis, and treatment plan.

**Tone:** Clinical, concise, technically accurate. Use veterinary abbreviations freely (WNL, NSF, BID, SID, PO, AU, AD, AS, DDx, etc.). Writing for other vets, not clients.

**Format:** EzyVet medical record format with sections: History Record → Physical Exam (Dermatological Exam) → Assessment → Plan → Prescription

---

## COMMON MEDICATIONS I PRESCRIBE (Reference for AI):

**Allergy/Itch Control:**
- Apoquel: 0.4-0.6 mg/kg PO BID x 14 days, then SID
- Cytopoint: 2 mg/kg SQ, every 4-8 weeks
- Prednisone/Prednisolone: 0.5-1 mg/kg PO SID-BID, then taper
- Atopica (cyclosporine): 5 mg/kg PO SID

**Antibiotics:**
- Cephalexin: 15-30 mg/kg PO BID x 3-4 weeks
- Clavaseptin/Clavamox: 12.5-25 mg/kg PO BID x 2-4 weeks

**Antifungals:**
- Ketoconazole: for Malassezia dermatitis

**Topicals:**
- Douxo S3 Calm Shampoo: bathe 1-2x weekly, 5-10 min contact time
- Douxo S3 Pyo Shampoo: bathe 1-2x weekly, 5-10 min contact time
- Mometamax: ear medication, typical 0.2-1ml per ear SID-BID
- Otic Prep (Baytril/Dexamethasone/TrizEDTA): for bacterial OE
- EpiOtic: ear cleaner

**Prescription Foods:**
- Hill's z/d: hydrolyzed protein, 8-12 week strict elimination trial
- Royal Canin Hydrolyzed Protein
- Novel protein diets (e.g., Canadian Naturals Pork)

---

## INPUT FIELDS (Tara provides these details):

### Patient Information:
- Species:
- Breed:
- Age:
- Sex:
- Weight:

### Reason for Visit:
[Why the patient is here - referred? Owner concern? Specific problem?]

### History:
- Duration of problem:
- Previous treatments tried:
- Response to previous treatments:
- Seasonal or year-round:
- Diet (current food, treats):
- Pruritus score (1-10):
- Areas affected (face, feet, ears, axillae, ventrum, etc.):
- Any other relevant history:

### Dermatological Exam Findings:

**Ears:**
- Left ear (AS):
- Right ear (AD):
- Cytology (if performed):

**Integument/Haircoat:**
- Overall haircoat condition:
- Areas of alopecia, erythema, lichenification, hyperpigmentation:
- Interdigital spaces:
- Cytology (if performed):

**Other relevant findings:**
- Pruritic score observed in exam room:
- Distribution of lesions:

### Assessment:
- Primary diagnosis:
- Differential diagnoses (if applicable):
- Secondary issues (pyoderma, Malassezia, etc.):

### Plan:
**Owner discussion points:**
[What was discussed with owner - diagnosis explanation, treatment rationale, realistic expectations]

**Treatment protocol:**
1. [Medication 1 with dosing]
2. [Medication 2 with dosing]
3. [Topical treatments with instructions]
4. [Diet recommendations if applicable]
5. [Other recommendations]

**Recheck:**
[Timeline - e.g., "2-4 weeks", "recheck PRN", etc.]

### Prescriptions (if applicable):
[List medications being sent home with dosing instructions]

---

## OUTPUT STRUCTURE (Match Tara's EzyVet format exactly):

#### History Record

**Reason For Visit** [Brief statement of presenting complaint]

[Detailed history paragraph including: duration, areas affected, previous treatments, response, seasonality, diet, pruritus level, other relevant information]

#### Physical Exam

##**Dermatological Exam**: Other Body Systems not examined

   *History*: [Concise summary of presenting complaint and relevant history]

   *Ears*: [Findings for each ear. If cytology performed, include: "*Cytology: [organisms and severity, e.g., cocci 3+, yeast 2+]*"]

   *Integument/Haircoat*: [Overall condition, specific findings - alopecia, erythema, lichenification, hyperpigmentation, distribution. If cytology performed, include: "*Cytology: [findings]*"]

   *Pruritic Score*: [X/10 with description - e.g., "8/10 Roxy is scratching excessively in exam room"]

   *Diet*: [Current food, treats, any dietary trials]

   *Diagnosis*: [Primary diagnosis with any qualifiers - e.g., "Canine atopic disease (exacerbated by hormonal changes)"]

   *Plan*: [Detailed plan with numbered items including:
   - Owner discussion/education points
   - Treatment protocol (medications, topicals, diet)
   - Specific instructions (e.g., bathing frequency, contact time)
   - Recheck timeline]

#### Prescription

**Prescribed By:** Dr. Tara Dixon

[For each medication prescribed, format as:]
X x [Medication Name] [Strength]

[DOSING INSTRUCTIONS IN CAPS]. EXP: [MM/YYYY]

[Repeat for each medication/product]

---

## EXAMPLE OUTPUT (Based on Tara's actual record - Record 4):

#### History Record

**Reason For Visit** scratching a lump near the lumbar area of her spine to the point of raw skin, check the ears as having itchy and redness, mainly the right one
**Is your pet currently on any medications?** no
**Does your pet have any known allergies we need to be aware of?** unknown
**Are there any additional problems or concerns you would like addressed?** no
**In the event your pet is kept in hospital with us, what is the best number you can be reached at?** 403-227-3346

#### Physical Exam

##**Dermatological Exam**: Other Body Systems not examined

   *History*: **Starting heat-- began on Saturday. Planning to be bred on this heat cycle.**
Initially looked like dandruff, that progressed into excessive pruritus and hotspots over ~3 months.
Right ear irritation, with noted bumps on the ear
Roxy's skin seems to flare during heat cycles and in the summertime
Many various foods have been trialed with variety of proteins (chicken, beef, salmon)
Gets bathed q2months - Roxy is indoors/outdoors 50/50 in the summer and 80/20 in the winter
Severely pruritic with general hair loss but no alopecic patches
Legs, axillae, chest, tail and sides of body, ears seems the main pruritic areas
They would like to avoid any systemic medications due to pending breeding
Seems pruritic year-round; hasn't paid close attention to her in the winter months to see how signs are then

   *Ears*: Left ear - appears normal. Right ear - medial pinna and ostia mildly erythematous, few crusts present. Lower canal is clear.
*Cytology(Right ear): cocci 3+, waxy debris*

   *Integument/Haircoat*: Haircoat appears full, no alopecic areas but is a bit dry and dull. No scale present.
*Cytology(skin): Cocci 2-3+, no yeast*

   *Pruritic Score*: 8/10 Roxy is scratching excessively in exam room

   *Diet*: Inukshuk kibble with Fortiflora and cod liver oil -- been on this diet for ~5 months; didn't notice any changes in signs with dietary changes
Gets beef bones q4-6wks

   *Diagnosis*: Canine atopic disease (exacerbated by hormonal changes)

   *Plan*: Discussed CAD and how signs can worsen during estrus periods/pregnancy. Went over various options for pruritic control including Apoquel, Cytopoint, steroids, antihistamines and the lack of studies investigating safety during breeding, pregnancy, lactation. Options include treating with systemic medications and discontinuing them 1-2wks before breeding or trialing topical tx only. Os opt for topical tx only. Discussed other options for itch control including atopic diets, topical oil application, etc but safety of these during pregnancy/breeding unknown.
Treatment protocol:
1) Douxo Calm shampoo (for anti itch) bathe 1-2x/week (alternating with Douxo Pyo Shampoo) Allow 5-10 minutes contact time before rinsing in luke warm/cool water
2) Douxo Pyo shampoo (for bacterial/yeast control) bathe 1-2x/week (alternating with Douxo Calm Shampoo) Allow 5-10 minutes contact time before rinsing in luke warm/cool water
3) EpiOtic Otic Cleanser Clean ears EOD x7ds then PRN

#### Prescription

**Prescribed By:** Dr. Tara Dixon

1 x Douxo S3 Calm shampoo 500ml

BATHE 1-2 TIMES WEEKLY FOR ITCH CONTROL. ALTERNATE BETWEEN SHAMPOOS. CAN BE USED MORE FREQUENTLY TO CONTROL ITCH. ALLOW LATHERED SHAMPOO 5-10 MINUTES OF CONTACT TIME BEFORE RINSING OFF IN LUKEWARM WATER. EXP: 04/2026

1 x Douxo S3 Pyo Shampoo 500mL

BATHE 1-2 TIMES WEEKLY FOR ITCH CONTROL. ALTERNATE BETWEEN SHAMPOOS. CAN BE USED MORE FREQUENTLY TO CONTROL ITCH. ALLOW LATHERED SHAMPOO 5-10 MINUTES OF CONTACT TIME BEFORE RINSING OFF IN LUKEWARM WATER. EXP: 06/2026

1 x Epi-Otic Cleanser 8oz

CLEAN EARS EVERY OTHER DAY FOR 1 WEEK, THEN AS NEEDED FOR ALLERGY CONTROL. EXP: 04/2027

---

## CRITICAL VERIFICATION CHECKLIST (Tara must verify before pasting into EzyVet):

- [ ] **Diagnosis is clinically accurate for this patient**
- [ ] **Medication dosages match patient weight** (AI suggests based on protocols, but Tara confirms)
- [ ] **Cytology results are accurate** (organisms, severity - AI only uses what Tara provided)
- [ ] **Treatment plan is appropriate for this specific case**
- [ ] **Owner discussion accurately reflects what was said**
- [ ] **Prognosis/expectations are realistic**
- [ ] **Recheck timeline is appropriate**
- [ ] **Prescription instructions are clear and accurate**
- [ ] **No hallucinated information** (AI only uses facts Tara provided)

---

## DOSAGE VERIFICATION REMINDER:

**AI will suggest dosages based on Tara's typical protocols, but TARA MUST VERIFY for this patient's specific weight.**

Example:
- AI suggests: "Apoquel 0.4-0.6 mg/kg PO BID"
- Tara calculates for 25kg dog: "Apoquel 16mg (1 tablet) PO BID"

**AI provides the protocol. Tara provides the patient-specific dose.**

---

## HOW TO USE THIS PROMPT:

### Step 1: Capture Information (3 minutes)
After the exam, fill in the INPUT FIELDS above with:
- Patient info
- History details
- Exam findings (ears, skin, cytology results)
- Your diagnosis
- Your treatment plan

**Format:** Bullets are fine, voice notes transcribed work too. Quick capture, don't worry about formatting.

### Step 2: Generate Draft (30 seconds)
- Copy this entire prompt into ChatGPT, Claude, or your preferred AI
- Paste your input details into the INPUT FIELDS section
- Run the prompt

### Step 3: Review and Refine (7-9 minutes)
- Read through the output
- Verify clinical accuracy (diagnosis, cytology, medications)
- Calculate specific dosages for patient weight
- Adjust tone/wording if needed
- Add patient-specific nuances AI might have missed

### Step 4: Copy into EzyVet (30 seconds)
- Copy the final version
- Paste into appropriate EzyVet record sections
- Sign the record

**Total time: ~10-12 minutes vs. 30-45 minutes writing from scratch**

---

## NOTES FOR REFINEMENT:

**After using this prompt 3-5 times, track:**
- What do you edit every time? → Update prompt to include that
- What does AI get wrong consistently? → Add constraints to prevent that
- What takes longest to review? → Simplify that section

**This prompt will improve with use. Version 1.0 is 80% accurate. By version 2.0, it should be 90% accurate.**

---

**END OF PROMPT**
```

---

## USAGE INSTRUCTIONS FOR TARA:

1. Save this file somewhere accessible
2. When documenting a new derm case, open this file
3. Fill in the INPUT FIELDS section with case details (3 min)
4. Copy entire prompt + your inputs into AI
5. Review/edit the output (7-9 min)
6. Paste into EzyVet

**Target: 10-12 minutes total instead of 30-45 minutes**
