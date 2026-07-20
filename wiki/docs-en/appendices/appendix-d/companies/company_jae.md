# Japan Aviation Electronics / JAE

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed".

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Japan Aviation Electronics |
| **English Name** | JAE |
| **Headquarters** | Shibuya, Tokyo, Japan |
| **Founded** | 1953 |
| **Official Website** | [https://www.jae.com](https://www.jae.com) |
| **Supply Chain Role** | Connectors, interconnects, aviation/automotive electronics |
| **Company Type** | Publicly listed (Tokyo Stock Exchange Prime: 6807) |
| **Parent Company/Group** | Independently listed |
| **Data Source** | Official website, product datasheets, annual reports |

## Company Overview

JAE (Japan Aviation Electronics) started in avionics and has grown into a major supplier of connectors for automotive, industrial, and communication applications. Its high-reliability connectors and wire harnesses are widely used in robot controllers, servo motors, cameras, LiDAR, and battery management systems.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| IL-WX Series | 1.25 mm wire-to-board | IL-WX | Industrial control, robot internal wiring |
| MX34 / MX23A | Automotive waterproof connection | MX34 | Automotive, outdoor robots |
| KN06 / KN07 | Circular connectors | KN Series | Industrial equipment, communications |

## Representative Products

### JAE IL-WX 1.25 mm Wire-to-Board Connector

> JAE IL-WX 1.25 mm wire-to-board connector: Please visit [official documentation](https://www.jae.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Number of Pins | 2 – 30 (selectable) | Official catalog |
| Rated Current | Not disclosed | Official datasheet |
| Rated Voltage | Not disclosed | Official datasheet |
| Protection Rating | IP20 | Product documentation |
| Pitch | 1.25 mm | Official catalog |
| Application Scenarios | Industrial controllers, robot internal wiring, camera modules | Product documentation |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: Low-profile design, reliable contact, suitable for robot controllers and sensor modules with limited PCB space.

**Application Scenarios**: Robot control boards, industrial cameras, LiDAR interfaces, encoders, communication modules.

### JAE MX34 Automotive Waterproof Connector

> JAE MX34 automotive waterproof connector: Please visit [official documentation](https://www.jae.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Number of Pins | Multiple specifications | Official catalog |
| Rated Current | Not disclosed | Official datasheet |
| Rated Voltage | Not disclosed | Official datasheet |
| Protection Rating | IP67 | Product documentation |
| Temperature Range | -40°C ~ +125°C | Product documentation |
| Application Scenarios | Automotive, outdoor robots, battery packs | Product documentation |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: Automotive-grade waterproof and dustproof, wide temperature range, suitable for robot power and signal connections in harsh environments.

**Application Scenarios**: Outdoor inspection robots, unmanned vehicles, battery management systems, automotive wire harnesses.

## Supply Chain Position

- **Upstream Key Components/Materials**: Copper alloys, engineering plastics, plating materials, cables, aviation-grade materials
- **Downstream Customers/Application Scenarios**: Automotive, aerospace, industrial automation, robotics, communication equipment
- **Main Competitors/Peers**: TE Connectivity, Amphenol, Molex, Hirose, J.S.T.

## Knowledge Graph Nodes and Relationships

- Company entity: `ent_company_jae`
- Product entity: `ent_product_jae_il_wx`
- Component entity: `ent_component_jae_il_wx`
- Key relationships:
  - `rel_ent_company_jae_manufactures_ent_product_jae_il_wx` (`ent_company_jae` → `manufactures` → `ent_product_jae_il_wx`)
  - `rel_ent_company_jae_manufactures_ent_component_jae_il_wx` (`ent_company_jae` → `manufactures` → `ent_component_jae_il_wx`)

## References

1. [Official Website](https://www.jae.com)
2. Product datasheets and publicly available technical reports
3. [Appendix D Product Catalog](../index-products.md)
