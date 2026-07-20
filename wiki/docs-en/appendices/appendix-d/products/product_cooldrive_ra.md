# CoolDrive RA Series Servo Drives

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [CoolDrive](../companies/company_cooldrive.md) |
| **Product Category** | Servo Drive / Humanoid Robot Core Component |
| **Release Date** | Continuous iteration since 2015 |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [https://www.cooldrive.com.cn](https://www.cooldrive.com.cn) |

## Product Overview

The CoolDrive RA series is a high-end servo drive launched by CoolDrive, targeting joint drives for industrial robots, collaborative robots, and humanoid robots.

The product supports industrial buses such as EtherCAT and CANopen, is compatible with various high-precision encoder protocols, features highly integrated multi-axis drive capability and functional safety design, and serves as an important domestic alternative for core components of humanoid robots in China.

## Product Image

> CoolDrive RA: Please visit [official materials](https://www.cooldrive.com.cn) for details.

## Specification Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Product Form | Single-axis / Multi-axis servo drive | CoolDrive official website |
| Power Range | 100 W – 15 kW (depending on model) | Product manual |
| Input Voltage | Three-phase 220 VAC / 380 VAC (depending on model) | Product manual |
| Control Mode | Position / Speed / Torque | Product manual |
| Communication Protocol | EtherCAT / CANopen | Product manual |
| Speed Loop Bandwidth | Not disclosed | - |
| Current Loop Frequency | Not disclosed | - |
| Encoder Support | 17/23-bit absolute, BiSS-C, EnDat 2.2 | Product manual |
| Safety Functions | STO / SS1, etc. | Product manual |
| Price | Not disclosed | Inquire for pricing |

## Supply Chain Position

- **Manufacturer**: [CoolDrive](../companies/company_cooldrive.md)
- **Core Components/Technology Sources**: IGBT, MOSFET, PCB, capacitors, current sensors, encoder interface chips, DSP/ARM control chips, heat sinks.
- **Downstream Applications/Customers**: Industrial robot manufacturers, humanoid robot integrators, collaborative robot manufacturers, CNC machine tools, semiconductor equipment, laser equipment.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_component_cooldrive_ra`
- Manufacturer Entity: `ent_company_cooldrive`
- Key Relationships:
  - `rel_ent_company_cooldrive_manufactures_ent_component_cooldrive_ra` (`ent_company_cooldrive` → `manufactures` → `ent_component_cooldrive_ra`)

## Application Scenarios

- **Industrial Robots**: Joint drives for six-axis, SCARA, and collaborative robots.
- **Humanoid Robots**: High dynamic response and force control drives for full-body joints.
- **CNC Machine Tools**: High-precision spindle and feed axis drives.
- **Semiconductor Equipment**: Precision motion platform drives.

## Competitive Comparison

| Comparison Item | CoolDrive RA | Main Competitors |
|----------------|--------------|------------------|
| Positioning | High-end servo drive / multi-axis drive | Inovance SV680, Leadshine L8, Yaskawa Σ series |
| Core Advantage | Multi-axis integration, high encoder compatibility, functional safety | Depends on specific model |
| Price | Not disclosed | Not disclosed |

## Selection and Deployment Recommendations

- Select the corresponding model based on power, number of axes, encoder type, and bus protocol.
- For humanoid robot applications, evaluate heat dissipation, synchronization performance, and fail-safe mechanisms of multi-axis drives.
- It is recommended to obtain the latest firmware, debugging software, and certification information through official CoolDrive channels.

## Related Entries

- [Manufacturer: CoolDrive](../companies/company_cooldrive.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [CoolDrive Official Website](https://www.cooldrive.com.cn)
2. CoolDrive RA Series Product Manual
3. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
