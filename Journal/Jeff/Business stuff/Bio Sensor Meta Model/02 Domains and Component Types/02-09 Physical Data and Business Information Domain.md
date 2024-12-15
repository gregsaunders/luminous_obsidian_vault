### Physical Data Domain
The physical data domain describes information stored in a format that enables it to be easily processed by a machine. Component types in this domain are commonly persistent stores of structured or semi-structured data (i.e. information whose semantics and values are separated) although increasingly machines are able to process unstructured content as well.

The main component type in this layer is the data store.

**Data Store Component** - A data store is one or more linked tables, files or any other type of structured, persistent dataset without a native user interface or executable business logic and configured for the storage and querying or searching of structured or semi-structured data.

Although a data store may exist as a sub-component of an application here it refers to a free-standing data store such as a data warehouse or operational data store (ODS).

### Business Information Domain
The **business information domain** classifies physical or digital information assets designed primarily to be read by people, such as documents or video. This type of information may be referred to as content or unstructured information. The main concept in this domain is the business artefact.
- **Business Artefact Component** - A **business artefact** is an item of unstructured information like a document, an image or a video or audio file. Traditionally these formats are easily read by humans who can understand their meaning but less easily by machines. However, as machine learning improves unstructured content is increasingly used an input into or output from automated processes.


### Luminous Physical Data Domain

**Data Store Components:**  
1. **Operational Data Store (ODS):**  
   - **Description:** A structured repository holding recent, high-frequency test result data, client information, and remediation recommendations.  
   - **Use Case:** Supports real-time queries, enabling timely updates to client dashboards, rapid SLA verification, and day-to-day operational decision-making.

2. **Data Warehouse:**  
   - **Description:** A centralized, historical repository that aggregates data from the ODS, external lab results, and regulatory benchmarks.  
   - **Use Case:** Powers advanced analytics, long-term trend analysis, predictive modeling, and KPI reporting across multiple clients and test cycles.

3. **Metadata Repository:**  
   - **Description:** Stores definitions, schemas, data lineage, and transformation rules for all information entities.  
   - **Use Case:** Ensures consistent data understanding and governance, facilitating auditability, compliance checks, and improved data quality management.

### Luminous Business Information Domain

**Business Artefacts:**  
1. **Compliance Reports:**  
   - **Format:** PDF or Word documents summarizing test results, compliance status, and recommended remediation steps for clients and regulators.  
   - **Use Case:** Provide easily digestible insights for environmental officers, executives, and stakeholders who need a narrative and visual interpretation of the data.

2. **Technical Documentation & Manuals:**  
   - **Format:** PDF documents, internal wiki pages, or instructional videos guiding clients on sample collection procedures, data portal navigation, and remediation best practices.  
   - **Use Case:** Supports user training, customer onboarding, and ongoing reference, improving service adoption and client self-sufficiency.

3. **Marketing and Thought Leadership Content:**  
   - **Format:** Whitepapers, case studies, and blog posts describing successful remediation strategies, industry best practices, and technology innovations.  
   - **Use Case:** Enhances brand reputation, educates the market, and attracts potential clients by showcasing expertise and successful project outcomes.

By clearly defining the data stores that maintain structured data for operational and analytical purposes, and managing business artefacts that communicate insights and guidance to human users, the company creates a cohesive ecosystem. This integration ensures data-driven decision-making, regulatory compliance, and accessible information assets that support the entire value chain—from testing and analytics to client engagement and remediation strategies.
