# Orbbec Gemini 335 / Orbbec Gemini 335

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Orbbec / Orbbec](../companies/company_orbbec.md) |
| **Product Category** | Stereo Depth Camera |
| **Release Date** | April 2024 |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [Orbbec Gemini 335 Product Page](https://www.orbbec.com/products/stereo-vision-camera/gemini-335/) |

## Product Overview

The Orbbec Gemini 335 is the standard version of the Gemini 330 series binocular 3D camera, designed for indoor and semi-outdoor robotic scenarios. The Gemini 335 is equipped with Orbbec's self-developed MX6800 depth engine ASIC, utilizing active + passive fusion stereo vision technology to stably output high-quality depth data in low-texture environments such as strong direct light, low light, and white walls.

The Gemini 335 features a compact body (90×25×30 mm, 97 g), supports USB 3.0 Type-C interface and UVC driver, facilitating rapid integration into AMRs, humanoid robots, robotic arms, drones, and other devices. Its depth diagonal FOV exceeds 100°, with a maximum measurement range over 10 m, and integrates IMU and multi-camera synchronization functions, making it one of the mainstream choices for robotic 3D vision.

## Product Image

> Orbbec Gemini 335: Please visit [Official Materials](https://www.orbbec.com/products/stereo-vision-camera/gemini-335/) for details.

## Specification Parameter Table

| Specification Item | Value | Notes/Source |
|--------------------|-------|--------------|
| Dimensions | 90 mm × 25 mm × 30 mm | Orbbec Store |
| Weight | 97 g | Orbbec Store |
| Depth Technology | Active + Passive Stereo Vision | Orbbec Official Website |
| Depth Resolution | Up to 1280×800 @ 30 fps | Orbbec Store |
| RGB Resolution | Up to 1920×1080 @ 30 fps | Orbbec Store |
| Depth FOV | 90° × 65° (Diagonal >100°) | Orbbec Store |
| Depth Range | 0.1 m – 20 m+ (Ideal 0.26–3.0 m) | Orbbec Store |
| Spatial Accuracy | ≤1.5% @ 2 m | Orbbec Store |
| Interface | USB 3.0 Type-C | Orbbec Store |
| Power Consumption | <3 W | Orbbec Store |
| Protection Rating | IP5X | Orbbec Store |
| Price | Approx. CNY 1,950 | Dealer Reference |

## Supply Chain Position

- **Manufacturer**: [Orbbec / Orbbec](../companies/company_orbbec.md)
- **Core Components/Technology Source**: Self-developed MX6800 depth engine ASIC, optical modules, depth algorithms; image sensors and laser projectors are externally sourced.
- **Downstream Applications/Customers**: AMRs, humanoid robots, collaborative robotic arms, drones, 3D scanning, and human body reconstruction.

## Knowledge Graph Nodes and Relationships

- Component Entity: `ent_component_orbbec_gemini_335`
- Manufacturer Entity: `ent_company_orbbec`
- Key Relationships:
  - `rel_ent_company_orbbec_manufactures_ent_component_orbbec_gemini_335` (`ent_company_orbbec` → `manufactures` → `ent_component_orbbec_gemini_335`)

## Application Scenarios

- **AMR/AGV Navigation and Obstacle Avoidance**: Indoor and outdoor large FOV depth perception and dynamic obstacle detection.
- **Humanoid Robot Vision**: Head or torso vision module supporting VSLAM, gesture and object recognition.
- **Collaborative Robotic Arms**: Bin picking, part localization, dimension measurement, and grasping guidance.
- **Drones and Outdoor Equipment**: Depth data usable under strong light to assist low-altitude obstacle avoidance and terrain mapping.

## Competitive Comparison

| Comparison Item | Orbbec Gemini 335 | Intel RealSense D435i | Stereolabs ZED 2i |
|-----------------|-------------------|-----------------------|-------------------|
| Depth Technology | Active + Passive Binocular | Active Infrared Stereo Vision | Passive Binocular |
| Range | 0.1–20 m+ | 0.3–10 m | 0.3–20 m |
| Power Consumption | <3 W | Approx. 3 W | Approx. 4 W |
| Core Advantage | Outdoor strong light, MX6800 ASIC, low latency | Mature ecosystem, good ROS support | High precision and 3D reconstruction |

## References

1. [Orbbec Gemini 335 Product Page](https://www.orbbec.com/products/stereo-vision-camera/gemini-335/)
2. [Orbbec Store – Gemini 335](https://store.orbbec.com/products/gemini-335)
3. [Orbbec Chinese Official Website – Gemini 330 Series Launch](https://www.orbbec.com.cn/index/News/info.html?cate=31&id=273)
4. [CSDN – ROS2 + Gemini 335L Usage](https://blog.csdn.net/imwaters/article/details/156425172)
