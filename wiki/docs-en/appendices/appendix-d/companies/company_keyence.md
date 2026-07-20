# Keyence

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 基恩士 |
| **English Name** | Keyence |
| **Headquarters** | Osaka, Japan |
| **Founded** | 1974 |
| **Website** | [https://www.keyence.com](https://www.keyence.com) |
| **Supply Chain Role** | Industrial sensors, machine vision, measurement instruments, barcode readers, PLC |
| **Company Type** | Publicly traded (Tokyo Stock Exchange: 6861 / New York Stock Exchange: KYCCF), global FA leader |
| **Parent/Group** | Independently listed |
| **Data Source** | Keyence official website, annual reports, product datasheets |

## Company Overview

Keyence is a globally leading supplier of factory automation (FA) sensors, measurement instruments, machine vision systems, and barcode readers, known for its direct sales model, high-value-added products, and rapid response service.

The company's product portfolio covers sensors, laser markers, machine vision systems, microscopes, measurement instruments, PLCs, and data acquisition equipment, widely used in industries such as automotive, electronics, semiconductors, food, pharmaceuticals, and logistics. Keyence has a strong product matrix in industrial barcode reading, dimensional measurement, defect detection, and position detection, making it an important vision and sensing supplier for robots and automated production lines.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Industrial Sensors | Photoelectric/Laser/Proximity/Fiber optic sensors | PZ-G / LR-Z / GT2 series | Automated production lines, robotics |
| Machine Vision | Smart cameras and image processing | CV-X / XG-X series | Defect detection, dimensional measurement |
| Industrial Barcode Readers | Barcode/QR code reading | SR-X100 / SR-X300 | Logistics, electronics, automotive traceability |
| Measurement Instruments | Laser displacement/profile measurement | LJ-X8000 / IX series | 3C, automotive, semiconductors |
| PLC/IO | Programmable logic controllers | KV-8000 / NR-X series | Factory automation |

## Representative Products

### Keyence SR-X100 AI Barcode Reader

> Keyence SR-X100: Please visit [official documentation](https://www.keyence.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | Standard AI barcode reader (1.4 megapixels) | Official datasheet |
| Image Sensor | CMOS image sensor | Official datasheet |
| Pixel Count | 1360 × 1024 | Official datasheet |
| Focus | Auto focus | Official datasheet |
| Illumination Source | High-brightness red LED | Official datasheet |
| Indicator Light Source | High-brightness green LED | Official datasheet |
| Supported 2D Codes | QR, MicroQR, DataMatrix, PDF417, Aztec, etc. | Official datasheet |
| Supported 1D Codes | CODE39, CODE128, EAN/UPC, etc. | Official datasheet |
| Minimum Resolution (2D Code) | 0.024 mm | Official datasheet |
| Minimum Resolution (Barcode) | 0.082 mm | Official datasheet |
| Reading Distance | 70 – 1000 mm | Official datasheet |
| Field of View | 74 mm × 55 mm (at 300 mm distance) | Official datasheet |
| Control Input/Output | 2 inputs / 3 outputs | Official datasheet |
| Communication Interfaces | Ethernet (100BASE-TX), RS-232C, USB 2.0 | Official datasheet |
| Supported Protocols | TCP/IP, EtherNet/IP, PROFINET, MC protocol, OPC UA, etc. | Official datasheet |
| Power Supply | 24 VDC +25%/-20% | Official datasheet |
| Power Consumption | Approx. 650 mA | Official datasheet |
| Protection Rating | IP65 / IP67 | Official datasheet |
| Operating Temperature | 0℃ – +45℃ | Official datasheet |
| Weight | Approx. 180 g | Official datasheet |
| Price | Not disclosed | - |

**Technical Highlights**: Auto focus, high-brightness multi-light source, AI filters (SR-X300 series), and rich communication protocols, suitable for high-speed and variable barcode reading scenarios.

**Application Scenarios**: Electronic PCB barcode reading, logistics sorting, automotive parts traceability, food and pharmaceutical packaging.

### Keyence LR-Z Series Laser Sensor

> Keyence LR-Z: Please visit [official documentation](https://www.keyence.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | Amplifier built-in CMOS laser sensor | Official datasheet |
| Detection Distance | Not disclosed | - |
| Detection Principle | Time-of-flight / Triangulation | Official datasheet |
| Features | High stability, resistant to color/angle/gloss effects | Official datasheet |
| Communication | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: CMOS laser technology enables high-precision detection, insensitive to target color, angle, and surface gloss variations.

**Application Scenarios**: Robot target detection, presence/absence detection on production lines, positioning, dimensional judgment.

## Supply Chain Position

- **Upstream Key Components/Materials**: CMOS sensors, lasers, LED lighting, optical lenses, FPGA/ASIC, structural parts
- **Downstream Customers/Application Scenarios**: Automotive, 3C electronics, semiconductors, food and pharmaceuticals, logistics and warehousing, robot OEMs
- **Main Competitors/Peers**: Cognex, Omron, SICK, Hikrobot, OPT

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_keyence`
- Product Entity: `ent_component_keyence_sr_x100`
- Product Entity: `ent_component_keyence_lr_z`
- Key Relationships:
  - `ent_company_keyence` -- `manufactures` --> `ent_component_keyence_sr_x100`
  - `ent_company_keyence` -- `manufactures` --> `ent_component_keyence_lr_z`
  - `ent_component_keyence_sr_x100` -- `used_in` --> `ent_product_logistics_sorting`

## References

1. [Keyence Official Website](https://www.keyence.com)
2. [Keyence SR-X100 Product Page](https://www.keyence.com.cn/products/barcode/barcode-readers/sr-x/models/sr-x100/)
3. [Keyence SR-X Series Specifications](https://www.keyence.com.my/products/barcode/barcode-readers/sr-x/specs/)
4. [Appendix D Product Catalog](../index-products.md)
