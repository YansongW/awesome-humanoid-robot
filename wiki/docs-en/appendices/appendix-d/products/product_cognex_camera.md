# Cognex In-Sight 3800 Vision System

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Cognex](../companies/company_cognex.md) |
| **Product Category** | AI + Rule-Based Industrial Vision System |
| **Release Date** | Continuous iteration since 2024 |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [Cognex Official Website](https://www.cognex.com) |

## Product Overview

The Cognex In-Sight 3800 is a high-performance industrial vision system designed for high-speed manufacturing scenarios. It integrates AI edge learning (ViDi EL) with rule-based vision tools, enabling defect detection, OCR, assembly verification, and part classification on a single platform.

This system offers six resolution models from 1.4 MP to 16 MP, featuring a global shutter CMOS sensor with a maximum monochrome frame rate of 125 fps. It is equipped with multi-color RGBW+IR lighting, HDR+ high dynamic range, and an optional HSLL high-speed liquid lens. With an IP67 protection rating and support for multiple industrial Ethernet protocols, the In-Sight 3800 is a premium choice for automotive, electronics, food, medical, and robotic vision guidance applications.

## Product Image

> Cognex In-Sight 3800: Please visit [Official Resources](https://www.cognex.com) for details.

## Specifications Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | AI + Rule-Based Industrial Vision System | Official datasheet |
| Resolution | 1.4 / 3 / 5 / 8 / 12 / 16 MP (6 models) | Official datasheet |
| Sensor | 1/2.3" – 1.1" CMOS, Global Shutter | Official datasheet |
| Max Frame Rate (Monochrome/Color) | 125 fps / 52 fps (IS3801) | Official datasheet |
| Pixel Size | 3.45 μm / 2.74 μm | Official datasheet |
| Lens Mount | C-Mount | Official datasheet |
| Memory | 4 GB | Official datasheet |
| Image Processing Memory | 512 MB / 1 GB | Official datasheet |
| Lighting | Multi-color RGBW + IR, optional advanced lighting | Official datasheet |
| Dynamic Range | HDR+ | Official datasheet |
| Protection Rating | IP67 | Official datasheet |
| Communication Protocols | TCP/IP, PROFINET, EtherNet/IP, Modbus TCP, SLMP | Official datasheet |
| Power Supply | 24 V DC ± 10%, max 2.0 A | Official datasheet |
| Operating Temperature | 0°C – 40°C | Official datasheet |
| Weight | Approx. 570 g (bare unit) | Official datasheet |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Cognex](../companies/company_cognex.md)
- **Core Components/Technology Source**: Self-developed ViDi EL edge learning algorithm and In-Sight Vision Suite software; CMOS sensors, optical lenses, lighting modules, FPGA/SoC are externally sourced.
- **Downstream Applications/Customers**: Automotive, consumer electronics, semiconductors, food and pharmaceuticals, logistics and warehousing, robot OEMs.

## Knowledge Graph Nodes and Relationships

- Component Entity: `ent_component_cognex_insight_3800`
- Manufacturer Entity: `ent_company_cognex`
- Key Relationship:
  - `rel_ent_company_cognex_manufactures_ent_component_cognex_insight_3800` (`ent_company_cognex` → `manufactures` --> `ent_component_cognex_insight_3800`)

## Application Scenarios

- **Defect Detection**: Surface defect inspection of electronic components, automotive parts, and food packaging.
- **OCR and Traceability**: Laser etching, inkjet printing, label character recognition, and serial number management.
- **Assembly Verification**: Presence, position, orientation, and completeness checks of components.
- **Robotic Vision Guidance**: Grasping positioning and path planning for humanoid/industrial robots.

## Competitive Comparison

| Comparison Item | Cognex In-Sight 3800 | Keyence CV-X | Hikrobot MV-CS |
|-----------------|----------------------|--------------|----------------|
| Type | AI + Rule-Based Vision System | Smart Camera/Vision System | Industrial Camera/Vision System |
| Resolution | 1.4 – 16 MP | Multiple models | Multiple models |
| AI Capability | ViDi EL Edge Learning | Built-in AI Image Processing | AI Vision Algorithms |
| Protection Rating | IP67 | Varies by model | Varies by model |
| Core Advantage | International brand, mature ecosystem | Direct sales service, FA integration | Cost advantage, localization |

## Selection and Deployment Recommendations

- Select the resolution and frame rate model based on inspection field of view, accuracy, and production line speed, and confirm the lens and lighting configuration.
- For complex scenarios, it is recommended to first use EasyBuilder for rapid verification, then use spreadsheets for highly customized development.

## References

1. [Cognex Official Website](https://www.cognex.com)
2. [Cognex In-Sight 3800 Product Page](https://www.cognex.com/en-us/products/2d-machine-vision-systems/in-sight-3800)
3. [Cognex In-Sight 3800 Datasheet](https://www.cognex.com/en-us/tools-and-resources/resource-center/in-sight-3800-datasheet)
4. [Appendix D Company Directory](../index-companies.md)
