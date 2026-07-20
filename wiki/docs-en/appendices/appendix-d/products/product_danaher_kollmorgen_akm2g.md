# Kollmorgen AKM2G Servo Motor / AKM2G

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Danaher (Kollmorgen)](../companies/company_danaher.md) |
| **Product Category** | Servo Motor |
| **Release Date** | 2018 |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [Danaher (Kollmorgen) Official Website](https://www.danaher.com) |

## Product Overview

The Kollmorgen AKM2G is a new generation synchronous servo motor launched by Kollmorgen under Danaher, offering higher torque density and richer configuration options.

The motor covers frame sizes from 40 mm to 180 mm, with optional multiple feedback devices and windings. When paired with the AKD servo drive, it enables plug-and-play functionality and is widely used in robotics, semiconductors, and precision automation equipment.

## Product Image

> Kollmorgen AKM2G Servo Motor: Please visit the [official documentation](https://www.danaher.com) for details.

## Specification Table

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Product Type | Synchronous Servo Motor | Official documentation |
| Power Range | 0.03 kW ~ 7.2 kW (specific range depends on model) | Official documentation |
| Peak Torque | 0.16 Nm ~ 53 Nm | Official documentation |
| Maximum Speed | 8,000 rpm | Official documentation |
| Frame Size | 40 / 60 / 80 / 130 / 180 mm | Official documentation |
| Feedback Type | Resolver / Incremental / Single-turn or Multi-turn Absolute Encoder | Official documentation |
| Protection Rating | IP65 (optional shaft seal) | Official documentation |
| Price | Not disclosed | Not disclosed |

## Supply Chain Position

- **Manufacturer**: [Danaher (Kollmorgen)](../companies/company_danaher.md)
- **Core Components/Technology Source**: Self-developed motor design and magnetic circuit optimization; magnetic materials, bearings, encoders, and winding insulation materials are externally sourced.
- **Downstream Applications/Customers**: Industrial robots, collaborative robots, semiconductor equipment, packaging machinery, humanoid robot joints.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_danaher_kollmorgen_akm2g`
- Manufacturer Entity: `ent_company_danaher`
- Key Relationship:
  - `ent_company_danaher` → `manufactures` → `ent_product_danaher_kollmorgen_akm2g` (Relationship file: `rel_ent_company_danaher_manufactures_ent_product_danaher_kollmorgen_akm2g.md`)

## Application Scenarios

- **Industrial Robots**: Joint servo and external axes.
- **Collaborative Robots**: Low inertia, high safety joint power.
- **Semiconductor Equipment**: Wafer handling and precision positioning.
- **Humanoid Robots**: Arm, leg, and waist joint power units.

## Competitive Comparison

| Comparison Item | Kollmorgen AKM2G Servo Motor | Panasonic MINAS A6 | Yaskawa Σ-7 |
|-----------------|-------------------------------|--------------------|-------------|
| Frame Size | 40–180 mm | Not disclosed | Not disclosed |
| Peak Torque | 0.16–53 Nm | Not disclosed | Not disclosed |
| Maximum Speed | 8,000 rpm | Not disclosed | Not disclosed |
| Price | Not disclosed | Not disclosed | Not disclosed |

## Selection and Deployment Recommendations

In robotic joint applications requiring high torque density and custom windings, the AKM2G can be prioritized; during selection, ensure compatibility of the mounting flange, feedback type, and drive.

## References

1. [Danaher (Kollmorgen) Official Website](https://www.danaher.com)
2. [Kollmorgen AKM2G Servo Motor Product Page](https://www.kollmorgen.com/en-us/products/motors/servo-motors/akm2g-servo-motors)
3. Kollmorgen AKM2G Servo Motor Datasheet
