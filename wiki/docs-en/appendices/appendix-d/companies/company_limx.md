# LimX Dynamics

> This entry belongs to [Appendix D: Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 逐际动力 |
| **English Name** | LimX Dynamics |
| **Headquarters** | Shenzhen, China |
| **Founded** | 2022 |
| **Website** | [https://www.limxdynamics.com](https://www.limxdynamics.com) |
| **Supply Chain Role** | Complete Machine OEM / Full-Size General-Purpose Humanoid Robots, Multi-Morphology Robots |
| **Enterprise Attributes** | Invested by Alibaba/JD.com; Motion Intelligence and Legged Robots |
| **Parent Company/Group** | None |
| **Data Sources** | LimX Dynamics Official Website, DoNews, IT Home, 36Kr |

## Company Profile

LimX Dynamics is an AI-driven embodied intelligence company, focusing on full-size general-purpose humanoid robots and multi-morphology robots.

Starting with the four-wheeled legged robot W1, the company has progressively launched the multi-morphology bipedal robot TRON 1, full-size humanoids CL-1 / CL-2, and the LimX Oli released in 2025. LimX Dynamics emphasizes the integration of "big and small brains" and the generalization capability of whole-body mobile manipulation.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Full-Size Humanoid | General Mobile Manipulation | CL-1 / CL-2 / Oli | Smart Manufacturing, Logistics, Home |
| Multi-Morphology Robot | Scientific Research & Rapid Validation | TRON 1 / TRON 2 | Research & Education, Algorithm Validation |
| Wheeled-Legged Robot | High-Speed Obstacle Crossing | W1 | Industrial Inspection, Logistics Distribution |

## Representative Products

### CL-1

> LimX Dynamics CL-1: Please visit [Official Information](https://www.limxdynamics.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Full-Size Humanoid | DoNews |
| Weight | Not disclosed | - |
| Degrees of Freedom | Not disclosed | - |
| Payload/Torque | Can carry 4.1–8.2 kg goods | LimX Dynamics Official Video / DoNews |
| Speed/Rotation Speed | Capable of jogging into a warehouse | DoNews |
| Battery Life | Not disclosed | - |
| Interface/Communication | Not disclosed | - |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: Whole-body mobile manipulation based on real-time perception, weighted squats/lifting/walking, dynamic balance, and disturbance rejection.

**Application Scenarios**: Warehouse handling, shelf restocking, smart manufacturing production lines.

### LimX Oli

> LimX Dynamics LimX Oli: Please visit [Official Information](https://www.limxdynamics.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Full-Size Humanoid | LimX Dynamics Official Website |
| Weight | Not disclosed | - |
| Degrees of Freedom | Not disclosed | - |
| Payload/Torque | Not disclosed | - |
| Speed/Rotation Speed | Not disclosed | - |
| Battery Life | Not disclosed | - |
| Interface/Communication | Not disclosed | - |
| Price | Starting from ¥158,000 | LimX Dynamics Official Website |

**Technical Highlights**: Full-size general-purpose humanoid robot, open for pre-order for research and commercial scenarios.

**Application Scenarios**: Research & education, commercial services, industrial collaboration.

## Supply Chain Position

- **Upstream Key Components/Materials**: Self-developed high-response joint modules; externally purchased motors, reducers, batteries, computing platforms, and vision sensors.
- **Downstream Customers/Application Scenarios**: Smart manufacturing, logistics & warehousing, research universities, preliminary validation for home services.
- **Main Competitors/Benchmarks**: Unitree H1, Robot Era STAR1, Zhiyuan A2-W.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_limx`
- Product Entities: `ent_product_limx_cl1`, `ent_product_limx_oli`
- Key Relationships:
  - `ent_company_limx` -- `manufactures` --> `ent_product_limx_cl1`
  - `ent_company_limx` -- `manufactures` --> `ent_product_limx_oli`
  - `ent_product_limx_cl1` -- `uses` --> `ent_component_limx_joint_module`

## References

1. [LimX Dynamics Official Website](https://www.limxdynamics.com)
2. [DoNews – LimX Dynamics CL-1 Whole-Body Mobile Manipulation](https://www.donews.com/news/detail/4/4507656.html)
3. [IT Home – LimX Dynamics CL-2 Debut](https://www.ithome.com/0/790/893.htm)
4. [36Kr – Shenzhen Humanoid Robot Industry Chain](http://mp.weixin.qq.com/s?__biz=MzU0ODAyNjc5Mg==&mid=2247554433&idx=1&sn=c7320680c83a328047750ab272d3c2f6)
5. [Appendix D.4 Key Product Wiki](../index-products.md)
