# Amphenol

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 安费诺 |
| **English Name** | Amphenol |
| **Headquarters** | Wallingford, Connecticut, USA |
| **Founded** | 1932 |
| **Website** | [https://www.amphenol.com](https://www.amphenol.com) |
| **Supply Chain Role** | Connectors, interconnects, antennas, cable assemblies |
| **Enterprise Type** | Public company (NYSE: APH) |
| **Parent Company/Group** | Independently listed |
| **Data Source** | Official website, annual reports, product datasheets |

## Company Overview

Amphenol is the world's second-largest connector manufacturer, covering the military/aerospace, communications, automotive, and industrial markets. Its high-density, high-reliability connectors and cable assemblies are used in robot controllers, sensors, servo systems, and communication modules.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Minitek MicroSpace | 1.27 mm compact connector | Minitek MicroSpace | Automotive electronics, robot controllers |
| M12 / M8 Circular Connectors | Industrial communication and sensors | Amphenol M12 X-Code | Industrial automation, robotics |
| RF and Antennas | Wireless connectivity | 5G/IoT antennas | Mobile robots, AGV/AMR |

## Representative Products

### Amphenol Minitek MicroSpace 1.27 mm Wire-to-Board Connector

> Amphenol Minitek MicroSpace 1.27 mm Wire-to-Board Connector: Please visit [official documentation](https://www.amphenol.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Number of Pins | 2 – 40 (selectable) | Official catalog |
| Rated Current | Not disclosed | Official datasheet |
| Rated Voltage | Not disclosed | Official datasheet |
| Protection Rating | IP20 | Product documentation |
| Pitch | 1.27 mm | Official catalog |
| Application Scenarios | Automotive electronics, robot controllers, sensor interfaces | Product documentation |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: 1.27 mm compact pitch, suitable for space-constrained designs, supports automated assembly and multiple plating options.

**Application Scenarios**: Robot control boards, motor drives, BMS, industrial controllers, automotive ECUs.

### Amphenol M12 X-Code 8-Position Circular Connector

> Amphenol M12 X-Code 8-Position Circular Connector: Please visit [official documentation](https://www.amphenol.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Number of Pins | 8 | Official catalog |
| Rated Current | Not disclosed | Official datasheet |
| Rated Voltage | Not disclosed | Official datasheet |
| Protection Rating | IP67 | Product documentation |
| Transmission Rate | 10 GbE | Product documentation |
| Application Scenarios | Industrial Ethernet, robot sensors, vision systems | Product documentation |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: M12 standard interface, industrial-grade waterproof and dustproof, supports high-speed Ethernet and high-vibration environments.

**Application Scenarios**: Collaborative robots, industrial robots, AGV/AMR, industrial cameras, LiDAR.

## Supply Chain Position

- **Upstream Key Components/Materials**: Copper alloys, high-performance plastics, plating materials, cables, magnetic materials
- **Downstream Customers/Application Scenarios**: Automotive, communications, industrial automation, robotics, aerospace
- **Main Competitors/Peers**: TE Connectivity, Molex, Hirose, JAE, J.S.T.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_amphenol`
- Product Entity: `ent_product_amphenol_minitek_microspace`
- Component Entity: `ent_component_amphenol_minitek_microspace`
- Key Relationships:
  - `rel_ent_company_amphenol_manufactures_ent_product_amphenol_minitek_microspace` (`ent_company_amphenol` → `manufactures` → `ent_product_amphenol_minitek_microspace`)
  - `rel_ent_company_amphenol_manufactures_ent_component_amphenol_minitek_microspace` (`ent_company_amphenol` → `manufactures` → `ent_component_amphenol_minitek_microspace`)

## References

1. [Official Website](https://www.amphenol.com)
2. Product datasheets and public technical reports
3. [Appendix D Product Catalog](../index-products.md)
