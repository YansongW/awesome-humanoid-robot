# Xinje DS5 Series Servo Drive

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Table of Contents](../index-products.md)
> Data update date: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Xinje Electric](../companies/company_xinje.md) |
| **Product Category** | Servo Drive / Motion Control Core Component |
| **Release Date** | Continuously iterated since the 2010s |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [https://www.xinje.com](https://www.xinje.com) |

## Product Overview

The Xinje DS5 series is an AC servo drive designed for small to medium-sized automation equipment and robot applications, with a power range covering 100 W to 7.5 kW.

The product supports multiple control interfaces such as Pulse, Modbus, CANopen, and EtherCAT. It features auto-tuning, inertia identification, and vibration suppression functions. Together with the Xinje XD/XL series PLCs and MS6 series servo motors, it forms a complete automation solution widely used in 3C, packaging, textile, machine tools, and humanoid robot joint drives.

## Product Image

> Xinje DS5: Please visit the [official website](https://www.xinje.com) for details.

## Specification Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Product Form | Single-axis AC servo drive | Xinje official website |
| Power Range | 100 W – 7.5 kW | Product manual |
| Input Voltage | Single-phase/Three-phase 220 VAC / 380 VAC | Product manual |
| Control Mode | Position / Speed / Torque | Product manual |
| Communication Protocol | Pulse / Modbus / CANopen / EtherCAT | Product manual |
| Speed Loop Bandwidth | 2.5 kHz (reference) | Product manual |
| Encoder Support | 17/23-bit absolute | Product manual |
| Safety Function | STO (on select models) | Product manual |
| Protection Rating | IP20 (typical) | Product manual |
| Price | Not disclosed | Requires inquiry |

## Supply Chain Position

- **Manufacturer**: [Xinje Electric](../companies/company_xinje.md)
- **Core Components/Technology Source**: Self-developed power modules, control boards, and servo algorithms; IGBT/MOS power devices, capacitors, and encoder chips are externally sourced.
- **Downstream Applications/Customers**: Automation equipment manufacturers, industrial robot manufacturers, humanoid robot integrators, 3C electronics, packaging and textile industries.

## Knowledge Graph Nodes and Relationships

- Component entity: `ent_component_xinje_ds5`
- Manufacturer entity: `ent_company_xinje`
- Key relationships:
  - `rel_ent_company_xinje_manufactures_ent_component_xinje_ds5` (`ent_company_xinje` → `manufactures` → `ent_component_xinje_ds5`)
  - `ent_component_xinje_ds5` -- `uses` --> `ent_component_xinje_ms6`

## Application Scenarios

- **Industrial Robots**: Servo drive for joints of six-axis robots, SCARA, and Delta robots.
- **Humanoid Robots**: Position, speed, and torque control for arm and leg joints.
- **Packaging Machinery**: Motion control for flying shears, chasing shears, and fixed-length conveying.
- **Textile Machinery**: High-precision transmission for flat knitting machines, circular knitting machines, and weaving machines.

## Competitive Comparison

| Comparison Item | Xinje DS5 | Inovance SV660 | INVT DA200 |
|----------------|-----------|----------------|------------|
| Power Range | 100 W – 7.5 kW | 50 W – 7.5 kW | 100 W – 7.5 kW |
| Communication Interface | EtherCAT / CANopen / Pulse | EtherCAT / Pulse | EtherCAT / CANopen / Pulse |
| Encoder | Up to 23-bit absolute | 23-bit absolute | Up to 23-bit absolute |
| Core Advantage | PLC ecosystem integration, high cost-performance | Localized service, fast response | Rich industry solutions |

## Selection and Deployment Recommendations

- It is recommended to use with Xinje PLC/HMI to leverage ecosystem integration advantages.
- Select the appropriate sub-model based on load inertia, rigidity requirements, and bus protocol.
- Obtain the latest firmware and debugging software through official Xinje channels.

## Related Entries

- [Manufacturer: Xinje Electric](../companies/company_xinje.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [Xinje official website](https://www.xinje.com)
2. Xinje DS5 series product manual
3. [WAIC 2026 exhibition report](https://www.worldrobotconference.com)
