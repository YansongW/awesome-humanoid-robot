# Horizon Robotics

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data updated: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 地平线 |
| **English Name** | Horizon Robotics |
| **Headquarters** | Beijing, China |
| **Founded** | 2015 |
| **Website** | [https://www.horizon.ai](https://www.horizon.ai) |
| **Supply Chain Role** | Edge AI chips, intelligent driving, robotics computing, BPU architecture |
| **Enterprise Type** | Listed company (HKEX: 9660), domestic autonomous driving chip unicorn |
| **Parent Company/Group** | None (independently listed entity) |
| **Data Source** | Horizon Robotics official website, prospectus, public press releases, industry research reports |

## Company Overview

Horizon Robotics is a leading edge AI chip company in China, centered on its self-developed BPU architecture, providing high-performance, low-power computing platforms for intelligent driving and robotics.

Horizon Robotics focuses on edge AI chips and solutions, independently developing the BPU (Brain Processing Unit) neural network processing architecture. Its products cover the Journey series of intelligent driving chips and Horizon Mono/Pilot/SuperDrive solutions. The Journey 6 series targets next-generation high-level autonomous driving and embodied intelligence computing, emphasizing algorithm-chip co-optimization.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Journey Intelligent Driving Chips | ADAS and high-level autonomous driving SoCs | Journey 2/3/5/6 series | Passenger and commercial vehicle autonomous driving |
| Robotics/Embodied Intelligence Computing | Robot perception and decision-making computing platforms | Journey 6 / derived robotics solutions | Humanoid robots, AMRs, unmanned vehicles |
| Algorithms and Toolchains | Perception/planning algorithms and development platforms | Horizon SuperDrive / OpenExplorer | Intelligent driving, robotics development |

## Representative Products

### Horizon Journey 6

> Horizon Journey 6: Please visit [official materials](https://www.horizon.ai) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| AI Compute | Journey 6E: 128 TOPS; Journey 6P: 560 TOPS | Horizon Robotics public materials |
| BPU Architecture | BPU Nash (Nash architecture) | Horizon Robotics public materials |
| Process Node | Not disclosed | - |
| CPU | Multi-core ARM Cortex-A78AE / Self-developed safety core | Public reports |
| ISP | Supports multi-channel high-resolution camera input | Horizon Robotics public materials |
| Functional Safety | ASIL-D / ASIL-B level support | Horizon Robotics public materials |
| Interfaces | PCIe, Ethernet, MIPI CSI-2, CAN-FD | Product manual |
| Price | Not disclosed | - |

**Technical Highlights**: High-compute BPU, algorithm-chip co-design, integrated perception and decision-making for high-level autonomous driving and embodied intelligence, support for multi-sensor fusion.

**Application Scenarios**: High-level intelligent driving, humanoid robot/AMR perception and decision-making, multimodal edge AI.

### Horizon Journey 5

> Horizon Journey 5: Please visit [official materials](https://www.horizon.ai) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| AI Compute | 128 TOPS | Horizon Robotics official website |
| BPU Architecture | BPU Bayes | Horizon Robotics official website |
| CPU | 8-core ARM Cortex-A55 / Dual-core A76 | Public reports |
| ISP | Supports 16 camera inputs | Horizon Robotics public materials |
| Power Consumption | Approx. 30 W | Public reports |
| Functional Safety | ASIL-B(D) target | Horizon Robotics public materials |
| Mass Production Status | Mass-produced and deployed in vehicles | Horizon Robotics public materials |
| Price | Not disclosed | - |

**Technical Highlights**: Mass-produced high-compute autonomous driving chip, open toolchain, supports integrated driving and parking, and highway/urban NOA.

**Application Scenarios**: Passenger car ADAS/AD, robot perception, intelligent transportation.

## Supply Chain Position

- **Upstream Key Components/Materials**: Wafer foundry (TSMC/SMIC, etc.), packaging and testing, memory, ISP IP, automotive-grade certification services.
- **Downstream Customers/Application Scenarios**: Volkswagen, BYD, Li Auto, Changan, and other automakers; robotics/unmanned vehicle solution providers and developers.
- **Main Competitors/Peers**: NVIDIA Drive, Mobileye, Qualcomm Snapdragon Ride, Black Sesame Technologies, Huawei Ascend.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_horizon`
- Product Entities: `ent_product_horizon_journey6`, `ent_product_horizon_journey5`
- Key Relationships:
  - `ent_company_horizon` -- `manufactures` --> `ent_product_horizon_journey6`
  - `ent_company_horizon` -- `manufactures` --> `ent_product_horizon_journey5`
  - `ent_product_horizon_journey6` -- `uses` --> `ent_component_bpu_nash`
  - `ent_product_horizon_journey5` -- `uses` --> `ent_component_bpu_bayes`

## References

1. [Official Website](https://www.horizon.ai)
2. [Horizon Robotics Official Website](https://www.horizon.ai)
3. Horizon Robotics Prospectus (HKEX: 9660)
