# Xvariable Quanta X2

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Index](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Xvariable / X Square Robot](../companies/company_xvariable.md) |
| **Product Category** | General-purpose wheeled humanoid robot |
| **Release Date** | August 2025 |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [https://x2robot.com](https://x2robot.com) |

## Product Overview

Industrial assembly, wire harness organization, hotel tissue replacement, clothes hanging, miscellaneous storage, beverage preparation, scientific research and education.

The Xvariable Quanta X2 (Quantum 2) is the flagship product of Xvariable. It features the WALL-A end-to-end operation large model with tens of billions of parameters, 62 DOF across the entire body, ±0.03 mm repeat positioning, a humanoid five-fingered dexterous hand, and cross-task cross-scenario generalization. Main specifications include: height 164 cm; working height 0–2 m (dimensions), weight not disclosed, 62 DOF across the entire body; torso 6 DOF; single-hand dexterous hand 20 DOF (degrees of freedom).

## Product Image

![Xvariable Quanta X2 (Quantum 2)](https://x2robot-open.oss-cn-shenzhen.aliyuncs.com/quantum2_qiepian/x2/12_m.png)

> Image source: Xvariable official website product image.

## Specification Parameter Table

| Specification Item | Value | Remarks/Source |
|--------------------|-------|----------------|
| Dimensions | Height 164 cm; working height 0–2 m | Xvariable official website |
| Weight | Not disclosed | - |
| Degrees of Freedom | 62 DOF across the entire body; torso 6 DOF; single-hand dexterous hand 20 DOF | Xvariable official website |
| Load/Torque | Single arm rated load 6 kg; maximum dual arm load 25 kg | Xvariable official website |
| Speed/Rotational Speed | End-effector speed 1.8 m/s; chassis movement speed 1 m/s | Xvariable official website |
| Battery Life | Not disclosed | - |
| Interface/Communication | 2D LiDAR, ultrasonic ×4, RGBD, 3D-TOF, single-point TOF, infrared; WALL-A end-to-end large model | Xvariable official website |
| Price | Not disclosed | Inquire for pricing |

## Supply Chain Position

- **Manufacturer**: [Xvariable / X Square Robot](../companies/company_xvariable.md)
- **Core Components/Technology Source**: Self-developed WALL-A large model, joints, dexterous hand, sensors, computing platform; externally purchased motors, reducers, batteries, camera modules.
- **Downstream Applications/Customers**: Industrial assembly, wire harness organization, hotel tissue replacement, clothes hanging, miscellaneous storage, beverage preparation, scientific research and education.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_xvariable_quanta_x2`
- Manufacturer Entity: `ent_company_xvariable`
- Key Relationships:
  - `rel_ent_company_xvariable_manufactures_ent_product_xvariable_quanta_x2` (`ent_company_xvariable` → `manufactures` → `ent_product_xvariable_quanta_x2`)
  - `ent_product_xvariable_quanta_x2` -- `uses` --> `ent_component_xvariable_artixon_hand`

## Application Scenarios

- **Industrial assembly, wire harness organization, hotel tissue replacement, clothes hanging, miscellaneous storage, beverage preparation, scientific research and education.**

## Competitive Comparison

| Comparison Item | This Product | Main Competitors |
|-----------------|--------------|------------------|
| Positioning | General-purpose wheeled humanoid robot | Similar products depend on specific scenarios |
| Core Advantage | WALL-A end-to-end operation large model with tens of billions of parameters, 62 DOF across the entire body, ±0.03 mm repeat positioning, humanoid five-fingered dexterous hand, cross-task cross-scenario generalization | Not disclosed |
| Price | Not disclosed | Not disclosed |

## Purchase and Deployment Recommendations

- It is recommended to confirm the latest software version, SDK support, and after-sales training through official channels.
- Scientific research and education users should prioritize evaluating secondary development interfaces, simulation platform compatibility, and community activity.
- Industrial users need to verify load, precision, protection level, and integration interfaces based on specific processes.

## References

1. [Xvariable Official Website](https://x2robot.com)
2. [Quanta X2 Product Page](https://x2robot.com/product/quantum2)
3. [About Us](https://x2robot.com/about)
