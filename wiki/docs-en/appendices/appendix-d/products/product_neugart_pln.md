# Neugart PLN Precision Planetary Gearbox

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Neugart](../companies/company_neugart.md) |
| **Product Category** | Precision Planetary Gearbox |
| **Release Date** | Current main model |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [Neugart Official Website](https://www.neugart.com) |

## Product Overview

PLN is Neugart's standard precision planetary gearbox, featuring spur gear high-rigidity design and preloaded tapered roller bearings, available in 1-stage and 2-stage configurations. The series ranges from PLN 070 to PLN 190, with reduction ratios of 3–100, 1-stage rated torque of 14–800 N·m, and 2-stage up to 43–2,880 N·m.

PLN offers IP65 protection, lifetime lubrication, PCS-2 quick motor adapter, and a long centering collar, achieving positioning accuracy of <1 arcmin (option). It is a cost-effective precision drive solution for machine tools, robots, and semiconductor equipment.

## Product Image

> Neugart PLN Precision Planetary Gearbox: Please visit the [official website](https://www.neugart.com) for details.

## Specification Table

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Reduction Ratio | 3:1 – 100:1 | Product manual |
| Frame Size | PLN 070 / 090 / 115 / 142 / 190 | Product manual |
| Rated Output Torque | 14 – 800 N·m (1-stage); 43 – 2,880 N·m (2-stage) | Product manual |
| Backlash | Standard <3 arcmin; Optional <1 arcmin | Product manual |
| Efficiency | Up to approx. 98% | Product manual |
| Protection Class | IP65 | Product manual |
| Maximum Input Speed | Up to 8,000 rpm (depending on size) | Product manual |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Neugart](../companies/company_neugart.md)
- **Core Components/Technology Sources**: Spur planetary gears, preloaded bearings, seals, grease, motor adapter flange
- **Downstream Applications/Customers**: CNC machine tools, industrial robots, humanoid robots, semiconductor and medical equipment

## Knowledge Graph Nodes and Relationships

- Component Entity: `ent_component_neugart_pln`
- Manufacturer Entity: `ent_company_neugart`
- Key Relationships:
  - `rel_ent_company_neugart_manufactures_ent_component_neugart_pln` (`ent_company_neugart` --> `manufactures` --> `ent_component_neugart_pln`)

## Application Scenarios

- **Industrial Robots**: Robot wrists, shoulders, rotary tables
- **Humanoid Robots**: Precision reduction in arm and leg joints
- **CNC Machine Tools**: Machine feed, tool changers, 4th/5th axis rotary tables
- **Other Automation**: Packaging, printing, medical positioning platforms

## Competitive Comparison

| Comparison Item | PLN Planetary Gearbox | Wittenstein SP+ | Apex Dynamics AB |
|-----------------|------------------------|-----------------|------------------|
| Core Advantage | High precision, lifetime lubrication, PCS-2 | Helical gears, constant backlash | Taiwan cost-effective, helical |
| Backlash/Accuracy | <1–3 arcmin | ≤1–3 arcmin | ≤1–5 arcmin |
| Price Level | High-end | High-end | Mid-to-high end |
| Delivery Lead Time | Medium | Medium | Short |

## Selection and Deployment Recommendations

For high positioning accuracy scenarios, prioritize the reduced backlash option; note that PLN uses spur gears. If noise sensitivity is a concern, consider PLE or helical competitors.

## References

1. [Neugart Official Website](https://www.neugart.com)
2. [Neugart PLN Precision Planetary Gearbox](https://www.neugart.com/en/gearboxes/precision-gearboxes/pln)
3. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
