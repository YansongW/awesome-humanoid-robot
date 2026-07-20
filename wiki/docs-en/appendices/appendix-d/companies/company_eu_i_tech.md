# EYouBot / EYou Technology

> This entry belongs to [Appendix D: Company/Product Wiki](../../appendix-d.md).
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 意优科技 (Jiangsu EYou Robot Technology Co., Ltd.) |
| **English Name** | EYouBot / Eyou Technology |
| **Headquarters** | Wuxi/Shanghai, China |
| **Founded** | 2018 |
| **Website** | [https://eyoubot.com](https://eyoubot.com) |
| **Supply Chain Role** | Motors & Drives / Integrated Servo Joint Modules |
| **Company Type** | Tier 1 Supplier of Humanoid Robot Joint Modules |
| **Parent Company/Group** | None |
| **Data Source** | EYouBot official website, OFweek, Sohu/OFweek 2026 new product reports |

## Company Profile

Founded in 2018, EYouBot focuses on the R&D and mass production of integrated servo joint modules for humanoid robots. The company has developed a self-researched FPGA-based full-hardware FOC control algorithm. Its product line includes three series of joint modules: harmonic, planetary, and linear, covering various power requirements for the upper limbs, waist, and lower limbs of humanoid robots.

In 2024, the company sold 30,000 units of joint module products, with its harmonic joints achieving the highest shipment volume in the humanoid robot industry nationwide. EYouBot currently has a production capacity of 80,000 units (Wuxi) and an additional 180,000 units from automated production lines under construction (Shanghai). The company has strategically positioned itself as a "leading Tier 1 supplier in the robotics industry." Its joint modules have been installed in mass-produced models of several leading humanoid robot companies.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| Harmonic Integrated Joint | Humanoid robot bionic joint | RHU / PHU Series | Humanoid robot shoulder, elbow, hip, knee |
| Planetary Integrated Joint | Low-cost, high-impact resistance joint | RP / PP Series | Semi-humanoid, small humanoid robots |
| Linear Integrated Joint | Biped/humanoid lower limb actuator | Linear Joint Module | Biped robots, humanoid robot lower limbs |
| Teleoperation & Upper Limb Platform | Secondary development & teleoperation | proLocation Teleoperation Robot / Universal Upper Limb | Research, teleoperation |

## Representative Products

### RHU Humanoid-Specific Harmonic Joint

> RHU Harmonic Joint: Please visit [official materials](https://eyoubot.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Dimensions | Volume and weight reduced by nearly 30% compared to conventional products at the same torque level | Sohu/OFweek |
| Weight | Not disclosed | - |
| Reduction Ratio | Not disclosed | - |
| Torque | Not disclosed | - |
| Communication Protocol | CAN / EtherCAT dual protocol | Sohu/OFweek |
| Functional Safety | Integrated STO function | Sohu/OFweek |
| Interface/Communication | Supports MIT force control mode | OFweek |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: Designed specifically for humanoid robots and high-end mobile robots, extremely compact, high power density, optional high-precision force control.

**Application Scenarios**: Full-body joints of humanoid robots, collaborative robotic arms, high-end mobile robots.

### RP Humanoid-Specific Planetary Joint

> RP Planetary Joint: Please visit [official materials](https://eyoubot.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Dimensions | Not disclosed | - |
| Weight | Not disclosed | - |
| Torque Density | Up to 114 N·m/kg | Sohu/OFweek |
| Encoder | First introduction of inductive encoder | Sohu/OFweek |
| Bearing | Crossed roller bearing, clamp/double-end fixed | Sohu/OFweek |
| Interface/Communication | CAN / EtherCAT | Sohu/OFweek |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: "Competition-grade" planetary joint with enhanced impact resistance design, suitable for 0.8–1.3 m class humanoid robots, low cost, high reliability.

**Application Scenarios**: Entertainment/competition humanoid robots, educational robots, semi-humanoid robots.

## Supply Chain Position

- **Upstream Key Components/Materials**: Externally sourced harmonic reducers, planetary reducers, motors, encoders, bearings, structural parts; self-developed FPGA drivers and FOC algorithms.
- **Downstream Customers/Application Scenarios**: Humanoid robot OEMs, collaborative robotic arm manufacturers, industrial automation equipment suppliers.
- **Main Competitors/Comparables**: Inovance Technology, Hechuan Technology, Maxon, Kollmorgen.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_eu_i_tech`
- Product Entities: `ent_product_eu_i_tech_rhu_joint`, `ent_product_eu_i_tech_rp_joint`
- Key Relationships:
  - `ent_company_eu_i_tech` -- `manufactures` --> `ent_product_eu_i_tech_rhu_joint`
  - `ent_company_eu_i_tech` -- `manufactures` --> `ent_product_eu_i_tech_rp_joint`

## References

1. [EYouBot Official Website](https://eyoubot.com)
2. [OFweek – EYouBot Exhibitor Recommendation](https://robot.ofweek.com/2025-05/ART-8321201-8120-30662701.html)
3. [Sohu/OFweek – EYouBot 2026 Full Series Joint Module Launch](https://www.sohu.com/a/979183416_122014422)
4. [Zhihu – EYouBot New Joint Products](https://zhuanlan.zhihu.com/p/1998116506324731740)
