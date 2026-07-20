# Mech-Mind Robotics

> This entry belongs to [Appendix D: Enterprise/Product Wiki](../../appendix-d.md).
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 梅卡曼德 (Mech-Mind (Xiong'an) Robotics Technology Co., Ltd.) |
| **English Name** | Mech-Mind Robotics |
| **Headquarters** | Beijing, China (with branches in Shanghai, Xiong'an, Munich, Tokyo, Seoul, etc.) |
| **Founded** | 2016 |
| **Official Website** | [https://www.mech-mind.com.cn](https://www.mech-mind.com.cn) |
| **Supply Chain Role** | Sensors / AI+3D Vision and Embodied Intelligence "Eye-Brain-Hand" |
| **Company Type** | AI+Robotics Unicorn, Leading Enterprise in Embodied Intelligent Robotics |
| **Parent Company/Group** | None |
| **Data Sources** | Mech-Mind official website, WAIC 2026 official reports, Ringier Industry Resources |

## Company Overview

Mech-Mind Robotics Technology Co., Ltd. is a well-known domestic provider of AI+3D+intelligent industrial robot solutions, focusing on the R&D, production, and sales of software and hardware products in the 3D vision field. The company has built a complete embodied intelligence technology system covering "Eye, Brain, and Hand." Among them, the "Eye+Brain" products have been widely applied in dozens of industries, including automotive, logistics, new energy, construction machinery, home appliances, and medical, serving over 100 Fortune 500 customers globally.

The company's product line includes the Mech-Eye industrial-grade 3D camera, Mech-Vision machine vision software, Mech-Viz robot programming software, Mech-GPT multimodal large model, and the embodied intelligence "Eye-Brain-Hand" robot platform. At WAIC 2026, Mech-Mind (Booth H1-A530) showcased six intelligent robot units, including humanoid robot collaborative loading/unloading, autonomous shelf picking, and generalized grasping of transparent objects.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Industrial 3D Camera | High-precision 3D perception hardware | Mech-Eye LSR L / ULTRA M / NANO | Unordered grasping, depalletizing, assembly |
| Machine Vision Software | Graphical vision engineering platform | Mech-Vision | Industrial vision guidance, quality inspection |
| Robot Programming Software | No-code robot programming | Mech-Viz | Trajectory planning, collision detection |
| Embodied Intelligence Brain | Multimodal large model driven | Mech-GPT | Human-robot interaction, autonomous task planning |
| Embodied Intelligence Platform | Eye-Brain-Hand collaborative system | "Eye-Brain-Hand" Robot Platform | Humanoid robots, dual-arm collaboration |

## Representative Products

### Mech-Eye LSR L

> Mech-Eye LSR L: Please visit [official documentation](https://www.mech-mind.com.cn) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Not disclosed | - |
| Weight | Not disclosed | - |
| Working Distance | Long range, large field of view | Official website |
| Accuracy | Visual positioning accuracy up to ±0.2 mm | Smzdm / AW 2026 report |
| Ambient Light Resistance | Stable imaging under >30,000 lux | World Robot Conference product manual |
| Interface/Communication | Supports TCP / Modbus / EtherNet/IP | Official website |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: Industrial-grade laser 3D camera, long-range high precision, excellent ambient light resistance, supports color point clouds.

**Application Scenarios**: Metal part grasping, depalletizing, positioning assembly, welding guidance, online measurement.

### Mech-GPT

> Mech-GPT: Please visit [official documentation](https://www.mech-mind.com.cn) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Model Type | Multimodal large model | Official website |
| Input Modalities | Vision, language, robot state | Official website |
| Output | Action planning, human-robot interaction response | Official website |
| Interface/Communication | Integrated with Mech-Mind Eye-Brain-Hand platform | Official website |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: Introduces large model capabilities into robot task understanding and natural interaction, achieving a "perception-decision-execution" closed loop.

**Application Scenarios**: Humanoid robot autonomous picking, sorting massive objects, generalized grasping of transparent objects, human-robot dialogue.

## Supply Chain Position

- **Upstream Key Components/Materials**: Self-developed 3D camera optical modules and algorithms; externally purchased lasers, camera modules, computing units, structural parts.
- **Downstream Customers/Application Scenarios**: Automotive OEMs, logistics and warehousing, new energy batteries, construction machinery, home appliances, medical manufacturing enterprises.
- **Main Competitors/Peers**: CrossWise, Orbbec, Perceptin, Cognex, Basler.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_mech_mind`
- Product Entities: `ent_product_mech_mind_mech_eye_lsr_l`, `ent_product_mech_mind_mech_gpt`
- Key Relationships:
  - `ent_company_mech_mind` -- `manufactures` --> `ent_product_mech_mind_mech_eye_lsr_l`
  - `ent_company_mech_mind` -- `manufactures` --> `ent_product_mech_mind_mech_gpt`

## References

1. [Mech-Mind Official Website](https://www.mech-mind.com.cn)
2. [Mech-Mind – WAIC 2026 Official Report](https://mech-mind.com.cn/NewsStd/mech-mind-waic-2026-shows-embodied-ai-breakthrough.html)
3. [Ringier Industry Resources – Mech-Mind at WAIC 2026](https://www.industrysourcing.cn/article/477721)
4. [Smzdm – Mech-Mind AW 2026 New Products](https://post.smzdm.com/p/ae6mkonk)
