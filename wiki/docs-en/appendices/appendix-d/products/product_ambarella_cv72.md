# Ambarella CV72 Vision AI SoC

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Table of Contents](../index-products.md)
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Ambarella](../companies/company_ambarella.md) |
| **Product Category** | Edge AI Vision SoC / Security and Robotics Vision Processor |
| **Release Date** | 2023 (CV72S) |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [Ambarella CV72 Product Page](https://www.ambarella.com/products/aiot-industrial-robotics/cv72-ai-soc/) |

## Product Overview

The Ambarella CV72 series is an edge AI vision SoC based on a 5 nm process, featuring a third-generation CVflow AI accelerator and an integrated ISP. Its AI computing power is approximately 12 TOPS, enabling local execution of the latest CNN and Transformer networks while supporting multi-channel 4K/8K video encoding at under 3 W power consumption. The CV72 also supports radar-vision sensor fusion and AI-ISP enhanced night vision, making it an ideal platform for security cameras, robotic vision, and industrial inspection.

## Product Image

> Ambarella CV72 Vision AI SoC: Please visit the [official page](https://www.ambarella.com/products/aiot-industrial-robotics/cv72-ai-soc/) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Process Node | 5 nm (public reports) | Ambarella public information |
| CPU | Dual-core / Quad-core Arm Cortex-A76 (up to 1.8 GHz depending on version) | Ambarella public information |
| AI Accelerator | Third-generation CVflow AI accelerator | Ambarella public information |
| AI Computing Power | Approximately 12 TOPS (CV72, public reports) | Ambarella public information |
| ISP | Integrated high-performance ISP, supports low-light HDR, AI-ISP (AISP) | Ambarella public information |
| Video | 4Kp120 / 8Kp30 encoding, multi-channel video concurrent | Ambarella public information |
| Memory | Supports LPDDR4x / LPDDR5 / LPDDR5x | Ambarella public information |
| Interfaces | PCIe, USB 3.2, GbE, MIPI CSI, radar fusion interface | Ambarella public information |
| Power Consumption | Typical < 3 W (CV72S, public reports) | Ambarella public information |
| Package | Not disclosed | Ambarella public information |
| Price | Not disclosed | Ambarella public information |

## Supply Chain Position

- **Manufacturer**: [Ambarella](../companies/company_ambarella.md)
- **Core Components/Technology Sources**: Samsung 5 nm foundry, ARM CPU IP, proprietary CVflow/ISP, LPDDR5x, packaging and testing, substrate
- **Downstream Applications/Customers**: Security OEMs, smart camera solution providers, robotics and drone manufacturers, traffic surveillance integrators

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_ambarella_cv72`
- Component Entity: `ent_component_ambarella_cv72_chip`
- Manufacturer Entity: `ent_company_ambarella`
- Key Relationships:
  - `rel_ent_company_ambarella_manufactures_ent_product_ambarella_cv72` (`ent_company_ambarella` → `manufactures` --> `ent_product_ambarella_cv72`)
  - `rel_ent_company_ambarella_manufactures_ent_component_ambarella_cv72_chip` (`ent_company_ambarella` → `manufactures` --> `ent_component_ambarella_cv72_chip`)
  - `ent_product_ambarella_cv72` -- `uses` --> `ent_component_ambarella_cv72_chip`

## Application Scenarios

- **Robotic Vision**: Multi-camera real-time object detection, semantic segmentation, and navigation assistance
- **Smart Security Cameras**: Edge-side 4K AI analysis, low-light color night vision, face/license plate recognition
- **Industrial Vision Inspection**: High-speed defect detection, dimensional measurement, OCR and barcode recognition

## Competitive Comparison

| Comparison Item | Ambarella CV72 | Qualcomm QCS8550 | NVIDIA Jetson Orin NX |
|---|---|---|---|
| Process Node | 5 nm | 4 nm | 8 nm |
| AI Computing Power | Approximately 12 TOPS | Approximately 15 TOPS | Up to 100 TOPS |
| Power Consumption | < 3 W | Approximately 5–10 W | 10–25 W |

## Selection and Deployment Recommendations

Evaluate Ambarella SDK support for target Transformer/CNN models; use the CVflow toolchain to quantize and optimize models; select the corresponding CV72 version and reference design based on camera and radar interfaces.

## Related Entries

- [Manufacturer: Ambarella](../companies/company_ambarella.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [Ambarella CV72 Product Page](https://www.ambarella.com/products/aiot-industrial-robotics/cv72-ai-soc/)
2. [Ambarella CV72S Press Release](https://www.ambarella.com/news/ambarella-launches-4k-5nm-edge-ai-soc-mainstream-security/)
3. [Ambarella Official Website](https://www.ambarella.com)
