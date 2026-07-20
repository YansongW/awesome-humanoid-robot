# Wolong Electric Drive

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).  
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 卧龙电驱 |
| **English Name** | Wolong Electric Drive |
| **Headquarters** | Shaoxing, China |
| **Founded** | 1984 |
| **Official Website** | [https://www.wolong.com](https://www.wolong.com) |
| **Supply Chain Role** | Motors / Drives / New Energy Vehicle Motors / Industrial Motors |
| **Enterprise Type** | Listed Company (SH.600580), Domestic Brand |
| **Parent Company/Group** | Wolong Holding Group Co., Ltd. |
| **Data Sources** | Official website, annual reports, product manuals, WAIC 2026 reports |

## Company Profile

A globally renowned supplier of motor and drive solutions, a leader in the fields of industrial motors and new energy vehicle motors.

Wolong Electric Drive primarily manufactures motor and drive control products, covering low-voltage/high-voltage motors, servo motors, new energy vehicle drive motors, industrial inverters, and energy storage systems. In recent years, the company has expanded into humanoid robots and embodied intelligence, offering high-power-density servo motors and joint drive solutions.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| Industrial Motors | Low-voltage/High-voltage asynchronous/synchronous motors | WE3, WE4 Series | Industry, Energy |
| Servo Motors | General-purpose and specialized servo | WM Series | Machine tools, Robotics |
| New Energy Drive Motors | Passenger/commercial vehicle motors | EV Platform | New Energy Vehicles |

## Representative Products

### Servo Motor / Wolong Servo Motor

> Servo Motor: Please visit [Official Materials](https://www.wolong.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Size | 40/60/80/130 Flange | Product Manual |
| Weight | 0.5–10 kg | Product Manual |
| Rated Power | 100 W – 7.5 kW | Product Manual |
| Rated Torque | 0.32–48 N·m | Product Manual |
| Rated Speed | 3,000 rpm | Product Manual |
| Maximum Speed | 6,000 rpm | Product Manual |
| Protection Level | IP65 (some models) | Product Manual |
| Price | Not disclosed | - |

**Technical Highlights**: High power density, wide speed range, supports multiple encoders, suitable for robot joints and automation equipment.

**Application Scenarios**: Industrial robots, humanoid robots, CNC machine tools, packaging machinery, new energy production lines.

### Variable Frequency Drive / Servo Drive / Wolong Variable Frequency / Servo Drive

> Variable Frequency Drive / Servo Drive: Please visit [Official Materials](https://www.wolong.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Size | Not disclosed | Product Manual |
| Weight | Not disclosed | Product Manual |
| Power Range | 0.4 kW – 630 kW | Product Manual |
| Control Method | V/F, Vector, Servo | Product Manual |
| Communication Protocol | Modbus, CANopen, EtherCAT | Product Manual |
| Supply Voltage | Single-phase/Three-phase 220/380/690 V | Product Manual |
| Protection Functions | Overvoltage, Overcurrent, Overtemperature, Short Circuit | Product Manual |
| Price | Not disclosed | - |

**Technical Highlights**: Covers the full power range from low to high voltage, supports multiple buses, suitable for large-scale automation and new energy equipment.

**Application Scenarios**: Industrial production lines, fans and pumps, elevators, new energy vehicles, high-power joints of humanoid robots.

## Supply Chain Position

- **Upstream Key Components/Materials**: Silicon steel sheets, copper wire, magnetic materials, bearings, power devices (IGBT/SiC), controller chips
- **Downstream Customers/Application Scenarios**: Industrial enterprises, new energy vehicle manufacturers, robot OEMs, energy equipment, home appliances
- **Main Competitors/Peers**: Siemens, ABB, WEG, Inovance Technology, Broad-Ocean Motor

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_wolong`
- Product/Component Entities: `ent_component_wolong_servo_motor`, `ent_component_wolong_drive`
- Key Relationships:
  - `ent_company_wolong` -- `manufactures` --> `ent_component_wolong_servo_motor`
  - `ent_company_wolong` -- `manufactures` --> `ent_component_wolong_drive`

## References

1. [Official Website](https://www.wolong.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.inovance.com) (Please verify against actual product models)
