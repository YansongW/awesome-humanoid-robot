# RoboSense E1R / RoboSense E1R

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Index](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [RoboSense / RoboSense](../companies/company_robosense.md) |
| **Product Category** | Solid-State LiDAR |
| **Release Date** | Launched with the E series in recent years |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [RoboSense Official Website](https://www.robosense.ai) |

## Product Overview

RoboSense E1R is a solid-state digital LiDAR that uses SPAD-SoC and 2D VCSEL technology, with no mechanical scanning components, designed for forward-facing and surround-view perception in robotics. The E1R features an ultra-wide field of view of 120°×90° and a close-range blind spot of less than 0.1 m, providing highly reliable 3D perception for humanoid robots, AMR/AGVs, lawn mowing robots, and unmanned delivery platforms.

The E1R is compact (69.5×95×43 mm, 330 g), consumes less than 10 W, and has an IP67/IP6K9K protection rating, making it suitable for complex indoor and outdoor environments. Its price is approximately USD 999, making it one of the mainstream solid-state LiDAR choices for cost-sensitive scenarios in the robotics industry.

## Product Image

> RoboSense E1R: Please visit the [official materials](https://www.robosense.ai) for details.

## Specification Table

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Dimensions | 69.5 mm × 95 mm × 43 mm | Official specs |
| Weight | 330 g (excluding cable) | Official specs |
| Depth Technology | Solid-state digital LiDAR (SPAD-SoC + 2D VCSEL) | Official specs |
| FOV | 120° × 90° | Official specs |
| Detection Range | 75 m (30 m @ 10% reflectivity) | Official specs |
| Point Rate | 260,000 points/sec (single echo); 520,000 points/sec (dual echo) | Official specs |
| Angular Resolution | 0.625° × 0.625° | Official specs |
| Blind Spot | <0.1 m | Official specs |
| Power Consumption | <10 W | Official specs |
| Protection Rating | IP67 / IP6K9K | Official specs |
| Price | Approx. USD 999 | Public information |

## Supply Chain Position

- **Manufacturer**: [RoboSense / RoboSense](../companies/company_robosense.md)
- **Core Components/Technology Source**: Self-developed SPAD-SoC, 2D VCSEL, optical system, and point cloud algorithms; semiconductor foundry and optical components sourced externally.
- **Downstream Applications/Customers**: Humanoid robots, AMR/AGVs, lawn mowing robots, unmanned delivery, industrial inspection.

## Knowledge Graph Nodes and Relationships

- Component Entity: `ent_component_robosense_e1r`
- Manufacturer Entity: `ent_company_robosense`
- Key Relationship:
  - `rel_ent_company_robosense_manufactures_ent_component_robosense_e1r` (`ent_company_robosense` → `manufactures` → `ent_component_robosense_e1r`)

## Application Scenarios

- **Humanoid Robots**: Head or torso surround-view/forward-facing solid-state LiDAR, providing 120°×90° 3D perception.
- **AMR/AGVs**: Indoor and outdoor navigation, obstacle avoidance, and shelf/pallet recognition.
- **Unmanned Delivery and Lawn Mowing Robots**: Low-cost, highly reliable short-range 3D perception.
- **Industrial Inspection**: Paired with quadruped or wheeled platforms for equipment and environment scanning.

## Competitive Comparison

| Comparison Item | RoboSense E1R | Hesai ET25 | Livox Mid-360 |
|-----------------|---------------|------------|---------------|
| Type | Solid-state LiDAR | Semi-solid/in-cabin LiDAR | Solid-state LiDAR |
| FOV | 120°×90° | 120°×25° | 360°×59° |
| Price | Approx. USD 999 | Not disclosed | Approx. USD 1,000 |
| Key Advantage | Solid-state, ultra-small blind spot, low cost | Ultra-thin long range, in-cabin installation | 360° surround view |

## References

1. [RoboSense Official Website](https://www.robosense.ai)
2. [RoboSense E1R Product Information](https://www.robosense.ai)
3. [The Robot Report – RoboSense LiDAR](https://www.therobotreport.com)
