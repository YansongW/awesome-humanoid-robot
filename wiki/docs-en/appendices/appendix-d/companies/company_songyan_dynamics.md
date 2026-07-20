# Songyan Dynamics / Noetix Robotics

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 松延动力 |
| **English Name** | Songyan Dynamics / Noetix Robotics |
| **Headquarters** | Beijing, China (Beijing Economic-Technological Development Area) |
| **Founded** | September 2023 |
| **Website** | [https://noetixrobotics.com](https://noetixrobotics.com) |
| **Supply Chain Role** | OEM / General-purpose Humanoid Robot + Bionic Robot |
| **Enterprise Attributes** | High-dynamic motion, small size, low cost, Tsinghua background |
| **Parent Company/Group** | None |
| **Data Sources** | Songyan Dynamics official website, Baidu Baike, OFweek/Weikehao |

## Company Profile

Songyan Dynamics focuses on high-dynamic general-purpose humanoid robots and bionic robots, promoting robots into homes and commercial scenarios with small size, low cost, and strong motion performance.

The core team comes from Tsinghua University and other institutions. In March 2025, it released the N2 humanoid robot, which is 1.18 m tall and weighs 30 kg, capable of high-difficulty actions such as running, jumping, and continuous backflips; in October of the same year, it launched the consumer-grade robot Bumi at a price of ten thousand yuan, further lowering the barrier to using humanoid robots. In 2026, it appeared on the CCTV Spring Festival Gala, demonstrating multi-product collaborative performance capabilities.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| High-dynamic General-purpose Humanoid | University research, entertainment performance | N2 / E1 | Research and education, commercial display, competitions |
| Consumer-grade Humanoid | Home companionship, children's education | Bumi | Family education, programming enlightenment |

## Representative Products

### Songyan Dynamics N2

![Songyan Dynamics N2](https://www.noetixrobotics.com/mtsc/uploads/Ckeditor/Images/2025-12-25/N2.webp)

> Image source: Product image from Songyan Dynamics official website.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | 1180×470×290 mm (standing) | Songyan official website / Baidu Baike |
| Weight | Approx. 30 kg | Songyan official website |
| Degrees of Freedom | 18 DOF (leg: 5 DOF×2, arm: 4 DOF×2) | Songyan official website |
| Load/Torque | Knee joint peak torque 150 N·m; continuous walking load approx. 5 kg | Songyan official website |
| Speed/RPM | Peak running speed 3.5 m/s | Songyan official website / Baidu Baike |
| Battery Life | Approx. 1–2 hours (48 V / 7 Ah) | Songyan official website |
| Interfaces/Communication | Wi-Fi 6, Bluetooth 5.2, OTA, secondary development interface (EDU version) | Songyan official website |
| Price | Starting from 39,900 yuan | Public reports |

**Technical Highlights**: World's first multi-scenario continuous backflip, MPC + reinforcement learning motion control, lightweight aluminum alloy structure, dual-encoder joints, optional NVIDIA Jetson Orin Nano Super

**Application Scenarios**: University research, early childhood companionship, entertainment performance, commercial display, robot competitions.

### Bumi

> Bumi: Please visit [official materials](https://noetixrobotics.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Height approx. 94 cm | Public reports |
| Weight | Approx. 12–17 kg | Public reports |
| Degrees of Freedom | 21 DOF | Public reports |
| Load/Torque | Not disclosed | - |
| Speed/RPM | Not disclosed | - |
| Battery Life | Not disclosed | - |
| Interfaces/Communication | Graphical programming platform, open motion control interface | Public reports |
| Price | 9,998 yuan | OFweek/Public reports |

**Technical Highlights**: Consumer-grade humanoid robot at ten thousand yuan level, first launched on JD platform, targeting family education and companionship

**Application Scenarios**: Children's education, home companionship, programming enlightenment.

## Supply Chain Position

- **Upstream Key Components/Materials**: Self-developed high-performance joint motors and drivers, aluminum alloy structural parts, depth cameras, IMU, lithium batteries; core components nearly 100% domestically sourced.
- **Downstream Customers/Application Scenarios**: Universities, K12 education, commercial display, home consumers.
- **Main Competitors/Comparables**: Unitree G1, Accelerated Evolution Booster T1, Zhongqing PM01

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_songyan_dynamics`
- Product Entity: `ent_product_songyan_dynamics_n2`
- Component Entity: `ent_component_songyan_joint_motor`
- Key Relationships:
  - `ent_company_songyan_dynamics` -- `manufactures` --> `ent_product_songyan_dynamics_n2`
  - `ent_company_songyan_dynamics` -- `manufactures` --> `ent_component_songyan_joint_motor`
  - `ent_product_songyan_dynamics_n2` -- `uses` --> `ent_component_songyan_joint_motor`

## References

1. [Songyan Dynamics N2 Product Page](https://noetixrobotics.com/n2)
2. [Songyan Dynamics Official Website](https://noetixrobotics.com/)
3. [Baidu Baike – Songyan Dynamics N2](https://baike.baidu.com/item/%E6%9D%BE%E5%BB%B6%E5%8A%A8%E5%8A%9BN2/67393633)
