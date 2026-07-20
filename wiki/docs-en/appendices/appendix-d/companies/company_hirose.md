# Hirose Electric

> This entry belongs to [Appendix D: Company/Product Wiki](../../appendix-d.md).  
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 广濑电机 |
| **English Name** | Hirose Electric |
| **Headquarters** | Shinagawa, Tokyo, Japan |
| **Founded** | 1937 |
| **Website** | [https://www.hirose.com](https://www.hirose.com) |
| **Supply Chain Role** | Connectors, Interconnects, FPC/FFC Connectors |
| **Company Type** | Public (TSE Prime: 6806) |
| **Parent/Group** | Independently Listed |
| **Data Sources** | Official website, product datasheets, annual reports |

## Company Overview

Hirose Electric is a Japanese high-end connector manufacturer known for high-density, high-reliability, and miniaturized connectors. Its DF, GT, and ZE series are widely used in drones, service robots, industrial cameras, servo encoders, and battery management systems.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| DF13 Series | 1.25 mm Wire-to-Board | DF13 | Small servos, encoders, cameras |
| GT Series | 0.8 mm Ultra-Compact | GT8E | Batteries, sensors, wearables |
| ZE05 / ZE064W | Waterproof Connectors | ZE05 | Outdoor robots, battery packs |

## Representative Products

### Hirose DF13 1.25 mm Wire-to-Board Connector

> Hirose DF13 1.25 mm Wire-to-Board Connector: Please visit [Official Documentation](https://www.hirose.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Pin Count | 2 – 40 (selectable) | Official catalog |
| Rated Current | Not disclosed | Official datasheet |
| Rated Voltage | Not disclosed | Official datasheet |
| Protection Rating | IP20 | Product documentation |
| Pitch | 1.25 mm | Official catalog |
| Application Scenarios | Small servos, encoders, industrial cameras, drones | Product documentation |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: Compact and reliable, good insertion/withdrawal feel, wide variety; a mainstream choice for signal connections in small robots.

**Application Scenarios**: Robot joint encoders, camera modules, IMUs, battery BMS, small actuators.

### Hirose GT8E 0.8 mm Ultra-Compact Connector

> Hirose GT8E 0.8 mm Ultra-Compact Connector: Please visit [Official Documentation](https://www.hirose.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Pin Count | 2 – 40 (selectable) | Official catalog |
| Rated Current | Not disclosed | Official datasheet |
| Rated Voltage | Not disclosed | Official datasheet |
| Protection Rating | IP20 | Product documentation |
| Pitch | 0.8 mm | Official catalog |
| Application Scenarios | Battery packs, sensors, wearable devices | Product documentation |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: 0.8 mm ultra-fine pitch, suitable for robot end-effectors and sensors with extreme space constraints.

**Application Scenarios**: Humanoid robot finger sensors, battery connections, micro cameras, AR/VR devices.

## Supply Chain Position

- **Upstream Key Components/Materials**: Phosphor bronze, high-performance plastics, gold/tin plating, cables
- **Downstream Customers/Applications**: Consumer electronics, automotive electronics, industrial robots, drones, medical equipment
- **Main Competitors/Peers**: J.S.T., JAE, Molex, Amphenol, TE Connectivity

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_hirose`
- Product Entity: `ent_product_hirose_df13`
- Component Entity: `ent_component_hirose_df13`
- Key Relationships:
  - `rel_ent_company_hirose_manufactures_ent_product_hirose_df13` (`ent_company_hirose` → `manufactures` → `ent_product_hirose_df13`)
  - `rel_ent_company_hirose_manufactures_ent_component_hirose_df13` (`ent_company_hirose` → `manufactures` → `ent_component_hirose_df13`)

## References

1. [Official Website](https://www.hirose.com)
2. Product datasheets and publicly available technical reports
3. [Appendix D: Product Catalog](../index-products.md)
