# Jaka Zu 3 Collaborative Robot

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Index](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Jaka Robot / Jaka](../companies/company_jaka.md) |
| **Product Category** | Collaborative Robot |
| **Release Date** | Continuously iterated since 2017 |
| **Status** | Mass Production / Commercial |
| **Website/Source** | [https://www.jaka.com](https://www.jaka.com) |

## Product Overview

The Jaka Zu 3 is a desktop 6-DOF collaborative robot launched by Jaka Robot, targeting flexible manufacturing scenarios in 3C, automotive, food, medical, and other industries.

The product's core selling points include wireless teaching, graphical programming, IP54 protection, and ±0.02 mm repeat positioning accuracy, making it suitable for human-machine collaboration lines and small-batch, multi-variety production.

## Product Image

> Jaka Zu 3: Please visit [Official Website](https://www.jaka.com) for details.

## Specification Parameter Table

| Specification Item | Value | Remarks/Source |
|--------------------|-------|----------------|
| Product Form | 6-DOF Desktop Collaborative Robot | Jaka Official Website |
| Weight | Approx. 12 kg | Product Manual |
| Payload | 3 kg | Product Manual |
| Reach | 626 mm | Product Manual |
| Degrees of Freedom | 6 DOF | Public Specifications |
| Repeat Positioning Accuracy | ±0.02 mm | Product Manual |
| Maximum End-Effector Speed | 2.3 m/s | Product Manual |
| Maximum Joint Speed | 180°/s (Reference) | Product Manual |
| Protection Rating | IP54 | Product Manual |
| Communication Interface | Ethernet / Modbus / ROS | Product Manual |
| Price | Not disclosed | Requires inquiry |

## Supply Chain Position

- **Manufacturer**: [Jaka Robot / Jaka](../companies/company_jaka.md)
- **Core Components/Technology Sources**: Self-developed joint modules, harmonic reducers, servo motors, controllers, encoders, structural parts.
- **Downstream Applications/Customers**: 3C electronics, automotive parts, food & medical, scientific research & education, humanoid robot OEMs.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_jaka_zu3`
- Manufacturer Entity: `ent_company_jaka`
- Key Relationships:
  - `rel_ent_company_jaka_manufactures_ent_product_jaka_zu3` (`ent_company_jaka` → `manufactures` → `ent_product_jaka_zu3`)
  - `ent_product_jaka_k1` -- `uses` --> `ent_product_jaka_zu3`

## Application Scenarios

- **3C Assembly**: Screw fastening, component insertion, inspection, labeling.
- **Automotive Parts**: Small workpiece loading/unloading, precision inspection.
- **Food & Medical**: Packaging, sorting, sample processing.
- **Scientific Research & Education**: Robot programming training, human-machine collaboration research.

## Competitive Comparison

| Comparison Item | Jaka Zu 3 | Main Competitors |
|-----------------|-----------|------------------|
| Positioning | Desktop Collaborative Robot | Similar products vary by scenario |
| Core Advantages | Wireless teaching, graphical programming, IP54 | AUBO i3, Han's Elfin 3, etc. |
| Price | Not disclosed | Not disclosed |

## Selection and Deployment Recommendations

- Choose from the Zu 3 / Zu 5 / Zu 7 / Zu 12 / Zu 18 series based on payload and reach requirements.
- Confirm interface compatibility of end-effectors, vision systems, and the Jaka controller.
- It is recommended to obtain the latest teaching pendant firmware and SDK documentation through official channels.

## Related Entries

- [Manufacturer: Jaka Robot / Jaka](../companies/company_jaka.md)
- [Appendix D.4 Key Product Wiki](../index-products.md)

## References

1. [Jaka Robot Official Website](https://www.jaka.com)
2. Jaka Zu Series Product Manual
3. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
