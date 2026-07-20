# ABB

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Swiss ABB Group |
| **English Name** | ABB Ltd. |
| **Headquarters** | Zurich, Switzerland |
| **Founded** | 1988 (merger of ASEA and BBC Brown Boveri) |
| **Website** | [https://global.abb](https://global.abb) |
| **Supply Chain Segment** | Industrial robots, motion control, electrical equipment, automation systems |
| **Enterprise Attribute** | Publicly traded company (SIX: ABBN) |
| **Parent Company/Group** | None (independently listed) |
| **Data Source** | ABB Robotics official website, product pages, public information |

## Company Overview

ABB is one of the global leaders in industrial automation and robotics technology. Its robotics business covers industrial robots, collaborative robots, and autonomous mobile robots.

ABB robots are widely used in automotive manufacturing, electronics assembly, metalworking, food and beverage, and logistics warehousing. Although ABB currently primarily serves the industrial sector, its heavy-duty robots, motion control technology, and digital platforms can provide key equipment and process capabilities for the assembly, testing, and production line automation of humanoid robot manufacturing.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Industrial Robots | Multi-joint heavy-duty/high-speed robots | IRB 8700 / IRB 7600 / IRB 4600 | Automotive, metalworking, logistics |
| Collaborative Robots | Human-robot collaborative assembly | YuMi / GoFa | Electronics, medical |
| Robot Software | Offline programming and simulation | RobotStudio | Robot integration and digital twins |

## Representative Products

### ABB IRB 8700 Industrial Robot

![IRB 8700](https://global.abb/products/robotics/industrial-robots/irb-8700)

> Image source: ABB Robotics official website. If the link is invalid or missing, please replace it with an official public image URL.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Number of Axes | 6 | ABB official website |
| Maximum Payload | 800 kg (1000 kg with wrist down) | ABB official website / Automate.org |
| Maximum Working Radius | 3.5 m | ABB official website |
| Repeat Positioning Accuracy | Not disclosed | Not disclosed |
| Protection Rating | IP 67 | ABB official website |
| Mounting Method | Floor | ABB official website |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: ABB's highest payload multi-purpose industrial robot, featuring a long reach and high inertia capability, suitable for heavy-duty handling, body assembly, and large workpiece processing.

**Application Scenarios**: Automotive final assembly lines, heavy component handling, humanoid robot complete assembly and testing production lines.

## Relevance to Humanoid Robots

- Batteries, power semiconductors, and advanced materials are common foundations for achieving long endurance, high dynamics, and lightweight design in humanoid robots.
- Industrial robots and automated production lines provide reusable manufacturing capabilities for the complete assembly, testing, and mass production of humanoid robots.

## Supply Chain Position

- **Upstream Key Components/Materials**: Servo motors, reducers, controllers, structural parts, sensors.
- **Downstream Customers/Application Scenarios**: Automotive OEMs, electronics manufacturers, metalworking enterprises, logistics warehousing.
- **Main Competitors/Peers**: FANUC, KUKA, Yaskawa, MOTOMAN.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_abb`
- Product Entity: `ent_product_abb_irb_8700`
- Key Relationship:
  - `ent_company_abb` -- `manufactures` --> `ent_product_abb_irb_8700`

## References

1. [ABB Official Website](https://global.abb)
2. [ABB IRB 8700 Product Page](https://global.abb/products/robotics/industrial-robots/irb-8700)
3. [Automate.org IRB 8700 Introduction](https://www.automate.org/products/abb-inc/irb-8700-abbs-highest-payload-robot)
