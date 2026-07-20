# Fourier Intelligence

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).  
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 傅利叶智能 |
| **English Name** | Fourier Intelligence |
| **Headquarters** | Shanghai, China |
| **Founded** | 2015 |
| **Website** | [https://www.fftai.cn](https://www.fftai.cn) |
| **Supply Chain Role** | OEM / Rehabilitation Robots + General-Purpose Humanoid Robots |
| **Enterprise Attribute** | Leading rehabilitation robot company expanding into general-purpose robots |
| **Parent Company/Group** | None |
| **Data Source** | Fourier official website, IT Home, Securities Times, Arterial Network |

## Company Profile

Fourier Intelligence started with exoskeletons and rehabilitation robots, gradually entering the field of general-purpose humanoid robots, with the vision of "empowering life with robotics technology."

In 2023, it released the GR-1, recognized as one of the first bipedal humanoid robots in China to achieve mass production and delivery. In 2025, it released the GR-3, positioned as an interactive companion Care-bot, emphasizing soft skin covering and a full-sense interaction system.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| General-Purpose Humanoid | Research, guided tours, industrial collaboration | GR-1 / GR-2 | Research & education, exhibition guided tours, rehabilitation |
| Companion Humanoid | Elderly care, companionship, interaction | GR-3 | Elderly care, medical, home |
| Rehabilitation Robots | Limb rehabilitation training | ExoMotus / AnkleMotus, etc. | Hospitals, rehabilitation centers |

## Representative Products

### GR-1

> Fourier GR-1: Please visit [official materials](https://www.fftai.cn) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Height | 165 cm | Fourier official website |
| Weight | 55 kg | Fourier official website |
| Degrees of Freedom | 44 DOF | Fourier official website |
| Load/Torque | Max joint torque 230 N·m | Fourier official website |
| Speed/Rotation | Gait walking 5 km/h | Fourier official website |
| Battery Life | Not disclosed | - |
| Interface/Communication | Not disclosed | - |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: Self-developed FSA integrated actuator, 6×RGB cameras for 360° perception, BEV+Transformer+OCC.

**Application Scenarios**: Research & education, AI embodied agents, reception & guided tours, rehabilitation assistance.

### GR-3

> Fourier GR-3: Please visit [official materials](https://www.fftai.cn) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Height | 165 cm | STAR Market Daily / Beijing Business Today |
| Weight | 71 kg | STAR Market Daily / Beijing Business Today |
| Degrees of Freedom | 55 DOF | Public reports |
| Load/Torque | 12 DOF dexterous hand | Public reports |
| Speed/Rotation | Not disclosed | - |
| Battery Life | Approx. 3 h (dual battery hot-swap) | Electronic Enthusiast Network |
| Interface/Communication | Not disclosed | - |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: Full-sense interaction system (31 sets of auditory/visual/tactile sensors), soft skin covering, micro-expressions and eye tracking.

**Application Scenarios**: Elderly care companionship, child interaction, rehabilitation institutions, public space services.

## Supply Chain Position

- **Upstream Key Components/Materials**: Self-developed FSA integrated actuator; externally purchased motors, reducers, sensors, soft covering materials.
- **Downstream Customers/Application Scenarios**: Hospitals, rehabilitation centers, research institutions, elderly care facilities.
- **Main Competitors/Comparables**: UBTECH Walker, Tesla Optimus, Japan's Cyberdyne.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_fourier`
- Product Entities: `ent_product_fourier_gr1`, `ent_product_fourier_gr3`
- Key Relationships:
  - `ent_company_fourier` -- `manufactures` --> `ent_product_fourier_gr1`
  - `ent_company_fourier` -- `manufactures` --> `ent_product_fourier_gr3`
  - `ent_product_fourier_gr1` -- `uses` --> `ent_component_fourier_fsa_actuator`

## References

1. [Fourier Intelligence Official Website](https://www.fftai.cn)
2. [Fourier GR-1 Product Page](https://www.fftai.cn/products-gr1)
3. [IT Home – Fourier GR-3 Launch](https://www.ithome.com/0/810/472.htm) (similar reports)
4. [Securities Times / STAR Market Daily – GR-3 Report](https://www.msn.cn/zh-cn/...)
5. [Appendix D.4 Key Product Wiki](../index-products.md)
