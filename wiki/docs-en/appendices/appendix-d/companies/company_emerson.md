# Emerson Electric Co.

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Emerson Electric |
| **English Name** | Emerson Electric Co. |
| **Headquarters** | St. Louis, Missouri, USA |
| **Founded** | 1890 |
| **Website** | [https://www.emerson.com](https://www.emerson.com) |
| **Supply Chain Role** | Process Control, Industrial Automation, Fluid Control, Electrical Equipment, Industrial Software |
| **Enterprise Attribute** | Public Company (NYSE: EMR) |
| **Parent Company/Group** | None (Independently Listed) |
| **Data Source** | Emerson Website, Product Catalog, Annual Report |

## Company Profile

Emerson Electric is a global leader in process industry automation and fluid control technology.

Through DeltaV DCS, PACSystems PLC, Ovation Control Systems, ASCO Fluid Control, Rosemount Instrumentation, and AspenTech Industrial Software, Emerson provides automation solutions for industries such as energy, chemicals, power, and life sciences. Its PACSystems RSTi-EP series combines compact controllers with distributed I/O, emphasizing modularity, scalability, and cybersecurity. Its sensors, valves, and motion control products also serve robotics and intelligent equipment.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| Process Control / DCS | Continuous Process Automation | DeltaV / Ovation | Oil & Gas, Chemicals, Power |
| PLC / PAC | Discrete and Hybrid Control | PACSystems RX3i / RSTi-EP | Manufacturing, Water Treatment, Energy |
| Fluid Control & Instrumentation | Valves, Actuators, Sensors | ASCO / Rosemount / AVENTICS | Process Plants, Robot Pneumatics |

## Representative Product

### Emerson PACSystems RSTi-EP PLC

> Emerson PACSystems RSTi-EP PLC: Please visit [Official Documentation](https://www.emerson.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Product Type | Programmable Automation Controller (PAC) | Official Documentation |
| I/O Capacity | Up to 2,048 points (depending on configuration) | Official Documentation |
| Scan Speed | 1 ms / 1K Boolean instructions | Official Documentation |
| Communication Interfaces | PROFINET, EtherNet/IP, Modbus/TCP, OPC UA | Official Documentation |
| Programming Software | PAC Machine Edition | Official Documentation |
| Redundancy Support | Supported | Official Documentation |
| Operating Temperature | -20 °C ~ 60 °C | Official Documentation |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: Compact modular PAC, distributed I/O expansion, built-in cybersecurity features, multi-protocol communication, and redundancy capability.

**Application Scenarios**: Water treatment, food & beverage, discrete manufacturing, energy, life sciences, robot cell control, and test systems.

## Relevance to Humanoid Robots

Humanoid robot prototype development and testing require collecting large amounts of sensor data and controlling peripheral equipment. The modular I/O and fast scan speed of PACSystems make it suitable for use as laboratory test benches and production line control nodes.

## Supply Chain Position

- **Upstream Key Components/Materials**: Processors, power modules, I/O modules, sensors, pneumatic components, PCBs
- **Downstream Customers/Application Scenarios**: Oil & gas, chemicals, power, water treatment, discrete manufacturing, robot integration
- **Main Competitors/Peers**: Honeywell, Siemens, Schneider Electric, Rockwell Automation

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_emerson`
- Product Entity: `ent_product_emerson_pacsystems_rsti_ep`
- Key Relationships:
  - `ent_company_emerson` -- `manufactures` --> `ent_product_emerson_pacsystems_rsti_ep`

## References

1. [Emerson Electric Website](https://www.emerson.com)
2. [Emerson PACSystems RSTi-EP PLC Product Page](https://www.emerson.com/en-us/catalog/controllers/pacsystems-rsti-ep)
3. Emerson PACSystems RSTi-EP product catalog
