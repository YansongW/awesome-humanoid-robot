# AUBO Robotics

> This entry belongs to [Appendix D: Company/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 遨博智能 |
| **English Name** | AUBO Robotics |
| **Headquarters** | Beijing, China |
| **Founded** | 2015 |
| **Website** | [https://www.aubo-robotics.cn](https://www.aubo-robotics.cn) |
| **Supply Chain Role** | OEM / Collaborative Robots / Humanoid Robot Components |
| **Company Type** | Domestic Brand, Core Collaborative Robot Manufacturer |
| **Parent Company/Group** | None |
| **Data Source** | AUBO official website, product manuals, WAIC 2026 reports, public press releases |

## Company Profile

AUBO Robotics is one of the earliest domestic manufacturers to achieve large-scale application of collaborative robots, known for high cost-performance and an open ecosystem.

The AUBO-i series collaborative robots cover payloads from 3 to 20 kg and are widely used in assembly, inspection, machine tending, grinding, and other fields. The company also provides solutions including robot vision, force control, and AGV composite robots, and is actively deploying humanoid robot joints and whole-robot collaborations.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Collaborative Robots | Industrial/Commercial/Scientific | AUBO-i3 / i5 / i10 / i16 / i20 | 3C, Automotive, Medical, Food |
| Composite Robots | Mobile Collaboration | AUBO-AMR Series | Warehouse Logistics, Flexible Production Lines |
| Humanoid Components | Integrated Joint Modules | Not disclosed | Humanoid Robots, Collaborative Robots |

## Representative Products

### AUBO-i5 Collaborative Robot

> AUBO-i5: Please visit [official documentation](https://www.aubo-robotics.cn) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Product Form | 6-DOF Collaborative Robot | AUBO official website |
| Weight | Approx. 24 kg | Product manual |
| Payload | 5 kg | Product manual |
| Reach | 1000 mm | Product manual |
| Degrees of Freedom | 6 DOF | Public specifications |
| Repeatability | ±0.03 mm | Product manual |
| Maximum End-Effector Speed | 2.8 m/s | Product manual |
| Protection Rating | IP54 | Product manual |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: Modular joints, open API, drag teaching, collision detection, supports ROS/ROS2, suitable for flexible automation upgrades in SMEs.

**Application Scenarios**: 3C assembly, automotive parts inspection, grinding and polishing, medical aids, coffee retail.

### AUBO-AMR Composite Robot

> AUBO-AMR: Please visit [official documentation](https://www.aubo-robotics.cn) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Product Form | Mobile Base + Collaborative Arm | AUBO official website |
| Payload | Not disclosed | - |
| Navigation Method | Laser SLAM | Product manual |
| Collaborative Arm Model | AUBO-i Series (depending on configuration) | Product manual |
| Battery Life | Not disclosed | - |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: Integrated mobile base and collaborative arm, supports material transfer and machine tending between production lines, reducing deployment costs.

**Application Scenarios**: Semiconductor wafer transfer, 3C production line material delivery, warehouse logistics, flexible manufacturing.

## Supply Chain Position

- **Upstream Key Components/Materials**: Harmonic reducers, servo motors, encoders, controllers, structural parts, cables, batteries (composite robots).
- **Downstream Customers/Application Scenarios**: 3C electronics, automotive parts, medical devices, food, logistics and warehousing.
- **Main Competitors/Peers**: Universal Robots (UR), JAKA, HAN'S Robot, YUJIN Robot, ROKAE.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_aubo`
- Product Entities: `ent_product_aubo_i5`, `ent_product_aubo_amr`
- Key Relationships:
  - `ent_company_aubo` -- `manufactures` --> `ent_product_aubo_i5`
  - `ent_company_aubo` -- `manufactures` --> `ent_product_aubo_amr`
  - `ent_product_aubo_amr` -- `uses` --> `ent_product_aubo_i5`

## References

1. [AUBO Robotics Official Website](https://www.aubo-robotics.cn)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. AUBO product manuals and public press releases
