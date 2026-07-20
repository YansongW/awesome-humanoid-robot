# Prysmian Group

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed".

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 普睿司曼 |
| **English Name** | Prysmian Group |
| **Headquarters** | Milan, Italy |
| **Founded** | 1879 (formerly Pirelli Cavi) |
| **Website** | [https://www.prysmiangroup.com](https://www.prysmiangroup.com) |
| **Supply Chain Role** | Power cables, communication cables, industrial specialty cables |
| **Enterprise Type** | Public company (BIT: PRY) |
| **Parent Company/Group** | Independently listed |
| **Data Source** | Official website, annual reports, product catalogs |

## Company Profile

Prysmian Group is one of the world's largest manufacturers of cable systems, with products covering energy, communications, construction, and industrial specialty cables. Its robot/track cables and flexible cables meet the high-dynamic, torsion-resistant, oil-resistant, and chemical-resistant requirements of robotic applications.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| Flexibot / Robot Cables | High-flexibility power/control cables | Flexibot series | Industrial robots, collaborative robots |
| Afumex Cables | Low smoke zero halogen cables | Afumex Green Power | Construction, new energy |
| Sicon Cables | Industrial communication/data cables | Sicon series | Industrial networks, sensors |

## Representative Products

### Prysmian Group Flexibot Robot Cables

> Prysmian Group Flexibot Robot Cables: Please visit [Official Documentation](https://www.prysmiangroup.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Number of cores | Customizable (commonly 4G1.5 mm²) | Official catalog |
| Rated current | Not disclosed | Official datasheet |
| Rated voltage | 300/500 V | Product documentation |
| Protection rating | IP65 (finished cable assembly) | Product documentation |
| Torsion resistance | ±180°/m (typical) | Product documentation |
| Sheath material | PUR | Product documentation |
| Application scenarios | Industrial robots, collaborative robots, humanoid robot joints | Product documentation |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: PUR outer sheath is oil-resistant, abrasion-resistant, and bend-resistant, supporting torsion and drag chain movement, suitable for robot power and signal transmission.

**Application Scenarios**: Robot joints, welding robots, handling robots, collaborative robots, humanoid robot full-machine wiring.

### Prysmian Group Afumex Green Power Cable

> Prysmian Group Afumex Green Power Cable: Please visit [Official Documentation](https://www.prysmiangroup.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Number of cores | Customizable | Official catalog |
| Rated current | Not disclosed | Official datasheet |
| Rated voltage | 0.6/1 kV | Product documentation |
| Protection rating | IP not disclosed | Product documentation |
| Flame retardance/smoke density | Low smoke zero halogen | Product documentation |
| Application scenarios | Construction, new energy, charging facilities | Product documentation |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: Low smoke zero halogen, flame retardant, environmentally friendly, suitable for public buildings and new energy infrastructure.

**Application Scenarios**: Data centers, charging stations, building power distribution, new energy power stations.

## Supply Chain Position

- **Upstream Key Components/Materials**: Copper/aluminum conductors, XLPE/PVC/PUR insulation materials, shielding materials, armoring materials
- **Downstream Customers/Application Scenarios**: Power, communications, construction, new energy, robotics, automotive
- **Main Competitors/Benchmarks**: LEONI, Nexans, NKT, Lapp, Igus

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_prysmian`
- Product Entity: `ent_product_prysmian_flexibot`
- Component Entity: `ent_component_prysmian_flexibot`
- Key Relationships:
  - `rel_ent_company_prysmian_manufactures_ent_product_prysmian_flexibot` (`ent_company_prysmian` → `manufactures` → `ent_product_prysmian_flexibot`)
  - `rel_ent_company_prysmian_manufactures_ent_component_prysmian_flexibot` (`ent_company_prysmian` → `manufactures` → `ent_component_prysmian_flexibot`)

## References

1. [Official Website](https://www.prysmiangroup.com)
2. Product datasheets and public technical reports
3. [Appendix D Product Catalog](../index-products.md)
