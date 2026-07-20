# Xvariable / X Square Robot

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 自变量机器人 |
| **English Name** | Xvariable / X Square Robot |
| **Headquarters** | Shenzhen, Guangdong, China |
| **Founded** | December 2023 |
| **Website** | [https://x2robot.com](https://x2robot.com) |
| **Supply Chain Role** | Complete Machine + Large Model / General Wheeled Humanoid Robot + Embodied Intelligence Large Model |
| **Enterprise Attribute** | End-to-End Embodied Intelligence Large Model WALL-A/B, Software-Hardware Integration |
| **Parent Company/Group** | None |
| **Data Source** | Xvariable official website, product pages, About Us |

## Company Profile

Xvariable focuses on developing proprietary general-purpose embodied intelligence large models, using an "Brain + Cerebellum" end-to-end architecture to drive wheeled humanoid robots to perform fine manipulation in open environments.

The company's GreatWall series WALL-A manipulation large model possesses autonomous perception, decision-making, and high-precision manipulation capabilities. In August 2025, it released the Quanta X2, a new generation general wheeled humanoid robot with 62 degrees of freedom across the body, a single arm span of 765 mm, and a repeat positioning accuracy of ±0.03 mm. It is equipped with multi-modal sensors such as 2D LiDAR, RGBD, and 3D-TOF, targeting scenarios like industrial assembly, home services, and hospitality.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| General Wheeled Humanoid Robot | Research, Industry, Service | Quanta X1 / Quanta X2 | Research & Education, Industrial Assembly, Hotel Service |
| Dexterous Hand | Fine Manipulation | ArtiXon Hand | Research, Industry, Service Robot End-Effector |

## Representative Products

### Xvariable Quanta X2

![Xvariable Quanta X2](https://x2robot-open.oss-cn-shenzhen.aliyuncs.com/quantum2_qiepian/x2/12_m.png)

> Image source: Xvariable official website product image.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | Height 164 cm; Working height 0–2 m | Xvariable official website |
| Weight | Not disclosed | - |
| Degrees of Freedom | Full body 62 DOF; Torso 6 DOF; Single dexterous hand 20 DOF | Xvariable official website |
| Payload/Torque | Single arm rated payload 6 kg; Max dual arm payload 25 kg | Xvariable official website |
| Speed/Rotation Speed | End-effector speed 1.8 m/s; Chassis movement speed 1 m/s | Xvariable official website |
| Battery Life | Not disclosed | - |
| Interfaces/Communication | 2D LiDAR, Ultrasonic ×4, RGBD, 3D-TOF, Single-point TOF, Infrared; WALL-A end-to-end large model | Xvariable official website |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: Billion-parameter WALL-A end-to-end manipulation large model, full body 62 DOF, ±0.03 mm repeat positioning, human-like five-finger dexterous hand, cross-task cross-scenario generalization

**Application Scenarios**: Industrial assembly, wire harness organization, hotel towel replacement, clothes hanging, clutter storage, beverage preparation, research & education.

### Xvariable Quanta X1

> Xvariable Quanta X1: Please visit [official materials](https://x2robot.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | Working height 0–1 m | Public reports |
| Weight | Not disclosed | - |
| Degrees of Freedom | Not disclosed | - |
| Payload/Torque | Not disclosed | - |
| Speed/Rotation Speed | Not disclosed | - |
| Battery Life | Not disclosed | - |
| Interfaces/Communication | WALL-A large model, Mechanical exoskeleton/VR teleoperation | Public reports |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: Wheeled dual-arm research platform, supports remote teleoperation, data collection, and model validation

**Application Scenarios**: Research & education, embodied intelligence algorithm validation.

## Supply Chain Position

- **Upstream Key Components/Materials**: Self-developed WALL-A large model, joints, dexterous hands, sensors, computing platform; externally purchased motors, reducers, batteries, camera modules.
- **Downstream Customers/Application Scenarios**: Industrial manufacturing, hotel services, new retail, research & education, home services.
- **Main Competitors/Benchmarks**: Zhiyuan Robot, Figure AI, Astribot, Galaxy General

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_xvariable`
- Product Entity: `ent_product_xvariable_quanta_x2`
- Component Entity: `ent_component_xvariable_artixon_hand`
- Key Relationships:
  - `ent_company_xvariable` -- `manufactures` --> `ent_product_xvariable_quanta_x2`
  - `ent_company_xvariable` -- `manufactures` --> `ent_component_xvariable_artixon_hand`
  - `ent_product_xvariable_quanta_x2` -- `uses` --> `ent_component_xvariable_artixon_hand`

## References

1. [Xvariable Official Website](https://x2robot.com)
2. [Quanta X2 Product Page](https://x2robot.com/product/quantum2)
3. [About Us](https://x2robot.com/about)
