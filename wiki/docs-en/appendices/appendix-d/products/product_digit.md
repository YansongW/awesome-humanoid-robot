# Agility Robotics Digit

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Agility Robotics](../companies/company_agility_robotics.md) |
| **Product Category** | Logistics/Warehouse Humanoid Robot |
| **Release Date** | First released in 2019; current version is a mass-produced iterative model |
| **Status** | Mass production/Commercial deployment |
| **Official Website/Source** | [Agility Robotics Official Website](https://agilityrobotics.com/) |

## Product Overview

The Agility Robotics Digit is one of the most widely deployed humanoid robots in the warehousing and logistics sector. It features an integrated head-torso design and reverse knee joints, optimized for moving totes in human-built environments such as narrow aisles, stairs, and ramps. Digit's perception system includes 4 Intel RealSense depth cameras, LiDAR, IMU, and force sensors, enabling autonomous navigation without external infrastructure.

Agility operates the RoboFab humanoid robot factory in Salem, Oregon, USA, with a designed annual production capacity of 10,000 units. Digit performs sorting and handling tasks in warehouses for customers such as Amazon, GXO, and Spanx, and is offered to enterprise clients through a Robot-as-a-Service (RaaS) model, lowering the initial procurement barrier.

## Product Image

> Agility Robotics Digit: Please visit the [official website](https://agilityrobotics.com/) for images.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 175 cm (height) | Public specification |
| Weight | Approx. 63.5–65 kg | Public specification |
| Degrees of Freedom (Total) | 16–28 DOF (varies by source) | Public specification |
| Key Performance Indicators | Payload 16 kg; continuous handling 35 lb | Official specification |
| Walking Speed | Approx. 5.4 km/h | Public specification |
| Battery Life | Approx. 4 hours (typical task) | Official specification |
| Charging | Autonomous docking charging | Agility Robotics |
| Price | Not disclosed (industry estimate approx. 250,000 USD or RaaS) | Third-party estimate |

## Supply Chain Position

- **Manufacturer**: [Agility Robotics](../companies/company_agility_robotics.md)
- **Core Components/Technology Sources**: Intel RealSense depth cameras, LiDAR, custom electric drive actuators, Agility Arc cloud fleet management platform.
- **Downstream Applications/Customers**: Warehousing and manufacturing clients such as Amazon, GXO, Spanx, Toyota Canada.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_agility_robotics_digit`
- Manufacturer Entity: `ent_company_agility_robotics`
- Key Relationship:
  - `rel_ent_company_agility_robotics_manufactures_ent_product_agility_robotics_digit` (`ent_company_agility_robotics` → `manufactures` → `ent_product_agility_robotics_digit`)

## Application Scenarios

- **E-commerce Warehousing**: Tote handling and sorting in warehouses for Amazon, GXO, etc.
- **Retail Distribution**: Restocking from shelves to conveyors, return sorting, and inventory relocation.
- **Manufacturing Logistics**: Parts distribution and line-side replenishment in automotive and consumer goods factories.

## Competitive Comparison

| Comparison Item | Agility Digit | Tesla Optimus Gen 3 | Figure 02 |
|-----------------|---------------|---------------------|-----------|
| Positioning | Logistics/Warehouse Humanoid | General/Industrial Humanoid | Industrial Manufacturing Humanoid |
| Hands | Custom end-effector | 22×2 Dexterous Hand | 16 DOF Dexterous Hand |
| Business Model | RaaS / Enterprise Deployment | Target Retail | Enterprise Pilot |
| Core Advantages | Deployment scale, battery life, RoboFab capacity | Cost and manufacturing scale targets | AI models and dexterous manipulation |

## Selection and Deployment Recommendations

- Enterprise clients can evaluate RaaS or procurement options through the Agility Robotics business team, typically requiring an on-site warehouse survey.
- Before deployment, confirm tote specifications, floor conditions, Wi-Fi coverage, and data interfaces with the WMS.

## References

1. [Agility Robotics Official Website](https://agilityrobotics.com/)
2. [Robozaps – Agility Robotics Digit Review](https://blog.robozaps.com/b/agility-robotics-digit-review)
3. [Humanoid.Guide – Digit](https://humanoid.guide/product/digit/)
4. [The Robot Report – Agility Digit Deployments](https://www.therobotreport.com)
