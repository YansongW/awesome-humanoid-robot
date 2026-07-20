# Keyence SR-X100 AI Code Reader

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Table of Contents](../index-products.md)
> Data update date: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Keyence](../companies/company_keyence.md) |
| **Product Category** | Industrial AI Code Reader / Vision Sensor |
| **Release Date** | Continuously on sale |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [Keyence Official Website](https://www.keyence.com) |

## Product Overview

The Keyence SR-X100 is a standard 1.4-megapixel AI code reader, featuring a built-in CMOS image sensor, high-brightness red LED illumination, and an auto-focus mechanism. It can quickly read QR codes, DataMatrix, PDF417, Aztec, and common 1D barcodes.

The SR-X100 supports a reading distance of 70 – 1000 mm, with a minimum QR code resolution of 0.024 mm. It offers multiple communication interfaces including Ethernet, RS-232C, and USB 2.0, and is compatible with EtherNet/IP, PROFINET, MC protocol, and OPC UA. Its IP65/IP67 protection rating and compact body (approx. 180 g) make it suitable for demanding industrial environments such as electronics, automotive, logistics, and robotics.

## Product Image

> Keyence SR-X100: Please visit the [official documentation](https://www.keyence.com) for details.

## Specifications Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Type | Standard AI Code Reader | Official datasheet |
| Image Sensor | CMOS Image Sensor | Official datasheet |
| Pixels | 1360 × 1024 (1.4 megapixels) | Official datasheet |
| Focus | Auto-focus | Official datasheet |
| Illumination Source | High-brightness Red LED | Official datasheet |
| Indicator Light Source | High-brightness Green LED | Official datasheet |
| Supported 2D Codes | QR, MicroQR, DataMatrix, PDF417, Aztec, etc. | Official datasheet |
| Supported 1D Codes | CODE39, CODE128, EAN/UPC, etc. | Official datasheet |
| Minimum Resolution (2D Code) | 0.024 mm | Official datasheet |
| Minimum Resolution (Barcode) | 0.082 mm | Official datasheet |
| Reading Distance | 70 – 1000 mm | Official datasheet |
| Field of View | 74 mm × 55 mm (at 300 mm distance) | Official datasheet |
| Control Input/Output | 2 inputs / 3 outputs | Official datasheet |
| Communication Interface | Ethernet (100BASE-TX), RS-232C, USB 2.0 | Official datasheet |
| Supported Protocols | TCP/IP, EtherNet/IP, PROFINET, MC Protocol, OPC UA, etc. | Official datasheet |
| Power Supply | 24 VDC +25%/-20% | Official datasheet |
| Power Consumption | Approx. 650 mA | Official datasheet |
| Protection Rating | IP65 / IP67 | Official datasheet |
| Operating Temperature | 0℃ – +45℃ | Official datasheet |
| Weight | Approx. 180 g | Official datasheet |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Keyence](../companies/company_keyence.md)
- **Core Component/Technology Source**: Self-developed image processing algorithms and auto-focus technology; CMOS sensor, LED illumination, optical lens, and communication chips are externally sourced.
- **Downstream Applications/Customers**: Electronics manufacturing, automotive, logistics and warehousing, food and pharmaceuticals, robotics OEM.

## Knowledge Graph Nodes and Relationships

- Component Entity: `ent_component_keyence_sr_x100`
- Manufacturer Entity: `ent_company_keyence`
- Key Relationship:
  - `rel_ent_company_keyence_manufactures_ent_component_keyence_sr_x100` (`ent_company_keyence` → `manufactures` --> `ent_component_keyence_sr_x100`)

## Application Scenarios

- **Electronics Manufacturing**: PCB QR code reading, SMT traceability, component identification.
- **Logistics and Warehousing**: Fast package barcode scanning, batch code reading on sorting lines.
- **Automotive Traceability**: Laser marking of parts, assembly process traceability.
- **Food and Pharmaceuticals**: Packaging lot numbers, expiration date OCR and traceability management.

## Competitive Comparison

| Comparison Item | Keyence SR-X100 | Cognex DataMan 260 | Hikrobot MV-ID |
|----------------|-----------------|--------------------|-----------------|
| Pixels | 1.4 megapixels | Multiple models | Multiple models |
| Reading Distance | 70 – 1000 mm | Varies by model | Varies by model |
| Minimum Resolution (2D Code) | 0.024 mm | Varies by model | Varies by model |
| Communication Protocols | EtherNet/IP, PROFINET, OPC UA, etc. | Rich | Rich |
| Protection Rating | IP65/IP67 | IP65/IP67 | Varies by model |
| Core Advantage | Auto-focus, FA ecosystem integration | Deep learning code reading | Cost advantage, localization |

## Selection and Deployment Recommendations

- When selecting, confirm the barcode type, minimum module size, reading distance, and production line speed, and verify the impact of on-site lighting and vibration.
- For low-contrast, reflective, or damaged barcodes, consider evaluating the SR-X300 series version with built-in AI filters.

## References

1. [Keyence Official Website](https://www.keyence.com)
2. [Keyence SR-X100 Product Page](https://www.keyence.com.cn/products/barcode/barcode-readers/sr-x/models/sr-x100/)
3. [Keyence SR-X Series Specifications](https://www.keyence.com.my/products/barcode/barcode-readers/sr-x/specs/)
4. [Appendix D Company Directory](../index-companies.md)
