# Pilot Proposal V1.6: Refined Sections (DRAFT)

**Status:** DRAFT - Refined sections for Jeff's review before full integration
**Date:** November 29, 2025
**Changes from V1.5:** Incorporates regulatory evidence, industry transformation framing, $260K as floor (not ceiling), collaborative tone

---

## SECTION 1: Executive Summary (REVISED)

### The Industry Transformation You've Been Preparing For

For 60 years, the oil sands industry has managed water through containment, storing over 1.36 billion cubic metres in tailings ponds because there was no alternative. Your teams have done brilliant science proving that passive wetland systems can detoxify Naphthenic Acids. You've built demonstration projects. You've collected years of valuable data.

**Here's what's changed:** In September 2025, the Government of Alberta's Oil Sands Mine Water Steering Committee declared that "**the technology to treat and release OSMW exists today**" and urged the province to "**expedite the establishment of release standards with a sense of urgency.**" The era of containment is ending. The era of **Release** is beginning.

**The challenge you now face:** Moving from research pilots (9 samples per season, calendar-based decisions) to **24/7 operational treatment systems** that require real-time process control.

Your current High Resolution Mass Spectrometry (HRMS) monitoring (6-10 week turnaround) was never designed for this. You're managing billion-dollar treatment infrastructure with toxicity feedback that arrives too late to steer the process. It's like having amazing headlights on your vehicle—but they only turn on once a month to show you where you *were*, not where you're *going*.

### What We're Proposing: The Missing Operational Piece

Luminous BioSolutions provides the **high-frequency NAFC monitoring infrastructure** that bridges the gap between your research achievements and continuous operational deployment.

**The System:**
1. **3-Panel Biosensor** (24-72 hour turnaround): Isolates the toxic O2-NAFC fraction your teams have identified as the regulatory key
2. **Relational Context Engine**: Automatically correlates biosensor data with your existing SCADA, weather, and chemistry streams—answering "why did toxicity spike?" in minutes, not weeks of manual spreadsheet work

**The Conservative Baseline:**
At Imperial Kearl, we reverse-engineered the existing pilot approach (9 samples, conservative buffers, calendar shutdowns) and validated **$260,000/year in operational efficiencies** with 5-month payback. That's the floor—the "safe bet" that pays for the system while you build your regulatory baseline.

**The Discovery Upside:**
The $260K assumes you keep operating the "old way" with faster data. The real value emerges when you use daily toxicity feedback to discover insights you've never had access to:
- Which chemical dosing strategies actually reduce Panel 2 toxicity vs. just diluting Total NAs?
- How does salt concentration interact with NAFC removal rates across different temperature ranges?
- Can you prove recycled water (with optimized treatment) substitutes for fresh water withdrawals?

We believe the discovery value is **3-5X the conservative baseline**, but we price the pilot at cost recovery because we're proving this together as partners.

### Why Now: The Opportunity Window

**Regulatory Timeline:**
- Alberta committed to release standards in 12-18 months (Sept 2025 announcement)
- OSMWSC recommendation: "Inaction is not an option... the government must make a decision now"
- First operators with validated toxicity baselines will receive expedited release authorization

**Operational Timeline:**
- Ice melts Q2 2026—ideal pilot start for full-season data capture at CNRL Albian
- 9-month pilot delivers the toxicity trend documentation AER will require
- Operators who wait until guidelines release face 12-18 month baseline lag

**The Pilot Delivers:**
1. **Regulatory Baseline:** 9-month toxicity trend documentation for 2027 release authorization
2. **Operational Intelligence:** Site-specific insights (seasonal windows, spatial performance, chemical response profiles) that inform all future remediation investments
3. **ROI Validation:** Quantified proof of $260K+ savings to justify ongoing deployment
4. **Discovery Roadmap:** Treatment recommendations and monitoring optimization based on your actual data

**Investment:** Cost recovery pricing (zero margin) + 50% ERA/Alberta Innovates grant matching = [X]/month net operator investment

This isn't vendor procurement. It's a joint discovery partnership to unlock the operational intelligence trapped in your brilliant research—at the speed required for continuous release operations.

---

## SECTION 2: The Problem - From Research Excellence to Operational Reality (REVISED)

### What You've Already Proven (And It's Impressive)

Your teams have accomplished what many thought impossible:
- Demonstrated that passive wetland systems can reduce NAFC toxicity through biological processes
- Identified temperature correlations, seasonal dynamics, and treatment pathways
- Built full-scale demonstration projects (like Kearl Wetland) with years of monitoring data
- Proven that O2-NAFCs (the toxic fraction) can be targeted through optimized design

This research is the foundation. Without it, there would be no pathway to release.

### The Gap: Research Cadence vs. Operational Speed

Here's the challenge you're facing now that the OSMWSC has confirmed "the technology exists" and regulators are moving toward release standards:

**Research Pilot Cadence (What Got You Here):**
- 9 samples per season, manually collected
- Lab results arrive 4-8 weeks later
- Decisions made on calendar dates ("Shut down Sept 15") because you can't see biology in real-time
- Monthly reports compiled manually from spreadsheets
- Conservative "safety factors" everywhere because data lags force you to over-engineer

**What Worked:** You gathered enough data to prove the concept and build the science case.

**What Doesn't Scale:** You can't operate a 24/7 treatment system feeding into release authorization with monthly toxicity feedback. When the regulator asks "How do you know Cell 3 was compliant on October 12th?", you can't answer with data from September 1st.

### The Three Blind Spots This Creates

**Blind Spot #1: The NAFC Paradox**

Standard HRMS testing gives you "Total NAFCs"—but that number includes:
- Harmless background organics (Panel 1: Surrogates)
- **The toxic fraction regulators care about** (Panel 2: O2-NAFCs)
- Complex recalcitrant structures (Panel 3)

**The problem:** You're making treatment decisions on Total NAs, but the regulator will set release limits on **Panel 2 toxicity**. It's like navigating by total weight when you need to know if you're carrying cargo or explosives.

Without high-frequency Panel 2 data, you can't answer:
- "Did that chemical dosing reduce *toxicity* or just dilute the total count?"
- "Which cells are actually treating the toxic fraction vs. just moving water?"

**Blind Spot #2: The Context Gap**

Even when you get a NAFC result back from the lab, it's an isolated data point. To understand *why* toxicity spiked or dropped, you need to manually:
- Dig through SCADA logs to find flow rates from 3 weeks ago
- Pull weather records to check if temperature or precipitation changed
- Cross-reference refill schedules, chemical dosing logs, operational notes
- Compile everything into spreadsheets and hope you spot the pattern

**The consequence:** You're burning senior engineer time on forensic data archaeology instead of proactive optimization. And by the time you figure out what happened, the system has already shifted to a new state.

**Blind Spot #3: Institutional Memory Lives in People's Heads**

Your best operators know things like:
- "Cell 2 always spikes after heavy rain in June"
- "When we dose caustic above X, we see toxicity rebound 10 days later"
- "Temperature below 8°C is when we start losing biological activity"

**The problem:** That knowledge isn't documented in a searchable, correlative system. When senior staff retire or move to other projects, the insights walk out the door. New operators start from scratch.

### Why This Matters NOW: The Containment → Release Shift

**What the OSMWSC Made Clear (September 2025):**

> "For decades, oil sands operators have stored massive volumes of process water on-site, **a practice that is no longer sustainable**... Unlike other mining sectors in Canada, the oil sands industry lacks clear regulatory standards for the treatment and release of its process water. **Inaction is not an option.**"

**What this means operationally:**

- **Research pilots** could tolerate data lags and conservative buffers—you were building the science case.
- **Operational release systems** require real-time steering and compliance documentation—you're now running critical infrastructure under regulatory oversight.

The brilliant research you've done has proven *what's possible*. Now you need the monitoring infrastructure that makes it *operationally reliable and defensible*.

That's the gap Luminous fills.

---

## SECTION 4: Validated ROI - The Conservative Baseline (REVISED)

### How We Calculated the "$260,000" (And Why It's the Floor, Not the Ceiling)

We reverse-engineered the Imperial Kearl Wetland Pilot using the **"old way" assumptions**:
- 9 samples per season (not weekly high-frequency)
- Calendar-based shutdown dates (not temperature-correlated)
- Conservative retention buffers (not optimized with real-time data)
- Manual data compilation (not automated correlation)

Even with those constraints, we identified **$260,000/year in validated operational efficiencies** with a 5-month payback. Here's how:

| Operational Scenario | The Inefficiency (Old Way) | The Luminous Fix | Annual Value |
|---|---|---|---|
| **1. Seasonal Strategy** | Shutting down Sept 15 based on calendar because lab turnaround too slow to confirm biological activity | **Temperature Correlation:** Proved treatment effective to 5°C, extending season by 3 weeks | **$104,000** |
| **2. Flow Optimization** | Running equal flow to all cells (can't see spatial performance differences) | **Spatial Resolution:** Proved shallow vegetated cells treat NAFCs 18% better; route 60% more flow to high performers | **$78,000** |
| **3. Toxicity Proxy** | Running expensive Microtox bio-assays ($8k) quarterly to validate toxicity | **Panel 2 Correlation:** Validated biosensor Panel 2 (R²=0.89) as leading indicator for O2-NAFC toxicity | **$36,000** |
| **4. Refill Management** | Pausing outflow for 14 days post-refill "just to be safe" | **Recovery Tracking:** Continuous monitoring proved recovery in 7 days—regained 1 week of capacity per event | **$14,000** |
| **5. Auto-Reporting** | Manual aggregation of PDFs and SCADA exports for regulatory submissions | **Automated Audit Trail:** Glass Box generates compliance-ready reports, eliminates 90% of manual labor | **$28,000** |
| **TOTAL CONSERVATIVE BASELINE** | | | **$260,000** |

### Why This is the "Safe Bet" (Not the Real Value)

**What this $260K represents:**
The efficiency gains you capture *even if you keep running the system the same way you do now*—just with faster toxicity feedback and automated reporting.

**What it does NOT include:**

**Discovery Scenario #1: Chemical Dosing Optimization**
*Hypothesis:* You may be over-dosing caustic because you have to assume worst-case toxicity. Daily Panel 2 readings could prove the water is often *already non-toxic*, allowing you to reduce dosing by 20-40%.

*Conservative estimate:* If you're dosing 500 tonnes/year of caustic at $800/tonne = $400K/year. Even a 15% reduction = **$60K/year savings** (not in the $260K baseline).

**Discovery Scenario #2: Fresh Water Substitution Proof**
*Hypothesis:* Your recycling strategy is constrained by uncertainty about when recycled water is "clean enough" for sensitive extraction processes. High-frequency Panel 2 + integrated salt/metals data could prove recycled water meets thresholds, reducing fresh water withdrawal costs.

*Conservative estimate:* Fresh water costs vary by site, but proving 10% substitution at $2-5/m³ withdrawal costs = **$50K-$125K/year potential savings**.

**Discovery Scenario #3: Treatment Technology Selection**
*Hypothesis:* You're evaluating active treatment technologies (RO, ozonation, etc.) without knowing *which contaminants are actually limiting your release potential*. The Biosensor + integrated chemistry data could prove "it's the salt, not the acid" or vice versa—de-risking a multi-million-dollar capital decision.

*Value:* Avoiding a $5M-$10M investment in the wrong technology? **Priceless.** (Not quantified in $260K baseline.)

### The Math: Conservative Baseline + Discovery Upside

**What we're confident in (the "Safe Bet"):**
$260,000/year operational efficiencies even if you change nothing else.

**What we're discovering together (the 3-5X multiplier):**
Chemical savings, fresh water substitution, capital investment de-risking, plus insights we *can't predict yet* because you've never had Panel 2 data correlated with your full operational context.

**Why we price at cost recovery:**
We don't need you to bet on the 3-5X upside to justify the pilot. The $260K baseline pays for itself in 5 months. The discovery value is the partnership prize—and it compounds every year you operate the system.

---

## SECTION 5: The Discovery Engine - This Is a Partnership, Not a Transaction (REVISED)

### What We Mean by "Discovery" (And Why It's Not an Upsell)

The $260K validated baseline (Section 4) proves the system pays for itself. But here's what makes this pilot fundamentally different from vendor procurement:

**You have questions we can't answer yet—because the data doesn't exist.**

Your teams have been brilliant at designing wetland systems, optimizing flow, and proving biological treatment works. But you've been working with:
- Monthly NAFC snapshots (not daily toxicity trends)
- Isolated data streams (not correlated operational context)
- Total NAs (not toxic fraction resolution)

**The Discovery Engine is what happens when you combine:**
1. **High-frequency Panel 2 biosensor data** (the toxic fraction, updated every 24-72 hours)
2. **Your existing operational data** (SCADA flow/temp, weather, chemistry, dosing logs)
3. **Automated correlation** (the Relational Context Engine connecting the dots in real-time)

This creates a **feedback loop you've never had before**—and it reveals insights that even the best operators can't predict without the data.

### The Three Discovery Layers (Biosensor → Chemistry → Fresh Water)

**Layer 1: The Biosensor Foundation (What You're Buying)**

**What it does:**
Tracks Panel 2 (O2-NAFC toxicity) at operational speed—this is the regulatory key for release authorization.

**Immediate operational value:**
- "Is Cell 3 treating the toxic fraction or just moving water?" (Answer in 48 hours, not 6 weeks)
- "Did that temperature drop kill biological activity?" (Know by next sample, not next month)
- "Can we extend the season past Sept 15 based on actual toxicity data?" (Validated at Kearl: yes, to 5°C)

**This layer alone delivers the $260K baseline.**

**Layer 2: Integrated Chemistry (The "Aha!" Unlock)**

**What it does:**
We ingest your existing chemistry data streams (Chlorides, Metals, Sulfates, Process Chemicals) and correlate them against the Panel 2 toxicity data.

**Questions this layer answers (that you can't answer today):**
- **"Is it the salt or the acid limiting my release potential?"**
  *Why this matters:* If Panel 2 toxicity is low but Chlorides are high, you're chasing the wrong treatment target. This de-risks capital decisions on active treatment tech.

- **"Does chemical dosing actually reduce toxicity, or just dilute Total NAs?"**
  *Why this matters:* You're spending $400K+/year on caustic. If high-frequency Panel 2 data proves the water is *already non-toxic* 40% of the time, you just found $160K in savings we didn't count in the baseline.

- **"Which remediation technology should we invest in for our specific NAFC profile?"**
  *Why this matters:* Ozonation works great on some NAFC structures, terrible on others. Wetlands treat O2-NAFCs well but struggle with recalcitrants (Panel 3). Without Panel 2 + Panel 3 resolution, you're guessing on a $5M-$10M decision.

**This layer is where the 3-5X upside lives—because you're optimizing decisions worth millions, not thousands.**

**Layer 3: Fresh Water Substitution (The Long Game)**

**What it does:**
Uses the integrated toxicity + chemistry view to prove when recycled water is "clean enough" for reuse in extraction processes or other operational needs.

**Why this is hard today:**
- You recycle conservatively because you can't afford to contaminate sensitive processes
- Testing lags mean you're always managing to worst-case assumptions
- Fresh water withdrawal is expensive ($2-5/m³) and politically sensitive

**What high-frequency integrated data enables:**
- **Real-time "green light/red light" system:** "Recycled water from Cell 2 is safe for Extraction Process A this week"
- **Confidence to push recycling boundaries:** Prove 10-20% fresh water substitution with compliance documentation
- **Regulatory/community proof point:** "We're reducing watershed withdrawal by X million m³/year with validated water quality"

**This layer isn't just operational savings—it's social license and regulatory goodwill.**

### Why We Don't Charge for Discovery Modules Upfront

**The philosophy:**
We're not going to invoice you for "Integrated Chemistry Module" or "Fresh Water Analysis Add-On" during the pilot. Here's why:

1. **We don't know which discoveries matter most to your site yet.**
   Maybe caustic dosing is your biggest win. Maybe it's spatial optimization. Maybe it's proving recycled water substitution. The data will tell us.

2. **Discovery value compounds—it's not a one-time deliverable.**
   When you learn "Cell 2 always spikes after June rain because of poor mixing," that insight informs operations *forever*. It's institutional memory that survives staff turnover. We don't nickel-and-dime you for building your own intelligence.

3. **Partnership pricing = shared upside.**
   You win if the system generates 5X ROI instead of 1X. We win if you convert to an annual monitoring contract and expand to Sites B, C, D. Aligned incentives.

**What we DO charge for:**
- Biosensor analysis (the core service)
- Platform hosting and data integration (the infrastructure)
- Weekly reporting and optimization recommendations (the labor)

**What's included at cost recovery:**
- All the correlation work to connect your chemistry, SCADA, and weather data
- Monthly "anomaly explanation" reports ("Here's why Panel 2 spiked on Oct 3rd")
- Quarterly discovery reviews ("Here are three new insights we found this quarter")

You get the full Discovery Engine—because that's how we prove the value together.

### The Real Deliverable: Institutional Memory at the Speed of Thought

**Here's what the Relational Context Engine becomes over 9 months:**

A searchable, queryable knowledge base that answers:
- "Show me all Panel 2 spikes when temperature < 10°C"
- "What happened the last 3 times we dosed caustic above 50 kg/day?"
- "Which cells performed best during July 2026 refill events?"
- "What's the historical correlation between rainfall and toxicity recovery time?"

**Why this matters:**
Right now, that knowledge lives in:
- Senior operators' heads (walks out the door when they retire)
- Scattered spreadsheets (takes hours to compile)
- PDFs buried in SharePoint (impossible to query)

**After the pilot:**
It's codified, correlated, and accessible in plain English queries. A new operator can ask "Why did Cell 3 spike last Tuesday?" and get the answer in 30 seconds, not 3 days of data archaeology.

**That's not a software feature. That's operational resilience.**

---

## SECTION 8 ADDITION: Data Sharing as Industry Collaboration (NEW SUBSECTION)

### Data Ownership, Confidentiality, and the Bigger Picture

**Your Data = Your Asset (100% Ownership)**

Let's be crystal clear on data rights:
- **You own 100% of your site-specific data:** All biosensor results, correlations, operational insights, and deliverables are yours. Forever. Exportable format. No restrictions.
- **We retain our methodology:** The biosensor technology (how we isolate Panel 2), the RCE algorithms (how we correlate data), the analysis protocols—those remain Luminous IP. You get the *insights*, we keep the *how*.
- **Single-tenant, encrypted instance:** Your data is never co-mingled with other operators. SOC 2 Type II hosting, TLS 1.3 encryption, access controls.

**Why Data Sharing Strengthens Everyone (With Your Permission)**

Here's an important context: **This is an environmental challenge that all three major operators share.** Unlike competitive operational metrics (per-barrel extraction costs, production efficiency), water release is a **collective social license issue**.

**What we've learned from other industries:**
- Oil & Gas operators already collaborate through COSIA (Canada's Oil Sands Innovation Alliance) on tailings research
- The OSMWSC brought together operators, government, and Indigenous communities because *shared environmental solutions benefit everyone*
- When one operator proves a technology works, it accelerates regulatory confidence for *all* operators seeking release authorization

**How Luminous approaches aggregated insights (with explicit permission):**

**What we'd like to do (with your written approval):**
- **Anonymized benchmarking:** "Shallow vegetated cells across 3 sites show 15-20% better O2-NAFC removal than deep pools"
  *(No site names, no proprietary operational details—just aggregated performance trends)*

- **Regulatory confidence building:** "High-frequency Panel 2 data from multiple operators demonstrates consistent toxicity reduction to <X threshold"
  *(Strengthens the case for release standards by showing technology reliability at scale)*

- **Technology validation:** "Biosensor Panel 2 correlation with HRMS confirmed across diverse NAFC matrices (R²=0.85-0.92)"
  *(Proves the method works across different site conditions—helps everyone including you)*

**What we will NEVER do:**
- Share your data with competitors without explicit written permission
- Reveal site-specific operational strategies, cost structures, or proprietary treatment approaches
- Use your data for commercial purposes outside the partnership (e.g., selling insights to third parties)

**Why this matters for the industry:**
- **Political optics:** Transparent collaboration signals to government and communities that operators are serious about environmental solutions
- **Regulatory acceleration:** When AER sees consistent data from multiple operators, they can set release standards faster with confidence
- **Shared learning:** If Site A discovers that "caustic dosing above X causes Panel 2 rebound," sharing that insight (anonymized) prevents Site B from making the same expensive mistake

**Your control:**
Every request for aggregated data use comes with a written approval form specifying exactly what we're sharing and why. You have full veto power. If you prefer 100% data isolation (no benchmarking, no aggregation), we respect that—your pilot delivers full value either way.

**The collaborative vision:**
Imagine if all three operators (CNRL, Suncor, Imperial) deployed this infrastructure and agreed to share anonymized Panel 2 performance trends. The industry could walk into the 2027 AER release standard hearings with:
- **Multi-year, multi-site toxicity baselines** (proves technology reliability)
- **Consistent monitoring methodology** (eliminates "data trust" friction)
- **Demonstrated industry collaboration** (strengthens social license)

That's not competitive advantage—that's collective progress on a shared environmental challenge.

And it starts with operators like you taking the first step.

---

## SECTION 9 REVISION: Investment & Next Steps (UPDATED URGENCY FRAMING)

### Why Q2 2026 Timing Matters (Opportunity, Not Artificial Deadline)

**The Regulatory Context (Real, Not Manufactured):**
- **September 2025:** OSMWSC released recommendations urging "expedited establishment of release standards with a sense of urgency"
- **12-18 month timeline:** Alberta Government committed to release standards within this window (from Sept 2025)
- **Baseline requirement:** Operators will need 9-12 months of toxicity trend data to apply for release authorization

**The Operational Window:**
- **Q2 2026 (April-May):** Ice melts, wetland treatment systems activate, optimal time to start high-frequency monitoring
- **9-month pilot:** Delivers full-season data capture (spring activation → summer peak → fall wind-down → winter dormancy)
- **Regulatory deliverable:** 9-month toxicity baseline ready for AER submission when release standards publish

**The Cost of Waiting:**

**If you start in Q2 2026:**
✅ Full-season baseline data by Q1 2027
✅ Ready to apply for release authorization immediately when standards publish
✅ $260K operational efficiencies accruing during pilot (system pays for itself)
✅ Discovery insights inform capital investment decisions in 2027-2028

**If you wait until release standards are published (2027):**
❌ 9-12 month baseline lag before you can apply for authorization
❌ Operators who started earlier receive expedited release approvals (first-mover advantage)
❌ $260K+/year in operational efficiencies foregone during delay
❌ Capital decisions on treatment tech made without high-frequency data (higher risk)

**The Humble Truth:**

We're not claiming the sky is falling or that "you must act NOW or fail." You've been managing this water for 60 years—you'll manage it for another year if needed.

But here's the opportunity cost framing:

**Every month you delay starting the pilot is a month you're not:**
- Building the toxicity baseline AER will require
- Capturing the $260K/year operational efficiencies
- Discovering the 3-5X upside in chemical savings, fresh water substitution, and capital de-risking
- Creating the institutional memory that survives when senior operators retire

**We have Q2 2026 deployment slots available now.** If this makes strategic sense for CNRL Albian, let's lock in the timeline. If you need more time to evaluate, we respect that—but we want to be transparent about the opportunity window.

### Revised Next Steps

1. **Discovery Call (30 minutes)** - Review historical data availability, site selection (Albian sands?), sampling logistics, grant eligibility
2. **Pilot Proposal Refinement** - Customize scope, pricing, deliverables based on your specific site needs
3. **Grant Application Coordination** - Luminous prepares ERA/Alberta Innovates applications (50% matching); you provide support letter
4. **Agreement Execution** - Pilot Agreement + Terms Addendum (reviewed by your procurement/legal)
5. **Q2 2026 Deployment** - Operational pilot begins with spring thaw (April-May target)

**Timeline to secure Q2 2026 slot:** 6-8 weeks from discovery call to deployment (accounts for grant application, procurement approvals, sample logistics setup)

**Your move:** Let us know if you'd like to schedule the 30-minute discovery call, or if you need additional information first.

---

## Summary of Changes in V1.6 vs. V1.5

**Section 1 (Executive Summary):**
- ✅ Opens with acknowledgment of brilliant research already done (respectful tone)
- ✅ Incorporates OSMWSC regulatory evidence (Sept 2025 urgency, "technology exists today")
- ✅ Frames containment → release as industry transformation (not operator failure)
- ✅ Positions $260K as conservative floor, discovery as 3-5X upside
- ✅ Clarifies Q2 2026 timing as opportunity (ice melt = full season data), not artificial deadline

**Section 2 (The Problem):**
- ✅ Reframed as "Research Excellence → Operational Reality" (not "you're blind")
- ✅ Acknowledges what operators have proven (validates their work)
- ✅ Identifies the gap as cadence shift (research pilots → 24/7 operations), not incompetence
- ✅ Three blind spots clarified with operational consequences (not fear-mongering)

**Section 4 (Validated ROI):**
- ✅ Explicitly states "$260K is the floor, not the ceiling"
- ✅ Shows how we calculated it (reverse-engineering "old way")
- ✅ Breaks out discovery scenarios with conservative estimates (chemical dosing, fresh water, capex de-risking)
- ✅ Explains why we price at cost recovery (partnership bet, not vendor margin)

**Section 5 (Discovery Engine):**
- ✅ Elevated from "Joint Discovery Upside" to equal importance with baseline
- ✅ Three layers explained (Biosensor → Chemistry → Fresh Water)
- ✅ Clarifies what's included vs. upsell (all correlation work is cost recovery)
- ✅ "Institutional memory at speed of thought" positioning (not just "platform feature")

**Section 8 Addition (Data Sharing):**
- ✅ Reframes from competitive advantage to collaborative environmental solution
- ✅ Acknowledges this is shared problem across three operators (not zero-sum game)
- ✅ Explains aggregated insights value (with explicit permission model)
- ✅ Positions transparency as political/regulatory goodwill, not weakness

**Section 9 (Investment & Next Steps):**
- ✅ Q2 2026 framing as opportunity (full-season data) not artificial deadline
- ✅ "Humble Canadian confidence" tone (not "sky is falling")
- ✅ Cost of waiting explained as opportunity cost, not fear tactic
- ✅ Maintains grant matching and cost recovery structure from V1.5

---

**Tone Check:**
- ✅ Respectful of existing research brilliance
- ✅ Partnership language throughout (not vendor-client)
- ✅ "Where have you been all my life" positioning for biosensor (missing operational piece)
- ✅ RCE as amplifying their work (institutional memory), not replacing it
- ✅ Collaborative on data sharing (industry environmental challenge, not competitive)
- ✅ Urgent but humble (opportunity-focused, not panic-driven)

---

**Jeff's Review Questions:**
1. Does Section 1 opening hit the right tone (acknowledge research brilliance → identify operational gap)?
2. Is the $260K "floor vs. ceiling" framing clear in Section 4?
3. Does Section 5 (Discovery Engine) feel like partnership exploration vs. upsell?
4. Is the data sharing section (Section 8 addition) appropriately collaborative without being naive?
5. Does the Q2 2026 timing feel like genuine opportunity vs. artificial pressure?
6. Any language that still feels condescending or "making them feel dumb"?

**Next Step:** Jeff reviews these sections, provides feedback, then we integrate into full V1.6 proposal.
