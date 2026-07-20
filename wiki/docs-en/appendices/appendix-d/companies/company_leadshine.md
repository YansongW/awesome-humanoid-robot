# Leadshine Technology

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 雷赛智能 |
| **English Name** | Leadshine Technology |
| **Headquarters** | Shenzhen, Guangdong, China |
| **Founded** | 1997 |
| **Website** | [https://www.leadshine.com](https://www.leadshine.com) |
| **Supply Chain Role** | Motion Control / Servo Drive / Stepper Drive / Motor / Controller |
| **Company Type** | Domestic brand, listed company (002979.SZ), motion control leader |
| **Parent/Group** | None (independently listed) |
| **Data Source** | Leadshine official website, product manuals, annual reports, WAIC 2026 coverage |

## Company Profile

Leadshine Technology is a leading enterprise in China's motion control field, with products covering servo drives, stepper drives, motion controllers, PLCs, and motors.

The company has long served industries such as industrial robots, semiconductor equipment, 3C equipment, lithium battery equipment, and humanoid robots. Leadshine continues to invest in robot joint drives, high-response servos, and bus communication, and is an important participant in the domestic substitution of core components for humanoid robots.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| AC Servo System | High-performance servo drive + motor | L8 Series / L7 Series | Industrial robots, humanoid robots |
| Stepper Drive | Open-loop/closed-loop stepper | DM / EM Series | 3C, engraving, textile |
| Motion Control Card/PLC | Multi-axis motion control | DMC / PMC Series | Automation equipment |

## Representative Products

### L8 Series AC Servo Drive

> L8 Series: Please visit [official materials](https://www.leadshine.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Product Form | AC servo drive | Leadshine official website |
| Power Range | 100 W – 7.5 kW | Product manual |
| Control Mode | Position/Speed/Torque | Product manual |
| Communication Protocol | EtherCAT / CANopen / Modbus | Product manual |
| Speed Loop Bandwidth | 3 kHz (reference) | Product manual |
| Encoder Support | 17/23-bit absolute, incremental | Product manual |
| Safety Function | STO (some models) | Product manual |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: High response bandwidth, supports multiple industrial Ethernet buses, suitable for joint drives of humanoid robots and collaborative robots, strong domestic substitution capability.

**Application Scenarios**: Industrial robots, humanoid robot joints, semiconductor equipment, lithium battery equipment, 3C automation.

### ACM Series Servo Motor

> ACM Series: Please visit [official materials](https://www.leadshine.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Product Form | AC servo motor | Leadshine official website |
| Power Range | 50 W – 7.5 kW | Product manual |
| Rated Speed | 1000–6000 rpm (depending on model) | Product manual |
| Frame Size | 40–180 mm | Product manual |
| Encoder | 17/23-bit absolute | Product manual |
| Protection Level | IP65 (some models) | Product manual |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: Low cogging torque, high overload capacity, deeply matched with Leadshine L8 series drives, supporting high-precision motion control for robots.

**Application Scenarios**: Industrial robots, humanoid robots, CNC machine tools, automated production lines.

## Supply Chain Position

- **Upstream Key Components/Materials**: IGBT, MOSFET, PCB, copper wire, aluminum housing, encoder chips, magnetic materials, DSP/ARM control chips.
- **Downstream Customers/Application Scenarios**: Industrial robot manufacturers, humanoid robot integrators, 3C equipment, semiconductor equipment, lithium battery equipment, CNC machine tools.
- **Main Competitors/Peers**: Inovance Technology, Hechuan Technology, Tsino-Dynatron, Yaskawa, Mitsubishi, Panasonic.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_leadshine`
- Product/Component Entities: `ent_component_leadshine_l8`, `ent_component_leadshine_acm`
- Key Relationships:
  - `ent_company_leadshine` -- `manufactures` --> `ent_component_leadshine_l8`
  - `ent_company_leadshine` -- `manufactures` --> `ent_component_leadshine_acm`
  - `ent_component_leadshine_l8` -- `uses` --> `ent_component_leadshine_acm`

## References

1. [Leadshine Technology Official Website](https://www.leadshine.com)
2. [WAIC 2026 Exhibition Coverage](https://www.worldrobotconference.com)
3. Leadshine Technology 2024 Annual Report and Product Manuals
