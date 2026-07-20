# OFILM 3D ToF Depth Camera Module

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update date: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [OFILM](../companies/company_ofilm.md) |
| **Product Category** | Time-of-Flight 3D Depth Camera Module |
| **Release Date** | Continuously available/iterated |
| **Status** | Mass production/commercial |
| **Official Website/Source** | [OFILM 3D ToF Depth Camera Module Product/Information Page](http://www.ofilm.com/en/products_inner1_39.html) |

## Product Overview

The OFILM 3D ToF Depth Camera Module is based on the Time-of-Flight principle. It uses a 940 nm VCSEL to emit modulated infrared light and receives the reflected light, outputting depth maps and point clouds in real time. The module can integrate an RGB camera for RGB-D alignment and is widely used for obstacle avoidance in robot vacuums, service robot navigation, AR/VR gesture interaction, and facial recognition.

## Product Image

> OFILM 3D ToF Depth Camera Module: Please visit the [official page](http://www.ofilm.com/en/products_inner1_39.html) for details.

## Specification Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Type | Time-of-Flight 3D Depth Camera Module | OFILM official website |
| Depth Resolution | VGA / QVGA (varies by model) | OFILM official website |
| RGB Resolution | Optional 2MP / 5MP | OFILM official website |
| Light Source | 940 nm VCSEL | OFILM official website |
| Field of View | 60°×45° / 70°×54° (typical) | OFILM official website |
| Range | 0.3 – 5 m | OFILM official website |
| Accuracy | Approx. 1% @ 1 m | OFILM official website |
| Frame Rate | Up to 30 fps | OFILM official website |
| Interface | MIPI / USB2.0 | OFILM official website |
| Power Supply | 3.3 V / 5 V DC | OFILM official website |
| Operating Temperature | -20℃ – +70℃ | OFILM official website |
| Weight | Not disclosed | - |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [OFILM](../companies/company_ofilm.md)
- **Core Components/Technology Sources**: VCSEL, ToF image sensor, DOE/optical lens, ISP, PCB/FPC, structural parts
- **Downstream Applications/Customers**: Smartphones, intelligent robots, AR/VR, smart home, automotive electronics

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_ofilm_tof_3d_module`
- Component Entity: `ent_component_ofilm_tof_module_core`
- Manufacturer Entity: `ent_company_ofilm`
- Key Relationships:
  - `rel_ent_company_ofilm_manufactures_ent_product_ofilm_tof_3d_module` (`ent_company_ofilm` → `manufactures` → `ent_product_ofilm_tof_3d_module`)
  - `rel_ent_company_ofilm_manufactures_ent_component_ofilm_tof_module_core` (`ent_company_ofilm` → `manufactures` → `ent_component_ofilm_tof_module_core`)
  - `ent_product_ofilm_tof_3d_module` -- `uses` --> `ent_component_ofilm_tof_module_core`

## Application Scenarios

- **Obstacle avoidance for robot vacuums, service robot navigation, AR/VR gestures, facial/biometric recognition, industrial 3D inspection**

## Competitive Comparison

| Comparison Item | This Product | Main Competitor A | Main Competitor B |
|----------------|--------------|-------------------|-------------------|
| Type | See specification table | Similar product | Similar product |
| Core Advantage | Officially disclosed performance metrics | Competitor's disclosed metrics | Competitor's disclosed metrics |
| Ecosystem/Service | Manufacturer's official support | Competitor's ecosystem | Competitor's ecosystem |

## Selection and Deployment Recommendations

- Select the specific model based on the resolution, range, accuracy, or computational requirements of the target application.
- Before deployment, confirm that the interface, power supply, heat dissipation, mechanical installation, and ambient temperature range are compatible.
- It is recommended to obtain the latest firmware, SDK, and technical support through official channels or authorized distributors.

## Related Entries

- [Manufacturer: OFILM](../companies/company_ofilm.md)
- [Appendix D.4 Key Product Wiki](../index-products.md)

## References

1. [OFILM Official Website](http://www.ofilm.com)
2. [OFILM 3D ToF Depth Camera Module Product/Information Page](http://www.ofilm.com/en/products_inner1_39.html)
3. Product datasheets and publicly available technical reports
4. [Appendix D Company Directory](../index-companies.md)
