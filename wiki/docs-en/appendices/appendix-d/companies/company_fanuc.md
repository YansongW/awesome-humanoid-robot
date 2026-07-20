# FANUC

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | FANUC Corporation |
| **English Name** | FANUC Corporation |
| **Headquarters** | Oshino, Yamanashi Prefecture, Japan |
| **Founded** | 1972 (spun off from Fujitsu's CNC division) |
| **Official Website** | [https://www.fanuc.com](https://www.fanuc.com) |
| **Supply Chain Role** | Industrial robots, CNC systems, servo motors, factory automation |
| **Company Type** | Publicly traded (Tokyo Stock Exchange: 6954) |
| **Parent Company/Group** | None (independently listed) |
| **Data Sources** | FANUC official website, FANUC America product pages, public specifications |

## Company Overview

FANUC is one of the world's largest manufacturers of industrial robots, renowned for high reliability, high precision, and high speed. Its business covers industrial robots, CNC systems, and factory automation solutions.

FANUC robots are widely used in the automotive, electronics, metalworking, and food industries. Its servo control and motion control technologies are core capabilities for robot joint actuation and whole-machine assembly line automation, providing key equipment for machining, assembly, and testing during the mass production phase of humanoid robots.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Industrial Robots | Multi-joint handling/assembly robots | M-20iD / R-2000iC / LR Mate | Automotive, electronics, logistics |
| Collaborative Robots | Human-robot collaboration | CRX Series | Assembly, inspection |
| CNC & Servo | CNC systems and servo drives | FANUC CNC / SERVO | Machine tools, automation |

## Representative Product

### FANUC M-20iD/35 Industrial Robot

![M-20iD/35](https://www.fanucamerica.com/products/robot/m-20id-35)

> Image source: FANUC America official website. If the link is invalid or missing, please replace it with an official public image URL.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Number of Axes | 6 | FANUC America |
| Maximum Payload | 35 kg | FANUC America |
| Maximum Working Radius | 1831 mm | FANUC America |
| Repeatability | ± 0.03 mm | FANUC America |
| Mechanical Unit Weight | 250 kg | FANUC America |
| Protection Rating | IP54 (standard) | FANUC America |
| Mounting Method | Floor / Tilt / Inverted | FANUC America |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: Hollow arm and wrist design with internal cable routing to reduce interference; high axis speed and high repeatability, suitable for handling and assembly in compact cells.

**Application Scenarios**: Machine tool loading/unloading, automotive parts assembly, humanoid robot component machining and assembly lines.

## Relevance to Humanoid Robots

- Batteries, power semiconductors, and advanced materials are common foundations for achieving long endurance, high dynamics, and lightweight design in humanoid robots.
- Industrial robots and automated production lines provide reusable manufacturing capabilities for the assembly, testing, and mass production of humanoid robots.

## Supply Chain Position

- **Upstream Key Components/Materials**: Servo motors, reducers, controllers, structural parts, sensors.
- **Downstream Customers/Application Scenarios**: Automotive OEMs, electronics manufacturers, machine tool factories, automation integrators.
- **Main Competitors/Peers**: ABB, KUKA, Yaskawa, MOTOMAN.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_fanuc`
- Product Entity: `ent_product_fanuc_m20id_35`
- Key Relationship:
  - `ent_company_fanuc` -- `manufactures` --> `ent_product_fanuc_m20id_35`

## References

1. [FANUC Official Website](https://www.fanuc.com)
2. [FANUC America M-20iD/35 Product Page](https://www.fanucamerica.com/products/robot/m-20id-35)
3. [FANUC M-20iD/25 Datasheet](https://www.robots.com/images/robots/Fanuc/M-Series/Fanuc_M-120iD_25_Datasheet.pdf)
