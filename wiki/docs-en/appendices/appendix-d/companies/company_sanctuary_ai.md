# Sanctuary AI / Sanctuary AI

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Sanctuary AI |
| **English Name** | Sanctuary AI |
| **Headquarters** | Vancouver, British Columbia, Canada |
| **Founded** | 2018 |
| **Website** | [https://www.sanctuary.ai](https://www.sanctuary.ai) |
| **Supply Chain Role** | General-purpose humanoid robots, embodied intelligence, AI systems |
| **Enterprise Type** | Startup |
| **Parent Company/Group** | None |
| **Data Source** | Sanctuary AI official website, The Robot Report, third-party specification summaries |

## Company Profile

Sanctuary AI aims for general-purpose labor robots. The Phoenix is equipped with high-degree-of-freedom hydraulic dexterous hands and the Carbon AI cognitive system.

Phoenix emphasizes human-like bimanual tactile perception and a teleoperation data loop. Carbon AI converts natural language into physical actions. The company collaborates with manufacturing partners such as Magna International to advance pilot projects.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Phoenix Humanoid Robot | General-purpose industrial humanoid | Phoenix Gen 8 / Gen 6 | Manufacturing, retail, logistics |
| Carbon AI | Robot cognitive system | Carbon | Task learning, reasoning, human-robot interaction |

## Representative Products

### Sanctuary AI Phoenix Gen 8

> Sanctuary AI Phoenix Gen 8: Please visit [official materials](https://www.sanctuary.ai) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 170 cm (height) | Public information |
| Weight | Approx. 70 kg | Public information |
| Degrees of Freedom | 44–75 (full body, depending on configuration); 20–21×2 (hands) | Public information |
| Payload/Torque | Approx. 25 kg; fine manipulation per hand approx. 1.5 kg | Public information |
| Speed/RPM | Approx. 4.8 km/h | Public information |
| Battery Life | Approx. 4 hours | Third-party summary |
| Interfaces/Communication | Depth/RGB cameras, force/torque and tactile sensors, Carbon AI | Public information |
| Price | Not disclosed (enterprise inquiry) | - |

**Technical Highlights**: Hydraulic high-DOF hands, fingertip tactile sensitivity approx. 5 mN, Carbon AI natural language to action, rapid task learning (<24 h).

**Application Scenarios**: Automotive manufacturing, retail checkout, material handling, data collection.

### Sanctuary AI Phoenix Gen 6

> Sanctuary AI Phoenix Gen 6: Please visit [official materials](https://www.sanctuary.ai) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 170 cm (height) | The Robot Report |
| Weight | Approx. 57.9 kg | The Robot Report |
| Degrees of Freedom | 20×2 (hands); full body not disclosed | Public information |
| Payload/Torque | Approx. 20.5 kg | The Robot Report |
| Speed/RPM | Approx. 3 mph (4.8 km/h) | The Robot Report |
| Battery Life | Not disclosed | - |
| Interfaces/Communication | Carbon AI, tactile/visual perception | Public information |
| Price | Not disclosed | - |

**Technical Highlights**: First integration of legs into the Phoenix platform, validating full-body humanoid form and bimanual dexterous manipulation.

**Application Scenarios**: Early multi-industry scenario validation, data collection, and algorithm iteration.

## Supply Chain Position

- **Upstream Key Components/Materials**: Hydraulic micro-valves, tactile sensors, computing platforms, structural parts; Magna manufacturing partnership.
- **Downstream Customers/Application Scenarios**: Magna International, Canadian Tire, automotive/retail enterprises.
- **Main Competitors/Peers**: Figure AI, Tesla Optimus, Apptronik Apollo, Agility Robotics Digit.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_sanctuary_ai`
- Product/Platform Entities: `ent_product_sanctuary_ai_phoenix_gen8`, `ent_product_sanctuary_ai_phoenix_gen6`
- Key Relationships:
  - `rel_ent_company_sanctuary_ai_manufactures_ent_product_sanctuary_ai_phoenix_gen8` (`ent_company_sanctuary_ai` → `manufactures` → `ent_product_sanctuary_ai_phoenix_gen8`)
  - `rel_ent_company_sanctuary_ai_manufactures_ent_product_sanctuary_ai_phoenix_gen6` (`ent_company_sanctuary_ai` → `manufactures` → `ent_product_sanctuary_ai_phoenix_gen6`)

## References

1. [Sanctuary AI Official Website](https://www.sanctuary.ai)
2. [The Robot Report Coverage of Phoenix](https://www.therobotreport.com/sanctuary-ai-unveils-general-purpose-humanoid-robot/)
3. [RoboZaps Sanctuary AI Phoenix Review](https://blog.robozaps.com/b/sanctuary-ai-phoenix-review)
