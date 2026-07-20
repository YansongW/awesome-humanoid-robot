# Kistler 9107B 3-Component Force Sensor

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Kistler](../companies/company_kistler.md) |
| **Product Category** | Piezoelectric 3-Component Force Sensor |
| **Release Date** | Continuously on sale |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [Kistler 9107B 3-Component Force Sensor Product/Data Page](https://www.kistler.com/en/products/force-sensors/9107b) |

## Product Overview

The 9107B is a compact piezoelectric 3-component force sensor from Kistler, capable of simultaneously measuring dynamic forces in three orthogonal directions: Fx, Fy, and Fz. Its high stiffness, high natural frequency, and extremely low crosstalk make it suitable for machining cutting force monitoring, robot end-effector force control, and structural testing.

## Product Image

> Kistler 9107B 3-Component Force Sensor: Please visit the [official page](https://www.kistler.com/en/products/force-sensors/9107b) for details.

## Specification Table

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | Piezoelectric 3-Component Force Sensor | Official website |
| Measurement Directions | Fx / Fy / Fz | Official website / Datasheet |
| Force Measurement Range (Fx/Fy) | Not disclosed | - |
| Force Measurement Range (Fz) | Not disclosed | - |
| Sensitivity | Not disclosed | - |
| Stiffness | High stiffness design | Official website / Datasheet |
| Natural Frequency | Not disclosed | - |
| Crosstalk | < ±1% (typical) | Official website / Datasheet |
| Operating Temperature | Not disclosed | - |
| Protection Class | Not disclosed | - |
| Output Interface | Piezoelectric charge output + compatible charge amplifier | Official website / Datasheet |
| Dimensions | Compact flange mounting | Official website / Datasheet |
| Weight | Not disclosed | - |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Kistler](../companies/company_kistler.md)
- **Core Components/Technology Source**: Piezoelectric quartz crystal sensing elements, preload mechanism, stainless steel housing, shielded cables, charge amplifier.
- **Downstream Applications/Customers**: Machine tool and tooling manufacturers, automotive testing laboratories, robot OEMs, aerospace research institutions, humanoid robot integrators.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_kistler_9107b`
- Component Entity: `ent_component_kistler_9107b_sensor`
- Manufacturer Entity: `ent_company_kistler`
- Key Relationships:
  - `rel_ent_company_kistler_manufactures_ent_product_kistler_9107b` (`ent_company_kistler` → `manufactures` → `ent_product_kistler_9107b`)
  - `rel_ent_company_kistler_manufactures_ent_component_kistler_9107b_sensor` (`ent_company_kistler` → `manufactures` → `ent_component_kistler_9107b_sensor`)
  - `rel_ent_product_kistler_9107b_uses_ent_component_kistler_9107b_sensor` (`ent_product_kistler_9107b` → `uses` → `ent_component_kistler_9107b_sensor`)

## Application Scenarios

- **Machining Cutting Force Monitoring**: Real-time three-directional cutting force analysis to optimize tool life and machining quality.
- **Robot End-Effector Force Control**: Dynamic force feedback during assembly, pressing, and grinding processes.
- **Structural Dynamic Testing**: High-stiffness sensor captures transient impact and vibration loads.
- **Humanoid Robot Foot**: Ground reaction force measurement during walking and balance control.

## Competitive Comparison

| Comparison Item | This Product | Main Competitor A | Main Competitor B |
|-----------------|--------------|-------------------|-------------------|
| Type | Piezoelectric 3-Component Force Sensor | ATI Mini Series | Kunwei KWR36 |
| Technology Principle | Piezoelectric Quartz | Silicon Strain Gauge | Metal Strain Gauge |
| Applicable Frequency Range | High-frequency dynamic | Medium-low frequency force control | Medium-low frequency force control |
| Core Advantage | High-frequency dynamic, low crosstalk | Mature robot integration | Miniature high precision |

## Selection and Deployment Recommendations

- Select the specific model based on the resolution, range, accuracy, or computational requirements of the target application.
- Confirm interface, power supply, cooling, mechanical installation, and ambient temperature range compatibility before deployment.
- It is recommended to obtain the latest firmware, SDK, and technical support through official channels or authorized distributors.

## Related Entries

- [Manufacturer: Kistler](../companies/company_kistler.md)
- [Appendix D.4 Key Product Wiki](../index-products.md)

## References

1. [Kistler Official Website](https://www.kistler.com)
2. [Kistler 9107B 3-Component Force Sensor Product/Data Page](https://www.kistler.com/en/products/force-sensors/9107b)
3. Product datasheet and public technical reports
4. [Appendix D Company Directory](../index-companies.md)
