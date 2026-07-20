# AG-160-95 Adaptive Electric Gripper / DH-Robotics AG-160-95 Adaptive Gripper

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [DH-Robotics](../companies/company_dh_robotics.md) |
| **Product Category** | Electric Gripper / End Effector |
| **Release Date** | Current Main Model |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [DH-Robotics Official Website](https://www.dh-robotics.com) |

## Product Overview

The AG-160-95 is a joint-type adaptive electric gripper launched by DH-Robotics. It adopts a linkage and lead screw nut transmission, featuring large stroke, force-position controllability, power-off self-locking, and intelligent feedback capabilities. It can be quickly integrated with humanoid robots, collaborative robots, and automated production lines to achieve stable and reliable flexible grasping.

## Product Image

> AG-160-95 Adaptive Electric Gripper: Please visit [Official Materials](https://www.dh-robotics.com) for details.

## Specification Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Dimensions | 184.6 × 162.3 × 67 mm | Third-party product page |
| Weight | Approx. 1 kg | Third-party product page |
| Degrees of Freedom | 1 DOF (Two-finger parallel) | Product manual |
| Gripping Force | 45–160 N per side | Third-party product page |
| Opening/Closing Speed | Opening/closing time approx. 0.9 s | Third-party product page |
| Repeat Positioning Accuracy | ±0.03 mm | Third-party product page |
| Supply Voltage | DC 24 V | Product manual |
| Communication Interface | Modbus RTU / I/O | Product manual |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [DH-Robotics](../companies/company_dh_robotics.md)
- **Core Components/Technology Sources**: Servo motor, ball screw/linkage, force/position sensor, aluminum alloy structural parts, driver IC.
- **Downstream Applications/Customers**: Collaborative robot integrators, 3C/new energy/semiconductor automation manufacturers, humanoid robot OEMs.

## Knowledge Graph Nodes and Relationships

- Component Entity: `ent_product_dh_robotics_hand`
- Manufacturer Entity: `ent_company_dh_robotics`
- Key Relationships:
  - `rel_ent_company_dh_robotics_manufactures_ent_product_dh_robotics_hand` (`ent_company_dh_robotics` --> `manufactures` --> `ent_product_dh_robotics_hand`)

## Application Scenarios

- **Industrial Automation**: 3C assembly, lithium battery sorting, semiconductor handling, food packaging
- **Collaborative Robots**: Paired with UR, AUBO, and other collaborative arms for loading/unloading and inspection
- **Humanoid Robots**: As a low-cost end effector adapted to bipedal/wheeled humanoid platforms
- **Research and Education**: Grasping algorithm validation, force control teaching, robot competitions

## Competitive Comparison

| Comparison Item | This Product | International Brands | Domestic Counterparts |
|----------------|--------------|----------------------|-----------------------|
| Core Advantage | Local supply, high cost-performance, large stroke, adjustable force control | High-end precision and reliability | Performance competition in the same range |
| Delivery Lead Time | Short / Configurable | Long | Short |
| Service Response | Fast | Medium | Fast |
| Price Level | Low-end to Mid-high-end | High-end | Low-end |

## Selection and Deployment Recommendations

- When selecting a model, match the appropriate type based on load, stroke, speed, and precision requirements. Contact the manufacturer for customized solutions if necessary.
- Before deployment, it is recommended to perform load inertia identification, stiffness matching, and vibration suppression debugging to ensure compatibility with the overall system.

## References

1. [DH-Robotics Official Website](https://www.dh-robotics.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.dh-robotics.com) (Please verify against the actual product model)
