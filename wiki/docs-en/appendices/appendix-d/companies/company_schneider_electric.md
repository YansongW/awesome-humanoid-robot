# Schneider Electric SE

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).  
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 施耐德电气 |
| **English Name** | Schneider Electric SE |
| **Headquarters** | Rueil-Malmaison, France |
| **Founded** | 1836 |
| **Website** | [https://www.se.com](https://www.se.com) |
| **Supply Chain Role** | Industrial Automation, Energy Management, Motion Control, Digital Power Distribution |
| **Company Type** | Publicly traded (EPA: SU) |
| **Parent Company/Group** | None (independently listed) |
| **Data Source** | Schneider Electric official website, annual reports, product documentation |

## Company Overview

Schneider Electric is one of the global leaders in energy management and industrial automation.

Schneider Electric provides full-stack solutions for buildings, data centers, infrastructure, and industrial customers, ranging from low-voltage power distribution and medium-voltage grids to automation control and industrial software. Its industrial automation business is centered on Modicon PLCs, Altivar drives, Lexium servos, and the EcoStruxure Industrial Internet of Things platform, widely used in discrete manufacturing, hybrid industries, and process industries. Its open Ethernet architecture, cybersecurity capabilities, and energy efficiency management technologies offer mature solutions for production line power distribution, motion control, and energy optimization on the manufacturing side of humanoid robots.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| PLC / ePAC | Process and discrete control hub | Modicon M580 / M340 / M241 | Energy, water treatment, smart manufacturing |
| Drives and Servos | Motor control and motion control | Altivar Process / Lexium 32 | Pumps, fans, conveyors, robotics |
| Industrial Software and Energy Management | Digital twin and energy optimization | EcoStruxure / AVEVA | Plant operations, data centers |

## Representative Products

### Schneider Electric Modicon M580 ePAC

> Schneider Electric Modicon M580 ePAC: Please visit [official documentation](https://www.se.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Product Type | ePAC (Ethernet Programmable Automation Controller) | Official documentation |
| Program/Data Memory | Up to 64 MB | Official documentation (depends on CPU model) |
| Maximum I/O Capacity | Not disclosed | Not disclosed |
| Communication Interfaces | EtherNet/IP, Modbus TCP, OPC UA | Official documentation |
| Security Certification | Achilles Level 2 | Official documentation |
| Supply Voltage | 24 VDC | Official documentation |
| Operating Temperature | 0 °C ~ 60 °C | Official documentation |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: Native Ethernet, built-in cybersecurity, convergence of process and discrete control, support for DCS/PLC hybrid architecture.

**Application Scenarios**: Power and energy, water treatment, petrochemicals, food and beverage, control and power distribution for humanoid robot assembly lines.

## Relevance to Humanoid Robots

Mass production of humanoid robots requires stable power distribution, energy efficiency management, and production line control. Schneider's ePACs, drives, and servo systems provide mature automation and energy management infrastructure for assembly, testing, and logistics processes.

## Supply Chain Position

- **Upstream Key Components/Materials**: Semiconductors, power devices, PCBs, connectors, structural parts, sensors
- **Downstream Customers/Application Scenarios**: Energy infrastructure, industrial manufacturing, data centers, building automation
- **Main Competitors/Peers**: Siemens, Rockwell Automation, ABB, Mitsubishi Electric

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_schneider_electric`
- Product Entity: `ent_product_schneider_modicon_m580`
- Key Relationships:
  - `ent_company_schneider_electric` -- `manufactures` --> `ent_product_schneider_modicon_m580`

## References

1. [Schneider Electric Official Website](https://www.se.com)
2. [Schneider Electric Modicon M580 ePAC Product Page](https://www.se.com/us/en/product-range/1469-modicon-m580/)
3. Schneider Electric Annual Report / EcoStruxure platform pages
