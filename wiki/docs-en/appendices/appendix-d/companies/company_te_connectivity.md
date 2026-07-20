# TE Connectivity

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed".

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 泰科电子 |
| **English Name** | TE Connectivity |
| **Headquarters** | Galway, Ireland (Operational headquarters: Berwyn, Pennsylvania, USA) |
| **Founded** | 1941 (predecessor AMP) |
| **Website** | [https://www.te.com](https://www.te.com) |
| **Supply Chain Role** | Connectors, interconnects, sensors, cable assemblies |
| **Enterprise Type** | Public company (NYSE: TEL) |
| **Parent/Group** | Independently listed |
| **Data Source** | Official website, annual reports, product datasheets |

## Company Overview

TE Connectivity is a global leader in the connectivity and sensing field, with annual revenue exceeding tens of billions of US dollars. Its products cover the transportation, industrial, communications, and medical markets. Its connectors and cable assemblies are widely used in industrial robots, collaborative robots, servo drives, sensors, and communication modules.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| M12 / M8 Circular Connectors | Industrial Ethernet and sensor connection | M12 X-Code 8-position | Industrial robots, collaborative robots, vision systems |
| AMPMODU / Dynamic Series | Board-to-board and wire-to-board connection | AMPMODU 2.0 mm | Controller I/O, motor feedback, battery management |
| Sensors and Cable Assemblies | Force/temperature/position sensing | Force sensors, temperature sensors | Robot joints, actuators, end-of-arm tooling |

## Representative Products

### TE Connectivity M12 X-Code Industrial Ethernet Connector

> TE Connectivity M12 X-Code Industrial Ethernet Connector: Please visit [Official Documentation](https://www.te.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Number of Pins | 8 | IEC 61076-2-109 |
| Rated Current | Not disclosed | Official datasheet |
| Rated Voltage | Not disclosed | Official datasheet |
| Protection Rating | IP67 | Official catalog |
| Transmission Rate | 10 GbE (Cat6A) | Official catalog |
| Application Scenarios | Industrial robots, collaborative robots, sensor networks, vision systems | Product documentation |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: M12 X-Code keying prevents mis-mating, supports 10 GbE Industrial Ethernet, metal locking, IP67 protection, suitable for high-vibration robot environments.

**Application Scenarios**: Collaborative robot joint communication, industrial cameras, LiDAR, force sensors, AGV/AMR networks.

### TE Connectivity AMPMODU 2.0 mm Wire-to-Board Connector

> TE Connectivity AMPMODU 2.0 mm Wire-to-Board Connector: Please visit [Official Documentation](https://www.te.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Number of Pins | 2 – 40 (selectable) | Official catalog |
| Rated Current | Not disclosed | Official datasheet |
| Rated Voltage | Not disclosed | Official datasheet |
| Protection Rating | IP20 | Product documentation |
| Pitch | 2.0 mm | Official catalog |
| Application Scenarios | Controller I/O, servo drive feedback, battery management | Product documentation |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: High density, low cost, standard 2.0 mm pitch, suitable for PCB signal and power distribution.

**Application Scenarios**: Robot controllers, servo drive boards, sensor interfaces, industrial automation equipment.

## Supply Chain Position

- **Upstream Key Components/Materials**: Copper alloys, engineering plastics, plating materials, semiconductor chips, cables
- **Downstream Customers/Application Scenarios**: Industrial robots, collaborative robots, automotive, communication equipment, medical equipment
- **Main Competitors/Peers**: Amphenol, Molex, Hirose, JAE, J.S.T., LEONI

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_te_connectivity`
- Product Entity: `ent_product_te_connectivity_m12`
- Component Entity: `ent_component_te_connectivity_m12`
- Key Relationships:
  - `rel_ent_company_te_connectivity_manufactures_ent_product_te_connectivity_m12` (`ent_company_te_connectivity` → `manufactures` → `ent_product_te_connectivity_m12`)
  - `rel_ent_company_te_connectivity_manufactures_ent_component_te_connectivity_m12` (`ent_company_te_connectivity` → `manufactures` → `ent_component_te_connectivity_m12`)

## References

1. [Official Website](https://www.te.com)
2. Product datasheets and public technical reports
3. [Appendix D Product Catalog](../index-products.md)
