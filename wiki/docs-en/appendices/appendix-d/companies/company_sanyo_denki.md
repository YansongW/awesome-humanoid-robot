---
id: ent_company_sanyo_denki
schema_version: 1
type: company
title: Sanyo Denki
domain: 02_components
theoretical_depth: system
names:
  zh: 山洋电气
  en: Sanyo Denki
status: active
sources:
  - id: src_sanyo_denki_official
    type: website
    title: Sanyo Denki Official Website
    url: https://www.sanyodenki.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# Sanyo Denki / 山洋电气

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 山洋电气 |
| **English Name** | Sanyo Denki |
| **Headquarters** | Tokyo, Japan |
| **Founded** | 1927 |
| **Website** | [https://www.sanyodenki.com](https://www.sanyodenki.com) |
| **Supply Chain Segment** | Servo Systems / Cooling Fans / Power Supplies / Motion Control |
| **Company Type** | Foreign Brand, Listed Company (TSE 6516) |
| **Parent Company/Group** | None (Independently Listed) |
| **Data Source** | Sanyo Denki Official Website, Product Manuals, Public Research Reports, WAIC 2026 Coverage |

## Company Overview

Sanyo Denki is a long-established Japanese manufacturer of servo systems and cooling equipment, renowned for high reliability, compact design, and low noise.

Its SANMOTION series servo motors and drives are widely used in semiconductor equipment, medical devices, robotics, and precision automation. Sanyo Denki holds a technological lead in compact high-response servos, brushless motors, and cooling fans, serving as a key supplier of components for advanced humanoid robots and precision equipment.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| SANMOTION R Servo | High-Performance AC Servo | SANMOTION R | Semiconductor, Medical, Robotics |
| SANMOTION G Servo | General-Purpose Servo | SANMOTION G | Automation, Machine Tools |
| Cooling Fans / Power Supplies | Thermal Management & Power Supply | 9S Series Fans | Servers, Industrial Equipment |

## Representative Products

### SANMOTION R Series Servo Motor

> SANMOTION R Series: Please visit [Official Documentation](https://www.sanyodenki.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Product Form | AC Servo Motor | Sanyo Denki Official Website |
| Frame Size | 20–130 mm (varies by model) | Product Manual |
| Rated Power | 10 W – 5 kW | Product Manual |
| Rated Speed | 1000–6000 rpm | Product Manual |
| Encoder | 20-bit Absolute (Reference) | Product Manual |
| Protection Rating | IP65 (some models) | Product Manual |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: Compact size, fast response, smooth low-speed operation, suitable for space-constrained joints such as robot fingers and wrists.

**Applications**: Semiconductor equipment, medical robots, collaborative robots, humanoid robot fingers/wrists.

### SANMOTION R ADVANCED Servo Drive

> SANMOTION R ADVANCED: Please visit [Official Documentation](https://www.sanyodenki.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Product Form | Single-Axis AC Servo Drive | Sanyo Denki Official Website |
| Power Range | 10 W – 5 kW | Product Manual |
| Communication Protocol | EtherCAT / MECHATROLINK / CANopen | Product Manual |
| Control Mode | Position / Speed / Torque | Product Manual |
| Encoder Support | 20/23-bit Absolute | Product Manual |
| Safety Function | STO (some models) | Product Manual |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: High response, high-resolution feedback, support for multiple industrial buses, suitable for precision motion and force control applications.

**Applications**: Semiconductor equipment, medical robots, humanoid robot joints, precision positioning stages.

## Supply Chain Position

- **Upstream Key Components/Materials**: Rare earth magnets, IGBT, PCB, copper wire, aluminum housing, encoder chips, bearings, DSP/ARM control chips.
- **Downstream Customers/Applications**: Semiconductor equipment manufacturers, medical robot manufacturers, humanoid robot integrators, precision automation equipment manufacturers.
- **Main Competitors/Peers**: Yaskawa, Panasonic, Mitsubishi, Inovance Technology, Hechuan Technology.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_sanyo_denki`
- Product Entities: `ent_component_sanyo_sanmotion_r_motor`, `ent_component_sanyo_sanmotion_r_drive`
- Key Relationships:
  - `ent_company_sanyo_denki` -- `manufactures` --> `ent_component_sanyo_sanmotion_r_motor`
  - `ent_company_sanyo_denki` -- `manufactures` --> `ent_component_sanyo_sanmotion_r_drive`
  - `ent_component_sanyo_sanmotion_r_drive` -- `uses` --> `ent_component_sanyo_sanmotion_r_motor`

## References

1. [Sanyo Denki Official Website](https://www.sanyodenki.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. Sanyo Denki Product Manuals and Annual Reports
