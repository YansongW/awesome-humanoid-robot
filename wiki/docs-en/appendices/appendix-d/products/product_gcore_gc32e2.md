# GalaxyCore GC32E2 CMOS Image Sensor

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update date: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [GalaxyCore](../companies/company_gcore.md) |
| **Product Category** | 32MP CMOS Image Sensor |
| **Release Date** | Mass production in 2024 |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [GalaxyCore GC32E2 CMOS Image Sensor Product/Data Page](https://en.gcoreinc.com/news/detail-67) |

## Product Overview

The GalaxyCore GC32E2 is a second-generation high-performance single-chip 32MP CMOS image sensor, utilizing backside illumination (BSI) process and single-frame DAG HDR technology to preserve highlight and shadow details in preview, photo, and video modes. The sensor supports PDAF phase detection autofocus and AON low-power mode, suitable for smartphone front cameras and robot vision applications.

## Product Image

> GalaxyCore GC32E2 CMOS Image Sensor: Please visit the [official page](https://en.gcoreinc.com/news/detail-67) for details.

## Specification Table

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | 32MP CMOS Image Sensor | GalaxyCore Official Website |
| Effective Pixels | 32 MP | GalaxyCore Official Website |
| Pixel Size | 0.7 µm | GalaxyCore Official Website |
| Optical Format | 1/3.1" | GalaxyCore Official Website |
| Process | Backside Illumination (BSI) | GalaxyCore Official Website |
| Shutter | Rolling Shutter | GalaxyCore Official Website |
| HDR | Single-frame DAG HDR | GalaxyCore Official Website |
| Autofocus | PDAF Phase Detection Autofocus | GalaxyCore Official Website |
| Output Format | RAW 10 / 12 | GalaxyCore Official Website |
| Interface | MIPI D-PHY | GalaxyCore Official Website |
| Package | COB / COM | GalaxyCore Official Website |
| Frame Rate | Up to 15 fps (Full Resolution) | GalaxyCore Official Website |
| Operating Temperature | -20°C – +70°C | GalaxyCore Official Website |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [GalaxyCore](../companies/company_gcore.md)
- **Core Components/Technology Sources**: Wafer foundry, packaging and testing, color filter, microlens, substrate
- **Downstream Applications/Customers**: Smartphone OEMs, ODM, tablets, robots, IoT camera manufacturers

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_gcore_gc32e2`
- Component Entity: `ent_component_gcore_gc32e2_sensor`
- Manufacturer Entity: `ent_company_gcore`
- Key Relationships:
  - `rel_ent_company_gcore_manufactures_ent_product_gcore_gc32e2` (`ent_company_gcore` → `manufactures` → `ent_product_gcore_gc32e2`)
  - `rel_ent_company_gcore_manufactures_ent_component_gcore_gc32e2_sensor` (`ent_company_gcore` → `manufactures` → `ent_component_gcore_gc32e2_sensor`)
  - `ent_product_gcore_gc32e2` -- `uses` --> `ent_component_gcore_gc32e2_sensor`

## Application Scenarios

- **Smartphone front cameras, tablets, robot vision, wearable devices, video calls**

## Competitive Comparison

| Comparison Item | This Product | Main Competitor A | Main Competitor B |
|----------------|--------------|-------------------|-------------------|
| Type | See Specification Table | Similar Product | Similar Product |
| Core Advantage | Officially disclosed performance metrics | Competitor's disclosed metrics | Competitor's disclosed metrics |
| Ecosystem/Service | Manufacturer's official support | Competitor's ecosystem | Competitor's ecosystem |

## Selection and Deployment Recommendations

- Select the specific model based on the resolution, range, accuracy, or computing power requirements of the target application.
- Before deployment, confirm that the interface, power supply, cooling, mechanical installation, and ambient temperature range are compatible.
- It is recommended to obtain the latest firmware, SDK, and technical support through official channels or authorized distributors.

## Related Entries

- [Manufacturer: GalaxyCore](../companies/company_gcore.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [GalaxyCore Official Website](https://www.gcoreinc.com)
2. [GalaxyCore GC32E2 CMOS Image Sensor Product/Data Page](https://en.gcoreinc.com/news/detail-67)
3. Product datasheet and public technical reports
4. [Appendix D Company Directory](../index-companies.md)
