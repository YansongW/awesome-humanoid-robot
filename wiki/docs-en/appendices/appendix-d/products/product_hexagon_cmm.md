# Hexagon Coordinate Measuring Machine

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Hexagon / Hexagon](../companies/company_hexagon.md) |
| **Product Category** | Precision geometric measurement equipment |
| **Release Date** | Continuously iterated; GLOBAL series is a classic product line |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | See references in the main text |

## Product Overview

The Hexagon Coordinate Measuring Machine (CMM) is core equipment in the field of industrial metrology, using contact probes to obtain workpiece geometric dimensions and form and position tolerances within a three-dimensional space. As Hexagon's classic bridge-type CMM, the GLOBAL series is widely used for precision inspection and quality control of core components such as robot joints, reducers, and connecting rods, thanks to its high accuracy, high stability, and rich probe/software ecosystem.

## Product Image

> Hexagon Coordinate Measuring Machine: Please visit [Official Materials](https://hexagon.com/products/coordinate-measuring-machines) for details.

## Specification Parameter Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Measuring Range | 500×700×500 mm to 2000×4000×1500 mm | Hexagon Product Manual |
| Accuracy | MPE_E approx. 1.5 + L/350 µm (varies by model) | Hexagon Product Manual |
| Probing System | HP-S-X5 / HH-T / Touch-trigger probe | Hexagon Product Manual |
| Software | PC-DMIS / QUINDOS | Hexagon Official Website |
| Structure | Granite worktable, air bearing guideways, steel bridge | Hexagon Product Manual |
| Temperature Compensation | Automatic temperature compensation | Hexagon Product Manual |
| Interface | USB / Ethernet | Hexagon Product Manual |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Hexagon / Hexagon](../companies/company_hexagon.md)
- **Core Components/Technology Sources**: High-precision linear encoders, air bearings, granite, probe sensors, industrial software.
- **Downstream Applications/Customers**: Automotive parts, aerospace, electronics, medical devices, robot component manufacturers.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_hexagon_cmm`
- Manufacturer Entity: `ent_company_hexagon`
- Key Relationships:
  - `rel_ent_company_hexagon_manufactures_ent_product_hexagon_cmm` (`ent_company_hexagon` → `manufactures` → `ent_product_hexagon_cmm`)
  - `ent_product_hexagon_cmm` -- `uses` --> `ent_component_linear_encoder`
  - `ent_product_hexagon_cmm` -- `measures` --> `ent_component_robot_gearbox`

## Application Scenarios

- **Robot Joint Inspection**: Measuring geometric accuracy of joint housings, output flanges, and bearing bores.
- **Reducer Inspection**: Measurement of tooth profile and position accuracy for gears, cycloidal discs, and pinwheel housings.
- **Machine Calibration**: Calibration of robot link parameters and DH parameters in conjunction with measuring arms.

## Competitive Comparison

| Comparison Item | Hexagon GLOBAL | ZEISS PRISMO | Wenzel LH |
|----------------|----------------|--------------|-----------|
| Accuracy Level | Micrometer level | Sub-micrometer level | Micrometer level |
| Software | PC-DMIS | CALYPSO | WM | Quartis |
| Advantage | Ecosystem and stability | Highest accuracy | Cost-effectiveness |

## Selection and Deployment Recommendations

- Select the corresponding model based on computing power/accuracy/scenario requirements, prioritizing official toolchain and ecosystem compatibility.
- Confirm before deployment that power supply, cooling, mechanical interfaces, and communication protocols meet the overall system requirements.
- It is recommended to obtain the latest firmware, SDK, and technical support through official channels or authorized distributors.

## Related Entries

- [Manufacturer: Hexagon / Hexagon](../companies/company_hexagon.md)
- [Appendix D.4 Key Product Wiki](../index-products.md)

## References

1. [Hexagon / Hexagon Official Product/Company Page](https://hexagon.com/products/coordinate-measuring-machines)
2. [Hexagon Official Website](https://hexagon.com)
3. Hexagon GLOBAL Series Technical Manual
