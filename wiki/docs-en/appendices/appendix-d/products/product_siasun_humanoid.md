# SIASUN Ruike MR73A / SIASUN MR73A

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Index](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [SIASUN Robot & Automation](../companies/company_siasun.md) |
| **Product Category** | Wheeled Humanoid Robot |
| **Release Date** | July 2025 |
| **Status** | Released/Commercial |
| **Official Website/Source** | [https://www.siasun.com](https://www.siasun.com) |

## Product Overview

Warehouse/factory handling, picking, inspection, guided tours, commercial reception, and document delivery.

The SIASUN Ruike MR73A is a representative product of SIASUN Robot. It features a wheeled humanoid design, dual-arm compliant control, whole-body impedance control, autonomous positioning navigation and dynamic obstacle avoidance, and voice large model multilingual interaction. Key specifications include: overall dimensions 650×600×1700 mm; folded dimensions 650×600×1100 mm, weight <100 kg, 21 DOF (some reports mention 27 DOF; official data prevails) (degrees of freedom).

## Product Image

![SIASUN Ruike MR73A](https://www.siasun.com/uploads/article/detail/20251015167/1752127099597286.jpg)

> Image source: Product image from SIASUN official website press release.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Overall 650×600×1700 mm; Folded 650×600×1100 mm | SIASUN official website / Industry report |
| Weight | <100 kg | SIASUN official website / Industry report |
| Degrees of Freedom | 21 DOF (some reports 27 DOF; official data prevails) | SIASUN official website / Industry report |
| Payload/Torque | Dual-arm 21 DOF, supports whole-body impedance control | SIASUN official website |
| Speed/Rotation Speed | Maximum movement speed approx. 0.8 m/s | Industry report |
| Battery Life | ≥6 hours | Industry report |
| Interface/Communication | Voice large model, multilingual, AI vision, autonomous positioning navigation | SIASUN official website |
| Price | Not disclosed | Inquire for pricing |

## Supply Chain Position

- **Manufacturer**: [SIASUN Robot & Automation](../companies/company_siasun.md)
- **Core Components/Technology Source**: Self-developed BSJ series bionic humanoid integrated joint modules, controllers, servo systems, sensors; externally purchased batteries, structural parts, computing platforms.
- **Downstream Applications/Customers**: Warehouse/factory handling, picking, inspection, guided tours, commercial reception, and document delivery.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_siasun_mr73a`
- Manufacturer Entity: `ent_company_siasun`
- Key Relationships:
  - `rel_ent_company_siasun_manufactures_ent_product_siasun_mr73a` (`ent_company_siasun` → `manufactures` → `ent_product_siasun_mr73a`)
  - `ent_product_siasun_mr73a` -- `uses` --> `ent_component_siasun_bsj_joint_module`

## Application Scenarios

- **Warehouse/factory handling, picking, inspection, guided tours, commercial reception, and document delivery.**
- **Scientific Research and Education**: As a hardware platform for robot control, AI training, and embodied intelligence research.
- **Industrial Manufacturing**: Performing handling, assembly, inspection, and other tasks on flexible production lines.
- **Commercial Services**: Used for guided tours, reception, exhibitions, and brand interaction.

## Competitive Comparison

| Comparison Item | This Product | Main Competitors |
|-----------------|--------------|------------------|
| Positioning | Wheeled humanoid robot | Similar products depend on specific scenarios |
| Core Advantages | Wheeled humanoid, dual-arm compliant control, whole-body impedance control, autonomous positioning navigation and dynamic obstacle avoidance, voice large model multilingual interaction | Not disclosed |
| Price | Not disclosed | Not disclosed |

## Procurement and Deployment Recommendations

- It is recommended to confirm the latest software version, SDK support, and after-sales training through official channels.
- Scientific research and education users should prioritize evaluating secondary development interfaces, simulation platform compatibility, and community activity.
- Industrial users need to verify payload, precision, protection level, and integration interfaces based on specific processes.

## References

1. [SIASUN Duco Bionic Humanoid Robot New Product Launch](https://www.siasun.com/news-detail167.html)
2. [SIASUN Industrial Robot Product Page](https://www.siasun.com/products.html)
3. [Tencent News – SIASUN Ruike Series Report](https://view.inews.qq.com/a/20250710A0496M00)
