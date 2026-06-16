# Humanoid Robot Industry-Chain Ontology

> **Status**: Draft — subject to review before v0.1.0  
> **Purpose**: Provide a concept map for organizing all knowledge about humanoid robots, from upstream materials to downstream markets.

---

## 1. Why an Ontology?

A flat list of papers, companies, or products cannot capture the relationships that make humanoid robotics complex. For example:

- The price of neodymium magnets affects actuator cost.
- Actuator cost affects the robot's BOM and therefore its market price.
- Manufacturing yield affects whether a design can be mass-produced.
- Mass production economics determine which applications are profitable.

An ontology lets us express these dependencies and place every entry in context.

---

## 2. The Ten Domains

We divide the humanoid robot value chain into four layers and ten domains:

```
┌─────────────────────────────────────────────────────────────────┐
│                        UPSTREAM                                  │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │ 01 Raw Materials │  │ 02 Components   │  │ 03 Manufacturing │ │
│  │   & Resources    │  │   & Subsystems  │  │   Processes      │ │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘ │
└───────────┼────────────────────┼────────────────────┼──────────┘
            │                    │                    │
┌───────────┼────────────────────┼────────────────────┼──────────┐
│           ▼                    ▼                    ▼          │
│                        MIDSTREAM                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │ 04 Assembly,    │  │ 05 Mass         │  │ 06 Design &     │ │
│  │    Integration  │  │    Production   │  │    Engineering  │ │
│  │    & Testing    │  │    & Scaling    │  │                 │ │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘ │
└───────────┼────────────────────┼────────────────────┼──────────┘
            │                    │                    │
┌───────────┼────────────────────┼────────────────────┼──────────┐
│           ▼                    ▼                    ▼          │
│                     INTELLIGENCE LAYER                           │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │ 07 AI Models    │  │ 08 Software &   │  │ 09 Data &       │ │
│  │   & Algorithms  │  │   Middleware    │  │   Datasets      │ │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘ │
└───────────┼────────────────────┼────────────────────┼──────────┘
            │                    │                    │
┌───────────┼────────────────────┼────────────────────┼──────────┐
│           ▼                    ▼                    ▼          │
│              VALIDATION, DEPLOYMENT & MARKETS                    │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │ 10 Evaluation   │  │ 11 Applications │  │ 12 Policy,      │ │
│  │   & Benchmarks  │  │   & Markets     │  │   Regulation    │ │
│  │                 │  │                 │  │   & Ethics      │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. Domain Definitions

### 01 Raw Materials & Critical Resources

**Question**: What physical substances are required to build a humanoid robot?

- Rare-earth elements (neodymium, dysprosium, terbium) for high-performance motors
- Lithium, nickel, cobalt for batteries
- Copper for windings and wiring
- Aluminum, magnesium, carbon fiber for lightweight structures
- Silicon for compute chips and sensors
- Steel and titanium for load-bearing parts

**Why it matters**: Supply constraints and price volatility in raw materials directly affect robot cost and availability.

---

### 02 Components & Subsystems

**Question**: What are the major building blocks of a humanoid robot?

| Subsystem | Examples | Key Metrics |
|-----------|----------|-------------|
| Actuation | Electric motors, hydraulic actuators, pneumatic muscles, series elastic actuators | Torque density, speed, efficiency, cost |
| Power | Battery packs, power distribution, thermal management | Energy density, cycle life, charge time |
| Sensing | Cameras, LiDAR, IMU, tactile sensors, force/torque sensors, joint encoders | Resolution, latency, robustness, cost |
| Compute | Edge GPUs, embedded controllers, SOCs | TOPS, latency, power consumption |
| Structure | Skeleton, joints, links, end effectors | Strength-to-weight, manufacturability |
| Communication | Buses (CAN, EtherCAT), wireless | Bandwidth, latency, reliability |

**Why it matters**: Component performance determines what a robot can physically do and at what cost.

---

### 03 Manufacturing Processes

**Question**: How are the physical parts made?

- CNC machining, die casting, injection molding
- Additive manufacturing (metal / polymer 3D printing)
- Stator/rotor winding, magnet insertion
- Gear hobbing, grinding, honing for reducers
- PCB fabrication and SMT assembly
- Cable harness assembly
- Surface treatment and coating

**Why it matters**: Process choice determines precision, yield, cost, and scalability.

---

### 04 Assembly, Integration & Testing

**Question**: How is a humanoid robot put together and validated?

- Subassembly: legs, torso, arms, head, hands
- System integration: wiring, calibration, software flashing
- Test benches: joint performance, static/dynamic balance
- Hardware-in-the-loop (HIL) testing
- Environmental testing: temperature, vibration, dust
- Safety testing: collision behavior, emergency stop

**Why it matters**: This is where design intent meets physical reality. High integration complexity is a major bottleneck.

---

### 05 Mass Production & Scaling

**Question**: How do you go from one working robot to thousands?

- Factory layout and automation
- Supply chain coordination
- Quality control at scale
- BOM cost reduction
- Production ramp and yield curves
- Workforce and logistics

**Why it matters**: Many impressive lab robots never reach mass production. This domain separates prototypes from products.

---

### 06 Design & Engineering

**Question**: What determines the robot's physical form and capability?

- Degrees of freedom (DoF) and joint layout
- Kinematics and dynamics modeling
- Humanoid morphology trade-offs (height, weight, proportions)
- Structural design for falls and impacts
- Cable routing and maintenance access
- Safety design (round edges, pinch points, emergency release)

**Why it matters**: Design choices constrain everything downstream: cost, performance, reliability, and applications.

---

### 07 AI Models & Algorithms

**Question**: What intelligence enables the robot to perceive, decide, and act?

- **Perception**: visual processing, 3D reconstruction, object detection, tactile interpretation
- **Planning**: task planning, motion planning, footstep planning, manipulation planning
- **Control**: balance control, whole-body control, impedance/admittance control
- **Learning**: imitation learning, reinforcement learning, sim-to-real transfer
- **Foundation models**: VLAs, world models, LLM-based planners
- **Loco-manipulation**: combined locomotion and manipulation policies

**Why it matters**: This is the layer most public attention focuses on, but it is only meaningful when combined with capable hardware.

---

### 08 Software & Middleware

**Question**: What software infrastructure connects algorithms to hardware?

- Real-time operating systems and middleware (ROS 2, DDS, EtherCAT)
- Simulation environments (Isaac Sim, MuJoCo, Gazebo, Genesis)
- Digital twins
- Data logging and fleet management
- Calibration and diagnostics tools
- Deployment and update pipelines

**Why it matters**: Good software infrastructure determines development velocity, debugging capability, and fleet maintainability.

---

### 09 Data & Datasets

**Question**: What data is needed to train and evaluate humanoid robots?

- Teleoperation demonstrations
- Human motion capture
- Simulation-generated data
- Real-world interaction logs
- Multimodal datasets (vision, language, action, force)
- Data licensing and privacy

**Why it matters**: Data is the fuel for learning-based methods. High-quality, diverse data is often scarcer than algorithms.

---

### 10 Evaluation & Benchmarks

**Question**: How do we know a humanoid robot is good?

- Simulation benchmarks (Isaac Gym, HumanoidBench, etc.)
- Real-world task benchmarks
- Hardware-in-the-loop evaluation
- Metrics: success rate, energy efficiency, speed, robustness, safety
- Standards: ISO, IEEE, regional safety certifications

**Why it matters**: Without agreed-upon benchmarks, progress is hard to measure and compare.

---

### 11 Applications & Markets

**Question**: Where will humanoid robots actually be used?

- Manufacturing (assembly, inspection, material handling)
- Logistics (warehousing, last-mile delivery)
- Healthcare (assistance, rehabilitation, eldercare)
- Home services (cleaning, companionship, assistance)
- Retail and hospitality
- Research and education
- Defense and hazardous environments

**Why it matters**: Market demand shapes investment, product design, and technical priorities.

---

### 12 Policy, Regulation & Ethics

**Question**: What rules and norms govern humanoid robots?

- Safety standards and certifications
- Liability and insurance
- Labor market impact
- Privacy and surveillance
- Autonomy and human oversight
- Cultural acceptance and human-robot interaction norms

**Why it matters**: Regulation can accelerate or block deployment regardless of technical maturity.

---

## 4. Cross-Cutting Relationships

The domains are not independent. Key relationships include:

- **Raw materials → Components**: magnet supply affects motor performance and cost.
- **Components → Design**: actuator torque density determines feasible morphology.
- **Design → Manufacturing**: design for manufacturability (DFM) determines yield.
- **Manufacturing → Mass Production**: process capability determines scaling potential.
- **AI Models → Components**: algorithms can compensate for sensor/actuator limitations, or require better hardware.
- **Data → AI Models**: data availability constrains learning-based approaches.
- **Benchmarks → Applications**: benchmarks should reflect real deployment needs.
- **Policy → Applications**: regulation determines which markets are accessible.
- **Markets → Investment → R&D**: market pull drives upstream innovation.

These relationships are captured in per-domain documents through **cross-links**.

---

## 5. How Entries Are Tagged

Every entry in this project is tagged with:

- **Domain**: one or more of the ten domains above
- **Layer**: Upstream / Midstream / Intelligence / Validation-Markets
- **Entity type**: Company / Product / Paper / Dataset / Benchmark / Standard / Material / Process / Concept
- **Verification status**: Verified / Partially verified / Unverified / Speculative
- **Relevance score**: High / Medium / Low for humanoid robotics specifically

---

## 6. Open Questions for the Ontology

1. Should we add a dedicated domain for **economics / business models** (e.g., RaaS, leasing, CapEx vs OpEx)?
2. How should we represent **geographic supply-chain clusters** (e.g., Shenzhen ecosystem, German precision manufacturing)?
3. Should we track **failed companies and discontinued products** as learning cases?
4. How do we handle **dual-use technologies** (civilian and defense applications)?
