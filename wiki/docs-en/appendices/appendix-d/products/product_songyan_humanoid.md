# Songyan N2

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Songyan Dynamics / Noetix Robotics](../companies/company_songyan_dynamics.md) |
| **Product Category** | General-purpose humanoid robot |
| **Release Date** | March 2025 |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [https://noetixrobotics.com](https://noetixrobotics.com) |

## Product Overview

University research, early childhood companionship, entertainment performance, commercial display, robot competition.

Songyan N2 is the flagship product of Songyan Dynamics. It is the world's first multi-scenario continuous backflip robot, featuring MPC + reinforcement learning motion control, lightweight aluminum alloy structure, dual-encoder joints, and optional NVIDIA Jetson Orin Nano Super. Key specifications include: 1180×470×290 mm (standing) (dimensions), approx. 30 kg (weight), 18 DOF (single leg 5 DOF×2, single arm 4 DOF×2) (degrees of freedom).

## Product Image

![Songyan N2](https://www.noetixrobotics.com/mtsc/uploads/Ckeditor/Images/2025-12-25/N2.webp)

> Image source: Songyan Dynamics official website product image.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | 1180×470×290 mm (standing) | Songyan official website / Baidu Baike |
| Weight | Approx. 30 kg | Songyan official website |
| Degrees of Freedom | 18 DOF (single leg 5 DOF×2, single arm 4 DOF×2) | Songyan official website |
| Load/Torque | Knee joint peak torque 150 N·m; continuous walking load approx. 5 kg | Songyan official website |
| Speed/RPM | Peak running speed 3.5 m/s | Songyan official website / Baidu Baike |
| Battery Life | Approx. 1–2 hours (48 V / 7 Ah) | Songyan official website |
| Interface/Communication | Wi-Fi 6, Bluetooth 5.2, OTA, secondary development interface (EDU version) | Songyan official website |
| Price | Starting from 39,900 RMB | Public reports |

## Supply Chain Position

- **Manufacturer**: [Songyan Dynamics / Noetix Robotics](../companies/company_songyan_dynamics.md)
- **Core Components/Technology Source**: Self-developed high-performance joint motors and drivers, aluminum alloy structural parts, depth camera, IMU, lithium battery; core components are nearly 100% domestically sourced.
- **Downstream Applications/Customers**: University research, early childhood companionship, entertainment performance, commercial display, robot competition.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_songyan_dynamics_n2`
- Manufacturer Entity: `ent_company_songyan_dynamics`
- Key Relationships:
  - `rel_ent_company_songyan_dynamics_manufactures_ent_product_songyan_dynamics_n2` (`ent_company_songyan_dynamics` → `manufactures` → `ent_product_songyan_dynamics_n2`)
  - `ent_product_songyan_dynamics_n2` -- `uses` --> `ent_component_songyan_joint_motor`

## Application Scenarios

- **University research, early childhood companionship, entertainment performance, commercial display, robot competition.**
- **Commercial Services**: Used for guided tours, reception, display, and brand interaction.

## Competitive Comparison

| Comparison Item | This Product | Main Competitors |
|-----------------|--------------|------------------|
| Positioning | General-purpose humanoid robot | Similar products depend on specific scenarios |
| Core Advantage | World's first multi-scenario continuous backflip, MPC + reinforcement learning motion control, lightweight aluminum alloy structure, dual-encoder joints, optional NVIDIA Jetson Orin Nano Super | Not disclosed |
| Price | Starting from 39,900 RMB | Not disclosed |

## Purchase and Deployment Recommendations

- It is recommended to confirm the latest software version, SDK support, and after-sales training through official channels.
- Research and education users should prioritize evaluating secondary development interfaces, simulation platform compatibility, and community activity.
- Industrial users need to verify load, precision, protection level, and integration interfaces based on specific processes.

## References

1. [Songyan N2 Product Page](https://noetixrobotics.com/n2)
2. [Songyan Dynamics Official Website](https://noetixrobotics.com/)
3. [Baidu Baike – Songyan N2](https://baike.baidu.com/item/%E6%9D%BE%E5%BB%B6%E5%8A%A8%E5%8A%9BN2/67393633)
