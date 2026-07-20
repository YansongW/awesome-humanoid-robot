# Booster Robotics

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 加速进化 |
| **English Name** | Booster Robotics |
| **Headquarters** | Beijing, China |
| **Founded** | 2023 |
| **Website** | [https://www.booster.tech](https://www.booster.tech) |
| **Supply Chain Role** | OEM / Humanoid Robot Development Platform |
| **Enterprise Attributes** | Tsinghua background, developer/competition platform, RoboCup champion |
| **Parent Company/Group** | None |
| **Data Sources** | Booster official website, Bipedal documentation, STAR Market Daily/36Kr |

## Company Overview

Booster Robotics provides lightweight, flexible, and durable humanoid robot platforms for developers, universities, and robotics competitions. It won the 2025 RoboCup AdultSize championship.

The Booster T1 stands approximately 1.2 m tall, weighs 30 kg, has 23 DOF, and is equipped with an Intel i7 1370p and NVIDIA Jetson AGX Orin (200 TOPS). It supports ROS2, simulation platforms, and mobile app control. The T1 can perform dynamic actions such as walking, soccer, push-ups, and martial arts, making it a widely adopted platform in research and competition fields.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Developer Humanoid Robot | Research, competition, education | Booster T1 | Universities, RoboCup, developers |
| Entry-Level Platform | Low-cost education | Booster K1 | Education, beginners |

## Representative Products

### Booster T1

![Booster T1](https://www.althumans.com/media/catalog/product/cache/7e65f7ea2c9ff177580b02a356862407/a/h/ah-booster-t1-01.jpg)

> Image source: AltHumans product image (Booster T1 distributor).

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | 118 cm (height) | Booster official website / Bipedal documentation |
| Weight | 30 kg | Booster official website / Bipedal documentation |
| Degrees of Freedom | 23 DOF (optional configuration up to 41 DOF) | Bipedal documentation / Public reports |
| Load/Torque | Knee joint peak torque 130 N·m; hollow shaft joint motor | Bipedal documentation |
| Speed/RPM | Omnidirectional walking, specific speed not disclosed | Bipedal documentation |
| Battery Life | 10.5 Ah battery; approximately 2 h walking, 4 h standing | Booster official website |
| Interfaces/Communication | ROS 2, USB, Ethernet, Wi-Fi 6, Bluetooth 5.2, mobile app | Booster official website |
| Price | Starting from approximately ¥199,000 (public reports) | 36Kr / Public reports |

**Technical Highlights**: Intel i7 1370p + NVIDIA Jetson AGX Orin 200 TOPS, omnidirectional walking, anti-interference, simulation platform support (Isaac Sim/Mujoco), RoboCup 2025 champion edition

**Application Scenarios**: University research, RoboCup competitions, motion control algorithm validation, AI training, industrial automation prototyping.

### Booster K1

> Booster K1: Please visit [official materials](https://www.booster.tech) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Not disclosed | - |
| Weight | Not disclosed | - |
| Degrees of Freedom | Not disclosed | - |
| Load/Torque | Not disclosed | - |
| Speed/RPM | Not disclosed | - |
| Battery Life | Not disclosed | - |
| Interfaces/Communication | Not disclosed | - |
| Price | Starting from $5,999 USD | Booster official website |

**Technical Highlights**: Entry-level embodied intelligence development platform, lowering the barrier to learning and developing humanoid robots

**Application Scenarios**: Education, entry-level development, lightweight research.

## Supply Chain Position

- **Upstream Key Components/Materials**: Self-developed hollow shaft joint motors, NVIDIA Jetson AGX Orin, Intel i7 computing platform, depth cameras, 9-axis IMU, battery.
- **Downstream Customers/Application Scenarios**: University research teams, RoboCup teams, developers, industrial prototyping clients.
- **Main Competitors/Comparables**: Unitree G1, Songyan N2, Robotis OP3

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_booster_robotics`
- Product Entity: `ent_product_booster_t1`
- Key Relationships:
  - `ent_company_booster_robotics` -- `manufactures` --> `ent_product_booster_t1`
  - `ent_product_booster_t1` -- `uses` --> `ent_component_nvidia_jetson_agx_orin`

## References

1. [Booster T1 Official Website](https://www.booster.tech/booster-t1/)
2. [Bipedal – Booster T1 Documentation](http://www.docs.bipedal.de/projects/t1/html/overview.html)
3. [STAR Market Daily – CES Report](https://www.cls.cn/detail/1912332)
