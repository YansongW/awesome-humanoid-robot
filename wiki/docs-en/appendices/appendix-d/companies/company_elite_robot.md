# Elite Robot

> This entry belongs to [Appendix D: Enterprise/Product Wiki](../../appendix-d.md).  
> Data update time: 2026-07-01. All parameters are based on official public materials; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 艾利特机器人 |
| **English Name** | Elite Robot |
| **Headquarters** | Suzhou, Jiangsu, China |
| **Founded** | 2014 |
| **Website** | [https://www.elite-robot.com](https://www.elite-robot.com) |
| **Supply Chain Role** | Complete Machine OEM / Collaborative Robots / Humanoid Robot Components |
| **Enterprise Type** | Domestic Brand, Core Collaborative Robot Manufacturer |
| **Parent Company/Group** | None |
| **Data Source** | Elite Robot official website, product manuals, WAIC 2026 reports, public press releases |

## Company Overview

Elite Robot is a key player in the domestic collaborative robot field, known for its modular, platform-based design and open ecosystem.

The company's EC series collaborative robots cover a payload range of 3–20 kg, emphasizing "platform robots." Through a unified control architecture and interfaces, they support rapid secondary development and industry-specific customization. Elite Robot has numerous deployed cases in automotive, 3C, medical, and education sectors, and is actively expanding into overseas markets.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| EC Series Collaborative Robots | Industrial/Commercial/Scientific Research | EC63 / EC66 / EC75 / EC612 | 3C, Automotive, Medical, Education |
| CS Series | High Protection/High Performance | CS Series | Machine Tending, Grinding |
| Industry Solutions | Composite Robots, Force Control | Custom Solutions | Flexible Manufacturing, Warehousing |

## Representative Products

### EC66 Collaborative Robot

> EC66: Please visit [official materials](https://www.elite-robot.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Product Form | 6-DOF Collaborative Robot | Elite Robot official website |
| Weight | Approx. 17.5 kg | Product manual |
| Payload | 6 kg | Product manual |
| Reach | 914 mm | Product manual |
| Degrees of Freedom | 6 DOF | Public specification |
| Repeatability | ±0.03 mm | Product manual |
| Maximum End-Effector Speed | 2.8 m/s | Product manual |
| Protection Rating | IP54 | Product manual |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: Platform-based control architecture, open SDK with ROS/ROS2 support, drag teaching, collision detection, graphical programming.

**Application Scenarios**: 3C assembly, automotive parts inspection, medical aids, food packaging, scientific research and education.

### EC612 Collaborative Robot

> EC612: Please visit [official materials](https://www.elite-robot.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Product Form | 6-DOF Collaborative Robot | Elite Robot official website |
| Weight | Approx. 38 kg | Product manual |
| Payload | 12 kg | Product manual |
| Reach | 1304 mm | Product manual |
| Degrees of Freedom | 6 DOF | Public specification |
| Repeatability | ±0.05 mm | Product manual |
| Protection Rating | IP54 | Product manual |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: High payload with long reach, suitable for heavy-duty collaborative applications such as material handling, palletizing, and machine tending.

**Application Scenarios**: Automotive assembly, machine tending, logistics handling, metalworking, new energy production lines.

## Supply Chain Position

- **Upstream Key Components/Materials**: Harmonic reducers, servo motors, encoders, controllers, structural parts, cables, sensors.
- **Downstream Customers/Application Scenarios**: 3C electronics, automotive, new energy, medical, food, education and scientific research.
- **Main Competitors/Peers**: JAKA, AUBO, HAN'S Robot, Yuejiang, Universal Robots (UR).

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_elite_robot`
- Product Entities: `ent_product_elite_ec66`, `ent_product_elite_ec612`
- Key Relationships:
  - `ent_company_elite_robot` -- `manufactures` --> `ent_product_elite_ec66`
  - `ent_company_elite_robot` -- `manufactures` --> `ent_product_elite_ec612`

## References

1. [Elite Robot Official Website](https://www.elite-robot.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. Elite Robot product manuals and public press releases
