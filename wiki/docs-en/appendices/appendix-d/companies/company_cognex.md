# Cognex

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 康耐视 |
| **English Name** | Cognex |
| **Headquarters** | Natick, Massachusetts, USA |
| **Founded** | 1981 |
| **Website** | [https://www.cognex.com](https://www.cognex.com) |
| **Supply Chain Role** | Machine vision systems, industrial barcode readers, deep learning vision software |
| **Company Type** | Public company (NASDAQ: CGNX), global leader in machine vision |
| **Parent/Group** | Independently listed |
| **Data Source** | Cognex official website, annual reports, product datasheets |

## Company Overview

Cognex is a leading global supplier of machine vision products, industrial barcode readers, and deep learning vision software, dedicated to helping manufacturers improve product quality, reduce production costs, and optimize traceability.

Cognex products are widely used in industries such as automotive, electronics, logistics, food and beverage, and medical pharmaceuticals. Its In-Sight series smart cameras, DataMan series barcode readers, and VisionPro software platform are benchmark products in the industrial vision field. With the development of humanoid robots and embodied intelligence, Cognex's high-resolution 3D vision and AI edge learning tools have also become important vision components for robot guidance, quality inspection, and sorting systems.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Smart Cameras/Vision Systems | 2D/3D inline inspection | In-Sight 3800 / 2800 / 9000 | Automotive, electronics, food, packaging |
| Industrial Barcode Readers | Barcode/QR code reading | DataMan 470 / 260 / 8700 | Logistics, electronics, automotive traceability |
| Vision Software | Deep learning and algorithm platform | VisionPro / ViDi EL | Defect detection, OCR, classification |
| 3D Vision | 3D measurement and guidance | In-Sight 3D-L4000 / VisionPro 3D | Robot guidance, assembly verification |

## Representative Products

### Cognex In-Sight 3800 Vision System

> Cognex In-Sight 3800: Please visit [official documentation](https://www.cognex.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | AI + rule-based industrial vision system | Official datasheet |
| Resolution | 1.4 / 3 / 5 / 8 / 12 / 16 MP (multiple models) | Official datasheet |
| Sensor | 1/2.3" – 1.1" CMOS, global shutter | Official datasheet |
| Frame Rate (Monochrome/Color) | Up to 125 fps / 52 fps (IS3801) | Official datasheet |
| Pixel Size | 3.45 μm / 2.74 μm | Official datasheet |
| Lens Mount | C-mount | Official datasheet |
| Memory | 4 GB | Official datasheet |
| Image Processing Memory | 512 MB / 1 GB | Official datasheet |
| Lighting | Multi-color RGBW + IR, optional advanced lighting | Official datasheet |
| Ingress Protection | IP67 | Official datasheet |
| Communication Protocols | TCP/IP, PROFINET, EtherNet/IP, Modbus TCP, SLMP | Official datasheet |
| Operating Temperature | 0°C – 40°C | Official datasheet |
| Power Supply | 24 V DC ± 10%, max 2.0 A | Official datasheet |
| Weight | Approx. 570 g (bare unit) | Official datasheet |
| Price | Not disclosed | - |

**Technical Highlights**: ViDi EL edge learning + rule-based tool dual engine, HDR+ high dynamic range, HSLL high-speed liquid lens, capable of handling complex inspections on high-speed production lines.

**Application Scenarios**: Defect detection, OCR, assembly verification, part classification, robot vision guidance, humanoid robot vision perception.

### Cognex DataMan 470 Industrial Barcode Reader

> Cognex DataMan 470: Please visit [official documentation](https://www.cognex.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | High-speed, large field-of-view industrial barcode reader | Official datasheet |
| Resolution | Multiple models available | Official datasheet |
| Read Speed | Up to 120 fps | Official datasheet |
| Code Reading Capability | 1D/2D/DPM codes | Official datasheet |
| Lighting | Multi-zone illumination, HDR | Official datasheet |
| Communication | TCP/IP, PROFINET, EtherNet/IP | Official datasheet |
| Ingress Protection | IP65 / IP67 | Official datasheet |
| Price | Not disclosed | - |

**Technical Highlights**: Multi-core parallel processing and advanced algorithms enable large field-of-view and deep depth-of-field reading on high-speed moving production lines.

**Application Scenarios**: Logistics sorting, automotive manufacturing traceability, electronic component traceability, warehouse management.

## Supply Chain Position

- **Upstream Key Components/Materials**: CMOS image sensors, optical lenses, LED/laser lighting, FPGA/SoC processing chips, heat sinks and structural parts
- **Downstream Customers/Application Scenarios**: Automotive, consumer electronics, semiconductors, logistics and warehousing, food and beverage, medical, robot OEMs
- **Main Competitors/Peers**: Keyence, Omron, Hikrobot, OPT, Basler

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_cognex`
- Product Entity: `ent_component_cognex_insight_3800`
- Product Entity: `ent_component_cognex_dataman_470`
- Key Relationships:
  - `ent_company_cognex` -- `manufactures` --> `ent_component_cognex_insight_3800`
  - `ent_company_cognex` -- `manufactures` --> `ent_component_cognex_dataman_470`
  - `ent_component_cognex_insight_3800` -- `used_in` --> `ent_product_industrial_robot_vision`

## References

1. [Cognex Official Website](https://www.cognex.com)
2. [Cognex In-Sight 3800 Product Page](https://www.cognex.com/zh-cn/products/2d-machine-vision-systems/in-sight-3800)
3. [Cognex In-Sight 3800 Datasheet](https://www.cognex.cn/zh-cn/tools-and-resources/resource-center/in-sight-3800-datasheet)
4. [Appendix D Product Catalog](../index-products.md)
