# MinebeaMitsumi

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 美蓓亚三美 |
| **English Name** | MinebeaMitsumi Inc. |
| **Headquarters** | Nagano Prefecture, Japan |
| **Founded** | 1951 |
| **Website** | [https://www.minebeamitsumi.com](https://www.minebeamitsumi.com) |
| **Supply Chain Role** | Micro Motors / Bearings / Sensors |
| **Enterprise Type** | Listed Company (TYO.6479), International Brand |
| **Parent Company/Group** | MinebeaMitsumi Inc. |
| **Data Source** | Official website, annual reports, product manuals, WAIC 2026 reports |

## Company Overview

A global comprehensive manufacturer of precision micro motors and bearings, known for high precision and low noise.

MinebeaMitsumi was formed by the merger of Minebea and Mitsumi Electric, covering businesses such as miniature ball bearings, small motors, LED backlights, sensors, and semiconductor packaging. Its micro motors are widely used in hard drives, optical drives, drones, robot joints, and other fields. The integration capability of high-precision bearings and motors provides key motion components for humanoid robots.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| Micro Motors | Brushed/Brushless DC Motors, Stepper Motors | PM Series, BLDC Series | Robotics, Automotive, Consumer Electronics |
| Precision Bearings | Miniature Ball Bearings | DDL Series | Motors, Robot Joints, Drones |
| Sensors & Modules | Angle/Force Sensors, Tactile Modules | Not disclosed | Robotics, Automotive, IoT |

## Representative Products

### Micro Brushless DC Motor / MinebeaMitsumi Micro BLDC Motor

> Micro Brushless DC Motor: Please visit [Official Documentation](https://www.minebeamitsumi.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Size | Ø10–Ø40 mm (series range) | Product Manual |
| Weight | 5–120 g (depending on model) | Product Manual |
| Rated Voltage | 6–36 VDC | Product Manual |
| Rated Speed | 3,000–15,000 rpm | Product Manual |
| Rated Torque | 0.3–40 mNm | Product Manual |
| Efficiency | ≥80% | Product Manual |
| Bearing Type | Miniature Ball Bearing | Product Manual |
| Price | Not disclosed | - |

**Technical Highlights**: Built-in high-precision ball bearings, low vibration, low noise, long life, suitable for high-speed precision transmission scenarios.

**Application Scenarios**: Humanoid robot joints, drone gimbals, hard disk drives, medical equipment, precision instruments.

### Miniature Ball Bearing / MinebeaMitsumi Miniature Ball Bearing

> Miniature Ball Bearing: Please visit [Official Documentation](https://www.minebeamitsumi.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Inner Diameter | 1–50 mm (series range) | Product Manual |
| Outer Diameter | 3–80 mm | Product Manual |
| Precision Grade | ABEC-1 to ABEC-7 | Product Manual |
| Material | Bearing Steel / Stainless Steel (optional) | Product Manual |
| Lubrication Method | Grease / Oil Lubrication | Product Manual |
| Rated Load | Depends on model | Product Manual |
| Seal Type | Open / Dust Cover / Rubber Seal | Product Manual |
| Price | Not disclosed | - |

**Technical Highlights**: Leading global market share in miniature bearings, high dimensional accuracy, low friction, key supporting components for robot joints and motors.

**Application Scenarios**: Motor rotor support, robot joint reducers, precision shaft systems, drone rotors.

## Supply Chain Position

- **Upstream Key Components/Materials**: Special steel, lubricating grease, magnetic materials, copper wire, resin materials
- **Downstream Customers/Application Scenarios**: Motor manufacturers, robot OEMs, automotive electronics, consumer electronics, aerospace
- **Main Competitors/Benchmarks**: NSK, NTN, Nidec, Faulhaber, HCH Bearing

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_minebea`
- Product/Component Entities: `ent_component_minebea_micro_bldc`, `ent_component_minebea_ball_bearing`
- Key Relationships:
  - `ent_company_minebea` -- `manufactures` --> `ent_component_minebea_micro_bldc`
  - `ent_company_minebea` -- `manufactures` --> `ent_component_minebea_ball_bearing`

## References

1. [Official Website](https://www.minebeamitsumi.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.minebeamitsumi.com/products/) (Please verify against actual product models)
