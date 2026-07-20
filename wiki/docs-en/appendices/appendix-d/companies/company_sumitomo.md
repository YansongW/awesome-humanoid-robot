# Sumitomo Heavy Industries

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 住友重工 |
| **English Name** | Sumitomo Heavy Industries, Ltd. |
| **Headquarters** | Tokyo, Japan |
| **Founded** | 1888 |
| **Website** | [https://www.shi.co.jp](https://www.shi.co.jp) |
| **Supply Chain Role** | Reducers / Heavy Machinery / Precision Transmission |
| **Enterprise Attribute** | Public Company (TYO.6302), International Brand |
| **Parent Company/Group** | Sumitomo Heavy Industries, Ltd. |
| **Data Source** | Official website, annual reports, product manuals, WAIC 2026 reports |

## Company Profile

A comprehensive heavy industry giant in Japan, with a leading global market share in Cyclo cycloidal reducers.

Sumitomo Heavy Industries' business covers heavy machinery, environmental equipment, semiconductor manufacturing equipment, precision reducers, and marine machinery. Its precision reducer division focuses on the Cyclo cycloidal reducer as its core product, featuring high rigidity, high torque, and impact resistance, widely used in industrial robots, humanoid robots, mining machinery, construction machinery, and energy equipment.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|-------------------------|-------------------|
| Cycloidal Reducer | High-torque, impact-resistant reduction | Cyclo Series | Industrial robots, heavy machinery |
| Planetary Reducer | Precision servo reduction | Fine Cyclo, IB Series | Semiconductors, robot joints |
| Servo Actuator | Integrated motor + reducer | Smart Cyclo Series | Automation, robotics |

## Representative Products

### Cyclo Series Cycloidal Reducer / Sumitomo Cyclo Drive

> Cyclo Series Cycloidal Reducer: Please visit [Official Documentation](https://www.shi.co.jp) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Size | 40–400 mm frame size (series range) | Product manual |
| Reduction Ratio | 6:1 – 658,503:1 | Product manual |
| Rated Output Torque | 20–1,200,000 N·m | Product manual |
| Transmission Efficiency | ≥90% | Product manual |
| Shock Load Capacity | 500% of rated torque | Product manual |
| Input Speed | Up to 3,000 rpm | Product manual |
| Lubrication Method | Grease / Oil bath lubrication | Product manual |
| Price | Not disclosed | - |

**Technical Highlights**: Cycloidal pinwheel transmission, multi-tooth meshing, high rigidity, impact resistance, suitable for heavy-load, high-reliability industrial applications.

**Application Scenarios**: Industrial robot bases and shoulders, humanoid robot torso joints, mining machinery, construction machinery, port equipment.

### Fine Cyclo Precision Reducer / Sumitomo Fine Cyclo Precision Reducer

> Fine Cyclo Precision Reducer: Please visit [Official Documentation](https://www.shi.co.jp) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Size | 40–220 mm frame size (series range) | Product manual |
| Reduction Ratio | 3:1 – 100:1 | Product manual |
| Rated Output Torque | 10–8,000 N·m | Product manual |
| Backlash | ≤ 3 arcmin | Product manual |
| Transmission Efficiency | ≥90% | Product manual |
| Input Speed | Up to 5,000 rpm | Product manual |
| Protection Class | IP54 | Product manual |
| Price | Not disclosed | - |

**Technical Highlights**: Combined cycloidal and planetary structure, balancing high precision and high torque, suitable for servo motor matching and robot joints.

**Application Scenarios**: Collaborative robots, humanoid robot joints, semiconductor equipment, CNC machine tools, automated production lines.

## Supply Chain Position

- **Upstream Key Components/Materials**: Special alloy steel, bearings, lubricants, seals, castings, motors
- **Downstream Customers/Application Scenarios**: Industrial robot manufacturers, humanoid robot integrators, construction machinery, mining, energy
- **Main Competitors/Peers**: Nabtesco, SEW-EURODRIVE, Bonfiglioli, NGC, Ningbo Donly

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_sumitomo`
- Product/Component Entities: `ent_component_sumitomo_cyclo_drive`, `ent_component_sumitomo_fine_cyclo`
- Key Relationships:
  - `ent_company_sumitomo` -- `manufactures` --> `ent_component_sumitomo_cyclo_drive`
  - `ent_company_sumitomo` -- `manufactures` --> `ent_component_sumitomo_fine_cyclo`

## References

1. [Official Website](https://www.shi.co.jp)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.shi.co.jp/products/) (Please verify against actual product models)
