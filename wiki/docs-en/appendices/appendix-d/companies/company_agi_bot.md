# AgiBot

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 智元机器人 (智元创新) |
| **English Name** | AgiBot |
| **Headquarters** | Shanghai, China |
| **Founded** | 2023 |
| **Website** | [https://www.zhiyuan-robot.com](https://www.zhiyuan-robot.com) |
| **Supply Chain Role** | Complete Machine OEM / General-Purpose Humanoid Robot |
| **Company Type** | Startup Unicorn, Leader in Embodied Intelligence |
| **Parent Company/Group** | None |
| **Data Source** | AgiBot Official Website, IT Home, Robothub, Public Reports |

## Company Profile

AgiBot was founded by "ZhiHuijun" Peng Zhihui and others, positioning itself as an embodied intelligence company with the mission of "creating unlimited productivity through intelligent robots."

The company rapidly iterates the Expedition series of humanoid robots, emphasizing multimodal interaction, enterprise knowledge bases, and large-scale commercial deployment. In 2025, it announced that the Expedition A2 became the world's first humanoid robot to simultaneously obtain four certifications from China, the United States, and Europe.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|---|---|---|---|
| Interactive Service | Exhibition Hall Guide, Reception, Commercial Performance | Expedition A2 / A2 Lite | Exhibition Halls, Shopping Malls, Performing Arts |
| Flexible Manufacturing | Wheeled Mobile Manipulation | Expedition A2-W | Factory Material Handling, Assembly |
| Heavy-Duty Special | High-Load Industrial Scenarios | Expedition A2-Max | Heavy-Duty Logistics |

## Representative Products

### Expedition A2

> AgiBot Expedition A2: Please visit [Official Materials](https://www.zhiyuan-robot.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | 169–170 cm | Multiple media reports |
| Weight | Approx. 69 kg | IT Home |
| Degrees of Freedom | 40+ DOF | Official promotion |
| Payload/Torque | Max single-arm payload 5 kg | Official specifications page |
| Speed/RPM | Max walking speed 1.2 m/s (after V1.3 OTA) | IT Home |
| Battery Life | Approx. 2 h (700 Wh battery) | Public reports |
| Interface/Communication | Not disclosed | - |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: Embodied Intelligence Brain EI-Brain, On-Device Multimodal Large Model, PLd-Level Safety Protection, Four Certifications from China, US, and Europe.

**Application Scenarios**: Automotive Showroom Sales Consultant, Shopping Mall Guide, Evening Gala Performance, Front Desk Reception.

### Expedition A2 Lite

> AgiBot Expedition A2 Lite: Please visit [Official Materials](https://www.zhiyuan-robot.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | 169 cm | Robothub |
| Weight | 64 kg | Robothub |
| Degrees of Freedom | 23 DOF | Robothub |
| Payload/Torque | Dual-arm payload 4 kg | Robothub |
| Speed/RPM | 2.88 km/h | Robothub |
| Battery Life | 4.5 h | Robothub |
| Interface/Communication | Not disclosed | - |
| Price | Approx. 198,000 RMB | Robothub |

**Technical Highlights**: Full-size performance platform for entertainment and commercial shows, supporting group control, VR teleoperation, and secondary creation.

**Application Scenarios**: Commercial Performances, Event Traffic Generation, IP Customization.

## Supply Chain Position

- **Upstream Key Components/Materials**: Self-developed joints and dexterous hands; externally purchased motors, reducers, batteries, LiDAR, cameras.
- **Downstream Customers/Application Scenarios**: Automotive OEMs, Shopping Malls, Cultural Tourism, Smart Manufacturing Factories.
- **Main Competitors/Comparables**: UBTECH Walker A2, Fourier GR-3, Galbot.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_agi_bot`
- Product Entities: `ent_product_agi_bot_a2`, `ent_product_agi_bot_a2_lite`
- Key Relationships:
  - `ent_company_agi_bot` -- `manufactures` --> `ent_product_agi_bot_a2`
  - `ent_company_agi_bot` -- `manufactures` --> `ent_product_agi_bot_a2_lite`
  - `ent_product_agi_bot_a2` -- `uses` --> `ent_component_lidar`

## References

1. [AgiBot Official Website](https://www.zhiyuan-robot.com)
2. [IT Home – Expedition A2 Launch and OTA Report](https://www.ithome.com/0/788/620.htm)
3. [Robothub – Expedition A2 Lite](https://www.robothub.app/zh/robots/expedition-a2-lite)
4. [Zhihu – Expedition A2 China-US-EU Certification](https://zhuanlan.zhihu.com/p/1911481259995168918)
5. [Appendix D.4 Key Product Wiki](../index-products.md)
