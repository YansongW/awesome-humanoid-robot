# MOONS' Electric

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 鸣志电器 |
| **English Name** | MOONS' Electric |
| **Headquarters** | Shanghai, China |
| **Founded** | 1994 |
| **Website** | [https://www.moons.com.cn](https://www.moons.com.cn) |
| **Supply Chain Role** | Motors / Drives / Motion Control |
| **Company Type** | Listed Company (SH.603728), Domestic Brand |
| **Parent Company/Group** | MOONS' Electric Co., Ltd. |
| **Data Source** | Official website, annual reports, product manuals, WAIC 2026 reports |

## Company Overview

A leading domestic supplier of control motors and drive systems, with a top global market share in stepper motors.

MOONS' Electric focuses on control motors and drive systems, with products covering stepper motors, brushless motors, servo motors, precision reducers, and motion controllers. The company has mass production capabilities in high-end categories such as coreless motors and slotless brushless motors, providing core motion components for robotics, medical, and semiconductor equipment. Its humanoid robot-related layout focuses on miniaturized, high-response motors and integrated joint modules.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Stepper Motors | Precision open-loop/closed-loop stepping | 57/86 series, NEMA series | 3C, semiconductor, medical equipment |
| Brushless Motors | High-speed slotless/coreless motors | ECU, DCU series | Robot joints, drones, medical |
| Servo Systems | Low-voltage servo and drive | M2AC, M3AC series | AGV, collaborative robots |

## Representative Products

### Coreless Brushless DC Motor / MOONS' Coreless Brushless DC Motor

> Coreless Brushless DC Motor: Please visit [Official Information](https://www.moons.com.cn) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Size | Ø16–Ø40 mm (series range) | Product manual |
| Weight | 20–150 g (depending on model) | Product manual |
| Rated Voltage | 12–48 VDC | Product manual |
| Rated Speed | 5,000–15,000 rpm | Product manual |
| Rated Torque | 3–50 mNm | Product manual |
| Efficiency | ≥85% | Product manual |
| Communication Interface | Hall / Encoder optional | Product manual |
| Price | Not disclosed | - |

**Technical Highlights**: Slotless coreless winding, low inertia, high dynamic response, suitable for driving in confined spaces such as robot fingers and dexterous hands.

**Application Scenarios**: Humanoid robot dexterous hands, medical handheld instruments, precision optical focusing, drone gimbals.

### Stepper Drive / MOONS' Stepper Drive

> Stepper Drive: Please visit [Official Information](https://www.moons.com.cn) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Size | Not disclosed | Product manual |
| Weight | Not disclosed | Product manual |
| Rated Current | 0.5–10 A | Product manual |
| Supply Voltage | 12–80 VDC | Product manual |
| Control Method | Pulse / CANopen / Modbus | Product manual |
| Microstepping Mode | Up to 256 microsteps | Product manual |
| Protection Features | Overcurrent, overvoltage, overtemperature | Product manual |
| Price | Not disclosed | - |

**Technical Highlights**: Closed-loop stepper control, vibration suppression, support for multiple bus protocols, suitable for precision positioning and low-cost automation.

**Application Scenarios**: 3C equipment, semiconductor packaging, medical instruments, small robot joints.

## Supply Chain Position

- **Upstream Key Components/Materials**: Rare earth permanent magnets, silicon steel sheets, copper wire, bearings, driver ICs, power devices
- **Downstream Customers/Application Scenarios**: Industrial robots, humanoid robots, medical equipment, semiconductor equipment, 3C automation manufacturers
- **Main Competitors/Benchmarks**: Maxon, Faulhaber, Inovance Technology, Step Electric, Hechuan Technology

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_moons`
- Product/Component Entities: `ent_component_moons_brushless_motor`, `ent_component_moons_stepper_drive`
- Key Relationships:
  - `ent_company_moons` -- `manufactures` --> `ent_component_moons_brushless_motor`
  - `ent_company_moons` -- `manufactures` --> `ent_component_moons_stepper_drive`

## References

1. [Official Website](https://www.moons.com.cn)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.inovance.com) (Please verify against actual product models)
