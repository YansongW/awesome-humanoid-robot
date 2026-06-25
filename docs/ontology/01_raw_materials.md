# 01 Raw Materials & Critical Resources

> **Domain Code**: `01_raw_materials`  
> **Layer**: Upstream  
> **Status**: Draft — subject to review before v0.1.0  
> **Purpose**: Define the raw-material and critical-resource concepts that flow into humanoid robot components, and establish how this domain links to the rest of the value chain.

---

## 1. Central Question

> **What physical substances are required to build a humanoid robot, where do they come from, and what supply risks do they carry?**

Humanoid robots are material-intensive systems. A production-scale fleet amplifies small per-unit material demands into large, concentrated exposures in minerals, metals, magnets, and polymers. This domain tracks the upstream inputs before they become components.

---

## 2. Scope

### 2.1 In Scope

- Critical minerals and rare-earth elements used in motors, batteries, sensors, and electronics.
- Base metals and alloys for structural and conductive parts.
- High-performance polymers, composites, and ceramics for lightweighting and tribology.
- Semiconductor-grade silicon, gallium, germanium, and related materials.
- Material supply-chain concentration, price volatility, and geopolitical risk.
- Recycling, secondary supply, and substitution pathways.

### 2.2 Out of Scope

- Finished components (covered in `02_components_supply_chain`).
- Manufacturing processes that transform raw materials (covered in `03_manufacturing_processes`).
- General commodity materials with no identified humanoid-robot relevance.

---

## 3. Key Concepts

### 3.1 Magnet Rare Earths

High-torque-density electric motors in humanoid joints rely on permanent-magnet synchronous machines, most commonly using **neodymium-iron-boron (NdFeB)** magnets. Key elements:

| Element | Role in NdFeB | Humanoid Relevance |
|---------|---------------|--------------------|
| Neodymium (Nd) / Praseodymium (Pr) | Base alloy (often combined as NdPr) | Provides high remanence and energy product |
| Dysprosium (Dy) | Heavy rare-earth additive | Improves high-temperature coercivity |
| Terbium (Tb) | Heavy rare-earth additive | Further coercivity enhancement at elevated temperatures |

**Sources and evidence**:
- The International Energy Agency (IEA) reports that magnet rare-earth elements (Nd, Pr, Dy, Tb) have seen demand double since 2015 and are set to expand by another third by 2030 under current policies, driven by electrification, automation, and robotics [IEA Rare Earth Elements 2026].
- NdFeB permanent magnets account for around 95% of total rare-earth consumption by value and underpin EV motors, wind turbines, industrial motors, robotics, and AI data centers [IEA Rare Earth Elements 2026].
- China controls the majority of global rare-earth processing capacity; export controls on Dy and Tb introduced in 2023–2025 create direct cost and availability risks for high-coercivity magnet grades [TDK Rare Earth Magnets analysis; Rare Earth Exchanges 2026].

### 3.2 Battery Materials

Current humanoid robots predominantly use lithium-ion cells derived from EV battery technology. Common cathode families include:

| Chemistry | Key Elements | Characteristics |
|-----------|--------------|-----------------|
| LFP (LiFePO₄) | Lithium, iron, phosphate | Safer, lower energy density (~90–160 Wh/kg cell) |
| NMC / NCA | Lithium, nickel, cobalt, manganese/aluminum | Higher energy density (~200–260 Wh/kg cell) |
| Solid-state (emerging) | Lithium, sulfur/oxide electrolytes | Potential >300–500 Wh/kg, improved safety |

**Sources and evidence**:
- A Fraunhofer IPA whitepaper notes that off-the-shelf Li-ion cells used in humanoids (LFP, NMC, NCA) offer ~200 Wh/kg, sufficient for demonstration but insufficient for many industrial use cases; solid-state batteries could exceed 500 Wh/kg [Fraunhofer IPA 2026].
- Industry analysis indicates Tesla Optimus Gen-2 uses a 2.3 kWh battery pack with roughly two hours of dynamic runtime, while Unitree H1 uses an 864 Wh pack [Interact Analysis 2026].
- The U.S. Department of Energy has set long-term targets for cobalt- and nickel-free cathodes and solid-state/Li-metal batteries achieving 500 Wh/kg and <$60/kWh production cost [BTBU-ECOSF report].

### 3.3 Structural and Lightweight Materials

Humanoid robots require high specific strength, fatigue resistance, and manufacturability. Common families:

| Material | Typical Application | Notes |
|----------|---------------------|-------|
| Aluminum alloys | Frames, housings, brackets | Balance of weight, cost, and machinability |
| Magnesium alloys | Lightweight structural parts | Lower density than aluminum; corrosion and cost challenges |
| Carbon-fiber composites | Limb links, torso panels | High stiffness-to-weight; higher cost and cycle time |
| PEEK (polyether ether ketone) | Gears, bearings, bushings, structural brackets | High specific strength, wear resistance, thermal stability; emerging metal replacement |
| Steel / titanium | High-load joints, fasteners | Strength and durability |

**Sources and evidence**:
- IDTechEx identifies high-performance materials (including PEEK, magnesium alloys, carbon-fiber composites, and ultra-high-molecular-weight polyethylene) as a tracked component category in humanoid robot hardware [IDTechEx Humanoid Robots 2025].
- Multiple industry analyses report that Tesla Optimus Gen-2 achieved ~10 kg weight reduction partly through PEEK use in joints and structural parts; estimates of PEEK usage per humanoid robot range from ~6.6 kg [industry estimates cited in Shunhan Plastics 2026; PEEKChina 2025].
- PEEK bearing grades (e.g., KT820SL30) incorporate PTFE/graphite solid lubricants and are used in dry-running joint applications; carbon-fiber-filled PEEK is reported to achieve structural performance approaching aerospace aluminum at roughly half the weight [Shunhan Plastics 2026].

### 3.4 Semiconductor and Sensor Materials

- **Silicon (Si)**: Compute chips, image sensors, MEMS.
- **Gallium (Ga) / Germanium (Ge)**: Power electronics, photonics, high-frequency devices.
- **Copper (Cu)**: Windings, wiring harnesses, busbars.
- **Platinum-group metals / specialty alloys**: Force/torque sensor strain elements, high-reliability contacts.

---

## 4. Supply-Risk Categories

| Risk Type | Description | Example |
|-----------|-------------|---------|
| Geographic concentration | Processing or mining concentrated in one region | China ~90% of rare-earth magnet manufacturing and heavy-REE processing |
| Co-product dependency | Element produced as by-product of another | Dysprosium/terbium tied to ionic clay REE mining |
| Price volatility | Sharp price swings affect BOM cost | Nd, Dy, Tb price spikes during export-control periods |
| Substitution difficulty | Limited technically viable material replacements | NdFeB for compact high-torque motors |
| Regulatory restriction | Export controls or sanctions | China 2024–2025 REE/magnet export licensing |

---

## 5. Relationship Patterns to Other Domains

| From | To | Relationship | Rationale |
|------|-----|--------------|-----------|
| `01_raw_materials` | `02_components_supply_chain` | `supplies` / `consumed_by` | Rare-earth magnets → servo motors; lithium → battery packs; aluminum/PEEK → structural parts |
| `01_raw_materials` | `03_manufacturing_processes` | `processed_by` | Ore → separated oxides → magnet powder; ingot → CNC machined part |
| `01_raw_materials` | `05_mass_production` | `constrains` | Material availability and cost determine production ramp feasibility |
| `01_raw_materials` | `06_design_engineering` | `constrains` / `enables` | Material density and strength shape morphology; magnet energy product limits motor size |
| `01_raw_materials` | `11_applications_markets` | `drives_cost_of` | Material cost affects end-user price and application economics |
| `01_raw_materials` | `12_policy_regulation_ethics` | `is_regulated_by` | Export controls, conflict-mineral rules, critical-minerals strategies |

---

## 6. Controlled Vocabulary

### 6.1 Material Categories

- `rare_earth_element`
- `permanent_magnet_material`
- `battery_cathode_material`
- `battery_anode_material`
- `electrolyte_material`
- `lightweight_metal`
- `structural_polymer`
- `fiber_reinforced_composite`
- `semiconductor_material`
- `conductive_metal`

### 6.2 Relevant Entity Types

From the project information model:

- `material`
- `component` (when discussing intermediate processed forms)
- `market_segment`
- `policy`

---

## 7. Key Sources

### 7.1 Primary / Authoritative Sources

1. **International Energy Agency (IEA)**. *Rare Earth Elements* (2026). Executive summary notes magnet REE demand doubling since 2015 and NdFeB magnets accounting for ~95% of REE consumption by value.  
   URL: https://www.iea.org/reports/rare-earth-elements/executive-summary

2. **Fraunhofer IPA**. *The Humanoid Hardware Value Chain* (2026). Assesses tactile sensors, electric motors, reducers, batteries; notes Li-ion ~200 Wh/kg and solid-state >500 Wh/kg potential.  
   URL: https://www.ipa.fraunhofer.de/content/dam/ipa/de/documents/Publikationen/Studien/260219_Humanoid_Value_Chain_final.pdf

3. **IDTechEx**. *Humanoid Robots 2025-2035: Technologies, Markets and Opportunities* (2025). Covers actuators, motors, reducers, sensors, batteries, high-performance materials, and market forecasts.  
   URL: https://www.idtechex.com/en/research-report/humanoid-robots/1093

### 7.2 Industry and Market Analysis

4. **Interact Analysis**. *Humanoid Robots and Lithium-Ion Batteries* (2026). Compares Optimus and Unitree H1 battery configurations; discusses NCM/NCA dominance and solid-state pilots.  
   URL: https://interactanalysis.com/insight/humanoid-robots-and-lithium-ion-batteries/

5. **Research and Markets / Embodied AI and Humanoid Robot Market Research 2024-2025**. Supply-chain and component outlook including actuators, sensors, battery, materials.  
   URL: https://www.researchandmarkets.com/reports/6078204/embodied-ai-humanoid-robot-market-research

### 7.3 Material-Specific Sources

6. **Shunhan Plastics**. *PI vs. PEEK in Humanoid Robots* (2026). PEEK properties, grades (KT820SL30, KT820CF30), and reported weight/speed benefits in humanoid trials.  
   URL: https://www.shunhanplastics.com/blogs/article/pi-vs-peek-in-humanoid-robots-which-high-performance-plastic-powers-the-future-of-robotics

7. **PEEKChina**. *Why PEEK is the Key Material for Tesla's Humanoid Robot Optimus-Gen2?* (2025). Industry estimate of ~6.6 kg PEEK per humanoid robot.  
   URL: https://www.peekchina.com/blog/key-material-for-humanoid-robots-peek-polymer.html

8. **Rare Earth Exchanges / e-VAC**. *America's Rare Earth Magnet Industry Reawakening* (2026). Discusses U.S. import dependence and global magnet demand projections.  
   URL: https://rareearthexchanges.com/news/e-vac-goes-live-americas-rare-earth-magnet-industry-reawakening/

---

## 8. Open Questions

1. What is the per-unit material mass breakdown for a representative humanoid robot BOM (e.g., Tesla Optimus, Unitree H1, Figure 02) with primary-source verification?
2. How will material demand scale with production volume, and what recycling infrastructure is needed to close the loop?
3. Which rare-earth reduction or substitution strategies (e.g., ferrite-assisted designs, synchronous reluctance motors, SmCo alternatives) are viable for humanoid actuators?
4. How should the ontology represent material-grade variations (e.g., N35 vs. N52 NdFeB, 6061 vs. 7075 aluminum) and their performance trade-offs?
