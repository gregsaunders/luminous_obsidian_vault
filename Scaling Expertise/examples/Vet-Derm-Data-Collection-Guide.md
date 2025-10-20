# Quick Guide: Getting Info from Tara (For Jeff)

**The Real Problem:** Tara spends 2-5 hours on her DAY OFF doing medical records, unpaid. This is the bottleneck.

**The Solution:** 2-3 AI prompt templates that let her capture case details in 2-3 minutes and review/edit output in 5-10 minutes instead of writing from scratch for 30-45 minutes.

---

## What You Actually Need from Her:

### 1. Sample Medical Records (CRITICAL)
**Get 5-10 EzyVet medical records:**
- De-identified (remove client personal info)
- Mix of common dermatology cases
- Shows her actual writing style, structure, tone

**How to ask:**
"Can you export 5-10 recent case records from EzyVet? Just remove client names/addresses. I need to see your actual writing to build prompts that sound like you."

**What to look for when you get them:**
- What structure does she use? (SOAP? Custom format?)
- What information is always included?
- What's her tone? (Clinical and terse? Detailed?)
- What medications/treatments appear frequently?
- How long are they? (1 paragraph? 1 page?)

### 2. Treatment Protocols (Quick Reference)
**Ask her to list:**
- Top 10 oral medications she prescribes (drug name, typical dose, conditions)
- Top 5-8 topical treatments (products, application instructions)
- Top 3-5 prescription foods (brands, conditions)

**Why:** This becomes the AI's knowledge base. Instead of generic veterinary info, it knows HER preferred treatments.

**How to ask:**
"What are your go-to medications, topicals, and foods? Just a quick list with typical dosages. This helps AI suggest the right treatments for each condition."

### 3. Top Conditions She Treats
**Ask her to list 5-8 most common cases:**
- Examples: Atopic dermatitis, food allergies, hot spots, yeast infections, etc.

**Why:** AI can recognize patterns and apply appropriate protocols.

### 4. How She Wants to Capture Input
**Ask:**
"When you're ready to document a case, would you rather:
- Talk through it (voice notes)?
- Type quick bullets?
- Fill in a structured form?"

**Why:** This determines the input format for the prompts.

### 5. Success Criteria
**Ask:**
"What would make this worth using? What would make you stop using it?"

**Why:** Understand her tolerance for editing and what "good enough" looks like.

---

## What You Do Once You Have Samples:

### Step 1: Analyze the Samples (1-2 hours)
- Read through 5-10 records
- Note patterns:
  - Structure (sections, headers)
  - Tone (clinical terseness vs. detailed narrative)
  - What's always included (signalment, diagnosis, meds, follow-up, etc.)
  - Length (avg word count)
  - Technical level (for other vets, so technical is fine)

### Step 2: Build First Prompt (30 minutes)
- Use [healthcare-prompts.md](healthcare-prompts.md) as starting template
- Customize based on her samples:
  - Structure: Match her format
  - Tone: Match her writing style
  - Content: Include fields she always fills out
  - Knowledge base: Include her common medications/treatments

### Step 3: Test with Her (15 minutes)
- Ask for details of ONE recent case (not from samples)
- Run through your prompt
- Send her the output
- Ask: "What would you change?"

### Step 4: Refine (30 minutes)
- Track what she edited
- Update prompt to address those issues
- Test again with 2-3 more cases

### Step 5: Deploy
- Give her the working prompt
- She uses for 1 week on all cases
- Check in: "What still needs adjustment?"

---

## The 3 Prompts You'll Probably Build:

### Prompt #1: Dermatology Case Medical Record
**Purpose:** Daily case documentation for EzyVet

**Input format:**
- Quick bullets or voice note with:
  - Patient info (species, breed, age, weight)
  - Diagnosis
  - Findings (exam, diagnostics)
  - Treatment prescribed (meds, topicals, food)
  - Follow-up plan

**Output:** Clean SOAP-style (or her preferred format) medical record, ready to paste into EzyVet

**Time savings:** 30-45 min → 5-10 min = **20-35 min per case**

### Prompt #2: Treatment Plan for Pet Owner (If Relevant)
**Purpose:** Educational letter explaining condition and treatment to client

**Input format:**
- Diagnosis
- Treatment protocol
- Prognosis

**Output:** 1-page letter in accessible language

**Time savings:** 30 min → 10 min = **20 min per letter**

### Prompt #3: Referral Summary Back to Primary Vet (If Relevant)
**Purpose:** Professional summary of her findings and recommendations

**Input format:**
- What referring vet sent
- Her findings
- Her treatment plan
- Recommendations for ongoing care

**Output:** Professional letter to referring vet

**Time savings:** 20-30 min → 5-10 min = **15-20 min per referral**

---

## Time Savings Math:

**Current state:**
- 2-5 hours/week on medical records = 8-20 cases taking 15-45 min each

**Target state:**
- Same 8-20 cases taking 5-10 min each = 40-200 min/week = 0.7-3.3 hours

**Time savings: 1.3-4.3 hours per week**

**Result:** She doesn't work on her day off anymore.

---

## Red Flags to Watch For:

**If she says:**
- "I don't have time to provide samples" → **Offer to extract from EzyVet yourself or shadow her for 2 hours**
- "AI won't understand dermatology" → **That's why you're building custom prompts with her treatment protocols**
- "I need it perfect" → **Manage expectations: AI gets to 80-90%, she refines the last 10-20%**
- "This seems complicated" → **Simplify: Just send me 5 records, I'll build the first version, you test once**

**If you notice:**
- Her records are very short (2-3 sentences) → Prompt should generate concise output
- Her records are very long (1+ pages) → Prompt needs to match that detail level
- She uses lots of abbreviations → Include common abbreviations in prompt
- She has a very specific format → Match it exactly

---

## Quick Start (Minimum Viable Data Collection):

**Can't get all 5 sections filled out? Do this:**

1. "Send me 5 recent case records from EzyVet" → **Analyze yourself**
2. "What are your top 5 medications?" → **Quick list**
3. Build first prompt from samples
4. Test with her on 1 case
5. Iterate

**Total time from her: 15 minutes**

You do the rest.

---

## Success = She Uses It Every Week

**The only metric that matters:**
- Does she use it for every case after week 2?
- If yes → Success
- If no → Ask why, fix that issue

**Most common failure modes:**
- Output is too generic (didn't use her samples)
- Takes too long to edit (prompt needs refinement)
- Doesn't match her style (analyze samples better)
- Too many steps (simplify input capture)

**Fix:** Iterate quickly. 3-5 test cases should get you to 90% accuracy.

---

## Bottom Line:

**You need:**
- 5-10 sample medical records (her actual writing)
- List of common treatments (her protocols)
- 2-3 test cases to refine

**You build:**
- 1-3 working prompts (based on her samples)
- Fast input capture method (bullets or voice)
- 80-90% accurate output

**She gets:**
- 2-5 hours per week back
- Her day off back
- Paid for expertise, not typing

**Timeline: 2-3 weeks from samples to deployment.**
