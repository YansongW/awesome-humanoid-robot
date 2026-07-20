# Figure AI / Figure AI

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Figure AI |
| **English Name** | Figure AI |
| **Headquarters** | Sunnyvale, California, USA |
| **Founded** | 2022 |
| **Website** | [https://www.figure.ai](https://www.figure.ai) |
| **Supply Chain Role** | Humanoid Robot OEM, Embodied Intelligence |
| **Enterprise Type** | Startup |
| **Parent Company/Group** | None |
| **Data Source** | Figure AI official website, public funding and deployment reports, third-party specification compilations |

## Company Overview

Figure AI is a startup focused on general-purpose humanoid robots, primarily targeting industrial manufacturing scenarios. The Figure 02 is being piloted at BMW's Spartanburg plant.

Figure AI has developed its own Helix multimodal AI model, enabling robots to learn new tasks through natural language instructions and visual demonstrations. The Figure 02 features enhanced computing and perception capabilities, aiming to replace repetitive and hazardous manual labor.

## Product Line

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Figure 02 Humanoid Robot | Industrial Humanoid | Figure 02 | Automotive manufacturing, logistics, warehousing |
| Figure 03 Humanoid Robot | Next-Generation General/Household | Figure 03 | Industrial, future home services |

## Representative Products

### Figure 02

> Figure 02: Please visit the [official website](https://www.figure.ai) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 168 cm (height) | Public information |
| Weight | Approx. 70 kg | Public information |
| Degrees of Freedom | 28 (full body); hands not separately disclosed | Humanoid.guide, etc. |
| Payload/Torque | Lifting approx. 20–25 kg | Public information |
| Speed/Rotation | Approx. 1.2 m/s (4.32 km/h) | Public information |
| Battery Life | Approx. 5 hours | Public information |
| Interface/Communication | Dual NVIDIA GPU computing, 6× RGB cameras, voice interaction | Public information |
| Price | Not disclosed (pilot project estimated at approx. 130,000 USD) | Third-party estimate |

**Technical Highlights**: Helix multimodal AI, BMW factory deployment validation, torso-integrated battery, 6× RGB cameras and voice interaction, 3× the computing power of Figure 01.

**Application Scenarios**: Automotive assembly line kitting, material handling, warehouse sorting.

### Figure 03

> Figure 03: Please visit the [official website](https://www.figure.ai) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 170 cm (height) | Public reports |
| Weight | Approx. 60–70 kg | Public reports |
| Degrees of Freedom | 40+; hands 16×2 | Public reports |
| Payload/Torque | Approx. 25 kg | Public reports |
| Speed/Rotation | Approx. 1.2 m/s | Public reports |
| Battery Life | Approx. 5+ hours (2.25 kWh) | Public reports |
| Interface/Communication | Helix VLA model, voice interaction | Public reports |
| Price | Not disclosed | - |

**Technical Highlights**: Higher degrees of freedom in hands, general-purpose design for home and industrial use, Helix VLA end-to-end reasoning.

**Application Scenarios**: Industrial manufacturing, future home assistance, retail services.

## Supply Chain Position

- **Upstream Key Components/Materials**: NVIDIA GPU computing, motors/reducers, sensors, and battery packs (purchased or customized).
- **Downstream Customers/Application Scenarios**: BMW Spartanburg plant, logistics and manufacturing enterprises.
- **Main Competitors/Peers**: Tesla Optimus, Boston Dynamics Atlas, Agility Robotics Digit, Apptronik Apollo.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_figure_ai`
- Product/Platform Entities: `ent_product_figure_ai_figure_02`, `ent_product_figure_ai_figure_03`
- Key Relationships:
  - `rel_ent_company_figure_ai_manufactures_ent_product_figure_ai_figure_02` (`ent_company_figure_ai` → `manufactures` → `ent_product_figure_ai_figure_02`)
  - `rel_ent_company_figure_ai_manufactures_ent_product_figure_ai_figure_03` (`ent_company_figure_ai` → `manufactures` → `ent_product_figure_ai_figure_03`)

## References

1. [Figure AI Official Website](https://www.figure.ai)
2. [Humanoid.guide Figure 02 Specifications](https://humanoid.guide/product/figure-02/)
3. [The Robot Report Coverage of Figure 02](https://www.therobotreport.com/figure-02-advances-humanoid-robotics-frontier)
