# ATI Industrial Automation

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | ATI Industrial Automation |
| **English Name** | ATI Industrial Automation |
| **Headquarters** | Apex, North Carolina, USA (near Raleigh) |
| **Founded** | 1989 |
| **Website** | [https://www.ati-ia.com](https://www.ati-ia.com) |
| **Supply Chain Role** | Six-axis force/torque sensors, robotic end-effectors, collision sensors |
| **Enterprise Type** | Private company, Novanta subsidiary (acquired in 2021) |
| **Parent Company/Group** | Novanta Inc. (NASDAQ: NOVT) |
| **Data Source** | Official website, Novanta acquisition announcement, product datasheets |

## Company Overview

ATI is a global leading supplier of six-axis force/torque sensors and robotic end-effectors, with products widely used in industrial, collaborative, and medical robotics.

ATI offers six-axis force/torque sensors in the Nano, Mini, Gamma, Delta series, as well as end-effectors such as tool changers and collision sensors. Its silicon strain gauge technology features high signal-to-noise ratio and high overload capacity, suitable for robotic precision assembly, grinding, medical surgery, and force-controlled operations.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Nano Series | Micro six-axis force sensors | Nano17 / Nano25 / Nano43 | Collaborative robots, medical robots, fingertip force research |
| Mini Series | Small six-axis force sensors | Mini40 / Mini45 / Mini58 | Robotic assembly, grinding, testing |
| Tool Changers & Collision Sensors | End-effectors | QC Series / Collision Sensor | Automated production lines, collaborative robots |

## Representative Products

### ATI Nano25

> ATI Nano25: Please visit [official documentation](https://www.ati-ia.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Diameter | 25 mm | Official datasheet |
| Height | 21.6 mm | Official datasheet |
| Weight | 63.4 g | Official datasheet |
| Force measurement range (Fx/Fy) | ±250 N | Official datasheet |
| Force measurement range (Fz) | ±1000 N | Official datasheet |
| Torque measurement range (Tx/Ty/Tz) | ±6 Nm / ±3.4 Nm | Official datasheet |
| Single-axis overload capacity | 7.1 – 15.1 times rated range | Official datasheet |
| Resonant frequency | Fx,Fy,Tz: 3600 Hz; Fz,Tx,Ty: 3800 Hz | Distributor datasheet |
| Protection rating | Optional IP65 / IP68 | Official datasheet |
| Output interface | Analog / DAQ / EtherCAT / Net / TWE / WNet / Controller | Official datasheet |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: Extremely small size, high stiffness, high signal-to-noise ratio silicon strain gauge, ultra-high overload protection, suitable for humanoid robot wrist/ankle force control.

**Application Scenarios**: Collaborative robot force control, medical surgical robots, robotic precision assembly, fingertip force research, humanoid robot joints.

### ATI Mini45

> ATI Mini45: Please visit [official documentation](https://www.ati-ia.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Diameter | 45 mm | Official datasheet |
| Height | 15.7 mm | Official datasheet |
| Weight | Approx. 91 g | Official datasheet |
| Force measurement range (Fx/Fy) | ±240 N | Official datasheet |
| Force measurement range (Fz) | ±660 N | Official datasheet |
| Torque measurement range | ±12 Nm | Official datasheet |
| Interface | Multiple acquisition systems available | Official datasheet |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: Medium size, high dynamic response, multiple mounting options, a common choice for force control at the end of industrial robot arms.

**Application Scenarios**: Robotic grinding, polishing, assembly, testing, collaborative robot operations.

## Supply Chain Position

- **Upstream Key Components/Materials**: High-strength stainless steel, silicon strain gauges, signal conditioning circuits, precision machining, data acquisition systems
- **Downstream Customers/Application Scenarios**: Industrial robots, collaborative robots, medical surgical robots, humanoid robots, robot OEMs such as FANUC
- **Main Competitors/Peers**: OnRobot, Robotiq, Sunrise Instruments, Kunwei Technology, Hypersen

## Knowledge Graph Nodes and Relationships

- Company entity: `ent_company_ati`
- Product entity: `ent_component_ati_nano25`
- Product entity: `ent_component_ati_mini45`
- Key relationships:
  - `ent_company_ati` -- `manufactures` --> `ent_component_ati_nano25`
  - `ent_company_ati` -- `manufactures` --> `ent_component_ati_mini45`
  - `ent_company_ati` -- `supplies` --> `ent_company_fanuc` (ATI provides end-effector kits for FANUC CRX collaborative robots)

## References

1. [Official website](https://www.ati-ia.com)
2. [Product documentation and public reports](https://www.ati-ia.com)
3. [Appendix D Product Catalog](../index-products.md)
