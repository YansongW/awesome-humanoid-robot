# qb SoftHand 5-Finger Soft Robotic Hand

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [qb Soft Robotics / qb Soft Robotics](../companies/company_qb_robotics.md) |
| **Product Category** | Soft Robotic Hand / End Effector |
| **Release Date** | Current Model |
| **Status** | Commercial / Research |
| **Official Website/Source** | [qb Soft Robotics Official Website](https://qbrobotics.com) |

## Product Overview

The qb SoftHand is a five-finger dexterous hand based on soft robotics technology developed by qbrobotics. It features a single-motor tendon drive and 19 soft joints working in coordination, achieving mechanical adaptability to grasp objects of various shapes. It is characterized by light weight, high payload-to-weight ratio, and safe human-robot interaction.

## Product Image

> qb SoftHand 5-Finger Soft Robotic Hand: Please visit the [official website](https://qbrobotics.com) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | 1:1 human hand scale, specifics not disclosed | Public information |
| Weight | 500 g | Public information |
| Number of Fingers | 5 | Public information |
| Degrees of Freedom | 19 joints / 1 active coordination (single motor) | Public information |
| Fingertip Pinch Force | 62 N | Public information |
| Rated Payload | 1.7 kg (in pinch state) | Public information |
| Open Hand to Fist | 1.1 s | Public information |
| Communication Interface | USB / RS485 | Public information |
| Compatibility | ROS, UR+ certified | Public information |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [qb Soft Robotics / qb Soft Robotics](../companies/company_qb_robotics.md)
- **Core Components/Technology Sources**: Elastomer materials, tendons/soft actuation, motors, sensors, 3D printed structural parts.
- **Downstream Applications/Customers**: Universities, research institutions, collaborative robot manufacturers, medical rehabilitation, industrial testing.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_qb_hand`
- Manufacturer Entity: `ent_company_qb_robotics`
- Key Relationships:
  - `rel_ent_company_qb_robotics_manufactures_ent_product_qb_hand` (`ent_company_qb_robotics` --> `manufactures` --> `ent_product_qb_hand`)

## Application Scenarios

- **Research**: Soft grasping, collaborative control, human-robot interaction studies
- **Education**: Robotics teaching, demonstrations, and competitions
- **Collaborative Robots**: Flexible end effectors, safe co-linear operations
- **Medical Rehabilitation**: Prosthetics, rehabilitation aids, human-robot interaction

## Competitive Comparison

| Comparison Item | This Product | International Brands | Domestic Counterparts |
|-----------------|--------------|----------------------|------------------------|
| Core Advantage | Soft adaptability, single-motor easy control, lightweight high payload, safety | High-end precision and reliability | Performance competition in the same range |
| Delivery Lead Time | Relatively short / configuration-based | Relatively long | Relatively short |
| Service Response | Fast | Moderate | Fast |
| Price Level | Mid-to-high end | High end | Mid-to-low end |

## Selection and Deployment Recommendations

- When selecting a model, match the appropriate model based on payload, stroke, speed, and precision requirements. Contact the manufacturer for customized solutions if necessary.
- Before deployment, it is recommended to perform load inertia identification, stiffness matching, and vibration suppression debugging to ensure compatibility with the overall system.

## References

1. [qb Soft Robotics Official Website](https://qbrobotics.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://qbrobotics.com) (Please verify against the actual product model)
