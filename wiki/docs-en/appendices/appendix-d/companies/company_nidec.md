# Nidec Corporation

> This entry belongs to [Appendix D: Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 日本电产 |
| **English Name** | Nidec Corporation |
| **Headquarters** | Kyoto, Japan |
| **Founded** | 1973 |
| **Website** | [https://www.nidec.com](https://www.nidec.com) |
| **Supply Chain Role** | Motors / Reducers / Drive Modules |
| **Company Type** | Publicly listed (TYO.6594), International brand |
| **Parent Company/Group** | Nidec Corporation |
| **Data Sources** | Official website, annual reports, product manuals, WAIC 2026 coverage |

## Company Overview

Global leader in small precision motors, with a leading market share in hard disk drive motors, actively expanding into robot joints and automotive drives.

Nidec started with hard disk drive spindle motors and has grown into a global supplier covering small motors, industrial motors, reducers, drive modules, and power semiconductors. Its product portfolio includes coreless motors, brushless DC motors, servo motors, planetary reducers, and integrated joint modules, widely used in humanoid robots, industrial robots, electric vehicles, and consumer electronics.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Small Precision Motors | Coreless/Brushless DC Motors | NX Series, N Series | Robot joints, medical, consumer electronics |
| Industrial Servo Systems | Servo motors and drives | SV Series, DX Series | Industrial robots, semiconductor equipment |
| Reducers and Modules | Planetary reducers, integrated joints | VRSF Series (Shimpo), Smart Flex | Collaborative robots, humanoid robots |

## Representative Products

### NX Series Servo Motor / Nidec NX Series Servo Motor

> NX Series Servo Motor: Please visit [official materials](https://www.nidec.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Size | 40–130 mm flange (series range) | Product manual |
| Rated Power | 50 W–5 kW | Product manual |
| Rated Speed | 1,000–6,000 rpm | Product manual |
| Rated Torque | 0.16–23.9 N·m | Product manual |
| Supply Voltage | 200–400 VAC / 24–48 VDC | Product manual |
| Encoder Resolution | 17–23 bit absolute optional | Product manual |
| Efficiency | ≥90% | Product manual |
| Price | Not disclosed | - |

**Technical Highlights**: High power density, low cogging torque, supports multiple feedback interfaces, suitable for high dynamic response robot joints and servo systems.

**Application Scenarios**: Humanoid robot joints, collaborative robots, semiconductor equipment, CNC machine tools, automated production lines.

### Coreless Brushless DC Motor / Nidec Coreless Brushless DC Motor

> Coreless Brushless DC Motor: Please visit [official materials](https://www.nidec.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Size | Ø8–Ø35 mm (series range) | Product manual |
| Weight | 2–80 g (depending on model) | Product manual |
| Rated Voltage | 6–48 VDC | Product manual |
| Rated Speed | 5,000–20,000 rpm | Product manual |
| Rated Torque | 0.5–60 mNm | Product manual |
| Efficiency | ≥85% | Product manual |
| Communication Interface | Hall / Encoder optional | Product manual |
| Price | Not disclosed | - |

**Technical Highlights**: Ironless rotor, low inductance, high acceleration capability, suitable for compact spaces such as dexterous hands and micro robotic arms.

**Application Scenarios**: Humanoid robot fingers, medical handheld instruments, drone gimbals, precision optical focusing.

## Supply Chain Position

- **Upstream Key Components/Materials**: Rare earth permanent magnets, silicon steel sheets, copper wire, bearings, driver ICs, power devices
- **Downstream Customers/Applications**: Robot OEMs, automotive manufacturers, industrial automation companies, consumer electronics brands
- **Main Competitors/Peers**: Maxon, Faulhaber, Moons', Zhaowei Machinery & Electronics, Inovance Technology

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_nidec`
- Product/Component Entities: `ent_component_nidec_nx_servo`, `ent_component_nidec_coreless_motor`
- Key Relationships:
  - `ent_company_nidec` -- `manufactures` --> `ent_component_nidec_nx_servo`
  - `ent_company_nidec` -- `manufactures` --> `ent_component_nidec_coreless_motor`

## References

1. [Official Website](https://www.nidec.com)
2. [WAIC 2026 Exhibition Coverage](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.nidec.com/en/product/category/ servo) (Please verify against actual product models)
