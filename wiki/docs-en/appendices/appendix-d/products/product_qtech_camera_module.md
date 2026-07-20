# Q-Tech Machine Vision / Automotive Camera Module

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Table of Contents](../index-products.md)
> Data update date: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Q-Tech](../companies/company_qtech.md) |
| **Product Category** | Machine Vision / Automotive-Grade Camera Module |
| **Release Date** | Continuously available / Iterative |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [Q-Tech Machine Vision / Automotive Camera Module Product/Information Page](https://www.qtechsmartvision.com/) |

## Product Overview

Q-Tech Machine Vision / Automotive Camera Modules target scenarios such as intelligent vehicle ADAS, drone aerial photography, service robot navigation, and industrial inspection. They utilize COB/COF high-reliability packaging, offer optional global shutter or rolling shutter CMOS, support MIPI or GMSL2 high-speed interfaces, and feature a wide temperature range and IP67 protection capability.

## Product Image

> Q-Tech Machine Vision / Automotive Camera Module: Please visit the [official information page](https://www.qtechsmartvision.com/) for details.

## Specification Table

| Specification Item | Value | Remarks/Source |
|--------------------|-------|----------------|
| Type | Machine Vision / Automotive-Grade Camera Module | Q-Tech Official Website |
| Resolution | 2MP / 5MP / 8MP Multiple Models | Q-Tech Official Website |
| Sensor | 1/2.8" – 1/2.3" CMOS | Q-Tech Official Website |
| Shutter | Global Shutter / Rolling Shutter (Optional) | Q-Tech Official Website |
| Field of View | 120° / 140° / Custom | Q-Tech Official Website |
| Interface | MIPI / GMSL2 | Q-Tech Official Website |
| Protection Rating | IP67 (Automotive Models) | Q-Tech Official Website |
| Operating Temperature | -40°C – +85°C | Q-Tech Official Website |
| Power Supply | 12 V DC (Typical) | Q-Tech Official Website |
| Weight | Approx. 30 – 80 g | Q-Tech Official Website |
| Price | Not Disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Q-Tech](../companies/company_qtech.md)
- **Core Components/Technology Sources**: CMOS Image Sensor, Lens, Voice Coil Motor, FPC, Driver IC, Structural Components
- **Downstream Applications/Customers**: Smartphone OEMs, Automotive OEMs/Tier1, Drones, Robots, IoT Manufacturers

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_qtech_machine_vision_camera_module`
- Component Entity: `ent_component_qtech_camera_module_core`
- Manufacturer Entity: `ent_company_qtech`
- Key Relationships:
  - `rel_ent_company_qtech_manufactures_ent_product_qtech_machine_vision_camera_module` (`ent_company_qtech` → `manufactures` → `ent_product_qtech_machine_vision_camera_module`)
  - `rel_ent_company_qtech_manufactures_ent_component_qtech_camera_module_core` (`ent_company_qtech` → `manufactures` → `ent_component_qtech_camera_module_core`)
  - `ent_product_qtech_machine_vision_camera_module` -- `uses` --> `ent_component_qtech_camera_module_core`

## Application Scenarios

- **Industrial Robot Vision Inspection, Drone Aerial Photography, Intelligent Vehicle Surround View / Forward View, Service Robot SLAM**

## Competitive Comparison

| Comparison Item | This Product | Main Competitor A | Main Competitor B |
|-----------------|--------------|-------------------|-------------------|
| Type | See Specification Table | Similar Product | Similar Product |
| Core Advantage | Official Public Performance Indicators | Competitor Public Indicators | Competitor Public Indicators |
| Ecosystem/Service | Manufacturer Official Support | Competitor Ecosystem | Competitor Ecosystem |

## Selection and Deployment Recommendations

- Select the specific model based on the resolution, range, accuracy, or computing power requirements of the target application.
- Before deployment, confirm that the interface, power supply, heat dissipation, mechanical installation, and ambient temperature range are compatible.
- It is recommended to obtain the latest firmware, SDK, and technical support through official channels or authorized distributors.

## Related Entries

- [Manufacturer: Q-Tech](../companies/company_qtech.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [Q-Tech Official Website](https://www.qtechsmartvision.com)
2. [Q-Tech Machine Vision / Automotive Camera Module Product/Information Page](https://www.qtechsmartvision.com/)
3. Product datasheets and public technical reports
4. [Appendix D Company Directory](../index-companies.md)
