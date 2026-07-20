# INVT DA200 Series Servo Drive / INVT DA200 Servo Drive

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [INVT Electric](../companies/company_invt.md) |
| **Product Category** | Servo Drive / Motion Control Core Component |
| **Release Date** | Continuous iteration since the 2010s |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [https://www.invt.com.cn](https://www.invt.com.cn) |

## Product Overview

The INVT DA200 series is an AC servo drive designed for general automation and robotics applications, with a power range covering 100 W to 7.5 kW.

The product supports multiple control interfaces such as Pulse, Modbus, CANopen, and EtherCAT. It features built-in inertia identification, auto-tuning, and vibration suppression functions. Paired with INVT servo motors, it meets the demand for cost-effective servo drives in industrial robots, humanoid robot joints, and automation equipment.

## Product Image

> INVT DA200: Please visit the [official website](https://www.invt.com.cn) for details.

## Specification Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Product Form | Single-axis AC servo drive | INVT official website |
| Power Range | 100 W – 7.5 kW | Product manual |
| Input Voltage | Single-phase/Three-phase 220 VAC / 380 VAC | Product manual |
| Control Mode | Position / Speed / Torque | Product manual |
| Communication Protocol | Pulse / Modbus / CANopen / EtherCAT | Product manual |
| Speed Loop Bandwidth | 2.5 kHz (reference) | Product manual |
| Encoder Support | 17/23-bit absolute, incremental | Product manual |
| Safety Function | STO (on select models) | Product manual |
| Protection Rating | IP20 (typical) | Product manual |
| Price | Not disclosed | Subject to inquiry |

## Supply Chain Position

- **Manufacturer**: [INVT Electric](../companies/company_invt.md)
- **Core Components/Technology Source**: Self-developed power modules, control boards, and servo algorithms; IGBT/MOS power devices, capacitors, and encoder chips are externally sourced.
- **Downstream Applications/Customers**: Industrial robots, humanoid robot joints, CNC machine tools, electronics manufacturing, packaging machinery.

## Knowledge Graph Nodes and Relationships

- Component Entity: `ent_component_invt_da200`
- Manufacturer Entity: `ent_company_invt`
- Key Relationships:
  - `rel_ent_company_invt_manufactures_ent_component_invt_da200` (`ent_company_invt` → `manufactures` → `ent_component_invt_da200`)

## Application Scenarios

- **Industrial Robots**: Servo drive for joints of six-axis robots, SCARA, and Delta robots.
- **Humanoid Robots**: Position, speed, and torque control for leg and arm joint motors.
- **CNC Machine Tools**: High-precision positioning and contour control for feed axes and spindles.
- **Packaging Machinery**: Motion control for flying shear, rotary shear, and fixed-length cutting.

## Competitive Comparison

| Comparison Item | INVT DA200 | Inovance SV660 | Delta ASDA-B3 |
|----------------|------------|----------------|---------------|
| Power Range | 100 W – 7.5 kW | 50 W – 7.5 kW | 100 W – 15 kW |
| Communication Interface | EtherCAT / CANopen / Pulse | EtherCAT / Pulse | EtherCAT / DMCNET / CANopen |
| Encoder | Up to 23-bit absolute | 23-bit absolute | Up to 23-bit absolute |
| Core Advantage | High cost-performance, rich industry solutions | Localized service, fast response | Multi-bus, wide power range |

## Selection and Deployment Recommendations

- Select the appropriate DA200 sub-model based on load inertia, rigidity requirements, and bus protocol.
- During commissioning, it is recommended to first perform online inertia identification and vibration suppression before integrating into the complete machine for trajectory optimization.
- It is advised to obtain the latest firmware and debugging software through INVT's official channels.

## Related Entries

- [Manufacturer: INVT Electric](../companies/company_invt.md)
- [Appendix D.4 Key Product Wiki](../index-products.md)

## References

1. [INVT Official Website](https://www.invt.com.cn)
2. INVT DA200 Series Product Manual
3. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
