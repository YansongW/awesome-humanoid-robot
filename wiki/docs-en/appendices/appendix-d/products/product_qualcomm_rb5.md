# Qualcomm RB5 / Robotics Platform

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Qualcomm](../companies/company_qualcomm.md) |
| **Product Category** | Robotics Edge AI Development Platform |
| **Release Date** | RB5 released in 2020 |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | See References in main text |

## Product Overview

The Qualcomm Robotics RB5 platform is based on the QRB5165 SoC, integrating a 5th-generation AI engine, supporting 7 concurrent cameras, 5G/Wi-Fi 6 connectivity, and a rich set of sensor interfaces. It is a common edge computing platform for prototyping AMRs, delivery robots, drones, and humanoid robots. The Qualcomm robotics platform emphasizes heterogeneous computing, connectivity capabilities, and the developer ecosystem.

## Product Image

> Qualcomm RB5 / Robotics Platform: Please visit the [official page](https://www.qualcomm.com/products/internet-of-things/industrial/robotics/qualcomm-robotics-rb5-platform) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| SoC | Qualcomm QRB5165 | Qualcomm Official Website |
| AI Compute | 5th Gen AI Engine, 15 TOPS | Qualcomm Public Information |
| CPU | Kryo 585 Octa-core (up to 2.84 GHz) | Qualcomm Official Website |
| GPU | Adreno 650 | Qualcomm Official Website |
| ISP | Supports 7 concurrent cameras | Qualcomm Official Website |
| Connectivity | 5G, Wi-Fi 6, Bluetooth 5.1, GPS | Qualcomm Official Website |
| Interfaces | USB 3.1, PCIe, MIPI CSI, GPIO | Development Kit Documentation |
| Price | Development Kit approx. 449 USD (reference price) | Qualcomm / Distributors |

## Supply Chain Position

- **Manufacturer**: [Qualcomm](../companies/company_qualcomm.md)
- **Core Components/Technology Sources**: TSMC foundry, ARM IP, memory, RF front-end, baseband, sensor ecosystem.
- **Downstream Applications/Customers**: AMR manufacturers, drone manufacturers, service robot manufacturers, developers, and educational institutions.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_qualcomm_rb5`
- Manufacturer Entity: `ent_company_qualcomm`
- Key Relationships:
  - `rel_ent_company_qualcomm_manufactures_ent_product_qualcomm_rb5` (`ent_company_qualcomm` → `manufactures` → `ent_product_qualcomm_rb5`)
  - `ent_product_qualcomm_rb5` -- `uses` --> `ent_component_qrb5165_soc`
  - `ent_product_qualcomm_rb5` -- `supports` --> `ent_component_5g_module`

## Application Scenarios

- **AMR**: Perception and navigation for autonomous mobile robots in warehouse logistics.
- **Delivery Robots**: Outdoor/indoor delivery, relying on 5G and AI vision.
- **Drones**: Edge AI and connectivity for aerial photography, inspection, and logistics drones.

## Competitive Comparison

| Comparison Item | RB5 | NVIDIA Jetson AGX Orin | Horizon Robotics Journey 5 |
|-----------------|------|------------------------|----------------------------|
| Compute Power | 15 TOPS | 275 TOPS | 128 TOPS |
| Connectivity | Integrated 5G/Wi-Fi 6 | Requires external module | Requires external module |
| Ecosystem | ROS 2 + Mobile Ecosystem | Strong CUDA/Isaac | Autonomous Driving Ecosystem |

## Selection and Deployment Recommendations

- Select the corresponding model based on compute power, precision, and scenario requirements, prioritizing officially supported toolchains and ecosystem compatibility.
- Before deployment, confirm that power supply, heat dissipation, mechanical interfaces, and communication protocols meet the overall system requirements.
- It is recommended to obtain the latest firmware, SDK, and technical support through official channels or authorized distributors.

## Related Entries

- [Manufacturer: Qualcomm](../companies/company_qualcomm.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [Qualcomm Official Product/Company Page](https://www.qualcomm.com/products/internet-of-things/industrial/robotics/qualcomm-robotics-rb5-platform)
2. [Qualcomm Robotics RB5 Page](https://www.qualcomm.com/products/internet-of-things/industrial/robotics/qualcomm-robotics-rb5-platform)
