# Tashan Technology TS-F+ Multimodal Tactile Sensor

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update date: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Tashan Technology](../companies/company_tashan.md) |
| **Product Category** | Multimodal Tactile Sensor / Electronic Skin |
| **Release Date** | 2024 (World Robot Conference debut) |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [Tashan Technology Official Website](https://www.iteschina.com) |

## Product Overview

The Tashan Technology TS-F+ Multimodal Tactile Sensor is a highly integrated capacitive tactile sensing unit designed for humanoid robot dexterous hands and electronic skin. The sensor is equipped with Tashan's self-developed analog-digital hybrid AI tactile chip, based on the R-SpiNNaker distributed brain-like architecture and Spiking Neural Network (SNN). It can extract 7–10 dimensions of tactile information from mixed signals, including three-dimensional force, material recognition, proximity sensing, and contact position.

TS-F+ supports adaptive force grasping of flexible, fragile, and irregularly shaped objects in complex environments, enabling fine operations such as holding a pen, pouring water, and grasping an egg. Tashan Technology has also released an open-source tactile simulation model based on MuJoCo and NVIDIA Isaac Sim, allowing developers to train tactile perception strategies at low cost in simulation environments and align them with real sensor data.

## Product Image

> Tashan TS-F+: Please visit the [official website](https://www.iteschina.com) for details.

## Specification Parameter Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Sensing Principle | Capacitive | Official website / Public reports |
| Perception Dimensions | 7–10 dimensions including 3D force, material, proximity, contact position | Public reports |
| Core Chip | Self-developed analog-digital hybrid AI tactile chip | Public reports |
| Chip Architecture | R-SpiNNaker distributed brain-like architecture | Public reports |
| Algorithm Model | 3D spatial capacitance tomography + SNN Spiking Neural Network | Public reports |
| Spatial Resolution | Not disclosed | - |
| Sensing Point Density | Not disclosed | - |
| Range (Normal Force) | Not disclosed | - |
| Response Time | Not disclosed | - |
| Sampling Frequency | Not disclosed | - |
| Communication Interface | Digital interface (compatible with mainstream robot buses) | Official website public information |
| Supply Voltage | Not disclosed | - |
| Operating Temperature | Not disclosed | - |
| Protection Level | Not disclosed | - |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Tashan Technology](../companies/company_tashan.md)
- **Core Components/Technology Source**: Self-developed analog-digital hybrid AI tactile chip, R-SpiNNaker brain-like architecture, capacitive sensitive materials; flexible substrates and packaging materials are outsourced.
- **Downstream Applications/Customers**: Humanoid robot dexterous hands, collaborative robot end-effectors, electronic skin, automotive interiors, home appliance touch control, consumer electronics.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_tashan_tactile_skin`
- Manufacturer Entity: `ent_company_tashan`
- Component Entity: `ent_component_tashan_tactile_sensor_chip`
- Key Relationships:
  - `rel_ent_company_tashan_manufactures_ent_product_tashan_tactile_skin` (`ent_company_tashan` → `manufactures` --> `ent_product_tashan_tactile_skin`)
  - `rel_ent_company_tashan_manufactures_ent_component_tashan_tactile_sensor_chip` (`ent_company_tashan` → `manufactures` --> `ent_component_tashan_tactile_sensor_chip`)
  - `rel_ent_product_tashan_tactile_skin_uses_ent_component_tashan_tactile_sensor_chip` (`ent_product_tashan_tactile_skin` → `uses` --> `ent_component_tashan_tactile_sensor_chip`)

## Application Scenarios

- **Humanoid Robot Dexterous Hands**: Tactile perception at fingertips/finger pads for fine grasping, slip detection, and material recognition.
- **Electronic Skin**: Covering robot arms and torso to provide proximity and contact safety protection.
- **Automotive and Home Appliances**: Intelligent force/material perception for steering wheels, seats, and touch panels.
- **Embodied Intelligence Training**: Combining simulation models for tactile strategy training and sim-to-real transfer.

## Competitive Comparison

| Comparison Item | Tashan TS-F+ | PX-6AX | XELA uSkin |
|----------------|--------------|--------|------------|
| Sensing Principle | Capacitive + AI Chip | 6D Hall Array | Magnetoresistive 3-axis |
| Perception Dimensions | 7–10 dimensions | 15 types of tactile information | 3-axis force |
| Special Features | Material recognition, proximity sensing, open-source simulation | Highly integrated dexterous hand | High-density 3-axis, soft and durable |
| Core Advantage | Brain-like chip + simulation ecosystem | Full-stack sensor-dexterous hand-robot | Easy integration, digital output |

## Selection and Deployment Recommendations

- Customize sensor attachment solutions based on the curved structure of the dexterous hand or electronic skin.
- The simulation model can be trained jointly with real sensor data; it is recommended to introduce tactile simulation early in the project to accumulate data.

## References

1. [Tashan Technology Official Website](https://www.iteschina.com)
2. [SENSOR CHINA 2025 – Tashan Technology Exhibition Report](https://www.sekorm.com/news/584921525.html)
3. [21st Century Business Herald – Interview with Tashan Technology CEO](http://mp.weixin.qq.com/s?__biz=Mzk4ODE4MjkzNA==&mid=2247484687&idx=1&sn=84fba2c156a5ed6bbac57f2f0dc097e7)
4. [Appendix D Company Directory](../index-companies.md)
