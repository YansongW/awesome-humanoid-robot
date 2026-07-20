# Panasonic Holdings Corporation / Panasonic Industry Co., Ltd.

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Panasonic Holdings / Panasonic Industry |
| **English Name** | Panasonic Holdings Corporation / Panasonic Industry Co., Ltd. |
| **Headquarters** | Osaka, Japan |
| **Founded** | 1918 |
| **Website** | [https://www.panasonic.com](https://www.panasonic.com) |
| **Supply Chain Segment** | Industrial automation, servo motors, PLCs, sensors, electronic components |
| **Enterprise Type** | Public company (TYO: 6752, holding company); industrial automation business operated by Panasonic Industry |
| **Parent Company/Group** | Panasonic Holdings Corporation |
| **Data Source** | Panasonic official website, Panasonic Industry product catalogs, public financial reports |

## Company Profile

Panasonic is a globally renowned manufacturer of electronics and industrial automation products. Its industrial automation business is operated by Panasonic Industry.

Panasonic Industry provides core industrial automation components such as the MINAS series servo systems, FP series PLCs, sensors, connectors, batteries, and motors. The MINAS A6 series is known for its 2.0 kHz speed response, 23-bit absolute encoder, and compact design, and is widely used in electronics manufacturing, semiconductors, robotics, and precision platforms. Panasonic also supplies key components such as cylindrical batteries and brushless motors for robots.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Servo Systems | High-speed response servo motors/drives | MINAS A6 Series | Electronics, semiconductors, robotics |
| PLCs / Controllers | Compact programmable controllers | FP-XH / FP0H / FP7 | 3C, packaging, equipment |
| Components & Batteries | Sensors, connectors, batteries | PM relays / 18650 cylindrical batteries | Automotive, robotics, energy |

## Representative Products

### Panasonic MINAS A6 Servo System

> Panasonic MINAS A6 Servo System: Please refer to [official documentation](https://www.panasonic.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Product Type | AC servo motor + driver | Official documentation |
| Power Range | 50 W ~ 5 kW | Official documentation (varies by model) |
| Speed Response | 2.0 kHz | Official documentation |
| Encoder | 23-bit absolute encoder | Official documentation |
| Communication Interface | EtherCAT / RTEX / Modbus (varies by model) | Official documentation |
| Control Mode | Position / Speed / Torque / Full closed loop | Official documentation |
| Protection Rating | IP67 (motor, varies by model) / IP20 (driver) | Official documentation |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: 2.0 kHz high-speed response, 23-bit high-precision absolute encoder, compact and lightweight design, rich bus options.

**Application Scenarios**: 3C electronics SMT, semiconductor equipment, CNC machine tools, industrial manipulators, humanoid robot arms and finger joints.

## Relevance to Humanoid Robots

Small-space joints such as humanoid robot fingers and wrists require small, high-speed response servos. The compact motor and high-precision encoder of the MINAS A6 provide a foundation for fine force control in the end joints of humanoid robots.

## Supply Chain Position

- **Upstream Key Components/Materials**: Rare earth magnets, silicon steel sheets, encoder chips, power semiconductors, PCBs, housings
- **Downstream Customers/Application Scenarios**: 3C electronics, semiconductors, automotive, robotics, medical equipment
- **Main Competitors/Peers**: Yaskawa, Mitsubishi Electric, Inovance, Kollmorgen

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_panasonic`
- Product Entity: `ent_product_panasonic_minas_a6`
- Key Relationship:
  - `ent_company_panasonic` -- `manufactures` --> `ent_product_panasonic_minas_a6`

## References

1. [Panasonic Holdings / Panasonic Industry Official Website](https://www.panasonic.com)
2. [Panasonic MINAS A6 Servo System Product Page](https://industry.panasonic.com/global/en/motor/servo_motor/a6)
3. Panasonic Industry MINAS A6 servo catalog
