# RealMan Intelligent / RealMan

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 睿尔曼智能 |
| **English Name** | RealMan Robotic |
| **Headquarters** | Beijing, China |
| **Founded** | 2018 |
| **Website** | [https://www.realman-robotics.com](https://www.realman-robotics.com) |
| **Supply Chain Role** | Complete Machine OEM / Collaborative Robot / Humanoid Robot Components / Ultra-Lightweight Humanoid Robotic Arm |
| **Company Type** | Domestic brand, specializing in ultra-lightweight humanoid robotic arms |
| **Parent Company/Group** | None |
| **Data Source** | RealMan official website, product manuals, WAIC 2026 reports, public press releases |

## Company Profile

RealMan Intelligent is a technology company focused on the R&D and industrialization of ultra-lightweight humanoid robotic arms, known for its highly integrated joint modules and lightweight body design.

The core team comes from universities such as Beihang University. Products cover scientific research, education, commercial services, and upper-body solutions for humanoid robots. RealMan emphasizes human-like motion performance and a high payload-to-weight ratio. The representative product, RLM-63, is widely used in embodied intelligence, teleoperation, and commercial service scenarios.

## Product Line

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Ultra-Lightweight Humanoid Robotic Arm | Desktop/Service-level humanoid arm | RLM-63 / RLM-85 / RLM-100 | Scientific research & education, commercial services, humanoid robots |
| Humanoid Robot Solution | Upper-body integration (dual arms + torso) | RLM-H1 | Embodied intelligence, exhibition services |
| Joint Module | Integrated servo joint | RJM Series | Robotic arms, humanoid robots |

## Representative Products

### RLM-63 Ultra-Lightweight Humanoid Robotic Arm

> RLM-63: Please visit [official materials](https://www.realman-robotics.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Product Form | 6-DOF ultra-lightweight humanoid robotic arm | RealMan official website |
| Weight | Approx. 4.5 kg | Product manual |
| Payload | 3 kg | Product manual |
| Reach | Approx. 630 mm | Product manual |
| Degrees of Freedom | 6 DOF | Public specifications |
| Repeatability | ±0.05 mm | Product manual |
| End-Effector Speed | Not disclosed | - |
| Communication Interface | CAN / RS485 / EtherCAT (depending on configuration) | Product manual |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: Integrated joint module, high payload-to-weight ratio, humanoid configuration, supports ROS/ROS2 and secondary development, suitable for upper-body integration of humanoid robots.

**Application Scenarios**: Embodied intelligence data collection, dual-arm operation of service robots, scientific research & education, exhibition explanations, commercial unmanned retail.

### RJM Integrated Joint Module

> RJM Joint Module: Please visit [official materials](https://www.realman-robotics.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Product Form | Frameless torque motor + harmonic reducer + dual encoder | RealMan official website |
| Torque Range | Not disclosed | - |
| Control Mode | Position/Velocity/Torque | Product manual |
| Communication Interface | CAN / EtherCAT | Product manual |
| Protection Level | Not disclosed | - |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: Highly integrated joint design, can be directly used in humanoid robotic arms and humanoid robot joints, shortening the overall development cycle.

**Application Scenarios**: Joints for robotic arms, humanoid robots, and special-purpose robots.

## Supply Chain Position

- **Upstream Key Components/Materials**: Harmonic reducers, frameless torque motors, encoders, drivers, aluminum-magnesium alloy structural parts, control chips.
- **Downstream Customers/Application Scenarios**: Universities and research institutes, embodied intelligence startups, service robot OEMs, commercial integrators.
- **Main Competitors/Peers**: Dobot, AUBO, JAKA, Han's Robot, Universal Robots UR.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_realman`
- Product Entity: `ent_product_realman_rlm63`, `ent_component_realman_rjm`
- Key Relationships:
  - `ent_company_realman` -- `manufactures` --> `ent_product_realman_rlm63`
  - `ent_company_realman` -- `manufactures` --> `ent_component_realman_rjm`
  - `ent_product_realman_rlm63` -- `uses` --> `ent_component_realman_rjm`

## References

1. [RealMan Intelligent Official Website](https://www.realman-robotics.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. RealMan product manuals and public press releases
