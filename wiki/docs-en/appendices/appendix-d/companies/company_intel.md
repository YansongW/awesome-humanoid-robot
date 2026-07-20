# Intel

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).  
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 英特尔 |
| **English Name** | Intel |
| **Headquarters** | Santa Clara, California, USA |
| **Founded** | 1968 |
| **Website** | [https://www.intel.com](https://www.intel.com) |
| **Supply Chain Role** | Depth vision sensors, computing platforms, AI inference hardware |
| **Enterprise Type** | Public company (NASDAQ: INTC), multinational semiconductor and computing enterprise |
| **Parent Company/Group** | Independently listed |
| **Data Source** | Official website, product datasheets, third-party reviews |

## Company Overview

Intel is one of the world's largest semiconductor and computing platform companies. Its RealSense series of depth cameras have a broad ecosystem in robotics vision and academic research.

The Intel RealSense product line covers multiple depth sensing technologies such as stereo vision, structured light, and LiDAR, providing modular solutions integrating RGB-D, IMU, and vision processors. Products are widely used in service robots, AMRs, industrial inspection, 3D scanning, and virtual reality, and rely on the open-source librealsense SDK and the ROS/ROS 2 community to form a complete developer ecosystem.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| RealSense D400 Series | Stereo depth cameras | D455 / D435i / D405 | Robot navigation, obstacle avoidance, SLAM, 3D scanning |
| RealSense D500 / New Platform | Next-generation depth sensing | D515 / D555, etc. | Augmented reality, digital twins, smart devices |

## Representative Products

### Intel RealSense D455

> Intel RealSense D455: Please visit [official documentation](https://www.intel.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | 124 mm × 26 mm × 29 mm | Official datasheet |
| Weight | Approx. 120 g | Third-party review |
| Depth Technology | Active IR stereo vision | Official datasheet |
| Depth FOV | 87° × 58° | Official datasheet |
| Depth Resolution/Frame Rate | Up to 1280×720 @ 90 fps | Official datasheet |
| RGB Resolution | Up to 1280×800 @ 30 fps | Official datasheet |
| Ideal Range | 0.6 m – 6 m | Official datasheet |
| Depth Accuracy | <2% @ 4 m | Official datasheet |
| IMU | Integrated 6-axis IMU | Official datasheet |
| Interface | USB-C 3.1 Gen 1 | Official datasheet |
| Price | Approx. USD 299 | Public market reference |

**Technical Highlights**: 95 mm baseline, global shutter, integrated IMU, wide field of view, suitable for indoor and outdoor robot navigation and dynamic scene perception.

**Application Scenarios**: Humanoid robot head/torso vision, AMR obstacle avoidance, 3D scanning, industrial inspection, academic research.

### Intel RealSense D435i

> Intel RealSense D435i: Please visit [official documentation](https://www.intel.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | 90 mm × 25 mm × 25 mm | Official datasheet |
| Weight | Approx. 72 g | Third-party review |
| Depth Technology | Active IR stereo vision | Official datasheet |
| Depth FOV | 87° × 58° | Official datasheet |
| Depth Resolution/Frame Rate | Up to 1280×720 @ 90 fps | Official datasheet |
| RGB Resolution | Up to 1920×1080 @ 30 fps | Official datasheet |
| Ideal Range | 0.1 m – 10 m | Official datasheet |
| Depth Accuracy | <2% @ 2 m | Official datasheet |
| IMU | Integrated Bosch BMI055 | Official datasheet |
| Interface | USB-C 3.1 | Official datasheet |
| Price | Approx. USD 199 | Public market reference |

**Technical Highlights**: Smaller size, lower cost, integrated IMU, suitable for robot platforms with size and budget constraints.

**Application Scenarios**: Drones, small AMRs, collaborative robot vision, education and research.

## Supply Chain Position

- **Upstream Key Components/Materials**: CMOS image sensors, infrared lasers, vision processor ASICs, optical lenses
- **Downstream Customers/Application Scenarios**: Service robots, AMRs/AGVs, humanoid robots, industrial inspection, 3D scanning equipment, research and educational institutions
- **Main Competitors/Peers**: Orbbec, Stereolabs, Azure Kinect, Hikrobot, Percipio

## Knowledge Graph Nodes and Relationships

- Company entity: `ent_company_intel`
- Product entity: `ent_component_intel_realsense_d455`
- Product entity: `ent_component_intel_realsense_d435i`
- Key relationships:
  - `ent_company_intel` -- `manufactures` --> `ent_component_intel_realsense_d455`
  - `ent_company_intel` -- `manufactures` --> `ent_component_intel_realsense_d435i`

## References

1. [Official website](https://www.intel.com)
2. [Product documentation and public reports](https://www.intel.com)
3. [Appendix D Product Catalog](../index-products.md)
