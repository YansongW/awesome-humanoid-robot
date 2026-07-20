# SRT SFG Soft Gripper

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Soft Robot Tech / SRT](../companies/company_srt.md) |
| **Product Category** | Pneumatic Soft Gripper / Soft Robot End Effector |
| **Release Date** | Continuous iteration since 2018 |
| **Status** | Mass Production / Commercial |
| **Website/Source** | [SRT Official Website](https://www.softrobottech.com) |

## Product Overview

The SRT SFG Soft Gripper is an adaptive pneumatic end effector based on soft robot technology. Unlike traditional rigid grippers, the SFG's fingers are made of food-grade silicone with a biomimetic air chamber structure: applying positive pressure causes the fingers to bend and adaptively envelop the target object; applying negative pressure causes the fingers to open and release the object. Due to its soft and deformable nature, the SFG can grasp objects of different sizes, shapes, hardnesses, and surface characteristics with the same gripper, making it particularly suitable for flexible, irregularly shaped, and fragile items that are difficult for traditional grippers to handle.

The SFG series has evolved into multiple structural forms, including the compact type (FTN), symmetrical adjustable type (FMA), and circumferential type (FNC). Finger modules and mounting brackets can be customized according to customer requirements, and the gripper is compatible with mainstream robots such as UR, ABB, and SIASUN.

## Product Image

> SRT SFG Gripper: Please visit the [official website](https://www.softrobottech.com) for details.

## Specification Parameter Table

| Specification Item | Value | Remarks/Source |
|--------------------|-------|----------------|
| Drive Method | Pneumatic (positive pressure grasp / negative pressure release) | Product Manual |
| Finger Material | Food-grade silicone | Product Manual |
| Finger Structure | Biomimetic air chamber / soft structure | Product Manual |
| Operating Temperature | -40 °C – 150 °C | Product Manual |
| Operating Pressure | -100 – 100 kPa | Product Manual |
| Service Life | >3 million cycles | Product Manual |
| Repeat Positioning Accuracy | 0.08 mm | Product Manual |
| Operating Frequency | ≤110 CPM | Product Manual |
| Load Range | 100 g – 7 kg (varies by model) | DirectIndustry |
| Gripper Weight | 38 g – 1090 g (varies by model) | DirectIndustry |
| Applicable Workpiece Size | Varies by model, can cover multiple SKUs | Product Manual |
| Drive Medium | Clean air | Product Manual |
| Mounting Interface | Compatible with ISO 9409-1:2004 / GB/T 14468.1 | Product Manual |
| Compatible Controller | SCB series pneumatic controller | Product Manual |
| Certifications | CE, RoHS, FDA, LFGB, JFSL370, etc. | Official website public information |
| Communication Interface | Pneumatic controller + Robot I/O | Product Manual |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Soft Robot Tech / SRT](../companies/company_srt.md)
- **Core Components/Technology Source**: Self-developed silicone material formulation, soft structure design and molding process; pneumatic components, controllers, and 3D vision modules are purchased externally.
- **Downstream Applications/Customers**: Food & fresh produce, 3C electronics, automotive parts, medical & daily chemical, logistics & warehousing, collaborative robot integrators.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_srt_soft_gripper`
- Manufacturer Entity: `ent_company_srt`
- Component Entity: `ent_component_srt_flexible_finger`
- Key Relationships:
  - `rel_ent_company_srt_manufactures_ent_product_srt_soft_gripper` (`ent_company_srt` → `manufactures` --> `ent_product_srt_soft_gripper`)
  - `rel_ent_company_srt_manufactures_ent_component_srt_flexible_finger` (`ent_company_srt` → `manufactures` --> `ent_component_srt_flexible_finger`)
  - `rel_ent_product_srt_soft_gripper_uses_ent_component_srt_flexible_finger` (`ent_product_srt_soft_gripper` → `uses` --> `ent_component_srt_flexible_finger`)

## Application Scenarios

- **Food & Fresh Produce**: Sorting and packaging of meat, fruits & vegetables, baked goods, seafood, and prepared foods.
- **3C Electronics**: Non-destructive loading/unloading of phone frames, circuit boards, and irregular electronic components.
- **Automotive Parts**: Assembly of rubber parts, wire harnesses, and irregular injection-molded parts.
- **Medical & Daily Chemical**: Ampoules, syringes, medical devices, and cosmetic packaging.
- **Logistics & Warehousing**: Mixed SKU sorting of irregular, soft, and fragile items.

## Competitive Comparison

| Comparison Item | SRT SFG | OnRobot Soft Gripper | Soft Robotics Inc. mGrip |
|-----------------|---------|----------------------|--------------------------|
| Drive Method | Pneumatic | Electric/Pneumatic | Pneumatic |
| Finger Material | Food-grade silicone | Flexible material | Flexible material |
| Operating Temperature | -40 °C – 150 °C | Varies by model | Varies by model |
| Service Life | >3 million cycles | Varies by model | Varies by model |
| Core Advantage | Food-grade certification, multiple series, many global customers | Plug-and-play ecosystem | Modular, easy integration |

## Selection and Deployment Recommendations

- Select the corresponding series (FTN/FMA/FNC, etc.) and finger modules based on workpiece weight, size, and shape.
- Requires a compatible clean air source and SRT pneumatic controller to ensure pressure and cycle time match.
- For direct food contact scenarios, it is recommended to choose the SFG-N food-grade certified model.

## References

1. [SRT Soft Robot Official Website](https://www.softrobottech.com)
2. [SRT Shopify International Site](https://softrobotgripper.com)
3. [Asian Robotics Review – SRT Report](https://asianroboticsreview.com/home620-html)
4. [DirectIndustry – SFG Series Product Parameters](https://www.directindustry.com/prod/soft-robot-tech-co-ltd/product-244815-2538729.html)
5. [Appendix D Company Directory](../index-companies.md)
