# SLAMTEC RPLIDAR A3 Laser Range Scanner

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update date: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [SLAMTEC / SLAMTEC](../companies/company_slamtec.md) |
| **Product Category** | 360° 2D Laser Range Scanner |
| **Release Date** | Continuously on sale since 2018 |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [SLAMTEC Official Website](https://www.slamtec.com) |

## Product Overview

The SLAMTEC RPLIDAR A3 is a low-cost, high-performance 360° 2D laser range scanner. It uses the laser triangulation ranging principle and the self-developed RPVision 3.0 high-speed vision ranging engine, with a sampling frequency of up to 16,000 times per second and a ranging radius of up to 25 meters.

The A3 supports Enhanced Mode and Outdoor Mode. In Enhanced Mode, the ranging radius and sampling frequency reach their maximum values, while Outdoor Mode provides stronger resistance to sunlight interference. The product adopts the proprietary OPTMAG (Optical-Magnetic Fusion) wireless power supply and optical communication technology, completely solving the wear problem of traditional slip rings, with a lifespan of up to 5 years. Its 4 cm ultra-thin body and 190 g weight make it very suitable for scenarios such as service robots, unmanned vehicles, large-screen interaction, and humanoid robot navigation.

## Product Image

> SLAMTEC RPLIDAR A3: Please visit the [official website](https://www.slamtec.com) for details.

## Specification Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Type | 360° 2D Laser Range Scanner | Official datasheet |
| Ranging Principle | Laser Triangulation | Official datasheet |
| Ranging Engine | RPVision 3.0 | Official datasheet |
| Scanning Angle | 360° | Official datasheet |
| Ranging Radius | 25 m (Enhanced Mode, white object) / 20 m (Outdoor Mode, white object) | Official datasheet |
| Minimum Range | 0.2 m | Official datasheet |
| Sampling Frequency | 16,000 samples/sec (Enhanced Mode) / 10,000 samples/sec (Outdoor Mode) | Official datasheet |
| Scan Frequency | 5 – 15 Hz (Typical 10 Hz) | Official datasheet |
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
| Laser Safety Class | Class 1 (Eye Safe) | Official datasheet |
| Lifespan | Optical-Magnetic Fusion Technology, up to 5 years | Official datasheet |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [SLAMTEC / SLAMTEC](../companies/company_slamtec.md)
- **Core Components/Technology Source**: Self-developed RPVision ranging engine, Optical-Magnetic Fusion power supply and communication technology; laser emitter, photodetector, brushless motor, optical lens, FPGA are purchased externally.
- **Downstream Applications/Customers**: Service robots, cleaning robots, delivery robots, unmanned vehicles, humanoid robots, large-screen interaction, surveying and inspection.

## Knowledge Graph Nodes and Relationships

- Component Entity: `ent_component_slamtec_rplidar_a3`
- Manufacturer Entity: `ent_company_slamtec`
- Key Relationships:
  - `rel_ent_company_slamtec_manufactures_ent_component_slamtec_rplidar_a3` (`ent_company_slamtec` → `manufactures` --> `ent_component_slamtec_rplidar_a3`)

## Application Scenarios

- **Service Robots**: Indoor navigation, obstacle avoidance, SLAM mapping and path planning.
- **Humanoid Robots**: Environmental perception, localization and mapping, autonomous walking.
- **Unmanned Vehicles/AGVs**: Obstacle detection and boundary recognition in low-speed scenarios.
- **Large-Screen Interaction**: Multi-touch, interactive projection, and spatial positioning.

## Competitive Comparison

| Comparison Item | SLAMTEC RPLIDAR A3 | Hesai ET25 | RoboSense M1 Plus |
|----------------|-------------------|------------|-------------------|
| Type | 2D Triangulation Ranging Lidar | Semi-Solid / In-Cabin Lidar | Semi-Solid Lidar |
| Ranging Radius | 25 m | 250 m | 180 m |
| Sampling Frequency | 16,000 samples/sec | >3 million points/sec | Not disclosed |
| Field of View | 360° (Horizontal Single Line) | 120°×25° | Not disclosed |
| Price | Hundreds to thousands of RMB | Automotive Grade | Automotive Grade |
| Core Advantage | Low cost, ultra-thin, long lifespan | Long-range automotive grade, in-cabin installation | Automotive grade mass production |

## Selection and Deployment Recommendations

- The performance of triangulation ranging lidar degrades in outdoor strong light or dark object scenarios. Enhanced Mode or Outdoor Mode should be selected based on the environment.
- During installation, avoid blocking the radar window or allowing dust to accumulate, and ensure a stable 5 V power supply to meet the startup current requirements.

## References

1. [SLAMTEC Official Website](https://www.slamtec.com)
2. [SLAMTEC RPLIDAR A3 Product Page](https://www.slamtec.com/cn/Lidar/A3)
3. [RPLIDAR A3M1 datasheet](https://files.seeedstudio.com/wiki/robotics/Sensor/Lidar/slamtec/LD310_SLAMTEC_rplidar_datasheet_A3M1_v1.9_cn.pdf)
4. [Appendix D Company Directory](../index-companies.md)
