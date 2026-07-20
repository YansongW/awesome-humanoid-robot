# Livox Technology

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 览沃 |
| **English Name** | Livox Technology |
| **Headquarters** | Shenzhen, China |
| **Founded** | 2016 |
| **Website** | [https://www.livoxtech.com](https://www.livoxtech.com) |
| **Supply Chain Role** | LiDAR, Hybrid Solid-State LiDAR, Robot 3D Perception |
| **Company Type** | Private Company, Independent Company Incubated by DJI |
| **Parent Company/Group** | Incubated by DJI / Independently Operated |
| **Data Source** | Official Website, DJI/Livox Public Materials, Product Datasheets |

## Company Profile

Livox Technology is a LiDAR company incubated by DJI, entering the robot and autonomous driving market with cost-effective hybrid solid-state LiDAR.

Livox is dedicated to providing high-performance, low-cost LiDAR sensors, utilizing a unique rotating mirror hybrid solid-state scanning technology. The Mid-360, with its 360° surround view, small size, and lightweight design, has become a popular choice for robot SLAM and navigation, and has been applied to quadruped robots, cleaning robots, and AMRs.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Mid Series | Robot 360° LiDAR | Mid-360 / Mid-360S / Mid-70 | AMR, Quadruped Robots, Cleaning Robots, SLAM |
| HAP / Horizon | Automotive-grade LiDAR | HAP / Horizon / Tele-15 | Autonomous Driving, Passenger Vehicles |
| Avia | Surveying-grade LiDAR | Avia | Drone Surveying, 3D Modeling |

## Representative Products

### Livox Mid-360

> Livox Mid-360: Please visit [Official Materials](https://www.livoxtech.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | 65 mm × 65 mm × 60 mm | Official Datasheet |
| Weight | 265 g | Official Datasheet |
| Laser Wavelength | 905 nm | Official Datasheet |
| Laser Safety Class | Class 1 (IEC60825-1:2014) | Official Datasheet |
| FOV | Horizontal 360°; Vertical -7° ~ 52° | Official Datasheet |
| Detection Range | 40 m @ 10% Reflectivity; 70 m @ 80% Reflectivity | Official Datasheet |
| Point Rate | 200,000 points/sec (First Return) | Official Datasheet |
| Frame Rate | 10 Hz (Typical) | Official Datasheet |
| Ranging Accuracy | ≤2 cm @ 10 m; ≤3 cm @ 0.2 m | Official Datasheet |
| IMU | Built-in ICM40609 | Official Datasheet |
| Interface | 100 BASE-TX Ethernet | Official Datasheet |
| Power Consumption | 6.5 W (Typical) | Official Datasheet |
| Price | Approx. CNY 3,999 | Official Online Store |

**Technical Highlights**: 360° surround view, ultra-compact size, built-in IMU, IP67 protection, a mainstream choice for robot SLAM and navigation.

**Application Scenarios**: AMR/AGV Navigation, Quadruped Robots, Cleaning Robots, Lawn Mowing Robots, 3D Surveying.

### Livox HAP

> Livox HAP: Please visit [Official Materials](https://www.livoxtech.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| FOV | 120°(H) × 30°(V) | Official Datasheet |
| Detection Range | 150 m @ 10% Reflectivity | Official Datasheet |
| Point Rate | 240,000 points/sec | Official Datasheet |
| Angular Resolution | 0.18°(H) × 0.23°(V) | Official Datasheet |
| Scanning Method | Hybrid Solid-State (Rotating Mirror) | Official Datasheet |
| Protection Rating | IP67 | Official Datasheet |
| Price | Not Disclosed | Not Disclosed |

**Technical Highlights**: Automotive-grade hybrid solid-state LiDAR, already mass-produced for several passenger vehicle models, balancing long-range detection and reliability.

**Application Scenarios**: Passenger Vehicle ADAS, Robotaxi, High-end Mobile Robots.

## Supply Chain Position

- **Upstream Key Components/Materials**: 905 nm Laser, SPAD/APD, Scanning Motor, Optical Lenses, Main Control SoC, IMU
- **Downstream Customers/Applications**: AMR/AGV, Quadruped Robots (e.g., Deep Robotics Jueying X30), Cleaning Robots, Lawn Mowing Robots, Autonomous Driving
- **Main Competitors/Peers**: Hesai Technology, RoboSense, Ouster, Velodyne, RoboSense

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_livox`
- Product Entity: `ent_component_livox_mid_360`
- Product Entity: `ent_component_livox_hap`
- Key Relationships:
  - `ent_company_livox` -- `manufactures` --> `ent_component_livox_mid_360`
  - `ent_company_livox` -- `manufactures` --> `ent_component_livox_hap`
  - `ent_company_livox` -- `supplies` --> `ent_company_deep_robotics` (Deep Robotics Jueying X30 Quadruped Robot Equipped with Livox Mid-360)

## References

1. [Official Website](https://www.livoxtech.com)
2. [Product Materials and Public Reports](https://www.livoxtech.com)
3. [Appendix D Product Catalog](../index-products.md)
