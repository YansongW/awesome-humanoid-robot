# CoolDrive

> This entry belongs to [Appendix D: Enterprise/Product Wiki](../../appendix-d.md).  
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 清能德创电气技术（北京）有限公司 |
| **English Name** | CoolDrive |
| **Headquarters** | Beijing, China |
| **Founded** | 2012 |
| **Official Website** | [https://www.cooldrive.com.cn](https://www.cooldrive.com.cn) |
| **Supply Chain Role** | Servo Drive / Motion Control / Core Components for Humanoid Robots |
| **Enterprise Attribute** | Domestic Brand, Representative of High-End Servo Drives |
| **Parent Company/Group** | None |
| **Data Source** | CoolDrive official website, product manuals, WAIC 2026 reports, public press releases |

## Company Profile

CoolDrive is a representative enterprise in the domestic high-end servo drive field, focusing on high-performance servo drive and motion control solutions.

The company's products are widely used in industrial robots, CNC machine tools, laser processing, semiconductor equipment, and humanoid robots. The CoolDrive RA series servo drives are known for their high response, high precision, and multi-axis coordination capabilities, serving as a core component supplier for many domestic humanoid robot integrators and collaborative robot manufacturers.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| High-End Servo Drives | Industrial/Robot Joint Drives | CoolDrive RA / R / S Series | Industrial Robots, Humanoid Robots |
| Multi-Axis Drives | Integrated Joint Drives | CoolDrive RA Multi-Axis | Collaborative Robots, SCARA |
| Motion Control | Controllers & Custom Solutions | CoolDrive MC | High-End Equipment |

## Representative Products

### CoolDrive RA Series Servo Drives

> CoolDrive RA: Please visit [Official Materials](https://www.cooldrive.com.cn) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Product Form | Single-Axis / Multi-Axis Servo Drive | CoolDrive Official Website |
| Power Range | 100 W – 15 kW (depending on model) | Product Manual |
| Control Mode | Position / Speed / Torque | Product Manual |
| Communication Protocol | EtherCAT / CANopen | Product Manual |
| Speed Loop Bandwidth | Not disclosed | - |
| Encoder Support | 17/23-bit Absolute, BiSS-C, EnDat 2.2 | Product Manual |
| Safety Functions | STO / SS1, etc. | Product Manual |
| Price | Not disclosed | Inquiry required |

**Technical Highlights**: Highly integrated multi-axis drive, support for multiple high-precision encoder protocols, high dynamic response adapted to robot joints, representative of domestic high-end servo drives.

**Application Scenarios**: Industrial robots, collaborative robots, humanoid robot joints, CNC machine tools, semiconductor equipment, laser processing.

### CoolDrive R Series Servo Drives

> CoolDrive R: Please visit [Official Materials](https://www.cooldrive.com.cn) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Product Form | General-Purpose Servo Drive | CoolDrive Official Website |
| Power Range | Not disclosed | - |
| Control Mode | Position / Speed / Torque | Product Manual |
| Communication Protocol | EtherCAT / Modbus | Product Manual |
| Encoder Support | Incremental / Absolute | Product Manual |
| Price | Not disclosed | Inquiry required |

**Technical Highlights**: Stable and reliable, high cost-performance, designed for batch applications in general automation and robotics.

**Application Scenarios**: General automation equipment, industrial robots, logistics equipment, textile machinery.

## Supply Chain Position

- **Upstream Key Components/Materials**: IGBT, MOSFET, PCB, capacitors, current sensors, encoder chips, DSP/ARM control chips, heat sinks.
- **Downstream Customers/Application Scenarios**: Industrial robot manufacturers, humanoid robot integrators, collaborative robot manufacturers, CNC machine tools, semiconductor equipment, laser equipment.
- **Main Competitors/Peers**: Inovance Technology, Leadshine, Hechuan Technology, Yaskawa, Mitsubishi, Panasonic.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_cooldrive`
- Product/Component Entities: `ent_component_cooldrive_ra`, `ent_component_cooldrive_r`
- Key Relationships:
  - `ent_company_cooldrive` -- `manufactures` --> `ent_component_cooldrive_ra`
  - `ent_company_cooldrive` -- `manufactures` --> `ent_component_cooldrive_r`

## References

1. [CoolDrive Official Website](https://www.cooldrive.com.cn)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. CoolDrive Product Manuals and Public Press Releases
