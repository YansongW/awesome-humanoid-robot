# DEEP Robotics Jueying X30

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update date: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [DEEP Robotics](../companies/company_deep_robotics.md) |
| **Product Category** | Industrial-grade Quadruped Robot |
| **Release Date** | October 2023 |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [DEEP Robotics X30 Product Page](https://deeprobotics.cn/robot/index/x30.html) |

## Product Overview

The Jueying X30 is a flagship quadruped robot from DEEP Robotics designed for industrial applications, focusing on scenarios such as power inspection, emergency rescue, fire reconnaissance, pipe gallery tunnels, and industrial surveying. The X30 features IP67 industrial-grade protection, operates in temperatures ranging from -20°C to 55°C, and supports fusion perception autonomous navigation in dim, bright, flickering, or even lightless environments.

The X30 weighs 56 kg, has a maximum speed of no less than 4 m/s, can overcome obstacles up to 20 cm, and climb stairs and slopes of 45°. Its battery supports quick field swapping, and the payload endurance has increased by 25% compared to the previous generation, with a range of no less than 10 km. With high protection, strong obstacle-crossing capability, and long endurance, the X30 has been deployed in power, metallurgy, mining, and emergency rescue projects both domestically and internationally.

## Product Image

> DEEP Robotics Jueying X30: Please visit the [official page](https://deeprobotics.cn/robot/index/x30.html) for details.

## Specification Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Dimensions | Standing dimensions 1000×695×470 mm | Official specifications |
| Weight | 56 kg | Official specifications |
| Degrees of Freedom (Total) | 12 DOF (3 DOF per leg) | Quadruped structure |
| Key Performance Indicators | Max speed ≥4 m/s; Climbing ≤45°; Obstacle crossing ≥20 cm | Official specifications |
| Payload Capacity | Effective payload ≥20 kg; Maximum payload up to 50 kg | Public information |
| Endurance | 2.5–4 h; Range ≥10 km | Official specifications |
| Protection Rating | IP67 | Official specifications |
| Operating Temperature | -20°C to 55°C | Official specifications |
| Price | Not disclosed (Industrial-grade customized solution) | - |

## Supply Chain Position

- **Manufacturer**: [DEEP Robotics](../companies/company_deep_robotics.md)
- **Core Components/Technology Source**: Self-developed high-torque joints (J80/J100), fusion perception system, motion control algorithms; LiDAR, depth cameras, batteries are outsourced.
- **Downstream Applications/Customers**: State Grid, China Southern Power Grid, Baosteel, Fluke, emergency rescue and fire departments.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_deep_robotics_x30`
- Manufacturer Entity: `ent_company_deep_robotics`
- Key Relationships:
  - `rel_ent_company_deep_robotics_manufactures_ent_product_deep_robotics_x30` (`ent_company_deep_robotics` → `manufactures` → `ent_product_deep_robotics_x30`)

## Application Scenarios

- **Power Inspection**: Equipment status, infrared temperature measurement, and meter identification in substations, transmission corridors, and distribution rooms.
- **Emergency Rescue**: Reconnaissance, search and rescue, and environmental monitoring in earthquake, explosion, and fire scenarios.
- **Industrial Inspection**: All-weather autonomous patrol and anomaly alarm in steel plants, chemical plants, pipe galleries, and tunnels.

## Competitive Comparison

| Comparison Item | DEEP Robotics Jueying X30 | Unitree B2 | Boston Dynamics Spot |
|----------------|---------------------------|------------|----------------------|
| Positioning | Industrial-grade Quadruped Robot | Industrial-grade Quadruped Robot | Commercial Quadruped Robot |
| Protection Rating | IP67 | IP66 | IP54 |
| Operating Temperature | -20°C to 55°C | Not disclosed | -20°C to 45°C |
| Core Advantages | High protection, high payload, long endurance | High dynamic motion, cost-effective | Mature ecosystem, rich SDK |

## Selection and Deployment Recommendations

- Industrial customers are advised to select payloads such as gimbals, gas sensors, and infrared thermal cameras based on inspection/rescue mission requirements.
- Before deployment, on-site map construction, autonomous charging point setup, and battery endurance verification under extreme environments should be completed.

## References

1. [DEEP Robotics X30 Product Page](https://deeprobotics.cn/robot/index/x30.html)
2. [DEEP Robotics Official Website](https://www.deeprobotics.cn/)
3. [AI Star Island – Jueying X30 Review](https://aixzd.com/robot/x30)
4. [NE Times – DEEP Robotics Completes Series C Financing](https://www.ne-time.cn/web/article/37321)
