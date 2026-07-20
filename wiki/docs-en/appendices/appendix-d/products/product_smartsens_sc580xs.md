# SmartSens SC580XS CMOS Image Sensor

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Table of Contents](../index-products.md)
> Data update date: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [SmartSens](../companies/company_smartsens.md) |
| **Product Category** | 50MP flagship smartphone/machine vision CMOS image sensor |
| **Release Date** | Released/mass production in 2024 |
| **Status** | Mass production/commercial |
| **Official Website/Source** | [SmartSens SC580XS CMOS Image Sensor Product/Data Page](https://www.smartsenstech.com/en/m) |

## Product Overview

The SmartSens SC580XS is a 50-megapixel 1/1.28-inch CMOS image sensor designed for flagship smartphone main cameras. It adopts 22 nm HKMG Stack process and SFCPixel®-2 technology, integrating PixGain HDR®, AllPix ADAF®, and Sparse PDAF, balancing high dynamic range, low noise, and full-pixel autofocus capability.

## Product Image

> SmartSens SC580XS CMOS Image Sensor: Please visit the [official page](https://www.smartsenstech.com/en/m) for details.

## Specification Table

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | 50MP CMOS image sensor | SmartSens official website |
| Effective Pixels | 50 MP | SmartSens official website |
| Pixel Size | 1.22 µm | SmartSens official website |
| Optical Format | 1/1.28" | SmartSens official website |
| Process | 22 nm HKMG Stack | SmartSens official website |
| HDR | PixGain HDR® / Triple exposure HDR | SmartSens official website |
| Dynamic Range | Up to 120 dB | SmartSens official website |
| Readout Noise | As low as 0.7 e⁻ | SmartSens official website |
| Autofocus | AllPix ADAF® / Sparse PDAF | SmartSens official website |
| Video | 4K 120 fps (4-cell binning mode) | SmartSens official website |
| Interface | MIPI C-PHY / D-PHY | SmartSens official website |
| Power Consumption | Approx. 500 mW at 50MP@25fps | SmartSens official website |
| Operating Temperature | -20°C – +70°C | SmartSens official website |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [SmartSens](../companies/company_smartsens.md)
- **Core Components/Technology Sources**: Wafer foundry, packaging and testing, optical lens, filter, ISP algorithm
- **Downstream Applications/Customers**: Smartphone OEMs, security camera manufacturers, automotive Tier1 suppliers, robotics, industrial cameras

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_smartsens_sc580xs`
- Component Entity: `ent_component_smartsens_sc580xs_sensor`
- Manufacturer Entity: `ent_company_smartsens`
- Key Relationships:
  - `rel_ent_company_smartsens_manufactures_ent_product_smartsens_sc580xs` (`ent_company_smartsens` → `manufactures` → `ent_product_smartsens_sc580xs`)
  - `rel_ent_company_smartsens_manufactures_ent_component_smartsens_sc580xs_sensor` (`ent_company_smartsens` → `manufactures` → `ent_component_smartsens_sc580xs_sensor`)
  - `ent_product_smartsens_sc580xs` -- `uses` --> `ent_component_smartsens_sc580xs_sensor`

## Application Scenarios

- **Flagship smartphone main camera, ultra-wide-angle, robot vision, industrial inspection, drone aerial photography**

## Competitive Comparison

| Comparison Item | This Product | Main Competitor A | Main Competitor B |
|-----------------|--------------|-------------------|-------------------|
| Type | See specification table | Similar product | Similar product |
| Core Advantage | Official public performance metrics | Competitor's public metrics | Competitor's public metrics |
| Ecosystem/Service | Manufacturer's official support | Competitor's ecosystem | Competitor's ecosystem |

## Selection and Deployment Recommendations

- Select the specific model based on the resolution, range, accuracy, or computing power requirements of the target application.
- Confirm interface, power supply, heat dissipation, mechanical installation, and ambient temperature range compatibility before deployment.
- It is recommended to obtain the latest firmware, SDK, and technical support through official channels or authorized distributors.

## Related Entries

- [Manufacturer: SmartSens](../companies/company_smartsens.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [SmartSens Official Website](https://www.smartsenstech.com)
2. [SmartSens SC580XS CMOS Image Sensor Product/Data Page](https://www.smartsenstech.com/en/m)
3. Product datasheet and public technical reports
4. [Appendix D Company Directory](../index-companies.md)
