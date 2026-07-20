# SLAMTEC

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).  
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 思岚科技 |
| **English Name** | SLAMTEC |
| **Headquarters** | Shanghai, China |
| **Founded** | 2013 (team started in 2009) |
| **Website** | [https://www.slamtec.com](https://www.slamtec.com) |
| **Supply Chain Role** | LiDAR, SLAM positioning and navigation, robot mobile chassis |
| **Enterprise Type** | Private enterprise, high-tech enterprise |
| **Parent Company/Group** | Independent operation |
| **Data Source** | SLAMTEC official website, product datasheets, public reports |

## Company Profile

SLAMTEC is the most representative provider of autonomous positioning and navigation technology for robots in China. Since 2009, the team has been dedicated to the research and development of core sensors and algorithms for autonomous robot positioning and navigation.

The company's core products include the RPLIDAR series of 2D LiDAR, the SLAMTEC Mapper laser mapping radar, the Zeus series of robot chassis, and related navigation algorithms. Known for low cost, high performance, and ease of integration, its products have essentially achieved import substitution for service robot LiDAR, bringing prices down to the hundreds to thousands of yuan level. They are widely used in service robots, cleaning robots, delivery robots, unmanned vehicles, and humanoid robot navigation.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| 2D LiDAR | Robot environment perception | RPLIDAR A1 / A2 / A3 / S1 | Service robots, unmanned vehicles, humanoid robots |
| Laser Mapping Radar | Real-time mapping and positioning | SLAMTEC Mapper | Surveying, inspection, robot navigation |
| Robot Chassis | Complete mobile platform | Zeus / Apollo series | Service robots, delivery robots |
| SLAM Algorithm/SDK | Positioning and navigation software | RoboStudio / SDK | Robot development |

## Representative Products

### SLAMTEC RPLIDAR A3 Laser Range Sensor

> SLAMTEC RPLIDAR A3: Please visit [official documentation](https://www.slamtec.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | 360° 2D laser ranging radar | Official datasheet |
| Ranging Principle | Laser triangulation | Official datasheet |
| Ranging Engine | RPVision 3.0 | Official datasheet |
| Scanning Angle | 360° | Official datasheet |
| Ranging Radius | 25 m (enhanced mode, white object) / 20 m (outdoor mode, white object) | Official datasheet |
| Minimum Range | 0.2 m | Official datasheet |
| Sampling Frequency | 16,000 samples/sec (enhanced mode) / 10,000 samples/sec (outdoor mode) | Official datasheet |
| Scan Frequency | 5 – 15 Hz (typical 10 Hz) | Official datasheet |
| Angular Resolution | 0.225° | Official datasheet |
| Range Resolution | ≤1% (≤12 m); ≤2% (12 m – 25 m) | Official datasheet |
| Range Accuracy | 1% (≤3 m); 2% (3 – 5 m); 2.5% (5 – 25 m) | Official datasheet |
| Communication Interface | TTL UART | Official datasheet |
| Communication Baud Rate | 256,000 bps | Official datasheet |
| Supply Voltage | 5 V | Official datasheet |
| Operating Current | 450 – 600 mA | Official datasheet |
| Power Consumption | 2.25 – 3 W | Official datasheet |
| Dimensions | Diameter 76 mm × Height 41 mm | Official datasheet |
| Weight | 190 g | Official datasheet |
| Operating Temperature | 0℃ – 40℃ | Official datasheet |
| Laser Safety Class | Class 1 (eye-safe) | Official datasheet |
| Lifespan | OPTMAG technology, up to 5 years | Official datasheet |
| Price | Not disclosed | - |

**Technical Highlights**: OPTMAG (Optical-Magnetic Fusion) wireless power supply + optical communication technology completely solves the slip ring wear problem; indoor/outdoor dual mode; ultra-thin 4 cm design suitable for service robot integration.

**Application Scenarios**: Service robot navigation and obstacle avoidance, unmanned vehicle environment perception, large-screen interaction, humanoid robot positioning and mapping.

### SLAMTEC Mapper Laser Mapping Radar

> SLAMTEC Mapper: Please visit [official documentation](https://www.slamtec.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | LiDAR integrated with real-time mapping and positioning | Official public information |
| Features | Plug-and-play, no external dependencies required | Official public information |
| Output | High-quality map data and positioning coordinates | Official public information |
| Anti-interference | Shaking or slow walking does not affect mapping | Public reviews |
| Ranging/Sampling | Not disclosed | - |
| Weight | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: Integrates LiDAR and SLAM algorithm into one unit, directly outputting maps and positioning information, lowering the barrier for robot development.

**Application Scenarios**: Robot inspection, indoor surveying, AGV/AMR positioning, scientific research and education.

## Supply Chain Position

- **Upstream Key Components/Materials**: Laser emitters, photodetectors, brushless motors, optical lenses, FPGA/SoC, structural parts, wireless power supply modules
- **Downstream Customers/Application Scenarios**: Service robots, cleaning robots, delivery robots, unmanned vehicles, humanoid robots, large-screen interaction, surveying and inspection
- **Main Competitors/Peers**: Hesai Technology, RoboSense, Benewake, LeiShen Intelligent, Osdan

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_slamtec`
- Product Entity: `ent_component_slamtec_rplidar_a3`
- Product Entity: `ent_product_slamtec_mapper`
- Key Relationships:
  - `ent_company_slamtec` -- `manufactures` --> `ent_component_slamtec_rplidar_a3`
  - `ent_company_slamtec` -- `manufactures` --> `ent_product_slamtec_mapper`
  - `ent_component_slamtec_rplidar_a3` -- `used_in` --> `ent_product_service_robot`

## References

1. [SLAMTEC Official Website](https://www.slamtec.com)
2. [SLAMTEC RPLIDAR A3 Product Page](https://www.slamtec.com/cn/Lidar/A3)
3. [RPLIDAR A3M1 Datasheet](https://files.seeedstudio.com/wiki/robotics/Sensor/Lidar/slamtec/LD310_SLAMTEC_rplidar_datasheet_A3M1_v1.9_cn.pdf)
4. [Appendix D Product Catalog](../index-products.md)
