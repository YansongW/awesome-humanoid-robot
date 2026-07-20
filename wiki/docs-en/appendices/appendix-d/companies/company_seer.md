# SEER Robotics

> This entry belongs to [Appendix D: Company/Product Wiki](../../appendix-d.md).
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 仙工智能 (Shanghai SEER Robotics Technology Co., Ltd.) |
| **English Name** | SEER Robotics |
| **Headquarters** | Shanghai, China |
| **Founded** | 2020 |
| **Website** | [https://www.seer-group.com](https://www.seer-group.com) |
| **Supply Chain Role** | Computing Platform / Mobile Robot Controller and Embodied Intelligence Controller |
| **Company Type** | Platform-type embodied intelligent robot company, leading robot controller manufacturer |
| **Parent Company/Group** | None |
| **Data Sources** | SEER Robotics official website, China Industrial Control Network, Sohu 2026 Review, EEFocus |

## Company Overview

Founded in 2020, SEER Robotics' founding team graduated from Zhejiang University and has won the RoboCup robot soccer world championship three times. With the mission of "accelerating an open and diverse intelligent civilization, making intelligent robots accessible to all," the company focuses on the core technology of mobile robot controllers—the "robot brain"—providing intelligent robot solutions to global customers.

The company's core product is the SRC series controller, which integrates perception and localization, intelligent decision-making, and motion control. It is compatible with over 400 components and supports various motion models, including two-wheel differential, four-wheel differential, Mecanum wheel, single/dual steering wheel, and tracked drive. In September 2024, SEER released the world's first integrated embodied intelligence controller, the SRC-5000, supporting integrated "hand-eye-foot" control for humanoid robots. The company has served over 2,100 global customers and has been the global leader in robot controller sales for three consecutive years.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| AMR Core Controller | Mobile robot "brain" | SRC-2000 / SRC-3000FS / SRC-800 | AGV/AMR, automated forklifts |
| Embodied Intelligence Controller | Humanoid/wheeled humanoid robot control | SRC-5000 | Humanoid robots, composite robots |
| Complete Mobile Robot | Standard vehicle reference and delivery | S series (shelf-to-person) / F series (forklift) | Manufacturing, logistics |
| Software Platform | Scheduling and digital middle platform | RDS / SEED / Roboview / M4 | Whole-factory intelligence |

## Representative Products

### SRC-5000

> SRC-5000: Please visit [official materials](https://www.seer-group.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | Not disclosed | - |
| Weight | Not disclosed | - |
| Computing Power | Integrated embodied intelligence controller | Sohu 2026 Review |
| Control Target | Integrated "hand-eye-foot" control for humanoid robots | Sohu 2026 Review |
| Algorithm Support | VLA, reinforcement learning, end-to-end navigation | Sohu 2026 Review |
| Interface/Communication | Compatible with 400+ components | Sohu 2026 Review |
| Price | Not disclosed | Inquiry required |

**Technical Highlights**: The world's first integrated embodied intelligence controller, integrating perception, decision-making, and motion control into one unit, lowering the development threshold for humanoid robots.

**Application Scenarios**: Humanoid robots, wheeled humanoid robots, composite robots, mobile manipulation platforms.

### SRC-3000FS

> SRC-3000FS: Please visit [official materials](https://www.seer-group.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | Not disclosed | - |
| Weight | Not disclosed | - |
| Processor | Cortex-A72×2 / A53×4 / M4×4 | China Industrial Control Network |
| Memory/Storage | 4 GB LPDDR4 / 16 GB eMMC | China Industrial Control Network |
| Interfaces | 24 DI + 16 DO / 2 isolated CAN / 3 isolated 485 / 5 Gigabit Ethernet | China Industrial Control Network |
| Safety Certification | IEC 61508 / IEC 62061 / ISO 13849 | China Industrial Control Network |
| Price | Not disclosed | Inquiry required |

**Technical Highlights**: The world's first safety-rated AMR controller, deeply integrating functional safety with navigation control, offering lower overall cost and higher integration.

**Application Scenarios**: Industrial AMRs, automated forklifts, smart factory infrastructure control.

## Supply Chain Position

- **Upstream Key Components/Materials**: Procured processors, LiDAR, servo motors, drives, sensors, structural parts; self-developed controller hardware, software, and algorithms.
- **Downstream Customers/Application Scenarios**: AGV/AMR manufacturers, automotive OEMs, 3C/semiconductor/new energy manufacturing companies, humanoid robot integrators.
- **Main Competitors/Comparables**: Ketei Robot, Yixing Robot, Sanad, NVIDIA Jetson platform.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_seer`
- Product Entities: `ent_product_seer_src_5000`, `ent_product_seer_src_3000fs`
- Key Relationships:
  - `ent_company_seer` -- `manufactures` --> `ent_product_seer_src_5000`
  - `ent_company_seer` -- `manufactures` --> `ent_product_seer_src_3000fs`

## References

1. [SEER Robotics Official Website](https://www.seer-group.com)
2. [China Industrial Control Network – SRC-3000FS Introduction](https://www.gongkong.com/product/202103/126995.html)
3. [Sohu – 2026 Industrial AGV Review (SEER Robotics)](https://www.sohu.com/a/1032796579_100126075)
4. [EEFocus – SEER Robotics Hong Kong IPO Report](https://www.eefocus.com/gadget/blog/12-03/245872_ae0ad.html)
