# Hexagon

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 海克斯康 |
| **English Name** | Hexagon |
| **Headquarters** | Stockholm, Sweden |
| **Founded** | 1975 (predecessor as Hexagon AB, transformed in the 1990s) |
| **Website** | [https://hexagon.com](https://hexagon.com) |
| **Supply Chain Role** | Precision measurement, coordinate measuring machines, industrial software, smart manufacturing, sensors |
| **Enterprise Type** | Publicly listed company (OMX: HEXA B), global leader in metrology and industrial software |
| **Parent/Group** | None (Hexagon AB is the listed entity) |
| **Data Source** | Hexagon official website, annual reports, product manuals, public press releases |

## Company Overview

Hexagon is a world-leading provider of digital reality solutions, enabling geometric measurement and quality control of robot components and complete machines through high-precision measurement, sensors, and industrial software.

Hexagon's business covers measurement technology (coordinate measuring machines, portable measuring arms, laser trackers), geospatial information technology, and industrial software (MSC, Simufact, Romax, etc.). In the robotics field, Hexagon's high-precision coordinate measuring machines and optical measurement systems are widely used for calibration of joints, reducers, links, and complete machine accuracy.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Coordinate Measuring Machines | High-precision geometric measurement | GLOBAL / Leitz / TIGO | Automotive parts, aerospace, robot components |
| Portable Measurement & Scanning | On-site dimensional inspection & reverse engineering | ROMER measuring arm / Leica laser tracker | Assembly, production line inspection, robot calibration |
| Industrial Software | Simulation & manufacturing intelligence | MSC Adams / Simufact / Q-DAS | Robot dynamics simulation, process optimization |

## Representative Products

### Hexagon Coordinate Measuring Machine / GLOBAL Series

> Hexagon Coordinate Measuring Machine / GLOBAL Series: Please visit [official documentation](https://hexagon.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Measuring Range | 500×700×500 mm to 2000×4000×1500 mm, multiple specifications | Hexagon product manual |
| Accuracy | MPE_E approx. 1.5 + L/350 µm (varies by model) | Hexagon product manual |
| Probing System | HP-S-X5 / HH-T / touch-trigger probe | Hexagon product manual |
| Software | PC-DMIS / QUINDOS | Hexagon official website |
| Structure | Granite worktable, air bearing guides, steel bridge | Hexagon product manual |
| Temperature Compensation | Automatic temperature compensation | Hexagon product manual |
| Interface | USB / Ethernet | Hexagon product manual |
| Price | Not disclosed | - |

**Technical Highlights**: High precision and stability, rich probe and software ecosystem, widely used for automotive and aerospace-grade component inspection.

**Application Scenarios**: Robot joint/reducer geometric inspection, automotive parts, aerospace structural components, mold inspection.

### Hexagon ROMER Portable Measuring Arm

> Hexagon ROMER Portable Measuring Arm: Please visit [official documentation](https://hexagon.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Measuring Range | 1.8 m – 4.5 m (arm length) | Hexagon product manual |
| Accuracy | Spatial accuracy ±0.020–±0.060 mm (varies by model) | Hexagon product manual |
| Probe | Touch-trigger / scanning / laser scanning probe | Hexagon product manual |
| Degrees of Freedom | 6-axis / 7-axis | Hexagon product manual |
| Software | PC-DMIS Portable | Hexagon official website |
| Portability | Field-deployable, no air supply required | Hexagon product manual |
| Interface | USB / Wi-Fi | Hexagon product manual |
| Price | Not disclosed | - |

**Technical Highlights**: On-site rapid inspection, no need for temperature-controlled workshop, supports scanning and reverse engineering, suitable for production line spot checks and robot calibration.

**Application Scenarios**: Complete robot assembly inspection, welding fixture inspection, casting/sheet metal part dimensional verification, reverse engineering.

## Supply Chain Position

- **Upstream Key Components/Materials**: High-precision linear encoders, air bearings, granite, probe sensors, industrial software IP.
- **Downstream Customers/Application Scenarios**: Automotive, aerospace, electronics, medical, robot component and complete machine manufacturers.
- **Main Competitors/Peers**: ZEISS, Wenzel, FARO, Nikon Metrology.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_hexagon`
- Product Entities: `ent_product_hexagon_cmm`, `ent_product_hexagon_romer_arm`
- Key Relationships:
  - `ent_company_hexagon` -- `manufactures` --> `ent_product_hexagon_cmm`
  - `ent_company_hexagon` -- `manufactures` --> `ent_product_hexagon_romer_arm`
  - `ent_product_hexagon_cmm` -- `uses` --> `ent_component_linear_encoder`
  - `ent_product_hexagon_romer_arm` -- `uses` --> `ent_component_probe_sensor`

## References

1. [Official Website](https://hexagon.com)
2. [Hexagon Official Website](https://hexagon.com)
3. Hexagon GLOBAL Series and ROMER product manuals
