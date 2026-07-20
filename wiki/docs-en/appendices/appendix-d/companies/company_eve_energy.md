# EVE Energy

> This entry belongs to [Appendix D: Enterprise/Product Wiki](../../appendix-d.md).  
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 惠州亿纬锂能股份有限公司 |
| **English Name** | EVE Energy Co., Ltd. |
| **Headquarters** | Huizhou, Guangdong Province, China |
| **Founded** | 2001 |
| **Website** | [https://www.evebattery.com](https://www.evebattery.com) |
| **Supply Chain Role** | Lithium-ion batteries, cylindrical/prismatic/pouch cells, energy storage systems |
| **Enterprise Type** | Publicly listed company (Shenzhen Stock Exchange: 300014) |
| **Parent/Group** | None (independently listed) |
| **Data Source** | Company website, EVE Energy North America product specification page, public datasheets |

## Company Overview

EVE Energy is a leading lithium battery platform company in China, with products covering consumer batteries, power batteries, and energy storage batteries, in cylindrical, prismatic, and pouch formats.

The company's customers include BMW, Daimler, XPeng, Bosch, and others. Its large-capacity LFP prismatic cells are widely used in energy storage and commercial vehicle applications, and can also be used in humanoid robot backup power or chassis battery packs that require high cycle life.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Power Batteries | Cells and modules for passenger/commercial vehicles | LF150 / LF280K | Electric vehicles, special vehicles |
| Energy Storage Batteries | Large-capacity, long-cycle cells | LF280K / MB31 | Grid energy storage, commercial & industrial storage |
| Cylindrical Batteries | Power tools, light electric vehicles | 18650 / 21700 | Consumer/industrial electronics |

## Representative Product

### LF280K LFP Cell

![LF280K](https://www.evebatteryusa.com/copy-of-18650-and-21700-specifications)

> Image source: EVE Energy North America product page. If the link is invalid or missing, please replace with an official public image URL.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 173.7 × 71.7 × 207.2 mm | EVE public specification (reference from same series) |
| Weight | Approx. 5.42 kg | Public datasheet |
| Chemistry | Lithium Iron Phosphate (LFP) | EVE official website |
| Nominal Voltage | 3.2 V | EVE official website |
| Nominal Capacity | 280 Ah | EVE official website |
| Energy | 896 Wh | Calculated value |
| Energy Density | Approx. 165 Wh/kg | Public information |
| Cycle Life | ≥6000 cycles (25 °C) | EVE official website |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: Large-capacity prismatic LFP cell with long cycle life and high safety, suitable for energy storage and long-life mobile platforms.

**Application Scenarios**: Energy storage containers, commercial vehicle chassis, long-endurance battery packs for humanoid robots.

## Relevance to Humanoid Robots

- Batteries, power semiconductors, and advanced materials are common foundations for achieving long endurance, high dynamics, and lightweight design in humanoid robots.
- Industrial robots and automated production lines provide reusable manufacturing capabilities for the assembly, testing, and mass production of humanoid robots.

## Supply Chain Position

- **Upstream Key Components/Materials**: LFP cathode, graphite anode, separator, electrolyte, structural parts.
- **Downstream Customers/Applications**: BMW, Daimler, XPeng, Bosch, energy storage integrators.
- **Main Competitors/Peers**: CATL, BYD, Gotion High-tech, Sunwoda.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_eve_energy`
- Product Entity: `ent_component_eve_lf280k_cell`
- Key Relationship:
  - `ent_company_eve_energy` -- `manufactures` --> `ent_component_eve_lf280k_cell`

## References

1. [EVE Energy Official Website](https://www.evebattery.com)
2. [EVE Energy North America Product Specifications](https://www.evebatteryusa.com/copy-of-18650-and-21700-specifications)
3. [EVE INR18650/30P Datasheet Public Information](https://static.chipdip.ru/lib2/b/925/DOC073925143.pdf)
