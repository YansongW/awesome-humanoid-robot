---
id: ent_company_invt
schema_version: 1
type: company
title: INVT Electric
domain: 02_components
theoretical_depth: system
names:
  zh: 英威腾
  en: INVT Electric
status: active
sources:
  - id: src_invt_official
    type: website
    title: INVT Electric Official Website
    url: https://www.invt.com.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# INVT Electric

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 英威腾 |
| **English Name** | INVT Electric |
| **Headquarters** | Shenzhen, Guangdong, China |
| **Founded** | 2002 |
| **Official Website** | [https://www.invt.com.cn](https://www.invt.com.cn) |
| **Supply Chain Segment** | Inverters / Servo Systems / PLC / New Energy Electric Drives |
| **Enterprise Type** | Domestic Brand, Listed Company (002334.SZ) |
| **Parent Company/Group** | None (Independently Listed) |
| **Data Source** | INVT Official Website, Product Manuals, Annual Reports, WAIC 2026 Coverage |

## Company Overview

INVT Electric is a representative enterprise in China's industrial automation and energy power sectors, with products covering inverters, servo systems, PLCs, UPS, and new energy vehicle electric drives.

The company's servo product line, represented by the DA200 and DA300 series, targets applications such as industrial robots, CNC machine tools, printing and packaging, and humanoid robots. With deep expertise in power electronics and drive control, INVT has become a key player in the domestic servo drive market, leveraging cost-performance advantages and industry solution capabilities.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|-------------------------|-------------------|
| DA200/DA300 Servo System | General/High-Performance Servo | DA200 / DA300 | Robotics, Machine Tools, Lithium Battery |
| Inverters | General Vector Control | Goodrive Series | Fans, Pumps, Hoisting |
| PLC/HMI | Industrial Control | IVC Series | Automated Production Lines |

## Representative Products

### DA200 Series Servo Drive

> DA200 Series Servo Drive: Please visit [Official Materials](https://www.invt.com.cn) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Product Form | Single-Axis AC Servo Drive | INVT Official Website |
| Power Range | 100 W – 7.5 kW | Product Manual |
| Input Voltage | Single-Phase/Three-Phase 220 VAC / 380 VAC | Product Manual |
| Control Mode | Position/Speed/Torque | Product Manual |
| Communication Protocol | Modbus / CANopen / EtherCAT | Product Manual |
| Speed Loop Bandwidth | 2.5 kHz (Reference) | Product Manual |
| Encoder Support | 17/23-Bit Absolute, Incremental | Product Manual |
| Safety Function | STO (Selected Models) | Product Manual |
| Price | Not Disclosed | Inquire for Pricing |

**Technical Highlights**: Fast response, easy commissioning, supports multiple buses, suitable for domestic substitution in robot joints and automation equipment.

**Application Scenarios**: Industrial Robots, Humanoid Robots, CNC Machine Tools, Electronics Manufacturing, Packaging Machinery.

### DA300 Series Servo Drive

> DA300 Series Servo Drive: Please visit [Official Materials](https://www.invt.com.cn) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Product Form | High-Performance AC Servo Drive | INVT Official Website |
| Power Range | 100 W – 7.5 kW | Product Manual |
| Control Mode | Position/Speed/Torque | Product Manual |
| Communication Protocol | EtherCAT / CANopen | Product Manual |
| Speed Loop Bandwidth | Not Disclosed | - |
| Encoder Support | 23-Bit Absolute | Product Manual |
| Price | Not Disclosed | Inquire for Pricing |

**Technical Highlights**: High response, high-precision positioning, suitable for high-end robotics and semiconductor equipment applications.

**Application Scenarios**: Industrial Robots, Collaborative Robots, Semiconductor Equipment, High-End CNC Machine Tools.

## Supply Chain Position

- **Upstream Key Components/Materials**: IGBT, MOSFET, PCB, Capacitors, Copper Wire, Aluminum Housing, Encoder Chips, Magnetic Materials, DSP/ARM Control Chips.
- **Downstream Customers/Application Scenarios**: Industrial Robot Manufacturers, Humanoid Robot Integrators, Machine Tools, Printing and Packaging, Lithium Battery Equipment, New Energy Vehicle Companies.
- **Main Competitors/Benchmarks**: Inovance Technology, Delta, Yaskawa, Mitsubishi, Leadshine.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_invt`
- Product Entities: `ent_component_invt_da200`, `ent_component_invt_da300`
- Key Relationships:
  - `ent_company_invt` -- `manufactures` --> `ent_component_invt_da200`
  - `ent_company_invt` -- `manufactures` --> `ent_component_invt_da300`

## References

1. [INVT Official Website](https://www.invt.com.cn)
2. [WAIC 2026 Exhibition Coverage](https://www.worldrobotconference.com)
3. INVT Annual Reports and Product Manuals
