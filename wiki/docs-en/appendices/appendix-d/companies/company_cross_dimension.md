# Cross-Dimension / DexForce

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).  
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 跨维智能 (Cross-Dimension (Shenzhen) Intelligent Digital Technology Co., Ltd.) |
| **English Name** | Cross-Dimension / DexForce |
| **Headquarters** | Shenzhen, China (Branch offices in Beijing, Shanghai, Zhuhai) |
| **Founded** | June 2021 |
| **Website** | [https://www.dexforce.com](https://www.dexforce.com) |
| **Supply Chain Role** | Sensors / Embodied AI & 3D Vision |
| **Enterprise Type** | National High-Tech Enterprise, Embodied Intelligence Solution Provider |
| **Parent/Group** | None |
| **Data Source** | Cross-Dimension official website, WAIC 2026 exhibitor list, Jiqizhixin, PingWest |

## Company Overview

Cross-Dimension is a national high-tech enterprise centered on Sim2Real, focusing on highly generalizable embodied intelligence technology. The company team is led by top 2% global scientists and has accumulated deep expertise in 3D generative AI, multimodal large models, and robotic applications, aiming to achieve large-scale commercial deployment of embodied intelligence through its self-developed engine.

The company has built a hardware-software integrated product matrix including the DexVerse™ embodied intelligence engine, DexSense pure vision spatial and embodied intelligence sensors, and the DexForce W1 / W1 Pro general-purpose humanoid robot. Its core business model is to use simulation to generate massive synthetic data, train VLA models, and directly transfer them to real robots, thereby shortening the deployment cycle for robots entering new scenarios. As of 2026, Cross-Dimension has served over 30 industries including automotive, 3C, semiconductors, home appliances, and logistics.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|-------------------------|-------------------|
| Embodied Intelligent Robots | Deployable high-precision mobile manipulation platforms | DexForce W1 / W1 Pro | Scientific research & education, commercial services, intelligent manufacturing |
| Intelligent Vision Sensors | Pure vision 3D perception and spatial intelligence | DexSense | Industrial loading/unloading, depalletizing, quality inspection |
| Embodied Intelligence Engine | Sim2Real data generation and model training | DexVerse™ / EmbodiChain | Algorithm development, scenario deployment |

## Representative Products

### DexForce W1 Pro

> DexForce W1 Pro: Please visit [official materials](https://www.dexforce.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 170 cm (full size) | Official public information |
| Weight | Not disclosed | - |
| Degrees of Freedom | 34+ power units / optional 6-DOF dexterous hand or two-finger gripper | PingWest |
| Payload/Torque | Not disclosed | - |
| Speed/RPM | Not disclosed | - |
| Battery Life | Not disclosed | - |
| Interface/Communication | Supports EmbodiChain development platform, ROS/Modbus/TCP | Official website |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: Self-developed pure vision binocular sensor (frame rate 60 Hz, binocular calibration error ≤±0.05 pixels), Engine-driven Sim2Real VLA, full-body harmonic joints and omnidirectional mobile chassis, repeat positioning accuracy ≤0.5 mm.

**Application Scenarios**: High-precision flexible assembly, inspection with manipulation, material sorting, home assistant, commercial guidance, and scientific research & education.

### DexSense Pure Vision Sensor

> DexSense: Please visit [official materials](https://www.dexforce.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Not disclosed | - |
| Weight | Not disclosed | - |
| Field of View | Horizontal 90° / Vertical 60° (human-like vision) | PingWest |
| Depth Accuracy | 3D contour reconstruction error ≤1 mm | PingWest |
| Frame Rate | Up to 60 Hz | PingWest |
| Interface/Communication | Supports TCP / Modbus | Official website |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: Pioneering binocular estimation large model, zero-shot depth estimation for any scene; microsecond-level multi-camera synchronization; enables rapid simulation-to-real transfer in DexVerse.

**Application Scenarios**: Unordered grasping, depalletizing, positioning assembly, industrial quality inspection.

## Supply Chain Position

- **Upstream Key Components/Materials**: Self-developed pure vision sensors and algorithms; externally purchased harmonic reducers, motors, computing units, structural parts.
- **Downstream Customers/Application Scenarios**: Leading manufacturing clients such as GAC, Midea, Haier, Panasonic, Lens Technology; scientific research & education, commercial service integrators.
- **Main Competitors/Peers**: Mech-Mind, Orbbec, Zhiyuan Robot.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_cross_dimension`
- Product Entities: `ent_product_cross_dimension_dexforce_w1_pro`, `ent_product_cross_dimension_dexsense`
- Key Relationships:
  - `ent_company_cross_dimension` -- `manufactures` --> `ent_product_cross_dimension_dexforce_w1_pro`
  - `ent_company_cross_dimension` -- `manufactures` --> `ent_product_cross_dimension_dexsense`

## References

1. [Cross-Dimension Official Website](https://www.dexforce.com)
2. [WAIC 2026 Exhibitor List - Jufair](https://www.jufair.com/information/319685.html)
3. [PingWest – Cross-Dimension Launches DexForce W1 Pro](https://www.pingwest.com/a/306441)
4. [Jiqizhixin – From Spatial Intelligence to Embodied Intelligence](https://www.jiqizhixin.com)
