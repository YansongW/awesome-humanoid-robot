# ROKAE xMate CR Series Collaborative Robots

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update date: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [ROKAE / ROKAE](../companies/company_rokae.md) |
| **Product Category** | Industrial Collaborative Robot |
| **Release Date** | Continuously iterated since 2019 |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [https://www.rokae.com](https://www.rokae.com) |

## Product Overview

The xMate CR series is an industrial collaborative robot launched by ROKAE, known for its self-developed xCore control system, high trajectory accuracy, and force control capabilities.

The product covers 3–12 kg payloads and 6/7 degrees of freedom, emphasizing high speed, high precision, and high rigidity, making it suitable for complex processes and human-robot collaborative flexible production lines.

## Product Image

> xMate CR: Please visit the [official website](https://www.rokae.com) for details.

## Specification Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Product Form | 6/7-DOF Industrial Collaborative Robot | ROKAE Official Website |
| Self-weight | Not disclosed | - |
| Payload | 3–12 kg (depending on model) | Product Manual |
| Reach | 717–1304 mm (depending on model) | Product Manual |
| Degrees of Freedom | 6/7 DOF (depending on model) | Public Specifications |
| Repeat Positioning Accuracy | ±0.02–±0.03 mm | Product Manual |
| Maximum End-Effector Speed | Not disclosed | - |
| Maximum Joint Speed | Not disclosed | - |
| Protection Class | IP54 | Product Manual |
| Communication Interface | Ethernet / EtherCAT / ROS | Product Manual |
| Price | Not disclosed | Inquiry required |

## Supply Chain Position

- **Manufacturer**: [ROKAE / ROKAE](../companies/company_rokae.md)
- **Core Components/Technology Source**: Self-developed xCore control system, harmonic reducers, servo motors, controllers, encoders, structural parts.
- **Downstream Applications/Customers**: Automotive, 3C, New Energy, Metal Processing, Medical, Humanoid Robot OEMs.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_rokae_xmate_cr`
- Manufacturer Entity: `ent_company_rokae`
- Key Relationships:
  - `rel_ent_company_rokae_manufactures_ent_product_rokae_xmate_cr` (`ent_company_rokae` → `manufactures` → `ent_product_rokae_xmate_cr`)

## Application Scenarios

- **3C Precision Assembly**: High-precision insertion, lamination, inspection.
- **Automotive Parts Grinding**: Force-controlled polishing, deburring.
- **Medical Device Loading/Unloading**: Flexible pick-and-place in sterile environments.
- **Scientific Research and Education**: Motion planning, force control interaction, human-robot collaboration research.

## Competitive Comparison

| Comparison Item | xMate CR | Main Competitors |
|----------------|----------|------------------|
| Positioning | Industrial-grade high-precision collaborative robot | Estun, JAKA, AUBO, KUKA iiwa |
| Core Advantage | Self-developed xCore, high trajectory accuracy, force control | Depends on specific model |
| Price | Not disclosed | Not disclosed |

## Selection and Deployment Recommendations

- Select the specific model based on payload, reach, and degrees of freedom requirements.
- For force-controlled grinding scenarios, confirm the matching solution of force sensors and control algorithms.
- It is recommended to obtain the latest control software and process packages through ROKAE's official channels.

## Related Entries

- [Manufacturer: ROKAE / ROKAE](../companies/company_rokae.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [ROKAE Official Website](https://www.rokae.com)
2. ROKAE xMate CR Series Product Manual
3. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
