# 04 Assembly, Integration & Testing

> **Domain Code**: `04_assembly_integration_testing`  
> **Layer**: Midstream  
> **Status**: Draft — subject to review before v0.1.0  
> **Purpose**: Define the assembly, integration, and testing concepts that turn humanoid robot components into validated systems, and establish how this domain links to the rest of the value chain.

---

## 1. Central Question

> **How does a humanoid robot go from a pile of components to a calibrated, validated, and deployable product?**

A humanoid robot is one of the most mechanically and software-dense products in modern manufacturing. Dozens of high-precision actuators, sensors, compute units, and wiring harnesses must be assembled into a kinematic chain, calibrated to sub-millimeter accuracy, and validated against safety and performance requirements before the robot can leave the factory. This domain tracks that transition from parts to product.

---

## 2. Scope

### 2.1 In Scope

- Subassembly of major mechanical modules: legs, torso, arms, head, and hands.
- System integration: wiring, connectors, compute, power distribution, and software flashing.
- Kinematic and sensor calibration (joint encoders, IMU, force/torque, vision).
- Test benches for joint performance, static/dynamic balance, and whole-body behavior.
- Hardware-in-the-loop (HIL) and software-in-the-loop (SIL) validation.
- Safety validation: collision behavior, emergency stop, force/pressure limits.
- Environmental testing: temperature, vibration, dust, ingress protection.
- Quality gates, traceability records, and factory acceptance criteria.

### 2.2 Out of Scope

- Design of individual components (covered in `02_components_supply_chain` and `06_design_engineering`).
- Manufacturing processes that produce raw parts (covered in `03_manufacturing_processes`).
- Mass-production line economics and yield optimization (covered in `05_mass_production`).
- Training of AI models and policies (covered in `07_ai_models_algorithms`).
- Field deployment and application economics (covered in `11_applications_markets`).

---

## 3. Key Concepts

### 3.1 Subassembly and Modular Integration

Humanoid robots are typically integrated as a stack of subassemblies rather than as a monolithic build. This modularity is essential for diagnostics, repair, and eventual mass production.

| Subassembly | Typical Contents | Integration Risk |
|-------------|------------------|------------------|
| Legs | Hip/knee/ankle actuators, foot force sensors, IMU mounts | Alignment of bipedal kinematic chain; backlash accumulation |
| Torso | Battery pack, main compute, power distribution, spine joints | Thermal management; cable routing through moving joints |
| Arms | Shoulder/elbow/wrist actuators, tactile sensors | Hand-eye coordination depends on arm link-length accuracy |
| Head | Cameras, LiDAR, microphones, display/speaker | Multi-sensor extrinsic calibration to neck kinematics |
| Hands | Finger actuators, tactile arrays, tendon/cable drives | High part count; fine mechanical adjustment |

**Sources and evidence**:
- Boston Dynamics describes its electric Atlas as built for enterprise applications, incorporating lessons from real-world testing, with iterative gripper design and full-body control integration [Boston Dynamics Atlas 2026].
- Fraunhofer IPA’s KMUmanoid project builds a gearbox-assembly demonstrator to study how humanoid robots can be integrated into SME workflows, emphasizing accessibility, safety distances, and space requirements [Fraunhofer IPA 2026].
- Industry deployment data show that automotive pilots (BMW Figure 02, Mercedes Apollo, Tesla Optimus, Hyundai Atlas) currently perform limited subtasks such as material handling and parts delivery, indicating that full integration into complex assembly workflows remains at pilot stage [IDTechEx Humanoid Robots 2025; Fraunhofer IPA 2026].

### 3.2 Calibration and Kinematic Identification

Calibration transforms nominal CAD dimensions and sensor readings into a consistent body schema that the control software can trust. Without it, repeatability degrades and manipulation accuracy collapses.

| Calibration Target | What is Estimated | Why It Matters |
|--------------------|-------------------|----------------|
| Joint encoder zero offset | Absolute zero position of each rotational joint | Repeatable startup pose and trajectory execution |
| Link lengths / joint axes | Denavit-Hartenberg or URDF geometric parameters | Accuracy of forward/inverse kinematics and footstep planning |
| IMU alignment | Orientation of IMU frame relative to pelvis/torso | Correct state estimation for balance control |
| Camera-hand (eye-hand) | Extrinsic transform from camera to end-effector | Precision grasping and visual servoing |
| Force/torque sensor | Bias, scaling, cross-talk, mounting orientation | Safe contact detection and impedance control |

**Sources and evidence**:
- A Frontiers in Robotics and AI paper on the iCub humanoid robot presents a markerless eye-hand kinematic calibration method using sequential Monte Carlo parameter estimation to estimate joint offsets β along the head-to-hand kinematic chain, significantly reducing projection error between perceived and simulated hand pose [Vicente et al. 2018].
- Related work in humanoid calibration notes that cross-calibrating vision sensors, an IMU, and their relation to a humanoid’s kinematic chain is harder than calibrating individual sensors, and that automated methods are faster and more accurate than manual tuning [Vicente et al. 2018].

### 3.3 Test Benches and Hardware-in-the-Loop (HIL) Validation

Before a humanoid is allowed to walk, each subsystem is exercised on specialized test equipment. HIL bridges simulation and physical testing by connecting real controllers to simulated plants.

| Test Type | Purpose | Typical Equipment |
|-----------|---------|-------------------|
| Joint-level test bench | Torque/speed/friction characterization, backlash measurement | Dynamometer, torque sensor, encoder reference |
| Static balance platform | Center-of-pressure, weight distribution, foot force calibration | Force plates, motion-capture reference |
| Dynamic gait test rig | Walking, stepping, disturbance rejection in a harness | Overhead gantry or tether, instrumented floor |
| Manipulation test stand | Grasp policies, gripper durability, force control | Object sets, force/torque sensor, vision system |
| Hardware-in-the-loop (HIL) | Validate controller firmware against simulated robot/environment | Real-time simulator (dSPACE, Speedgoat, NI), DUT controller |

**Sources and evidence**:
- MathWorks documentation defines HIL testing as connecting real controller hardware to a real-time simulated plant via analog/digital signals and protocols such as CAN and Ethernet, enabling validation before the full physical system is available [MathWorks HIL 2025].
- Fraunhofer IPA’s humanoid benchmark records objective measurements using a 3D tracking system and force sensors across six modules: technologies/basic capabilities, complex capabilities, cleanroom suitability, functional safety, cybersecurity, and energy efficiency [Fraunhofer IPA 2026].
- A study on electromechanical actuators notes that HIL variants include signal/computer HIL (sHIL/cHIL), power HIL (pHIL), and mechanical HIL (mHIL), and that these techniques require real-time simulation to capture dynamics, delays, and computational load [MathWorks HIL 2025].

### 3.4 Safety and Environmental Validation

Humanoid robots inherit hazards from industrial robots, mobile robots, powered machinery, and battery systems. Current deployments rely on a patchwork of existing standards because no dedicated humanoid safety standard is yet published.

| Standard / Framework | Scope | Relevance to Humanoids |
|----------------------|-------|------------------------|
| ISO 10218-1:2025 | Industrial robot design safety | Robot design, actuators, emergency stop, protective stop |
| ISO 10218-2:2025 | Industrial robot system integration | Cell layout, risk assessment, safeguarding, validation |
| ISO/TS 15066:2016 | Collaborative robots (merged into ISO 10218-2:2025) | Power/force limiting, speed/separation monitoring, biomechanical thresholds |
| ISO 13482:2014 | Personal care robots | Service/home humanoids; stability, collision avoidance, fail-safe behavior |
| ISO 25785-1 (proposed) | Dynamically stable humanoid robots | Bipedal locomotion and balance hazards — not yet published |

**Sources and evidence**:
- ISO/TS 15066:2016 defines biomechanical force/pressure thresholds by body region (e.g., skull/forehead transient force 130 N, chest 140 N, hand/fingers 140 N) based on pain-threshold research, and specifies four collaborative modes including power/force limiting and speed/separation monitoring [ISO/TS 15066:2016].
- Fraunhofer IPA’s benchmark found that Unitree G1 collision forces can exceed 500 N — well above the pain thresholds permitted by ISO/TS 15066 — highlighting a gap between current hardware and collaborative force limits [Fraunhofer IPA 2026].
- ISO 13482:2014 addresses mobile servant, physical assistant, and person-carrier robots; it is the most relevant published standard for service-oriented humanoids and covers stability, collision avoidance, and fail-safe behavior [ISO 13482:2014].

### 3.5 Software Integration and Firmware Flashing

Integration is not only mechanical. Middleware, real-time operating systems, device drivers, safety controllers, and AI inference stacks must boot, synchronize, and recover from faults.

| Layer | Integration Concern | Typical Artifacts |
|-------|---------------------|-------------------|
| Real-time control | Joint controllers, safety-rated stops, watchdogs | EtherCAT/CAN bus configuration, servo drive parameters |
| Middleware | Communication between perception, planning, and control | ROS 2, DDS, shared memory, time synchronization (PTP) |
| Perception/AI stack | Camera, LiDAR, IMU fusion; policy inference | Calibration files, model weights, runtime pipelines |
| Fleet/cloud | OTA updates, mission scheduling, telemetry | Update packages, rollback images, incident logs |
| Digital twin | Virtual commissioning before physical build | Simulation model synchronized with production configuration |

**Sources and evidence**:
- Boston Dynamics integrates Atlas with its Orbit fleet-management platform for site maps, mission scheduling, remote camera access, and manual inspections, illustrating the software layer required to scale from single robots to fleets [Boston Dynamics Atlas 2026].
- Calibration literature emphasizes that camera, IMU, and kinematic calibration files are software artifacts that must be loaded and version-controlled alongside firmware [Vicente et al. 2018].

---

## 4. Relationship Patterns to Other Domains

| From | To | Relationship | Rationale |
|------|-----|--------------|-----------|
| `04_assembly_integration_testing` | `02_components_supply_chain` | `integrates` | Assembly domain integrates motors, sensors, batteries, compute, and structural parts into a robot system. |
| `04_assembly_integration_testing` | `03_manufacturing_processes` | `consumes` / `is_prerequisite_for` | Assembly consumes manufactured parts; process capability (tolerances, surface finish) determines assembly yield. |
| `04_assembly_integration_testing` | `05_mass_production` | `is_prerequisite_for` | A validated assembly and test workflow is prerequisite for repeatable mass production. |
| `04_assembly_integration_testing` | `06_design_engineering` | `constrains` / `is_constrained_by` | Assembly feasibility and serviceability constrain design; design choices determine the assembly sequence. |
| `04_assembly_integration_testing` | `07_ai_models_algorithms` | `requires` / `is_validated_by` | Integrated software requires AI models; test benches and real-world pilots validate control and perception policies. |
| `04_assembly_integration_testing` | `08_software_middleware` | `requires` | System integration depends on real-time OS, middleware (ROS 2 / DDS), and communication buses. |
| `04_assembly_integration_testing` | `10_evaluation_benchmarks` | `is_evaluated_by` | Assembly quality, calibration accuracy, and safety are evaluated against benchmarks and standards. |
| `04_assembly_integration_testing` | `11_applications_markets` | `is_prerequisite_for` | A validated robot is prerequisite for field deployment in factories, logistics, or services. |
| `04_assembly_integration_testing` | `12_policy_regulation_ethics` | `is_regulated_by` | Safety, environmental, and cybersecurity testing are regulated by standards and conformity-assessment rules. |

---

## 5. Controlled Vocabulary

### 5.1 Assembly / Integration / Testing Categories

- `subassembly`
- `system_integration`
- `calibration`
- `kinematic_identification`
- `test_bench`
- `hardware_in_the_loop` (`HIL`)
- `software_in_the_loop` (`SIL`)
- `safety_validation`
- `environmental_testing`
- `firmware_flashing`
- `OTA_update`
- `quality_gate`
- `digital_twin_commissioning`
- `factory_acceptance_test`

### 5.2 Relevant Entity Types

From the project information model:

- `process`
- `tool_equipment`
- `facility`
- `system`
- `standard`
- `benchmark`

---

## 6. Key Sources

### 6.1 Primary / Authoritative Sources

1. **Fraunhofer IPA**. *Standardized analyses for application-relevant criteria of humanoid robots* (2026). Describes a six-module benchmark (basic capabilities, complex capabilities, cleanroom, functional safety, cybersecurity, energy efficiency) applied to Unitree G1; reports collision forces >500 N and operating times of 2 h 49 min standing / 1 h 49 min mixed standing-walking. Also covers the KMUmanoid gearbox-assembly demonstrator for SME integration.  
   URL: https://silicon-saxony.de/en/fraunhofer-ipa-standardized-analyses-for-application-relevant-criteria-of-humanoid-robots/; https://silicon-saxony.de/en/fraunhofer-ipa-kmumanoid-project-tests-humanoid-robots-for-smes/

2. **International Organization for Standardization (ISO)**. *ISO 10218-1:2025 Robots and robotic devices — Safety requirements for industrial robots — Part 1: Robots* and *ISO 10218-2:2025 Part 2: Robot systems and integration* (2025). Core safety standards for robot design and integration; the 2025 revisions integrate collaborative-robot requirements and add cybersecurity considerations.  
   URL: https://www.iso.org/standard/86780.html (Part 1); https://www.iso.org/standard/86781.html (Part 2)

3. **International Organization for Standardization (ISO)**. *ISO/TS 15066:2016 Collaborative robots — Safety requirements* (2016). Defines power/force limiting, speed/separation monitoring, hand guiding, and biomechanical contact thresholds by body region. Content merged into ISO 10218-2:2025.  
   URL: https://www.iso.org/standard/62996.html

4. **International Organization for Standardization (ISO)**. *ISO 13482:2014 Robots and robotic devices — Safety requirements for personal care robots* (2014). Safety requirements for mobile servant, physical assistant, and person-carrier robots; most relevant existing standard for service-oriented humanoids.  
   URL: https://www.iso.org/standard/53820.html

### 6.2 Industry and Market Analysis

5. **IDTechEx**. *Humanoid Robots 2025-2035: Technologies, Markets and Opportunities* (2025). Tracks component integration, automotive pilot deployments, and market timelines; identifies automotive and logistics as lead sectors.  
   URL: https://www.idtechex.com/en/research-report/humanoid-robots/1093

6. **Boston Dynamics**. *Atlas Humanoid Robot* (2026). Official product page describing electric Atlas enterprise readiness, integration roadmap, Orbit fleet software, and field testing at Hyundai.  
   URL: https://bostondynamics.com/products/atlas/

### 6.3 Domain-Specific Sources

7. **Vicente P., Jamone L., Bernardino A.** "Markerless Eye-Hand Kinematic Calibration on the iCub Humanoid Robot." *Frontiers in Robotics and AI* 5:46 (2018). Open-access paper on estimating joint offsets along the eye-hand kinematic chain using sequential Monte Carlo parameter estimation.  
   URL: https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2018.00046/full

8. **MathWorks**. "What Is Hardware-in-the-Loop (HIL)?" (2025). Engineering guide explaining HIL architecture, MIL/SIL/PIL/HIL differences, and real-time simulator interfaces.  
   URL: https://www.mathworks.com/discovery/hardware-in-the-loop-hil.html

---

## 7. Open Questions

1. What is the optimal modular assembly sequence and tooling set for high-DoF humanoid robots, and how does it change from pilot builds to mass production?
2. How should joint-offset, IMU, and eye-hand calibration drift be monitored and corrected automatically across a deployed fleet?
3. When ISO 25785-1 or equivalent humanoid-specific safety standards are published, how will they change test-bench requirements and acceptance criteria?
4. To what extent can HIL, SIL, and digital-twin commissioning reduce the number of physical prototypes and field-test hours required before commercial release?
