# Booster T1 / Booster T1

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Accelerated Evolution / Booster Robotics](../companies/company_booster_robotics.md) |
| **Product Category** | General-purpose humanoid robot |
| **Release Date** | Not disclosed |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [https://www.booster.tech](https://www.booster.tech) |

## Product Overview

University research, RoboCup competitions, motion control algorithm validation, AI training, industrial automation prototypes.

Booster T1 is the flagship product of Accelerated Evolution. It features an Intel i7 1370p + NVIDIA Jetson AGX Orin 200 TOPS, omnidirectional walking, anti-interference capabilities, simulation platform support (Isaac Sim/Mujoco), and is the RoboCup 2025 champion edition. Key specifications include: 118 cm (height) (dimensions), 30 kg (weight), 23 DOF (optional configuration up to 41 DOF) (degrees of freedom).

## Product Image

![Booster T1](https://www.althumans.com/media/catalog/product/cache/7e65f7ea2c9ff177580b02a356862407/a/h/ah-booster-t1-01.jpg)

> Image source: AltHumans product image (Booster T1 distributor).

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | 118 cm (height) | Booster official website / Bipedal documentation |
| Weight | 30 kg | Booster official website / Bipedal documentation |
| Degrees of Freedom | 23 DOF (optional configuration up to 41 DOF) | Bipedal documentation / Public reports |
| Load/Torque | Knee joint peak torque 130 N·m; hollow shaft joint motor | Bipedal documentation |
| Speed/RPM | Omnidirectional walking; specific speed not disclosed | Bipedal documentation |
| Battery Life | 10.5 Ah battery; approximately 2 h walking, 4 h standing | Booster official website |
| Interfaces/Communication | ROS 2, USB, Ethernet, Wi-Fi 6, Bluetooth 5.2, Mobile App | Booster official website |
| Price | Starting from approximately 199,000 RMB (public reports) | 36Kr / Public reports |

## Supply Chain Position

- **Manufacturer**: [Accelerated Evolution / Booster Robotics](../companies/company_booster_robotics.md)
- **Core Components/Technology Sources**: Self-developed hollow shaft joint motor, NVIDIA Jetson AGX Orin, Intel i7 computing platform, depth camera, 9-axis IMU, battery.
- **Downstream Applications/Customers**: University research, RoboCup competitions, motion control algorithm validation, AI training, industrial automation prototypes.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_booster_t1`
- Manufacturer Entity: `ent_company_booster_robotics`
- Key Relationships:
  - `rel_ent_company_booster_robotics_manufactures_ent_product_booster_t1` (`ent_company_booster_robotics` → `manufactures` → `ent_product_booster_t1`)
  - `ent_product_booster_t1` -- `uses` --> `ent_component_nvidia_jetson_agx_orin`

## Application Scenarios

- **University research, RoboCup competitions, motion control algorithm validation, AI training, industrial automation prototypes.**

## Competitive Comparison

| Comparison Item | This Product | Main Competitors |
|-----------------|--------------|------------------|
| Positioning | General-purpose humanoid robot | Similar products depend on specific scenarios |
| Core Advantages | Intel i7 1370p + NVIDIA Jetson AGX Orin 200 TOPS, omnidirectional walking, anti-interference, simulation platform support (Isaac Sim/Mujoco), RoboCup 2025 champion edition | Not disclosed |
| Price | Starting from approximately 199,000 RMB (public reports) | Not disclosed |

## Procurement and Deployment Recommendations

- It is recommended to confirm the latest software version, SDK support, and after-sales training through official channels.
- Research and education users should prioritize evaluating secondary development interfaces, simulation platform compatibility, and community activity.
- Industrial users need to verify load, precision, protection level, and integration interfaces based on specific processes.

## References

1. [Booster T1 Official Website](https://www.booster.tech/booster-t1/)
2. [Bipedal – Booster T1 Documentation](http://www.docs.bipedal.de/projects/t1/html/overview.html)
3. [Science and Technology Innovation Board Daily – CES Report](https://www.cls.cn/detail/1912332)
