# Yaskawa Electric Corporation

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).  
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Yaskawa Electric |
| **English Name** | Yaskawa Electric Corporation |
| **Headquarters** | Kitakyushu, Japan |
| **Founded** | 1915 |
| **Website** | [https://www.yaskawa.com](https://www.yaskawa.com) |
| **Supply Chain Role** | Servo motors, motion control, industrial robots, inverters |
| **Enterprise Type** | Publicly traded (Tokyo Stock Exchange: 6506) |
| **Parent Company/Group** | None (independently listed) |
| **Data Source** | Yaskawa official website, Yaskawa Motoman product pages, public specifications |

## Company Overview

Yaskawa Electric is a globally renowned motion control and industrial robotics company. Its servo drives, inverters, and MOTOMAN robots are widely used in manufacturing automation.

Yaskawa's core competitiveness lies in motor drive and motion control technology. The MOTOMAN series of industrial robots covers welding, handling, assembly, and other scenarios, while the HC series of collaborative robots emphasizes safety and ease of use. Its products provide key components and equipment for humanoid robot joint drives, servo systems, and automated production lines.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Industrial Robots | High-speed, high-precision multi-joint robots | MOTOMAN GP / AR / SP series | Automotive, electronics, metalworking |
| Collaborative Robots | Human-robot collaboration, safety certified | MOTOMAN HC series | Assembly, inspection, packaging |
| Servo & Motion Control | Servo drives, inverters, motion controllers | Σ series / MP3300 | Machine tools, semiconductors, robotics |

## Representative Products

### Yaskawa MOTOMAN HC20DTP Collaborative Robot

> MOTOMAN HC20DTP: Please visit [official materials](https://www.yaskawa.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Number of Axes | 6 | Yaskawa official website |
| Maximum Payload | 20 kg | Yaskawa official website |
| Maximum Working Radius | 1900 mm | Yaskawa official website |
| Repeat Positioning Accuracy | ± 0.05 mm | Yaskawa official website |
| Mechanical Unit Weight | Not disclosed | Yaskawa official website |
| Protection Rating | IP67 (wrist) / IP54 (body) | Yaskawa official website |
| Mounting Method | Floor / Inverted | Yaskawa official website |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: High payload collaborative capability, optional food-grade lubrication, IP67 wrist protection, suitable for collaborative operations in high hygiene standards and harsh environments.

**Application Scenarios**: Food processing, packaging, machine tool loading/unloading, humanoid robot component assembly and inspection.

## Connection to Humanoid Robots

- Yaskawa Electric's capabilities in servo motors, motion control, industrial robots, and inverters can provide key equipment or basic components for humanoid robot component processing, complete machine assembly, and testing.
- High-precision motion control, force control, and autonomous navigation technology are core supports for human-like movement and operation.
- The company's implementation experience in scenarios such as automotive OEMs can provide commercial references for future applications of humanoid robots.

## Supply Chain Position

- **Upstream Key Components/Materials**: Servo motors, reducers, encoders, controllers, structural parts, sensors.
- **Downstream Customers/Application Scenarios**: Automotive OEMs, food & beverage, electronics manufacturing, logistics & warehousing, automation integrators.
- **Main Competitors/Peers**: FANUC, KUKA, ABB, Universal Robots.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_yaskawa`
- Product Entity: `ent_product_yaskawa_motoman`
- Key Relationship:
  - `ent_company_yaskawa` -- `manufactures` --> `ent_product_yaskawa_motoman`

## References

1. [Yaskawa Electric Official Website](https://www.yaskawa.com)
2. [MOTOMAN HC20DTP Product Page](https://www.yaskawa.com/products/robotics/collaborative-robots/motoman-hc20dtp)
3. [Public Materials and Industry Reports](https://www.yaskawa.com)
