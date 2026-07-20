# Ewellix

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 伊维莱 |
| **English Name** | Ewellix |
| **Headquarters** | Gothenburg, Sweden |
| **Founded** | 2021 (formerly SKF Linear Drive Technology division) |
| **Website** | [https://www.ewellix.com](https://www.ewellix.com) |
| **Supply Chain Role** | Linear drive / Electric cylinder / Ball screw / Linear guide |
| **Enterprise Type** | International brand (formerly under SKF) |
| **Parent Company/Group** | Formerly SKF Group, acquired by Triton in 2023 |
| **Data Source** | Official website, product manuals, public reports, WAIC 2026 coverage |

## Company Profile

An independent supplier of global linear motion and control technology, inheriting SKF's linear transmission business expertise.

Ewellix was spun off from SKF's linear drive technology business, focusing on products such as electric cylinders, ball screws, linear guides, linear modules, and lifting columns. The company serves industries including medical, industrial automation, robotics, mobile machinery, and automotive, emphasizing high energy efficiency, compact design, and intelligent control.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Electric Cylinder | High-thrust electromechanical actuator | CASM / LAMBDA series | Industrial, Medical |
| Ball Screw | Precision transmission | Ewellix Ball Screw | Machine tools, Automation |
| Linear Guide | High-rigidity guidance | LLTH / LLRA series | Automation |
| Linear Module | Integrated linear motion | ModLine series | Robotics, 3C |

## Representative Products

### Electric Cylinder / Electromechanical Cylinder

> Electric cylinder: Please visit [official documentation](https://www.ewellix.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Thrust Range | Up to approx. 100 kN | Product manual |
| Stroke | Max approx. 2,500 mm | Product manual |
| Speed | Max approx. 2,000 mm/s | Product manual |
| Repeatability | ±0.01 mm | Product manual |
| Motor Configuration | Servo / Stepper optional | Product manual |
| Protection Class | IP54 / IP65 optional | Product manual |
| Price | Not disclosed | - |

**Technical Highlights**: Modular design, integrated controller, low energy consumption, can replace traditional hydraulic/pneumatic cylinders.

**Application Scenarios**: Automated production lines, humanoid robot linear joints, medical equipment, packaging machinery.

### Linear Guide / Linear Guide

> Linear guide: Please visit [official documentation](https://www.ewellix.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Rail Width | 15–65 mm | Product manual |
| Accuracy Grade | Normal / High / Precision | Product manual |
| Rated Dynamic Load | Not disclosed | Product manual |
| Carriage Type | Flanged / Square / Narrow | Product manual |
| Material | Bearing steel | Product manual |
| Price | Not disclosed | - |

**Technical Highlights**: Inherits SKF manufacturing processes, low friction, high rigidity, smooth operation.

**Application Scenarios**: Machine tools, semiconductor equipment, automation platforms, robotics.

## Supply Chain Position

- **Upstream Key Components/Materials**: Bearing steel, balls, grease, servo motors, controllers, seals
- **Downstream Customers/Application Scenarios**: Industrial automation, medical equipment, robot OEMs, automotive, 3C manufacturing
- **Main Competitors/Peers**: THK, NSK, HIWIN, Bosch Rexroth, Nanjing Craft

## Knowledge Graph Nodes and Relationships

- Company entity: `ent_company_ewellix`
- Product/Component entities: `ent_component_ewellix_linear_actuator`, `ent_component_ewellix_linear_guide`
- Key relationships:
  - `ent_company_ewellix` -- `manufactures` --> `ent_component_ewellix_linear_actuator`
  - `ent_company_ewellix` -- `manufactures` --> `ent_component_ewellix_linear_guide`

## References

1. [Ewellix Official Website](https://www.ewellix.com)
2. [Triton Acquisition Announcement](https://www.triton-partners.com)
3. [WAIC 2026 Exhibition Coverage](https://www.worldrobotconference.com)
