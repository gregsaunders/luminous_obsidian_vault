# Contact List Development & Automation Strategy
## GROW Campaign - Luminous BioSolutions

---

## CONTACT LIST TEMPLATE (CSV Format)

### Required Fields:
```
First_Name, Last_Name, Email, Job_Title, Company, Segment, Priority, LinkedIn_URL, Source, Notes, Tags
```

### Field Definitions:

**First_Name**: Contact's first name
**Last_Name**: Contact's last name
**Email**: Primary business email address
**Job_Title**: Current position title
**Company**: Organization name
**Segment**: Choose one:
- `Operator` (Oil sands operators)
- `Academic` (University researchers)
- `Regulatory` (Government/regulatory bodies)
- `Consultant` (Environmental consulting firms)

**Priority**: Choose one:
- `High` (Key decision-makers, direct prospects)
- `Medium` (Influencers, secondary contacts)
- `Low` (General interest, awareness building)

**LinkedIn_URL**: Full LinkedIn profile URL
**Source**: Where you found this contact (e.g., "LinkedIn Search", "GROW Website", "Conference", "Referral")
**Notes**: Any relevant context about this contact
**Tags**: Comma-separated keywords (e.g., "COSIA_Member, Water_Treatment_Lead, Previously_Contacted")

---

## TARGET CONTACT PROFILES BY SEGMENT

### SEGMENT 1: OIL SANDS OPERATORS (Priority: HIGH)

#### Companies to Target:
1. **Imperial Oil Resources**
   - Target Titles: Environmental Manager, Water Treatment Director, Sustainability Lead, R&D Manager, Kearl Operations Manager
   - Why: Actively involved in GROW project, largest oil sands producer

2. **Suncor Energy**
   - Target Titles: Environmental Affairs Manager, Tailings Management Lead, Innovation & Technology Director
   - Why: Major operator, strong focus on innovation

3. **Canadian Natural Resources Limited (CNRL)**
   - Target Titles: Environment & Regulatory Manager, Water Management Specialist, Operations VP
   - Why: Largest producer, extensive tailings management needs

4. **Cenovus Energy**
   - Target Titles: Environmental Technology Manager, Sustainability & Environment VP, Water Resources Lead
   - Why: Focus on environmental technology adoption

5. **MEG Energy**
   - Target Titles: Environmental Manager, Technical Services Manager
   - Why: Smaller operator, potentially more agile for pilot deployments

6. **ConocoPhillips Canada**
   - Target Titles: Environmental Lead, Operations Manager
   - Why: International operator with innovation focus

#### LinkedIn Search Queries:
```
"Environmental Manager" AND "Imperial Oil" AND "Alberta"
"Water Treatment" AND "Suncor" AND "Oil Sands"
"Tailings Management" AND "CNRL"
"Sustainability Director" AND "Cenovus"
"Environmental Technology" AND "Oil Sands" AND "Canada"
```

#### Estimated Contact Count: 25-35 per company = ~150-200 total

---

### SEGMENT 2: ACADEMIC RESEARCHERS (Priority: MEDIUM-HIGH)

#### Institutions:
1. **University of Calgary**
   - Departments: Biological Sciences, Chemical & Petroleum Engineering, Geoscience
   - Key Faculty: Anyone involved in GROW project, environmental microbiology, genomics

2. **University of Saskatchewan**
   - Departments: Civil, Geological & Environmental Engineering, Biology
   - Key Faculty: GROW collaborators, water treatment research

3. **Athabasca University**
   - Departments: Science & Technology
   - Key Faculty: Dr. Lewenza's colleagues, environmental science

4. **University of Alberta**
   - Departments: Civil & Environmental Engineering, Biological Sciences
   - Key Faculty: Oil sands research, wetland ecology

5. **INRS (Institut national de la recherche scientifique) Quebec**
   - GROW project partner

6. **Brock University**
   - GROW project partner, environmental science

7. **Simon Fraser University (SFU)**
   - GROW project partner

#### Data Sources:
- GROW project website (all listed researchers)
- University department directories
- Recent publications on "naphthenic acids", "OSPW", "constructed wetlands", "oil sands remediation"
- ResearchGate, Google Scholar profiles

#### Estimated Contact Count: 50-75 researchers

---

### SEGMENT 3: REGULATORY & GOVERNMENT (Priority: MEDIUM)

#### Organizations:
1. **Alberta Energy Regulator (AER)**
   - Target Titles: Environmental Scientist, Water Quality Specialist, Regulatory Compliance Officer

2. **Environment and Climate Change Canada (ECCC)**
   - Target Titles: Environmental Assessment Officer, Oil Sands Monitoring Scientist, Water Quality Lead
   - Focus: National Hydrology Research Centre (Saskatoon)

3. **Natural Resources Canada (NRCan)**
   - Target Titles: Research Scientist, Oil Sands Program Lead
   - Focus: Laurentian Forestry Centre, Northern Forestry Centre

4. **Alberta Environment and Protected Areas**
   - Target Titles: Water Policy Analyst, Environmental Monitoring Specialist

#### LinkedIn Search Queries:
```
"Alberta Energy Regulator" AND "Environmental"
"Environment Canada" AND "Oil Sands"
"Water Quality" AND "Government of Alberta"
```

#### Estimated Contact Count: 30-40 total

---

### SEGMENT 4: ENVIRONMENTAL CONSULTANTS & ENGINEERING FIRMS (Priority: MEDIUM)

#### Companies:
1. **Golder Associates (WSP)**
2. **Stantec**
3. **AECOM**
4. **Wood PLC**
5. **SNC-Lavalin**
6. **Tetra Tech**
7. **ERM (Environmental Resources Management)**
8. **Intrinsik**

#### Target Titles:
- Environmental Consultant
- Senior Water Resources Engineer
- Oil Sands Practice Lead
- Environmental Assessment Manager
- Wetland Specialist

#### LinkedIn Search Queries:
```
"Environmental Consultant" AND "Stantec" AND "Calgary"
"Water Resources Engineer" AND "Oil Sands"
"Wetland Specialist" AND "AECOM"
```

#### Estimated Contact Count: 40-60 total

---

## AUTOMATION STRATEGIES

### OPTION 1: LinkedIn Sales Navigator + CSV Export

**Tools Needed:**
- LinkedIn Sales Navigator subscription ($99/month)
- Export tool (e.g., Phantombuster, Dux-Soup)

**Process:**
1. Create saved searches for each target profile
2. Use LinkedIn Sales Navigator filters:
   - Geography: Alberta, Canada
   - Current Company: [Target companies]
   - Job Title: [Target titles]
   - Industry: Oil & Gas, Environmental Services, Higher Education
3. Export to CSV using browser extension
4. Clean data and deduplicate
5. Enrich with email finder tools

**Pros**: Most accurate job titles and current companies
**Cons**: Costs ~$100-200/month for tools

---

### OPTION 2: Web Scraping + Email Enrichment

**Tools Needed:**
- Hunter.io (email finding) - $49/month
- LinkedIn profile scraper (Phantombuster) - $30/month
- Or all-in-one: Apollo.io ($49/month)

**Process:**
1. Scrape LinkedIn profiles matching target criteria
2. Use email enrichment API to find business emails
3. Verify emails with validation tool (NeverBounce, ZeroBounce)
4. Import to CRM or email marketing platform

**Pros**: Automated, scalable
**Cons**: Email accuracy ~70-80%

---

### OPTION 3: Manual Research (Free but Time-Intensive)

**Tools Needed:**
- LinkedIn (free account)
- Company websites
- Google search

**Process:**
1. Visit each target company website
2. Navigate to "Team" or "About Us" pages
3. Find relevant team members
4. Search for them on LinkedIn to confirm current role
5. Use email pattern guessing (firstname.lastname@company.com)
6. Verify emails with Hunter.io free tier (50/month)

**Time Investment**: ~15-20 hours for 200-300 contacts
**Pros**: Free, high accuracy
**Cons**: Very time-consuming

---

## RECOMMENDED HYBRID APPROACH

### Phase 1: High-Priority Manual Research (Week 1)
- Manually research top 30-40 HIGH priority contacts (key decision-makers at Imperial, Suncor, CNRL, Cenovus)
- Verify emails using Hunter.io
- Add detailed notes about each contact
- **Time**: 8-10 hours
- **Quality**: 95%+ accuracy

### Phase 2: Automated Medium-Priority (Week 1-2)
- Use LinkedIn Sales Navigator for medium-priority contacts (academics, consultants, regulatory)
- Export and enrich with Apollo.io or Hunter.io
- **Time**: 2-3 hours
- **Cost**: ~$50-100
- **Quality**: 75-85% accuracy

### Phase 3: GROW Attendee List (Week 1)
- Email grow@ucalgary.ca and request:
  - List of GROW symposium attendees (if public)
  - GROW team member contact information (publicly listed on website)
- Add all GROW presenters from seminar schedule
- **Time**: 2 hours
- **Quality**: 100% accuracy (publicly available)

---

## EMAIL ENRICHMENT TOOLS COMPARISON

| Tool | Cost/Month | Emails/Month | Accuracy | Best For |
|------|-----------|--------------|----------|----------|
| Hunter.io | $49 | 500 | 85% | Small lists, email verification |
| Apollo.io | $49 | 2,000 | 80% | Large lists, all-in-one platform |
| LinkedIn Sales Nav | $99 | Unlimited | N/A | Finding contacts, no emails |
| Lusha | $29 | 80 | 90% | High accuracy, small volume |
| ZoomInfo | $15,000/year | Unlimited | 95% | Enterprise, very expensive |

**Recommendation for this campaign**: Hunter.io ($49) + LinkedIn Sales Navigator ($99) = $150/month for 1 month

---

## CONTACT LIST BUILD TIMELINE

### Week of January 20-24:
- [ ] Set up Hunter.io account
- [ ] Set up LinkedIn Sales Navigator (7-day free trial available)
- [ ] Create master spreadsheet template
- [ ] Research and manually add top 30 HIGH priority oil sands operator contacts

### Week of January 27-31:
- [ ] Use Sales Navigator to find academic researchers (GROW participants)
- [ ] Export and enrich consultant/engineering firm contacts
- [ ] Research regulatory contacts (AER, ECCC, NRCan)
- [ ] Deduplicate and clean all data

### Week of February 3:
- [ ] Final verification of all emails
- [ ] Upload to email marketing platform (Mailchimp, HubSpot, etc.)
- [ ] Create audience segments
- [ ] Launch Email #1

---

## EMAIL MARKETING PLATFORM SETUP

### Recommended Platforms:

**Option 1: Mailchimp (Free up to 500 contacts)**
- Pros: Easy to use, good templates, free tier
- Cons: Limited automation on free plan
- Cost: Free for <500 contacts

**Option 2: HubSpot (Free CRM + Email)**
- Pros: Full CRM, unlimited contacts, automation
- Cons: Steeper learning curve
- Cost: Free

**Option 3: Constant Contact ($12/month)**
- Pros: Great for events, easy RSVP tracking
- Cons: Less CRM functionality
- Cost: $12/month

**Recommendation**: Start with HubSpot Free CRM
- Upload contact list
- Create custom properties for: Segment, Priority, Event Registration Status
- Set up email campaigns
- Track opens, clicks, registrations
- Free forever, upgrade later if needed

---

## SAMPLE CONTACT LIST (First 10 Entries)

```csv
First_Name,Last_Name,Email,Job_Title,Company,Segment,Priority,LinkedIn_URL,Source,Notes,Tags
John,Smith,john.smith@imperial.com,Environmental Manager,Imperial Oil,Operator,High,linkedin.com/in/johnsmith,LinkedIn Sales Nav,Kearl operations focus,COSIA_Member
Sarah,Johnson,sarah.johnson@suncor.com,Water Treatment Director,Suncor Energy,Operator,High,linkedin.com/in/sarahjohnson,Company Website,Spoke at conference 2024,Innovation_Lead
Dr. Doug,Muench,dmuench@ucalgary.ca,Professor,University of Calgary,Academic,High,linkedin.com/in/dougmuench,GROW Website,GROW co-lead,GROW_Team
Emily,Chen,emily.chen@cnrl.com,Sustainability Lead,Canadian Natural Resources,Operator,High,linkedin.com/in/emilychen,LinkedIn Sales Nav,Reports to VP Environment,Key_Decision_Maker
Michael,Brown,mbrown@aer.ca,Senior Environmental Scientist,Alberta Energy Regulator,Regulatory,Medium,linkedin.com/in/michaelbrown,Government Directory,Oil sands oversight,Regulatory_Contact
Dr. Lisa,Gieg,lgieg@ucalgary.ca,Professor,University of Calgary,Academic,High,lgieg@ucalgary.ca,GROW Website,GROW team member,GROW_Team
James,Wilson,james.wilson@stantec.com,Senior Water Resources Engineer,Stantec,Consultant,Medium,linkedin.com/in/jameswilson,LinkedIn Sales Nav,Calgary office,Wetland_Specialist
Christine,Martineau,christine.martineau@nrcan-rncan.gc.ca,Research Scientist,Natural Resources Canada,Regulatory,High,linkedin.com/in/christinemartineau,GROW Website,GROW co-lead,GROW_Team
David,Lee,david.lee@cenovus.com,Environmental Technology Manager,Cenovus Energy,Operator,High,linkedin.com/in/davidlee,LinkedIn Sales Nav,Innovation budget holder,Pilot_Prospect
Anna,Martinez,anna.martinez@ec.gc.ca,Oil Sands Monitoring Lead,Environment Canada,Regulatory,Medium,linkedin.com/in/annamartinez,Government Website,ECCC National Hydrology,Regulatory_Contact
```

---

## GDPR / CASL COMPLIANCE

### Canada's Anti-Spam Legislation (CASL) Requirements:

✅ **Consent**:
- Implied consent: If you have existing business relationship OR contact requested information
- Express consent: For cold contacts, include clear opt-in language

✅ **Identification**:
- Clearly identify Luminous BioSolutions as sender
- Include physical mailing address in footer

✅ **Unsubscribe**:
- Easy, one-click unsubscribe in every email
- Honor unsubscribe requests within 10 business days

**Safe Approach for This Campaign**:
- All contacts have professional relationship to oil sands/OSPW (relevant business interest)
- Offering valuable educational content (GROW presentation)
- Clear unsubscribe in every email
- Not selling products directly (informational/educational)

This likely qualifies for implied consent, but include unsubscribe to be safe.

---

## TRACKING & MEASUREMENT

### Metrics to Track in Spreadsheet:
- Email 1 sent: Y/N
- Email 1 opened: Y/N
- Email 1 clicked: Y/N
- Email 2 sent: Y/N
- Email 2 opened: Y/N
- (etc. for all 4 emails)
- Registered for presentation: Y/N
- Attended presentation: Y/N
- Post-event follow-up: Y/N
- Demo requested: Y/N

### CRM Automation (if using HubSpot):
- Automatically add tag "Opened Email 1" when opened
- Move to "Engaged" list if clicked any email
- Move to "Hot Lead" if registered for presentation
- Trigger post-event email sequence automatically

---

## NEXT STEPS CHECKLIST

- [ ] Decide on contact list building approach (hybrid recommended)
- [ ] Budget approval for tools ($150 for 1 month)
- [ ] Assign team member to contact list building (10-15 hours total)
- [ ] Set up HubSpot Free CRM account
- [ ] Create master contact spreadsheet template
- [ ] Begin Phase 1: High-priority manual research
- [ ] Set target: 250-350 total contacts by February 1

---

**Questions? Need help with specific tools or automation? Let me know!**
