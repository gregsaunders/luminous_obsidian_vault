### Variable 14: Precipitation & Evapotranspiration (The Water Balance)

In an engineered wetland, the **Water Balance** determines the concentration of everything else. It is the denominator in all your math.

#### 1. The Heavy Rain Event (The "Flush" Risk)

- **The Impact:** A massive rain event causes a sudden surge in water volume.
    
- **The Problem:** This dramatically reduces **Residence Time (Variable 8)**. Water is pushed through the channels faster than the bacteria can process it.
    
- **The Forensic Shift:** Rain also introduces "Fresh" runoff from the surrounding landscape, which can spike **Turbidity (Variable 5)**, blocking the **Sun (Variable 1)**.
    
- **RCE Response:** The engine sees the flow-rate increase and the dilution of **Salinity**. However, if the **Daily Biosensor** shows that the water hasn't been "cleaned" yet, the RCE triggers the **Gate-Keep** to stop discharge, forcing the water into temporary storage until the microbes catch up.
    

#### 2. The Hot Dry Summer (The "Evaporation" Risk)

- **The Impact:** High heat leads to **Evapotranspiration** (water lost through plant leaves and the surface).
    
- **The Problem:** As water leaves, the toxins stay behind. **Salinity (Variable 6)** and **Naphthenic Acids** become highly concentrated.
    
- **The Ionic Wall:** This can push the **SAR (Variable 7)** past the "Green Light" threshold of 4.0.
    
- **RCE Response:** The engine flags a "Toxicity Concentration" warning. It may recommend adding "Makeup Water" (fresh runoff) to the system to bring the ion balance back to a range where the plants and biosensors can function.
    

---

### The -30°C Cold Snap: A System Stress Test

When Northern Alberta hits -30°C, the "Bio-engine" doesn't just slow down; it prepares for a freeze-out.

|Variable|-30°C Cold Snap Impact|RCE & Operational Reaction|
|---|---|---|
|**Variable 2: Temp**|Water temp drops toward 0°C.|**Biological Shutdown:** The Daily Biosensor will report near-zero activity.|
|**Variable 4: Oxygen**|Ice cover prevents atmospheric gas exchange.|**Anoxia Risk:** The system shifts from aerobic to anaerobic. Decomposition slows by 90%+.|
|**Variable 14: Snow**|Heavy snow provides **insulation**.|**The Silver Lining:** A thick snow layer can actually keep the water underneath from freezing solid, allowing a "trickle" of treatment to continue.|
|**Cost Model**|Energy costs spike.|Pumps must work harder to prevent line freezing; heat tracing may be required.|

Export to Sheets

**The RCE Decision:** During a cold snap, the RCE identifies that **"Safe-to-Release" thresholds cannot be met.** It automatically shifts the system to **"Storage Mode."** Water is held in the wetland cells throughout the winter, essentially using the season as one long **Residence Time** event, preparing for a "Spring Cleaning" once the ice thaws.

---

### Integrating Precipitation into the Data Model

For your developers and the RCE, Precipitation is a **Dynamic Multiplier**.

- **Positive Multiplier (Rain):** Decreases Salinity/SAR but increases the risk of "Short-Circuiting" (water moving too fast).
    
- **Negative Multiplier (Dry Heat):** Increases the effectiveness of **UV Photolysis** (Variable 1) but increases the risk of "Salt Loading" that can kill the wetland plants.
    

### Impact on the Financial Model

1. **CAPEX (Storage):** You must build enough "freeboard" (extra depth) into your wetland to hold a "1-in-100 year" rain event without overflowing untreated water.
    
2. **OPEX (Seasonal Pumping):** You must budget for high energy use in the winter (pumping to prevent freezing) and potential "Water Acquisition" costs in a severe drought to keep the plants alive.
    

### Does this complete the "Pre-FEED" Library?

You have now addressed the "Climate Reality" of the North. You have a system that doesn't just work in a lab, but accounts for the wild swings of the Alberta seasons.