# Tesla, Inc.

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 特斯拉 |
| **English Name** | Tesla, Inc. |
| **Headquarters** | Austin, Texas, USA |
| **Founded** | 2003 |
| **Website** | [https://www.tesla.com](https://www.tesla.com) |
| **Supply Chain Role** | Vehicle/OEM, Humanoid Robot OEM, Core Component In-house R&D |
| **Enterprise Type** | Public Company (NASDAQ: TSLA) |
| **Parent Company/Group** | None (Tesla, Inc. is the listed entity) |
| **Data Source** | Tesla Official Website, AI Day Public Demonstrations, Third-party Technical Compilations |

## Company Overview

Tesla is a globally renowned electric vehicle and clean energy company. Through the Optimus humanoid robot, it is extending its vertically integrated manufacturing and AI capabilities into the field of general-purpose robotics.

The Tesla Bot (later named Optimus) was first unveiled at Tesla AI Day 2021, with the goal of initially deploying it within Tesla factories, then gradually targeting enterprise and consumer markets. Optimus leverages Tesla's in-house actuators, battery packs, FSD visual perception, and vehicle-grade computing platforms, emphasizing scalable manufacturing and cost control.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Optimus Humanoid Robot | General-purpose/Industrial Humanoid | Optimus Gen 2 / Gen 1 | Factory handling, sorting, future home services |
| Autonomous Driving & Robot AI | Perception/Decision Software Stack | FSD / Dojo | Vehicle autonomous driving, robot task planning |

## Representative Products

### Tesla Optimus Gen 2

> Tesla Optimus Gen 2: Please visit [Official Information](https://www.tesla.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 173 cm (height) | Tesla AI Day / Public Information |
| Weight | Approx. 57 kg | Tesla Official Disclosure |
| Degrees of Freedom | Torso 28+; Hands 11×2 (Gen 2), Gen 3 hands upgraded to 22×2 | Public Information |
| Payload/Torque | Two-hand carry approx. 20 kg | Public Demonstration |
| Speed/Rotation | Walking max approx. 8 km/h | Third-party Review |
| Battery Life | Approx. 2–4 hours (task-dependent) | Not officially confirmed |
| Interface/Communication | Proprietary interface, FSD computing platform | Official Disclosure |
| Price | Target retail price 20,000–30,000 USD | Musk's Public Statement |

**Technical Highlights**: Lightweight body, Tesla in-house linear/rotary actuators, torso-integrated battery, FSD-derived neural network, human-like hands with tactile feedback.

**Application Scenarios**: Battery/material sorting in automotive factories, general industrial handling, future home and personal services.

### Tesla Optimus Gen 1

> Tesla Optimus Gen 1: Please visit [Official Information](https://www.tesla.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 173 cm (height) | Tesla AI Day 2022 |
| Weight | Approx. 73 kg | Public Information |
| Degrees of Freedom | Torso approx. 28; Hands 11×2 | Public Information |
| Payload/Torque | Two-hand carry approx. 20 kg; Deadlift approx. 68 kg | Public Demonstration |
| Speed/Rotation | Walking < 2 km/h | Prototype Demonstration |
| Battery Life | Not disclosed | - |
| Interface/Communication | Proprietary interface | - |
| Price | Not disclosed | - |

**Technical Highlights**: First-generation public prototype, validating electric drive joints, basic bipedal walking, and torso-integrated computing architecture.

**Application Scenarios**: Laboratory validation, public demonstrations, and foundation for subsequent iterations.

## Supply Chain Position

- **Upstream Key Components/Materials**: In-house actuators, battery cells and power management, vision sensors, computing chips; some structural parts and raw materials outsourced.
- **Downstream Customers/Application Scenarios**: Tesla's own factories, potential future automotive/logistics companies, and consumer market.
- **Main Competitors/Peers**: Figure AI, Boston Dynamics, Apptronik, 1X Technologies, Agility Robotics.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_tesla`
- Product/Platform Entities: `ent_product_tesla_optimus_gen2`, `ent_product_tesla_optimus_gen1`
- Key Relationships:
  - `rel_ent_company_tesla_manufactures_ent_product_tesla_optimus_gen2` (`ent_company_tesla` → `manufactures` → `ent_product_tesla_optimus_gen2`)
  - `rel_ent_company_tesla_manufactures_ent_product_tesla_optimus_gen1` (`ent_company_tesla` → `manufactures` → `ent_product_tesla_optimus_gen1`)

## References

1. [Tesla Official Website](https://www.tesla.com)
2. [Tesla AI Day 2022 Public Demonstration](https://www.tesla.com/AI)
3. [Robohuman Tesla Optimus Specification Summary](https://robohuman.org/product/tesla-optimus)
