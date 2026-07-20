# CATL Qilin Battery

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [CATL / CATL](../companies/company_catl.md) |
| **Product Category** | Power Battery System (CTP 3.0) |
| **Release Date** | 2022 |
| **Status** | Mass Production / Commercial |
| **Official Website / Source** | [CATL Qilin Battery Press Release](https://www.catl.com/en/news/958.html) |

## Product Overview

The Qilin Battery is CATL's third-generation CTP (Cell to Pack) power battery system. By eliminating the module structure and directly integrating cells into the battery pack, it achieves a volume utilization rate exceeding 72% and an energy density of over 255 Wh/kg. The Qilin Battery supports 4C fast charging, enabling a charge from 10% to 80% in 10 minutes, and features a multi-functional elastic interlayer integrated with a water-cooling plate design to enhance heat dissipation and safety performance.

Although the Qilin Battery is primarily aimed at the passenger car market, its high energy density, fast charging capability, and cost advantages at scale make it a potential battery solution for mobile platforms such as humanoid robots and quadruped robots. Several robot manufacturers have adopted the Qilin Battery as a high-endurance power source in prototype or concept designs.

## Product Image

> CATL Qilin Battery: Please visit [Official Materials](https://www.catl.com/en/news/958.html) for details.

## Specification Table

| Specification | Value | Remarks / Source |
|---------------|-------|------------------|
| Technology Route | LFP / NCM CTP 3.0 | CATL Official |
| Volume Utilization | >72% | CATL Official |
| Energy Density | >255 Wh/kg | CATL Official |
| Fast Charging Capability | 4C; 10%–80% in 10 min | CATL Official |
| Range | Up to 1000 km (passenger car application) | CATL Official |
| Cooling Method | Integrated water-cooling plate design | CATL Official |
| Dimensions / Weight | Varies by vehicle model / application | Not disclosed |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [CATL / CATL](../companies/company_catl.md)
- **Core Components / Technology Source**: Self-developed cells, CTP structure, BMS and thermal management system; cathode/anode materials, separators, and electrolytes are supplied by the supply chain.
- **Downstream Applications / Customers**: Passenger car OEMs, energy storage systems, some robot / unmanned platform prototypes.

## Knowledge Graph Nodes and Relationships

- Component Entity: `ent_component_catl_qilin_battery`
- Manufacturer Entity: `ent_company_catl`
- Key Relationships:
  - `rel_ent_company_catl_manufactures_ent_component_catl_qilin_battery` (`ent_company_catl` → `manufactures` → `ent_component_catl_qilin_battery`)

## Application Scenarios

- **New Energy Vehicles**: High-endurance, fast-charging battery pack solutions for passenger cars and commercial vehicles.
- **Energy Storage Systems**: Energy storage for grid-side and user-side storage stations.
- **Robots / Unmanned Platforms**: High energy density power source for humanoid robots, quadruped robots, and unmanned vehicles (prototype / concept).

## Competitive Comparison

| Comparison Item | CATL Qilin Battery | BYD Blade Battery | EVE Energy LF280K |
|-----------------|--------------------|-------------------|-------------------|
| Technology Route | CTP 3.0 | CTP / Blade | LFP Prismatic |
| Volume Utilization | >72% | Not disclosed | Not disclosed |
| Fast Charging | 4C (10–80% in 10 min) | High fast-charge version | 1C–2C primarily |
| Core Advantage | Energy density, fast charging, scalability | Safety, cost | Cost and production capacity |

## Selection and Deployment Recommendations

- If robots / unmanned platforms plan to adopt the Qilin Battery, they should confirm cell specifications, BMS interfaces, and thermal management solutions with CATL or integrators.
- Passenger car customers should pay attention to battery pack compatibility, warranty terms, and fast-charging infrastructure matching from vehicle manufacturers.

## References

1. [CATL – Qilin Battery Press Release](https://www.catl.com/en/news/958.html)
2. [CATL Official Website](https://www.catl.com)
3. [CATL Qilin Battery Technology Analysis](https://www.catl.com)
