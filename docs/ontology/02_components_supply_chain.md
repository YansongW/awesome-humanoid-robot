# 02 Components & Supply Chain

> **Domain Code**: `02_components_supply_chain`  
> **Layer**: Upstream  
> **Status**: Draft — subject to review before v0.1.0  
> **Purpose**: Define the component and supply-chain concepts that sit between raw materials and manufacturing/assembly, and establish how this domain links to the rest of the value chain.

---

## 1. Central Question

> **What are the major hardware building blocks of a humanoid robot, who supplies them, and how do their performance, cost, and availability determine mass-production feasibility?**

A humanoid robot is an integrated stack of electromechanical, sensing, power, compute, and structural subsystems. This domain tracks those subsystems before they are assembled into a complete robot: the motors, reducers, sensors, batteries, edge computers, wiring, structural parts, and the tiered supplier network that produces them. Component choices here propagate downstream into design constraints, manufacturing complexity, unit economics, and application capability.

---

## 2. Scope

### 2.1 In Scope

- Actuators, motors, reducers/gearboxes, drivetrains, and end effectors.
- Sensors: cameras, depth sensors, LiDAR, IMU, force/torque sensors, tactile sensors, joint encoders.
- Power subsystems: battery cells/packs, battery management systems (BMS), chargers, thermal management.
- Compute: edge AI SoCs/GPUs, embedded real-time controllers, sensor interfaces.
- Structural parts, cable harnesses, connectors, and fasteners.
- Supplier tiers (Tier-2, Tier-1, OEM), integration strategies, and BOM cost drivers.
- Supply-chain risks: lead times, geographic concentration, single-sourcing, and qualification bottlenecks.

### 2.2 Out of Scope

- Extraction and refining of raw materials (covered in `01_raw_materials`).
- Transformation processes such as CNC machining, winding, or PCB fabrication (covered in `03_manufacturing_processes`).
- Final assembly, calibration, and system-level testing (covered in `04_assembly_integration_testing`).
- AI models, software stacks, and datasets (covered in `07_ai_models_algorithms`, `08_software_middleware`, `09_data_datasets`).
- End-use markets and policy frameworks (covered in `11_applications_markets`, `12_policy_regulation_ethics`), except where they directly influence component demand or cost.

---

## 3. Key Concepts

### 3.1 Actuation & Transmission Subsystems

Humanoid locomotion and manipulation require compact, high-torque, backdrivable joints. Most electric humanoids today use brushless DC or permanent-magnet synchronous motors paired with a speed reducer, position sensor, and motor driver in a single actuator module.

| Component | Function | Common Technologies | Key Metrics |
|-----------|----------|---------------------|-------------|
| Rotary actuator module | Generate controlled joint torque | BLDC/PMSM motor + reducer + encoder + driver | Torque density, peak torque, backdrivability, efficiency, cost |
| Reducer / gearbox | Torque amplification and speed reduction | Harmonic drive, cycloidal drive, planetary gearbox, quasi-direct drive (QDD) | Gear ratio, backlash, efficiency, stiffness, lifetime |
| Linear actuator | Provide linear force for leg/hip extension | Frameless motor + ball/roller screw | Force, stroke, speed, force density |
| End effector / hand | Grasp and manipulate objects | Tendon-driven, gear-driven, underactuated | Degrees of freedom, grip force, tactile sensing, cost |

**Sources and evidence**:
- Fraunhofer IPA's bottom-up hardware value-chain analysis identifies actuators, gears, batteries, and sensors as cost- and performance-relevant components that currently meet industrial requirements only partially in terms of robustness, service life, and cost structure; the study also flags flexible hands as the biggest scaling bottleneck [2].
- IDTechEx provides a component-level technical and cost analysis covering actuators, motors, reducers, screws, bearings, and end effectors, plus 10-year market forecasts for each [1].
- A comparative study of a low-backlash planetary gearbox for humanoid robots reports <4 arcmin backlash, ~97% efficiency, roughly 4× load capacity, and ~5× lower price than a comparable harmonic drive, with similar overall dimensions and about 10% greater mass, suggesting planetary alternatives are gaining viability [6].
- The Unitree H1 illustrates current actuator performance: a knee joint peak torque of ~360 N·m and a reported peak torque density of ~189 N·m/kg [4].

### 3.2 Sensing & Perception Subsystems

Sensors convert the physical world into signals that perception and control algorithms can use. Humanoids typically fuse exteroceptive sensors (cameras, depth, LiDAR) with proprioceptive sensors (IMU, encoders, force/torque) and, increasingly, tactile arrays for manipulation.

| Sensor Type | Role | Examples | Key Metrics |
|-------------|------|----------|-------------|
| Vision cameras | RGB/visual perception | Stereo RGB, global-shutter, fisheye | Resolution, field of view, latency, dynamic range |
| Depth / 3D sensors | Scene geometry & obstacle detection | Stereo depth, time-of-flight, structured light, LiDAR | Range, precision, point density, sunlight robustness, cost |
| IMU | Body orientation & acceleration | MEMS IMU | Bias stability, noise density, bandwidth |
| Joint encoders | Joint position & velocity | Optical/magnetic incremental and absolute encoders | Resolution, accuracy, robustness |
| Force/torque & tactile | Contact detection & compliant manipulation | 6-axis wrist sensors, fingertip tactile arrays | Resolution, range, compliance, durability |

**Sources and evidence**:
- IDTechEx analyzes cameras, LiDAR, radar, ultrasonic, and tactile sensors as part of its component-level humanoid robot coverage [1].
- The Unitree H1 ships with a 3D LiDAR and depth camera for 360° panoramic scanning, plus IMU, joint encoders, and force sensors [4].
- Fraunhofer IPA treats sensing as one of four hardware value-chain pillars (sensors, actuators, structure, energy) and notes that sensor reliability and cost are central to industrial scalability [2].
- Figure 02 integrates six onboard RGB cameras and an onboard vision-language model; its hands include 16 degrees of freedom and tactile sensing for dexterous manipulation [7].

### 3.3 Power & Thermal Subsystems

Power density and thermal management directly constrain runtime, dynamic performance, and safety. Current humanoids predominantly repurpose lithium-ion cells from electric-vehicle or consumer-electronics supply chains, while solid-state and higher-energy-density chemistries remain in development.

| Component | Function | Typical Chemistries / Architectures | Key Metrics |
|-----------|----------|-------------------------------------|-------------|
| Battery cells / pack | Store and deliver energy | LFP, NMC, NCA Li-ion; solid-state emerging | Energy density (Wh/kg), cycle life, C-rate, cost ($/kWh) |
| Battery management system (BMS) | Safety, balancing, state estimation | BMS + contactors + fuses + thermal sensors | SoC/SoH accuracy, thermal-runaway prevention |
| Charging / swapping | Refuel or replace energy | Docking station, conductive charging, hot-swap packs | Charge time, swap time, fleet uptime |
| Thermal management | Maintain actuator and compute temperatures | Heat sinks, fans, heat pipes, liquid cooling, TIM | TDP, junction temperature, reliability |

**Sources and evidence**:
- Interact Analysis compares current humanoid battery configurations: Tesla Optimus Gen-2 is reported to use a 2.3 kWh pack with roughly two hours of dynamic runtime, while Unitree H1 uses an 864 Wh swappable pack; NCM/NCA chemistries dominate, with solid-state pilots emerging [3].
- Fraunhofer IPA notes that off-the-shelf Li-ion cells at ~200 Wh/kg are sufficient for demonstrations but insufficient for many industrial use cases, while solid-state batteries could exceed 500 Wh/kg [2].
- Unitree lists the H1 battery as 15 Ah (0.864 kWh) at a maximum voltage of 67.2 V, with a quickly swappable design [4].
- Figure 02 uses a torso-integrated 2.25 kWh battery pack, delivering roughly 50% more energy than Figure 01 and supporting approximately five to ten hours of operation depending on duty cycle [7].

### 3.4 Compute, Communication & Structural Backbone

Compute must handle high-rate sensor fusion, perception, planning, and low-level motor control within tight power and thermal budgets. The structural backbone and cable harness must carry loads, route power/signals, and survive repeated motion and falls.

| Component | Role | Examples | Key Metrics |
|-----------|------|----------|-------------|
| Edge AI compute | Run perception, planning, and learning models | NVIDIA Jetson AGX Orin / Thor, Intel Core, custom SoCs | TOPS/W, memory bandwidth, latency, I/O |
| Real-time controller | Deterministic joint control and safety | Microcontrollers, FPGAs, motor drives | Cycle time, deterministic buses, functional-safety support |
| Communication buses | Interconnect sensors, actuators, and compute | CAN-FD, EtherCAT, Ethernet, USB, MIPI CSI-2 | Bandwidth, latency, determinism, wiring complexity |
| Structural parts & cabling | Mechanical frame, harnesses, connectors | Aluminum/magnesium/composite skeleton; cable harnesses; connectors | Strength-to-weight, modularity, EMI shielding, maintainability |

**Sources and evidence**:
- NVIDIA's Jetson AGX Orin series delivers up to 275 TOPS of AI performance at 15–60 W, with up to 64 GB LPDDR5 memory and 204.8 GB/s memory bandwidth, and supports multiple high-speed camera interfaces [5].
- The Unitree H1 uses Intel Core i5/i7 compute as standard and offers an optional NVIDIA Jetson Orin NX module; its software stack is ROS2-compatible [4].
- Fraunhofer IPA includes structure and energy as core hardware value-chain segments and emphasizes that different hardware decisions materially affect total system cost [2].
- IDTechEx tracks software/AI, high-performance materials, and arm effectors alongside hardware components, highlighting the interaction between compute and mechanical design [1].

### 3.5 Supply-Chain Architecture & Tiering

The humanoid component supply chain is still immature. Many leading OEMs vertically integrate actuators and hands to protect IP and control cost, while commodity items such as connectors, fasteners, and standard sensors are sourced from established Tier-1/Tier-2 suppliers.

| Tier | Typical Role | Relevance to Humanoids |
|------|--------------|------------------------|
| Tier-2 | Materials, processed parts, and semiconductors | Magnet wire, rare-earth magnets, gear blanks, MEMS chips, battery cells, raw castings |
| Tier-1 | Subsystem/module suppliers | Actuator modules, battery packs, sensor modules, compute modules, cable harnesses |
| OEM / robot brand | System integration and final product | Tesla, Figure, Unitree, Agility, Apptronik, Boston Dynamics |
| Aftermarket / service | Spares, battery swap, refurbishment, recycling | Service networks, remanufacturing, closed-loop battery recovery |

**Sources and evidence**:
- Fraunhofer IPA argues that European component manufacturers can enter the emerging humanoid value chain by focusing on cost- and performance-relevant hardware components and collaborating early with humanoid OEMs [2].
- IDTechEx's market forecast segments humanoid component demand by actuators, motors, reducers, sensors, batteries, and high-performance materials, providing a demand-side view of supplier opportunities [1].
- *Speculative*: As production volumes grow, we expect Tier-1 module suppliers to consolidate around standardized actuator, battery, and compute platforms; today, however, OEM-specific designs dominate and vertical integration is high.

---

## 4. Relationship Patterns to Other Domains

| From | To | Relationship | Rationale |
|------|-----|--------------|-----------|
| `02_components_supply_chain` | `01_raw_materials` | `consumes` | Motors consume NdFeB magnets and copper; battery packs consume lithium cells; structures consume aluminum, magnesium, and composites |
| `03_manufacturing_processes` | `02_components_supply_chain` | `produces` | Motors are wound and assembled; gears are hobbed/ground; PCBs are fabricated and populated; cells are packaged into modules |
| `02_components_supply_chain` | `04_assembly_integration_testing` | `is_part_of` | Actuator modules, sensor suites, battery packs, and compute units are integrated and calibrated into the full robot |
| `02_components_supply_chain` | `05_mass_production` | `constrains` | Component cost, lead time, yield, and supplier capacity determine production ramp and unit economics |
| `02_components_supply_chain` | `06_design_engineering` | `enables` / `constrains` | Actuator torque density and sensor capability bound morphology, kinematics, and control architecture |
| `02_components_supply_chain` | `07_ai_models_algorithms` | `requires` / `enables` | VLAs require edge compute; force/torque sensors enable contact-rich learning; low-latency buses enable whole-body control |
| `11_applications_markets` | `02_components_supply_chain` | `drives_demand_for` | Industrial tasks drive requirements for payload, runtime, IP rating, and safety sensors |

---

## 5. Controlled Vocabulary

### 5.1 Category Tags

- `actuator`
- `motor`
- `reducer`
- `gearbox`
- `harmonic_drive`
- `cycloidal_drive`
- `planetary_gearbox`
- `quasi_direct_drive`
- `sensor`
- `camera`
- `lidar`
- `depth_sensor`
- `imu`
- `force_torque_sensor`
- `tactile_sensor`
- `encoder`
- `battery_pack`
- `bms`
- `edge_compute`
- `jetson`
- `end_effector`
- `robot_hand`
- `cable_harness`
- `structural_part`
- `tier1_supplier`
- `tier2_supplier`
- `component_manufacturer`
- `bill_of_materials`

### 5.2 Relevant Entity Types

From the project information model:

- `component`
- `tier1_supplier`
- `tier2_supplier`
- `component_manufacturer`
- `robot_system`
- `technology`
- `report`
- `standard`

---

## 6. Key Sources

### 6.1 Primary / Authoritative Sources

1. **IDTechEx**. *Humanoid Robots 2025-2035: Technologies, Markets and Opportunities* (2025). Component-level technical and cost analysis covering actuators, motors, reducers, screws, bearings, cameras, LiDAR, tactile sensors, batteries, and end effectors, plus 10-year market forecasts.  
   URL: https://www.idtechex.com/en/research-report/humanoid-robots/1093

2. **Fraunhofer IPA**. *The Humanoid Hardware Value Chain* (2026). White paper analyzing sensors, actuators, structure, and energy; builds a bottom-up cost model and identifies industrial gaps in component robustness, service life, and cost.  
   URL: https://www.ipa.fraunhofer.de/content/dam/ipa/de/documents/Publikationen/Studien/260219_Humanoid_Value_Chain_final.pdf

3. **Interact Analysis**. *Humanoid Robots and Lithium-Ion Batteries* (2026). Compares battery configurations across Tesla Optimus and Unitree H1 and discusses Li-ion chemistry choices and solid-state pilots.  
   URL: https://interactanalysis.com/insight/humanoid-robots-and-lithium-ion-batteries/

### 6.2 Industry and Product Sources

4. **Unitree Robotics**. *Unitree H1 Humanoid Robot — Product Specifications* (2025). Official product page listing joint torques, battery capacity, sensor suite, compute options, and dimensions.  
   URL: https://unitreerobotics.us/products/unitree-h1-humanoid-robot

5. **NVIDIA**. *Jetson AGX Orin Series* (official product page). Specifies up to 275 TOPS AI performance, 15–60 W power envelope, memory bandwidth, and camera/IO support.  
   URL: https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/

6. **Built In**. *What Is Figure AI Building?* (2024). Describes Figure 02 hardware including six RGB cameras, 2.25 kWh battery, 16-degree-of-freedom hands, and 3× compute improvement over Figure 01.  
   URL: https://builtin.com/articles/figure-ai

### 6.3 Domain-Specific / Technical Sources

7. **Pencic, M. et al.** *Development of the Low Backlash Planetary Gearbox for Humanoid Robots*. FME Transactions, vol. 45 (2017). Peer-reviewed comparison of a low-backlash planetary gearbox against a harmonic-drive baseline, reporting efficiency, load capacity, and cost trade-offs.  
   URL: https://www.mas.bg.ac.rs/_media/istrazivanje/fme/vol45/1/20_mpencic_et_al_doi.pdf

---

## 7. Open Questions

1. What is the current per-component cost breakdown and supplier mapping for commercially deployed humanoids (e.g., Unitree H1, Figure 02, Agility Digit) based on verified teardowns or OEM disclosures?
2. How will the choice between harmonic drive, cycloidal drive, planetary, and quasi-direct-drive architectures evolve as production volumes scale from hundreds to tens of thousands of units?
3. Which sensor and compute configurations are necessary versus sufficient for industrial tasks, and how do they trade off against battery runtime and thermal budget?
4. How should the ontology represent component variants (e.g., motor windings, gear ratios, battery chemistries) and multi-sourcing relationships across Tier-1 and Tier-2 suppliers?
