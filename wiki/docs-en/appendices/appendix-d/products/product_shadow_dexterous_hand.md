# Shadow Dexterous Hand

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Table of Contents](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Shadow Robot Company](../companies/company_shadow_robot.md) |
| **Product Category** | Dexterous Hand / End Effector |
| **Release Date** | Current flagship model |
| **Status** | Commercial / Research |
| **Official Website/Source** | [Shadow Robot Company Official Website](https://www.shadowrobot.com) |

## Product Overview

The Shadow Dexterous Hand is a highly anthropomorphic five-fingered dexterous hand developed by Shadow Robot Company. It features kinematics and dimensions similar to the human hand, supports position, force, and torque multi-mode control, and is one of the most influential dexterous hand platforms in global research and high-end teleoperation.

## Product Image

> Shadow Dexterous Hand: Please visit [Official Materials](https://www.shadowrobot.com) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Anthropomorphic adult male hand size | Official datasheet |
| Weight | 4.3 kg (including forearm) | Official datasheet |
| Degrees of Freedom | 20 active + 4 passive / 24 joints | Official datasheet |
| Payload | Power grasp 4–5 kg | Official datasheet / Public reports |
| Motion Speed | Typical joint 1.0 Hz | Official datasheet |
| Communication Interface | EtherCAT | Official datasheet |
| Control Frequency | Position loop 1 kHz / Torque loop 5 kHz | Official datasheet |
| Supply Voltage | Not disclosed | - |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Shadow Robot Company](../companies/company_shadow_robot.md)
- **Core Components/Technology Sources**: Micro motors, tendons, force/tactile sensors, aluminum alloy/engineering plastics, EtherCAT control board.
- **Downstream Applications/Customers**: Universities and research institutions, medical surgery, nuclear industry, teleoperation, humanoid robots.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_shadow_dexterous_hand`
- Manufacturer Entity: `ent_company_shadow_robot`
- Key Relationships:
  - `rel_ent_company_shadow_robot_manufactures_ent_product_shadow_dexterous_hand` (`ent_company_shadow_robot` --> `manufactures` --> `ent_product_shadow_dexterous_hand`)

## Application Scenarios

- **Research**: Grasping strategies, dexterous manipulation, AI algorithm validation
- **Medical**: Surgical training, rehabilitation robotics, remote surgery
- **Nuclear Industry**: Teleoperation and maintenance in hazardous environments
- **Humanoid Robots**: End effector for high-end humanoid platforms

## Competitive Comparison

| Comparison Item | This Product | International Brands | Domestic Counterparts |
|-----------------|--------------|----------------------|------------------------|
| Core Advantage | High DOF, mature ROS/EtherCAT ecosystem, research benchmark | High precision and reliability | Performance competition in same range |
| Delivery Lead Time | Short / Configuration-dependent | Long | Short |
| Service Response | Fast | Medium | Fast |
| Price Level | Very high | High-end | Mid-to-low end |

## Selection and Deployment Recommendations

- When selecting a model, match the appropriate variant based on payload, stroke, speed, and precision requirements; contact the manufacturer for customized solutions if necessary.
- Before deployment, it is recommended to perform load inertia identification, stiffness matching, and vibration suppression debugging to ensure compatibility with the overall system.

## References

1. [Shadow Robot Company Official Website](https://www.shadowrobot.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.shadowrobot.com) (Please verify against the actual product model)
