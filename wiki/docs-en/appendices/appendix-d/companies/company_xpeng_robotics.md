# XPeng Robotics

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 小鹏机器人 |
| **English Name** | XPeng Robotics |
| **Headquarters** | Guangzhou, Guangdong, China |
| **Founded** | 2024 (robotics business), parent company XPeng Motors founded in 2014 |
| **Official Website** | [https://www.xiaopeng.com/airobot.html](https://www.xiaopeng.com/airobot.html) |
| **Supply Chain Role** | OEM / General-purpose Humanoid Robot |
| **Enterprise Attribute** | Incubated by XPeng Motors; part of the car·robot·flying car ecosystem |
| **Parent Company/Group** | XPeng Motors |
| **Data Source** | XPeng official website, XPeng Tech Day, Huajin Securities research report |

## Company Profile

XPeng Robotics leverages XPeng Motors' expertise in intelligent driving, three-electric systems, and AI large models to develop humanoid robots for factory and commercial service applications.

In November 2024, XPeng released its first humanoid robot, Iron, at AI Tech Day. It stands 178 cm tall, weighs 70 kg, and is equipped with the self-developed Turing AI chip. In November 2025, XPeng unveiled the next-generation Iron, featuring a human-like spine, biomimetic muscles, and fully wrapped flexible skin. It has 82 active degrees of freedom (DoF) across the body and 22 DoF in the hands, and it is the first to use an all-solid-state battery. Mass production is planned for the end of 2026.

## Product Line

| Product Line | Positioning | Representative Product | Application Areas |
|---|---|---|---|
| General-purpose Humanoid Robot | Factory training, commercial guidance, human-machine interaction | Iron (2024/2025 generations) | Automotive manufacturing, offline stores, exhibition hall guidance |
| Future Products | Higher dynamics, more human-like | Iterating mass-production version of Iron | Home services, elderly care and companionship |

## Representative Products

### Iron (First Generation)

![Iron (First Generation)](https://xps01.xiaopeng.com/cms/content/pic/2026/02-28/23-34-440349-1822507725.png)

> Image source: XPeng Motors official press release.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | 178 cm | Public reports |
| Weight | 70 kg | Public reports |
| Degrees of Freedom | 62 active DoF | Public reports |
| Payload/Torque | 15 DoF in hands, supports tactile feedback | Public reports |
| Speed/RPM | Not disclosed | - |
| Battery Life | Not disclosed | - |
| Interface/Communication | Not disclosed | - |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: Self-developed Turing AI chip (40 cores, 3000 TOPS), 720° Eagle Eye Vision, Tianji AIOS, end-to-end large model + reinforcement learning

**Application Scenarios**: P7 production training at XPeng's Guangzhou factory, screw tightening, material sorting, production form inspection; future applications in store guidance and commercial services.

### Iron (Second Generation, 2025 Tech Day)

> Iron (Second Generation, 2025 Tech Day): Please visit [official materials](https://www.xiaopeng.com/airobot.html) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | 178 cm (official website) / ≤ 170 cm (press conference statement) | XPeng official website / Huajin Securities research report |
| Weight | Not disclosed | - |
| Degrees of Freedom | 82 active DoF | 2025 XPeng Tech Day |
| Payload/Torque | 22 DoF in hands, fingertip tactile feedback precision 0.01 mm | Public reports |
| Speed/RPM | Walking speed approx. 1.2 m/s | Public reports |
| Battery Life | Approx. 8 hours (all-solid-state battery) | Public reports |
| Interface/Communication | Open SDK | Public reports |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: Human-like spine, biomimetic muscles, fully wrapped flexible skin, 3 Turing AI chips (2250 TOPS), all-solid-state battery, second-generation VLA large model

**Application Scenarios**: Commercial service guidance, shopping assistance, training guidance; mass production planned for the end of 2026.

## Supply Chain Position

- **Upstream Key Components/Materials**: Self-developed Turing AI chip, solid-state battery, harmonic reducer, flexible skin and tactile sensors; leverages XPeng Motors' intelligent driving and three-electric supply chain.
- **Downstream Customers/Application Scenarios**: XPeng Motors factory training, offline store guidance and shopping assistance, commercial display and service.
- **Main Competitors/Benchmarks**: Tesla Optimus, UBTECH Walker, Figure 02

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_xpeng_robotics`
- Product Entity: `ent_product_xpeng_iron`
- Component Entity: `ent_component_xpeng_turing_chip`
- Key Relationships:
  - `ent_company_xpeng_robotics` -- `manufactures` --> `ent_product_xpeng_iron`
  - `ent_company_xpeng_robotics` -- `manufactures` --> `ent_component_xpeng_turing_chip`
  - `ent_product_xpeng_iron` -- `uses` --> `ent_component_xpeng_turing_chip`

## References

1. [XPeng AI Robot Official Website](https://www.xiaopeng.com/airobot.html)
2. [XPeng Robot Mass Production Base News](https://www.xiaopeng.com/news/company_news/5537.html)
3. [Huajin Securities – Automotive Industry Weekly Report](https://pdf.dfcfw.com/pdf/H3_AP202511111779514833_1.pdf)
