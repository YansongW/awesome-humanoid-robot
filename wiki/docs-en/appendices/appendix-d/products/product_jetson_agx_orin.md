# NVIDIA Jetson AGX Orin

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [NVIDIA](../companies/company_nvidia.md) |
| **Product Category** | Edge AI Computing Module |
| **Release Date** | 2022 |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [NVIDIA Jetson Orin Page](https://www.nvidia.cn/autonomous-machines/embedded-systems/jetson-orin/) |

## Product Overview

The NVIDIA Jetson AGX Orin is a high-performance computing module designed for autonomous machines, robotics, and edge AI, with AI performance up to 275 TOPS (64 GB version), over 8 times that of the previous generation Jetson AGX Xavier. The module features an NVIDIA Ampere architecture GPU, Arm Cortex-A78AE CPU, and next-generation deep learning/vision accelerators, supporting high-speed interfaces for multiple high-resolution cameras, LiDAR, IMUs, and other sensors.

The Jetson AGX Orin is available in three versions: 64 GB, 32 GB, and an industrial variant, with power consumption configurable between 15 W and 60 W, meeting the needs of everything from low-power mobile robots to high-load industrial equipment. Its unified JetPack SDK, Isaac ROS, and Isaac Sim ecosystem make it the mainstream computing platform for humanoid robots, AMRs, drones, and autonomous driving prototype development.

## Product Image

> NVIDIA Jetson AGX Orin: Please visit [Official Documentation](https://www.nvidia.cn/autonomous-machines/embedded-systems/jetson-orin/) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | 100 mm × 87 mm (module) | NVIDIA Official Website |
| AI Performance | Up to 275 TOPS (64 GB) | NVIDIA Official Website |
| GPU | 2048-core NVIDIA Ampere architecture GPU, 64 Tensor Cores | NVIDIA Official Website |
| CPU | 12-core Arm Cortex-A78AE v8.2 | NVIDIA Official Website |
| Memory | 64 GB / 32 GB LPDDR5, 204.8 GB/s | NVIDIA Official Website |
| DL Accelerator | 2× NVDLA v2 | NVIDIA Official Website |
| Vision Accelerator | 1× PVA v2 | NVIDIA Official Website |
| Camera Interface | 16-lane MIPI CSI-2 | NVIDIA Official Website |
| Power Consumption | 15 W – 60 W (configurable) | NVIDIA Official Website |
| Price | Not disclosed (Developer Kit approx. 1,999 USD) | Third-party Reference |

## Supply Chain Position

- **Manufacturer**: [NVIDIA](../companies/company_nvidia.md)
- **Core Components/Technology Source**: In-house Ampere GPU, Arm CPU, NVDLA, PVA; storage, PMIC, carrier board provided by partners.
- **Downstream Applications/Customers**: Humanoid robots, AMR/AGV, drones, industrial vision, autonomous driving prototypes, scientific research and education.

## Knowledge Graph Nodes and Relationships

- Component Entity: `ent_component_nvidia_jetson_agx_orin`
- Manufacturer Entity: `ent_company_nvidia`
- Key Relationships:
  - `rel_ent_company_nvidia_manufactures_ent_component_nvidia_jetson_agx_orin` (`ent_company_nvidia` → `manufactures` → `ent_component_nvidia_jetson_agx_orin`)

## Application Scenarios

- **Humanoid Robot Brain**: Running VLM/VLA models, SLAM, dynamic obstacle avoidance, and dexterous hand control.
- **AMR/AGV**: Multi-camera and LiDAR fusion perception and path planning.
- **Industrial Vision Inspection**: Real-time edge-side defect detection, object recognition, and measurement.
- **Autonomous Driving Prototypes**: Perception and decision verification platform for passenger cars and unmanned vehicles.

## Competitive Comparison

| Comparison Item | Jetson AGX Orin | Jetson Orin NX | Jetson AGX Xavier |
|-----------------|-----------------|----------------|-------------------|
| AI Performance | Up to 275 TOPS | Up to 157 TOPS | 32 TOPS |
| Power Consumption | 15–60 W | 10–40 W | 10–30 W |
| Memory | 64 GB LPDDR5 | 16 GB LPDDR5 | 16 GB LPDDR4 |
| Key Advantage | Highest performance, unified ecosystem | Compact size, cost-effective | Mature and stable |

## References

1. [NVIDIA Jetson Orin Official Page](https://www.nvidia.cn/autonomous-machines/embedded-systems/jetson-orin/)
2. [NVIDIA Jetson AGX Orin Developer Kit](https://developer.nvidia.com/embedded/jetson-agx-orin-developer-kit)
3. [EEFocus – Humanoid Robot Main Chip Comparison](https://www.eefocus.com/article/1821462.html)
4. [CSDN – Jetson Series Performance Comparison](https://blog.csdn.net/qq_43298381/article/details/144167933)
