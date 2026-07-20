# Benmo TITA

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Index](../index-products.md)
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Benmo Technology / Direct Drive Technology](../companies/company_benmo.md) |
| **Product Category** | Wheel-legged robot |
| **Release Date** | 2023 |
| **Status** | Mass production/Development platform |
| **Official Website/Source** | [https://directdrive.com](https://directdrive.com) |

## Product Overview

Smart park patrol, logistics delivery, terrain mapping, agriculture, home companionship, mobile filming.

Benmo TITA is the flagship product of Benmo Technology. It features a quasi-direct drive 8-axis wheel-leg configuration, standing/jumping/obstacle crossing/auto recovery, a top universal rail for modular expansion, and perception via infrared laser + ultrasonic + binocular camera. Main specifications include: standing 510×590×490 mm; crouching 510×590×300 mm (dimensions), 24.1 kg (without battery) (weight), 8 DOF (degrees of freedom).

## Product Image

> Benmo TITA: Please visit the [official website](https://directdrive.com) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Standing 510×590×490 mm; Crouching 510×590×300 mm | Benmo company introduction PDF |
| Weight | 24.1 kg (without battery) | Benmo company introduction PDF |
| Degrees of Freedom | 8 DOF | Benmo company introduction PDF |
| Payload/Torque | Mobile payload 10 kg | Benmo company introduction PDF |
| Speed/RPM | Max speed 3 m/s (5 m/s requires API unlock) | Benmo company introduction PDF |
| Battery Life | Approximately 2 hours with dual batteries, supports hot swap | Benmo company introduction PDF |
| Interface/Communication | NVIDIA Jetson Orin NX 16G, RPC/onboard programming, behavior-level and joint-level interfaces | Benmo company introduction PDF |
| Price | Not disclosed | Requires inquiry |

## Supply Chain Position

- **Manufacturer**: [Benmo Technology / Direct Drive Technology](../companies/company_benmo.md)
- **Core Components/Technology Source**: Self-developed direct drive motors, M15/M07 series joint modules, hub motors, controllers, batteries, and navigation tower (LiDAR).
- **Downstream Applications/Customers**: Smart park patrol, logistics delivery, terrain mapping, agriculture, home companionship, mobile filming.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_benmo_tita`
- Manufacturer Entity: `ent_company_benmo`
- Key Relationships:
  - `rel_ent_company_benmo_manufactures_ent_product_benmo_tita` (`ent_company_benmo` → `manufactures` → `ent_product_benmo_tita`)
  - `ent_product_benmo_tita` -- `uses` --> `ent_component_benmo_m1502d`

## Application Scenarios

- **Smart park patrol, logistics delivery, terrain mapping, agriculture, home companionship, mobile filming.**
- **Research and Education**: Serves as a hardware platform for robot control, AI training, and embodied intelligence research.

## Competitive Comparison

| Comparison Item | This Product | Main Competitors |
|-----------------|--------------|------------------|
| Positioning | Wheel-legged robot | Similar products depend on specific scenarios |
| Core Advantage | Quasi-direct drive 8-axis wheel-leg, standing/jumping/obstacle crossing/auto recovery, top universal rail for modular expansion, perception via infrared laser + ultrasonic + binocular camera | Not disclosed |
| Price | Not disclosed | Not disclosed |

## Procurement and Deployment Recommendations

- It is recommended to confirm the latest software version, SDK support, and after-sales training through official channels.
- Research and education users should prioritize evaluating secondary development interfaces, simulation platform compatibility, and community activity.
- Industrial users need to verify payload, precision, protection level, and integration interfaces based on specific processes.

## References

1. [Benmo Technology Official Website](https://directdrive.com)
2. [Benmo Technology Company Introduction PDF](https://www.worldrobotconference.com/profile/robot/download/2025/07/10/250110%20%E6%9C%AC%E6%9C%AB%E7%A7%91%E6%8A%80%E4%BB%8B%E7%BB%8D_20250710110734A073.pdf)
3. [Hard氪 – Benmo Technology Financing Report](http://mp.weixin.qq.com/s?__biz=MzkwMTI4MjU0Mw==&mid=2247520049&idx=2&sn=36133880658fdda8d838fcf5d975fbb0)
