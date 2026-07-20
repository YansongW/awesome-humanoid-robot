# EngineAI PM01

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [EngineAI](../companies/company_engineai.md) |
| **Product Category** | General-purpose humanoid robot |
| **Release Date** | End of 2024 / 2025 |
| **Status** | Mass production/commercial |
| **Website/Source** | [https://www.engineai.com.cn](https://www.engineai.com.cn) |

## Product Overview

Algorithm validation for scientific research and education, secondary development for industrial manufacturing, commercial display and dance performance.

EngineAI PM01 is a representative product of EngineAI. It features full-stack self-developed integrated joints, waist rotation >300°, open-source training/deployment code, handheld remote control, and an interactive screen. Key specifications include: standing dimensions 1400(H)×535.55(W)×252.66(D) mm, commercial version approx. 42 kg; education version approx. 43 kg (weight), commercial version 23 DOF; education version 24 DOF (degrees of freedom).

## Product Image

![EngineAI PM01](https://cn-engineai-1304599088.cos.ap-guangzhou.myqcloud.com/uploads/upload/images/20251029/668bd44456c24b778a8c7d824e42d858.png)

> Image source: EngineAI official website product image.

## Specification Table

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Dimensions | Standing 1400(H)×535.55(W)×252.66(D) mm | EngineAI official website |
| Weight | Commercial version approx. 42 kg; Education version approx. 43 kg | EngineAI official website |
| Degrees of Freedom | Commercial version 23 DOF; Education version 24 DOF | EngineAI official website |
| Load/Torque | Knee joint peak torque 145 N·m (Q90H motor) | EngineAI official website |
| Speed | Movement speed >2 m/s (hardware supported) | EngineAI official website |
| Battery Life | Approx. 2 hours (10000 mAh quick-release battery) | EngineAI official website |
| Interface/Communication | Education version supports secondary development, equipped with NVIDIA Jetson Orin NX (16G) | EngineAI official website |
| Price | Commercial version 88,000 RMB (tax included) | Official FAQ |

## Supply Chain Position

- **Manufacturer**: [EngineAI](../companies/company_engineai.md)
- **Core Components/Technology Source**: Self-developed Q90H/Q25H integrated joint motors, planetary/harmonic reducers, motors; Intel RealSense, NVIDIA Jetson, battery.
- **Downstream Applications/Customers**: Algorithm validation for scientific research and education, secondary development for industrial manufacturing, commercial display and dance performance.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_engineai_pm01`
- Manufacturer Entity: `ent_company_engineai`
- Key Relationships:
  - `rel_ent_company_engineai_manufactures_ent_product_engineai_pm01` (`ent_company_engineai` → `manufactures` → `ent_product_engineai_pm01`)
  - `ent_product_engineai_pm01` -- `uses` --> `ent_component_engineai_q90h`

## Application Scenarios

- **Algorithm validation for scientific research and education, secondary development for industrial manufacturing, commercial display and dance performance.**
- **Industrial Manufacturing**: Performs tasks such as handling, assembly, and inspection on flexible production lines.
- **Commercial Services**: Used for guided tours, reception, display, and brand interaction.

## Competitive Comparison

| Comparison Item | This Product | Main Competitors |
|-----------------|--------------|------------------|
| Positioning | General-purpose humanoid robot | Similar products depend on specific scenarios |
| Core Advantages | Full-stack self-developed integrated joints, waist rotation >300°, open-source training/deployment code, handheld remote control, interactive screen | Not disclosed |
| Price | Commercial version 88,000 RMB (tax included) | Not disclosed |

## Purchase and Deployment Recommendations

- It is recommended to confirm the latest software version, SDK support, and after-sales training through official channels.
- Research and education users should prioritize evaluating secondary development interfaces, simulation platform compatibility, and community activity.
- Industrial users need to verify load, precision, protection level, and integration interfaces based on specific processes.

## References

1. [EngineAI PM01 Product Page](https://www.engineai.com.cn/product-pm01.html)
2. [EngineAI SE01 Product Page](https://en.engineai.com.cn/product-se01)
3. [EngineAI FAQ](https://www.engineai.com.cn/about-news-media/23.html)
