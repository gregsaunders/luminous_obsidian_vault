# CDL Technical Assessment: Team Strategy Cheat Sheet

**Goal:** Demonstrate that our pivot to monitoring is a mature, market-driven decision and our technology is ready for pilot deployment with CDL's help.

**Core Message:** The technology is proven, the market need is urgent, and the regulatory timing is perfect. We need CDL's network to secure the initial pilot projects that will unlock commercial scale.

---

### **Part 1: The Opening & Pivot Narrative (Jeff)**

*   **Opening Statement (First 60 Seconds):**
    > "Luminous is a monitoring and data intelligence company solving the critical data-time gap preventing effective tailings water management. The industry is shifting toward regulated release, but you can't manage treatment processes with data that's weeks old. We provide 24-hour operational intelligence that makes this transition possible."

*   **The Pivot Narrative (When Asked About Bioaugmentation):**
    > "Bioaugmentation remains our long-term vision. However, engaging with operators revealed a universal, urgent pain point: they're flying blind with weeks-old data. We realized the most valuable thing we could do is solve that monitoring bottleneck first. Our biosensor and data platform are at higher TRL and address this critical need. This is the foundational step required for any treatment technology—including our future bioaugmentation—to succeed."

---

### **Part 2: Core Data & Platform Talking Points**

*   **The Data Gap Problem (Jeff):** Sets the context that regulated release requires process control, which is impossible with the multi-week turnaround and high cost of HRMS. The industry needs operational data.

*   **Platform Performance (Shawn):** Delivers the core scientific validation.
    *   **Peer-Reviewed:** Lead with the *ACS Synthetic Biology* publication.
    *   **Data Points:** Provide the hard numbers: 24-hour results, detection limits of 2-30 mg/L, successful detection in 22/24 raw OSPW samples, and strong correlation with Orbitrap MS (R-values up to -0.99) in controlled studies.

*   **Deployment & Platform (Greg):** Connects the science to practical application.
    *   **Field Results:** Mention the large-scale pilot where you tracked NA reduction from ~70mg/L to <40mg/L.
    *   **The Platform:** Explain that Confluent solves the "spreadsheet hell" with a modern architecture, REST API for LIMS integration, and an immutable log for a full audit trail.

---

### **Part 3: Critical Q&A Responses (By Role)**

*   **Technical Questions (Shawn Leads):**
    *   **On Interference:** "That's a key research area. Preliminary studies show consistent performance in target matrices, which are often less complex than raw tailings. Our biological mechanism provides specificity advantages over chemical methods. Further interference validation across water types is a priority R&D objective."
    *   **On Calibration:** "We use matrix-matched calibration with actual OSPW extracts, not commercial standards. Our ACS paper demonstrates this approach with strong MS correlation."

*   **Commercial Questions (Jeff Leads):**
    *   **On Customers:** "We're pre-customer by strategic design. The regulatory environment just shifted—OSMWSC recommended pilot projects in September. Operators need field validation before commitment. CDL's network is crucial for securing these foundational pilots."
    *   **On HRMS Competition:** "We complement, not compete. HRMS is essential for final compliance. We provide the 99 operational data points that give you confidence in the 1 data point you send to the regulator."

*   **Platform Questions (Greg Leads):**
    *   **On Confluent:** "It’s a modern data hub designed to solve the 'spreadsheet problem.' It uses a REST API for LIMS integration, offers CSV export, and has an immutable, timestamped logging system for a full audit trail. It's built on TerminusDB to handle complex environmental data relationships."

---

### **Part 4: Role-Specific Reminders**

*   **JEFF (COO - Market & Strategy):** Your role is to frame the narrative. Open with the market problem, handle all business model questions, and close by clearly stating the value of CDL to your commercialization plan.

*   **SHAWN (CSO - Scientific Validation):** Your role is to be the credible scientific authority. Lead with your peer-reviewed data, handle all technical performance questions, and answer honestly about limitations. Mention your decade of focus on this specific problem.

*   **GREG (CTO - Technical Implementation):** Your role is to provide confidence in the execution and scalability of the technology. Speak to the data platform, integration, and the robust architecture designed for complex environmental data.