# Unitree Robotics

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).  
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed".

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 宇树科技 |
| **English Name** | Unitree Robotics |
| **Headquarters** | Hangzhou, China |
| **Founded** | 2016 |
| **Website** | [https://www.unitree.com](https://www.unitree.com) |
| **Supply Chain Role** | OEM / Quadruped + Humanoid Robots, Self-developed Joint Motors |
| **Company Type** | Unicorn, Global Sales Leader in Quadruped Robots |
| **Parent Company/Group** | None |
| **Data Sources** | Unitree Official Website, IT Home, Robozaps, Third-party Product Databases |

## Company Overview

Unitree Robotics entered the market with cost-effective quadruped robots (robot dogs). In 2023, it released its first full-size humanoid robot, the H1, followed by the compact humanoid G1 in 2024.

The company insists on vertical integration of core components, self-developing the M107 permanent magnet synchronous motor, drivers, and whole-body motion control algorithms. Through its ROS2-compatible ecosystem and aggressive pricing strategy, it has become one of the highest-volume humanoid platforms among research institutions and developer communities.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| Full-size Humanoid | High-dynamic motion, research prototype | H1 / H1-2 | Research & education, AI embodied intelligence research |
| Compact Humanoid | Low-cost development platform | G1 / G1-Comp | Education, developers, light industry |
| Quadruped Robot | Inspection, transportation, research | Go2 / B2 / B2-W | Power inspection, emergency rescue, research |

## Representative Products

### Unitree H1

> Unitree H1: Please visit [Official Information](https://www.unitree.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | 180 cm | Unitree public info / Robozaps |
| Weight | 47 kg | Public specification |
| Degrees of Freedom | 26 DOF (base version) | Robozaps summary |
| Load/Torque | Knee joint peak torque 360 N·m | Public specification |
| Speed | Walking approx. 1.5 m/s; Running 3.3 m/s | Unitree claims world record |
| Battery Life | Approx. 1.5–2 h (864 Wh battery) | Public specification |
| Interface/Communication | Wi-Fi, Bluetooth, ROS2 / Unitree SDK | Public specification |
| Price | Approx. $90,000 / Approx. ¥650,000 domestically | Dealer and media reports |

**Technical Highlights**: M107 high torque density motor (189 N·m/kg), reinforcement learning-based gait, hot-swappable battery, OTA continuous updates.

**Application Scenarios**: Bipedal locomotion research, embodied intelligence algorithm validation, university laboratories.

### Unitree G1

> Unitree G1: Please visit [Official Information](https://www.unitree.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | 127 cm | Public specification |
| Weight | Approx. 35 kg | Public specification |
| Degrees of Freedom | 23–43 DOF (including dexterous hand configuration) | Unitree configuration differences |
| Load/Torque | Payload approx. 2 kg | Humanoid.Guide |
| Speed | Approx. 2 m/s | Public specification |
| Battery Life | Approx. 2 h | Public specification |
| Interface/Communication | Wi-Fi, Bluetooth, ROS2 | Public specification |
| Price | Approx. $16,000 / Starting at ¥99,000 domestically | Media reports |

**Technical Highlights**: Three-finger force-controlled dexterous hand, Intel RealSense / LIVOX sensors, low cost and high accessibility.

**Application Scenarios**: Educational demonstrations, AI research, light logistics and commercial displays.

## Supply Chain Position

- **Upstream Key Components/Materials**: Self-developed M107 motors and drivers, externally purchased reducers, bearings, batteries, vision sensors (see [Chapter 4 Actuators](../../../chapters/chapter-04.md)).
- **Downstream Customers/Application Scenarios**: Universities, research institutes, developers, logistics and security customers.
- **Main Competitors/Peers**: UBTECH Walker, Fourier GR-1, Tesla Optimus.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_unitree`
- Product Entities: `ent_product_unitree_h1`, `ent_product_unitree_g1`
- Key Relationships:
  - `ent_company_unitree` -- `manufactures` --> `ent_product_unitree_h1`
  - `ent_company_unitree` -- `manufactures` --> `ent_product_unitree_g1`
  - `ent_product_unitree_h1` -- `uses` --> `ent_component_unitree_m107_motor`

## References

1. [Unitree Official Website](https://www.unitree.com)
2. [Robozaps – Unitree H1 Review](https://blog.robozaps.com/b/unitree-h1-review)
3. [Humanoid.Guide – Unitree G1](https://humanoid.guide/product/g1/)
4. [IT Home – Unitree Humanoid Robot Report](https://www.ithome.com)
5. [Appendix D.4 Key Product Wiki](../index-products.md)
