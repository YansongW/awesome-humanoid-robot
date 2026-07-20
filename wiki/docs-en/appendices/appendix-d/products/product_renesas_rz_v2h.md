# Renesas RZ/V2H Vision AI MPU

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update date: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Renesas Electronics](../companies/company_renesas.md) |
| **Product Category** | Vision AI MPU with integrated DRP-AI3 / Robot Edge Computing Platform |
| **Release Date** | 2024 |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [Renesas RZ/V2H Product Page](https://www.renesas.com/en/products/rz-v2h) |

## Product Overview

The Renesas RZ/V2H is an MPU for high-performance vision AI, integrating Renesas' third-generation DRP-AI3 accelerator, providing 8 TOPS dense computing power and up to 80 TOPS sparse computing power. The chip features a heterogeneous combination of quad-core Cortex-A55, dual-core real-time Cortex-R8, and Cortex-M33, supporting four MIPI CSI, PCIe Gen3, USB 3.2, and multiple CAN-FD interfaces, making it suitable for autonomous robots, industrial vision, and smart camera applications requiring low power consumption and high computing power.

## Product Image

> Renesas RZ/V2H Vision AI MPU: Please visit [Official Documentation](https://www.renesas.com/en/products/rz-v2h) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Process Node | Not disclosed | Renesas public information |
| CPU | Quad-core Arm Cortex-A55 @ 1.8 GHz + Dual-core Cortex-R8 @ 800 MHz + Cortex-M33 @ 200 MHz | Renesas public information |
| AI Accelerator | DRP-AI3 (Dynamically Reconfigurable Processor + AI-MAC) | Renesas public information |
| AI Computing Power | 8 TOPS (dense models) / Up to 80 TOPS (sparse models) | Renesas public information |
| ISP | Optional Arm Mali-C55 ISP | Renesas public information |
| GPU | GE3D 3D GPU | Renesas public information |
| Memory | LPDDR4 / LPDDR4X interface | Renesas public information |
| Interfaces | PCIe Gen3 x4, USB 3.2 Gen2 x2, GbE x2, MIPI CSI-2 x4, CAN-FD x6 | Renesas public information |
| Power Consumption | Not disclosed (typically below 10 W) | Renesas public information |
| Package | BGA 19 mm × 19 mm, 1368 pin | Renesas public information |
| Price | Not disclosed | Renesas public information |

## Supply Chain Position

- **Manufacturer**: [Renesas Electronics](../companies/company_renesas.md)
- **Core Components/Technology Sources**: Renesas self-developed DRP-AI3 IP, ARM CPU/ISP/GPU IP, LPDDR4x, packaging and testing, PMIC, carrier board
- **Downstream Applications/Customers**: Robot OEMs, industrial camera and vision solution providers, AGV/AMR manufacturers, drone manufacturers

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_renesas_rz_v2h`
- Component Entity: `ent_component_renesas_rz_v2h_soc`
- Manufacturer Entity: `ent_company_renesas`
- Key Relationships:
  - `rel_ent_company_renesas_manufactures_ent_product_renesas_rz_v2h` (`ent_company_renesas` → `manufactures` --> `ent_product_renesas_rz_v2h`)
  - `rel_ent_company_renesas_manufactures_ent_component_renesas_rz_v2h_soc` (`ent_company_renesas` → `manufactures` --> `ent_component_renesas_rz_v2h_soc`)
  - `ent_product_renesas_rz_v2h` -- `uses` --> `ent_component_renesas_rz_v2h_soc`

## Application Scenarios

- **Autonomous Mobile Robots**: Multi-channel visual perception, SLAM, dynamic obstacle avoidance, and path planning
- **Smart Industrial Cameras**: High-speed defect detection, object recognition, and measurement without external accelerators
- **Vision-Guided Robots**: Real-time pose estimation and grasping positioning, supporting Transformer/CNN hybrid networks

## Competitive Comparison

| Comparison Item | RZ/V2H | NXP i.MX 8M Plus | TI TDA4VM |
|---|---|---|---|
| AI Computing Power (Dense) | 8 TOPS | 2.3 TOPS | 8 TOPS |
| Sparse Computing Power | Up to 80 TOPS | Not disclosed | Not disclosed |
| CPU | Quad-core A55 + Dual-core R8 | Quad-core A53 + M7 | Dual-core A72 + Hexa-core R5F |

## Selection and Deployment Recommendations

Use the DRP-AI TVM / RUHMI toolchain to compile quantized models; confirm DRP-AI support for target operators; select the RZ/V2H EVK or custom carrier board based on the number of cameras and bandwidth.

## Related Entries

- [Manufacturer: Renesas Electronics](../companies/company_renesas.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [Renesas RZ/V2H Product Page](https://www.renesas.com/en/products/rz-v2h)
2. [Renesas RZ/V Series](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rz-v-ai-accelerator)
3. [DRP-AI TVM GitHub](https://renesas-rz.github.io/rzv_drp-ai_tvm/)
