# Astribot / Astribot

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).  
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 星尘智能 |
| **English Name** | Astribot |
| **Headquarters** | Shenzhen, Guangdong, China |
| **Founded** | 2022 |
| **Website** | [https://www.astribot.com](https://www.astribot.com) |
| **Supply Chain Role** | OEM / Wheeled Humanoid Robot + Operational AI Robot |
| **Enterprise Attributes** | Cable-driven transmission, Design for AI, AI Robot Assistant |
| **Parent Company/Group** | None |
| **Data Source** | Astribot official website, RobotScope, Baidu Baike |

## Company Profile

Astribot focuses on general-purpose AI robot assistants, leveraging cable-driven transmission and high-dynamic manipulation capabilities to build wheeled humanoid robots that can work in real-world environments.

In August 2024, Astribot released the Astribot S1, positioned as a "versatile operational" AI robot with manipulation speed and precision close to that of an adult human. It can perform complex tasks such as folding clothes, cooking, calligraphy, and brewing Kung Fu tea. In 2025, the company launched the S1-U semi-body commercial version and the T1 compact wheeled product line, continuously expanding deployment in research, service, and industrial scenarios.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Full-size Operational Humanoid | Research, Service, Flexible Manufacturing | Astribot S1 | Research & Education, New Retail, Smart Elderly Care |
| Commercial/Compact Version | Semi-body Commercial, Low-cost Wheeled | S1-U / T1 | Commercial Service, Home Assistant |

## Representative Products

### Astribot S1

![Astribot S1](https://cdn.shopify.com/s/files/1/0659/1437/2184/files/Astribot_image_1_resized.png?v=1768350773&width=800)

> Image source: Astribot product image (third-party distributor).

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | 170 cm (height) | Astribot official website |
| Weight | 80 kg | Astribot official website |
| Degrees of Freedom | 23 DOF total (7 DOF per arm × 2, 4 DOF torso, 2 DOF head, 3 DOF omnidirectional wheeled base) | Astribot official website / Technical documentation |
| Payload/Torque | Rated payload 5 kg per arm at horizontal extension, peak 10 kg | Astribot official website |
| Speed/RPM | End-effector max speed ≥10 m/s | Astribot official website |
| Battery Life | 4–6 hours (supports plug-in power) | Astribot official website |
| Interface/Communication | ROS 2 / Python SDK, Gigabit Ethernet, Wi-Fi | Technical documentation |
| Price | Research version approx. ¥500,000; Enterprise/research grade approx. $96,000–$150,000 | Public reports |

**Technical Highlights**: Cable-driven transmission, ±0.1 mm repeatability, 100 m/s² end-effector acceleration, force-controlled safety, VR teleoperation, and zero-code visual interface.

**Application Scenarios**: Folding clothes, cooking, cleaning, calligraphy, brewing Kung Fu tea, research experiments, elderly care companionship, new retail displays.

### Astribot S1-U

> Astribot S1-U: Please visit [official materials](https://www.astribot.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Not disclosed | - |
| Weight | Not disclosed | - |
| Degrees of Freedom | Not disclosed | - |
| Payload/Torque | Not disclosed | - |
| Speed/RPM | Not disclosed | - |
| Battery Life | Not disclosed | - |
| Interface/Communication | Not disclosed | - |
| Price | Not disclosed | Contact for pricing |

**Technical Highlights**: Semi-body commercial version of S1, designed for desktop and service scenarios, lowering deployment barriers.

**Application Scenarios**: Commercial service, exhibition hall guidance, desktop operations.

## Supply Chain Position

- **Upstream Key Components/Materials**: Self-developed cable-driven actuators, high-performance motors, force/torque sensors, computing platforms; externally purchased cameras, LiDAR, batteries.
- **Downstream Customers/Application Scenarios**: Research & education, smart elderly care, home services, new retail displays, flexible manufacturing small-batch assembly.
- **Main Competitors/Peers**: Figure 02, Tesla Optimus, UBTECH Walker, Zhiyuan Robot

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_astribot`
- Product Entity: `ent_product_astribot_s1`
- Component Entity: `ent_component_astribot_cable_actuator`
- Key Relationships:
  - `ent_company_astribot` -- `manufactures` --> `ent_product_astribot_s1`
  - `ent_company_astribot` -- `manufactures` --> `ent_component_astribot_cable_actuator`
  - `ent_product_astribot_s1` -- `uses` --> `ent_component_astribot_cable_actuator`

## References

1. [Astribot Official Product Page](https://www.astribot.com/en/product)
2. [RobotScope – Astribot Company Profile](https://robotscope.net/companies/astribot/)
3. [Baidu Baike – Astribot S1](https://baike.baidu.com/item/Astribot%20S1/64813493)
