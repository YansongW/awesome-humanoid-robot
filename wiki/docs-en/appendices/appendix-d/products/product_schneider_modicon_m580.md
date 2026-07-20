# Schneider Electric Modicon M580 ePAC / Modicon M580

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Table of Contents](../index-products.md)
> Data update date: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Schneider Electric](../companies/company_schneider_electric.md) |
| **Product Category** | Programmable Automation Controller (ePAC) |
| **Release Date** | 2012 (Active series continuously updated) |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [Schneider Electric Official Website](https://www.se.com) |

## Product Overview

The Modicon M580 is an ePAC launched by Schneider Electric based on a native Ethernet architecture, combining the flexibility of a PLC with the process control capabilities of a DCS, emphasizing built-in cybersecurity and open connectivity.

This series supports protocols such as Modbus TCP, EtherNet/IP, and OPC UA, enabling seamless integration with drives, servos, HMIs, and upper-layer MES/SCADA systems. It is suitable for smart manufacturing scenarios requiring high availability and IIoT connectivity.

## Product Image

> Schneider Electric Modicon M580 ePAC: Please visit [Official Documentation](https://www.se.com) for details.

## Specification Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Product Type | ePAC (Ethernet Programmable Automation Controller) | Official documentation |
| Program/Data Memory | Up to 64 MB | Official documentation (depends on CPU model) |
| Maximum I/O Capacity | Not disclosed | Not disclosed |
| Communication Interfaces | EtherNet/IP, Modbus TCP, OPC UA | Official documentation |
| Security Certification | Achilles Level 2 | Official documentation |
| Supply Voltage | 24 VDC | Official documentation |
| Operating Temperature | 0 °C ~ 60 °C | Official documentation |
| Price | Not disclosed | Not disclosed |

## Supply Chain Position

- **Manufacturer**: [Schneider Electric](../companies/company_schneider_electric.md)
- **Core Components/Technology Source**: Self-developed control firmware and software; processors, Ethernet chips, power devices, and memory chips are externally sourced.
- **Downstream Applications/Customers**: Process industry, energy and water treatment, food and beverage, humanoid robot production line control hubs.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_schneider_modicon_m580`
- Manufacturer Entity: `ent_company_schneider_electric`
- Key Relationships:
  - `ent_company_schneider_electric` → `manufactures` → `ent_product_schneider_modicon_m580` (Relationship file: `rel_ent_company_schneider_electric_manufactures_ent_product_schneider_modicon_m580.md`)

## Application Scenarios

- **Process Control**: Continuous processes such as oil and gas, chemical, and water treatment.
- **Discrete Manufacturing**: Automotive, electronics, and food and beverage production lines.
- **Robotics Cells**: Provides control hubs for humanoid robot assembly and testing.
- **Energy Management**: Production line energy efficiency monitoring and optimization.

## Competitive Comparison

| Comparison Item | Schneider Electric Modicon M580 ePAC | Siemens S7-1500 | Rockwell ControlLogix |
|----------------|--------------------------------------|-----------------|-----------------------|
| Product Type | ePAC | PLC | PLC |
| Native Ethernet | Yes | Yes | Yes |
| Typical Security Certification | Achilles Level 2 | Not disclosed | Not disclosed |
| Price | Not disclosed | Not disclosed | Not disclosed |

## Selection and Deployment Recommendations

Prioritize the M580 in scenarios requiring the integration of process and discrete control, as well as compliance with cybersecurity requirements. When selecting a model, confirm I/O points, communication protocols, and redundancy needs.

## References

1. [Schneider Electric Official Website](https://www.se.com)
2. [Schneider Electric Modicon M580 ePAC Product Page](https://www.se.com/us/en/product-range/1469-modicon-m580/)
3. Schneider Electric Annual Report / EcoStruxure platform pages
