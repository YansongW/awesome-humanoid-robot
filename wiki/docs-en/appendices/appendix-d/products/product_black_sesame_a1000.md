# Black Sesame Intelligent Huashan A1000 / Black Sesame A1000

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Black Sesame Intelligent / Black Sesame](../companies/company_black_sesame.md) |
| **Product Category** | Autonomous Driving/Robotics AI Computing Chip |
| **Release Date** | Huashan A1000 released in 2020 |
| **Status** | Mass Production/Commercial |
| **Official Website/Source** | Black Sesame Intelligent official website, Hong Kong Stock Exchange prospectus |

## Product Overview

The Black Sesame Intelligent Huashan A1000 is a high-performance AI chip designed for high-level autonomous driving and intelligent robotics, integrating a proprietary ISP, neural network processing engine, and multi-sensor fusion capabilities.

The Huashan A1000 adopts Black Sesame's proprietary NeuralIQ ISP and DynamAI NN engine, supporting multiple high-definition cameras, LiDAR, and millimeter-wave radar inputs, with functional safety targets ranging from ASIL-B to ASIL-D. The single-chip computing power meets the requirements of L2+ to L3 autonomous driving and can also be extended for multi-modal perception and real-time decision-making in robotics.

## Product Image

> Black Sesame Intelligent Huashan A1000: Please visit the [official website](https://www.blacksesame.com.cn) for details.

## Specification Table

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| AI Processor | Huashan A1000 | Black Sesame Intelligent official website |
| Architecture | NeuralIQ ISP + DynamAI NN | Black Sesame public information |
| Process Node | 16 nm | Public reports |
| AI Computing Power | ~58 TOPS (INT8) | Black Sesame public information |
| CPU | ARM Cortex-A55 multi-core | Public reports |
| ISP | Proprietary NeuralIQ, supports multiple high dynamic range image streams | Black Sesame public information |
| Sensor Interfaces | Multiple cameras, LiDAR, millimeter-wave radar | Black Sesame public information |
| Functional Safety | ASIL-B / ASIL-D (target for some modules) | Black Sesame public information |
| Power Consumption | ~15–25 W | Public reports |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Black Sesame Intelligent / Black Sesame](../companies/company_black_sesame.md)
- **Core Components/Technology Sources**: Proprietary ISP/NN architecture, wafer foundry, automotive-grade memory, automotive Ethernet PHY, packaging and testing, PCB.
- **Downstream Applications/Customers**: OEMs, Tier1 suppliers, autonomous driving solution providers, robot integrators, sensor manufacturers.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_black_sesame_a1000`
- Component Entity: `ent_component_black_sesame_a1000_chip`
- Manufacturer Entity: `ent_company_black_sesame`
- Key Relationships:
  - `rel_ent_company_black_sesame_manufactures_ent_product_black_sesame_a1000` (`ent_company_black_sesame` → `manufactures` → `ent_product_black_sesame_a1000`)
  - `rel_ent_company_black_sesame_manufactures_ent_component_black_sesame_a1000_chip` (`ent_company_black_sesame` → `manufactures` → `ent_component_black_sesame_a1000_chip`)
  - `ent_product_black_sesame_a1000` -- `uses` --> `ent_component_black_sesame_a1000_chip`

## Application Scenarios

- **Autonomous Driving Domain Controller**: Serves as the main chip for environment perception, fusion positioning, and path planning.
- **Robotic Perception Brain**: Fuses camera and LiDAR data to support SLAM, obstacle avoidance, and manipulation.
- **Multi-Sensor Fusion Platform**: Used in complex scenarios such as unmanned vehicles, autonomous delivery, and humanoid robots.

## Competitive Comparison

| Comparison Item | Huashan A1000 | Horizon Journey 5 | NVIDIA Orin |
|-----------------|---------------|-------------------|-------------|
| Computing Power | ~58 TOPS | ~128 TOPS | ~200–254 TOPS |
| Functional Safety | ASIL-D target | ASIL-B/D | ASIL-D |
| Ecosystem | Black Sesame toolchain | Horizon Tiangong Kaiwu | NVIDIA DRIVE |

## Procurement and Deployment Recommendations

- Prioritize evaluating the match between the number of camera and radar interfaces and the A1000, as well as the toolchain's support for the target algorithm.
- Complete functional safety and thermal design verification before deployment to ensure compliance with automotive/industrial-grade reliability requirements.
- It is recommended to obtain the latest BSP, SDK, and reference designs through Black Sesame's official channels.

## Related Entries

- [Manufacturer: Black Sesame Intelligent / Black Sesame](../companies/company_black_sesame.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [Black Sesame Intelligent Official Website](https://www.blacksesame.com.cn)
2. [Black Sesame Intelligent Huashan Series](https://www.blacksesame.com.cn/products/1.html)
3. Black Sesame Intelligent Hong Kong Stock Exchange Prospectus
