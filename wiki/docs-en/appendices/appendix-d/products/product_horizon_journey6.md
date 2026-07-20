# Horizon Journey 6

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Horizon Robotics](../companies/company_horizon.md) |
| **Product Category** | Intelligent Driving/Embodied Intelligent Computing SoC |
| **Release Date** | Released in 2024 |
| **Status** | In mass production introduction |
| **Official Website/Source** | See references in the main text |

## Product Overview

The Horizon Journey 6 series is a high-performance edge AI SoC designed for next-generation advanced intelligent driving and embodied intelligence scenarios. Adopting the self-developed BPU Nash architecture, Journey 6 emphasizes algorithm-chip co-design, supports multi-channel high-resolution camera, LiDAR, and millimeter-wave radar fusion, aiming to provide perception and decision-making computing power for advanced intelligent driving and humanoid robots/AMRs.

## Product Image

> Horizon Journey 6: Please visit [Official Materials](https://www.horizon.ai) for details.

## Specification Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| AI Computing Power | Journey 6E 128 TOPS; Journey 6P 560 TOPS | Horizon public materials |
| BPU Architecture | BPU Nash | Horizon public materials |
| CPU | Multi-core ARM Cortex-A78AE / Safety Core | Public reports |
| ISP | Supports multi-channel high-resolution cameras | Horizon public materials |
| Functional Safety | ASIL-D / ASIL-B support | Horizon public materials |
| Interfaces | PCIe, Ethernet, MIPI CSI-2, CAN-FD | Product manual |
| Power Consumption | Not disclosed | - |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Horizon Robotics](../companies/company_horizon.md)
- **Core Components/Technology Sources**: Wafer foundry, ARM IP, memory, ISP IP, automotive certification, sensor partners.
- **Downstream Applications/Customers**: Passenger car OEMs, Tier 1 suppliers, robot/AMR solution providers, autonomous driving companies.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_horizon_journey6`
- Manufacturer Entity: `ent_company_horizon`
- Key Relationships:
  - `rel_ent_company_horizon_manufactures_ent_product_horizon_journey6` (`ent_company_horizon` → `manufactures` → `ent_product_horizon_journey6`)
  - `ent_product_horizon_journey6` -- `uses` --> `ent_component_bpu_nash`
  - `ent_product_horizon_journey6` -- `processes` --> `ent_component_camera_sensor`

## Application Scenarios

- **Advanced Intelligent Driving**: Supports highway and urban NOA, integrated driving and parking.
- **Embodied Intelligent Perception**: Provides visual/multi-sensor fusion perception for robots.
- **Multimodal Edge AI**: Low-latency visual language understanding and decision-making.

## Competitive Comparison

| Comparison Item | Journey 6 | NVIDIA Orin | Qualcomm Snapdragon Ride |
|----------------|-----------|-------------|--------------------------|
| Computing Power | 128–560 TOPS | 254 TOPS | Tens to hundreds of TOPS |
| Architecture | BPU Nash | Ampere/Blackwell | Adreno/DSP |
| Advantages | Algorithm co-design, cost optimization | Mature ecosystem | Connectivity and cockpit-driving integration |

## Selection and Deployment Recommendations

- Select the corresponding model based on computing power, accuracy, and scenario requirements, prioritizing the official toolchain and ecosystem compatibility.
- Before deployment, confirm whether power supply, heat dissipation, mechanical interfaces, and communication protocols meet the overall system requirements.
- It is recommended to obtain the latest firmware, SDK, and technical support through official channels or authorized distributors.

## Related Entries

- [Manufacturer: Horizon Robotics](../companies/company_horizon.md)
- [Appendix D.4 Key Product Wiki](../index-products.md)

## References

1. [Horizon Robotics Official Product/Company Page](https://www.horizon.ai)
2. [Horizon Official Website](https://www.horizon.ai)
3. Horizon Journey 6 Launch Event Materials
