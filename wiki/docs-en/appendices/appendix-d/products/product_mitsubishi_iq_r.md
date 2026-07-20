# Mitsubishi Electric MELSEC iQ-R R04CPU / MELSEC iQ-R

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Table of Contents](../index-products.md)
> Data update date: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Mitsubishi Electric](../companies/company_mitsubishi_electric.md) |
| **Product Category** | Programmable Logic Controller (PLC) |
| **Release Date** | 2014 (Current series continuously updated) |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [Mitsubishi Electric Official Website](https://www.mitsubishielectric.com) |

## Product Overview

The MELSEC iQ-R series is Mitsubishi Electric's next-generation modular PLC, characterized by high-speed processing, large program memory, and built-in high-speed networking.

The R04CPU, as a representative CPU module of the iQ-R series, supports nanosecond-level logic operations, CC-Link IE field network, and the GX Works3 unified programming environment, making it suitable for large-scale, high-takt production line control.

## Product Image

> Mitsubishi Electric MELSEC iQ-R R04CPU: Please visit [Official Documentation](https://www.mitsubishielectric.com) for details.

## Specification Table

| Specification Item | Value | Notes/Source |
|-------------------|-------|--------------|
| Product Type | Modular PLC CPU | Official documentation |
| Program Capacity | 40 k steps | Official documentation (R04CPU) |
| Basic Instruction Processing Speed | 0.98 ns | Official documentation |
| Maximum I/O Points | 4,096 points | Official documentation |
| Communication Interfaces | CC-Link IE Field, Ethernet, RS-232 | Official documentation |
| Programming Software | GX Works3 | Official documentation |
| Supply Voltage | 100–240 VAC / 24 VDC | Official documentation |
| Price | Not disclosed | Not disclosed |

## Supply Chain Position

- **Manufacturer**: [Mitsubishi Electric](../companies/company_mitsubishi_electric.md)
- **Core Components/Technology Source**: Self-developed CPU and FA network chips; power devices, memory, connectors, and structural parts are outsourced.
- **Downstream Applications/Customers**: Automotive, semiconductor equipment, machine tools, robot integration, humanoid robot motion control platforms.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_mitsubishi_iq_r`
- Manufacturer Entity: `ent_company_mitsubishi_electric`
- Key Relationships:
  - `ent_company_mitsubishi_electric` → `manufactures` → `ent_product_mitsubishi_iq_r` (Relationship file: `rel_ent_company_mitsubishi_electric_manufactures_ent_product_mitsubishi_iq_r.md`)

## Application Scenarios

- **Automotive Production Lines**: Body and powertrain assembly control.
- **Semiconductor Equipment**: Wafer handling, exposure machine control.
- **CNC Machine Tools**: High-precision interpolation and axis control.
- **Robot Systems**: High-speed control for humanoid robot assembly and testing.

## Competitive Comparison

| Comparison Item | Mitsubishi Electric MELSEC iQ-R R04CPU | Siemens S7-1500 | OMRON NJ501 |
|-----------------|----------------------------------------|-----------------|-------------|
| Program Capacity | 40 k steps (R04CPU) | Not disclosed | Not disclosed |
| Basic Instruction Speed | 0.98 ns | Not disclosed | Not disclosed |
| Main Field Network | CC-Link IE | PROFINET | EtherCAT |
| Price | Not disclosed | Not disclosed | Not disclosed |

## Selection and Deployment Recommendations

In Japanese equipment ecosystems or production lines already using CC-Link IE networks, the iQ-R series offers seamless upgrades; selection should match I/O modules and network topology.

## References

1. [Mitsubishi Electric Official Website](https://www.mitsubishielectric.com)
2. [Mitsubishi Electric MELSEC iQ-R R04CPU Product Page](https://www.mitsubishielectric.com/fa/products/cnt/plc/r/r04cpu.html)
3. Mitsubishi Electric FA Global Website / MELSEC iQ-R Catalog
