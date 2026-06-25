# 06 Design & Engineering

> **Domain Code**: `06_design_engineering`  
> **Layer**: Midstream  
> **Status**: Draft — subject to review before v0.1.0  
> **Purpose**: Define the mechanical and systems-engineering concepts that determine humanoid robot morphology, kinematics, dynamics, manufacturability, and safety, and map how this domain links to the rest of the value chain.

---

## 1. Central Question

> **What physical form, kinematic layout, actuation architecture, and safety design are required to turn a humanoid robot concept into a mass-producible, industrially useful product?**

Design and engineering sit at the translation layer between components and an integrated robot. Choices made here constrain cost, performance, reliability, and deployability. This domain tracks the decisions that determine whether a humanoid remains a prototype or becomes a scalable product.

---

## 2. Scope

### 2.1 In Scope

- Humanoid morphology, degrees of freedom (DoF), limb proportions, and joint range of motion.
- Kinematic and dynamic modeling that links morphology to control and task capability.
- Actuator selection, joint transmission design, and backdrivability trade-offs.
- Structural design, lightweighting, topology optimization, and material selection.
- Design for manufacturability, assembly, testing, and serviceability (DFX).
- Cable routing, thermal management, sealing, and maintenance access.
- Safety design: force limiting, pinch points, rounded surfaces, emergency stop, and fall behavior.

### 2.2 Out of Scope

- Manufacturing processes that transform raw materials into parts (see `03_manufacturing_processes`).
- Factory design, production ramp, and yield curves (see `05_mass_production`).
- AI/learning algorithms, software middleware, and datasets (see `07_ai_models_algorithms`, `08_software_middleware`, `09_data_datasets`).
- Market applications and policy enforcement (see `11_applications_markets` and `12_policy_regulation_ethics`).

---

## 3. Key Concepts

### 3.1 Morphology & Degrees of Freedom

A humanoid robot's morphology defines the physical envelope within which it can operate. Key design parameters include height, mass, total DoF, limb layout, and workspace reach. The trend in industrial platforms is toward adult-scale, high-DoF designs that can use human workstations, but each added joint increases cost, mass, wiring, and control complexity.

| Parameter | Representative Range | Design Implication |
|-----------|---------------------|--------------------|
| Height | 1.6–1.9 m | Matches human-scale workstations, doors, and tools [1][7] |
| Mass | 30–90 kg | Affects actuator sizing, energy use, fall hazard, and transportability [1][4] |
| Total DoF | 20–56+ | More DoF expands dexterity and posture choice; raises cost and calibration burden [6][7] |
| Legs | 6–7 DoF per leg | Six DoF is common for bipedal walking; seven adds yaw/rotation for uneven terrain [6] |
| Arms | 6–8 DoF per arm | Defines reachable workspace and manipulation redundancy [6][7] |
| Hands | 4–22+ DoF | Underactuated or high-DoF hands trade grasp versatility against cost and durability [4][7] |
| Waist / neck | 1–3 DoF | Enables gaze/attention decoupling and social legibility [7] |

**Sources and evidence**:
- A survey of humanoid robot development notes that humanoid platforms generally require at least 20 DoF, and that increasing DoF tends to increase size, processing requirements, power consumption, and cost [6].
- The *Humanoid Factors* framework defines a full humanoid as combining a torso and head/neck sensing cluster, bimanual arms, bipedal locomotion, and dexterous hands, and emphasizes that morphology is invariant during operation and preconditions compatibility with human environments [7].
- Boston Dynamics' 2026 Atlas product has 56 DoF, a height of 1.9 m, a weight of 90 kg, a 2.3 m reach, and an instant payload of 50 kg, illustrating the upper end of current industrial morphology [1].

### 3.2 Actuator & Joint Integration

Joint design is the central mechanical decision in a humanoid. The actuator-gear-sensor triad determines torque density, bandwidth, backdrivability, efficiency, and cost. High-torque-density electric actuators—combined with harmonic, planetary, or cycloidal reducers—have made adult-scale humanoids feasible, while direct-drive and quasi-direct-drive designs prioritize backdrivability and impact tolerance at the expense of torque multiplication.

| Design Choice | Common Options | Key Trade-off |
|---------------|----------------|---------------|
| Actuation paradigm | Direct-drive (DD), quasi-direct-drive (QDD), series elastic actuator (SEA), geared servo | Backdrivability/bandwidth vs. torque density and shock tolerance [8][4] |
| Gear ratio | Low ratio (DD/QDD) vs. high ratio (harmonic/RV/planetary) | Low ratio improves transparency and force control; high ratio amplifies torque and stiffness [8] |
| Transmission type | Harmonic drive, cycloidal, planetary, ball/roller screw | Precision, backlash, weight, and cost differ by joint loading [4] |
| Sensor integration | Joint encoders, force/torque sensors, current sensing | Determines closed-loop bandwidth and collision detectability [4] |
| Thermal path | Heat sinking, conductive housing, forced air | Affects continuous torque and service intervals [4] |

**Sources and evidence**:
- Kenneally, De, and Koditschek present design principles for direct-drive legged robots, showing that low mechanical impedance, high backdrivability, and high control bandwidth can be achieved by pairing high-torque-density motors with low-ratio transmissions [8].
- Boston Dynamics states that its 2026 Atlas uses custom electric actuators supplied by Hyundai Mobis, with the two companies building a "highly reliable component supply chain" to accelerate actuator development and production [1].
- IDTechEx identifies actuators, motors, reducers, screws, bearings, and sensors as critical hardware components whose cost and manufacturing challenges dominate humanoid robot economics [4].

### 3.3 Structural Design, Lightweighting & Durability

Structural design balances specific strength, stiffness, fatigue life, thermal management, and environmental sealing. Lightweighting is not merely material substitution: it includes topology optimization, part consolidation, and integrated die-cast or molded housings. For mass production, the structure must also support repeatable assembly, service access, and protection against dust and water ingress.

| Concern | Common Approach | Mass-Production Implication |
|---------|-----------------|-----------------------------|
| Lightweighting | Aluminum/magnesium alloys, carbon-fiber/PEEK composites, topology optimization | Lower moving mass reduces actuator load and extends battery life [4][7] |
| Stiffness | Ribbed housings, bearing preloading, closed load paths | Maintains precision under payload and dynamic loads [4] |
| Thermal management | Heat sinks, thermally conductive housings, segregated power/sensor zones | Sustains continuous operation and protects electronics [4] |
| Environmental sealing | Gaskets, sealed connectors, IP-rated enclosures | Required for factory floor reliability and wash-down [1] |
| Serviceability | Modular sub-assemblies, field-replaceable units, accessible fasteners | Drives mean-time-to-repair and total cost of ownership [1] |

**Sources and evidence**:
- IDTechEx tracks high-performance materials (magnesium alloys, PEEK, carbon-fiber composites, ultra-high-molecular-weight polyethylene) as a distinct component category in humanoid robots and notes lightweighting as a key design trend [4].
- Boston Dynamics specifies Atlas with an IP67 rating, modular components, field-replaceable parts, and customer self-repair certification, illustrating the shift from research prototype to serviceable product [1].
- The *Humanoid Factors* framework highlights that structural design and material applications are among the emerging challenges required to bring humanoid capabilities closer to humans [7].

### 3.4 Design for Manufacturability, Assembly & Serviceability (DFX)

DFX methods link early design decisions to downstream production cost, quality, and service cost. For humanoids, the payoff is especially large because part counts are high, tolerances are tight, and wiring/cabling is dense. DFMA (Design for Manufacture and Assembly), DFT (Design for Test), and DFS (Design for Serviceability) should be applied before tooling is committed.

| Method | Goal | Humanoid Application |
|--------|------|----------------------|
| DFM | Minimize part count and select process-compatible geometries and tolerances | Reduces machining, molding, and fixturing cost [5] |
| DFA | Reduce fasteners, enable self-location, and standardize interfaces | Cuts assembly time and error rates for dense mechatronic systems [5] |
| DFT | Provide test points, fixture interfaces, and diagnostic access | Supports end-of-line calibration and HIL testing [5] |
| DFS | Modular leg/arm/head sub-assemblies, labeled harnesses, easy access | Lowers field service time and spare-parts inventory [1][5] |
| DFC | Early cost estimation and should-costing | Prevents designs that cannot hit target BOM cost [4][5] |

**Sources and evidence**:
- Boothroyd, Dewhurst, and Knight's *Product Design for Manufacture and Assembly* provides the foundational DFMA methodology, including analytical tools to estimate assembly time and cost before detailed design is finalized [5].
- Boston Dynamics describes the 2026 Atlas as "the most production friendly robot we've ever designed," noting a significant reduction in unique parts and components designed for compatibility with automotive supply chains [1].
- IDTechEx emphasizes that cost reduction with volume upscaling depends on design choices around modularity, efficient materials, and power efficiency [4].

### 3.5 Safety & Human-Robot Interaction Design

Safety design must satisfy existing industrial robot standards while addressing the special hazards of a mobile, balancing, multi-joint platform: collision forces, pinch points, falls, and unintended motion. Standards such as ISO/TS 15066 provide biomechanical force limits for collaborative robots, and ISO 10218-1 sets inherent safe-design requirements for industrial robots. Humanoids currently fall into a regulatory patchwork; mechanical safety design is therefore a first line of defense.

| Hazard | Design Mitigation | Standard / Evidence Basis |
|--------|-------------------|---------------------------|
| Collision / impact force | Force/torque limiting, rounded surfaces, compliant covers, low effective mass | ISO/TS 15066 force/pressure limits by body region [2] |
| Pinch points | Guarded joint gaps, shrouds, pinch-free kinematics | ISO 10218-1 protective design requirements [3] |
| Falls / tipping | Low center of mass, wide support polygon, fall-recovery behavior | Stability margins and dynamic balance limits [4][7] |
| Emergency stop | Accessible e-stop, safe state within 500 ms, category 0/1 stop | ISO 10218-1 stop-performance and safety-function requirements [3] |
| Speed / force in shared zones | Power and force limiting (PFL), speed separation monitoring | ISO/TS 15066 collaborative operation modes [2] |

**Sources and evidence**:
- ISO/TS 15066:2016 specifies biomechanical force and pressure limits for transient and quasi-static contact, categorized by body region, and is the reference for power- and force-limiting collaborative robot design [2].
- ISO 10218-1:2025 sets inherently safe design, risk-reduction measures, emergency stop, and functional-safety requirements for industrial robots, including collaborative applications [3].
- Boston Dynamics lists Atlas safety features as fenceless guarding and human detection, reflecting the move toward uncaged, shared-space operation [1].

---

## 4. Relationship Patterns to Other Domains

| From | To | Relationship | Rationale |
|------|-----|--------------|-----------|
| `06_design_engineering` | `02_components_supply_chain` | `requires` | Joint designs require specific actuators, reducers, encoders, sensors, fasteners, and cables. |
| `06_design_engineering` | `01_raw_materials` | `constrains` / `enables` | Material density, strength, and magnet energy product bound morphology, actuator size, and structural mass. |
| `06_design_engineering` | `03_manufacturing_processes` | `constrains` / `is_prerequisite_for` | DFM/DFA decisions determine which processes (CNC, die-casting, molding, winding) are viable and economical. |
| `06_design_engineering` | `04_assembly_integration_testing` | `is_prerequisite_for` | Modular architecture, tolerance stacks, and test-point access dictate assembly sequence and fixture design. |
| `06_design_engineering` | `05_mass_production` | `enables` / `constrains` | Part-count reduction and supply-chain-compatible design determine yield, unit cost, and scaling potential. |
| `06_design_engineering` | `07_ai_models_algorithms` | `constrains` / `requires` | Morphology and DoF define the action space and sensing envelope available to control and learning policies. |
| `06_design_engineering` | `10_evaluation_benchmarks` | `is_regulated_by` / `verified_by` | Safety and performance claims are validated against standards (ISO/TS 15066, ISO 10218) and task benchmarks. |
| `06_design_engineering` | `12_policy_regulation_ethics` | `is_regulated_by` | Mechanical safety must comply with machinery directives, robot safety standards, and regional certification rules. |

---

## 5. Controlled Vocabulary

### 5.1 Category Tags

- `morphology`
- `degrees_of_freedom`
- `kinematics`
- `dynamics`
- `actuator_integration`
- `transmission_design`
- `backdrivability`
- `direct_drive`
- `series_elastic_actuator`
- `structural_design`
- `lightweighting`
- `topology_optimization`
- `material_selection`
- `dfm` (Design for Manufacturability)
- `dfa` (Design for Assembly)
- `dft` (Design for Test)
- `dfs` (Design for Serviceability)
- `design_for_x`
- `cable_routing`
- `thermal_management`
- `ip_rating`
- `safety_design`
- `force_limiting`
- `pinch_point`
- `emergency_stop`
- `fall_resistance`
- `human_robot_interaction`

### 5.2 Relevant Entity Types

From the project information model:

- `robot_system`
- `component`
- `technology`
- `standard`
- `paper`
- `report`
- `facility`
- `process`

---

## 6. Key Sources

### 6.1 Primary / Authoritative Sources

1. **Boston Dynamics**. *Boston Dynamics Unveils New Atlas Robot to Revolutionize Industry* (2026). Official product launch; describes 56 DoF, 1.9 m height, 90 kg mass, 2.3 m reach, 50 kg payload, IP67 rating, fenceless guarding, human detection, automotive-supply-chain compatibility, and actuator partnership with Hyundai Mobis.  
   URL: https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/

2. **ISO/TS 15066:2016**. *Robots and robotic devices — Collaborative robots — Safety requirements* (2016). Defines biomechanical force and pressure limits for human-robot contact, categorized by body region and contact type (transient/quasi-static).  
   URL: https://www.iso.org/standard/62996.html

3. **ISO 10218-1:2025**. *Robotics — Safety requirements for industrial robots — Part 1: Robots* (2025). Sets inherently safe design, risk-reduction measures, emergency stop, functional safety, and collaborative-robot requirements for industrial robot manufacturers.  
   URL: https://www.iso.org/standard/73933.html

### 6.2 Industry and Market Analysis

4. **IDTechEx**. *Humanoid Robots 2025-2035: Technology, Market, and Opportunity* (2025). Independent market and technology analysis covering actuators, motors, reducers, sensors, batteries, high-performance materials, design/manufacturing challenges, and cost forecasts for humanoid robots.  
   URL: https://www.idtechex.com/en/research-report/humanoid-robots/1093

### 6.3 Domain-Specific Sources

5. **Boothroyd, G., Dewhurst, P., and Knight, W. A.** *Product Design for Manufacture and Assembly* (3rd ed., CRC Press, 2011). Foundational DFMA textbook providing methods to reduce part count, estimate assembly cost, and integrate manufacturing considerations into early design.  
   URL: https://doi.org/10.1201/9781420089288

6. **Saeedvand, S., Jafari, M., Aghdasi, H. S., and Baltes, J.** *A comprehensive survey on humanoid robot development* (The Knowledge Engineering Review, 34, e20, 2019). Survey of humanoid morphology, DoF requirements, and the relationship between DoF, size, processing, and cost.  
   URL: https://doi.org/10.1017/S0269888919000158

7. **Liu, X., Sadikoglu, E., Senanayake, R., and Huang, L.** *Humanoid Factors: Design Principles for AI Humanoids in Human Worlds* (arXiv:2602.10069, 2026). Proposes a physical-cognitive-social-ethical framework; defines full humanoid morphology and discusses actuation and material advances.  
   URL: https://arxiv.org/abs/2602.10069

8. **Kenneally, G., De, A., and Koditschek, D. E.** *Design principles for a family of direct-drive legged robots* (IEEE Robotics and Automation Letters, vol. 1, no. 2, pp. 900–907, 2016). Establishes principles for low-impedance, backdrivable, high-bandwidth actuation in dynamic legged robots.  
   URL: https://doi.org/10.1109/LRA.2016.2528294

---

## 7. Open Questions

1. What is the minimum viable morphology and DoF configuration for representative industrial tasks, and how should the trade-off between kinematic redundancy, cost, and reliability be quantified?
2. How do specific design choices (actuation topology, materials, mass distribution) translate into measurable field metrics such as fall tolerance, maintenance interval, and total cost of ownership?
3. Which DFMA/DFS metrics and test interfaces should become standard for humanoid robot mass production, given the diversity of current platforms?
4. How should biomechanical safety limits originally developed for fixed-base collaborative robots (ISO/TS 15066) be adapted for mobile, balancing humanoids controlled by learned policies?
