# Orbbec

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 奥比中光 |
| **English Name** | Orbbec |
| **Headquarters** | Shenzhen, China |
| **Founded** | 2013 |
| **Website** | [https://www.orbbec.com](https://www.orbbec.com) |
| **Supply Chain Role** | 3D Vision Sensors, Depth Cameras, Robot Vision Modules |
| **Company Type** | Listed Company (688322.SH), China's First 3D Vision Stock |
| **Parent Company/Group** | Independently Listed |
| **Data Source** | Official Website, Financial Reports, Public Reports |

## Company Overview

Orbbec is a leading 3D vision perception company in China, offering 3D vision sensors across all technology routes including structured light, stereo, iToF/dToF, and LiDAR.

Orbbec possesses full-stack capabilities from depth engine ASIC, optical systems, to algorithms and mass production. Its products cover consumer-grade and industrial-grade 3D cameras. The Gemini series of stereo depth cameras are widely used in robotics, AMRs, and humanoid robot vision, with partnerships established with UBTECH, NVIDIA Jetson ecosystem, and others.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Gemini 330 Series | Stereo Depth Cameras | Gemini 335 / 335L / 336 | Service Robots, AMRs, Humanoid Robots |
| Astra Series | Structured Light Depth Cameras | Astra / Astra Pro | Facial Recognition, Gesture Interaction, Smart TVs |
| Femto / Dabai Series | iToF / dToF | Femto Bolt / Dabai | 3D Scanning, Medical, Industrial Measurement |

## Representative Products

### Orbbec Gemini 335

> Orbbec Gemini 335: Please visit [Official Documentation](https://www.orbbec.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | 90 mm × 25 mm × 30 mm | Official Datasheet |
| Weight | 97 g | Official Datasheet |
| Depth Technology | Active + Passive Stereo Vision | Official Datasheet |
| Depth FOV | 90° × 65° | Official Datasheet |
| Depth Resolution / Frame Rate | Up to 1280×800 @ 30 fps / 640×400 @ 60 fps | Official Datasheet |
| RGB Resolution | Up to 1920×1080 @ 30 fps | Official Datasheet |
| Depth Range | 0.1 m – 20 m+ (Ideal 0.26 m – 3.0 m) | Official Datasheet |
| Spatial Accuracy | ≤1.5% @ 2 m | Official Datasheet |
| IMU | Supported | Official Datasheet |
| Interface | USB 3.0 Type-C | Official Datasheet |
| Price | Approx. CNY 1,950 | Public Market Reference |

**Technical Highlights**: Indoor/outdoor usability in all scenarios, MX6800 Depth Engine ASIC, Hardware D2C, IP5X Dust Protection, Multi-camera Synchronization Support.

**Application Scenarios**: Humanoid Robot Vision, AMR Navigation & Obstacle Avoidance, Collaborative Robot Grasping, Drones, 3D Scanning.

### Orbbec Gemini 335Lg

> Orbbec Gemini 335Lg: Please visit [Official Documentation](https://www.orbbec.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | 124 mm × 29 mm × 36 mm | Seeed Studio Wiki |
| Weight | 164 g ± 3 g | Seeed Studio Wiki |
| Depth Technology | Active + Passive Stereo Vision | Official Datasheet |
| Depth FOV | 90° × 65° | Official Datasheet |
| Depth Resolution / Frame Rate | 1280×800 @ 30 fps / 848×480 @ 60 fps | Official Datasheet |
| RGB Resolution | 1280×800 @ 60 fps | Official Datasheet |
| Spatial Accuracy | ≤0.8% @ 2 m; ≤1.6% @ 4 m | Official Datasheet |
| Interface | GMSL2 FAKRA + USB 3 | Official Datasheet |
| Protection Rating | IP65 | Official Datasheet |
| Price | Not Disclosed | Not Disclosed |

**Technical Highlights**: GMSL2 Long-distance Transmission, Global Shutter RGB, IP65 Protection, Suitable for Automotive-grade and Outdoor Robots.

**Application Scenarios**: Humanoid Robots, Autonomous Driving, AMRs, Industrial Inspection, Outdoor Mapping.

## Supply Chain Position

- **Upstream Key Components/Materials**: CMOS Image Sensors, VCSEL/Lasers, Depth Engine ASIC, Optical Lenses, ISP Algorithms
- **Downstream Customers/Application Scenarios**: Service Robots, AMRs/AGVs, Humanoid Robots (e.g., UBTECH Walker Series), Smart TVs, Payment Terminals, 3D Scanning
- **Main Competitors/Peers**: Intel RealSense, Stereolabs, Perceptiv, Hikrobot, Microsoft Azure Kinect

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_orbbec`
- Product Entity: `ent_component_orbbec_gemini_335`
- Product Entity: `ent_component_orbbec_gemini_335lg`
- Key Relationships:
  - `ent_company_orbbec` -- `manufactures` --> `ent_component_orbbec_gemini_335`
  - `ent_company_orbbec` -- `manufactures` --> `ent_component_orbbec_gemini_335lg`
  - `ent_company_orbbec` -- `supplies` --> `ent_company_ubtech` (UBTECH Walker S/X equipped with Orbbec 3D vision sensors)

## References

1. [Official Website](https://www.orbbec.com)
2. [Product Documentation and Public Reports](https://www.orbbec.com)
3. [Appendix D Product Catalog](../index-products.md)
