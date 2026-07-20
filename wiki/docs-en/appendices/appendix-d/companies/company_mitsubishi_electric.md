# Mitsubishi Electric Corporation

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Mitsubishi Electric |
| **English Name** | Mitsubishi Electric Corporation |
| **Headquarters** | Tokyo, Japan |
| **Founded** | 1921 |
| **Official Website** | [https://www.mitsubishielectric.com](https://www.mitsubishielectric.com) |
| **Supply Chain Segment** | Factory Automation (FA), PLC, Servo Systems, CNC, Industrial Robots |
| **Enterprise Attribute** | Public Company (TYO: 6503) |
| **Parent Company/Group** | Mitsubishi Group (No single controlling parent; independently listed) |
| **Data Source** | Mitsubishi Electric official website, FA product catalogs, public financial reports |

## Company Overview

Mitsubishi Electric is a globally leading comprehensive manufacturer of factory automation (FA) and electromechanical products.

Mitsubishi Electric's FA business covers MELSEC programmable controllers, MELSERVO servos, CNC systems, industrial robots (MELFA), and visualization software. Its iQ platform is renowned for high speed, high reliability, and network integration, with a strong foundation in automotive, semiconductor, machine tool, and elevator industries. Mitsubishi Electric's servo and motion control technology can provide core components for humanoid robot joint actuation and precision positioning.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| PLC / Controller | High-speed modular controller | MELSEC iQ-R / iQ-F | Automotive, Semiconductor, Machine Tools |
| Servo System | High-precision motion control | MELSERVO-J5 / J4 | Electronics, Robotics, Packaging |
| Industrial Robot | Vertical articulated / SCARA | MELFA RV / RH / F Series | Assembly, Handling, Welding |

## Representative Products

### Mitsubishi Electric MELSEC iQ-R R04CPU

> Mitsubishi Electric MELSEC iQ-R R04CPU: Please visit [Official Documentation](https://www.mitsubishielectric.com) for details.

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Product Type | Modular PLC CPU | Official Documentation |
| Program Capacity | 40 k steps | Official Documentation (R04CPU) |
| Basic Instruction Processing Speed | 0.98 ns | Official Documentation |
| Maximum I/O Points | 4,096 points | Official Documentation |
| Communication Interfaces | CC-Link IE Field, Ethernet, RS-232 | Official Documentation |
| Programming Software | GX Works3 | Official Documentation |
| Supply Voltage | 100–240 VAC / 24 VDC | Official Documentation |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: Nanosecond-level instruction processing, built-in CC-Link IE Field network, unified engineering software GX Works3, modular high scalability.

**Application Scenarios**: Automotive production line control, semiconductor equipment, CNC machine tools, elevator control, humanoid robot assembly and testing equipment.

## Relevance to Humanoid Robots

Humanoid robot joint servos demand stringent high-speed response and positioning accuracy. Mitsubishi Electric's MELSERVO and iQ-R controllers can provide a highly reliable platform for joint module development and overall robot motion control.

## Supply Chain Position

- **Upstream Key Components/Materials**: Semiconductors, power modules, encoders, magnetic materials, structural parts, PCBs
- **Downstream Customers/Application Scenarios**: Automotive manufacturing, semiconductor equipment, machine tools, elevators, energy infrastructure
- **Main Competitors/Benchmarks**: Siemens, OMRON, Schneider Electric, Fanuc

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_mitsubishi_electric`
- Product Entity: `ent_product_mitsubishi_iq_r`
- Key Relationship:
  - `ent_company_mitsubishi_electric` -- `manufactures` --> `ent_product_mitsubishi_iq_r`

## References

1. [Mitsubishi Electric Official Website](https://www.mitsubishielectric.com)
2. [Mitsubishi Electric MELSEC iQ-R R04CPU Product Page](https://www.mitsubishielectric.com/fa/products/cnt/plc/r/r04cpu.html)
3. Mitsubishi Electric FA Global Website / MELSEC iQ-R Catalog
