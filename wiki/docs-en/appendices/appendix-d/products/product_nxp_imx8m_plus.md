# NXP i.MX 8M Plus Application Processor

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update date: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [NXP Semiconductors](../companies/company_nxp.md) |
| **Product Category** | Industrial-grade Application Processor with Integrated NPU / Edge AI SoC |
| **Release Date** | Released in 2020, mass production in 2021 |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [NXP i.MX 8M Plus Product Page](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-8-applications-processors/i-mx-8m-plus-arm-cortex-a53-machine-learning-vision-multimedia-and-industrial-iot:IMX8MPLUS) |

## Product Overview

The NXP i.MX 8M Plus is a 14 nm heterogeneous application processor for industrial and AIoT applications, integrating a 2.3 TOPS NPU, dual ISP, quad-core Cortex-A53, and a real-time Cortex-M7. This chip supports TSN Gigabit Ethernet, CAN-FD, PCIe 3.0, and multiple display outputs, enabling local execution of visual AI tasks such as defect detection and object recognition, while offering an industrial temperature range and long-term supply. It is widely used in robotics, AGVs, and industrial gateways.

## Product Image

> NXP i.MX 8M Plus Application Processor: Please visit the [official documentation](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-8-applications-processors/i-mx-8m-plus-arm-cortex-a53-machine-learning-vision-multimedia-and-industrial-iot:IMX8MPLUS) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Process Node | 14 nm FinFET | NXP Public Information |
| CPU | Quad-core Arm Cortex-A53 @ up to 1.8 GHz + Cortex-M7 @ 800 MHz | NXP Public Information |
| NPU | Integrated Neural Processing Unit | NXP Public Information |
| AI Compute | Up to 2.3 TOPS INT8 | NXP Public Information |
| ISP | Dual ISP, supports 12MP, HDR, Fisheye Correction | NXP Public Information |
| GPU | Vivante GC7000UL 3D GPU + GC520L 2D GPU | NXP Public Information |
| Memory | Supports LPDDR4/DDR4, up to 6 GB (common module sizes 2–4 GB) | NXP Public Information |
| Interfaces | USB 3.0, PCIe 3.0, 2× GbE (with TSN), 2× CAN-FD, MIPI CSI/DSI, HDMI, LVDS | NXP Public Information |
| Power Consumption | Not disclosed (typical full board 2–5 W) | NXP Public Information |
| Package | FCBGA 15 mm × 15 mm | NXP Public Information |
| Price | Not disclosed | NXP Public Information |

## Supply Chain Position

- **Manufacturer**: [NXP Semiconductors](../companies/company_nxp.md)
- **Core Components/Technology Sources**: NXP self-developed NPU and system IP, ARM CPU/GPU IP, TSMC/GlobalFoundries 14 nm foundry, LPDDR4/DDR4, PMIC, packaging and testing
- **Downstream Applications/Customers**: Industrial automation equipment manufacturers, AGV/AMR vendors, robot OEMs, medical and smart gateway customers

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_nxp_imx8m_plus`
- Component Entity: `ent_component_nxp_imx8m_plus_soc`
- Manufacturer Entity: `ent_company_nxp`
- Key Relationships:
  - `rel_ent_company_nxp_manufactures_ent_product_nxp_imx8m_plus` (`ent_company_nxp` → `manufactures` --> `ent_product_nxp_imx8m_plus`)
  - `rel_ent_company_nxp_manufactures_ent_component_nxp_imx8m_plus_soc` (`ent_company_nxp` → `manufactures` --> `ent_component_nxp_imx8m_plus_soc`)
  - `ent_product_nxp_imx8m_plus` -- `uses` --> `ent_component_nxp_imx8m_plus_soc`

## Application Scenarios

- **Industrial Vision Inspection**: NPU accelerates defect classification and OCR; dual ISP supports HDR and high dynamic range scenes
- **AGV/AMR Main Controller**: TSN/CAN-FD supports real-time communication; low-power operation for SLAM and navigation
- **Smart Gateways and HMI**: Multi-display with independent content, rich interfaces, and industrial-grade reliability

## Competitive Comparison

| Comparison Item | i.MX 8M Plus | TI TDA4VM | Renesas RZ/V2H |
|---|---|---|---|
| AI Compute | 2.3 TOPS | 8 TOPS | 8 TOPS (Dense) |
| CPU | Quad-core A53 + M7 | Dual-core A72 + Hexa-core R5F | Quad-core A55 + Dual-core R8 |
| Industrial Interfaces | TSN, CAN-FD, PCIe 3.0 | TSN, CAN-FD, PCIe | CAN-FD, PCIe, USB 3.2 |

## Selection and Deployment Recommendations

Use the NXP eIQ toolchain to evaluate model performance on the NPU; note whether different versions (Quad/Lite) integrate the NPU; confirm temperature grade and ECC memory configuration for industrial scenarios.

## Related Entries

- [Manufacturer: NXP Semiconductors](../companies/company_nxp.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [NXP i.MX 8M Plus Product Page](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-8-applications-processors/i-mx-8m-plus-arm-cortex-a53-machine-learning-vision-multimedia-and-industrial-iot:IMX8MPLUS)
2. [NXP i.MX 8M Plus Datasheet](https://www.nxp.com/docs/en/data-sheet/IMX8MPLUSIEC.pdf)
3. [NXP eIQ Machine Learning Software](https://www.nxp.com/design/software/development-software/eiq-ml-software-development-environment:EIQ)
