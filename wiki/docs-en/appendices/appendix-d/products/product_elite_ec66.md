# Elite Robot EC66 Collaborative Robot

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Table of Contents](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Elite Robot](../companies/company_elite_robot.md) |
| **Product Category** | Collaborative Robot |
| **Release Date** | Continuous iteration since 2018 |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [https://www.elite-robot.com](https://www.elite-robot.com) |

## Product Overview

The EC66 is a 6-degree-of-freedom collaborative robot launched by Elite Robot, with a payload of 6 kg and a reach of 914 mm, targeting industrial flexible manufacturing and scientific research education.

The product adopts a platform-based control architecture, supporting drag teaching, graphical programming, collision detection, and open ROS/ROS2 interfaces, emphasizing rapid secondary development and industry customization capabilities.

## Product Image

> EC66: Please visit the [official website](https://www.elite-robot.com) for details.

## Specification Parameter Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Product Form | 6-DOF Collaborative Robot | Elite Robot official website |
| Weight | Approx. 17.5 kg | Product manual |
| Payload | 6 kg | Product manual |
| Reach | 914 mm | Product manual |
| Degrees of Freedom | 6 DOF | Public specifications |
| Repeat Positioning Accuracy | ±0.03 mm | Product manual |
| Maximum End-Effector Speed | 2.8 m/s | Product manual |
| Maximum Joint Speed | Not disclosed | - |
| Protection Rating | IP54 | Product manual |
| Communication Interface | Ethernet / Modbus / ROS | Product manual |
| Price | Not disclosed | Inquire for pricing |

## Supply Chain Position

- **Manufacturer**: [Elite Robot](../companies/company_elite_robot.md)
- **Core Components/Technology Sources**: Self-developed joint modules, harmonic reducers, servo motors, controllers, encoders, structural components.
- **Downstream Applications/Customers**: 3C electronics, automotive, new energy, medical, food, education and research.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_elite_ec66`
- Manufacturer Entity: `ent_company_elite_robot`
- Key Relationships:
  - `rel_ent_company_elite_robot_manufactures_ent_product_elite_ec66` (`ent_company_elite_robot` → `manufactures` → `ent_product_elite_ec66`)

## Application Scenarios

- **3C Assembly**: Screw fastening, component insertion, inspection, handling.
- **Automotive Parts Inspection**: Online inspection in flexible production lines.
- **Medical Aids**: Rehabilitation training, surgical assistance, sample processing.
- **Scientific Research and Education**: Robot programming training, human-robot collaboration research.

## Competitive Comparison

| Comparison Item | EC66 | Main Competitors |
|----------------|------|------------------|
| Positioning | Industrial/research collaborative robot | JAKA Zu 5, AUBO i5, HAN'S Elfin 5 |
| Core Advantage | Platform architecture, open SDK, rapid customization | Depends on specific model |
| Price | Not disclosed | Not disclosed |

## Selection and Deployment Recommendations

- Choose the EC63 / EC66 / EC75 / EC612 series based on payload and reach requirements.
- Secondary development users should prioritize evaluating the SDK, ROS interface, and community support.
- It is recommended to obtain the latest controller firmware and certified accessories through Elite Robot's official channels.

## Related Entries

- [Manufacturer: Elite Robot](../companies/company_elite_robot.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [Elite Robot Official Website](https://www.elite-robot.com)
2. Elite Robot EC Series Product Manual
3. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
