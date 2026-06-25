# 05 Mass Production & Scaling

> **Domain Code**: `05_mass_production`  
> **Layer**: Midstream  
> **Status**: Draft — subject to review before v0.1.0  
> **Purpose**: Define the factory design, production ramp, supply-chain coordination, yield control, and unit-economics concepts that turn a working humanoid robot prototype into a scalable product.

---

## 1. Central Question

> **What does it take to go from one working humanoid robot to thousands or millions of units, reliably and at viable cost?**

Mass production is the bridge between a validated prototype and an economically deployable product. It is where design choices, component availability, assembly discipline, test coverage, and logistics converge. For humanoid robots, this domain is especially critical because the industry is moving from hand-built prototypes to dedicated factories while many component supply chains are still immature.

---

## 2. Scope

### 2.1 In Scope

- Factory layout, line design, and capacity planning for humanoid robot production.
- Production ramp strategies, cycle-time optimization, and yield management.
- Supply-chain coordination, vertical-integration decisions, and tier-1/tier-2 supplier qualification.
- Manufacturing execution systems (MES), product lifecycle management (PLM), ERP, and warehouse management systems (WMS) for robot production.
- End-of-line (EOL) testing, burn-in, reliability screening, and quality traceability.
- Unit economics, bill-of-materials (BOM) cost reduction, learning curves, and design-for-manufacturability (DFM) feedback loops.
- Workforce planning and human-robot collaboration on the production line.

### 2.2 Out of Scope

- Component-level design and performance (covered in `02_components_supply_chain`).
- Individual manufacturing processes such as CNC machining or injection molding (covered in `03_manufacturing_processes`).
- Subsystem assembly, calibration, and integration test benches (covered in `04_assembly_integration_testing`).
- General economic forecasting not tied to production scaling decisions.

---

## 3. Key Concepts

### 3.1 Factory Design and Production Ramp

Humanoid robot factories are being built with a wide range of strategies, from vertically integrated in-house facilities to modular, CapEx-light assembly plants.

| Model | Example | Design Rationale | Reported Scale |
|-------|---------|------------------|----------------|
| Vertically integrated, in-house | Figure AI BotQ (California) | Control quality, iteration speed, and IP; custom MES and PLM | Initial line: ~12,000 robots/year; target 100,000 over four years [Figure 2025; Figure 2026] |
| CapEx-light modular assembly | Agility Robotics RoboFab (Oregon) | Avoid heavy industrial machinery; work-cell architecture allows rapid expansion | Peak capacity: 10,000 robots/year; first-year output in the hundreds [Agility 2025] |
| Regional ecosystem/pilot line | Shenzhen/Leju Robotics Roban 2 line | Validate process stability before mass transfer; leverage local supplier base | Pilot: 500–1,000/year; mass line: >10,000/year, one unit every 30 minutes [Shenzhen Gov 2026] |
| Automotive-style mega-factory | Tesla Optimus lines (Fremont/Giga Texas) | Repurpose EV production expertise; target consumer-scale volumes | Fremont target: 1M/year; Giga Texas target: 10M/year [Tesla 2026] |

**Sources and evidence**:
- Figure AI reports that its BotQ facility was built from the ground up for high-volume manufacturing, with dedicated lines for actuators, batteries, sensors, structures, and electronics, and an internally developed MES [Figure 2025].
- In April 2026, Figure announced it had increased Figure 03 throughput from one robot per day to one per hour in under 120 days, with end-of-line first-pass yield exceeding 80% and battery-line yield at 99.3% [Figure 2026].
- Agility Robotics describes RoboFab as a CapEx-light assembly facility with modular work cells for legs, arms, torsos, and actuators, designed to produce each sub-assembly in roughly the same amount of time [Agility 2025].
- UBTECH's 2025 annual report discloses 1,079 full-size humanoid units sold and annualized production capacity exceeding 6,000 units, with full-size humanoid revenue reaching RMB 820.6 million [UBTECH 2026].
- **Speculative note**: Tesla's 10-million-unit annual target for Giga Texas is widely reported as aspirational. Independent analysts suggest 2–5 million units/year by 2027 may be more realistic, given construction permits and supply-chain qualification timelines [Tesla 2026].

### 3.2 Supply-Chain Coordination and Vertical Integration

Because a mature tiered supply chain for humanoid robots does not yet exist, OEMs must decide which subsystems to build in-house and which to source from external vendors.

| Decision Axis | In-House (Vertical Integration) | External Sourcing |
|---------------|---------------------------------|-------------------|
| Rationale | Control IP, quality, iteration speed, and margin | Access existing scale, avoid capital intensity, leverage supplier expertise |
| Typical modules | Actuators, hands, battery packs, software stack | Fasteners, bearings, commodity electronics, certain castings/stampings |
| Risks | Capital intensity, talent scarcity, slower supplier learning | Supply qualification time, yield variability, geopolitical/export-control exposure |

**Sources and evidence**:
- Figure AI states it vertically integrates core module builds including actuators, batteries, sensors, structures, and electronics, while partnering strategically with component suppliers capable of meeting volume and quality targets [Figure 2025].
- Jabil, a contract manufacturer working with Apptronik on the Apollo humanoid, notes that humanoid supply chains are at the stage AMR/AGV supply chains were 15–20 years ago: key components are still expensive because volumes are low and supply chains are still forming [Jabil 2026].
- Tesla's 2025 production ramp was reportedly constrained by China's April 2025 export restrictions on NdFeB magnets, illustrating how upstream material policy directly disrupts mass-production plans [Tesla 2026].

### 3.3 Yield, Quality Control, and End-of-Line Testing

At low volumes, hand tuning and manual rework can mask quality problems. At scale, consistent yield requires in-process inspection, automated test stations, and full component traceability.

| Quality Layer | Purpose | Examples |
|---------------|---------|----------|
| Incoming inspection | Reject out-of-spec components before they enter assembly | Dimensional checks on gears, magnet grades, winding resistance |
| In-process inspection | Catch defects at the sub-assembly stage | Grease dispense verification, backlash measurement, torque-ripple checks |
| End-of-line (EOL) testing | Verify full-robot function before shipment | Joint range-of-motion, burn-in (squats, jogging), sensor calibration, safety-stop verification |
| Field traceability | Link failures back to production lots | MES genealogy, serialized component records, OTA diagnostic feedback |

**Sources and evidence**:
- Figure AI reports more than 50 in-process inspection points, over 80 functional verification tests per robot, and burn-in sessions where robots perform squats, shoulder presses, and jogging at cycle counts in the thousands [Figure 2026].
- EngineAI's Shenzhen base reports 79 full-dimensional quality inspections and 46 working-condition simulation tests per robot before delivery, plus full-link digital traceability [EngineAI 2026].
- EYOU Robot Technology's automated joint production line is reported to achieve first-pass yield exceeding 95% through automation and standardization [EYOU 2026; Global Times 2026].
- Automated frameless torque motor assembly lines are emerging with cycle times around 180 s/pc, quality rates ≥99%, and MES connectivity for traceability.

### 3.4 Unit Economics and BOM Cost Reduction

The cost structure of early humanoid robots is dominated by low-volume components, manual assembly, and high rework rates. Mass production aims to drive costs down through learning curves, process tooling, and design simplification.

| Cost Driver | Early-Stage Impact | Scale Mitigation |
|-------------|--------------------|------------------|
| Actuators / joints | Often 40–55% of BOM cost at low volume [DBS/TrendForce via ResearchWise 2025] | Automated winding, die-casting, stamping, and standardized integrated joint modules |
| Dexterous hands | Complex micro-actuators and cabling; high labor content | Tooling, injection molding, metal injection molding |
| Manual assembly and rework | High labor hours per unit; inconsistent quality | Line balancing, fixture automation, test automation |
| Low-volume tooling amortization | High per-unit depreciation | Higher volumes spread mold/fixture costs |

**Sources and evidence**:
- Goldman Sachs revised its 2035 humanoid robot market estimate upward from $6 billion to $38 billion, citing 40% year-over-year manufacturing-cost declines and component cost reductions that brought high-end robot production costs from $50,000–$250,000 to roughly $30,000–$150,000 [Goldman Sachs via BardAI 2024; CircuitNet 2024].
- Figure AI switched from CNC-from-billet prototyping for Figure 02 to tooled processes such as injection molding, die-casting, and stamping for Figure 03, reporting that parts previously requiring over a week on a CNC machine can now be made in under 20 seconds with complex steel molds [Figure 2025].
- DBS/TrendForce analysis estimates the "movement plane" (actuation and transmission) accounts for about 55% of humanoid robot BOM cost, with Chinese domestic suppliers already providing roughly 90% of that category's cost contribution in China-built robots [ResearchWise 2025].
- **Speculative note**: Tesla's stated target of a $20,000–$30,000 consumer price for Optimus is a company target contingent on multi-million-unit annual volumes and should be treated as forward-looking [Tesla 2026].

### 3.5 Manufacturing Systems and Workforce

Scaling production requires more than hardware: it requires software infrastructure for planning, execution, and traceability, plus a workforce with cross-functional skills in robotics, automation, and quality systems.

| System | Role in Mass Production | Relevance to Humanoids |
|--------|-------------------------|------------------------|
| MES (Manufacturing Execution System) | Real-time production tracking, genealogy, test-data collection | Custom MES common because off-the-shelf systems lack humanoid-specific processes |
| PLM / ERP / WMS | Design change control, procurement, inventory, outbound logistics | Critical for multi-SKU actuator management and rapid design iteration |
| Digital twin / simulation | Line layout, throughput optimization, offline programming | Reduces commissioning time and validates human-robot work cells |
| Workforce | Assembly technicians, manufacturing engineers, quality engineers, automation specialists | Shortage of cross-functional "AI + manufacturing" engineers is widely cited as a scaling bottleneck |

**Sources and evidence**:
- Figure AI explicitly calls its internally built MES "the backbone" of BotQ, integrating supply-chain tracking, assembly efficiency monitoring, and stringent quality control [Figure 2025].
- Safety standards ISO 10218-1/2 and ISO/TS 15066 define power/force limiting, speed/separation monitoring, and risk-assessment requirements for collaborative robot systems, which govern how humanoid robots can be integrated into shared production cells [Universal Robots 2018; A3 2016].

---

## 4. Relationship Patterns to Other Domains

| From | To | Relationship | Rationale |
|------|-----|--------------|-----------|
| `05_mass_production` | `02_components_supply_chain` | `consumes` / `sources_from` | Factories consume actuators, sensors, batteries, and structural parts; supplier qualification determines ramp speed. |
| `05_mass_production` | `03_manufacturing_processes` | `is_based_on` / `uses` | Mass production scales up specific processes (CNC, die-casting, injection molding, winding, SMT). |
| `05_mass_production` | `04_assembly_integration_testing` | `is_prerequisite_for` / `requires` | Stable assembly and test flows are prerequisites for repeatable mass production. |
| `05_mass_production` | `06_design_engineering` | `constrains` / `feeds_back_to` | Manufacturing capability constraints drive DFM feedback; design choices determine tooling and cycle time. |
| `05_mass_production` | `07_ai_models_algorithms` | `requires` / `enables` | AI guides vision inspection, robot assembly, and fleet diagnostics; production data improves models. |
| `05_mass_production` | `08_software_middleware` | `requires` | MES, PLM, ERP, WMS, and digital-twin platforms are essential for scaling. |
| `05_mass_production` | `11_applications_markets` | `produces` / `serves` | Mass production supplies robots to industrial, logistics, and eventually consumer markets. |
| `05_mass_production` | `12_policy_regulation_ethics` | `is_regulated_by` | Factory safety, worker protection, product certification, and export controls shape production operations. |
| `05_mass_production` | `01_raw_materials` | `consumes` | Scaling concentrates demand for magnets, lithium, copper, aluminum, and engineered polymers. |

---

## 5. Controlled Vocabulary

### 5.1 Production Concepts

- `production_ramp`
- `factory_design`
- `vertical_integration`
- `contract_manufacturing`
- `yield_management`
- `end_of_line_testing`
- `burn_in_testing`
- `manufacturing_execution_system`
- `digital_twin`
- `design_for_manufacturability`
- `bill_of_materials`
- `learning_curve`
- `cycle_time`
- `throughput`
- `component_traceability`

### 5.2 Relevant Entity Types

From the project information model:

- `facility` (factory, production line)
- `tool_equipment` (test bench, assembly fixture, automated station)
- `oem` (robot manufacturer)
- `tier1_supplier`
- `tier2_supplier`
- `component_manufacturer`
- `software_platform` (MES, PLM, ERP, WMS)
- `report` (market analysis, teardown)
- `standard`

---

## 6. Key Sources

### 6.1 Primary / Authoritative Sources

1. **Figure AI**. *BotQ + Ramping Figure 03 Production* (2025–2026). Official company sources on vertical integration, tooling shift from CNC to die-casting/injection molding, custom MES/PLM, and ramp from one robot per day to one per hour with >80% first-pass yield.  
   URLs: https://www.figure.ai/news/botq; https://www.figure.ai/news/ramping-figure-03-production

2. **Agility Robotics**. *RoboFab* (2025). Official description of the 70,000 sq ft CapEx-light factory, modular work cells, and 10,000-robot/year peak capacity.  
   URL: https://agilityrobotics.com/robofab

3. **UBTECH Robotics**. *Annual Report 2025* (2026). Discloses 1,079 full-size humanoid units sold, RMB 820.6 million humanoid revenue, and annualized production capacity exceeding 6,000 units.  
   URL: https://owebsite-cdn.ubtrobot.com/resources/file/2026/04/21/797179114676293.pdf

### 6.2 Industry and Market Analysis

4. **Goldman Sachs / DBS-TrendForce**. *Humanoid Robot Market and BOM Cost Analysis* (2024–2025). Goldman Sachs revised its 2035 market estimate to $38 billion and flagged ~40% year-over-year manufacturing-cost declines; DBS/TrendForce estimates movement/actuation at ~55% of BOM cost and Chinese domestic share at ~71.8% of total cost contribution.  
   URLs: https://bardai.ai/2024/03/28/goldman-sachs-over-1-million-humanoids-will-likely-be-produced-annually-in-10-years/; https://researchwise.dbsvresearch.com/ResearchManager/DownloadResearch.aspx?E=ifaeakhah

5. **Jabil / Robotics and Automation News**. *Scaling Humanoid Robots from Prototype to Production* (2026). Contract-manufacturer perspective on supply-chain maturity, unit economics, DFM, and safety validation.  
   URL: https://roboticsandautomationnews.com/2026/04/16/interview-jabil-on-scaling-humanoid-robots-from-prototype-to-production/100706/

### 6.3 Domain-Specific Sources

6. **China Mass-Production Ecosystem** (2026). Shenzhen Government Online reports Leju Robotics' pilot line and >10,000-unit/year automated line; EngineAI reports its 12,000 sq m Shenzhen base with 15-minute takt time; EYOU/Global Times report the world's first automated humanoid robot joint line with 100,000-unit annual capacity and >95% first-pass yield.  
   URLs: https://www.sz.gov.cn/en_szgov/news/infocus/aisz/news/content/post_12733795.html; https://www.morningstar.com/news/pr-newswire/20260529cn70096/engineai-launches-shenzhen-intelligent-manufacturing-base-as-first-batch-of-t800-humanoid-robots-roll-off-the-production-line-to-begin-mass-delivery; https://hotel.report/technology/chinese-company-launches-automated-production-line-for-robot-joints-step-toward-humanoid-robots-mass-production

7. **ISO/TS 15066 Collaborative Robot Safety** (Universal Robots 2018; A3 2016). Technical specification for power/force limiting, speed/separation monitoring, and risk assessment in collaborative robot systems.  
   URL: https://www.universal-robots.com/news-and-media/news-center/universal-robots-welcomes-the-new-technical-specification-on-collaborative-robot-design/

8. **Tesla / Industry coverage of Optimus production targets** (2025–2026). Aggregates company production targets (5,000–10,000 units in 2025; 50,000–100,000 in 2026; $20,000–$30,000 consumer price target; 10M-unit/year Giga Texas aspiration) as reported by third-party industry trackers. These are forward-looking company targets, not independently verified production figures.  
   URLs: https://optimusk.blog/blog/what-is-tesla-optimus/; https://www.ccn.com/news/technology/how-much-does-tesla-optimus-cost-elon-musk/

---

## 7. Open Questions

1. What is the empirically validated learning-curve exponent for humanoid robot assembly, and which subsystems (actuators, hands, battery packs) dominate cost reduction as volume scales?
2. How should the ontology represent factory-level data — should each production line, work cell, and test station be a separate `facility`/`tool_equipment` entity, or should factory attributes be embedded in the OEM entity?
3. Which humanoid robot production claims (e.g., Tesla's 10M-unit/year Giga Texas target, Figure's 100,000-unit four-year target) are supported by verifiable physical evidence versus forward-looking company guidance?
4. What are the most effective cross-domain metrics for comparing mass-production maturity across OEMs: yield, cycle time, capacity utilization, or cost-per-unit per subsystem?
