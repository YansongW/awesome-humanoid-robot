# Sunny Optical Automotive / Robot Camera Module

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update date: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed".

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Sunny Optical](../companies/company_shunyu.md) |
| **Product Category** | Automotive-grade camera module |
| **Release Date** | Continuously on sale / iterating |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [Sunny Optical Automotive / Robot Camera Module Product/Information Page](https://www.sunnyoptical.com/en/pro/009017006/index.html) |

## Product Overview

Sunny Optical's automotive/robot camera modules are designed for ADAS, smart cockpits, and embodied intelligent robot vision scenarios. They integrate self-developed glass-plastic hybrid lenses, CMOS image sensors, and ISP tuning, offering high reliability, a wide temperature range, and IP67/IP69K protection ratings. The modules support high-speed serial interfaces such as GMSL2/FPD-Link III and can output high-definition images for object detection, lane recognition, SLAM, and hand-eye coordination.

## Product Image

> Sunny Optical Automotive / Robot Camera Module: Please visit the [official page](https://www.sunnyoptical.com/en/pro/009017006/index.html) for details.

## Specification Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Type | Automotive-grade camera module | Official product information |
| Resolution | 2MP / 3MP / 8MP multiple models | Official product information |
| Sensor | 1/2.7" – 1/2.3" CMOS | Official product information |
| Field of View | 30° – 120° (varies by model) | Official product information |
| Lens | Glass-plastic hybrid high-resolution lens | Official product information |
| Interface | GMSL2 / FPD-Link III / Coaxial | Official product information |
| Frame Rate | Up to 60 fps (varies by resolution and interface) | Official product information |
| Protection Rating | IP67 / IP69K | Official product information |
| Operating Temperature | -40°C – +85°C | Official product information |
| Power Supply | 12 V DC (typical) | Official product information |
| Weight | Approx. 50 – 150 g | Official product information |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Sunny Optical](../companies/company_shunyu.md)
- **Core Components/Technology Sources**: CMOS image sensor, optical lens, voice coil motor, FPC/PCB, ISP chip, structural parts
- **Downstream Applications/Customers**: Smartphone OEMs, Automotive OEMs/Tier1, Robot manufacturers, AR/VR vendors

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_shunyu_automotive_camera_module`
- Component Entity: `ent_component_shunyu_camera_module_core`
- Manufacturer Entity: `ent_company_shunyu`
- Key Relationships:
  - `rel_ent_company_shunyu_manufactures_ent_product_shunyu_automotive_camera_module` (`ent_company_shunyu` → `manufactures` → `ent_product_shunyu_automotive_camera_module`)
  - `rel_ent_company_shunyu_manufactures_ent_component_shunyu_camera_module_core` (`ent_company_shunyu` → `manufactures` → `ent_component_shunyu_camera_module_core`)
  - `ent_product_shunyu_automotive_camera_module` -- `uses` --> `ent_component_shunyu_camera_module_core`

## Application Scenarios

- **Humanoid robot / service robot visual guidance, autonomous driving perception, smart cockpit DMS/OMS, industrial inspection**

## Competitive Comparison

| Comparison Item | This Product | Main Competitor A | Main Competitor B |
|----------------|--------------|-------------------|-------------------|
| Type | See specification table | Similar product | Similar product |
| Core Advantage | Official public performance indicators | Competitor's public indicators | Competitor's public indicators |
| Ecosystem/Service | Manufacturer's official support | Competitor's ecosystem | Competitor's ecosystem |

## Selection and Deployment Recommendations

- Select the specific model based on the resolution, range, accuracy, or computing power requirements of the target application.
- Before deployment, confirm that the interface, power supply, heat dissipation, mechanical installation, and ambient temperature range are compatible.
- It is recommended to obtain the latest firmware, SDK, and technical support through official channels or authorized distributors.

## Related Entries

- [Manufacturer: Sunny Optical](../companies/company_shunyu.md)
- [Appendix D.4 Key Product Wiki](../index-products.md)

## References

1. [Sunny Optical Official Website](https://www.sunnyoptical.com)
2. [Sunny Optical Automotive / Robot Camera Module Product/Information Page](https://www.sunnyoptical.com/en/pro/009017006/index.html)
3. Product datasheets and public technical reports
4. [Appendix D Company Directory](../index-companies.md)
