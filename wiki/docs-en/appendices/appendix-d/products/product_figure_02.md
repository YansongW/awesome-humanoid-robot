# Figure 02

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Figure AI](../companies/company_figure_ai.md) |
| **Product Category** | General-purpose humanoid robot |
| **Release Date** | August 2024 |
| **Status** | Enterprise pilot / Limited deployment |
| **Official Website/Source** | [Figure AI Official Website](https://www.figure.ai) |

## Product Overview

Figure 02 is the second-generation general-purpose humanoid robot launched by Figure AI, designed for industrial manufacturing and logistics scenarios. The entire machine features a matte black appearance and an integrated cable layout, equipped with Figure's self-developed Helix VLA (Vision-Language-Action) AI model, capable of controlling the upper body at a frequency of 200 Hz, enabling zero-shot grasping of thousands of unseen objects.

Figure 02 has been validated in real-world tasks at automotive manufacturing bases such as BMW Spartanburg, primarily responsible for collaborative processes with humans, including chassis assembly and material handling. Its dual NVIDIA RTX GPU computing modules provide approximately 3 times the on-device inference capability of Figure 01, while 6 RGB cameras and multimodal sensors support 24/7 environmental perception.

## Product Image

> Figure 02: Please visit the [official materials](https://www.figure.ai) for viewing.

## Specification Table

| Specification Item | Value | Notes/Source |
|-------------------|-------|--------------|
| Dimensions | Approx. 168 cm (height) | Public specification |
| Weight | Approx. 70 kg | Public specification |
| Degrees of Freedom (Total) | 28 DOF (Hands: 16 DOF/pair) | Public specification |
| Key Performance Indicators | Hand payload 25 kg; Total robot payload 20 kg | Public specification |
| Walking Speed | Approx. 1.2 m/s | Public specification |
| Battery Life | Approx. 5 hours | Public specification |
| Battery Capacity | 2.25 kWh (integrated in torso) | Public specification |
| Computing Platform | Dual NVIDIA RTX GPU modules | Figure AI |
| Price | Not disclosed (Industry estimate approx. 130,000 USD) | Third-party estimate |

## Supply Chain Position

- **Manufacturer**: [Figure AI](../companies/company_figure_ai.md)
- **Core Components/Technology Sources**: NVIDIA GPU computing modules, self-developed Helix VLA model, OpenAI voice interaction, 6×RGB cameras and depth perception modules.
- **Downstream Applications/Customers**: BMW manufacturing bases, logistics warehousing, automotive assembly lines.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_figure_ai_figure_02`
- Manufacturer Entity: `ent_company_figure_ai`
- Key Relationships:
  - `rel_ent_company_figure_ai_manufactures_ent_product_figure_ai_figure_02` (`ent_company_figure_ai` → `manufactures` → `ent_product_figure_ai_figure_02`)

## Application Scenarios

- **Automotive Manufacturing**: Executes chassis assembly, wire harness installation, and material handling at bases like BMW Spartanburg.
- **Warehousing and Logistics**: Sorting, handling, and production line replenishment of standardized boxes.
- **Industrial Collaboration**: Works alongside human workers to complete assembly and inspection tasks requiring dexterous hands.

## Competitive Comparison

| Comparison Item | Figure 02 | Tesla Optimus Gen 3 | Agility Digit |
|----------------|-----------|---------------------|---------------|
| Positioning | Industrial manufacturing humanoid | General/Industrial humanoid | Logistics warehousing humanoid |
| AI Architecture | Helix VLA | FSD-derived neural network | Proprietary perception/planning stack |
| Battery Life | Approx. 5 h | Approx. 2–4 h (estimated) | Approx. 4 h |
| Core Advantage | On-device VLA, BMW deployment, hand payload | Manufacturing scale target, cost control | Logistics deployment maturity |

## Selection and Deployment Recommendations

- Figure 02 is currently primarily for enterprise pilots. It is recommended to contact Figure AI directly to assess the feasibility of factory scenarios.
- Before deployment, confirm the generalization capability of the Helix VLA model for target workpieces and plan the training data collection process.

## References

1. [Figure AI Official Website](https://www.figure.ai)
2. [Robozaps – Figure 02 Review](https://blog.robozaps.com/b/figure-02-review)
3. [Humanoid.Guide – Figure 02](https://humanoid.guide/product/figure-02/)
4. [The Robot Report – Figure BMW Deployment](https://www.therobotreport.com)
