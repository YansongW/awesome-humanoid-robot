# Percipio.XYZ

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).  
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 图漾科技 |
| **English Name** | Percipio.XYZ |
| **Headquarters** | Shanghai, China |
| **Founded** | 2015 |
| **Website** | [https://www.percipio.xyz](https://www.percipio.xyz) |
| **Supply Chain Role** | 3D Industrial Cameras, Machine Vision, Depth Sensing |
| **Enterprise Type** | Private Company, Independent 3D Machine Vision Supplier |
| **Parent Company/Group** | Independent |
| **Data Source** | Official website, public reports, distributor datasheets |

## Company Profile

Percipio.XYZ is a globally leading supplier of 3D industrial cameras, entering the industrial automation and logistics market with cost-effective active stereo/structure light cameras.

The company focuses on 3D machine vision hardware and supporting software solutions, with products covering the FM, FS, PM, PS series of industrial 3D cameras. Adopting an independent vision product supplier model, it provides equipment manufacturers and system integrators with cost-effective depth cameras, widely used in industrial sorting, grasping, measurement, inspection, and other scenarios.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| FM Series | Industrial 3D Cameras | FM811 / FM851 / FM855 | Industrial sorting, grasping, measurement |
| FS Series | Short-range High-precision Cameras | FS820 | Eye-in-hand, collaborative robots |
| PM/PS Series | ToF / Structure Light | PM801 / PS800 | Logistics, people counting, security |

## Representative Products

### Percipio.XYZ FM851-E2

> Percipio.XYZ FM851-E2: Please visit [Official Documentation](https://www.percipio.xyz) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | 125 mm × 85 mm × 30 mm | Distributor datasheet |
| Weight | 500 g | Distributor datasheet |
| Depth Technology | Active Stereo Structure Light | Official datasheet |
| Working Distance | 0.2 m – 1.0 m | Distributor datasheet |
| FOV (H/V) | 63° / 48° | Distributor datasheet |
| Depth Resolution | 1280 × 960 | Distributor datasheet |
| RGB Resolution | 2560 × 1920 | Distributor datasheet |
| Z-axis Accuracy | ±0.1 mm @ 200 mm | Distributor datasheet |
| Interface | Gigabit Ethernet / M8 Trigger | Distributor datasheet |
| Protection Rating | IP65 | Distributor datasheet |
| Price | Approx. USD 2,199 | Seeed Studio |

**Technical Highlights**: Million-level depth resolution, Gigabit Ethernet interface, IP65 protection, hard trigger and multi-camera fusion, suitable for industrial precision operations.

**Application Scenarios**: Robotic random bin picking, loading/unloading, industrial measurement, 3D inspection, Bin Picking.

### Percipio.XYZ FS820

> Percipio.XYZ FS820: Please visit [Official Documentation](https://www.percipio.xyz) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Working Distance | 0.3 m – 1.3 m | Seeed Studio |
| Depth Technology | Active Stereo Structure Light | Official datasheet |
| Frame Rate | 5 fps | Seeed Studio |
| RGB Resolution | 2 MP | Seeed Studio |
| Interface | Gigabit Ethernet | Official datasheet |
| Features | Compact size, suitable for eye-in-hand mounting | Official datasheet |
| Price | Approx. USD 749 | Seeed Studio |

**Technical Highlights**: Short-range high precision, small size, low power consumption, optimized for collaborative robot eye-in-hand scenarios.

**Application Scenarios**: Collaborative robot grasping, precision assembly, medical robots, flexible production lines.

## Supply Chain Position

- **Upstream Key Components/Materials**: CMOS sensors, lasers/projectors, industrial Ethernet chips, optical lenses, structure light algorithms
- **Downstream Customers/Application Scenarios**: Industrial robots, collaborative robots, logistics automation, 3C/semiconductor inspection, medical equipment
- **Main Competitors/Peers**: Orbbec, Hikrobot, Intel RealSense, Cognex, Keyence

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_percipio`
- Product Entity: `ent_component_percipio_fm851_e2`
- Product Entity: `ent_component_percipio_fs820`
- Key Relationships:
  - `ent_company_percipio` -- `manufactures` --> `ent_component_percipio_fm851_e2`
  - `ent_company_percipio` -- `manufactures` --> `ent_component_percipio_fs820`

## References

1. [Official Website](https://www.percipio.xyz)
2. [Product Documentation and Public Reports](https://www.percipio.xyz)
3. [Appendix D Product Catalog](../index-products.md)
