# Shadow Robot Company

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Shadow Robot Company |
| **English Name** | Shadow Robot Company |
| **Headquarters** | London, UK |
| **Founded** | 1987 |
| **Website** | [https://www.shadowrobot.com](https://www.shadowrobot.com) |
| **Supply Chain Role** | Anthropomorphic Dexterous Hand / Robot End Effector / Research Platform |
| **Enterprise Attribute** | World-leading dexterous hand company, research-grade products |
| **Parent Company/Group** | Shadow Robot Company Ltd. |
| **Data Source** | Official website, product manuals, public reports, WAIC 2026 coverage |

## Company Overview

One of the world's most advanced developers of anthropomorphic dexterous hands, deeply engaged in research and high-end applications.

Shadow Robot Company was founded in 1987 and is headquartered in London, UK. It has long focused on the development of highly anthropomorphic robotic dexterous hands. The Shadow Dexterous Hand features dimensions and kinematics similar to the human hand and is widely used in robotic grasping research, teleoperation, medical surgery, nuclear industry, and humanoid robotics. It is one of the most representative research-grade dexterous hands in the ROS/EtherCAT ecosystem.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Shadow Dexterous Hand | High-DOF research-grade | Five-fingered dexterous hand | Research, Medical |
| Shadow Hand Lite | Lightweight, low-cost | Four-fingered dexterous hand | Education, Commercial |
| Teleoperation Systems | Teleoperation | Shadow Glove | Remote control, Nuclear industry |

## Representative Products

### Shadow Dexterous Hand

> Shadow Dexterous Hand: Please visit [official materials](https://www.shadowrobot.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Dimensions | Anthropomorphic adult male hand size | Official datasheet |
| Weight | 4.3 kg (including forearm) | Official datasheet |
| Degrees of Freedom | 20 active + 4 passive / 24 joints | Official datasheet |
| Payload | Power grasp 4–5 kg | Official datasheet / Public reports |
| Movement Speed | Typical joint 1.0 Hz | Official datasheet |
| Communication Interface | EtherCAT | Official datasheet |
| Control Frequency | Position loop 1 kHz / Torque loop 5 kHz | Official datasheet |
| Supply Voltage | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: Highly biomimetic kinematics, fingertip/palm tactile sensors, full ROS integration, multi-mode control (position/force/torque), capable of fine manipulation tasks such as threading a needle and pinching.

**Application Scenarios**: Grasping research in universities and research institutions, medical surgical training, nuclear industry teleoperation, high-end validation for humanoid robots.

### Shadow Hand Lite

> Shadow Hand Lite: Please visit [official materials](https://www.shadowrobot.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Dimensions | Not disclosed | - |
| Weight | Not disclosed | - |
| Degrees of Freedom | Not disclosed | - |
| Payload | Not disclosed | - |
| Fingertip Force | Not disclosed | - |
| Communication Interface | EtherCAT | Product manual |
| Supply Voltage | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: Streamlined structure while retaining the fine manipulation capabilities of the Shadow Hand, targeting broader educational and commercial applications.

**Application Scenarios**: Educational demonstrations, commercial displays, lightweight research, service robots.

## Supply Chain Position

- **Upstream Key Components/Materials**: Micro motors, tendons, force/tactile sensors, aluminum alloy/engineering plastics, EtherCAT control boards
- **Downstream Customers/Application Scenarios**: Universities and research institutions, medical surgery, nuclear industry, teleoperation, humanoid robots
- **Main Competitors/Peers**: SCHUNK, qb Soft Robotics, Agile Robots, Inspire Robots

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_shadow_robot`
- Product/Component Entity: `ent_product_shadow_dexterous_hand`
- Key Relationship:
  - `ent_company_shadow_robot` -- `manufactures` --> `ent_product_shadow_dexterous_hand`

## References

1. [Official Website](https://www.shadowrobot.com)
2. [WAIC 2026 Exhibition Coverage](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.shadowrobot.com) (Please verify against actual product models)
