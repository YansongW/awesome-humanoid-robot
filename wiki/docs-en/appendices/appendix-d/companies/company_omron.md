# OMRON Corporation

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 欧姆龙 |
| **English Name** | OMRON Corporation |
| **Headquarters** | Kyoto, Japan |
| **Founded** | 1933 |
| **Official Website** | [https://www.omron.com](https://www.omron.com) |
| **Supply Chain Segment** | Industrial Automation, Control Equipment, Sensors, Servo Systems, Industrial Robots |
| **Enterprise Attribute** | Public Company (TYO: 6645) |
| **Parent Company/Group** | None (Independently Listed) |
| **Data Source** | OMRON Official Website, Product Manuals, Public Financial Reports |

## Company Profile

OMRON is a global industrial automation and electronic components enterprise with "Sensing & Control + Think" as its core technology.

OMRON's industrial automation business covers PLCs, motion control, machine vision, sensors, safety components, and industrial robots, with products known for high reliability and compact design. Its Sysmac platform integrates logic, motion, robotics, and vision under a single architecture, providing automation capabilities from single machines to entire production lines for industries such as 3C electronics, automotive, and food packaging. Its sensing and control technologies are also applicable to humanoid robot environmental perception and actuation units.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| Controllers / PLCs | Integrated Logic and Motion | NX / NJ Sysmac | 3C, Automotive, Packaging |
| Servo & Motion Control | High-Precision Motor Control | 1S / G5 Series Servo | Electronics, Machine Tools, Robotics |
| Vision & Sensors | Inspection, Measurement, and Identification | FH Vision System / E3AS Photoelectric | Quality Inspection, Positioning, Robot Guidance |

## Representative Products

### OMRON NJ501 Sysmac Controller

> OMRON NJ501 Sysmac Controller: Please visit [Official Documentation](https://www.omron.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Product Type | Machine Automation Controller (MAC) | Official Documentation |
| Maximum Controlled Axes | 64 axes (EtherCAT) | Official Documentation |
| Maximum I/O Points | 2,560 points | Official Documentation (varies by model) |
| Program Capacity | Not disclosed | Not disclosed |
| Communication Interfaces | EtherCAT, EtherNet/IP, USB, OPC UA | Official Documentation |
| Programming Standard | IEC 61131-3 / PLCopen Motion Control Function Blocks | Official Documentation |
| Supply Voltage | 24 VDC | Official Documentation |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: Integration of PLC and motion control, up to 64 axes of EtherCAT synchronized control, unified programming environment Sysmac Studio.

**Application Scenarios**: 3C electronics assembly, automotive parts processing, packaging machinery, robot cell control, humanoid robot joint motion control.

## Relevance to Humanoid Robots

Humanoid robots have a large number of joints and require high synchronization for motion control. Sysmac's multi-axis EtherCAT control capability and compact I/O can provide a control platform for the development and testing of small to medium-scale humanoid robot bodies.

## Supply Chain Position

- **Upstream Key Components/Materials**: MCU, sensor chips, power semiconductors, PCB, connectors, encoders
- **Downstream Customers/Application Scenarios**: 3C electronics, automotive, food & beverage, medical, semiconductor equipment
- **Main Competitors/Peers**: Mitsubishi Electric, Siemens, Schneider Electric, Keyence

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_omron`
- Product Entity: `ent_product_omron_nj501`
- Key Relationships:
  - `ent_company_omron` -- `manufactures` --> `ent_product_omron_nj501`

## References

1. [OMRON Official Website](https://www.omron.com)
2. [OMRON NJ501 Sysmac Controller Product Page](https://www.omron.com.cn/products/family/3194/)
3. OMRON FA product catalog / Sysmac Studio documentation
