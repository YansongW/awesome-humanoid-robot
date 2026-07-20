# DEEPRobotics

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).  
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 云深处科技 |
| **English Name** | DEEPRobotics |
| **Headquarters** | Hangzhou, China |
| **Founded** | 2017 |
| **Website** | [https://www.deeprobotics.cn](https://www.deeprobotics.cn) |
| **Supply Chain Role** | Complete machine OEM / Quadruped robots + Humanoid robots, Joint modules |
| **Enterprise Attribute** | Leader in power inspection, specialized legged robots for extreme environments |
| **Parent Company/Group** | None |
| **Data Source** | DEEPRobotics official website, public reports, business review of nearly 30 embodied intelligence companies |

## Company Profile

DEEPRobotics is a pioneer in the commercialization of quadruped robots in China. The "Jueying" series has been widely used in scenarios such as power inspection, emergency rescue, and pipe gallery tunnels.

Since 2024, the company has entered the humanoid robot field, proposing an "integrated solution for legged and humanoid robots in extreme environments," and launched the J-series joint modules and the Lynx M20 wheeled-legged robot.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| Industrial Quadruped | Explosion-proof, all-terrain inspection | Jueying X20 / X30 | Power, firefighting, pipe galleries |
| Education & Research Quadruped | Lightweight, secondary development | Jueying Lite3 | Education, research |
| Wheeled-legged / Humanoid | Multi-morphology mobile manipulation | Lynx M20 / DR01 / DR02 | Industry, rescue |

## Representative Products

### Jueying X30

> DEEPRobotics Jueying X30: Please visit [official materials](https://www.deeprobotics.cn) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | Approx. 100 × 69.5 × 47 cm | Public battery industry data |
| Weight | Approx. 56 kg | Public battery industry data |
| Degrees of Freedom | Not disclosed | - |
| Payload/Torque | Payload approx. 15 kg | Industry analysis report |
| Speed/Rotation | Can climb 45° slopes / stairs | DEEPRobotics official website / Industry reports |
| Battery Life | 2.5–4 h (industry data); another report of 8 h | Configuration differences across scenarios |
| Interface/Communication | Not disclosed | - |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: IP67/IP68 protection, operating temperature -20 °C to 55 °C, dual-light PTZ, multi-sensor fusion navigation.

**Application Scenarios**: Substation inspection, fire rescue, underground pipe galleries, metal smelting.

### Jueying Lite3

> DEEPRobotics Jueying Lite3: Please visit [official materials](https://www.deeprobotics.cn) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | Not disclosed | - |
| Weight | Not disclosed | - |
| Degrees of Freedom | Not disclosed | - |
| Payload/Torque | Not disclosed | - |
| Speed/Rotation | Not disclosed | - |
| Battery Life | Approx. 4 h | Industry analysis report |
| Interface/Communication | Supports secondary development | DEEPRobotics official website |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: Lightweight design, 50% increase in joint torque, 3x improvement in computing power, modular expansion.

**Application Scenarios**: Education & research, inspection algorithm validation, developer community.

## Supply Chain Position

- **Upstream Key Components/Materials**: Self-developed J60/J80/J100 joint modules, externally purchased motors, reducers, batteries, LiDAR, PTZ.
- **Downstream Customers/Application Scenarios**: State Grid Corporation of China, China Southern Power Grid, Singapore Power, emergency rescue units.
- **Main Competitors/Comparables**: Unitree B2, Boston Dynamics Spot, ANYbotics ANYmal.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_deep_robotics`
- Product Entities: `ent_product_deep_robotics_x30`, `ent_product_deep_robotics_lite3`
- Key Relationships:
  - `ent_company_deep_robotics` -- `manufactures` --> `ent_product_deep_robotics_x30`
  - `ent_company_deep_robotics` -- `manufactures` --> `ent_product_deep_robotics_lite3`
  - `ent_product_deep_robotics_x30` -- `uses` --> `ent_component_deep_robotics_j_series_joint`

## References

1. [DEEPRobotics Official Website](https://www.deeprobotics.cn)
2. [DEEPRobotics Industry Application Page](https://www.deeprobotics.cn/robot/index/industry.html)
3. [Grepow Battery – Analysis of Mainstream Robot Power Batteries](https://www.grepow.cn/hyxw/ysyscxmwlzljqrdc.html)
4. [Reportify – Business Overview of Nearly 30 Embodied Intelligence Companies](https://reportify.cn/social-media/690201058833550)
5. [Appendix D.4 Key Product Wiki](../index-products.md)
