# Step Automation / Kinco

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 步科股份 |
| **English Name** | Step Automation / Kinco |
| **Headquarters** | Shenzhen, China |
| **Founded** | 1996 |
| **Official Website** | [https://www.kinco.cn](https://www.kinco.cn) |
| **Supply Chain Role** | Servo Drive / Low-Voltage Servo / HMI |
| **Company Type** | Listed Company (SH.688160), Domestic Brand |
| **Parent Company/Group** | Shenzhen Step Electric Co., Ltd. / Kinco |
| **Data Sources** | Official website, annual reports, product manuals, WAIC 2026 reports |

## Company Profile

A leading domestic supplier of machine automation and digital solutions, with a leading market share in low-voltage servo systems for mobile robots.

Step Automation primarily manufactures core components for industrial automation equipment control, including HMI, PLC, servo systems, low-voltage servo motors, and drives. The company's low-voltage servo products are widely used in AGV/AMR, collaborative robots, medical rehabilitation equipment, and humanoid robot joints, featuring high integration, low energy consumption, and fast response.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| Low-Voltage Servo System | Dedicated for mobile robots | FD Series, SMC Series | AGV/AMR, Service Robots |
| Servo Drive | General-purpose and dedicated servo | JD Series, OD Series | Industrial Robots, Machine Tools |
| Human-Machine Interface | Industrial HMI | GL100, GT100 Series | Production Line Monitoring, Equipment Control |

## Representative Products

### Low-Voltage Servo System / Step Low-Voltage Servo System

> Low-Voltage Servo System: Please visit the [official website](https://www.kinco.cn) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | Drive approx. 70×120×40 mm (reference) | Product Manual |
| Weight | Not disclosed | Product Manual |
| Supply Voltage | DC 24–72 V | Product Manual |
| Rated Power | 50 W – 1 kW | Product Manual |
| Rated Speed | 3,000 rpm | Product Manual |
| Encoder | 17/23-bit multi-turn absolute | Product Manual |
| Communication Interface | CANopen / EtherCAT / RS485 | Product Manual |
| Price | Not disclosed | - |

**Technical Highlights**: Low-voltage DC power supply, high power density, support for multiple buses, suitable for mobile robots and battery-powered equipment.

**Application Scenarios**: AGV/AMR hub drive, collaborative robot joints, humanoid robot lower limbs, exoskeletons.

### Servo Motor / Step Servo Motor

> Servo Motor: Please visit the [official website](https://www.kinco.cn) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | 40/60/80 flange (series range) | Product Manual |
| Weight | 0.3–3 kg | Product Manual |
| Rated Power | 100 W – 1.5 kW | Product Manual |
| Rated Torque | 0.32–4.77 N·m | Product Manual |
| Rated Speed | 3,000 rpm | Product Manual |
| Protection Rating | IP65 (some models) | Product Manual |
| Encoder | 23-bit absolute | Product Manual |
| Price | Not disclosed | - |

**Technical Highlights**: High-precision encoder, low cogging torque, compact structure, suitable for integrated joint modules.

**Application Scenarios**: Collaborative robots, SCARA, Delta, humanoid robot joints.

## Supply Chain Position

- **Upstream Key Components/Materials**: IGBT/SiC power devices, MCU/FPGA control chips, magnetic materials, encoder chips, capacitors, resistors
- **Downstream Customers/Application Scenarios**: AGV/AMR manufacturers, collaborative robot companies, humanoid robot OEMs, medical equipment, logistics automation
- **Main Competitors/Peers**: Inovance, Hechuan Technology, Leadshine, Moons', Inovance

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_step`
- Product/Component Entities: `ent_component_step_low_voltage_servo`, `ent_component_step_servo_motor`
- Key Relationships:
  - `ent_company_step` -- `manufactures` --> `ent_component_step_low_voltage_servo`
  - `ent_company_step` -- `manufactures` --> `ent_component_step_servo_motor`

## References

1. [Official Website](https://www.kinco.cn)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.inovance.com) (Please verify against actual product models)
