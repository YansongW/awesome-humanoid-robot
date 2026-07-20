# Sony IMX500 Intelligent Vision Sensor

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Sony Semiconductor Solutions](../companies/company_sony_semiconductor.md) |
| **Product Category** | Stacked CMOS Image Sensor (Integrated AI Inference) |
| **Release Date** | Commercialized from 2020 |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [Sony IMX500 Intelligent Vision Sensor Product/Data Page](https://www.sony-semicon.co.jp/products/common/IMX500.html) |

## Product Overview

The IMX500 is the world's first image sensor to integrate an AI processing unit within a stacked structure of pixel chip and logic chip. It can complete image recognition and inference at the sensor end, outputting only metadata, significantly reducing system power consumption and data bandwidth. It is suitable for robot vision, intelligent surveillance, and embodied intelligent edge devices.

## Product Image

> Sony IMX500 Intelligent Vision Sensor: Please visit the [official page](https://www.sony-semicon.co.jp/products/common/IMX500.html) for details.

## Specification Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Type | Stacked CMOS Image Sensor + AI Inference | Official website/datasheet |
| Effective Pixels | Approx. 12.3 million (4056 × 3040) | Official website/datasheet |
| Optical Format | 1/2.3 type | Official website/datasheet |
| Pixel Size | Not disclosed | - |
| Shutter | Rolling Shutter | Official website/datasheet |
| Maximum Frame Rate | Not disclosed | - |
| AI Capability | On-sensor AI model inference | Official website/datasheet |
| Output Format | Metadata / Image + Metadata | Official website/datasheet |
| Interface | MIPI D-PHY / SLVS-EC | Official website/datasheet |
| Power Supply | Not disclosed | - |
| Power Consumption | Not disclosed | - |
| Operating Temperature | Not disclosed | - |
| Package | COB / CSP | Official website/datasheet |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Sony Semiconductor Solutions](../companies/company_sony_semiconductor.md)
- **Core Components/Technology Source**: Self-developed stacked pixel chip, AI processing logic chip, DRAM, ISP algorithm, reference design, and model toolchain.
- **Downstream Applications/Customers**: Robot OEMs, smart camera manufacturers, security surveillance, industrial vision integrators, automotive Tier 1, consumer electronics brands.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_sony_semiconductor_imx500`
- Component Entity: `ent_component_sony_semiconductor_imx500_sensor`
- Manufacturer Entity: `ent_company_sony_semiconductor`
- Key Relationships:
  - `rel_ent_company_sony_semiconductor_manufactures_ent_product_sony_semiconductor_imx500` (`ent_company_sony_semiconductor` → `manufactures` → `ent_product_sony_semiconductor_imx500`)
  - `rel_ent_company_sony_semiconductor_manufactures_ent_component_sony_semiconductor_imx500_sensor` (`ent_company_sony_semiconductor` → `manufactures` → `ent_component_sony_semiconductor_imx500_sensor`)
  - `rel_ent_product_sony_semiconductor_imx500_uses_ent_component_sony_semiconductor_imx500_sensor` (`ent_product_sony_semiconductor_imx500` → `uses` → `ent_component_sony_semiconductor_imx500_sensor`)

## Application Scenarios

- **Robot Visual Perception**: Low-latency object recognition and localization, reducing main controller computing load.
- **Intelligent Surveillance**: Outputs only event metadata, protecting privacy and reducing storage costs.
- **Industrial Quality Inspection**: Edge AI real-time defect classification and assembly verification.
- **Embodied Intelligence**: End-side perception-decision closed loop, reducing system response latency.

## Competitive Comparison

| Comparison Item | This Product | Main Competitor A | Main Competitor B |
|----------------|--------------|-------------------|-------------------|
| Type | Intelligent Vision Sensor | GalaxyCore GC32E2 | OmniVision OX08D10 |
| AI Location | On-sensor Inference | ISP/SoC Side | ISP/SoC Side |
| Output | Metadata/Image+Metadata | RAW Image | RAW Image |
| Core Advantage | Low power, low bandwidth, privacy | High pixel count, low cost | Automotive high dynamic range |

## Selection and Deployment Recommendations

- Select the specific model based on the resolution, range, accuracy, or computing power requirements of the target application.
- Confirm interface, power supply, heat dissipation, mechanical installation, and ambient temperature range compatibility before deployment.
- It is recommended to obtain the latest firmware, SDK, and technical support through official channels or authorized distributors.

## Related Entries

- [Manufacturer: Sony Semiconductor Solutions](../companies/company_sony_semiconductor.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [Sony Semiconductor Solutions Official Website](https://www.sony-semicon.co.jp)
2. [Sony IMX500 Intelligent Vision Sensor Product/Data Page](https://www.sony-semicon.co.jp/products/common/IMX500.html)
3. Product datasheet and public technical reports
4. [Appendix D Company Directory](../index-companies.md)
