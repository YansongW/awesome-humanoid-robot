# 2F-85 Adaptive Gripper / Robotiq 2F-85 Adaptive Gripper

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Robotiq / Robotiq](../companies/company_robotiq.md) |
| **Product Category** | Electric Gripper / End Effector |
| **Release Date** | Current main model |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [Robotiq Official Website](https://robotiq.com) |

## Product Overview

The Robotiq 2F-85 is an adaptive two-finger electric gripper designed for collaborative robots. It supports three gripping modes: parallel, enveloping, and internal gripping, and features force/position closed-loop control, drop detection, and UR+ plug-and-play capability. It is one of the most widely used grippers in the global collaborative robot field.

## Product Image

> 2F-85 Adaptive Gripper: Please visit [Official Documentation](https://robotiq.com) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Not disclosed (refer to dimensional drawing) | - |
| Weight | 0.9 kg | Product Manual |
| Degrees of Freedom | 1 (Two-finger parallel motion) | Product Manual |
| Stroke | 0–85 mm | Product Manual |
| Gripping Force | 20–235 N | Product Manual |
| Recommended Payload | 5 kg | Product Manual |
| Closing Speed | 20–150 mm/s | Product Manual |
| Position Resolution | 0.4 mm | Product Manual |
| Communication Interface | Modbus RTU (RS-485/RS-232) | Product Manual |
| Protection Rating | IP40 | Product Manual |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Robotiq / Robotiq](../companies/company_robotiq.md)
- **Core Components/Technology Sources**: Servo motor, lead screw/gear, force sensor, aluminum alloy, seals.
- **Downstream Applications/Customers**: Collaborative robot integrators, automotive, 3C, food, logistics.

## Knowledge Graph Nodes and Relationships

- Component Entity: `ent_product_robotiq_hand`
- Manufacturer Entity: `ent_company_robotiq`
- Key Relationships:
  - `rel_ent_company_robotiq_manufactures_ent_product_robotiq_hand` (`ent_company_robotiq` --> `manufactures` --> `ent_product_robotiq_hand`)

## Application Scenarios

- **Assembly**: Insertion, press-fitting, precision part assembly
- **Handling**: Machine tool loading/unloading, packaging sorting
- **Inspection**: Vision-guided quality inspection, missing part detection
- **Collaborative Robots**: Plug-and-play with collaborative arms such as UR

## Competitive Comparison

| Comparison Item | This Product | International Brands | Domestic Counterparts |
|-----------------|--------------|----------------------|------------------------|
| Core Advantage | Plug-and-play, adaptive gripping, force-position closed-loop, mature ecosystem | High-end precision and reliability | Performance competition in the same range |
| Delivery Lead Time | Relatively short / configuration-dependent | Relatively long | Relatively short |
| Service Response | Fast | Medium | Fast |
| Price Level | Mid-to-high end | High end | Mid-to-low end |

## Selection and Deployment Recommendations

- When selecting, match the appropriate model based on load, stroke, speed, and precision requirements. Contact the manufacturer for customized solutions if necessary.
- Before deployment, it is recommended to perform load inertia identification, stiffness matching, and vibration suppression debugging to ensure compatibility with the overall system.

## References

1. [Robotiq Official Website](https://robotiq.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://robotiq.com) (Please verify against the actual product model)
