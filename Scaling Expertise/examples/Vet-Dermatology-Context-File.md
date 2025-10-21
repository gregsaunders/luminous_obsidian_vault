# Veterinary Dermatology - AI Context File
**Veterinarian:** Dr. Tara Dixon, DVM (Board-certified veterinary dermatologist)
**Practice:** Cedarwood Veterinary & Animal Emergency Hospital, Red Deer, Alberta, Canada
**Specialty:** Veterinary dermatology (referral-based specialty practice)

**Purpose of this file:** Complete context for AI to build accurate medical record automation prompts

**Last updated:** January 21, 2025

---

## DESIGN PRINCIPLES (CRITICAL - Read First)

### 1. Keep It Simple (Anti-Over-Engineering)
**The failure mode:** Building complex systems with multiple tools, compliance frameworks, and 50-step workflows that the professional never uses.

**The success mode:**
- Professional provides raw expertise in fastest format (bullets, voice notes)
- AI generates 80-90% accurate draft
- Professional reviews/edits in 10-20% of original time
- Copy-paste into existing workflow (no new tools to learn)

**Simple = Adopted. Complex = Abandoned.**

### 2. Mirror the Professional's Existing Process
**Don't redesign their workflow. Slot AI into the existing process.**

**Tara's current process:**
1. See patient (exam, diagnosis, treatment decisions) - 15-30 min
2. *[Gap: Hours pass, she batches documentation]*
3. Sit down to write medical record from memory - 30-60 min
4. Paste into EzyVet

**AI-enhanced process:**
1. See patient (exam, diagnosis, treatment decisions) - 15-30 min
2. Capture key details (2-3 min: bullets or voice note)
3. AI generates draft (30 seconds)
4. Review and refine draft - 5-10 min
5. Paste into EzyVet

**What changed:** Step 2 (quick capture) and Step 3 (AI draft) replace Step 3 (write from scratch).
**What stayed the same:** Her expertise, her review, her EzyVet workflow.

### 3. Match the Professional's Expertise, Not Generic AI Output
**Bad prompt:** "Write a veterinary dermatology record"
→ Result: Generic, textbook language that doesn't sound like Tara

**Good prompt:** Includes Tara's medications, dosing, diagnostic procedures, terminology, abbreviations, structure
→ Result: Sounds like Tara wrote it, minimal editing needed

**The context in this file exists to make AI sound like Tara, not like Wikipedia.**

### 4. Absolutely Simple to Use
**If it takes more than 3 steps, it won't get used.**

**Tara's workflow:**
1. **Input:** Type bullets or record voice note (2-3 min)
2. **Generate:** Paste into AI prompt, run (30 sec)
3. **Refine:** Edit output (5-10 min)

**That's it. No apps. No integrations. No API keys. No complexity.**

Copy-paste is fine if it saves 70% of the time.

### 5. Transferable Framework (For Scaling to Other Professions)

**This project is a template for ANY expertise-based professional with documentation bottleneck.**

**Universal pattern:**
- Expertise time << Documentation time (the bottleneck)
- Professional has consistent patterns (medications, procedures, structure)
- Output has clear audience (clients vs. professionals)
- Professional maintains quality control (reviews AI output)

**To replicate for another professional:**
1. **Collect samples** (their actual work, 5-10 examples)
2. **Identify patterns** (structure, tone, common protocols)
3. **Map document types** (prioritize by time burden)
4. **Build context file** (use this file as template)
5. **Create prompts** (match their voice + domain knowledge)
6. **Test and refine** (3-5 real cases, track edits)
7. **Deploy** (simple workflow, measure adoption)

**See:** `Scaling Expertise/core-concepts/` for universal framework
**See:** This file as domain-specific implementation

---

## THE PROBLEM TO SOLVE

**Current state:** Tara spends 2-5 hours on her day off (unpaid) writing medical records that accumulated during the week.

**Root cause:** Documentation time is disproportionate to expertise time
- Diagnosis/expertise: 15-30 minutes per case
- Documentation: 30-60 minutes per case
- **Bottleneck ratio: 2:1 to 4:1**

**Goal:** Reduce documentation time by 70-80% through AI automation while maintaining 95%+ clinical accuracy.

**Target outcome:** Tara gets her day off back, stops working unpaid hours.

---

## DOCUMENT TYPES TO AUTOMATE (Priority Order)

### Priority 1: Client Discharge Instructions / Treatment Plans ⭐⭐⭐
- **Current time:** 30-45 minutes to write well (which is why she never does)
- **Target time:** 10 minutes (review/edit AI output)
- **Time savings:** 20-35 min per case
- **Frequency:** 2-3 per week
- **Weekly savings:** 40-105 minutes
- **Audience:** Pet owners (accessible language, not technical)
- **See example:** `Client discharge instructions example.md`

### Priority 2: Clinical Summary / Referral Update Letters ⭐⭐⭐
- **Current time:** 20-30 minutes
- **Target time:** 8 minutes
- **Time savings:** 12-22 min per letter
- **Frequency:** 3-5 per week
- **Weekly savings:** 36-110 minutes
- **Audience:** Referring veterinarians (professional, narrative style)
- **See example:** `Clinical Summary - Referral Update For Stripe example.md`

### Priority 3: New Dermatology Case Records (EzyVet)
- **Current time:** 30-45 minutes
- **Target time:** 12 minutes
- **Time savings:** 18-33 min per case
- **Frequency:** 2-3 per week
- **Weekly savings:** 36-99 minutes
- **Audience:** Internal medical records, other veterinarians
- **See examples:** Records 2, 4 in `Vet Record Examples.md`

### Priority 4: Surgical Procedure Records (EzyVet)
- **Current time:** 20-30 minutes
- **Target time:** 10 minutes
- **Time savings:** 10-20 min per procedure
- **Frequency:** 1-2 per week
- **Weekly savings:** 10-40 minutes
- **Audience:** Internal medical records, other veterinarians
- **See examples:** Records 1, 6, 9, 11 in `Vet Record Examples.md`

### Priority 5: Dermatology Recheck Records (EzyVet)
- **Current time:** 10-15 minutes
- **Target time:** 5 minutes
- **Time savings:** 5-10 min per recheck
- **Frequency:** 5-8 per week
- **Weekly savings:** 25-80 minutes
- **Audience:** Internal medical records, other veterinarians
- **See examples:** Records 3, 5, 7 in `Vet Record Examples.md`

**TOTAL POTENTIAL WEEKLY SAVINGS: 147-434 minutes (2.5-7.2 hours)**

---

## TARA'S WRITING STYLE (Critical for AI Prompts)

### EzyVet Medical Records (Vets as Audience)

**Structure (consistent across all records):**
1. **History** (with pre-surgical client questions if applicable)
2. **Physical Exam** (system-by-system OR focused dermatological exam)
3. **Assessment** (diagnosis + differential diagnoses)
4. **Plan** (numbered, clear action items)
5. **Prescriptions** (separate section with exact dosing)
6. **Procedure Notes** (if applicable - detailed step-by-step)

**Tone:**
- Clinical and concise (not wordy, gets to the point)
- Technical language appropriate (writing for other vets)
- Uses veterinary abbreviations freely: DDx, WNL, NSF, AU, BID, SID, PO, IM, SQ, OD (right), OS (left), OU (both eyes), AD (right ear), AS (left ear), PE, Dx, Tx, Rx, TNTC, etc.
- Structured bullets/paragraphs (easy to scan)

**Length:**
- Routine cases: 1-2 paragraphs per section
- Complex cases: More detailed but still organized and concise

**Key Elements She ALWAYS Includes:**
- Patient signalment (species, breed, age, sex, weight)
- Body condition score (X/5 scale)
- Diagnosis (with DDx when uncertain)
- Medications with exact dosing (drug name, mg/kg, route, frequency, duration)
- Cytology results when performed (organisms present, severity: 1-4+ scale)
- Follow-up plan
- Recheck timeline (specific: "2 weeks", "3-4 weeks", etc.)

**Abbreviations She Uses Consistently:**
- WNL = Within Normal Limits
- NSF = No Significant Findings
- DDx = Differential Diagnosis
- Dx = Diagnosis
- Tx = Treatment
- Rx = Prescription
- BID = Twice daily
- SID = Once daily
- TID = Three times daily
- QID = Four times daily
- EOD = Every other day
- PRN = As needed
- PO = By mouth (oral)
- SQ = Subcutaneous
- IM = Intramuscular
- IV = Intravenous
- AU = Both ears
- AD = Right ear
- AS = Left ear
- OU = Both eyes
- OD = Right eye
- OS = Left eye
- PE = Physical exam
- O = Owner
- TNTC = Too Numerous To Count
- C/S = Culture and sensitivity
- MIC = Minimum inhibitory concentration
- MMM = Masticatory muscle myositis
- CAD = Canine atopic dermatitis
- OE = Otitis externa
- OM = Otitis media
- TM = Tympanic membrane
- FNA = Fine needle aspirate
- GA = General anesthetic
- UDF = Until directed further

### Client Discharge Instructions (Pet Owners as Audience)

**Structure:**
1. **Date and client/patient info**
2. **Reason for visit / Diagnosis** (clear header)
3. **Summary of diagnostics / treatment** (narrative, tells the story)
4. **What we found** (plain language explanation)
5. **What it means** (prognosis, what to expect)
6. **Medications** (numbered list with clear instructions)
7. **What to watch for** (warning signs to call about)
8. **Next steps** (recheck timing, follow-up)

**Tone:**
- Professional but warm and accessible
- Educational without being condescending
- Uses plain language, explains technical terms
- Empathetic and reassuring
- Honest about challenges and realistic expectations

**Key Characteristics:**
- Translates medical findings into plain language
- Explains WHY treatments are needed (not just WHAT)
- Addresses common owner concerns proactively
- Clear medication instructions (when to start, how to give)
- Specific about what to monitor and when to call

### Referral Update Letters (Referring Vets as Audience)

**Structure:**
1. **Greeting** ("Dear Dr. [Name],")
2. **Opening line** (patient name, date seen, reason for referral)
3. **Initial presentation summary** (what referring vet sent, what Tara found initially)
4. **What was done** (diagnostics, procedures, narrative style)
5. **Diagnosis** (bolded, clear)
6. **Prognosis and owner counseling** (what was discussed with owner)
7. **Ongoing care plan** (medications, rechecks, long-term management)
8. **Closing** (thank you, offer to discuss, contact info)
9. **Signature block** (Dr. Tara Dixon credentials, clinic address)

**Tone:**
- Professional, collegial vet-to-vet communication
- Narrative style (tells the story, not bullet points)
- Respectful of referring vet's initial work
- Educational about specialty findings
- Collaborative approach to ongoing care

---

## TARA'S TREATMENT PROTOCOLS

### Common Medications (with typical dosing)

**Allergy/Itch Control:**
- **Apoquel (oclacitinib):** 0.4-0.6 mg/kg PO BID x 14 days, then SID for maintenance
- **Cytopoint (lokivetmab):** 2 mg/kg SQ, every 4-8 weeks
- **Prednisone/Prednisolone:** Varies by condition; typical starting 0.5-1 mg/kg PO SID-BID, then taper
- **Atopica (cyclosporine):** 5 mg/kg PO SID (monitor and adjust)

**Antibiotics:**
- **Cephalexin:** 15-30 mg/kg PO BID x 3-4 weeks (pyoderma)
- **Clavaseptin/Clavamox:** 12.5-25 mg/kg PO BID x 2-4 weeks
- **Enrofloxacin (Baytril):** For resistant infections, dosed based on C/S results

**Antifungals:**
- **Ketoconazole:** Typical dosing for Malassezia dermatitis or systemic use
- **Itraconazole:** For resistant yeast or fungal infections

**Pain Management:**
- **Gabapentin:** 10-20 mg/kg PO BID-TID (neuropathic pain, anxiety)
- **Buprenorphine:** 0.01-0.02 mg/kg PO/SQ BID-TID (moderate pain)
- **Meloxicam:** 0.1 mg/kg PO SID (anti-inflammatory)

**Other:**
- **N-Acetylcysteine (NAC):** For biofilm disruption in chronic ear infections

### Topical Treatments

**Shampoos:**
- **Douxo S3 Calm Shampoo:** For atopic/sensitive skin; bathe 1-2x weekly, 5-10 min contact time
- **Douxo S3 Pyo Shampoo:** For bacterial/yeast control; bathe 1-2x weekly, 5-10 min contact time
- **Douxo Pyo Pads:** For skin fold cleaning, interdigital cleaning; use 2-3x weekly

**Ear Medications:**
- **Mometamax:** For otitis externa (bacterial + yeast + inflammation); typical 0.2-1ml per ear SID-BID
- **Otic Prep (Baytril/Dexamethasone/TrizEDTA):** For resistant bacterial OE; BID dosing
- **Miconazole/Dex/Triz Solution:** For yeast otitis; SID-BID dosing
- **Posatex:** For OE with mixed infections
- **EpiOtic / KlearOtic:** Ear cleaners (maintenance or pre-treatment)
- **SA Baytril Solution:** For instillation into bulla during ear flushes

**Other Topicals:**
- **CortOtic Spray:** For itch control in skin folds or localized areas

### Prescription Foods (for food allergy trials)

- **Hill's z/d:** Hydrolyzed protein diet; strict 8-12 week elimination trial
- **Royal Canin Hydrolyzed Protein:** Alternative hydrolyzed diet
- **Canadian Naturals Pork (or other novel protein):** Single protein source diet trial

**Key instruction for food trials:** Must be EXCLUSIVE (no treats, table food, flavored medications) for 8-12 weeks to be diagnostic.

---

## COMMON DERMATOLOGY DIAGNOSES

### Primary Diagnoses

**Canine Atopic Dermatitis (CAD):**
- Chronic allergic skin disease (environmental allergens)
- Typical presentation: Pruritus (face, feet, axillae, ventrum, ears)
- Often seasonal initially, becomes year-round
- Secondary infections common (bacterial pyoderma, Malassezia)
- Long-term management required (immunosuppressives, topical therapy)

**Food Allergy:**
- Similar presentation to CAD (pruritus, skin/ear infections)
- Diagnosed via strict elimination diet trial (8-12 weeks)
- Only definitive Dx is dietary challenge (reintroduce old food, signs recur)

**Pyoderma (Bacterial Skin Infection):**
- Often secondary to allergic disease or other underlying cause
- Cytology: Cocci 2-4+, neutrophils
- Treatment: Antibiotics (3-4 weeks minimum) + topical therapy
- Recurrent cases: Look for underlying cause, consider C/S for resistance

**Malassezia Dermatitis (Yeast Infection):**
- Common in allergic dogs, secondary opportunist
- Cytology: Yeast organisms 2-4+
- Treatment: Antifungal shampoos, systemic ketoconazole if severe

**Otitis Externa (OE):**
- Ear canal infection (bacterial, yeast, or mixed)
- Often secondary to allergies, ear conformation, foreign material
- Cytology determines organisms (cocci, rods, yeast)
- Treatment: Topical medications, address underlying cause

**Otitis Media (OM):**
- Middle ear infection (bulla involvement)
- Often chronic, may have ruptured tympanic membrane
- Requires systemic antibiotics + topical therapy
- May need ear flush under GA (video otoscopy)

### Specialty Cases

**Masticatory Muscle Myositis (MMM):**
- Immune-mediated inflammation of masticatory muscles
- Presentation: Facial pain, difficulty chewing, trismus, muscle atrophy
- Diagnosis: Clinical signs, rule out other causes (trauma, TMJ, retrobulbar abscess)
- Treatment: Immunosuppression (prednisone high dose initially, taper)

**Ceruminous Cystomatosis:**
- Cystic lesions in ear canal (ceruminous gland origin)
- Often leads to chronic OE/OM
- Treatment: Surgical removal of cysts, long-term steroids to reduce recurrence
- Prognosis: Cysts often recur, may ultimately require TECA-BO (salvage surgery)

**Aural Hematoma:**
- Blood-filled swelling of pinna
- Often secondary to head shaking from ear infection
- Treatment: Surgical drainage and tacking sutures
- Must address underlying ear disease or will recur

---

## DIAGNOSTIC PROCEDURES TARA PERFORMS

### Cytology
**Skin cytology:**
- Technique: Tape prep, impression smear, or direct smear
- Documents organisms: Cocci (bacteria), rods (bacteria), yeast (Malassezia), neutrophils
- Severity scale: 1+ (rare), 2+ (few), 3+ (moderate), 4+ (many), TNTC (too numerous to count)

**Ear cytology:**
- Technique: Swab from canal, roll onto slide
- Documents organisms and inflammatory cells
- Helps guide treatment selection (antibacterial vs. antifungal)

**Cytology reporting format Tara uses:**
- Location (e.g., "Skin cytology - ventrum", "Cytology AD")
- Organisms: "cocci 3+, yeast 2+, neutrophils TNTC"

### Video Otoscopy (Ear Flushes)
**Performed under general anesthesia:**
- Examine ear canal and tympanic membrane with video otoscope
- Flush/suction canal to remove debris
- If TM ruptured: Flush bulla, instill medication directly into bulla
- Cytology of canal and/or bulla discharge
- May remove masses, polyps, foreign material
- Post-procedure: Systemic + topical medications for 4-8 weeks

### Other Diagnostics
- **Skin scrapings:** Rule out mites (Demodex, Sarcoptes)
- **FNA (fine needle aspirate):** For masses/lumps (cytology to differentiate lipoma, mast cell tumor, etc.)
- **Skin biopsy:** For unusual presentations, rule out immune-mediated disease
- **Allergy testing:** Intradermal or serum testing for allergen identification (for immunotherapy)
- **Culture & Sensitivity (C/S):** For resistant or recurrent infections

---

## FOLLOW-UP & RECHECK PROTOCOLS

**Typical recheck timelines:**
- **Otitis media:** Every 2 weeks until resolved (may take 6-8 weeks total)
- **Pyoderma:** 3-4 weeks (continue antibiotics 1 week past clinical resolution)
- **New allergy cases:** 2-4 weeks initially, then q3-6 months once stable
- **Chronic allergy management:** Every 3-6 months (stable cases)
- **Post-surgical:** 1-2 weeks (depending on procedure)

**What Tara tells owners to monitor:**
- Pruritus level (scratching, licking, rubbing)
- Secondary signs (redness, odor, discharge)
- Medication side effects (GI upset from antibiotics, increased thirst/urination from steroids)
- Response to treatment (improvement timeline)

**When to call immediately:**
- Neurologic signs after ear flush (head tilt, Horner's syndrome, ataxia)
- Severe medication reactions (vomiting, diarrhea, lethargy)
- Worsening clinical signs despite treatment
- Signs of pain or distress

---

## OWNER EDUCATION THEMES

**Tara consistently educates owners about:**

**Chronic nature of allergic disease:**
- "This is a lifelong condition we manage, not cure"
- "Like people with hay fever - we control symptoms but can't eliminate the allergy"
- "Flare-ups can happen; we adjust treatment as needed"

**Compliance importance:**
- "Stopping antibiotics too early leads to recurrence and resistance"
- "Bathing protocols are critical - we're not just cleaning, we're treating"
- "Consistency with medications is key to success"

**Realistic expectations:**
- "Most dogs do very well with treatment, but it requires ongoing commitment"
- "We're aiming for 80-90% improvement, not perfection"
- "It may take 2-3 adjustments to find the right protocol for your pet"

**Treatment rationale:**
- "We're treating the infection now, then addressing the underlying allergy"
- "Steroids reduce inflammation and help break the itch-scratch cycle"
- "Topical therapy is just as important as oral medications"

**Cost transparency:**
- "Initial workup typically runs $X-Y"
- "Ongoing management usually costs $X/month"
- "This is an investment in your pet's quality of life"

---

## PRACTICE CONTEXT (Important for Prompts)

**Location:** Red Deer, Alberta, Canada
- No DEA/controlled substance complexity (Canadian regulations different from US)
- Provincial veterinary practice act (Alberta) governs standards
- Less regulatory documentation burden than US practices

**Practice Type:** Referral-based specialty practice
- Tara sees cases referred from general practice vets
- Also sees clients directly for dermatology concerns
- Mix of new consultations and ongoing management

**Patient Population:**
- Primarily dogs, some cats
- Dermatology focus: Allergic disease, ear infections, skin infections
- Some general medicine/surgery (wellness, dentals, emergencies)

**Medical Records:**
- Uses EzyVet practice management software
- Records are for internal use + other veterinarians (referring vets, future care providers)
- Copy-paste workflow acceptable (AI generates, Tara reviews/edits, pastes into EzyVet)

**Professional Obligations:**
- Maintain complete, accurate medical records (standard of care)
- Communicate findings to referring veterinarians (professional courtesy)
- Educate clients about diagnoses and treatment plans (informed consent)
- Document client discussions and consent
- No VCPR documentation complexity (less formal than US requirements)

---

## AI PROMPT REQUIREMENTS

**To generate accurate outputs, AI prompts must:**

1. **Match Tara's voice and style:**
   - Clinical/concise for vet audiences
   - Educational/accessible for client audiences
   - Use her abbreviations and terminology

2. **Include domain-specific knowledge:**
   - Her common medications and dosing
   - Her topical treatment protocols
   - Her diagnostic procedures
   - Her follow-up timelines

3. **Maintain structure consistency:**
   - EzyVet records: History → PE → Assessment → Plan → Rx
   - Client instructions: Reason → What we did → Diagnosis → Medications → Watch for → Follow-up
   - Referral letters: Greeting → Summary → Findings → Diagnosis → Plan → Thank you

4. **Never hallucinate clinical information:**
   - Dosages must be provided by Tara (AI doesn't guess)
   - Cytology results must be provided (AI doesn't invent)
   - Patient-specific details must come from input (AI doesn't assume)

5. **Flag for Tara to verify:**
   - Drug dosages (AI can suggest based on her protocols, but Tara confirms for patient weight)
   - Diagnosis accuracy
   - Treatment appropriateness
   - Client-specific context

6. **80-20 Rule:**
   - AI generates 80-90% accurate draft
   - Tara reviews/edits the critical 10-20% (clinical judgment, patient-specific nuances)
   - Target: Reduce her time by 70-80%, not eliminate her review

---

## SUCCESS METRICS

**Adoption (most important):**
- Does Tara use the prompts for every case after Week 2?
- If no, why? (Fix that issue)

**Time Savings:**
- Time per document before AI: X minutes
- Time per document after AI (input + review): Y minutes
- Savings per document: X - Y
- Weekly savings: (X - Y) × frequency

**Quality:**
- Edit time (how long does Tara spend refining AI output?)
- Revision rate (how often does she need to start over vs. refine?)
- Client feedback (do discharge instructions improve client comprehension?)
- Referring vet feedback (are referral letters clear and complete?)

**Outcome:**
- Does Tara stop working on her day off?
- Stress reduction (subjective but important)
- Capacity increase (can she see more patients? provide better service?)

**Target:**
- 2-5 hours per week saved
- 80-90% accurate output (10-20% needs Tara's refinement)
- 100% adoption (she uses it every time)
- Zero unpaid weekend work

---

## SAMPLE RECORDS REFERENCE

**All sample records located in:** `Vet Record Examples.md`

**Dermatology Rechecks:** Records 2, 3, 5, 7
**New Dermatology Cases:** Record 4
**Surgical Procedures:** Records 1, 6, 9, 11 (ear flushes, mass removals)
**General Medicine:** Records 8, 10, 12 (wellness, dental, lameness)

**Additional document samples:**
- `Client discharge instructions example.md` (Stripe - ear flush)
- `Clinical Summary - Referral Update For Stripe example.md` (letter to referring vet)
- `Referral Form Example.md` (incoming referral format - what Tara receives)

---

## NEXT STEPS FOR AI PROMPT BUILDING

**Phase 1: Build Priority 1 & 2 Prompts**
1. Client Discharge Instructions
2. Referral Update Letters

**Phase 2: Test with Real Cases**
- Tara provides case details
- Run through prompts
- Track edits
- Refine prompts

**Phase 3: Build Remaining Prompts**
3. New Dermatology Case Records
4. Surgical Procedure Records
5. Dermatology Recheck Records

**Phase 4: Deploy & Measure**
- Weekly time tracking
- Adoption monitoring
- Refinement based on usage

---

**This context file ensures any AI can immediately understand Tara's practice and build accurate, useful automation prompts without re-explaining the fundamentals.**
