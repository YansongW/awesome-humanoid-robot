---
id: ent_company_inovance
schema_version: 1
type: company
title: Inovance Technology
domain: 02_components
theoretical_depth: system
names:
  zh: 汇川技术
  en: Inovance Technology
status: active
sources:
  - id: src_inovance_official
    type: website
    title: Inovance Technology Official Website
    url: https://www.inovance.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# Inovance Technology / 汇川技术

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 汇川技术 |
| **English Name** | Inovance Technology |
| **Headquarters** | Shenzhen, China |
| **Founded** | 2003 |
| **Official Website** | [https://www.inovance.com](https://www.inovance.com) |
| **Supply Chain Segment** | Servo Systems / Motors / Drives / Frequency Converters |
| **Enterprise Attribute** | Domestic Brand, Listed Company (300124.SZ) |
| **Parent Company/Group** | None (Independently Listed) |
| **Data Sources** | Official Website, Product Manuals, Public Research Reports, WAIC 2026 Coverage |

## Company Overview

China's leading industrial automation company, providing servo motors, drives, PLCs, and robot core components.

Inovance Technology's MS1 series servo motors, paired with the SV680 series high-performance servo drives, cover a power range of 50 W–7.5 kW and support 23/26-bit absolute encoders. They are widely used in industrial robots, humanoid robots, and new energy equipment.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| MS1 Servo Motor | High-response servo motor | MS1H2 / MS1H3 / MS1H4 | Robotics, Machine Tools, Lithium Battery |
| SV680 Servo Drive | High-end single-axis servo drive | SV680P / SV680-INT | Semiconductors, Robotics |

## Representative Products

### MS1H4-40B30CB Servo Motor

> MS1H4-40B30CB Servo Motor: Please visit [Official Materials](https://www.inovance.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Frame Size | 40 mm | Inovance SV630P Manual |
| Rated Power | 400 W | Inovance SV630P Manual |
| Rated Speed | 3000 rpm | Inovance Manual |
| Maximum Speed | 6000 rpm | Inovance Official Website |
| Rated Torque | Not disclosed | - |
| Maximum Torque | Approx. 3.5x rated torque | Inovance Manual (H4 Model) |
| Rotor Inertia | 0.43 kg·cm² | Inovance Manual |
| Encoder | 18-bit multi-turn absolute (T3) | Inovance Manual |
| Protection Rating | IP67 | Inovance Manual |

**Technical Highlights**: Small inertia, small capacity design, high overload capacity, suitable for small robot joints and high-speed positioning applications.

**Application Scenarios**: SCARA, collaborative robot joints, humanoid robot arms, 3C automation.

### SV680P Servo Drive

> SV680P Servo Drive: Please visit [Official Materials](https://www.inovance.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Power Range | 50 W – 7.5 kW | Inovance Official Website |
| Communication Protocol | CANopen / EtherCAT / Pulse | Inovance Official Website |
| Speed Loop Bandwidth | 3.5 kHz | Inovance Europe Official Website |
| Current Loop Frequency | 625 kHz | Inovance Europe Official Website |
| Encoder Support | 23/26-bit absolute, BiSS-C, EnDat 2.2 | Inovance Europe Official Website |
| Safety Functions | STO / SS1 / SLS etc. SIL3/PL e | Inovance Europe Official Website |
| Certifications | CE / UL / KC / UKCA / SEMI F47 | Inovance Official Website |

**Technical Highlights**: High response, comprehensive functional safety, suitable for the dynamic performance and safety requirements of humanoid robots.

**Application Scenarios**: Industrial robots, semiconductor equipment, humanoid robot joint drives.

## Supply Chain Position

- **Upstream Key Components/Materials**: Rare earth magnets, IGBT, PCB, copper wire, aluminum housing, encoder chips
- **Downstream Customers/Application Scenarios**: Industrial robot, humanoid robot, new energy vehicle, photovoltaic/lithium battery equipment manufacturers
- **Main Competitors/Benchmarks**: Hechuan Technology, Leadshine, Yaskawa, Mitsubishi

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_inovance`
- Product Entities: `ent_component_inovance_ms1h4_40b`, `ent_component_inovance_sv680p`
- Key Relationships:
  - `ent_company_inovance` -- `manufactures` --> `ent_component_inovance_ms1h4_40b`
  - `ent_company_inovance` -- `manufactures` --> `ent_component_inovance_sv680p`

## References

1. [Official Website](https://www.inovance.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.inovance.com) (Please verify against actual product models)
