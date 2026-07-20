# EngineAI

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 众擎机器人 |
| **English Name** | EngineAI |
| **Headquarters** | Shenzhen, Guangdong, China |
| **Founded** | 2023 |
| **Website** | [https://www.engineai.com.cn](https://www.engineai.com.cn) |
| **Supply Chain Role** | OEM / General-purpose Humanoid Robot |
| **Company Attributes** | High-dynamic, Open-source, Anthropomorphic Gait |
| **Parent Company/Group** | None |
| **Data Sources** | EngineAI Official Website, Official FAQ, Qubit/Robot Lecture Hall |

## Company Overview

EngineAI focuses on high-dynamic motion and full-stack self-developed joints, providing an open humanoid robot platform for scientific research, education, and industrial manufacturing.

EngineAI has released the PM01 lightweight open-source humanoid robot and the SE01 full-size anthropomorphic gait humanoid robot. The PM01 is 1.38 m tall, weighs approximately 42 kg, has ≥23 degrees of freedom (DOF) across the body, and its waist can rotate 320°. The SE01 is 1.7 m tall, weighs approximately 55 kg, has 32 DOF, uses aerospace-grade aluminum alloy, and emphasizes natural gait and long lifespan.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|---|---|---|---|
| Lightweight Open-source Humanoid | Scientific Research, Education, Algorithm Validation | PM01 | Universities, Laboratories, Developers |
| Full-size General-purpose Humanoid | Industrial and Home Scenarios | SE01 | Smart Manufacturing, Warehousing, Services |

## Representative Products

### EngineAI PM01

![EngineAI PM01](https://cn-engineai-1304599088.cos.ap-guangzhou.myqcloud.com/uploads/upload/images/20251029/668bd44456c24b778a8c7d824e42d858.png)

> Image source: EngineAI official website product image.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | Standing 1400(H)×535.55(W)×252.66(D) mm | EngineAI Official Website |
| Weight | Commercial version approx. 42 kg; Education version approx. 43 kg | EngineAI Official Website |
| Degrees of Freedom | Commercial version 23 DOF; Education version 24 DOF | EngineAI Official Website |
| Load/Torque | Knee joint peak torque 145 N·m (Q90H motor) | EngineAI Official Website |
| Speed | Movement speed >2 m/s (hardware supported) | EngineAI Official Website |
| Battery Life | Approx. 2 hours (10000 mAh quick-release battery) | EngineAI Official Website |
| Interfaces/Communication | Education version supports secondary development, equipped with NVIDIA Jetson Orin NX (16G) | EngineAI Official Website |
| Price | Commercial version 88,000 RMB (tax included) | Official FAQ |

**Technical Highlights**: Full-stack self-developed integrated joints, waist rotation >300°, open-source training/deployment code, handheld remote control, interactive screen.

**Application Scenarios**: Scientific research and education algorithm validation, industrial manufacturing secondary development, commercial displays and dance performances.

### EngineAI SE01

> EngineAI SE01: Please visit [Official Materials](https://www.engineai.com.cn) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | 170 cm (height) | Public Reports |
| Weight | Approx. 55 kg | Public Reports |
| Degrees of Freedom | 32 DOF | Public Reports |
| Load/Torque | Knee joint maximum torque 186 N·m | Robot Dealer Materials |
| Speed | Normal walking speed 2 m/s | Public Reports |
| Battery Life | Approx. 2 hours | Public Reports |
| Interfaces/Communication | Intel RealSense D435, 360° LiDAR, 6 HD cameras | Public Reports |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: Aerospace-grade aluminum, anthropomorphic natural gait, multi-layer planning algorithms, 5–10 year design lifespan.

**Application Scenarios**: Industrial manufacturing, warehouse inspection, home services, and other complex scenarios.

## Supply Chain Position

- **Upstream Key Components/Materials**: Self-developed Q90H/Q25H integrated joint motors, planetary/harmonic reducers, motors; Intel RealSense, NVIDIA Jetson, batteries.
- **Downstream Customers/Application Scenarios**: University research, developers, industrial manufacturing enterprises, commercial displays.
- **Main Competitors/Comparables**: Unitree G1/H1, Zhiyuan Robot, Fourier GR Series.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_engineai`
- Product Entity: `ent_product_engineai_pm01`
- Component Entity: `ent_component_engineai_q90h`
- Key Relationships:
  - `ent_company_engineai` -- `manufactures` --> `ent_product_engineai_pm01`
  - `ent_company_engineai` -- `manufactures` --> `ent_component_engineai_q90h`
  - `ent_product_engineai_pm01` -- `uses` --> `ent_component_engineai_q90h`

## References

1. [EngineAI PM01 Product Page](https://www.engineai.com.cn/product-pm01.html)
2. [EngineAI SE01 Product Page](https://en.engineai.com.cn/product-se01)
3. [EngineAI FAQ](https://www.engineai.com.cn/about-news-media/23.html)
