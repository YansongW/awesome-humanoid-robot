# Bota Systems

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Bota Systems (博塔系统) |
| **English Name** | Bota Systems |
| **Headquarters** | Zurich, Switzerland |
| **Founded** | 2019 |
| **Website** | [https://www.bota-systems.com](https://www.bota-systems.com) |
| **Supply Chain Role** | Six-axis force/torque sensors, collaborative robot end-effector force sensing |
| **Company Type** | Private company, ETH Zurich spin-off |
| **Parent/Group** | Independent operation |
| **Data Source** | Bota Systems official website, product datasheets, industry reviews |

## Company Overview

Bota Systems is a Swiss supplier of six-axis force/torque sensors focused on collaborative robot and humanoid robot applications, known for compact, cost-effective force sensing solutions.

Incubated by the ETH Zurich research team, Bota Systems is dedicated to providing high-precision, low-cost six-axis force/torque sensors for collaborative robots, humanoid robots, and medical robots. Its products utilize advanced silicon strain gauges and compact mechanical design to achieve reliable force control and collision detection in confined spaces, and are widely used in robotic assembly, polishing, testing, and embodied intelligence research.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| SensONE Series | Six-axis force sensor for collaborative robots | SensONE / SensONE Mini | Collaborative robots, humanoid robot wrists |
| MiniONE Series | Ultra-miniature six-axis force sensor | MiniONE | Medical robots, dexterous hands, research |
| OEM / Custom Modules | Embedded force sensing units | Custom F/T modules | Robot joints, test platforms |

## Representative Products

### Bota Systems SensONE Six-Axis Force Sensor

> Bota Systems SensONE Six-Axis Force Sensor: Please visit the [official page](https://www.bota-systems.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | Six-axis force/torque sensor | Official website |
| Diameter | Approx. 80 mm | Official website/datasheet |
| Height | Approx. 21 mm | Official website/datasheet |
| Weight | Approx. 290 g | Official website/datasheet |
| Force measurement range (Fx/Fy) | ±200 N | Official website/datasheet |
| Force measurement range (Fz) | ±500 N | Official website/datasheet |
| Torque measurement range (Mx/My/Mz) | ±8 Nm | Official website/datasheet |
| Accuracy | Not disclosed | - |
| Overload capacity | Approx. 500% FS | Official website/datasheet |
| Sampling frequency | Up to 1000 Hz | Official website/datasheet |
| Communication interface | EtherCAT / Ethernet / USB / RS485 / CAN | Official website/datasheet |
| Protection rating | IP67 | Official website/datasheet |
| Power supply | Not disclosed | - |
| Operating temperature | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: Compact structure optimized for collaborative robot end-effectors, built-in high-precision silicon strain gauges and multi-axis decoupling algorithms, supports plug-and-play and mainstream robot interfaces, with high overload protection and industrial-grade protection.

**Application Scenarios**: Collaborative robot force control, drag teaching, precision assembly, polishing and grinding, humanoid robot wrist/ankle force feedback, medical rehabilitation robots.

### Bota Systems MiniONE Ultra-Miniature Six-Axis Force Sensor

> Bota Systems MiniONE Ultra-Miniature Six-Axis Force Sensor: Please visit the [official page](https://www.bota-systems.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | Ultra-miniature six-axis force sensor | Official website |
| Diameter | Approx. 15 mm | Official website |
| Height | Approx. 8 mm | Official website |
| Weight | Approx. 5 g | Official website |
| Force/torque range | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: Ultra-miniature six-axis force sensing solution for extremely space-constrained scenarios such as medical robots and dexterous hands.

**Application Scenarios**: Medical minimally invasive surgical instruments, robot dexterous hand fingertips, miniature force-controlled grippers, academic research.

## Supply Chain Position

- **Upstream Key Components/Materials**: High-strength aluminum alloy/stainless steel, silicon strain gauges, signal conditioning chips, precision machining, connectors and cables
- **Downstream Customers/Application Scenarios**: Collaborative robots, humanoid robots, medical robots, automated production lines, research institutions
- **Main Competitors/Peers**: ATI Industrial Automation, OnRobot, Robotiq, Kunwei Technology, Yuli Instrument, Keli Sensing

## Knowledge Graph Nodes and Relationships

- Company entity: `ent_company_bota_systems`
- Product entity: `ent_product_bota_systems_sensone`
- Component entity: `ent_component_bota_systems_sensone_sensor`
- Key relationships:
  - `ent_company_bota_systems` -- `manufactures` --> `ent_product_bota_systems_sensone`
  - `ent_company_bota_systems` -- `manufactures` --> `ent_component_bota_systems_sensone_sensor`
  - `ent_product_bota_systems_sensone` -- `uses` --> `ent_component_bota_systems_sensone_sensor`

## References

1. [Bota Systems Official Website](https://www.bota-systems.com)
2. [Bota Systems SensONE Six-Axis Force Sensor Product/Information Page](https://www.bota-systems.com/sensone)
3. Company annual reports, product datasheets, and public press releases
4. [Appendix D Product Catalog](../index-products.md)
