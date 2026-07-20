# KUKA Robotics

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | KUKA Robotics |
| **English Name** | KUKA Robotics |
| **Headquarters** | Augsburg, Germany |
| **Founded** | 1898 |
| **Website** | [https://www.kuka.com](https://www.kuka.com) |
| **Supply Chain Role** | Industrial robots, collaborative robots, mobile robots, automation system integration |
| **Enterprise Attribute** | Public company (formerly Frankfurt Stock Exchange), now a subsidiary of Midea Group |
| **Parent Company/Group** | Midea Group (acquired in 2017) |
| **Data Source** | KUKA official website, KUKA annual reports, public news materials |

## Company Profile

KUKA is a global leader in industrial robots and automation solutions, renowned for its orange six-axis industrial robots, the LBR iiwa collaborative robot, and mobile robot platforms.

KUKA's products cover industries such as automotive, electronics, metalworking, logistics, and medical. Its robot controllers, servo drives, and offline programming software form a complete automation ecosystem. In the humanoid robot supply chain, KUKA's precision assembly robots, collaborative arms, and digital production line solutions can provide core equipment for joint module assembly, full-machine calibration, and batch testing.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Industrial Robots | High-load, high-precision six-axis robots | KR QUANTEC / KR AGILUS / KR CYBERTECH | Automotive, electronics, metalworking |
| Collaborative Robots | Human-robot collaboration, force-controlled safety | LBR iiwa / iiQKA | Assembly, inspection, medical |
| Mobile Robots | Factory logistics AMR/AGV | KMP series / KMR iiwa | Warehousing, semiconductors, automotive |

## Representative Products

### KUKA LBR iiwa Collaborative Robot

> LBR iiwa: Please visit [official materials](https://www.kuka.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Number of axes | 7 | KUKA official website |
| Maximum payload | 14 kg (iiwa 14) / 7 kg (iiwa 7) | KUKA official website |
| Maximum working radius | 820 mm / 1260 mm | KUKA official website |
| Repeatability | ± 0.1 mm | KUKA official website |
| Mechanical unit weight | Not disclosed | KUKA official website |
| Protection rating | IP54 | KUKA official website |
| Mounting method | Floor / Ceiling / Wall | KUKA official website |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: Built-in joint torque sensors enable compliance control and safe human-robot collaboration; open Java interface and iiQKA operating system support rapid deployment.

**Application Scenarios**: Precision assembly, screw tightening, polishing, flexible assembly and testing of humanoid robot components.

## Relevance to Humanoid Robots

- KUKA Robotics' capabilities in industrial robots, collaborative robots, mobile robots, and automation system integration can provide key equipment or basic components for humanoid robot component processing, full-machine assembly, and testing.
- High-precision motion control, force control, and autonomous navigation technologies are core supports for human-like motion and manipulation.
- The company's implementation experience in scenarios such as automotive OEMs can provide commercial references for future applications of humanoid robots.

## Supply Chain Position

- **Upstream Key Components/Materials**: Servo motors, reducers, controllers, structural parts, sensors, cables.
- **Downstream Customers/Application Scenarios**: Automotive OEMs, electronics manufacturers, logistics and warehousing, medical surgical equipment, automation integrators.
- **Main Competitors/Peers**: FANUC, ABB, Yaskawa, MOTOMAN.

## Knowledge Graph Nodes and Relationships

- Company entity: `ent_company_kuka`
- Product entity: `ent_product_kuka_iiwa`
- Key relationships:
  - `ent_company_kuka` -- `manufactures` --> `ent_product_kuka_iiwa`

## References

1. [KUKA Robotics Official Website](https://www.kuka.com)
2. [LBR iiwa Product Page](https://www.kuka.com/en-us/products/robotics-systems/industrial-robots/lbr-iiwa)
3. [Public Materials and Industry Reports](https://www.kuka.com)
