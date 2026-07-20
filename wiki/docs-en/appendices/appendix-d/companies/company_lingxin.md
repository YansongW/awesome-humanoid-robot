# Linkerbot

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 灵心巧手 (Linkerbot / 灵心巧手（北京）科技有限公司) |
| **English Name** | Linkerbot |
| **Headquarters** | Beijing, China |
| **Founded** | 2023 |
| **Website** | [https://www.linkerbot.cn](https://www.linkerbot.cn) |
| **Supply Chain Role** | Structural components / Dexterous hand end-effectors |
| **Company Type** | Dexterous hand unicorn, leader in high-DOF end-effectors |
| **Parent Company/Group** | None |
| **Data Sources** | Linkerbot official website, 36Kr PitchHub, WRC exhibitor information, Xinhua Net |

## Company Profile

Linkerbot is a high-tech enterprise with the mission of "creating everything," focusing on embodied intelligence solutions for dexterous manipulation. The company independently develops the Linker Hand series of high-degree-of-freedom (DOF) dexterous hands and provides supporting products such as motion capture teleoperation systems and digital twin platforms for dexterous manipulation. It is the world's first dexterous hand company to achieve full coverage of the three mainstream technical routes: tendon-driven, linkage-driven, and direct-drive.

The company claims to hold over 80% of the global market share for high-DOF dexterous hands. Its products are used by top laboratories such as Stanford, Cambridge, Tsinghua, and Peking University, as well as enterprises like Honor, ZTE, Midea, and Foxconn. Linkerbot's monthly production capacity exceeds 4,000 units, with plans to deliver 50,000 to 100,000 dexterous hands in 2026 and expand into scenarios such as industrial manufacturing, scientific research, artistic performance, and rehabilitation assistance.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| High-DOF Dexterous Hand | Precision manipulation for research and industry | Linker Hand L20 / L30 | Humanoid robots, research, industry |
| Lightweight Industrial Dexterous Hand | High cost-performance, suitable for small devices | Linker Hand O6 / O7 / L6 | Industrial gripping, education, elderly care |
| Teleoperation & Perception | Data collection and remote control | Force feedback glove / Motion capture glove / Open TeleDex | Data collection, teleoperation |
| Complete Robot Platform | Dual-arm + dexterous hand operation demonstration | Linkerbot Workbench / Linkerbot Orchestra | Industrial display, artistic performance |

## Representative Products

### Linker Hand L20

> Linker Hand L20: Please visit the [official page](https://www.linkerbot.cn) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Size | Approximately the size of an adult male palm | WRC exhibitor materials |
| Weight | Not disclosed | - |
| DOF | 21 DOF (L20 industrial version: 21 DOF) | 36Kr / WRC |
| Load/Torque | Maximum grip force of four fingers: 12 N; industrial version lead screw end thrust: 200 N | East Money |
| Speed/RPM | Full hand open/close: 0.2–0.3 s | 36Kr / OFweek |
| Repeatability | ±0.1–0.2 mm | 36Kr / OFweek |
| Interface/Communication | Not disclosed | - |
| Price | Approximately 49,900 RMB (L20 general version) | 36Kr |

**Technical Highlights**: Linkage transmission, self-developed micro motors and "super electric cylinders," drive efficiency of approximately 90%, tested lifespan exceeding one million cycles; supports fingertip vision and tactile perception.

**Application Scenarios**: Precision assembly, screw tightening, piano playing, research and education, humanoid robot end-effectors.

### Linker Hand O6

> Linker Hand O6: Please visit the [official page](https://www.linkerbot.cn) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Size | Approximately the size of an adult female palm | East Money |
| Weight | Approximately 370 g | East Money |
| DOF | 6 DOF | 36Kr |
| Load/Torque | Maximum grip load: 50 kg | East Money |
| Speed/RPM | Not disclosed | - |
| Battery Life | Not disclosed | - |
| Interface/Communication | Not disclosed | - |
| Price | 6,666 RMB (subsidized Lite version approximately 3,999 RMB) | 36Kr |

**Technical Highlights**: Uses PEEK engineering plastic ("plastic instead of steel"), achieving high load capacity at extremely low weight, earning the nickname "Little King Kong."

**Application Scenarios**: Small robotic arm end-effectors, educational demonstrations, elderly care assistance, light industrial gripping.

## Supply Chain Position

- **Upstream Key Components/Materials**: Self-developed motors, reducers, tactile sensors; externally purchased structural components, electronic skin materials, cables.
- **Downstream Customers/Application Scenarios**: Humanoid robot integrators (e.g., Zhiyuan, Unitree, etc.), manufacturing enterprises such as Foxconn/BYD/Samsung, global university laboratories.
- **Main Competitors/Peers**: Shadow Robot, CloudMinds, Dahuan Robot, InTime Robot.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_lingxin`
- Product Entities: `ent_product_lingxin_linker_hand_l20`, `ent_product_lingxin_linker_hand_o6`
- Key Relationships:
  - `ent_company_lingxin` -- `manufactures` --> `ent_product_lingxin_linker_hand_l20`
  - `ent_company_lingxin` -- `manufactures` --> `ent_product_lingxin_linker_hand_o6`

## References

1. [Linkerbot Official Website](https://www.linkerbot.cn)
2. [36Kr PitchHub – Linkerbot Project Information](https://pitchhub.36kr.com/project/3220383134980225)
3. [World Robot Conference – Linkerbot Exhibitor Information](https://www.worldrobotconference.com/expo/company/514.html)
4. [Xinhua Net – Linkerbot at Zhongguancun Forum](https://www.news.cn/world/20260327/f0c853dfc5c24e50be4368123282e6d1/c.html)
5. [East Money – Linkerbot at CES 2026](http://finance.eastmoney.com/a/202601083613162942.html)
