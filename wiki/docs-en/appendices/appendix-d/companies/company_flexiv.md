# Flexiv

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 非夕科技 (Shanghai Flexiv Robot Technology Co., Ltd.) |
| **English Name** | Flexiv |
| **Headquarters** | Shanghai, China |
| **Founded** | 2016 |
| **Website** | [https://www.flexiv.cn](https://www.flexiv.cn) |
| **Supply Chain Role** | OEM / Adaptive Robot Manufacturer |
| **Enterprise Type** | General Intelligent Robot Unicorn |
| **Parent Company/Group** | None |
| **Data Source** | Flexiv official website, Baidu Baike, China International Industry Fair exhibitor materials, TechNode |

## Company Profile

Flexiv was founded in 2016 by Wang Shiquan and several Stanford alumni, with the core founding team originating from the Stanford Robotics and Artificial Intelligence Laboratory. The company proposed the "Adaptive Robot" category, dedicated to deeply integrating industrial-grade force control, computer vision, and artificial intelligence technology, enabling robotic arms to coordinate hand and eye like humans to complete complex tasks in uncertain environments.

Flexiv's product line includes the adaptive robotic arm Rizon, the force-controlled parallel robot Moonlight, the force-controlled gripper Grav, the AMR mobile platform, and the fully-perceptive adaptive robot Enlight. The company provides solutions for flexible assembly, surface grinding, plugging and sorting in industries such as automotive, 3C electronics, medical, aviation, and logistics, and leads the development of the national standard "Technical Requirements for Robot Adaptive Capabilities."

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|---|---|---|---|
| Adaptive Robotic Arm | 7-axis force-controlled collaborative robot | Rizon 4 / Rizon 4s / Rizon 10 | Precision assembly, grinding, loading/unloading |
| Force-Controlled Parallel Robot | Contact process automation | Moonlight | Grinding, polishing, lamination |
| Force-Controlled Gripper | Industrial-grade force-controlled end-effector | Grav | Gripping, plugging |
| Mobile Manipulation Platform | AMR + Robotic Arm | Flexiv AMR Mobile Platform | Production line logistics, mobile manipulation |

## Representative Products

### Rizon 10

> Rizon 10: Please visit [official materials](https://www.flexiv.cn) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | Reach 941 mm | Flexiv official website |
| Weight | 38 kg | Flexiv official website |
| Degrees of Freedom | 7 DOF | Flexiv official website |
| Payload/Torque | 10 kg | Flexiv official website |
| Speed/Rotation Speed | Standard end-effector linear speed 1.0 m/s | Flexiv official website |
| Force Sensing Accuracy | 0.2 N | Flexiv official website |
| Interface/Communication | Profinet / Modbus TCP/IP | Flexiv official website |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: Human-like 7-degree-of-freedom design, industrial-grade force control, IP65 protection, CE/ETL dual certification, supports installation at any angle and integration with AMR/AGV.

**Application Scenarios**: Cable plugging, precision assembly, flexible grinding, curved surface operations, IDC maintenance.

### Moonlight

> Moonlight: Please visit [official materials](https://www.flexiv.cn) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | Not disclosed | - |
| Weight | Not disclosed | - |
| Degrees of Freedom | Not disclosed | - |
| Payload/Torque | Not disclosed | - |
| Speed/Rotation Speed | Not disclosed | - |
| Force Control Accuracy | Industrial-grade force control | Flexiv official website |
| Interface/Communication | Supports Flexiv control system | Flexiv official website |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: The world's first force-controlled parallel robot, integrating Flexiv's years of force control and sensing technology, suitable for contact process automation.

**Application Scenarios**: Grinding, polishing, lamination, precision machining.

## Supply Chain Position

- **Upstream Key Components/Materials**: Self-developed force sensors, joint-integrated actuators, mechanical structures; externally purchased motors, reducers, vision cameras, computing platforms.
- **Downstream Customers/Application Scenarios**: Manufacturing production lines and automation integrators in automotive, 3C, medical, aviation, logistics, and other industries.
- **Main Competitors/Peers**: ABB, FANUC, Universal Robots, Han's Robot.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_flexiv`
- Product Entities: `ent_product_flexiv_rizon_10`, `ent_product_flexiv_moonlight`
- Key Relationships:
  - `ent_company_flexiv` -- `manufactures` --> `ent_product_flexiv_rizon_10`
  - `ent_company_flexiv` -- `manufactures` --> `ent_product_flexiv_moonlight`

## References

1. [Flexiv Official Website](https://www.flexiv.cn)
2. [Baidu Baike – Flexiv](https://baike.baidu.com/item/Flexiv/55718139)
3. [Flexiv Official Website – Rizon Product Parameters](https://www.flexiv.cn/product/rizon)
4. [TechNode – Flexiv: The Era of Adaptive Robots](https://cn.technode.com/post/2020-01-05/flexiv-cb-2020/)
5. [China International Industry Fair – Flexiv Exhibitor Introduction](https://www.shifair.com/informationDetails/46551.html)
