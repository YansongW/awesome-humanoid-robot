# Rockwell Automation, Inc.

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Rockwell Automation |
| **English Name** | Rockwell Automation, Inc. |
| **Headquarters** | Milwaukee, WI, USA |
| **Founded** | 1903 |
| **Website** | [https://www.rockwellautomation.com](https://www.rockwellautomation.com) |
| **Supply Chain Segment** | Industrial Automation, PLC, Servo Drives, Industrial Software, Information Security |
| **Enterprise Type** | Publicly Traded (New York Stock Exchange: ROK) |
| **Parent Company/Group** | None (Independently Listed) |
| **Data Source** | Rockwell Automation Official Website, Allen-Bradley Product Pages, Public Specifications |

## Company Overview

Rockwell Automation is one of the world's largest industrial automation and information companies. Its Allen-Bradley brand PLCs and ControlLogix systems hold a significant position in the discrete manufacturing sector.

Rockwell Automation provides complete solutions ranging from controllers, servo drives, and variable frequency drives to FactoryTalk industrial software, Industrial Internet of Things (IIoT), and cybersecurity. Its Integrated Architecture platform supports deep integration of robotics, motion control, and digital manufacturing, enabling support for humanoid robot production line integration, data collection, and MES connectivity.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| Control Systems | PLC, PAC, Safety Controllers | ControlLogix / CompactLogix / GuardLogix | Automotive, Food & Beverage, Logistics |
| Motion Control | Servo Drives, Servo Motors, Variable Frequency Drives | Kinetix 5700 / PowerFlex | Packaging, Robotics, Conveying |
| Industrial Software | MES, Asset Performance, Analytics | FactoryTalk / Plex | Smart Manufacturing, Digital Factory |

## Representative Products

### Rockwell Automation Integrated Architecture / ControlLogix

> ControlLogix 5580: Please visit the [official documentation](https://www.rockwellautomation.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Controller Type | Programmable Automation Controller (PAC) | Rockwell Official Website |
| Processor | Not disclosed | Rockwell Official Website |
| I/O Expansion | Modular, supports local and distributed I/O | Rockwell Official Website |
| Communication Protocols | EtherNet/IP, ControlNet, DeviceNet | Rockwell Official Website |
| Programming Environment | Studio 5000 Logix Designer | Rockwell Official Website |
| Protection Rating | IP20 (within control cabinet) | Rockwell Official Website |
| Mounting Method | DIN Rail / Panel Mount | Rockwell Official Website |
| Price | Not disclosed | Requires quotation |

**Technical Highlights**: Unified Logix control engine integrating standard, safety, motion, and process control; seamless connection of robots, servos, and information systems via EtherNet/IP.

**Application Scenarios**: Production line control, robot cell integration, humanoid robot testing and assembly lines, digital factory MES/OT convergence.

## Relevance to Humanoid Robots

- Rockwell Automation's capabilities in industrial automation, PLCs, servo drives, industrial software, and information security can provide key equipment or foundational components for humanoid robot parts processing, complete machine assembly, and testing.
- High-precision motion control, force control, and autonomous navigation technologies are core supports for human-like motion and manipulation.
- The company's implementation experience in scenarios such as automotive OEMs can provide commercial references for future humanoid robot applications.

## Supply Chain Position

- **Upstream Key Components/Materials**: Semiconductor chips, PCBs, connectors, power supplies, industrial software licenses.
- **Downstream Customers/Application Scenarios**: Automotive OEMs, consumer goods, life sciences, oil & gas, automation integrators.
- **Main Competitors/Peers**: Siemens, Schneider Electric, Mitsubishi Electric.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_rockwell`
- Product Entity: `ent_product_rockwell_automation`
- Key Relationship:
  - `ent_company_rockwell` -- `manufactures` --> `ent_product_rockwell_automation`

## References

1. [Rockwell Automation Official Website](https://www.rockwellautomation.com)
2. [ControlLogix 5580 Product Page](https://www.rockwellautomation.com/en-us/products/hardware/allen-bradley/controllers/programmable-automation-controllers.html)
3. [Public Information and Industry Reports](https://www.rockwellautomation.com)
