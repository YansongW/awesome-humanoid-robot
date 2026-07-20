# Leju Robotics

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 乐聚机器人 |
| **English Name** | Leju Robotics |
| **Headquarters** | Shenzhen, China (founding team from Harbin Institute of Technology) |
| **Founded** | 2016 |
| **Official Website** | [https://www.lejurobot.com](https://www.lejurobot.com) |
| **Supply Chain Role** | Full machine OEM / OpenHarmony humanoid robots |
| **Enterprise Attributes** | HIT background, open-source ecosystem, Huawei partner |
| **Parent Company/Group** | None |
| **Data Sources** | Leju official website, IT Home, 36Kr, Robot Online |

## Company Profile

Leju Robotics was founded by Dr. Leng Xiaokun from Harbin Institute of Technology, focusing on high-dynamic humanoid robots and industrialization.

In collaboration with Shenzhen Kaihong Digital, the company launched KUAVO (Kuafu), China's first high-dynamic humanoid robot based on OpenHarmony (KaihongOS), emphasizing an "out-of-the-box" research platform and a domestically produced supply chain.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| High-Dynamic Humanoid | Research, Service, Industrial Collaboration | KUAVO 4 / 4 Pro | Research & Education, Exhibition Halls, Industry |
| Service Humanoid | Guided Tours, Interaction | KUAVO MY | Exhibition Halls, Retail, Banks |

## Representative Products

### KUAVO 4 Pro

> Leju KUAVO 4 Pro: Please visit [Official Materials](https://www.lejurobot.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | 166 cm | aixzd.com / IT Home |
| Weight | 55 kg | aixzd.com |
| Degrees of Freedom | 30 DOF | IT Home |
| Load/Torque | Single leg peak torque 220 N·m | Xiaoxiong AI Network |
| Speed/Rotation | Walking 5 km/h | aixzd.com |
| Battery Life | Approx. 1 h (6 Ah battery) | aixzd.com |
| Interfaces/Communication | Wi-Fi, KaihongOS, ROS | Public Reports |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: OpenHarmony KaihongOS, three-segment torso design, Gemini-335L binocular depth camera, mid-360 LiDAR, NVIDIA Orin-NX upper computer.

**Application Scenarios**: Research platform, exhibition hall guided tours, commercial services, industrial collaborative handling.

### KUAVO (First Generation)

> Leju KUAVO: Please visit [Official Materials](https://www.lejurobot.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Not disclosed | - |
| Weight | Approx. 45 kg | 36Kr / Robot Online |
| Degrees of Freedom | 26 DOF | Robot Online |
| Load/Torque | Not disclosed | - |
| Speed/Rotation | Max 4.6 km/h; continuous jumps >20 cm | 36Kr |
| Battery Life | Not disclosed | - |
| Interfaces/Communication | OpenHarmony, SDK, Simulation Platform | IT Home |
| Price | Approx. several hundred thousand RMB | 36Kr |

**Technical Highlights**: China's first OpenHarmony humanoid robot capable of jumping and adapting to multi-terrain walking, with open-source motion controller.

**Application Scenarios**: Education & research, special services, preliminary validation for home services.

## Supply Chain Position

- **Upstream Key Components/Materials**: Shenzhen Kaihong Digital KaihongOS, Orbbec depth cameras, Hesai/Livox LiDAR, domestic motors and reducers.
- **Downstream Customers/Application Scenarios**: Universities, Huawei ecosystem exhibition halls, banks, factories.
- **Main Competitors/Counterparts**: Unitree G1, Fourier GR-1, Zhiyuan A2.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_leju`
- Product Entities: `ent_product_leju_kuavo_4pro`, `ent_product_leju_kuavo`
- Key Relationships:
  - `ent_company_leju` -- `manufactures` --> `ent_product_leju_kuavo_4pro`
  - `ent_company_leju` -- `manufactures` --> `ent_product_leju_kuavo`
  - `ent_product_leju_kuavo_4pro` -- `uses` --> `ent_component_orbbec_gemini335`

## References

1. [Leju Robotics Official Website](https://www.lejurobot.com)
2. [IT Home – Leju KUAVO Research Edition Released](https://www.ithome.com/0/800/849.htm)
3. [36Kr – Leju Releases KUAVO](https://so.html5.qq.com/page/real/search_news?docid=70000021_145656eac9b02752)
4. [aixzd.com – KUAVO 4 Pro Introduction](https://aixzd.com/robot/kuavo-4pro)
5. [Appendix D.4 Key Product Wiki](../index-products.md)
