# Bosch Rexroth AG

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Bosch Rexroth |
| **English Name** | Bosch Rexroth AG |
| **Headquarters** | Lohr am Main, Germany |
| **Founded** | 2001 (Rexroth origins trace back to 1795) |
| **Website** | [https://www.boschrexroth.com](https://www.boschrexroth.com) |
| **Supply Chain Role** | Drive and control technology, hydraulics, linear motion, servo systems, industrial automation platforms |
| **Company Type** | Privately held (wholly owned subsidiary of Robert Bosch GmbH) |
| **Parent Company/Group** | Robert Bosch GmbH |
| **Data Source** | Bosch Rexroth website, product pages, Bosch Group annual report |

## Company Overview

Bosch Rexroth is a global system supplier in the field of drive and control technology.

Bosch Rexroth offers products such as hydraulics, electric drives and controls, linear motion and assembly technologies, IoT and automation platforms, serving factory automation, mobile machinery, and Industry 4.0. Its ctrlX AUTOMATION platform features a "smartphone-like" app ecosystem and an open Linux real-time system, supporting PLC, motion, robotics, IoT, and machine vision applications. Its servo and linear motion products are also suitable for humanoid robot joints and actuators.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Automation Platform | Open, app-based control | ctrlX CORE / ctrlX OS | Machine tools, packaging, mobile machinery |
| Electric Drives | Servo drives and motors | IndraDrive / MS2N | Robotics, machine tools, logistics |
| Linear Motion | Guide rails, ball screws, electric cylinders | Ball rail systems / Planetary roller screws | Assembly, semiconductors, medical |

## Representative Products

### Bosch Rexroth ctrlX CORE

> Bosch Rexroth ctrlX CORE: Please visit [official documentation](https://www.boschrexroth.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Product Type | Industrial automation controller / IPC | Official documentation |
| Operating System | ctrlX OS (based on Linux real-time kernel) | Official documentation |
| Processor | Not disclosed | Not disclosed |
| Number of Controlled Axes | Up to 99 axes | Official documentation |
| Communication Interfaces | EtherCAT, Sercos III, PROFINET, OPC UA, MQTT | Official documentation |
| Supply Voltage | 24 VDC | Official documentation |
| Operating Temperature | 0 °C ~ 50 °C | Official documentation |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: app-based architecture, open Linux real-time system, integrated PLC/motion/IoT/robotics functions, multi-protocol communication.

**Application Scenarios**: Smart machine tools, packaging machinery, mobile robots, warehouse logistics, humanoid robot control systems and edge computing.

## Relevance to Humanoid Robots

Humanoid robot development requires flexible software architecture and multi-axis real-time control. The app ecosystem and open interfaces of ctrlX CORE can serve as a robot body controller or joint drive gateway.

## Supply Chain Position

- **Upstream Key Components/Materials**: Processors, power semiconductors, hydraulic components, bearings, aluminum, PCBs
- **Downstream Customers/Application Scenarios**: Machine tools, packaging, mobile machinery, automotive, logistics automation
- **Main Competitors/Peers**: Siemens, Beckhoff, B&R, Schneider Electric

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_bosch_rexroth`
- Product Entity: `ent_product_bosch_rexroth_ctrlx_core`
- Key Relationship:
  - `ent_company_bosch_rexroth` -- `manufactures` --> `ent_product_bosch_rexroth_ctrlx_core`

## References

1. [Bosch Rexroth Official Website](https://www.boschrexroth.com)
2. [Bosch Rexroth ctrlX CORE Product Page](https://www.boschrexroth.com/en/us/products/product-groups/controls/ctrlx-automation/ctrlx-core)
3. Bosch Rexroth ctrlX AUTOMATION product pages
