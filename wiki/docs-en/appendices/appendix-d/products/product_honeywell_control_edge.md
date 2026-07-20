# Honeywell ControlEdge PLC / ControlEdge PLC

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Table of Contents](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Honeywell / Honeywell](../companies/company_honeywell.md) |
| **Product Category** | Programmable Logic Controller (PLC) |
| **Release Date** | 2016 |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [Honeywell Official Website](https://www.honeywell.com) |

## Product Overview

The ControlEdge PLC is Honeywell's next-generation PLC for process and discrete hybrid applications, supporting IEC 61131-3 programming and multiple industrial Ethernet protocols.

This product can be directly integrated into the Experion PKS distributed control system and enables IIoT data upload to the cloud via OPC UA and MQTT, making it suitable for critical infrastructure requiring high reliability and cybersecurity certification.

## Product Image

> Honeywell ControlEdge PLC: Please visit [Official Documentation](https://www.honeywell.com) for details.

## Specification Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Product Type | Programmable Logic Controller (PLC) | Official Documentation |
| Communication Protocols | Modbus/TCP, EtherNet/IP, OPC UA, MQTT | Official Documentation |
| Redundancy Support | Supported (depending on configuration) | Official Documentation |
| Programming Standard | IEC 61131-3 | Official Documentation |
| Operating Temperature | -20 °C ~ 60 °C | Official Documentation |
| Safety Certification | Not disclosed | Not disclosed |
| Supply Voltage | 24 VDC | Official Documentation |
| Price | Not disclosed | Not disclosed |

## Supply Chain Position

- **Manufacturer**: [Honeywell / Honeywell](../companies/company_honeywell.md)
- **Core Components/Technology Source**: Self-developed control firmware and Experion integration software; processors, communication chips, I/O modules, and power supplies are externally sourced.
- **Downstream Applications/Customers**: Process industry, power, water treatment, pharmaceuticals, smart manufacturing, robot testing platforms.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_honeywell_control_edge`
- Manufacturer Entity: `ent_company_honeywell`
- Key Relationships:
  - `ent_company_honeywell` → `manufactures` → `ent_product_honeywell_control_edge` (Relationship file: `rel_ent_company_honeywell_manufactures_ent_product_honeywell_control_edge.md`)

## Application Scenarios

- **Oil & Gas and Chemical**: Storage and transportation, reactor, compressor control.
- **Power and Water Treatment**: Auxiliary control systems and remote monitoring.
- **Pharmaceutical and Food**: Batch control and traceability.
- **Robot Testing**: Providing process monitoring for humanoid robot laboratories.

## Competitive Comparison

| Comparison Item | Honeywell ControlEdge PLC | Emerson PACSystems | Siemens S7-1500 |
|----------------|---------------------------|--------------------|-----------------|
| Target Market | Process/Hybrid Industry | Discrete/Process Industry | Discrete/General Purpose |
| DCS Integration | Experion PKS | DeltaV | SIMATIC PCS 7 |
| IIoT Protocols | OPC UA / MQTT | OPC UA / MQTT | OPC UA / PROFINET |
| Price | Not disclosed | Not disclosed | Not disclosed |

## Selection and Deployment Recommendations

Suitable for process plants with an existing Honeywell DCS system looking to expand discrete control, or for scenarios requiring IIoT connectivity and high environmental adaptability.

## References

1. [Honeywell Official Website](https://www.honeywell.com)
2. [Honeywell ControlEdge PLC Product Page](https://process.honeywell.com/us/en/products/control-edge-plc)
3. Honeywell Process Solutions ControlEdge PLC datasheet
