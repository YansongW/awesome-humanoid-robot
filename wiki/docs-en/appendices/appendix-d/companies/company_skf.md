# SKF Group

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 斯凯孚 |
| **English Name** | SKF Group |
| **Headquarters** | Gothenburg, Sweden |
| **Founded** | 1907 |
| **Website** | [https://www.skf.com](https://www.skf.com) |
| **Supply Chain Role** | Bearings / Linear Motion / Seals / Lubrication |
| **Enterprise Attribute** | Listed Company (STO.SKF B), International Brand |
| **Parent Company/Group** | Independent |
| **Data Source** | Official website, annual reports, product manuals, WAIC 2026 reports |

## Company Profile

One of the world's largest suppliers of bearings and rotary/linear motion solutions, with a century of engineering heritage.

SKF's business covers bearings, seals, lubrication, condition monitoring, and linear motion systems. Its linear motion business (originally SKF Linear Motion Technology, later partially independent as Ewellix) offers ball screws, linear guides, electric cylinders, linear modules, and engineering services, serving industrial automation, medical, energy, and transportation.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Rolling Bearings | General/Precision Bearings | Ball Bearings / Roller Bearings | All industries |
| Linear Motion Systems | Guides/Screws/Actuators | LLTH / LGET / CASM | Automation |
| Seals | Rotary/Static Seals | CR / HMS Series | Automotive, Industry |
| Lubrication & Condition Monitoring | Predictive Maintenance | SKF Reliability | Energy, Industry |

## Representative Products

### Linear Motion System

> Linear Motion System: Please visit [official documentation](https://www.skf.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Rail Width | 15–65 mm | Product manual |
| Accuracy Grade | Normal / High / Precision | Product manual |
| Rated Dynamic Load | Depends on model | Product manual |
| Carriage Type | Flange / Square / Miniature | Product manual |
| Material | Bearing steel / Stainless steel | Product manual |
| Temperature Range | -20 °C – +80 °C | Product manual |
| Price | Not disclosed | - |

**Technical Highlights**: Integrates bearing, sealing, and lubrication technologies, providing long-life, low-maintenance linear motion solutions.

**Application Scenarios**: Machine tools, automated production lines, humanoid robot joints, semiconductor equipment, medical machinery.

### Ball Screw

> Ball Screw: Please visit [official documentation](https://www.skf.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Screw Diameter | Ø6–Ø80 mm | Product manual |
| Lead | 1–50 mm | Product manual |
| Accuracy Grade | C3–C10 | Product manual |
| Rated Dynamic Load | Depends on model | Product manual |
| Preload Method | Double nut / Single nut | Product manual |
| Material | Bearing steel / Stainless steel | Product manual |
| Price | Not disclosed | - |

**Technical Highlights**: High transmission efficiency, low friction, forms system-level solutions with SKF guides/actuators.

**Application Scenarios**: CNC machine tools, industrial robots, medical positioning platforms, new energy equipment.

## Supply Chain Position

- **Upstream Key Components/Materials**: Special steel, grease, sealing materials, sensors, ceramic balls, cages
- **Downstream Customers/Application Scenarios**: Automotive, wind power, machine tools, robot OEMs, aviation, railway
- **Main Competitors/Benchmarks**: Schaeffler, NSK, NTN, Timken, THK, Bosch Rexroth

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_skf`
- Product/Component Entities: `ent_component_skf_linear_motion`, `ent_component_skf_ball_screw`
- Key Relationships:
  - `ent_company_skf` -- `manufactures` --> `ent_component_skf_linear_motion`
  - `ent_company_skf` -- `manufactures` --> `ent_component_skf_ball_screw`

## References

1. [SKF Official Website](https://www.skf.com)
2. [SKF Investor Relations](https://investors.skf.com)
3. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
