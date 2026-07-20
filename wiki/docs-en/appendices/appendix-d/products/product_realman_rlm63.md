# RLM-63 Ultra-Lightweight Humanoid Robotic Arm

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [RealMan / RealMan](../companies/company_realman.md) |
| **Product Category** | Ultra-lightweight Humanoid Robotic Arm / Humanoid Robot Component |
| **Release Date** | Continuous iteration since the 2020s |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [https://www.realman-robotics.com](https://www.realman-robotics.com) |

## Product Overview

The RLM-63 is an ultra-lightweight humanoid robotic arm launched by RealMan, targeting embodied intelligence, service robots, and scientific research/education scenarios.

The product adopts an integrated joint module and lightweight structural design, achieving a 3 kg payload with 6 degrees of freedom human-like motion at a self-weight of 4.5 kg. It is suitable for use as the upper body dual arms of a humanoid robot or as a desktop-level manipulation platform.

## Product Image

> RLM-63: Please visit the [official website](https://www.realman-robotics.com) for details.

## Specification Parameter Table

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Product Form | 6-DOF Ultra-lightweight Humanoid Robotic Arm | RealMan official website |
| Self-weight | Approx. 4.5 kg | Product manual |
| Payload | 3 kg | Product manual |
| Reach | Approx. 630 mm | Product manual |
| Degrees of Freedom | 6 DOF | Public specifications |
| Repeatability | ±0.05 mm | Product manual |
| Maximum End-effector Speed | Not disclosed | - |
| Joint Range | Not disclosed | - |
| Communication Interface | CAN / RS485 / EtherCAT (depending on configuration) | Product manual |
| Protection Rating | Not disclosed | - |
| Price | Not disclosed | Subject to inquiry |

## Supply Chain Position

- **Manufacturer**: [RealMan / RealMan](../companies/company_realman.md)
- **Core Components/Technology Source**: Self-developed integrated joint modules, harmonic reducers, frameless torque motors, dual encoders, lightweight structural parts, controllers.
- **Downstream Applications/Customers**: Embodied intelligence startups, service robot OEMs, university research, commercial integrators.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_realman_rlm63`
- Manufacturer Entity: `ent_company_realman`
- Component Entity: `ent_component_realman_rjm`
- Key Relationships:
  - `rel_ent_company_realman_manufactures_ent_product_realman_rlm63` (`ent_company_realman` → `manufactures` → `ent_product_realman_rlm63`)
  - `ent_product_realman_rlm63` -- `uses` --> `ent_component_realman_rjm`

## Application Scenarios

- **Embodied Intelligence Data Collection**: Serves as a dual-arm manipulation platform for collecting imitation learning training data.
- **Service Robots**: Integrated into the upper body of humanoid robots for delivery, grasping, and interaction.
- **Scientific Research and Education**: Supports ROS/ROS2, suitable for research in robotics, motion planning, and human-robot interaction.
- **Commercial Display**: Exhibition hall explanations, coffee retail, unmanned retail scenarios.

## Competitive Comparison

| Comparison Item | RLM-63 | Main Competitors |
|-----------------|--------|------------------|
| Positioning | Ultra-lightweight Humanoid Robotic Arm | Desktop collaborative arm, humanoid robot arm |
| Core Advantage | Lightweight, high payload-to-weight ratio, humanoid configuration | Depends on specific model |
| Price | Not disclosed | Not disclosed |

## Selection and Deployment Suggestions

- Choose the RLM-63 / RLM-85 / RLM-100 series based on end-effector payload and reach requirements.
- Confirm compatibility of the communication interface (CAN/RS485/EtherCAT) with the main control system.
- When integrating into a humanoid robot, it is recommended to evaluate joint heat dissipation, cable routing, and overall stiffness matching.

## Related Entries

- [Manufacturer: RealMan / RealMan](../companies/company_realman.md)
- [Appendix D.4 Key Product Wiki](../index-products.md)

## References

1. [RealMan Official Website](https://www.realman-robotics.com)
2. RealMan RLM Series Product Manual
3. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
