# Danaher Corporation

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Danaher |
| **English Name** | Danaher Corporation |
| **Headquarters** | Washington, D.C., USA |
| **Founded** | 1969 |
| **Official Website** | [https://www.danaher.com](https://www.danaher.com) |
| **Supply Chain Segment** | Life Sciences, Diagnostics, Environmental & Applied Solutions, Industrial Motion Control |
| **Enterprise Attribute** | Publicly traded company (NYSE: DHR) |
| **Parent Company/Group** | None (independently listed) |
| **Data Source** | Danaher official website, annual reports, Kollmorgen product documentation |

## Company Overview

Danaher is a global science and technology innovation enterprise, providing life sciences and industrial automation solutions through its portfolio of brands.

Danaher owns numerous brands including Kollmorgen (motion control), Tektronix (test and measurement), and Beckman Coulter (life sciences). In the industrial automation field, Kollmorgen offers servo motors, drives, linear motors, gearboxes, and motion controllers, known for high power density and customization capabilities. Its AKM2G synchronous servo motor can provide compact, high-performance power units for industrial robot, collaborative robot, and humanoid robot joints.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Motion Control | Servo motors and drives | Kollmorgen AKM / AKD | Robotics, packaging, semiconductors |
| Linear Motion | Linear motors, guides, ball screws | Kollmorgen DDL / Thomson | Precision platforms, medical |
| Automation Software | Motion control and simulation | Kollmorgen Motion Toolbox | Machine design, digital twins |

## Representative Products

### Kollmorgen AKM2G Servo Motor

> Kollmorgen AKM2G Servo Motor: Please visit [Official Documentation](https://www.danaher.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Product Type | Synchronous servo motor | Official documentation |
| Power Range | 0.03 kW ~ 7.2 kW (specific range depends on model) | Official documentation |
| Peak Torque | 0.16 Nm ~ 53 Nm | Official documentation |
| Maximum Speed | 8,000 rpm | Official documentation |
| Frame Size | 40 / 60 / 80 / 130 / 180 mm | Official documentation |
| Feedback Type | Resolver / Incremental / Single-turn or multi-turn absolute encoder | Official documentation |
| Protection Rating | IP65 (optional shaft seal) | Official documentation |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: High torque density, wide range of frame sizes and feedback options, plug-and-play with AKD series servo drives, suitable for compact robot joints.

**Application Scenarios**: Industrial robot joints, collaborative robots, semiconductor equipment, packaging machinery, humanoid robot arm and leg joints.

## Relevance to Humanoid Robots

Humanoid robots have extremely high requirements for joint motor torque density, heat generation, and reliability. The AKM2G offers multiple frame sizes and custom windings, making it an optional power unit solution for joint modules.

## Supply Chain Position

- **Upstream Key Components/Materials**: Rare earth magnets, silicon steel laminations, bearings, encoders, winding materials, aluminum alloy housings
- **Downstream Customers/Application Scenarios**: Industrial robots, semiconductor equipment, medical equipment, packaging and printing, aerospace, humanoid robots
- **Main Competitors/Peers**: Siemens, Panasonic, Yaskawa, Inovance

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_danaher`
- Product Entity: `ent_product_danaher_kollmorgen_akm2g`
- Key Relationship:
  - `ent_company_danaher` -- `manufactures` --> `ent_product_danaher_kollmorgen_akm2g`

## References

1. [Danaher Official Website](https://www.danaher.com)
2. [Kollmorgen AKM2G Servo Motor Product Page](https://www.kollmorgen.com/en-us/products/motors/servo-motors/akm2g-servo-motors)
3. Kollmorgen AKM2G servo motor datasheet
