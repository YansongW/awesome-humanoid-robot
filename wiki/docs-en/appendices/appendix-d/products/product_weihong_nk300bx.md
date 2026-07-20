# Weihong NK300BX Motion Controller

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Weihong](../companies/company_weihong.md) |
| **Product Category** | Motion Controller / CNC Control System |
| **Release Date** | Continuously iterated since the 2010s |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [https://www.weihong.com.cn](https://www.weihong.com.cn) |

## Product Overview

The Weihong NK300BX is an integrated multi-axis motion controller designed for engraving machines, cutting machines, small CNC equipment, and automation devices.

The product integrates motion control, PLC logic, and HMI interface into one unit, supporting up to 6 axes of control. It offers rich process packages and secondary development interfaces, and is widely used in woodworking, advertising, metal processing, and 3C industries. Its high cost-effectiveness and ease of use make it a mainstream control solution for domestic engraving machines and small CNC equipment.

## Product Image

> Weihong NK300BX: Please visit [Official Materials](https://www.weihong.com.cn) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Product Form | Multi-axis integrated motion controller | Weihong official website |
| Number of Control Axes | Up to 6 axes | Product manual |
| Number of Simultaneous Axes | 3/4/5 axes (depending on configuration) | Product manual |
| Control Accuracy | 0.001 mm (reference) | Product manual |
| Interpolation Method | Linear / Circular / Spline | Product manual |
| Communication Interface | Ethernet / USB | Product manual |
| Programming Language | G-code / Macro program | Product manual |
| Operating System | Embedded Linux / Windows | Product manual |
| Price | Not disclosed | Inquire for pricing |

## Supply Chain Position

- **Manufacturer**: [Weihong](../companies/company_weihong.md)
- **Core Components/Technology Source**: Self-developed motion control software and PLC kernel; industrial computers, display panels, FPGA/DSP, PCBs, connectors purchased externally.
- **Downstream Applications/Customers**: Engraving machine/cutting machine manufacturers, woodworking machinery, advertising equipment, 3C processing, small CNC equipment vendors.

## Knowledge Graph Nodes and Relationships

- Component entity: `ent_component_weihong_nk300bx`
- Manufacturer entity: `ent_company_weihong`
- Key relationship:
  - `rel_ent_company_weihong_manufactures_ent_component_weihong_nk300bx` (`ent_company_weihong` → `manufactures` → `ent_component_weihong_nk300bx`)

## Application Scenarios

- **Woodworking Engraving**: Processing of door panels, furniture, decorative carvings.
- **Advertising Cutting**: Cutting of acrylic, MDF, metal letters.
- **Mold Processing**: Processing of small molds, electrodes, parts.
- **3C Processing**: Processing of phone frames, metal parts, fixtures.

## Competitive Comparison

| Comparison Item | Weihong NK300BX | Beckhoff FSCUT4000 | Googol GUC Series |
|-----------------|-----------------|--------------------|--------------------|
| Positioning | Engraving/cutting/small CNC control | Dedicated laser cutting control | General multi-axis motion control |
| Number of Control Axes | Up to 6 axes | 4 axes | Multi-axis |
| Core Advantage | High cost-effectiveness, rich process packages | Strong laser process database | Open architecture, strong algorithms |
| Price | Not disclosed | Not disclosed | Not disclosed |

## Selection and Deployment Recommendations

- Select the appropriate configuration based on the number of axes, simultaneous axis requirements, and processing technology.
- For engraving and cutting equipment, it is recommended to use the process packages provided by Weihong to shorten commissioning time.
- It is recommended to obtain the latest software versions and technical support through Weihong's official channels.

## Related Entries

- [Manufacturer: Weihong](../companies/company_weihong.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [Weihong Official Website](https://www.weihong.com.cn)
2. Weihong NK300BX Product Manual
3. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
