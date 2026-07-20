# Stereolabs

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Stereolabs |
| **English Name** | Stereolabs |
| **Headquarters** | Paris, France / San Francisco, USA |
| **Founded** | 2010 |
| **Website** | [https://www.stereolabs.com](https://www.stereolabs.com) |
| **Supply Chain Role** | Stereo vision depth cameras, AI perception software, edge computing |
| **Company Type** | Private company, AI vision and depth perception technology company |
| **Parent Company/Group** | Acquired by Ouster in 2026 (wholly owned subsidiary) |
| **Data Sources** | Official website, product pages, Ouster acquisition announcement |

## Company Overview

Stereolabs is a global leader in stereo vision and AI perception. Its ZED series depth cameras are widely used in robotics, drones, and spatial analysis.

Stereolabs offers the ZED series stereo depth cameras, ZED SDK, AI perception algorithms, and edge computing platforms. Its neural network depth engine enables high-precision depth estimation without active light sources. The products support edge platforms such as NVIDIA Jetson and are widely used in autonomous navigation, 3D measurement, mixed reality, and robotic vision.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| ZED 2i | Industrial-grade stereo camera | ZED 2i | Robot navigation, outdoor perception, spatial analysis |
| ZED X | GMSL2 automotive/industrial camera | ZED X | Autonomous driving, AMR, industrial vision |
| ZED Box | Edge AI computing | ZED Box Mini | Multi-camera fusion, edge perception |

## Representative Products

### Stereolabs ZED 2i

> Stereolabs ZED 2i: Please visit [official documentation](https://www.stereolabs.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | 175.25 mm × 30.25 mm × 43.10 mm | Official datasheet |
| Weight | 230 g | Official datasheet |
| Depth Technology | Neural network stereo depth | Official datasheet |
| FOV (2.1 mm lens) | 110°(H) × 70°(V) × 120°(D) | Official datasheet |
| Video Resolution | 2K @ 15 fps / 1080p @ 30 fps / 720p @ 60 fps | Official datasheet |
| Depth Range | 0.3 m – 20 m (2.1 mm lens) | Official datasheet |
| Motion Sensors | Accelerometer, gyroscope, barometer, magnetometer, temperature | Official datasheet |
| Ingress Protection | IP66 (optional) | Official datasheet |
| Interface | USB 3.1 Type-C | Official datasheet |
| Price | Approx. USD 499 and up | Official store |

**Technical Highlights**: Neural network depth perception, wide field of view, IP66 protection, integrated multi-sensors, suitable for indoor/outdoor robots and dynamic scenes.

**Application Scenarios**: Humanoid robot/AMR vision, outdoor mapping, spatial analysis, mixed reality, industrial inspection.

### Stereolabs ZED X

> Stereolabs ZED X: Please visit [official documentation](https://www.stereolabs.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | 164 mm × 32 mm × 37 mm | Official datasheet |
| Weight | 240 g | Official datasheet |
| Depth Technology | Neural Depth Engine 2 + global shutter | Official datasheet |
| Resolution | 1920×1200 @ 60 fps / 960×600 @ 120 fps | Official datasheet |
| FOV | 110°(H) × 80°(V) × 120°(D) (2.2 mm) | Official datasheet |
| Interface | GMSL2 (up to 15 m) | Official datasheet |
| Ingress Protection | IP67 | Official datasheet |
| IMU | 16-bit three-axis accelerometer/gyroscope | Official datasheet |
| Operating Temperature | -20°C ~ +55°C | Official datasheet |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: GMSL2 long-distance transmission, global shutter, IP67 protection, multi-camera hardware synchronization, designed for automotive and industrial environments.

**Application Scenarios**: Autonomous driving, humanoid robots, agricultural robots, digital twins, high-precision SLAM.

## Supply Chain Position

- **Upstream Key Components/Materials**: CMOS image sensors, AI accelerator chips, optical lenses, GMSL2 interface chips
- **Downstream Customers/Application Scenarios**: AMR, drones, humanoid robots, autonomous driving, AR/VR, spatial analysis platforms
- **Main Competitors/Peers**: Intel RealSense, Orbbec, Perceptiv, Hikrobot, Ouster

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_stereolabs`
- Product Entity: `ent_component_stereolabs_zed_2i`
- Product Entity: `ent_component_stereolabs_zed_x`
- Key Relationships:
  - `ent_company_stereolabs` -- `manufactures` --> `ent_component_stereolabs_zed_2i`
  - `ent_company_stereolabs` -- `manufactures` --> `ent_component_stereolabs_zed_x`

## References

1. [Official Website](https://www.stereolabs.com)
2. [Product Documentation and Public Reports](https://www.stereolabs.com)
3. [Appendix D Product Catalog](../index-products.md)
