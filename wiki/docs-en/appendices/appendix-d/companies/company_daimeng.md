# Daimeng Robotics

> This entry belongs to [Appendix D: Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 戴盟机器人 (Daimeng (Shenzhen) Robotics Technology Co., Ltd.) |
| **English Name** | Daimeng Robotics |
| **Headquarters** | Shenzhen, China |
| **Founded** | December 2021 |
| **Website** | [https://www.dmrobot.com](https://www.dmrobot.com) |
| **Supply Chain Role** | OEM / General-purpose Humanoid Robots |
| **Company Type** | Startup, Specializing in Tactile Perception and Dexterous Manipulation |
| **Parent Company/Group** | None |
| **Data Sources** | Daimeng official website, Sohu WAIC 2026 report, Lenovo Capital, New Strategy Robot Network |

## Company Overview

Daimeng Robotics was incubated at the Hong Kong University of Science and Technology and founded by Professor Wang Yu, a pioneer in the international robotics field. The company focuses on high-resolution multimodal tactile perception, dexterous hand hardware and software, and "human-centered" teleoperation data systems. With the mission of "making robots guardians of humanity," Daimeng proposes the VTLA (Vision-Tactile-Language-Action) embodied manipulation large model approach, emphasizing that touch is a key modality for robots to understand the physical world.

In October 2025, the Daimeng Sparky 1 robot began mass production at Lenovo Group's Southern Smart Manufacturing Base, marking its transition from demo to batch production. At WAIC 2026 (Booth H3-B324), the company demonstrated vision-tactile sensors, data acquisition equipment, and humanoid robots' long-sequence complex manipulation capabilities in contact-rich scenarios such as fruit packaging and desktop organization.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|---|---|---|---|
| Humanoid Robot | Dexterous General-purpose Robot | Sparky 1 | Industrial Assembly, Service Manipulation |
| Vision-Tactile Sensor | Multidimensional High-Resolution High-Frequency Tactile Perception | DM-Tac W | Dexterous Hands, Industrial Inspection |
| Dexterous Hand | Multidimensional Tactile Perception Five-Fingered Hand | DM-Hand1 | Research, Industrial Grasping |
| Data Acquisition System | Wearable Teleoperation and Data Platform | DM-EXton / EGO | Data Training, Teleoperation |

## Representative Products

### Sparky 1

> Sparky 1: Please visit [Official Information](https://www.dmrobot.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | Not disclosed | - |
| Weight | Not disclosed | - |
| Degrees of Freedom | Not disclosed | - |
| Payload/Torque | Single-arm/Two-hand Fine Manipulation | Official Demo |
| Speed/RPM | Not disclosed | - |
| Battery Life | Not disclosed | - |
| Interface/Communication | Supports Teleoperation, VTLA Large Model | Sohu Report |
| Price | Not disclosed | Inquire for Pricing |

**Technical Highlights**: Multimodal perception integrating vision and touch, VTLA end-to-end manipulation large model, teleoperation data acquisition, capable of fine tasks such as pouring water and precision component assembly.

**Application Scenarios**: Smart Manufacturing, Warehouse Logistics, Home Services, Research & Education.

### DM-Tac W

> DM-Tac W: Please visit [Official Information](https://www.dmrobot.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | Thickness reduced to millimeter level | Lenovo Capital Report |
| Weight | Not disclosed | - |
| Resolution | Tangential force 320×240 | Lenovo Capital Report |
| Perception Modalities | Shape, Texture, Hardness, Slip, Pressure, Tangential Force | Lenovo Capital Report |
| Lifespan | Contact material lifespan approx. 5,000,000 cycles | Lenovo Capital Report |
| Interface/Communication | Not disclosed | - |
| Price | Not disclosed | Inquire for Pricing |

**Technical Highlights**: World's first "monochromatic light + pattern encoding" vision-tactile sensor, eliminating complex calibration, enabling high-frequency perception with a monochrome camera, and fitting into human-like fingertips.

**Application Scenarios**: Dexterous Fingertips, Soft Packaging Inspection, Microstructure Inspection, Fruit Sorting.

## Supply Chain Position

- **Upstream Key Components/Materials**: Self-developed vision-tactile sensors and dexterous hands; externally purchased motors, reducers, cameras, computing platforms.
- **Downstream Customers/Application Scenarios**: Smart Manufacturing Factories, Warehouse Logistics, Fast-Moving Consumer Goods Sorting, Research & Education.
- **Main Competitors/Peers**: Lingxin Qiaoshou, Zhiyuan Robot, Figure AI.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_daimeng`
- Product Entities: `ent_product_daimeng_sparky_1`, `ent_product_daimeng_dm_tac_w`
- Key Relationships:
  - `ent_company_daimeng` -- `manufactures` --> `ent_product_daimeng_sparky_1`
  - `ent_company_daimeng` -- `manufactures` --> `ent_product_daimeng_dm_tac_w`

## References

1. [Daimeng Robotics Official Website](https://www.dmrobot.com)
2. [Sohu – Daimeng Robotics to Debut at WAIC 2026](https://www.sohu.com/a/1037991173_785961)
3. [Lenovo Capital – Looking at Chinese Innovation: Daimeng Robotics](https://capital.lenovo.com/news/detail/id/1176/s/2.html)
4. [New Strategy Robot Network – Daimeng Robotics Debuts at WAIC 2025](http://www.xzlrobot.com/c14483.html)
