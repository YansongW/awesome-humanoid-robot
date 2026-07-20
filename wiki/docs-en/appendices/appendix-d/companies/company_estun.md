# Estun Automation

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 埃斯顿自动化 |
| **English Name** | Estun Automation |
| **Headquarters** | Nanjing, Jiangsu Province, China |
| **Founded** | 1993 |
| **Official Website** | [https://www.estun.com](https://www.estun.com) |
| **Supply Chain Segment** | Industrial robots, servo systems, motion control, collaborative robots, humanoid robot components |
| **Company Type** | Listed company (SZ: 002747), leading domestic industrial robot manufacturer |
| **Parent/Group** | Nanjing Estun Automation Co., Ltd. |
| **Data Sources** | Estun official website, annual reports, public press releases, industry research reports |

## Company Overview

Estun is a leading provider of industrial robots and motion control solutions in China. By developing its own servo systems, controllers, and robot bodies, the company extends into core components and complete machines for humanoid robots.

The company's business covers industrial robots (SCARA, six-axis, collaborative robots), servo systems, motion controllers, CNC systems, and intelligent manufacturing solutions. Estun has enhanced its technology and global presence through acquisitions such as UK-based Trio and Germany-based Cloos, and continues to invest in key humanoid robot components including harmonic reducers, frameless torque motors, and joint modules.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Industrial Robots | Six-axis/SCARA/Collaborative robot bodies | ER series, UNO series | Welding, handling, assembly, grinding |
| Servo & Motion Control | Servo drives, motors, PLCs, motion controllers | PRONET, ED3L, EM3A | Automation equipment, robots, machine tools |
| Humanoid Robot Components | Joint modules, reducers, frameless motors | Harmonic reducers, torque motor modules | Humanoid robots, collaborative robots |

## Representative Products

### Estun Industrial Robot / ER Series

> Estun Industrial Robot / ER Series: Please visit [official materials](https://www.estun.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Product Form | Six-axis industrial robot, SCARA, collaborative robot | Estun official website |
| Load Capacity | 3–600 kg (six-axis series) | Public specifications |
| Repeat Positioning Accuracy | ±0.02–±0.05 mm | Product manual |
| Reach | 500–3200 mm | Product manual |
| Degrees of Freedom | 4–6 DOF | Public specifications |
| Protection Rating | IP40–IP67 (varies by model) | Product manual |
| Controller | Self-developed ESTUN controller | Estun official website |
| Price | Not disclosed | - |

**Technical Highlights**: Full coverage of industrial robot series, self-developed servo and controller, acquisition of Cloos to enhance welding technology, leading domestic alternative.

**Application Scenarios**: Automotive welding, 3C assembly, lithium battery, photovoltaic, metal processing, logistics handling.

### Estun Servo System / PRONET Series

> Estun Servo System / PRONET Series: Please visit [official materials](https://www.estun.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Product Form | Servo drive + servo motor | Estun official website |
| Power Range | 0.05 kW–75 kW | Product manual |
| Control Mode | Position/Speed/Torque/Bus | Product manual |
| Communication Interface | EtherCAT, Modbus, CANopen | Product manual |
| Encoder | 17/23-bit absolute encoder | Product manual |
| Response Frequency | Not disclosed | - |
| Protection Rating | IP65 (some motors) | Product manual |
| Price | Not disclosed | - |

**Technical Highlights**: Representative of high-end domestic servo, supports multiple industrial Ethernet protocols, deeply integrated with self-developed robots.

**Application Scenarios**: Industrial robots, CNC machine tools, lithium battery equipment, semiconductor equipment, packaging machinery.

## Supply Chain Position

- **Upstream Key Components/Materials**: Rare earth permanent magnet materials, chips, electronic components, reducers, bearings, castings.
- **Downstream Customers/Application Scenarios**: Automotive, 3C, lithium battery, photovoltaic, metal processing, logistics industries; humanoid robot integrators.
- **Main Competitors/Peers**: Fanuc, ABB, KUKA, Yaskawa; domestic alternatives compared to Inovance Technology, EFORT.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_estun`
- Product Entities: `ent_product_estun_robot`, `ent_product_estun_servo`
- Key Relationships:
  - `ent_company_estun` -- `manufactures` --> `ent_product_estun_robot`
  - `ent_company_estun` -- `manufactures` --> `ent_product_estun_servo`
  - `ent_product_estun_robot` -- `uses` --> `ent_component_estun_servo`
  - `ent_product_estun_servo` -- `uses` --> `ent_component_magnetic_steel`

## References

1. [Official Website](https://www.estun.com)
2. [Estun Official Website](https://www.estun.com)
3. Estun 2024 Annual Report
