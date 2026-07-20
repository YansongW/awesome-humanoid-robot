# Sanhua Thermal Management Components

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Sanhua Intelligent Controls / Sanhua](../companies/company_sanhua.md) |
| **Product Category** | Thermal management valves/heat exchangers/actuator cooling components |
| **Release Date** | Continuously iterated; robot solutions disclosed around 2024 |
| **Status** | Mass production (automotive/refrigeration); robot solutions under development |
| **Website/Source** | See references in the main text |

## Product Overview

Sanhua thermal management components cover electronic expansion valves, solenoid valves, electronic water pumps, Chillers, microchannel heat exchangers, and integrated thermal management modules. Leveraging its global leading position in new energy vehicle thermal management, Sanhua extends its precision fluid control and thermal management technologies to robot actuator cooling, battery thermal management, and overall machine temperature control, providing reliable heat dissipation solutions for high-power-density robots.

## Product Images

> Sanhua thermal management components: Please visit [official website](https://www.sanhuaglobal.com) for details.

## Specification Table

| Specification Item | Value | Remarks/Source |
|--------------------|-------|----------------|
| Product Form | Electronic expansion valves, solenoid valves, electronic water pumps, Chillers, heat exchangers | Sanhua official website |
| Control Precision | High-precision flow and pressure regulation | Sanhua public information |
| Working Pressure | 0–4.5 MPa (depending on model) | Product manual |
| Medium | R134a, R1234yf, coolant, ethylene glycol aqueous solution | Sanhua information |
| Flow Range | 0–100 L/min depending on model | Product manual |
| Lifespan | >100,000 cycles (typical valve) | Sanhua public information |
| Dimensions | Valve body diameter 20–60 mm (depending on model) | Public specifications |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Sanhua Intelligent Controls / Sanhua](../companies/company_sanhua.md)
- **Core Components/Technology Sources**: Copper, aluminum, rare earth magnets, electronic controllers, seals, sensors.
- **Downstream Applications/Customers**: New energy vehicles, energy storage systems, data center liquid cooling, robot OEMs.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_sanhua_thermal`
- Manufacturer Entity: `ent_company_sanhua`
- Key Relationships:
  - `rel_ent_company_sanhua_manufactures_ent_product_sanhua_thermal` (`ent_company_sanhua` → `manufactures` → `ent_product_sanhua_thermal`)
  - `ent_product_sanhua_thermal` -- `uses` --> `ent_component_electronic_expansion_valve`
  - `ent_product_sanhua_thermal` -- `cools` --> `ent_component_servo_motor`

## Application Scenarios

- **Robot Joint Thermal Management**: Provides liquid cooling or coolant circulation for motors and reducers.
- **Battery Thermal Management**: Temperature control for new energy vehicle and robot battery packs.
- **Data Center Liquid Cooling**: Efficient heat dissipation for servers and intelligent computing centers.

## Competitive Comparison

| Comparison Item | Sanhua Thermal Management | Yinlun Co., Ltd. | Dun'an Environment |
|-----------------|---------------------------|------------------|--------------------|
| Core Advantage | Global leader in valve precision and scale | Heat exchanger and module integration | Cost of refrigeration valves |
| Main Products | Expansion valves/water pumps/Chillers | Oil coolers/water-cooled plates/modules | Four-way valves/expansion valves |
| Robot Layout | Actuator cooling and thermal management | Battery/motor cooling | Refrigeration systems |

## Selection and Deployment Recommendations

- Select the corresponding model based on computing power/precision/scenario requirements, prioritizing official toolchain and ecosystem compatibility.
- Confirm before deployment whether power supply, heat dissipation, mechanical interfaces, and communication protocols meet overall machine requirements.
- It is recommended to obtain the latest firmware, SDK, and technical support through official channels or authorized distributors.

## Related Entries

- [Manufacturer: Sanhua Intelligent Controls / Sanhua](../companies/company_sanhua.md)
- [Appendix D.4 Key Product Wiki](../index-products.md)

## References

1. [Sanhua Intelligent Controls / Sanhua official product/company page](https://www.sanhuaglobal.com)
2. Sanhua Intelligent Controls 2024 Annual Report
3. Sanhua Intelligent Controls investor communication minutes
