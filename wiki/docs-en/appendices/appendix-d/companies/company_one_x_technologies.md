# 1X Technologies

> This entry belongs to [Appendix D: Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 1X Technologies |
| **English Name** | 1X Technologies |
| **Headquarters** | Moss, Norway / Santa Clara, California, USA |
| **Founded** | 2014 |
| **Website** | [https://www.1x.tech](https://www.1x.tech) |
| **Supply Chain Role** | Consumer-grade humanoid robots, embodied learning |
| **Enterprise Attribute** | Startup (invested by OpenAI, etc.) |
| **Parent Company/Group** | None |
| **Data Source** | 1X Technologies official website, public product pages, third-party specification summaries |

## Company Overview

1X Technologies is dedicated to creating safe, lightweight, general-purpose humanoid robots for the home, featuring tendon-driven actuation and soft exoskeleton design.

1X's products include the bipedal NEO and the wheeled dual-arm EVE. NEO emphasizes home safety, low noise, and natural interaction, utilizing embodied learning through 1X Studio remote teaching.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| NEO | Bipedal home/commercial humanoid | NEO | Home services, caregiving, retail |
| EVE | Wheeled dual-arm robot | EVE | Commercial security, logistics, research |

## Representative Products

### 1X NEO

> 1X NEO: Please visit [official materials](https://www.1x.tech) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 167–168 cm (height) | Public information |
| Weight | Approx. 30 kg | Public information |
| Degrees of Freedom | 39 | HumanoidHub summary |
| Payload/Torque | Overall carrying approx. 25 kg; max lifting approx. 70 kg | Public information |
| Speed/Rotation | Walking approx. 1.4 m/s; max running approx. 6.2 m/s | Public information |
| Battery Life | Approx. 4 hours (842 Wh) | Public information |
| Interface/Communication | 1X NEO Cortex (NVIDIA Jetson Thor), Wi-Fi/Bluetooth/5G | Public information |
| Price | 20,000 USD + 499 USD/month subscription; deposit 200 USD | Public information |

**Technical Highlights**: Tendon-driven Myofibers, soft exoskeleton with 3D lattice polymer, low noise, home-safe design, expert teleop embodied learning.

**Application Scenarios**: Household chores, elderly care, light commercial services, research.

### 1X EVE

> 1X EVE: Please visit [official materials](https://www.1x.tech) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Not disclosed | - |
| Weight | Not disclosed | - |
| Degrees of Freedom | Not disclosed | - |
| Payload/Torque | Not disclosed | - |
| Speed/Rotation | Not disclosed | - |
| Battery Life | Not disclosed | - |
| Interface/Communication | Wheeled mobility, dual-arm operation | Public description |
| Price | Not disclosed | - |

**Technical Highlights**: Wheeled dual-arm platform capable of performing tasks such as patrolling and item delivery in commercial environments, providing preliminary data and scenario validation for NEO.

**Application Scenarios**: Commercial security, logistics assistance, research.

## Supply Chain Position

- **Upstream Key Components/Materials**: NVIDIA Jetson Thor computing, tendon-driven actuators, soft materials, vision and microphone arrays.
- **Downstream Customers/Application Scenarios**: Home users, elderly care institutions, retail and security enterprises.
- **Main Competitors/Peers**: Tesla Optimus, Figure 03, Apptronik Apollo.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_one_x_technologies`
- Product/Platform Entities: `ent_product_one_x_technologies_neo`, `ent_product_one_x_technologies_eve`
- Key Relationships:
  - `rel_ent_company_one_x_technologies_manufactures_ent_product_one_x_technologies_neo` (`ent_company_one_x_technologies` → `manufactures` → `ent_product_one_x_technologies_neo`)
  - `rel_ent_company_one_x_technologies_manufactures_ent_product_one_x_technologies_eve` (`ent_company_one_x_technologies` → `manufactures` → `ent_product_one_x_technologies_eve`)

## References

1. [1X Technologies Official Website](https://www.1x.tech)
2. [HumanoidHub 1X NEO Specifications](https://www.humanoidhub.ai/robots/1x-neo)
3. [RoboZaps 1X NEO Review](https://blog.robozaps.com/b/1x-neo-review)
