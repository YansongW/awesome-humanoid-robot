# Honeywell / Honeywell International Inc.

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 霍尼韦尔 |
| **English Name** | Honeywell International Inc. |
| **Headquarters** | Charlotte, North Carolina, USA |
| **Founded** | 1906 |
| **Website** | [https://www.honeywell.com](https://www.honeywell.com) |
| **Supply Chain Role** | Industrial Automation, Process Control, Building Automation, Sensors, PLC |
| **Enterprise Type** | Public Company (NASDAQ: HON) |
| **Parent Company/Group** | None (Independently Listed) |
| **Data Source** | Honeywell official website, process control product documentation, public financial reports |

## Company Overview

Honeywell is a global leader in industrial automation, aerospace, and building technologies.

Honeywell's industrial automation business focuses on process control (Experion PKS), safety systems, field instruments, PLCs (ControlEdge), and industrial software, covering industries such as oil & gas, chemicals, power generation, and pharmaceuticals. The ControlEdge PLC emphasizes seamless integration with Experion PKS, IIoT connectivity, and cybersecurity, making it suitable for hybrid industries and critical infrastructure. Its sensors and control technologies are also applicable to robotic environmental perception and process monitoring.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| DCS / Process Control | Large-scale continuous process control | Experion PKS | Oil & gas, chemicals, power generation |
| PLC / RTU | Discrete and hybrid control | ControlEdge PLC / RTU | Process plants, remote sites |
| Industrial Software & Security | Production management, cybersecurity | Honeywell Forge / SMX | Smart factories, energy |

## Representative Products

### Honeywell ControlEdge PLC

> Honeywell ControlEdge PLC: Please visit [official documentation](https://www.honeywell.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Product Type | Programmable Logic Controller (PLC) | Official documentation |
| Communication Protocols | Modbus/TCP, EtherNet/IP, OPC UA, MQTT | Official documentation |
| Redundancy Support | Supported (depending on configuration) | Official documentation |
| Programming Standard | IEC 61131-3 | Official documentation |
| Operating Temperature | -20 °C ~ 60 °C | Official documentation |
| Safety Certification | Not disclosed | Not disclosed |
| Supply Voltage | 24 VDC | Official documentation |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: Deep integration with Experion PKS, built-in OPC UA/MQTT support, designed for IIoT and process industries, redundancy and high availability options.

**Application Scenarios**: Oil & gas storage and transportation, chemical processes, power auxiliary control, water treatment, pharmaceuticals, process monitoring in humanoid robot testing environments.

## Relevance to Humanoid Robots

Humanoid robot manufacturing involves extensive environmental monitoring, energy management, and process data acquisition. Honeywell's PLCs and sensor networks can provide a stable process control and data foundation for laboratories and production lines.

## Supply Chain Position

- **Upstream Key Components/Materials**: Semiconductors, sensor elements, PCBs, power modules, connectors, enclosures
- **Downstream Customers/Application Scenarios**: Oil & gas, chemicals, power generation, pharmaceuticals, buildings & infrastructure
- **Main Competitors/Peers**: Emerson, Siemens, ABB, Yokogawa

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_honeywell`
- Product Entity: `ent_product_honeywell_control_edge`
- Key Relationships:
  - `ent_company_honeywell` -- `manufactures` --> `ent_product_honeywell_control_edge`

## References

1. [Honeywell Official Website](https://www.honeywell.com)
2. [Honeywell ControlEdge PLC Product Page](https://process.honeywell.com/us/en/products/control-edge-plc)
3. Honeywell Process Solutions ControlEdge PLC datasheet
