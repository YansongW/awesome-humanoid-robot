# Emerson PACSystems RSTi-EP PLC / RSTi-EP

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Emerson Electric / Emerson Electric](../companies/company_emerson.md) |
| **Product Category** | Programmable Automation Controller (PAC) |
| **Release Date** | Active (RSTi-EP series continuously updated) |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [Emerson Electric Official Website](https://www.emerson.com) |

## Product Overview

PACSystems RSTi-EP is Emerson's PAC platform designed for compact, high-density applications, integrating a controller with scalable distributed I/O.

The platform supports PROFINET, EtherNet/IP, Modbus/TCP, and OPC UA, features cybersecurity and redundancy options, and is suitable for discrete and hybrid process applications requiring high flexibility and reliability.

## Product Image

> Emerson PACSystems RSTi-EP PLC: Please visit [Official Documentation](https://www.emerson.com) for details.

## Specification Table

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Product Type | Programmable Automation Controller (PAC) | Official documentation |
| I/O Capacity | Up to 2,048 points (depending on configuration) | Official documentation |
| Scan Speed | 1 ms / 1K Boolean instructions | Official documentation |
| Communication Interfaces | PROFINET, EtherNet/IP, Modbus/TCP, OPC UA | Official documentation |
| Programming Software | PAC Machine Edition | Official documentation |
| Redundancy Support | Supported | Official documentation |
| Operating Temperature | -20 °C ~ 60 °C | Official documentation |
| Price | Not disclosed | Not disclosed |

## Supply Chain Position

- **Manufacturer**: [Emerson Electric / Emerson Electric](../companies/company_emerson.md)
- **Core Components/Technology Source**: Self-developed PAC firmware and Machine Edition software; processors, communication modules, I/O modules, and power supplies are sourced externally.
- **Downstream Applications/Customers**: Water treatment, food and beverage, life sciences, energy, robotics testing, and integrated systems.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_emerson_pacsystems_rsti_ep`
- Manufacturer Entity: `ent_company_emerson`
- Key Relationships:
  - `ent_company_emerson` → `manufactures` → `ent_product_emerson_pacsystems_rsti_ep` (Relationship file: `rel_ent_company_emerson_manufactures_ent_product_emerson_pacsystems_rsti_ep.md`)

## Application Scenarios

- **Water Treatment**: Pump station, aeration, and filtration control.
- **Food and Beverage**: Filling, packaging, and conveyor lines.
- **Life Sciences**: Batch control and equipment integration.
- **Robotics Testing**: Provides high-speed I/O and motion coordination for humanoid robot laboratories.

## Competitive Comparison

| Comparison Item | Emerson PACSystems RSTi-EP PLC | Honeywell ControlEdge | Siemens S7-1500 |
|-----------------|-------------------------------|-----------------------|-----------------|
| Product Form | Compact PAC + Distributed I/O | Modular PLC | Modular PLC |
| Scan Speed | 1 ms / 1K Boolean | Not disclosed | Not disclosed |
| Primary Communication | PROFINET / EtherNet/IP | EtherNet/IP / Modbus | PROFINET / EtherNet/IP |
| Price | Not disclosed | Not disclosed | Not disclosed |

## Selection and Deployment Recommendations

Prioritize RSTi-EP in scenarios with dispersed I/O points and requirements for space and scan speed; confirm I/O module types and cybersecurity function licenses during selection.

## References

1. [Emerson Electric Official Website](https://www.emerson.com)
2. [Emerson PACSystems RSTi-EP PLC Product Page](https://www.emerson.com/en-us/catalog/controllers/pacsystems-rsti-ep)
3. Emerson PACSystems RSTi-EP product catalog
