# Inovance SV660 Servo Drive

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Table of Contents](../index-products.md)
> Data update date: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed".

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Inovance](../companies/company_inovance.md) |
| **Product Category** | Servo Drive |
| **Release Date** | SV660 series is the current mainstream model |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [Inovance Official Website](https://www.inovance.com) |

## Product Overview

The Inovance SV660 series is a high-performance, medium-to-low power AC servo drive launched by Inovance Technology. The power range covers 0.05 kW to 7.5 kW, supporting multiple control interfaces such as Pulse and EtherCAT (SV660N). It is widely used in automation equipment including semiconductor equipment, pick-and-place machines, PCB processing, handling machinery, machine tools, and conveying machinery.

The SV660 series features built-in rigidity table settings, online inertia identification, auto-tuning, and vibration suppression functions. Paired with the MS1 series 23-bit single-turn/multi-turn absolute encoder servo motor, it enables fast and precise position, speed, and torque control. Its compact size and split encoder design help reduce motor dimensions and weight, making it suitable for moving mechanisms and space-constrained installations.

## Product Image

> Inovance SV660: Please visit the [official website](https://www.inovance.com) for details.

## Specification Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Power Range | 0.05 kW – 7.5 kW | Official Manual |
| Control Interface | Pulse (SV660P) / EtherCAT (SV660N) | Official Manual |
| Encoder Support | 23-bit single-turn/multi-turn absolute encoder | Official Manual |
| Control Mode | Position / Speed / Torque / Hybrid Mode | Official Manual |
| Communication Protocol | EtherCAT / CANopen / Modbus | Official Manual |
| Protection Rating | IP20 (Typical) | Official Manual |
| Supply Voltage | Single-phase/Three-phase 220 VAC or 380 VAC (depending on model) | Official Manual |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Inovance](../companies/company_inovance.md)
- **Core Components/Technology Source**: Self-developed power modules, control boards, and servo algorithms; IGBT/SiC power devices, capacitors, and encoder chips are externally sourced.
- **Downstream Applications/Customers**: Industrial robots, humanoid robot joints, semiconductor equipment, 3C electronics, machine tools, logistics automation.

## Knowledge Graph Nodes and Relationships

- Component Entity: `ent_component_inovance_sv660`
- Manufacturer Entity: `ent_company_inovance`
- Key Relationships:
  - `rel_ent_company_inovance_manufactures_ent_component_inovance_sv660` (`ent_company_inovance` → `manufactures` → `ent_component_inovance_sv660`)

## Application Scenarios

- **Industrial Robots**: Servo drive for joints of six-axis robots, SCARA, and Delta robots.
- **Humanoid Robots**: Position, speed, and torque control for leg and arm joint motors.
- **CNC Machine Tools**: High-precision positioning and contour control for feed axes and spindles.
- **Electronics Manufacturing**: Precision motion control for pick-and-place machines, PCB drilling machines, and handling machinery.

## Competitive Comparison

| Comparison Item | Inovance SV660 | Yaskawa Σ-7 | Panasonic A6 |
|----------------|----------------|-------------|--------------|
| Power Range | 0.05–7.5 kW | 0.03–55 kW | 0.05–5 kW |
| Communication Interface | EtherCAT / Pulse | EtherCAT / MECHATROLINK | EtherCAT / Pulse |
| Encoder | 23-bit absolute | 24-bit absolute | 23-bit absolute |
| Core Advantage | Localized service, cost-effectiveness, quick commissioning | High-end precision and reliability | High-speed response |

## Selection and Deployment Recommendations

- When selecting a model, choose the SV660P (Pulse) or SV660N (EtherCAT) based on load inertia, rigidity requirements, and bus protocol.
- For commissioning, it is recommended to first perform online inertia identification and vibration suppression, then integrate into the complete machine for trajectory optimization.

## References

1. [Inovance Official Website](https://www.inovance.com)
2. [Inovance SV660N Series Servo Manual](https://idea-tech.in/wp-content/uploads/2020/04/INOVANCE-SV660-SERVO-ETHERCAT-MANUAL-CHINESE-20-4-20.pdf)
3. [CSDN – Inovance SV660N Commissioning Manual](https://blog.csdn.net/crown6465/article/details/145727125)
4. [Originality Document – Inovance SV660N Series Servo Commissioning Manual](https://max.book118.com/html/2024/0807/8125023046006117.shtm)
