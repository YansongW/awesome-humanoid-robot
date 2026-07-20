# Shenyuansheng MLL Series 6-Axis Force Sensor

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Shenyuansheng](../companies/company_shenyuan.md) |
| **Product Category** | Aluminum alloy analog 6-axis force/torque sensor |
| **Release Date** | Continuously on sale |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [Shenyuansheng MLL Series 6-Axis Force Sensor Product/Data Page](http://www.nbit6d.com/product/687.html) |

## Product Overview

The Shenyuansheng MLL Series is an aluminum alloy analog 6-axis force sensor designed for scientific instruments, precision testing, and robotic applications. It can simultaneously measure forces and torques in three orthogonal directions. The product features high stiffness, high resolution, and low crosstalk error. It can be optionally paired with the NST series data acquisition unit for digital output and real-time analysis.

## Product Image

> Shenyuansheng MLL Series 6-Axis Force Sensor: Please visit the [official page](http://www.nbit6d.com/product/687.html) for details.

## Specification Table

| Specification Item | Value | Notes/Source |
|-------------------|-------|--------------|
| Type | Aluminum alloy analog 6-axis force sensor | Shenyuansheng official website |
| Force measurement range (Fx/Fy/Fz) | 50 / 50 / 100 N (typical model) | Shenyuansheng official website |
| Torque measurement range (Mx/My/Mz) | 2 / 2 / 4 Nm (typical model) | Shenyuansheng official website |
| Accuracy | ≤ 0.5% FS | Shenyuansheng official website |
| Resolution | 24 bit (with data acquisition unit) | Shenyuansheng official website |
| Overload capacity | ≥ 300% FS | Shenyuansheng official website |
| Crosstalk error | ≤ 2% FS | Shenyuansheng official website |
| Power supply | 5 – 24 VDC | Shenyuansheng official website |
| Output | Analog / USB / RS485 (with data acquisition unit) | Shenyuansheng official website |
| Sampling frequency | Up to 1000 Hz | Shenyuansheng official website |
| Operating temperature | 0°C – +60°C | Shenyuansheng official website |
| Weight | Approx. 200 g (varies by model) | Shenyuansheng official website |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Shenyuansheng](../companies/company_shenyuan.md)
- **Core Components/Technology Source**: Aerospace aluminum alloy, strain gauges, signal conditioning chips, cables and connectors
- **Downstream Applications/Customers**: Collaborative robots, humanoid robots, medical robots, aerospace testing, university research

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_shenyuan_mll_6axis_sensor`
- Component Entity: `ent_component_shenyuan_mll_sensor_core`
- Manufacturer Entity: `ent_company_shenyuan`
- Key Relationships:
  - `rel_ent_company_shenyuan_manufactures_ent_product_shenyuan_mll_6axis_sensor` (`ent_company_shenyuan` → `manufactures` → `ent_product_shenyuan_mll_6axis_sensor`)
  - `rel_ent_company_shenyuan_manufactures_ent_component_shenyuan_mll_sensor_core` (`ent_company_shenyuan` → `manufactures` → `ent_component_shenyuan_mll_sensor_core`)
  - `ent_product_shenyuan_mll_6axis_sensor` -- `uses` --> `ent_component_shenyuan_mll_sensor_core`

## Application Scenarios

- **Collaborative robot drag teaching, humanoid robot wrist/ankle force control, medical surgical force feedback, 3C assembly, scientific experiments**

## Competitive Comparison

| Comparison Item | This Product | Main Competitor A | Main Competitor B |
|----------------|--------------|-------------------|-------------------|
| Type | See specification table | Similar product | Similar product |
| Core Advantage | Official public performance indicators | Competitor public indicators | Competitor public indicators |
| Ecosystem/Service | Manufacturer official support | Competitor ecosystem | Competitor ecosystem |

## Selection and Deployment Recommendations

- Select the specific model based on the resolution, range, accuracy, or computational requirements of the target application.
- Before deployment, confirm that the interface, power supply, heat dissipation, mechanical installation, and ambient temperature range are compatible.
- It is recommended to obtain the latest firmware, SDK, and technical support through official channels or authorized distributors.

## Related Entries

- [Manufacturer: Shenyuansheng](../companies/company_shenyuan.md)
- [Appendix D.4 Key Product Wiki](../index-products.md)

## References

1. [Shenyuansheng Official Website](https://www.shenyuansheng.com)
2. [Shenyuansheng MLL Series 6-Axis Force Sensor Product/Data Page](http://www.nbit6d.com/product/687.html)
3. Product datasheet and public technical reports
4. [Appendix D Company Directory](../index-companies.md)
