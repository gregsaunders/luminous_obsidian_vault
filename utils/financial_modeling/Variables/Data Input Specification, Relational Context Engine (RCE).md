## 🛠️ Data Input Specification: Relational Context Engine (RCE)

### 1. The Immutable Header (Metadata)

Every data packet entering the RCE, whether from a field sensor or a lab bench, must carry a "Standard Identity Wrapper."

- **SourceID:** UUID of the specific sensor or lab station.
    
- **Timestamp:** ISO 8601 UTC format (to sync across different time zones/shifts).
    
- **Geo-Tag:** GPS coordinates of the sampling point (to identify **Stagnation Areas** vs. **Flow Channels**).
    
- **Hash:** A cryptographic checksum (SHA-256) generated at the point of entry to ensure the record is immutable.
    

### 2. Variable Schema & Frequency

The developers need to build a relational database (e.g., PostgreSQL or a Time-Series DB like InfluxDB) that can handle the following 13 variables.

|Category|Variable|Data Type|Source|Unit|Input Frequency|
|---|---|---|---|---|---|
|**Functional**|**Biosensor (Master)**|Float (0.0-1.0)|Lab (Bio-Assay)|% of Control|**Daily**|
|**Forensic**|**Refractory NAs**|JSON / Array|Lab (HRMS)|mg/L (Z-spec)|**Quarterly**|
|**Ionic**|**Salinity (Cl-)**|Float|Sensor (ISE)|mg/L|Hourly|
|**Ionic**|**SAR**|Float|Sensor (Calculated)|Ratio|Hourly|
|**Metabolic**|**Metabolites**|Boolean/Float|Lab (Bio-Assay)|Stress Ind.|**Daily**|
|**Physical**|**Temp (Water)**|Float|Sensor|°C|Hourly|
|**Physical**|**DO (Oxygen)**|Float|Sensor|mg/L|Hourly|
|**Physical**|**pH**|Float|Sensor|0-14|Hourly|
|**Physical**|**Turbidity**|Float|Sensor|NTU|Hourly|
|**Nutrient**|**Nitrogen (N)**|Float|Lab (Auto-analyser)|mg/L|Weekly|
|**Nutrient**|**Phosphorus (P)**|Float|Lab (Auto-analyser)|mg/L|Weekly|
|**Flow**|**Residence Time**|Float|Pump SCADA|Hours/Days|Hourly|
|**Energy**|**UV Irradiance**|Float|Weather Station|W/m2|Hourly|

Export to Sheets

---

## 🏗️ Developer Logic: The "Relational" Requirement

The RCE must do more than store the table above. Developers must build **Correlation Pipelines**.

- **The Decay Relationship:** The engine must link **Variable 1 (UV)** and **Variable 2 (Temp)** to the **Daily Biosensor**result. If UV is high but Biosensor activity is low, the system flags a "System Efficiency Drop" for the operator.
    
- **The Ionic Guardrail:** If **Variable 7 (SAR)** trends toward > 4.0, the engine must trigger a warning that the **Physical Wetland Structure** is at risk, regardless of how "clean" the NAs are.
    
- **Audit Trail:** Every time a threshold is crossed (e.g., a "Red Light" on the Biosensor), the RCE must automatically snapshot all other 12 variables at that exact moment. This creates the "Forensic Proof" for the third-party auditor.
    

---

## 🏢 Operational Protocol: Ensuring Data Quality

For the Oil Sands Operator, the "Garbage In, Garbage Out" rule applies.

1. **Calibration Verification:** Every daily **Biosensor** input must be accompanied by a "Control Validation." The lab tech must input the response of the sensor to a known standard. The RCE will reject the data if the control is out of spec.
    
2. **Sample Chain of Custody:** For **Quarterly HRMS**, the data model must include a "Chain of Custody" field (Digital Signature) to prove the sample taken from the wetland is the same one that reached the high-resolution lab.
    
3. **Flagging Stagnation:** Operators must use the **Geo-Tag** data to identify if certain "cells" in the wetland are underperforming. If the Biosensor shows 0% change over 7 days in "Cell 3," the RCE flags a **Stagnation Risk**.
    

---

## 📄 Auditability Statement for Third Parties

To prove to the **AER** or **Indigenous Communities** that the system is honest, the RCE provides a **"Verification Hash."**

> _"Any stakeholder can take a Quarterly Compliance Report and run the data through a public verification tool. If a single decimal point in the Salt or Biosensor data was changed after the initial entry, the cryptographic hash will break, and the audit will fail."_