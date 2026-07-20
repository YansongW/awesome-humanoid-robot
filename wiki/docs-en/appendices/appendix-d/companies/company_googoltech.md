---
id: ent_company_googoltech
schema_version: 1
type: company
title: Googol Technology
domain: 02_components
theoretical_depth: system
names:
  zh: 固高科技
  en: Googol Technology
status: active
sources:
  - id: src_googoltech_official
    type: website
    title: Googol Technology Official Website
    url: https://www.googoltech.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# Googol Technology / 固高科技

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 固高科技 |
| **English Name** | Googol Technology |
| **Headquarters** | Shenzhen, Guangdong, China |
| **Founded** | 1999 |
| **Official Website** | [https://www.googoltech.com](https://www.googoltech.com) |
| **Supply Chain Role** | Motion Controller / Servo Drive / Industrial Software |
| **Enterprise Attribute** | Domestic Brand, Listed Company (301510.SZ), Motion Control Leader |
| **Parent Company/Group** | None (Independently Listed) |
| **Data Source** | Googol Technology Official Website, Product Manuals, Prospectus, WAIC 2026 Reports |

## Company Profile

Googol Technology is a leading enterprise in China's motion control technology field, specializing in high-performance motion controllers, servo drives, and industrial control software.

Founded by Professor Li Zexiang and others, the company has long focused on core motion control algorithms and hardware/software platforms. Its products cover the complete chain from motion control cards and controllers to servo drives, widely applied in industrial robots, semiconductor equipment, laser processing, CNC machine tools, and humanoid robots. Its open control architecture and multi-axis coordination capabilities offer strong substitution potential in the domestic high-end equipment sector.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Motion Control Card/Controller | Multi-axis Motion Control | GT-400 / GUC Series | Robotics, CNC, Laser |
| Servo Drive | High-performance Servo Drive | GSHD Series | Industrial Robots, Humanoid Robots |
| Drive-Controller Integrated Unit | Integrated Motor + Drive | Not disclosed | Collaborative Robots |

## Representative Products

### GSHD Series Servo Drive

> GSHD Series Servo Drive: Please visit [Official Materials](https://www.googoltech.com) for details.

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Product Form | Single-axis/Multi-axis AC Servo Drive | Googol Technology Official Website |
| Power Range | 100 W – 7.5 kW | Product Manual |
| Input Voltage | Single-phase/Three-phase 220 VAC / 380 VAC | Product Manual |
| Control Mode | Position/Speed/Torque | Product Manual |
| Communication Protocol | EtherCAT / CANopen | Product Manual |
| Speed Loop Bandwidth | Not disclosed | - |
| Encoder Support | 17/23-bit Absolute, BiSS-C | Product Manual |
| Safety Function | STO (on select models) | Product Manual |
| Price | Not disclosed | Inquiry required |

**Technical Highlights**: High integration, strong multi-axis coordination capability, suitable for high-dynamic force control and complex trajectory planning in robots.

**Application Scenarios**: Industrial robots, humanoid robot joints, semiconductor equipment, laser processing, CNC machine tools.

### GT-400 Motion Control Card

> GT-400 Motion Control Card: Please visit [Official Materials](https://www.googoltech.com) for details.

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Product Form | Multi-axis Motion Control Card | Googol Technology Official Website |
| Number of Controlled Axes | 2/4 axes (depending on model) | Product Manual |
| Control Method | Point-to-Point / Continuous Path / Electronic Gearing | Product Manual |
| Interface | PCI / Terminal Board | Product Manual |
| Encoder Input | 4 channels ABZ Incremental | Product Manual |
| Price | Not disclosed | Inquiry required |

**Technical Highlights**: Open architecture, rich motion control function library, widely used in university research and industrial equipment prototype development.

**Application Scenarios**: Robot control platforms, CNC machine tools, laser cutting machines, semiconductor equipment.

## Supply Chain Position

- **Upstream Key Components/Materials**: DSP/ARM control chips, FPGA, IGBT, PCB, encoder chips, capacitors, magnetic materials.
- **Downstream Customers/Application Scenarios**: Industrial robot manufacturers, humanoid robot integrators, semiconductor equipment, laser equipment, CNC machine tools.
- **Main Competitors/Benchmarks**: Inovance Technology, Leadshine Technology, Beckhoff Electronics, PMAC, Googol's self-developed ecosystem.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_googoltech`
- Product Entities: `ent_component_googoltech_gshd`, `ent_component_googoltech_gt400`
- Key Relationships:
  - `ent_company_googoltech` -- `manufactures` --> `ent_component_googoltech_gshd`
  - `ent_company_googoltech` -- `manufactures` --> `ent_component_googoltech_gt400`

## References

1. [Googol Technology Official Website](https://www.googoltech.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. Googol Technology Prospectus and Product Manuals
