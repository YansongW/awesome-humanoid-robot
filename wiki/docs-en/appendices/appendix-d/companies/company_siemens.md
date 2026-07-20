# Siemens AG

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Siemens |
| **English Name** | Siemens AG |
| **Headquarters** | Munich, Germany |
| **Founded** | 1847 |
| **Official Website** | [https://www.siemens.com](https://www.siemens.com) |
| **Supply Chain Role** | Factory automation, PLC, industrial software, digital twin, drive technology |
| **Company Type** | Publicly traded (Frankfurt Stock Exchange: SIE) |
| **Parent Company/Group** | None (independently listed) |
| **Data Source** | Siemens official website, Siemens Industry product pages, public specifications |

## Company Overview

Siemens is a global leader in industrial automation and digitalization solutions. Its PLCs, drives, industrial software, and digital twin technology form the core infrastructure of smart manufacturing.

Through SIMATIC controllers, SINAMICS drives, TIA Portal engineering software, and Industrial Edge, Siemens provides full-stack solutions for factory automation, robot integration, and digital production lines. In the field of humanoid robots, its controllers, edge computing, and digital twins can be used for production line simulation, motion control, and quality traceability.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Factory Automation | PLC, HMI, industrial communication | SIMATIC S7-1500 / ET 200 | Discrete manufacturing, process industry |
| Drive Technology | Servo drives, motors, frequency converters | SINAMICS S210 / V90 | Machine tools, robots, conveyors |
| Industrial Software | Digital twin, MES, PLC programming | TIA Portal / NX MCD / Opcenter | Automotive, electronics, energy |

## Representative Products

### Siemens SIMATIC S7-1500 Automation System

> SIMATIC S7-1500: Please visit the [official page](https://www.siemens.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Controller Type | Modular PLC | Siemens official website |
| Processing Speed | Not disclosed | Siemens official website |
| I/O Expansion | Modular, supports distributed I/O | Siemens official website |
| Communication Protocols | PROFINET, PROFIBUS, OPC UA | Siemens official website |
| Programming Environment | TIA Portal | Siemens official website |
| Protection Rating | IP20 (in control cabinet) | Siemens official website |
| Mounting Method | DIN rail mounting | Siemens official website |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: High-performance modular PLC with integrated motion control, fail-safe, and OPC UA, supporting the unified TIA Portal engineering environment.

**Application Scenarios**: Production line control, robot cell integration, humanoid robot test benches, digital factory edge control.

## Relevance to Humanoid Robots

- Siemens' capabilities in factory automation, PLC, industrial software, digital twin, and drive technology can provide key equipment or basic components for humanoid robot parts processing, assembly, and testing.
- High-precision motion control, force control, and autonomous navigation technology are core supports for human-like motion and manipulation.
- The company's implementation experience in scenarios such as automotive OEMs can provide commercial references for future applications of humanoid robots.

## Supply Chain Position

- **Upstream Key Components/Materials**: Semiconductor chips, PCBs, connectors, power modules, industrial software.
- **Downstream Customers/Application Scenarios**: Automotive OEMs, electronics manufacturing, energy, medical equipment, automation integrators.
- **Main Competitors/Peers**: Rockwell Automation, Schneider Electric, Mitsubishi Electric.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_siemens`
- Product Entity: `ent_product_siemens_simatic`
- Key Relationship:
  - `ent_company_siemens` -- `manufactures` --> `ent_product_siemens_simatic`

## References

1. [Siemens Official Website](https://www.siemens.com)
2. [SIMATIC S7-1500 Product Page](https://www.siemens.com/global/en/products/automation/systems/industrial-plc/simatic-s7-1500.html)
3. [Public Information and Industry Reports](https://www.siemens.com)
