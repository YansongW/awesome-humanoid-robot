# Tashan Technology

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 他山科技 |
| **English Name** | Tashan Technology |
| **Headquarters** | Beijing, China |
| **Founded** | 2017 |
| **Website** | [https://www.iteschina.com](https://www.iteschina.com) |
| **Supply Chain Role** | AI tactile sensing chips, multi-dimensional tactile sensors, electronic skin, embodied intelligent perception |
| **Enterprise Type** | Private enterprise, technology-based SME, specialized and new enterprise |
| **Parent Company/Group** | Independent operation (received strategic investment from Keli Sensing, etc.) |
| **Data Source** | Tashan Technology official website, SENSOR CHINA 2025 public reports, Keli Sensing investment announcements |

## Company Profile

Tashan Technology is an R&D provider of AI tactile sensing chips and application solutions, founded by a multinational R&D team with a Tsinghua background. The company focuses on capacitive tactile sensing technology, has completed the development of the world's leading digital-analog hybrid AI tactile chip, and based on the R-SpiNNaker distributed brain-like chip architecture, has solved the industry challenges of capacitive tactile sensors in terms of anti-interference and simultaneous analysis of multi-dimensional tactile signals.

The company has built a full-stack capability of "chip + sensor + algorithm model + simulation platform," with products covering the TS-F fingertip tactile sensor, TS-E robotic hand tactile sensor, TS-F+ multimodal tactile sensor, TS-V vision-tactile fusion training platform, and TS-ES embodied safety protection, widely used in humanoid robot dexterous hands, electronic skin, automotive, home appliances, and consumer electronics.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|-------------------------|-------------------|
| Multimodal Tactile Sensors | High-precision tactile sensing for robot fingertips/pads | TS-F+ / TS-F | Dexterous hands, electronic skin, precision grasping |
| Robotic Hand Tactile Sensors | Full-hand tactile perception and force control | TS-E | Collaborative robot end-effectors, humanoid robots |
| Vision-Tactile Fusion Platform | Multimodal perception training and deployment | TS-V | Embodied intelligence, complex environment manipulation |
| Embodied Safety Protection | Proximity and contact safety solutions | TS-ES | Human-robot collaboration, service robots |

## Representative Products

### Tashan TS-F+ Multimodal Tactile Sensor

> Tashan TS-F+: Please visit [official materials](https://www.iteschina.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Sensing Principle | Capacitive + digital-analog hybrid AI tactile chip | Official website/public reports |
| Perception Dimensions | 3D force, material, proximity, contact position, etc., 7–10 dimensions | Public reports |
| Spatial Resolution | Not disclosed | - |
| Range | Not disclosed | - |
| Response Time | Not disclosed | - |
| Communication Interface | Digital interface (compatible with mainstream robot buses) | Official public materials |
| Driver Chip | Self-developed R-SpiNNaker distributed brain-like chip | Public reports |
| Algorithm Model | 3D spatial capacitance tomography + SNN spiking neural network | Public reports |
| Operating Temperature | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: The world's first combination of a digital-analog hybrid AI tactile chip and capacitive multi-dimensional tactile perception, supporting material recognition, proximity sensing, and dynamic collaborative perception. Tactile simulation models have been open-sourced in MuJoCo and NVIDIA Isaac Sim.

**Application Scenarios**: Dexterous manipulation of humanoid robots, adaptive grasping of flexible/fragile objects, precision assembly, electronic skin for service robots.

### Tashan TS-V Vision-Tactile Fusion Training Platform

> Tashan TS-V: Please visit [official materials](https://www.iteschina.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Fusion Modalities | Vision + proximity + contact + force | Official public materials |
| Training Framework | MuJoCo / NVIDIA Isaac Sim | Public reports |
| Data Output | Tactile simulation data + real sensor data alignment | Public reports |
| Applicable Objects | Dexterous hands, robotic arms, humanoid robots | Official public materials |
| Price | Not disclosed | - |

**Technical Highlights**: Integrates global visual planning with local tactile feedback to enhance robot manipulation robustness in complex scenarios such as occlusion, reflection, and slippage.

**Application Scenarios**: Embodied intelligence training, complex environment grasping, transparent/reflective object manipulation, service robot skill learning.

## Supply Chain Position

- **Upstream Key Components/Materials**: Capacitive sensitive materials, flexible substrates, ASIC signal processing chips, MEMS processes, silicone encapsulation materials
- **Downstream Customers/Application Scenarios**: Humanoid robot OEMs, dexterous hand manufacturers, industrial robots, automotive electronics, home appliances, consumer electronics
- **Main Competitors/Peers**: Paxi Perception Technology, XELA Robotics, SynTouch, Force Sensing Technology

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_tashan`
- Product Entity: `ent_product_tashan_tactile_skin`
- Component Entity: `ent_component_tashan_tactile_sensor_chip`
- Key Relationships:
  - `ent_company_tashan` -- `manufactures` --> `ent_product_tashan_tactile_skin`
  - `ent_company_tashan` -- `manufactures` --> `ent_component_tashan_tactile_sensor_chip`
  - `ent_product_tashan_tactile_skin` -- `uses` --> `ent_component_tashan_tactile_sensor_chip`

## References

1. [Tashan Technology Official Website](https://www.iteschina.com)
2. [SENSOR CHINA 2025 – Tashan Technology Exhibition Report](https://www.sekorm.com/news/584921525.html)
3. [Keli Sensing Investment Announcement on Tashan Technology](https://finance.sina.com.cn/stock/relnews/cn/2025-08-17/doc-infmfuim2729687.shtml)
4. [21st Century Business Herald – Interview with Tashan Technology CEO](http://mp.weixin.qq.com/s?__biz=Mzk4ODE4MjkzNA==&mid=2247484687&idx=1&sn=84fba2c156a5ed6bbac57f2f0dc097e7)
5. [Appendix D Product Catalog](../index-products.md)
