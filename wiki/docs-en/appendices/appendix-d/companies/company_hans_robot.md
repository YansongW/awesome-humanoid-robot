# Han's Robot

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 大族机器人 |
| **English Name** | Han's Robot |
| **Headquarters** | Shenzhen, Guangdong, China |
| **Founded** | 2017 (originating from the motor robotics division of Han's Laser) |
| **Website** | [https://www.hansrobot.com](https://www.hansrobot.com) |
| **Supply Chain Role** | OEM / Collaborative Robots / Humanoid Robot Components |
| **Company Type** | Domestic brand, Han's Laser group, core collaborative robot manufacturer |
| **Parent Company/Group** | Han's Laser Technology Industry Group Co., Ltd. (002008.SZ) |
| **Data Sources** | Han's Robot official website, product manuals, WAIC 2026 reports, public press releases |

## Company Overview

Han's Robot was incubated internally by Han's Laser, focusing on the R&D and industrialization of intelligent collaborative robots, with the Elfin series of collaborative arms as its core product.

The company inherits its parent company's capabilities in precision manufacturing and motion control. Its product portfolio covers payloads from 3 to 20 kg, emphasizing ease of use, safety, and an open ecosystem. Han's Robot is also developing composite mobile robots, force-controlled polishing, and medical rehabilitation robots, and actively participates in the R&D of core components for humanoid robots.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| Collaborative Robots | Industrial/Commercial/Scientific | Elfin 3 / Elfin 5 / Elfin 10 | 3C, Automotive, Medical, Food |
| Composite Robots | Mobile Collaboration | Han's AMR + Elfin | Logistics, Flexible Production Lines |
| Smart Applications | Force-Controlled Polishing, Welding, Machine Tending | Industry Solutions | Metalworking, Automotive |

## Representative Products

### Elfin 5 Collaborative Robot

> Elfin 5: Please visit the [official page](https://www.hansrobot.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Product Type | 6-DOF Collaborative Robot | Han's Robot official website |
| Weight | Approx. 24 kg | Product manual |
| Payload | 5 kg | Product manual |
| Reach | 950 mm | Product manual |
| Degrees of Freedom | 6 DOF | Public specification |
| Repeatability | ±0.03 mm | Product manual |
| Maximum End-Effector Speed | Not disclosed | - |
| Ingress Protection | IP54 | Product manual |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: Dual-joint modular design, drag teaching, graphical programming, collision detection, open ROS/ROS2 interface.

**Application Scenarios**: 3C assembly, automotive parts machine tending, medical sample handling, food packaging, force-controlled polishing.

### Elfin 10 Collaborative Robot

> Elfin 10: Please visit the [official page](https://www.hansrobot.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Product Type | 6-DOF Collaborative Robot | Han's Robot official website |
| Weight | Approx. 38 kg | Product manual |
| Payload | 10 kg | Product manual |
| Reach | 1300 mm | Product manual |
| Degrees of Freedom | 6 DOF | Public specification |
| Repeatability | ±0.05 mm | Product manual |
| Ingress Protection | IP54 | Product manual |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: High payload with long reach, suitable for heavy-duty collaborative tasks such as material handling, palletizing, and machine tending.

**Application Scenarios**: Automotive assembly, logistics handling, metalworking, food & beverage, new energy battery production lines.

## Supply Chain Position

- **Upstream Key Components/Materials**: Harmonic drives, servo motors, encoders, controllers, structural parts, cables, sensors.
- **Downstream Customers/Application Scenarios**: 3C electronics, automotive, new energy, medical, food, metalworking.
- **Main Competitors/Peers**: JAKA, AUBO, Yuejiang, Universal Robots (UR), ROKAE.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_hans_robot`
- Product Entities: `ent_product_hans_elfin5`, `ent_product_hans_elfin10`
- Key Relationships:
  - `ent_company_hans_robot` -- `manufactures` --> `ent_product_hans_elfin5`
  - `ent_company_hans_robot` -- `manufactures` --> `ent_product_hans_elfin10`

## References

1. [Han's Robot Official Website](https://www.hansrobot.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. Han's Robot product manuals and public press releases
