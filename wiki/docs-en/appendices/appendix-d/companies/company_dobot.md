# Yuejiang Technology / Dobot / Yuejiang Technology

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 越疆科技 |
| **English Name** | Dobot / Yuejiang Technology |
| **Headquarters** | Shenzhen, Guangdong, China |
| **Founded** | 2015 |
| **Website** | [https://www.dobot.cn](https://www.dobot.cn) |
| **Supply Chain Role** | Complete Machine OEM / Collaborative Robots + Humanoid Robots + Teleoperation Training Platform |
| **Enterprise Attribute** | Leading collaborative robot company extending into embodied intelligence |
| **Parent Company/Group** | None |
| **Data Source** | Yuejiang official website, Dobot X-Trainer user manual and brochure, 36Kr |

## Company Overview

Yuejiang Technology started with collaborative robots and has gradually entered the fields of embodied intelligent robots, teleoperation data training platforms, and humanoid robots.

Yuejiang has product lines including CRA, CR, Nova, MG400, X-Trainer, and Magician for collaborative and educational robots, with industry-leading cumulative shipments. Since 2024, it has launched the X-Trainer dual-arm teleoperation AI training platform for research and data collection teams; in 2025, it released the industrial humanoid robot ATOM-M, targeting flexible manufacturing scenarios in automotive, electronics, and semiconductor industries.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| Collaborative Robots | Industrial, Commercial, Education | CRA / CR / Nova / MG400 | 3C, Automotive, Research & Education |
| Embodied Intelligence & Humanoid | Teleoperation Training, Industrial Humanoid | X-Trainer / ATOM-M | Data Collection, Automotive & Electronics Flexible Production Lines |

## Representative Products

### Dobot X-Trainer

![Dobot X-Trainer](https://www.dobot-robots.com/media/upload/2024/x-trainer/tab.png)

> Image source: Dobot official product image.

| Specification | Value | Remarks/Source |
|---|---|---|
| Dimensions | Base 1400×1000 mm (lightweight version, without handles) | Dobot X-Trainer User Manual |
| Weight | Not disclosed | - |
| Degrees of Freedom | Master hand 6-DOF×2, Slave hand Nova 2 collaborative arm×2 | User Manual |
| Payload/Torque | Single arm can carry 2 kg, dual arms 3 kg; gripper max stroke 95 mm | Brochure |
| Speed/Rotation Speed | End-effector max speed 1.6 m/s | Brochure |
| Battery Life | Mains powered | - |
| Interfaces/Communication | Gigabit Ethernet, USB, WiFi (Nova 2 optional) | User Manual |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: Industrial-grade Nova 2 collaborative arm as slave hand, ±0.05 mm repeat positioning accuracy, 25 Hz end-to-end motion interface, VR/controller teleoperation, data collection SDK

**Application Scenarios**: Embodied intelligence data collection, imitation learning, research & education, AGI scenario simulation and competition.

### Dobot ATOM-M

> Dobot ATOM-M: Please visit [official materials](https://www.dobot.cn) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Dimensions | Not disclosed | - |
| Weight | Not disclosed | - |
| Degrees of Freedom | Not disclosed | - |
| Payload/Torque | Not disclosed | - |
| Speed/Rotation Speed | Not disclosed | - |
| Battery Life | Not disclosed | - |
| Interfaces/Communication | Not disclosed | - |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: Wheeled humanoid integrated whole-body control, hand-eye-foot coordination, dual-arm high-precision operation, suitable for automotive/electronics/semiconductor multi-variety small-batch flexible production

**Application Scenarios**: Flexible manufacturing, unmanned workshop handling and assembly.

## Supply Chain Position

- **Upstream Key Components/Materials**: Self-developed collaborative robot joints, motors, reducers, controllers; Intel RealSense D405 depth camera; NVIDIA Jetson computing platform.
- **Downstream Customers/Application Scenarios**: University research, industrial data collection teams, automotive/electronics/semiconductor manufacturers.
- **Main Competitors/Peers**: Universal Robots UR, Fanuc, AUBO, JAKA, Han's Robot

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_dobot`
- Product Entity: `ent_product_dobot_x_trainer`
- Component Entity: `ent_component_dobot_nova2`
- Key Relationships:
  - `ent_company_dobot` -- `manufactures` --> `ent_product_dobot_x_trainer`
  - `ent_company_dobot` -- `manufactures` --> `ent_component_dobot_nova2`
  - `ent_product_dobot_x_trainer` -- `uses` --> `ent_component_dobot_nova2`

## References

1. [Dobot X-Trainer Product Page](https://www.dobot-robots.com/products/humanoid-robots/x-trainer.html)
2. [Dobot X-Trainer Brochure](https://www.roscomponents.com/wp-content/uploads/2026/02/X-Trainer-leaflet-Lightweight-Base_Brochure.pdf)
3. [Yuejiang Technology Official Website](https://www.dobot.cn)
