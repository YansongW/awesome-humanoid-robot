# Qualcomm

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 高通 |
| **English Name** | Qualcomm |
| **Headquarters** | San Diego, California, USA |
| **Founded** | 1985 |
| **Website** | [https://www.qualcomm.com](https://www.qualcomm.com) |
| **Supply Chain Role** | Mobile SoC, AI Computing, Robotics Platforms, RB5/RB3, Wireless Communications |
| **Company Type** | Public Company (NASDAQ: QCOM), Global Leader in Wireless Communications and Mobile Computing |
| **Parent Company/Group** | None (Qualcomm Incorporated is the listed entity) |
| **Data Source** | Qualcomm Official Website, Qualcomm Robotics Official Materials, Public Press Releases |

## Company Overview

Qualcomm provides edge computing and connectivity foundations for AMRs, drones, service robots, and humanoid robots through its robotics platforms integrating AI, 5G, vision, and connectivity capabilities.

Qualcomm is a global leader in wireless technology innovation. The Snapdragon platform covers smartphones, automotive, XR, PCs, and robotics. The Qualcomm Robotics platforms (RB3, RB5, RB6, RB1/RB2) integrate high-performance CPU/GPU/NPU, ISP, AI engine, and 5G/Wi-Fi connectivity, supporting ROS 2, AI inference, and multi-camera fusion, making them one of the mainstream platforms for robot development.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Robotics Platforms | Robot development platforms and reference designs | RB5 / RB3 / RB6 / RB1 / RB2 | AMR, Drones, Service Robots, Humanoid Robots |
| Snapdragon Mobile/Compute Platforms | Mobile and edge AI computing | Snapdragon 8 / X / 7 Series | Smart Terminals, XR, Robotics |
| Automotive Platforms | Cockpit-driver integration and vehicle networking | Snapdragon Ride / Cockpit | Smart Cockpits, Autonomous Driving |

## Representative Products

### Qualcomm RB5 / Robotics Development Platform

> Qualcomm RB5 / Robotics Development Platform: Please visit [Official Materials](https://www.qualcomm.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| SoC | Qualcomm QRB5165 | Qualcomm Official Website |
| AI Compute | 5th Gen AI Engine, 15 TOPS | Qualcomm Public Materials |
| CPU | Kryo 585 Octa-core (up to 2.84 GHz) | Qualcomm Official Website |
| GPU | Adreno 650 | Qualcomm Official Website |
| ISP | Supports 7 concurrent cameras | Qualcomm Official Website |
| Connectivity | 5G, Wi-Fi 6, Bluetooth 5.1, GPS | Qualcomm Official Website |
| Interfaces | USB 3.1, PCIe, MIPI CSI, GPIO | Development Kit Materials |
| Price | Development Kit approx. 449 USD (Reference Price) | Qualcomm/Distributors |

**Technical Highlights**: 5G + AI integrated robotics platform, heterogeneous computing, supports ROS 2 and machine learning, rich reference designs.

**Application Scenarios**: AMR, Delivery Robots, Drones, Service Robots, Humanoid Robot Prototyping.

### Qualcomm RB1 / RB2 Robotics Platforms

> Qualcomm RB1 / RB2 Robotics Platforms: Please visit [Official Materials](https://www.qualcomm.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| SoC | QRB2210 (RB1) / QRB4210 (RB2) | Qualcomm Official Website |
| AI Compute | RB2: approx. 5–7 TOPS | Qualcomm Public Materials |
| CPU | Quad-core/Octa-core ARM Cortex | Qualcomm Official Website |
| Camera | Supports multiple cameras | Qualcomm Official Website |
| Connectivity | Wi-Fi, Bluetooth, optional 4G/5G | Qualcomm Official Website |
| Form Factor | Development board form | Development Kit Materials |
| Power Consumption | Low power design | Qualcomm Public Materials |
| Price | Not disclosed | - |

**Technical Highlights**: Cost-effective platform for mid-to-low-end robots, integrated connectivity and AI, lowers development barriers.

**Application Scenarios**: Small Service Robots, Educational Robots, Cleaning Robots, IoT Gateways.

## Supply Chain Position

- **Upstream Key Components/Materials**: TSMC/Samsung Foundry, ARM IP, Memory, RF Front-end, Baseband IP, Sensor Partners.
- **Downstream Customers/Application Scenarios**: Robot OEM/ODM, AMR Manufacturers, Drone Manufacturers, Automotive Companies, Mobile/PC Manufacturers.
- **Main Competitors/Comparables**: NVIDIA Jetson, Intel Movidius, Horizon Journey, Huawei Ascend, MediaTek.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_qualcomm`
- Product Entities: `ent_product_qualcomm_rb5`, `ent_product_qualcomm_rb1_rb2`
- Key Relationships:
  - `ent_company_qualcomm` -- `manufactures` --> `ent_product_qualcomm_rb5`
  - `ent_company_qualcomm` -- `manufactures` --> `ent_product_qualcomm_rb1_rb2`
  - `ent_product_qualcomm_rb5` -- `uses` --> `ent_component_qrb5165_soc`
  - `ent_product_qualcomm_rb1_rb2` -- `uses` --> `ent_component_qrb4210_soc`

## References

1. [Official Website](https://www.qualcomm.com)
2. [Qualcomm Official Website](https://www.qualcomm.com)
3. [Qualcomm Robotics RB5 Page](https://www.qualcomm.com/products/internet-of-things/industrial/robotics/qualcomm-robotics-rb5-platform)
