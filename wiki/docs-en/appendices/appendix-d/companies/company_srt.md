# Soft Robot Technology (SRT)

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 软体机器人科技 |
| **English Name** | Soft Robot Technology (SRT) |
| **Headquarters** | Beijing, China |
| **Founded** | 2016 |
| **Website** | [https://www.softrobottech.com](https://www.softrobottech.com) |
| **Supply Chain Role** | Soft robot end effectors, flexible grippers, intelligent manufacturing solutions |
| **Enterprise Type** | Private enterprise, National High-tech Enterprise, Zhongguancun High-tech Enterprise |
| **Parent Company/Group** | Independent operation |
| **Data Source** | SRT official website, CIIF reports, Asian Robotics Review, DirectIndustry |

## Company Profile

Soft Robot Technology (SRT) is a world-leading supplier of soft robot technology and flexible end effectors. Its core R&D team comes from Harvard University, Northeastern University, the Chinese Academy of Sciences, Beihang University, and other institutions. The company focuses on structural design, material formulation, molding processes, and pneumatic control technology for flexible materials such as silicone, solving 96% of industrial automation handling challenges for flexible, irregularly shaped, and fragile items.

SRT owns 9 major series and over 200 products, including SFG flexible grippers, ISC internal gripping fixtures, OSC external gripping fixtures, MVG micro vacuum suction cups, NBM flexible air bladders, and IEG intelligent electric grippers. It has served more than 500 leading industry clients in over 30 countries, covering sectors such as food & fresh produce, 3C electronics, automotive parts, medical & daily chemicals, and logistics & warehousing.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Flexible Grippers | Adaptive enveloping grasping | SFG Series | Food, 3C, Logistics, Automotive |
| Internal/External Gripping Fixtures | Positioning and clamping irregular workpieces | ISC / OSC Series | Industrial assembly, Packaging |
| Micro Vacuum Suction Cups | Grasping thin/smooth surfaces | MVG Series | Electronics, Semiconductors |
| Intelligent Electric Grippers | Electrified flexible end effectors | IEG Series | Collaborative robots, Precision assembly |
| Pneumatic Control Modules | Gripper drive and control | SCB Series | Flexible grasping systems |

## Representative Products

### SRT SFG Flexible Gripper

> SRT SFG Gripper: Please visit [official materials](https://www.softrobottech.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Drive Method | Pneumatic (positive pressure grasp / negative pressure release) | Official website/dealer materials |
| Finger Material | Food-grade silicone | Official website/dealer materials |
| Operating Temperature | -40 °C – 150 °C | Product manual |
| Operating Pressure | -100 – 100 kPa | Product manual |
| Service Life | >3 million cycles | Product manual |
| Repeat Positioning Accuracy | 0.08 mm | Product manual |
| Operating Frequency | ≤110 CPM (approx. 300 cycles/min) | Product manual |
| Load Range | 100 g – 7 kg (varies by model) | DirectIndustry |
| Gripper Weight | 38 g – 1090 g (varies by model) | DirectIndustry |
| Applicable Workpieces | Irregular, fragile, soft, non-uniform objects | Official website public info |
| Certifications | CE, RoHS, FDA, LFGB, JFSL370, etc. | Official website public info |
| Communication Interface | Pneumatic controller + Robot I/O | Product manual |
| Price | Not disclosed | - |

**Technical Highlights**: A bionic soft structure mimicking starfish arms, achieving adaptive enveloping grasping through pneumatics. It can handle multi-SKU flexible production without changing grippers based on workpiece size.

**Application Scenarios**: Fresh meat/fruit & vegetable sorting, baked food packaging, 3C electronics assembly, medical consumables, automotive parts loading/unloading, logistics & warehousing.

### SRT SFG-N Series Food-Grade Flexible Gripper

> SRT SFG-N: Please visit [official materials](https://www.softrobottech.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Material | Food-grade silicone, can directly contact food | Public reports |
| Certifications | US FDA, Japan JFSL370, EU AP / LFGB | Public reports |
| Operating Temperature | -40 °C – 150 °C | Product manual |
| Features | Washable, acid/alkali resistant, antibacterial and anti-contamination | Public reports |
| Price | Not disclosed | - |

**Technical Highlights**: Designed specifically for the food industry, it can directly contact fresh produce, baked goods, etc., meeting multiple national food contact material certifications and supporting harsh environments such as humidity and low temperatures.

**Application Scenarios**: Meat sorting, fruit & vegetable packaging, baking tray loading, prepared food processing, central kitchen automation.

## Supply Chain Position

- **Upstream Key Components/Materials**: Food-grade silicone, pneumatic components, pneumatic controllers, 3D vision modules, industrial robot bodies
- **Downstream Customers/Application Scenarios**: Food & fresh produce, 3C electronics, automotive parts, medical & daily chemicals, logistics & warehousing, collaborative robot OEMs
- **Main Competitors/Peers**: OnRobot, Soft Robotics Inc. (USA), Schmalz, Robotiq

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_srt`
- Product Entity: `ent_product_srt_soft_gripper`
- Component Entity: `ent_component_srt_flexible_finger`
- Key Relationships:
  - `ent_company_srt` -- `manufactures` --> `ent_product_srt_soft_gripper`
  - `ent_company_srt` -- `manufactures` --> `ent_component_srt_flexible_finger`
  - `ent_product_srt_soft_gripper` -- `uses` --> `ent_component_srt_flexible_finger`

## References

1. [SRT Soft Robot Official Website](https://www.softrobottech.com)
2. [SRT Shopify International Site](https://softrobotgripper.com)
3. [Asian Robotics Review – SRT Report](https://asianroboticsreview.com/home620-html)
4. [DirectIndustry – SFG Series Product Parameters](https://www.directindustry.com/prod/soft-robot-tech-co-ltd/product-244815-2538729.html)
5. [Appendix D Product Catalog](../index-products.md)
