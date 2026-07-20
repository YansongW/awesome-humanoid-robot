# RoboSense

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).  
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 速腾聚创 |
| **English Name** | RoboSense |
| **Headquarters** | Shenzhen, China |
| **Founded** | 2014 |
| **Website** | [https://www.robosense.ai](https://www.robosense.ai) |
| **Supply Chain Role** | LiDAR, Robot Vision, AI Perception Chips |
| **Company Type** | Listed Company (HKEX: 2498), AI-driven Robotics Technology Company |
| **Parent Company/Group** | Independently Listed |
| **Data Source** | Official Website, Prospectus, Public Financial Reports and News |

## Company Overview

RoboSense is a global leader in LiDAR market share, specializing in digital LiDAR chips and robot perception solutions.

Leveraging self-developed SPAD-SoC, VCSEL, and driver chips, RoboSense offers all-solid-state digital LiDAR covering ADAS and robotics fields. Products like the E1R have been widely deployed in scenarios such as lawn mowing robots, autonomous delivery, and humanoid robots.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| M Series | Automotive-grade MEMS LiDAR | M1 / M1 Plus / M3 | Passenger Vehicle ADAS |
| E Series | All-solid-state Digital LiDAR | E1 / E1R | Robotics, AMR, Lawn Mowers, Humanoid Robots |
| Perception Software | HyperVision | RS-LiDAR-Perception | Autonomous Driving, Robot Perception |

## Representative Products

### RoboSense E1R

> RoboSense E1R: Please visit [Official Materials](https://www.robosense.ai) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | 69.5 × 95 × 43 mm | Official Store |
| Weight | 330 g (excluding cable) | Official Store |
| Depth Technology | All-solid-state Digital LiDAR (SPAD-SoC + 2D VCSEL) | Official Datasheet |
| FOV | 120° × 90° | Official Datasheet |
| Detection Range | 75 m (30 m @ 10% reflectivity) | Official Datasheet |
| Point Rate | 260,000 points/s (single echo); 520,000 points/s (dual echo) | Official Datasheet |
| Angular Resolution | 0.625° × 0.625° | Official Datasheet |
| Blind Zone | <0.1 m | Official Datasheet |
| Power Consumption | <10 W | Official Datasheet |
| Protection Rating | IP67 / IP6K9K | Official Datasheet |
| Price | Approx. USD 999 | Official Store |

**Technical Highlights**: All-solid-state with no mechanical scanning, ultra-wide FOV, small blind zone, automotive-grade reliability, designed for forward/surround perception in robotics.

**Application Scenarios**: Humanoid Robots, AMR/AGV, Lawn Mowing Robots, Autonomous Delivery, Industrial Inspection.

### RoboSense M1 Plus

> RoboSense M1 Plus: Please visit [Official Materials](https://www.robosense.ai) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Depth Technology | MEMS Semi-solid-state LiDAR | Official Datasheet |
| FOV | 120°(H) × 25°(V) | Official Datasheet |
| Detection Range | 180 m @ 10% reflectivity | Official Datasheet |
| Angular Resolution | 0.1° × 0.1° | Official Datasheet |
| Point Rate | Not disclosed | Not disclosed |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: Automotive-grade MEMS solution, mass-produced in multiple vehicle models, suitable for forward primary LiDAR in passenger cars.

**Application Scenarios**: Passenger Vehicle ADAS, Robotaxi, Long-haul Logistics.

## Supply Chain Position

- **Upstream Key Components/Materials**: VCSEL Lasers, SPAD-SoC Chips, Driver ICs, Optical Lenses, MEMS Micromirrors
- **Downstream Customers/Application Scenarios**: Passenger Vehicle OEMs (BYD, XPeng, Geely, etc.), Humanoid Robots, AMR, Autonomous Delivery, Lawn Mowing Robots
- **Main Competitors/Peers**: Hesai Technology, Livox, Huawei, Ouster, Luminar, Innovusion

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_robosense`
- Product Entity: `ent_component_robosense_e1r`
- Product Entity: `ent_component_robosense_m1_plus`
- Key Relationships:
  - `ent_company_robosense` -- `manufactures` --> `ent_component_robosense_e1r`
  - `ent_company_robosense` -- `manufactures` --> `ent_component_robosense_m1_plus`

## References

1. [Official Website](https://www.robosense.ai)
2. [Product Materials and Public Reports](https://www.robosense.ai)
3. [Appendix D Product Catalog](../index-products.md)
