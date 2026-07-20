# Unitree G1

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Index](../index-products.md)
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Unitree Robotics](../companies/company_unitree.md) |
| **Product Category** | Compact Humanoid Robot |
| **Release Date** | 2024 |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [Unitree G1 Product Page](https://www.unitree.com/g1) |

## Product Overview

The Unitree G1 is a compact humanoid robot launched by Unitree for education, research, and developers, known for its aggressive pricing and high accessibility. The G1 stands approximately 127 cm tall and weighs about 35 kg. The base version has 23 degrees of freedom, while the EDU version can be expanded to 43 DOF and is equipped with the Dex3-1 five-finger dexterous hand and the NVIDIA Jetson Orin computing module.

The G1 uses 3D LiDAR, depth cameras, and an 8-core CPU (the EDU version adds Jetson Orin), supporting ROS2, Python/C++ SDK, and OTA updates. Its foldable design facilitates transportation and deployment, making it one of the leading humanoid development platforms in global shipments.

## Product Image

> Unitree G1: Please visit the [official page](https://www.unitree.com/g1) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 127 cm (height) | Public specs |
| Weight | Approx. 35 kg | Public specs |
| Degrees of Freedom (Whole Body) | 23–43 DOF | Configuration difference between base/EDU versions |
| Key Performance Indicators | Joint peak torque 90–120 N·m; payload approx. 2 kg | Public specs |
| Walking Speed | Approx. 2 m/s | Public specs |
| Battery Life | Approx. 1.5–2 hours (9,000 mAh quick-swap battery) | Public specs |
| Computing Platform | 8-core CPU; EDU version optional NVIDIA Jetson Orin | Public specs |
| Price | Approx. 16,000 USD / Starting at 99,000 RMB domestically | Media reports |

## Supply Chain Position

- **Manufacturer**: [Unitree Robotics](../companies/company_unitree.md)
- **Core Components/Technology Sources**: Self-developed joint motors and drivers, 3D LiDAR, Intel RealSense depth cameras, NVIDIA Jetson Orin (EDU version).
- **Downstream Applications/Customers**: Universities, educational institutions, developers, AI research, and commercial demonstrations.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_unitree_g1`
- Manufacturer Entity: `ent_company_unitree`
- Key Relationships:
  - `rel_ent_company_unitree_manufactures_ent_product_unitree_g1` (`ent_company_unitree` → `manufactures` → `ent_product_unitree_g1`)

## Application Scenarios

- **Educational Demonstrations**: Used by universities, primary/secondary schools, and science museums for robotics courses, exhibitions, and competitions.
- **AI and Robotics Research**: Developer community experiments with imitation learning, reinforcement learning, and multimodal interaction.
- **Lightweight Commercial Use**: Retail displays, guided tours, reception, and small-scale logistics pilots.

## Competitive Comparison

| Comparison Item | Unitree G1 | Unitree H1 | Unitree R1 |
|-----------------|------------|------------|------------|
| Positioning | Compact development platform | Full-size high-dynamic platform | Entry-level development platform |
| Height | 127 cm | 180 cm | 121 cm |
| Price | Approx. 16,000 USD | Approx. 90,000 USD | Approx. 5,900 USD |
| Core Advantage | High cost-effectiveness, full EDU features | High-dynamic motion, large payload | Ultra-low barrier, developer-friendly |

## Selection and Deployment Recommendations

- Educational/research institutions are advised to prioritize the G1 EDU version for SDK, ROS2, and Jetson Orin computing support.
- During deployment, ensure the site has sufficient safety space and configure emergency stop devices and protective barriers.

## References

1. [Unitree G1 Product Page](https://www.unitree.com/g1)
2. [Robozaps – Unitree G1 Review](https://blog.robozaps.com/b/unitree-g1-review)
3. [Humanoid.Guide – Unitree G1](https://humanoid.guide/product/g1/)
4. [Humanoid Index – G1](https://humanoidindex.org/robots/g1)
