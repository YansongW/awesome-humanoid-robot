# Junto Robotics

> This entry belongs to [Appendix D: Enterprise/Product Wiki](../../appendix-d.md).  
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 钧舵机器人 |
| **English Name** | Junto Robotics |
| **Headquarters** | Suzhou, China |
| **Founded** | 2018 |
| **Website** | [https://www.jodell.cn](https://www.jodell.cn) |
| **Supply Chain Segment** | Electric servo end-effectors / Electric grippers / Dexterous hands |
| **Company Attributes** | National High-Tech Enterprise, incubated by HIT Robotics Institute |
| **Parent Company/Group** | Suzhou Junto Robotics Co., Ltd. |
| **Data Sources** | Official website, product manuals, public reports, WAIC 2026 coverage |

## Company Overview

A one-stop electric servo end-effector solution provider, specializing in intelligent grasping and dexterous manipulation.

Founded by a team of PhDs from the Robotics Institute of Harbin Institute of Technology, Junto Robotics has mass-produced over ten products across five series: industrial dexterous hands, intelligent electric grippers, electric suction cups, lift-rotate grippers, and Z/R actuators. The company's products feature integrated drive and control, power-off self-locking, and intelligent feedback, serving hundreds of customers in industries such as life sciences, lithium batteries, 3C, semiconductors, and food.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| EPG Series Electric Parallel Grippers | Precision force control | EPG-M06 / EPG-HP26 | 3C, semiconductor, medical |
| RG Series Robot Grippers | Modular integrated drive and control | RG52-050 / RG75-300 | Industrial loading/unloading, collaborative robots |
| Dexterous Hand Series | Intelligent bionic five-finger | JQ3-5 | Humanoid robots, scientific research |

## Representative Products

### RG52-050 Electric Gripper / Junto RG52-050 Electric Gripper

> RG52-050 Electric Gripper: Please visit [official documentation](https://www.jodell.cn) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Dimensions | Not disclosed | - |
| Weight | 0.75 kg | Product manual |
| Degrees of Freedom | 1 DOF (two-finger parallel) | Product manual |
| Adjustable Stroke | 0–52 mm | Product manual |
| Single Finger Gripping Force | 2–50 N | Product manual |
| Recommended Payload | 1 kg | Product manual |
| Open/Close Time | 0.5 s | Product manual |
| Supply Voltage | DC 24 V | Product manual |
| Communication Interface | Modbus RTU (RS485) / I/O | Product manual |
| Price | Not disclosed | - |

**Technical Highlights**: Integrated drive and control, mechatronic integration, precise force control, IP54 protection, supports fast networking and drop detection.

**Application Scenarios**: PCB handling, in vitro diagnostics, lithium battery sorting, 3C assembly, collaborative robot loading/unloading.

### JQ3-5 Industrial Dexterous Hand / Junto JQ3-5 Industrial Dexterous Hand

> JQ3-5 Industrial Dexterous Hand: Please visit [official documentation](https://www.jodell.cn) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Dimensions | Not disclosed | - |
| Weight | Not disclosed | - |
| Degrees of Freedom | Not disclosed | - |
| Payload | Not disclosed | - |
| Fingertip Force | Not disclosed | - |
| Supply Voltage | DC 24 V | Product manual |
| Communication Interface | Modbus RTU (RS485) | Product manual |
| Price | Not disclosed | - |

**Technical Highlights**: Bionic five-finger structure, industrial-grade reliability, designed for humanoid robots and complex grasping tasks.

**Application Scenarios**: Humanoid robots, laboratory automation, education and research, service robots.

## Supply Chain Position

- **Upstream Key Components/Materials**: Servo motors, reducers, force sensors, aluminum alloy structural parts, control boards
- **Downstream Customers/Application Scenarios**: Medical automation, lithium batteries, 3C, semiconductor, food industry equipment manufacturers
- **Main Competitors/Peers**: Dahon Robotics, Robotiq, SCHUNK, Inspire Robots

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_junto`
- Product/Component Entity: `ent_product_junto_hand`
- Key Relationships:
  - `ent_company_junto` -- `manufactures` --> `ent_product_junto_hand`

## References

1. [Official Website](https://www.jodell.cn)
2. [WAIC 2026 Exhibition Coverage](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.jodell.cn) (Please verify against actual product models)
