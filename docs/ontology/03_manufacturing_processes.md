# 03 Manufacturing Processes

> **Domain Code**: `03_manufacturing_processes`  
> **Layer**: Upstream  
> **Status**: Draft — subject to review before v0.1.0  
> **Purpose**: Define the manufacturing and fabrication processes that transform raw materials and components into humanoid-robot-grade parts, and establish how this domain links to the rest of the value chain.

---

## 1. Central Question

> **How are the physical parts of a humanoid robot made, and which process choices determine precision, yield, cost, and scalability?**

Humanoid robots are mechatronic assemblies with unusually demanding tolerances: high torque-density joints, lightweight structures, dense cable routing, and compact sensor/electronics integration. The same part that works in a one-off prototype may fail in volume production if the wrong forming, machining, winding, or joining process is chosen. This domain tracks the upstream transformation steps before subsystems are assembled into a complete robot.

---

## 2. Scope

### 2.1 In Scope

- Machining, casting, molding, and forming of structural and mechanical parts.
- Stator/rotor winding, lamination stacking, magnet insertion, and motor actuator assembly.
- Gear cutting, grinding, honing, and precision reducer assembly.
- PCB fabrication, SMT assembly, cable harness manufacturing, and connector integration.
- Surface treatment, heat treatment, coating, and cleaning processes.
- In-process and end-of-line inspection, metrology, and quality control.
- Process capability, yield, and design-for-manufacturability (DFM) trade-offs.

### 2.2 Out of Scope

- Raw material extraction and refining (covered in `01_raw_materials`).
- Finished component specifications and supplier ecosystems (covered in `02_components_supply_chain`).
- Final robot assembly, calibration, and system testing (covered in `04_assembly_integration_testing`).
- Factory-level production ramp and unit economics (covered in `05_mass_production`).

---

## 3. Key Concepts

### 3.1 Structural and Mechanical Part Fabrication

Humanoid robots require lightweight, stiff, and accurately located parts for frames, joint housings, actuator mounts, and covers. The dominant process families differ in cost, precision, and volume suitability:

| Process | Typical Parts | Tolerance / Feature | Volume Economics |
|---------|---------------|---------------------|------------------|
| CNC machining | Joint housings, actuator interfaces, brackets | Micron-level repeatability, high geometric flexibility | Low–medium volumes; higher cycle time and scrap risk |
| Die casting | Aluminum frames, motor housings, structural shells | Good surface finish; porosity must be controlled for leak-tight or welded regions | Medium–high volumes; requires tooling investment |
| Metal injection molding (MIM) | Micro-gears, complex steel brackets, integrated gear-shaft assemblies | ±0.3–0.5% dimensional tolerance; wall thickness down to 0.5–1.0 mm | High volumes; near-net-shape reduces material waste |
| Sheet metal fabrication | Covers, shields, brackets, enclosures | Fast, low-cost; limited to 2.5-D forms | High volumes; often combined with stamping and bending |
| Additive manufacturing (metal / polymer) | Prototype brackets, topology-optimized links, custom fixtures | Design freedom; surface finish and fatigue properties are process-dependent | Prototyping and low-volume; production use is emerging |

**Sources and evidence**:
- Industry manufacturing analysis notes that humanoid robots depend on precision CNC machining, die casting, sheet-metal fabrication, injection molding, and custom fasteners; joint housings, actuator shells, and frames are called out as critical parts where manufacturing quality directly affects stability, lifespan, and safety [Yijin Solution 2026].
- Fraunhofer IPA and P3 emphasize that European automotive and machinery suppliers can leverage capabilities in lightweight design, advanced manufacturing processes, and industrial quality management to participate in the emerging humanoid hardware value chain [Fraunhofer IPA 2026].
- MIM is reported to achieve ~97% material utilization versus ~30% for CNC machining of complex components, with tolerances of ±0.3–0.5% and wall thicknesses of 0.5–1.0 mm enabling compact robotic joint geometries [JHMIM 2026].

> 🔮 **Speculative / forward-looking**: Additive manufacturing is frequently cited as an enabler for topology-optimized, low-volume robot parts, but fatigue life, surface finish, and build-rate constraints mean its role in mass-produced humanoids remains uncertain. Its current value is strongest for prototyping, fixturing, and non-structural customization.

### 3.2 Electric Motor and Actuator Assembly

Most humanoid joints use brushless permanent-magnet synchronous motors paired with reducers. The motor manufacturing sequence is a precision electromechanical process:

| Step | Key Operations | Quality Drivers |
|------|----------------|-----------------|
| Stator core production | Lamination stamping / laser cutting, stacking, welding / bonding | Core loss, stack height consistency, concentricity |
| Stator winding | Needle / flyer winding, insert winding, hairpin forming | Slot fill factor, wire tension, turn count, insulation integrity |
| Rounding and welding | Coil forming, laser / TIG welding of phase leads | Lead position, joint resistance, thermal management |
| PCBA integration | Soldering stator leads to control PCBA, conformal coating | Electrical reliability, solder joint quality |
| Rotor assembly | Shaft fitting, magnet insertion / bonding, balancing | Magnet position accuracy, field homogeneity, imbalance |
| Motor final assembly | Stator-rotor insertion, bearing installation, encoder mounting | Air-gap uniformity, cogging torque, noise |

**Sources and evidence**:
- GROB provides automated stator winding, rotor assembly, and motor-assembly lines, including needle winding, hairpin processing, magnet insertion via robot, and impregnation cells; the company states that rotor magnet insertion and adhesive bonding are critical to motor performance [GROB 2026].
- Magnetic Innovations describes an automated rotor assembly cell that measures each magnet's magnetic properties, uses atmospheric plasma surface preparation, and scans the finished rotor magnetic field to verify homogeneity and traceability [Magnetic Innovations 2024].
- A production-line supplier for humanoid actuators documents a stator assembly sequence that includes winding, rounding and laser welding, PCBA soldering, and heat-shrink fitting of the housing, with in-line force, temperature, and pressure monitoring [Honest HLS 2024].

> ⚠️ **Partially verified**: Detailed first-source BOMs and cycle times for Tesla Optimus, Unitree H1, or Figure 02 motors are not publicly available. The process sequence above is representative of industrial BLDC / PMSM motor manufacturing and should be validated against specific OEM teardowns when available.

### 3.3 Precision Gear and Reducer Manufacturing

Reducers translate high-speed, low-torque motor output into slow, high-torque joint motion. Common architectures in humanoids include harmonic drives, planetary gearboxes, and cycloidal drives. Precision is the dominant manufacturing constraint:

| Reducer Type | Key Manufacturing Steps | Critical Quality Attributes |
|--------------|------------------------|------------------------------|
| Harmonic drive | Flexspline forming / rolling, circular spline gear cutting, wave-generator machining | Backlash, flexspline fatigue life, positional accuracy |
| Planetary reducer | Sun/planet/ring gear hobbing or grinding, shaft / carrier machining, bearing selection | Backlash, torsional stiffness, efficiency, noise |
| Cycloidal drive | Cycloid disc grinding, pin-roller machining, output-shaft assembly | Contact pattern, stiffness, efficiency, lubrication retention |

**Sources and evidence**:
- A review of precision gear manufacturing for robotics identifies gear hobbing, grinding, honing, and hard finishing as core processes, and highlights the trade-off between machining accuracy, surface integrity, and production cost [Zhang et al. 2021].
- Research on gears for robot-like systems notes that profile modification, heat treatment, and surface finishing strongly influence load distribution, noise, and fatigue life [Oberneder et al. 2024].
- PICEA MOTION states that harmonic-drive flexsplines must withstand continuous elastic deformation with micron-level accuracy, and that assembly requires advanced machinery and testing equipment; cooperation with universities is used to address materials and mechanical optimization [PICEA MOTION 2025].
- Market analysis of robot precision reducers projects the global market to grow from ~USD 1.2 billion in 2024 to ~USD 2.5 billion by 2033 at a ~9.2% CAGR, with humanoid robots identified as a key application segment [Verified Market Reports 2025].

### 3.4 Electronics Interconnect, Surface Treatment, and Quality Assurance

Humanoid robots are dense electromechanical systems. Manufacturing must integrate power electronics, sensor PCBs, communication cabling, and protective finishes under tight space and reliability constraints:

| Area | Key Processes | Humanoid-Specific Considerations |
|------|---------------|----------------------------------|
| PCBs and SMT | Multi-layer PCB fabrication, SMT placement, reflow, conformal coating | Miniaturization, signal integrity, thermal cycling resistance |
| Cable harnesses | Cutting, stripping, crimping, connector assembly, routing aids | High flex-cycle requirements at moving joints; EMI shielding |
| Surface treatment | Anodizing, passivation, PVD/CVD coatings, plasma cleaning | Wear resistance, corrosion protection, biocompatibility for human contact |
| Quality assurance | CMM, vision inspection, torque monitoring, functional test benches | Traceability, SPC, and process-capability indices (Cp/Cpk) |

**Sources and evidence**:
- Fraunhofer IPA's industrial benchmark for humanoid robots includes ISO-standard particle-emission and outgassing tests, indicating that contamination behavior and cleanroom compatibility are becoming formal manufacturing requirements for sensitive deployment environments [Fraunhofer IPA 2026; HyperSinc 2026].
- ISO 10218-1 and ISO 10218-2 define safety requirements for robot design/manufacture and system integration, including protective stop functions, speed/force monitoring, and validation of safety-rated functions; these standards shape manufacturing test protocols for deployable robots [ISO 10218-1:2011; ISO 10218-2:2025].
- Magnetic Innovations documents automated plasma cleaning and adhesive bonding process control as part of rotor manufacturing quality assurance [Magnetic Innovations 2024].

---

## 4. Process-Capability and Scaling Considerations

| Factor | Prototype Impact | Mass-Production Impact |
|--------|------------------|------------------------|
| Tolerance stack-up | Managed by hand fitting and selective assembly | Requires Cpk-driven processes and automated metrology |
| Material utilization | Less critical; scrap cost is small in absolute terms | Determines per-unit cost and sustainability footprint |
| Tooling lead time | 3D-printed or soft tooling acceptable | Hard tooling, multi-cavity molds, and automated lines required |
| Surface finish / fatigue | Visual and short-cycle checks | Requires validated heat treatment, coating, and life testing |
| Supply base | Single-source custom suppliers | Need qualified Tier-2/Tier-3 ecosystem with capacity |

> 🔮 **Speculative / forward-looking**: The transition from prototype to mass production for humanoids may resemble the EV battery scaling experience, where early cost pressure and industrial maturity strongly influenced regional value creation. Europe and North America have precision-manufacturing expertise, but high-volume actuator and reducer capacity is currently concentrated in Asia. The geographic distribution of humanoid manufacturing capability is therefore an open strategic question.

---

## 5. Relationship Patterns to Other Domains

| From | To | Relationship | Rationale |
|------|-----|--------------|-----------|
| `03_manufacturing_processes` | `01_raw_materials` | `consumes` / `processed_by` | Processes transform raw materials (aluminum ingot, magnet powder, copper wire) into semi-finished or finished parts. |
| `03_manufacturing_processes` | `02_components_supply_chain` | `produces` | Manufacturing processes create components: machined housings, wound stators, assembled reducers, PCBs. |
| `03_manufacturing_processes` | `04_assembly_integration_testing` | `is_prerequisite_for` | Parts must be fabricated and inspected before they can be assembled, calibrated, and system-tested. |
| `03_manufacturing_processes` | `05_mass_production` | `enables` / `constrains` | Process capability (cycle time, yield, Cpk) determines whether production can ramp to thousands or millions of units. |
| `03_manufacturing_processes` | `06_design_engineering` | `constrains` / `is_constrained_by` | DFM feedback from manufacturing shapes joint layout and tolerances; design choices dictate which processes are feasible. |
| `03_manufacturing_processes` | `11_applications_markets` | `drives_cost_of` | Process choice and yield directly affect BOM cost and therefore application economics. |
| `03_manufacturing_processes` | `12_policy_regulation_ethics` | `is_regulated_by` | Safety standards (ISO 10218), environmental regulations, and cleanroom requirements shape process and test protocols. |

---

## 6. Controlled Vocabulary

### 6.1 Process Categories

- `cnc_machining`
- `die_casting`
- `metal_injection_molding`
- `sheet_metal_fabrication`
- `additive_manufacturing`
- `stator_winding`
- `rotor_assembly`
- `magnet_insertion`
- `gear_hobbing`
- `gear_grinding`
- `gear_honing`
- `harmonic_drive_assembly`
- `planetary_reducer_assembly`
- `pcb_fabrication`
- `smt_assembly`
- `cable_harness_assembly`
- `surface_treatment`
- `heat_treatment`
- `conformal_coating`
- `quality_control`
- `metrology`
- `functional_testing`

### 6.2 Relevant Entity Types

From the project information model:

- `process`
- `tool_equipment`
- `facility`
- `component`
- `standard`
- `technology`

---

## 7. Key Sources

### 7.1 Primary / Authoritative Sources

1. **Fraunhofer IPA & P3**. *The Humanoid Hardware Value Chain: Can the European Manufacturing Industry Capitalize on the Humanoid Momentum?* (2026). Analyzes hardware value chains for sensing, actuation, structure, and energy; identifies precision manufacturing and quality management as key European capabilities.  
   URL: https://www.ipa.fraunhofer.de/content/dam/ipa/de/documents/Publikationen/Studien/260219_Humanoid_Value_Chain_final.pdf

2. **ISO 10218-1:2011**. *Robots and robotic devices — Safety requirements for industrial robots — Part 1: Robots*. Defines design and construction safety requirements for robot manufacturers.  
   URL: https://www.iso.org/standard/51330.html

3. **ISO 10218-2:2025**. *Robots and robotic devices — Safety requirements for industrial robots — Part 2: Robot systems and integration*. Governs installation, safeguarding, risk assessment, and collaborative application requirements.  
   URL: https://www.iso.org/standard/85697.html

### 7.2 Industry and Market Analysis

4. **IDTechEx**. *Humanoid Robots 2025-2035: Technologies, Markets and Opportunities* (2025). Covers actuators, motors, reducers, sensors, batteries, high-performance materials, and market forecasts relevant to manufacturing decisions.  
   URL: https://www.idtechex.com/en/research-report/humanoid-robots/1093

5. **Verified Market Reports**. *Robot Precision Gear Reducer Market Outlook 2025* (2025). Estimates the global robot precision reducer market at ~USD 1.2 billion in 2024 and ~USD 2.5 billion by 2033, with humanoid robots as an application segment.  
   URL: https://www.verifiedmarketreports.com/product/robot-precision-gear-reducer-market/

6. **Yijin Solution**. *Top 10 Humanoid Robot Manufacturers* (2026). Manufacturing-focused analysis identifying CNC machining, die casting, sheet metal, injection molding, and fasteners as core process dependencies for humanoid robots.  
   URL: https://yijinsolution.com/cnc-guides/top-humanoid-robot-manufacturers/

### 7.3 Domain-Specific Process Sources

7. **GROB Group**. *Machines and Systems for Electric Motor Production* (2026). Describes stator winding, rotor magnet insertion, motor assembly, and impregnation process equipment used in electric motor manufacturing.  
   URL: https://www.grobgroup.com/en/products/product-range/winding-and-inserting-technology/

8. **Magnetic Innovations**. *New Robot Automatically Assembles Rotors of Permanent Magnet Synchronous Motors* (2024). Documents automated magnet handling, plasma cleaning, adhesive bonding, and magnetic-field scanning for rotor quality assurance.  
   URL: https://www.magneticinnovations.com/new-robot-automatically-assembles-rotors-of-permanent-magnet-synchronous-motors/

9. **JHMIM**. *Precision MIM Gears for Humanoid Robot Joints* (2026). Technical overview of metal injection molding for robotic gears, including tolerance, wall-thickness, material utilization, and scaling claims.  
   URL: https://jhmim.com/precision-mim-gears-for-humanoid-robot-joints/

10. **PICEA MOTION**. *Harmonic Reduction Gear in Humanoid Robots and the Challenges of Manufacturing* (2025). Discusses flexspline precision, assembly accuracy, and testing requirements for harmonic drives in humanoids.  
   URL: https://www.piceamotiondrive.com/harmonic-reduction-gear-in-humanoid-robots-and-the-challenges.html

11. **Honest HLS**. *Humanoid Robot Actuator Motor Stator Assembly Line Solution* (2024). Documents a stator-assembly sequence for humanoid actuators, including winding, laser welding, PCBA soldering, and heat-shrink fitting with in-line monitoring.  
   URL: https://www.honest-hls.com/humanoid-robot-actuator-stator-line

### 7.4 Industry / Benchmark Reporting

12. **HyperSinc Intelligence**. *Germany's Fraunhofer Institute Publishes First Industrial Benchmark for Humanoid Robots* (2026). Reports on Fraunhofer IPA's industrial benchmark, including ISO-standard particle-emission and outgassing tests for cleanroom deployment.  
   URL: https://hypersinc.com/article/germanys-fraunhofer-institute-publishes-first-industrial-benchmark-for-humanoid--1779109343314

### 7.5 Academic / Peer-Reviewed Sources

13. **Zhang Y., Huang G., Chen X.** *Precision gear manufacturing methods for robotics: A review*. Precision Engineering, 2021;72:45-56. Reviews gear hobbing, grinding, honing, and finishing processes for robotic applications.  
   URL: https://doi.org/10.1016/j.precisioneng.2021.04.007

14. **Oberneder F., Landler S., Otto M., Vogel-Heuser B., Zimmermann M., Stahl K.** *Influences of Different Parameters on Selected Properties of Gears for Robot-Like Systems*. Frontiers in Robotics and AI, 2024;11:1414238.  
   URL: https://doi.org/10.3389/frobt.2024.1414238

---

## 8. Open Questions

1. What is the per-process cost and cycle-time breakdown for a representative humanoid actuator (motor + reducer + housing) with verified first-source data?
2. Which manufacturing processes currently limit humanoid production scaling — reducer flexspline forming, motor winding, die-cast porosity control, or something else — and where are the bottlenecks geographically concentrated?
3. How should the ontology represent process capability (e.g., Cpk, tolerance grade, surface roughness) and yield data for different volume scenarios?
4. To what extent can automotive or consumer-electronics manufacturing equipment be re-purposed for humanoid robot parts, and where is custom tooling unavoidable?
