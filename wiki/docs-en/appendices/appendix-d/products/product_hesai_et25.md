# Hesai ET25

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Index](../index-products.md)
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Hesai Technology / Hesai](../companies/company_hesai.md) |
| **Product Category** | Automotive-grade LiDAR |
| **Release Date** | 2023 |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [Hesai Technology Official Website](https://www.hesaitech.com) |

## Product Overview

The Hesai ET25 is an ultra-thin in-cabin LiDAR with a body thickness of only 25 mm. It can be installed behind the windshield of passenger vehicles, balancing ADAS forward long-range perception with vehicle styling design. The ET25 uses a 905 nm automotive-grade LiDAR solution, featuring a 120°(H) × 25°(V) field of view. Even behind the windshield, it achieves a detection range of 225 m (10% reflectivity target).

The ET25 is characterized by low power consumption (12 W) and low noise (<25 dB), making it suitable for passenger vehicle applications sensitive to power consumption and in-cabin noise. With a point rate exceeding 3 million points per second and an angular resolution of 0.05° × 0.05°, it provides dense and accurate 3D perception data for advanced intelligent driving and long-range robot navigation.

## Product Image

> Hesai ET25: Please visit the [official materials](https://www.hesaitech.com) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Thickness 25 mm | Official specs |
| Weight | Not disclosed | - |
| Depth Technology | 905 nm automotive-grade LiDAR | Official specs |
| FOV | 120°(H) × 25°(V) | Official specs |
| Detection Range | 250 m @ 10% reflectivity (without windshield); 225 m (behind windshield) | Official specs |
| Point Rate | >3 million points/second | Official specs |
| Angular Resolution | 0.05° × 0.05° | Official specs |
| Power Consumption | 12 W | Official specs |
| Noise | <25 dB (in-cabin) | Official specs |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Hesai Technology / Hesai](../companies/company_hesai.md)
- **Core Components/Technology Source**: Self-developed laser emission/reception modules, scanning mechanism, SPAD receiving chip, and point cloud algorithms; optical components and PCBs are outsourced.
- **Downstream Applications/Customers**: Passenger vehicle ADAS, autonomous driving, high-end robot long-range navigation.

## Knowledge Graph Nodes and Relationships

- Component entity: `ent_component_hesai_et25`
- Manufacturer entity: `ent_company_hesai`
- Key relationships:
  - `rel_ent_company_hesai_manufactures_ent_component_hesai_et25` (`ent_company_hesai` → `manufactures` → `ent_component_hesai_et25`)

## Application Scenarios

- **Passenger Vehicle ADAS**: Forward long-range perception, supporting highway NOA and urban navigation assistance.
- **Autonomous Driving Robotaxi**: In-cabin installation behind the windshield, balancing styling and perception performance.
- **High-end Robots**: Long-range navigation and obstacle avoidance for humanoid robots, unmanned vehicles, and other platforms.

## Competitive Comparison

| Comparison Item | Hesai ET25 | RoboSense M1 Plus | Livox HAP |
|-----------------|------------|-------------------|-----------|
| Type | Semi-solid / In-cabin LiDAR | Semi-solid LiDAR | Semi-solid LiDAR |
| Thickness | 25 mm | Not disclosed | Not disclosed |
| Detection Range | 250 m @ 10% | 180 m @ 10% | 150 m @ 10% |
| Core Advantage | Ultra-thin in-cabin, low noise | Cost and mass production | Large FOV, high reliability |

## Selection and Deployment Recommendations

- Passenger vehicle customers need to confirm with Tier 1/OEM the compatibility, calibration, and cleaning system solutions for the ET25 and windshield.
- Robot customers using in-cabin/in-body installations should verify the impact of heat dissipation, EMC, and structural resonance.

## References

1. [Hesai Technology Official Website](https://www.hesaitech.com)
2. [Hesai ET25 Product Materials](https://www.hesaitech.com)
3. [The Robot Report – Hesai LiDAR](https://www.therobotreport.com)
