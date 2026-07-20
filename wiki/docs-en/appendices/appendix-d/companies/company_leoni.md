# LEONI

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed".

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 莱尼 |
| **English Name** | LEONI |
| **Headquarters** | Nuremberg, Germany |
| **Founded** | 1917 |
| **Website** | [https://www.leoni.com](https://www.leoni.com) |
| **Supply Chain Role** | Cables, Wiring Harnesses, Connection Systems |
| **Company Type** | Publicly listed (XETRA: LEO) |
| **Parent Company/Group** | Independently listed |
| **Data Source** | Official website, annual reports, product catalog |

## Company Profile

LEONI is a globally leading supplier of cables and wiring harness systems, covering automotive, industrial, medical, and communication sectors. Its Dacar data cables, robot cables, and custom wiring harnesses meet the wiring requirements of humanoid robots for high flexibility, torsion resistance, oil resistance, and bend resistance.

## Product Lines

| Product Line | Positioning | Representative Product | Application Area |
|--------------|-------------|------------------------|------------------|
| Dacar Data Cables | In-vehicle/industrial data communication | Dacar 302 | ADAS, robot sensor networks |
| Robot Cables | High-flexibility power/control cables | LEONI Robotic Cable | Industrial robots, collaborative robots |
| Wiring Harness Systems | Complete vehicle/machine wiring harnesses | Custom wiring harnesses | Automotive, humanoid robot OEMs |

## Representative Products

### LEONI Dacar® 302 Automotive Ethernet Cable

> LEONI Dacar® 302 Automotive Ethernet Cable: Please visit [official materials](https://www.leoni.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Number of cores | 1 pair (2 cores) | Official catalog |
| Rated current | Not disclosed | Official datasheet |
| Rated voltage | Not disclosed | Official datasheet |
| Transmission rate | 100 Mbps (100BASE-T1) | Official catalog |
| Temperature range | -40°C ~ +105°C | Official catalog |
| Shielding | Overall shielding | Product documentation |
| Application scenarios | In-vehicle/robot sensor networks, cameras, LiDAR | Product documentation |
| Price | Not disclosed | Not disclosed |

**Technical highlights**: Designed for single-pair Ethernet, lightweight, high-temperature resistant, well-shielded, suitable for long-distance data communication in robots.

**Application scenarios**: Autonomous driving/robot sensor bus, industrial cameras, LiDAR, domain controller interconnection.

### LEONI High-Flexibility Robot Cable

> LEONI High-Flexibility Robot Cable: Please visit [official materials](https://www.leoni.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Number of cores | Custom (commonly 4G0.75 mm²) | Official catalog |
| Rated current | Not disclosed | Official datasheet |
| Rated voltage | 300/500 V | Product documentation |
| Protection rating | IP40 (cable body, depends on connector) | Product documentation |
| Bending life | Not disclosed | Official datasheet |
| Application scenarios | Robot joints, cable carriers, servo motor connections | Product documentation |
| Price | Not disclosed | Not disclosed |

**Technical highlights**: High flexibility, torsion resistance, oil resistance, flame retardant, suitable for continuous motion robot joints and cable carrier wiring.

**Application scenarios**: Industrial robots, collaborative robots, humanoid robot joints, CNC machine cable carriers.

## Supply Chain Position

- **Upstream key components/materials**: Copper rod, PVC/TPE/PUR insulation materials, aluminum foil/braided shielding, connectors
- **Downstream customers/application scenarios**: Automotive OEMs, robot OEMs, industrial automation, medical equipment
- **Main competitors/benchmarks**: Prysmian, Nexans, Lapp, Igus, Coroplast

## Knowledge Graph Nodes and Relationships

- Company entity: `ent_company_leoni`
- Product entity: `ent_product_leoni_dacar_302`
- Component entity: `ent_component_leoni_dacar_302`
- Key relationships:
  - `rel_ent_company_leoni_manufactures_ent_product_leoni_dacar_302` (`ent_company_leoni` → `manufactures` → `ent_product_leoni_dacar_302`)
  - `rel_ent_company_leoni_manufactures_ent_component_leoni_dacar_302` (`ent_company_leoni` → `manufactures` → `ent_component_leoni_dacar_302`)

## References

1. [Official website](https://www.leoni.com)
2. Product datasheets and public technical reports
3. [Appendix D Product Catalog](../index-products.md)
