# NSK

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 日本精工 |
| **English Name** | NSK Ltd. |
| **Headquarters** | Tokyo, Japan |
| **Founded** | 1916 |
| **Website** | [https://www.nsk.com](https://www.nsk.com) |
| **Supply Chain Role** | Bearings / Ball Screws / Linear Guides / Steering Systems |
| **Enterprise Type** | Publicly listed company (TYO.6471), international brand |
| **Parent Company/Group** | Independent |
| **Data Source** | Official website, annual reports, product catalogs, WAIC 2026 reports |

## Company Overview

A global giant in bearings and precision mechanical components, a core supplier of ball screws and linear guides.

NSK is Japan's largest and one of the world's leading bearing manufacturers, with products covering rolling bearings, ball screws, linear guides, steering systems, and automotive components. Its Precision Machinery Division provides high-precision ball screws, linear guides, and XY positioning stages for machine tools, semiconductors, robotics, and medical equipment.

## Product Lines

| Product Line | Positioning | Representative Products | Application Fields |
|--------------|-------------|------------------------|--------------------|
| Ball Screws | Machine-tool-grade precision screws | NSK S1 / HMC Series | Machine tools, robotics |
| Linear Guides | High-precision linear guides | NH/NS/PU/PE Series | Automation, semiconductors |
| Bearings | General-purpose / precision bearings | Deep groove / Angular contact / Roller bearings | Automotive, industry |
| XY Positioning Stages | Integrated positioning systems | Model numbers not disclosed | Semiconductors, inspection |

## Representative Products

### Ball Screw

> Ball Screw: Please visit [official documentation](https://www.nsk.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Screw Diameter | Ø4–Ø120 mm | Product catalog |
| Lead | 1–50 mm | Product catalog |
| Accuracy Grade | C0–C10 | Product catalog |
| Dynamic Load Rating | Depends on model | Product catalog |
| Maximum Speed | Depends on model | Product catalog |
| Preload Method | Double nut / Single nut offset | Product catalog |
| Material | Bearing steel / Stainless steel | Product catalog |
| Price | Not disclosed | - |

**Technical Highlights**: High precision, low noise, long life; available in special specifications such as dust-proof, low particle emission, and vacuum-compatible.

**Application Scenarios**: CNC machine tools, semiconductor equipment, linear joints of humanoid robots, medical instruments.

### Linear Guide

> Linear Guide: Please visit [official documentation](https://www.nsk.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Rail Width | 15–100 mm | Product catalog |
| Accuracy Grade | Normal / H / P / SP / UP | Product catalog |
| Dynamic Load Rating | Depends on model | Product catalog |
| Carriage Type | Flanged / Square / Miniature | Product catalog |
| Material | Bearing steel / Stainless steel | Product catalog |
| Price | Not disclosed | - |

**Technical Highlights**: High dust resistance, high load capacity, low friction; suitable for clean rooms and heavy cutting environments.

**Application Scenarios**: Machine tools, semiconductors, LCD panel equipment, robotics, automation.

## Supply Chain Position

- **Upstream Key Components/Materials**: Bearing steel, specialty steel, grease, seals, ceramic balls, cage materials
- **Downstream Customers/Application Scenarios**: Automotive OEMs, machine tool manufacturers, semiconductor equipment, robot OEMs, medical
- **Main Competitors/Peers**: NTN, SKF, Schaeffler, THK, HIWIN, Qinchuan Machine Tool

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_nsk`
- Product/Component Entities: `ent_component_nsk_ball_screw`, `ent_component_nsk_linear_guide`
- Key Relationships:
  - `ent_company_nsk` -- `manufactures` --> `ent_component_nsk_ball_screw`
  - `ent_company_nsk` -- `manufactures` --> `ent_component_nsk_linear_guide`

## References

1. [NSK Official Website](https://www.nsk.com)
2. [NSK Investor Relations](https://www.nsk.com/ir/)
3. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
