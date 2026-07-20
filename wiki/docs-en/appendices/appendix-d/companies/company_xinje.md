---
id: ent_company_xinje
schema_version: 1
type: company
title: Xinje Electric
domain: 02_components
theoretical_depth: system
names:
  zh: 信捷电气
  en: Xinje Electric
status: active
sources:
  - id: src_xinje_official
    type: website
    title: Xinje Electric Official Website
    url: https://www.xinje.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# Xinje Electric

> This entry belongs to [Appendix D: Enterprise/Product Wiki](../../appendix-d.md).
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 信捷电气 |
| **English Name** | Xinje Electric |
| **Headquarters** | Wuxi, Jiangsu, China |
| **Founded** | 2008 |
| **Official Website** | [https://www.xinje.com](https://www.xinje.com) |
| **Supply Chain Segment** | PLC / Servo System / HMI / Inverter |
| **Enterprise Attribute** | Domestic brand, listed company (603416.SH) |
| **Parent Company/Group** | None (independently listed) |
| **Data Source** | Xinje official website, product manuals, annual reports, WAIC 2026 coverage |

## Company Profile

Xinje Electric is a key player in China's small PLC and servo system market, known for high cost-performance, ease of use, and fast delivery.

The company's core products include the XD/XL series PLCs, DS series servo drives, touchscreens, and inverters, widely used in 3C, packaging, textiles, machine tools, and humanoid robot joint drives. Through its independently developed PLC platform and servo algorithms, Xinje continues to penetrate the mid-to-high-end motion control market.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|-------------------------|-------------------|
| DS Series Servo System | General-purpose servo drive + motor | DS5 / DS3 | Automation, Robotics |
| XD/XL Series PLC | Small/Medium Programmable Logic Controller | XD3 / XD5 / XL1 | Production Line Control |
| HMI/Touchscreen | Human-Machine Interface | TGA62 / TG765 | Equipment Operation Panels |

## Representative Products

### DS5 Series Servo Drive

> DS5 Series Servo Drive: Please visit [Official Documentation](https://www.xinje.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Product Form | Single-axis AC servo drive | Xinje official website |
| Power Range | 100 W – 7.5 kW | Product manual |
| Input Voltage | Single-phase/Three-phase 220 VAC / 380 VAC | Product manual |
| Control Mode | Position/Speed/Torque | Product manual |
| Communication Protocol | Modbus / CANopen / EtherCAT | Product manual |
| Speed Loop Bandwidth | 2.5 kHz (reference) | Product manual |
| Encoder Support | 17/23-bit absolute | Product manual |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: Easy commissioning, fast response, deep integration with Xinje PLC/HMI ecosystem, suitable for small-to-medium automation and robot joints.

**Application Scenarios**: Industrial robots, humanoid robots, packaging machinery, textile machinery, 3C automation.

### MS6 Series Servo Motor

> MS6 Series Servo Motor: Please visit [Official Documentation](https://www.xinje.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Product Form | AC servo motor | Xinje official website |
| Frame Size | 40–180 mm | Product manual |
| Rated Power | 50 W – 7.5 kW | Product manual |
| Rated Speed | 1000–6000 rpm | Product manual |
| Encoder | 17/23-bit absolute | Product manual |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: Low inertia design, high overload capacity, paired with DS5 series drives.

**Application Scenarios**: Automated production lines, robot joints, CNC machine tools, conveying equipment.

## Supply Chain Position

- **Upstream Key Components/Materials**: IGBT, MOSFET, PCB, capacitors, copper wire, aluminum housing, encoder chips, magnetic materials, DSP/ARM control chips.
- **Downstream Customers/Application Scenarios**: Automation equipment manufacturers, industrial robot manufacturers, humanoid robot integrators, 3C electronics, packaging and textiles.
- **Main Competitors/Benchmarks**: Inovance Technology, Delta, Mitsubishi, Omron, Leadshine.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_xinje`
- Product Entities: `ent_component_xinje_ds5`, `ent_component_xinje_ms6`
- Key Relationships:
  - `ent_company_xinje` -- `manufactures` --> `ent_component_xinje_ds5`
  - `ent_company_xinje` -- `manufactures` --> `ent_component_xinje_ms6`
  - `ent_component_xinje_ds5` -- `uses` --> `ent_component_xinje_ms6`

## References

1. [Xinje Electric Official Website](https://www.xinje.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. Xinje Electric Annual Reports and Product Manuals
