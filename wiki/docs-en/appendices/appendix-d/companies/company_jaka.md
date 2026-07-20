# Jaka Robotics

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 节卡机器人 |
| **English Name** | Jaka Robotics |
| **Headquarters** | Shanghai, China |
| **Founded** | 2014 |
| **Website** | [https://www.jaka.com](https://www.jaka.com) |
| **Supply Chain Role** | OEM / Collaborative Robots / Humanoid Robot Components |
| **Enterprise Attribute** | Domestic Brand, First Tier in Collaborative Robots, Listed on STAR Market |
| **Parent Company/Group** | None (Independently Listed) |
| **Data Source** | Jaka Official Website, Prospectus, Product Manuals, WAIC 2026 Reports |

## Company Overview

Jaka Robotics is a leading enterprise in China's collaborative robot sector, known for "wireless teaching, graphical programming, and high protection rating."

The company's core product line, the Zu series, covers payloads from 3 to 20 kg and is widely used in automotive, 3C, food, medical, and new energy sectors. Jaka is also expanding into humanoid robot components and industry solutions, possessing full-stack capabilities from robot bodies to control systems and joint modules, while actively exploring overseas markets.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Collaborative Robots | Industrial/Commercial/Scientific | Zu 3 / Zu 5 / Zu 7 / Zu 12 / Zu 18 | Automotive, 3C, Food, Medical |
| Humanoid Robots | Industrial Humanoid Complete Machine | Jaka K-1 | Flexible Manufacturing, Material Handling & Assembly |
| Perception & Software | Vision, Force Control, Cloud Platform | Jaka Lens / Jaka Smart | Smart Manufacturing |

## Representative Products

### Jaka Zu 3 Collaborative Robot

> Jaka Zu 3: Please visit [Official Information](https://www.jaka.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Product Form | 6-DOF Desktop Collaborative Robot | Jaka Official Website |
| Weight | Approx. 12 kg | Product Manual |
| Payload | 3 kg | Product Manual |
| Reach | 626 mm | Product Manual |
| Degrees of Freedom | 6 DOF | Public Specifications |
| Repeatability | ±0.02 mm | Product Manual |
| Maximum End-Effector Speed | 2.3 m/s | Product Manual |
| Protection Rating | IP54 | Product Manual |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: Wireless teach pendant, graphical programming, collision detection, IP54 protection, drag teaching, suitable for human-machine collaborative flexible production lines.

**Application Scenarios**: 3C assembly, automotive parts inspection, food packaging, laboratory automation, education and research.

### Jaka K-1 Humanoid Robot

> Jaka K-1: Please visit [Official Information](https://www.jaka.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Product Form | Wheeled Dual-Arm Humanoid Robot | Jaka Official Website |
| Height | Approx. 170 cm | Public Reports |
| Degrees of Freedom | Not disclosed | - |
| Single-Arm Payload | 5 kg (Reference) | Public Reports |
| Mobility | Chassis Movement | Public Reports |
| Battery Life | Not disclosed | - |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: Dual-arm operation capability based on the Zu series collaborative arms, targeting industrial flexible manufacturing scenarios, emphasizing rapid deployment and process migration.

**Application Scenarios**: Automotive assembly, 3C production line loading/unloading, warehouse material handling, human-machine collaborative workstations.

## Supply Chain Position

- **Upstream Key Components/Materials**: Harmonic drives, servo motors, encoders, controllers, structural parts, cables, vision sensors.
- **Downstream Customers/Application Scenarios**: Automotive OEMs, 3C electronics, food & medical, new energy batteries, humanoid robot complete machine manufacturers.
- **Main Competitors/Peers**: Universal Robots (UR), AUBO, HAN'S Robot, Estun, Yuejiang.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_jaka`
- Product Entities: `ent_product_jaka_zu3`, `ent_product_jaka_k1`
- Key Relationships:
  - `ent_company_jaka` -- `manufactures` --> `ent_product_jaka_zu3`
  - `ent_company_jaka` -- `manufactures` --> `ent_product_jaka_k1`
  - `ent_product_jaka_k1` -- `uses` --> `ent_product_jaka_zu3`

## References

1. [Jaka Robotics Official Website](https://www.jaka.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. Jaka Prospectus and Public Press Releases
