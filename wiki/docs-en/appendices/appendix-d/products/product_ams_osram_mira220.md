# ams OSRAM Mira220 NIR CMOS Image Sensor

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [ams OSRAM](../companies/company_ams_osram.md) |
| **Product Category** | Near-infrared enhanced global shutter CMOS image sensor |
| **Release Date** | Commercially available from 2022 |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [ams OSRAM Mira220 NIR CMOS Image Sensor Product/Data Page](https://ams-osram.com/products/sensors/area-imaging-sensors/ams-mira220) |

## Product Overview

The Mira220 is a 2.2 MP global shutter CMOS image sensor from ams OSRAM designed for 3D sensing and near-infrared imaging. It offers high quantum efficiency in the 850 nm and 940 nm NIR bands, supports low-power, high-frame-rate operation, and is an ideal photosensitive element for robot 3D vision, structured light/ToF cameras, and in-cabin monitoring.

## Product Image

> ams OSRAM Mira220 NIR CMOS Image Sensor: Please visit the [official page](https://ams-osram.com/products/sensors/area-imaging-sensors/ams-mira220) for details.

## Specification Table

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | NIR-enhanced global shutter CMOS | Official website/datasheet |
| Effective Pixels | 2.2 MP | Official website/datasheet |
| Resolution | Approx. 1920 × 1080 | Official website/datasheet |
| Optical Format | 1/2.7 type | Official website/datasheet |
| Pixel Size | 2.79 µm | Official website/datasheet |
| Shutter | Global shutter | Official website/datasheet |
| NIR QE | High quantum efficiency at 850/940 nm | Official website/datasheet |
| Max Frame Rate | Up to 90 fps | Official website/datasheet |
| Interface | MIPI CSI-2 | Official website/datasheet |
| Power Consumption | Not disclosed | - |
| Power Supply | Not disclosed | - |
| Operating Temperature | Not disclosed | - |
| Package | CSP | Official website/datasheet |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [ams OSRAM](../companies/company_ams_osram.md)
- **Core Components/Technology Source**: Self-developed NIR-enhanced pixels, global shutter readout circuit, MIPI interface, wafer-level optics (WLO) adaptation.
- **Downstream Applications/Customers**: 3D camera module manufacturers, robot OEMs, AR/VR device vendors, security surveillance, automotive Tier 1.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_ams_osram_mira220`
- Component Entity: `ent_component_ams_osram_mira220_sensor`
- Manufacturer Entity: `ent_company_ams_osram`
- Key Relationships:
  - `rel_ent_company_ams_osram_manufactures_ent_product_ams_osram_mira220` (`ent_company_ams_osram` → `manufactures` → `ent_product_ams_osram_mira220`)
  - `rel_ent_company_ams_osram_manufactures_ent_component_ams_osram_mira220_sensor` (`ent_company_ams_osram` → `manufactures` → `ent_component_ams_osram_mira220_sensor`)
  - `rel_ent_product_ams_osram_mira220_uses_ent_component_ams_osram_mira220_sensor` (`ent_product_ams_osram_mira220` → `uses` → `ent_component_ams_osram_mira220_sensor`)

## Application Scenarios

- **Robot 3D Vision**: Used with structured light/ToF projectors to obtain high-quality depth maps.
- **Face Recognition and Gesture**: High NIR QE improves recognition rates in low-light and strong-light conditions.
- **In-Cabin Monitoring**: Low-power continuous monitoring of driver/passenger status.
- **AR/VR Tracking**: High-speed global shutter reduces motion artifacts.

## Competitive Comparison

| Comparison Item | This Product | Main Competitor A | Main Competitor B |
|-----------------|--------------|-------------------|-------------------|
| Type | NIR global shutter CMOS | Sony IMX426 | Himax 3D Sensing |
| NIR Optimization | High QE at 850/940 nm | Supported in some models | Module-level solution |
| Shutter | Global shutter | Global shutter | Structured light/ToF |
| Core Advantage | Integrated emission+reception optics | High resolution | WLO miniaturization |

## Selection and Deployment Recommendations

- Select the specific model based on the resolution, range, accuracy, or computational requirements of the target application.
- Before deployment, confirm that the interface, power supply, cooling, mechanical mounting, and ambient temperature range are compatible.
- It is recommended to obtain the latest firmware, SDK, and technical support through official channels or authorized distributors.

## Related Entries

- [Manufacturer: ams OSRAM](../companies/company_ams_osram.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [ams OSRAM Official Website](https://ams-osram.com)
2. [ams OSRAM Mira220 NIR CMOS Image Sensor Product/Data Page](https://ams-osram.com/products/sensors/area-imaging-sensors/ams-mira220)
3. Product datasheet and public technical reports
4. [Appendix D Company Directory](../index-companies.md)
