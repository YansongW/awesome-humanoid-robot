# AUBO-i5 Collaborative Robot

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [AUBO Intelligent / AUBO](../companies/company_aubo.md) |
| **Product Category** | Collaborative Robot |
| **Release Date** | Continuous iteration since 2017 |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [https://www.aubo-robotics.cn](https://www.aubo-robotics.cn) |

## Product Overview

The AUBO-i5 is a 6-degree-of-freedom collaborative robot launched by AUBO Intelligent, with a payload of 5 kg and a reach of 1000 mm, targeting industrial flexible manufacturing and commercial services.

The product is known for its high cost-effectiveness, open ecosystem, and ease of use. It supports drag teaching, ROS/ROS2, and a rich set of secondary development interfaces, making it a typical representative of large-scale collaborative robot applications in China.

## Product Image

> AUBO-i5: Please visit [Official Materials](https://www.aubo-robotics.cn) for details.

## Specification Parameter Table

| Specification Item | Value | Remarks/Source |
|--------------------|-------|----------------|
| Product Form | 6-DOF Collaborative Robot | AUBO Official Website |
| Weight | Approx. 24 kg | Product Manual |
| Payload | 5 kg | Product Manual |
| Reach | 1000 mm | Product Manual |
| Degrees of Freedom | 6 DOF | Public Specification |
| Repeat Positioning Accuracy | ±0.03 mm | Product Manual |
| Maximum End-Effector Speed | 2.8 m/s | Product Manual |
| Maximum Joint Speed | 180°/s (Reference) | Product Manual |
| Protection Level | IP54 | Product Manual |
| Communication Interface | Ethernet / Modbus / ROS | Product Manual |
| Price | Not Disclosed | Requires Inquiry |

## Supply Chain Position

- **Manufacturer**: [AUBO Intelligent / AUBO](../companies/company_aubo.md)
- **Core Components/Technology Source**: Self-developed joint modules, harmonic reducers, servo motors, controllers, encoders, structural parts.
- **Downstream Applications/Customers**: 3C Electronics, Automotive Parts, Medical Devices, Food, Logistics & Warehousing, Scientific Research & Education.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_aubo_i5`
- Manufacturer Entity: `ent_company_aubo`
- Key Relationships:
  - `rel_ent_company_aubo_manufactures_ent_product_aubo_i5` (`ent_company_aubo` → `manufactures` → `ent_product_aubo_i5`)
  - `ent_product_aubo_amr` -- `uses` --> `ent_product_aubo_i5`

## Application Scenarios

- **3C Assembly**: Screw fastening, insertion, inspection, handling.
- **Automotive Parts**: Grinding, polishing, loading/unloading, inspection.
- **Medical Aids**: Rehabilitation training, surgical assistance, sample processing.
- **Commercial Services**: Coffee making, unmanned retail, exhibition interaction.

## Competitive Comparison

| Comparison Item | AUBO-i5 | Main Competitors |
|-----------------|---------|------------------|
| Positioning | Industrial/Commercial Collaborative Robot | JAKA Zu 5, HAN'S Elfin 5, etc. |
| Core Advantage | High cost-effectiveness, open ecosystem, large-scale application | Depends on specific model |
| Price | Not Disclosed | Not Disclosed |

## Selection and Deployment Recommendations

- Choose the AUBO-i3 / i5 / i10 / i16 / i20 series based on payload and reach requirements.
- Confirm whether the protection level meets the workshop environment requirements (dust, oil, humidity).
- It is recommended to obtain the latest controller firmware and certified accessory list through AUBO's official channels.

## Related Entries

- [Manufacturer: AUBO Intelligent / AUBO](../companies/company_aubo.md)
- [Appendix D.4 Key Product Wiki](../index-products.md)

## References

1. [AUBO Intelligent Official Website](https://www.aubo-robotics.cn)
2. AUBO AUBO-i Series Product Manual
3. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
