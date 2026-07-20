# Molex

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 莫仕 |
| **English Name** | Molex |
| **Headquarters** | Lisle, Illinois, USA |
| **Founded** | 1938 |
| **Website** | [https://www.molex.com](https://www.molex.com) |
| **Supply Chain Role** | Connectors, Cable Assemblies, Antennas, Sensors |
| **Enterprise Type** | Private Company (Subsidiary of Koch Industries) |
| **Parent Company/Group** | Koch Industries |
| **Data Source** | Official website, product datasheets, industry reports |

## Company Overview

Molex is a leading global supplier of electronic connectors and interconnect solutions, with products covering consumer electronics, automotive, industrial, and medical sectors. Its Micro-Fit, Mini-Fit, and Brad industrial circular connectors are widely used in robot power, signal, and communication connections.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Micro-Fit 3.0 | 3.0 mm power/signal connection | Micro-Fit 3.0 | Servo drives, robot joints |
| Brad M12 / M8 | Industrial circular connectors | Brad M12 8-position | Industrial Ethernet, sensors |
| Custom cable assemblies | Custom wiring harnesses | Robot harnesses | Full machine OEM, Tier 1 |

## Representative Products

### Molex Micro-Fit 3.0 Connector System

> Molex Micro-Fit 3.0 Connector System: Please visit [official documentation](https://www.molex.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Number of pins | 2 – 24 (selectable) | Official catalog |
| Rated current | Not disclosed | Official datasheet |
| Rated voltage | Not disclosed | Official datasheet |
| Protection rating | IP20 | Product documentation |
| Pitch | 3.00 mm | Official catalog |
| Application scenarios | Robot power distribution, servo drives, controller I/O | Product documentation |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: The 3.0 mm pitch balances current carrying capacity and space, featuring positive locking and polarization keying, suitable for medium-power power and signal applications.

**Application Scenarios**: Humanoid robot joint power supply, servo drives, battery packs, industrial controllers.

### Molex Brad M12 Industrial Circular Connector

> Molex Brad M12 Industrial Circular Connector: Please visit [official documentation](https://www.molex.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Number of pins | 4 / 8 (selectable) | Official catalog |
| Rated current | Not disclosed | Official datasheet |
| Rated voltage | Not disclosed | Official datasheet |
| Protection rating | IP67 | Product documentation |
| Interface type | M12 D-Code / X-Code | Product documentation |
| Application scenarios | Industrial Ethernet, sensors, actuators | Product documentation |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: The Brad series is designed for industrial environments, offering corrosion resistance, vibration resistance, and plug-and-play capability, supporting Profinet/EtherNet/IP.

**Application Scenarios**: Collaborative robot end-of-arm tooling, industrial cameras, force sensors, AGV/AMR.

## Supply Chain Position

- **Upstream Key Components/Materials**: Copper alloys, LCP/PBT plastics, plating materials, cables, magnetic materials
- **Downstream Customers/Application Scenarios**: Automotive, consumer electronics, industrial automation, robotics, medical
- **Main Competitors/Peers**: TE Connectivity, Amphenol, Hirose, JAE, J.S.T.

## Knowledge Graph Nodes and Relationships

- Company entity: `ent_company_molex`
- Product entity: `ent_product_molex_micro_fit_3`
- Component entity: `ent_component_molex_micro_fit_3`
- Key relationships:
  - `rel_ent_company_molex_manufactures_ent_product_molex_micro_fit_3` (`ent_company_molex` → `manufactures` → `ent_product_molex_micro_fit_3`)
  - `rel_ent_company_molex_manufactures_ent_component_molex_micro_fit_3` (`ent_company_molex` → `manufactures` → `ent_component_molex_micro_fit_3`)

## References

1. [Official website](https://www.molex.com)
2. Product datasheets and public technical reports
3. [Appendix D Product Catalog](../index-products.md)
