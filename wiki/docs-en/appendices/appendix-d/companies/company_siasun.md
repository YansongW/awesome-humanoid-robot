# SIASUN Robot & Automation

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed".

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 新松机器人 |
| **English Name** | SIASUN Robot & Automation |
| **Headquarters** | Shenyang, Liaoning, China |
| **Founded** | 2000 |
| **Website** | [https://www.siasun.com](https://www.siasun.com) |
| **Supply Chain Role** | OEM / Industrial Robots + Humanoid Robots + Intelligent Manufacturing Systems |
| **Enterprise Attribute** | Leading domestic robot manufacturer, listed company (300024) |
| **Parent Company/Group** | Backed by Shenyang Institute of Automation, Chinese Academy of Sciences |
| **Data Source** | SIASUN official website, Zhongke SIASUN press releases, industry research reports |

## Company Profile

SIASUN Robot & Automation is a leading domestic provider of robots and intelligent manufacturing solutions. Leveraging its accumulated expertise in industrial robots, mobile robots, and collaborative robots, it has launched the wheeled humanoid robot Ruike series.

In July 2025, Zhongke SIASUN released two bionic humanoid robots, the MR73A and MR73B, from the "Ruike (rico)" series, targeting industrial flexible collaboration with "hand-brain coordination" and "agile legs and feet" respectively. SIASUN also launched the "Songyi" wheeled humanoid robot and the "Songxing" bipedal humanoid robot, continuously expanding its embodied intelligence product matrix.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| Industrial Robots & Collaborative Robots | Welding, handling, assembly, inspection | SR/SCR/GCR series, Duco collaborative robots | Automotive, 3C, Semiconductor, Energy |
| Humanoid Robots | Industrial flexible collaboration, commercial service | Ruike MR73A / MR73B, Songyi / Songxing | Warehouse logistics, exhibition hall guidance, home companionship |

## Representative Products

### SIASUN Ruike MR73A

![SIASUN Ruike MR73A](https://www.siasun.com/uploads/article/detail/20251015167/1752127099597286.jpg)

> Image source: Product image from SIASUN official website press release.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | Whole unit 650×600×1700 mm; Folded 650×600×1100 mm | SIASUN official website / Industry research report |
| Weight | < 100 kg | SIASUN official website / Industry research report |
| Degrees of Freedom | 21 DOF (some reports mention 27 DOF, subject to official confirmation) | SIASUN official website / Industry research report |
| Payload/Torque | Dual arms with 21 DOF, supports whole-body impedance control | SIASUN official website |
| Speed/RPM | Max movement speed approx. 0.8 m/s | Industry research report |
| Battery Life | ≥ 6 hours | Industry research report |
| Interface/Communication | Voice large model, multilingual, AI vision, autonomous localization and navigation | SIASUN official website |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: Wheeled humanoid, dual-arm compliant control, whole-body impedance control, autonomous localization and navigation with dynamic obstacle avoidance, multilingual voice large model interaction

**Application Scenarios**: Warehouse/factory handling, picking, inspection, guidance, commercial reception, document delivery.

### SIASUN Ruike MR73B

> SIASUN Ruike MR73B: Please visit [official materials](https://www.siasun.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | 550×550×1600 mm | Industry research report |
| Weight | ≤ 100 kg | Industry research report |
| Degrees of Freedom | Not disclosed | - |
| Payload/Torque | Not disclosed | - |
| Speed/RPM | Movement speed 1 m/s | Industry research report |
| Battery Life | > 6 hours | Industry research report |
| Interface/Communication | Autonomous navigation, obstacle avoidance, lifting column, autonomous charging | Industry research report |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: Lifting column chassis, intelligent lifting for storage/retrieval, suitable for shelves and workstations of varying heights

**Application Scenarios**: Cargo handling in warehouse logistics centers, intelligent inbound/outbound, material distribution in production workshops.

## Supply Chain Position

- **Upstream Key Components/Materials**: Self-developed BSJ series bionic humanoid integrated joint modules, controllers, servo systems, sensors; externally purchased batteries, structural parts, computing platforms.
- **Downstream Customers/Application Scenarios**: Automotive manufacturing, 3C electronics, warehouse logistics, commercial services, exhibition hall guidance, healthcare institutions.
- **Main Competitors/Peers**: ABB, Fanuc, KUKA, Estun Automation, Inovance Technology, UBTECH

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_siasun`
- Product Entity: `ent_product_siasun_mr73a`
- Component Entity: `ent_component_siasun_bsj_joint_module`
- Key Relationships:
  - `ent_company_siasun` -- `manufactures` --> `ent_product_siasun_mr73a`
  - `ent_company_siasun` -- `manufactures` --> `ent_component_siasun_bsj_joint_module`
  - `ent_product_siasun_mr73a` -- `uses` --> `ent_component_siasun_bsj_joint_module`

## References

1. [SIASUN Duco Bionic Humanoid Robot New Product Launch](https://www.siasun.com/news-detail167.html)
2. [SIASUN Industrial Robot Product Page](https://www.siasun.com/products.html)
3. [Tencent News – SIASUN Ruike Series Report](https://view.inews.qq.com/a/20250710A0496M00)
