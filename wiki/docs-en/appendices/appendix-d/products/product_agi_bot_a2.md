# Zhiyuan Expedition A2 / AgiBot Expedition A2

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Zhiyuan Robot / AgiBot](../companies/company_agi_bot.md) |
| **Product Category** | General-purpose Humanoid Robot |
| **Release Date** | August 2024 |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [Zhiyuan Robot Official Website](https://www.zhiyuan-robot.com) |

## Product Overview

The Zhiyuan Expedition A2 is a full-size humanoid robot launched by Zhiyuan Robot for interactive services, automotive manufacturing, and 3C electronics scenarios. The A2 adopts human factors engineering design, supports 40+ full-body degrees of freedom, and is equipped with 360° LiDAR, 6 high-definition cameras, and PowerFlow quasi-direct drive joint modules, with a single-leg peak torque exceeding 350 N·m.

The Expedition A2 emphasizes a "brain-cerebellum-body" three-level embodied intelligence architecture. The self-developed EI-Brain framework and SkillHand dexterous hand (12 active + 5 passive DOF) support precision assembly and material handling. In 2025, the A2 became the world's first humanoid robot to simultaneously pass China's CR, the EU's CE-MD/CE-RED, and the US FCC certifications, and completed a long-duration autonomous walking challenge in a high-temperature environment.

## Product Image

> AgiBot Expedition A2: Please visit the [official website](https://www.zhiyuan-robot.com) for details.

## Specification Table

| Specification Item | Value | Notes/Source |
|-------------------|-------|--------------|
| Dimensions | Approx. 169–175 cm (height) | Differences between flagship version/official website parameters |
| Weight | Approx. 55–69 kg | Configuration differences between flagship/youth version |
| Degrees of Freedom (Whole Body) | 40+ DOF; official website states 49+ | Public specifications |
| Key Performance Indicators | Single arm max load 5 kg; joint peak torque 350 N·m | Official website parameters |
| Walking Speed | Approx. 7 km/h (approx. 1.94 m/s) | Official website parameters |
| Battery Life | Approx. 2 hours (700 Wh battery) | Public specifications |
| AI Computing Power | 200 TOPS | Official website parameters |
| Price | Not disclosed (listed on JD.com/Zhiyuan Mall in China) | Official channels |

## Supply Chain Position

- **Manufacturer**: [Zhiyuan Robot / AgiBot](../companies/company_agi_bot.md)
- **Core Components/Technology Sources**: Self-developed PowerFlow joint modules, SkillHand dexterous hand, embodied intelligence brain EI-Brain, NVIDIA Jetson AGX Orin (some configurations), LiDAR and vision sensors.
- **Downstream Applications/Customers**: Automotive OEMs, 3C electronics, supermarket navigation, exhibition hall explanation, scientific research and education.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_agi_bot_a2`
- Manufacturer Entity: `ent_company_agi_bot`
- Key Relationships:
  - `rel_ent_company_agi_bot_manufactures_ent_product_agi_bot_a2` (`ent_company_agi_bot` → `manufactures` → `ent_product_agi_bot_a2`)

## Application Scenarios

- **Automotive Manufacturing**: Appearance inspection on automotive production lines, interior assembly verification, seat belt installation inspection, and screw tightening.
- **3C Electronics**: Semiconductor loading/unloading, precision assembly, and auxiliary operations for new energy battery PACK lines.
- **Interactive Services**: Exhibition hall explanation, supermarket navigation, marketing customer service, and auto show sales consultant.

## Competitive Comparison

| Comparison Item | Zhiyuan Expedition A2 | Ubtech Walker S2 | Tesla Optimus Gen 3 |
|-----------------|-----------------------|------------------|---------------------|
| Positioning | General-purpose/Service Humanoid | Industrial Humanoid | General-purpose/Industrial Humanoid |
| Whole Body DOF | 40+ (Official website 49+) | 52 | 28+ Torso + 22×2 Hands |
| Certifications | CR / CE-MD / CE-RED / FCC | Not disclosed | Not disclosed |
| Core Advantages | Full-stack self-developed, multi-country certification, interaction capability | Factory deployment, hot-swappable battery | Manufacturing scale target, FSD vision |

## Selection and Deployment Recommendations

- It is recommended to check stock configurations, delivery cycles, and after-sales policies via the Zhiyuan official mall or JD.com flagship store.
- Before industrial scenario deployment, complete CR/CE certification document verification, on-site safety assessment, and operator training.

## References

1. [Zhiyuan Robot Official Website](https://www.zhiyuan-robot.com)
2. [Zhiyuan Expedition A2 Product Page](https://www.agibot.com/product/169/detail/4.html)
3. [IT Home – Zhiyuan Expedition A2 Cross-Province Walking](https://www.ithome.com/0/898/193.htm)
4. [EEFocus – Zhiyuan Expedition A2 Motion Control](https://www.eefocus.com/article/1952915.html)
