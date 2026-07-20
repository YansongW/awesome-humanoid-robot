# DH-Robotics

> This entry belongs to [Appendix D: Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 大寰机器人 |
| **English Name** | DH-Robotics |
| **Headquarters** | Shenzhen, China |
| **Founded** | 2016 |
| **Website** | [https://www.dh-robotics.com](https://www.dh-robotics.com) |
| **Supply Chain Role** | Electric Grippers / Dexterous Hands / End Effectors |
| **Enterprise Attributes** | National High-Tech Enterprise, Specialized and New Enterprise |
| **Parent Company/Group** | Shenzhen DH-Robotics Technology Co., Ltd. |
| **Data Sources** | Official website, product manuals, public reports, WAIC 2026 reports |

## Company Overview

A leading domestic supplier of electric servo end effectors and dexterous hand core components.

DH-Robotics focuses on the R&D and mass production of electric grippers, servo electric cylinders, dexterous hands, and intelligent flexible motion systems. Its product line covers over 200 detailed models, including thin parallel grippers, adaptive grippers, and three-finger/five-finger dexterous hands, serving more than 800 customers in over 30 countries. Its solutions are characterized by integrated drive and control, precise force control, and fast response, and are widely used in 3C electronics, semiconductors, new energy lithium batteries, medical automation, and other scenarios.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| PGE Series Thin Parallel Grippers | Small size, fast response | PGE-2-12 / PGE-50-26 | 3C, Semiconductors, Lithium Batteries |
| AG/PGH Series Adaptive Grippers | Large stroke, force-controlled gripping | AG-160-95 / AG-95 | Industrial sorting, Collaborative robots |
| DH-5 Five-Finger Dexterous Hand | Highly integrated anthropomorphic dexterous hand | DH-5 | Humanoid robots, Scientific research |

## Representative Products

### DH-Robotics AG-160-95 Adaptive Gripper

> AG-160-95 Adaptive Gripper: Please visit [Official Documentation](https://www.dh-robotics.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | 184.6 × 162.3 × 67 mm | Third-party product page |
| Weight | Approx. 1 kg | Third-party product page |
| Degrees of Freedom | 1 DOF (Two-finger parallel) | Product manual |
| Gripping Force | 45–160 N per side | Third-party product page |
| Opening/Closing Speed | Opening/closing time approx. 0.9 s | Third-party product page |
| Repeatability | ±0.03 mm | Third-party product page |
| Supply Voltage | DC 24 V | Product manual |
| Communication Interface | Modbus RTU / I/O | Product manual |
| Price | Not disclosed | - |

**Technical Highlights**: Linkage and lead screw nut transmission, force-position hybrid control, IP54 protection, CE/FCC/RoHS certified, compatible with collaborative robots and automated production lines.

**Application Scenarios**: 3C assembly, lithium battery sorting, semiconductor handling, food packaging, collaborative robot loading/unloading.

### DH-Robotics DH-5 Dexterous Hand

> DH-5 Dexterous Hand: Please visit [Official Documentation](https://www.dh-robotics.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Not disclosed | - |
| Weight | Approx. 700 g | Public reports |
| Degrees of Freedom | 6 Active DOF / 11 Motion Joints | Public reports |
| Payload | Not disclosed | - |
| Fingertip Force Control | Integrated force sensors at fingertips | Public reports |
| Supply Voltage | DC 24 V | Product manual |
| Communication Interface | CAN / RS485 | Product manual |
| Price | Not disclosed | - |

**Technical Highlights**: Micro electric cylinder drive, linkage transmission, 7-series aluminum alloy frame, suitable for precise grasping in humanoid robots and scientific research validation.

**Application Scenarios**: Humanoid robot manipulation, service robots, education and research, prosthetics and rehabilitation.

## Supply Chain Position

- **Upstream Key Components/Materials**: Servo motors, ball screws/linkages, force/position sensors, aluminum alloy structural parts, driver ICs
- **Downstream Customers/Application Scenarios**: Collaborative robot manufacturers, 3C/new energy/semiconductor automation integrators, humanoid robot OEMs
- **Main Competitors/Peers**: Robotiq, SCHUNK, Junduo Robotics, Inspire Robots

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_dh_robotics`
- Product/Component Entity: `ent_product_dh_robotics_hand`
- Key Relationship:
  - `ent_company_dh_robotics` -- `manufactures` --> `ent_product_dh_robotics_hand`

## References

1. [Official Website](https://www.dh-robotics.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.dh-robotics.com) (Please verify against actual product models)
