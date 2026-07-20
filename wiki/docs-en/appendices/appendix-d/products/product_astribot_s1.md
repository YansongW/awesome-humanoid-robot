# Astribot S1 / Astribot S1

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Astribot](../companies/company_astribot.md) |
| **Product Category** | General-purpose humanoid robot |
| **Release Date** | August 2024 |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [https://www.astribot.com](https://www.astribot.com) |

## Product Overview

Folding clothes, cooking, cleaning, calligraphy, brewing Kung Fu tea, scientific research experiments, elderly care, new retail demonstrations.

The Astribot S1 is the flagship product of Astribot. It features cable-driven actuation, ±0.1 mm repeat positioning accuracy, 100 m/s² end-effector acceleration, force-controlled safety, VR teleoperation, and a zero-code visual interface. Key specifications include: 170 cm (height) (dimensions), 80 kg (weight), 23 DOF total (7 DOF per arm × 2, 4 DOF torso, 2 DOF head, 3 DOF omnidirectional wheeled chassis) (degrees of freedom).

## Product Image

![Astribot S1](https://cdn.shopify.com/s/files/1/0659/1437/2184/files/Astribot_image_1_resized.png?v=1768350773&width=800)

> Image source: Astribot product material (third-party distributor).

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | 170 cm (height) | Astribot official website |
| Weight | 80 kg | Astribot official website |
| Degrees of Freedom | 23 DOF total (7 DOF per arm × 2, 4 DOF torso, 2 DOF head, 3 DOF omnidirectional wheeled chassis) | Astribot official website / Technical documentation |
| Payload/Torque | Rated payload 5 kg per arm at horizontal extension, peak 10 kg | Astribot official website |
| Speed/Rotation Speed | Maximum end-effector speed ≥10 m/s | Astribot official website |
| Battery Life | 4–6 hours (supports plug-in power) | Astribot official website |
| Interface/Communication | ROS 2 / Python SDK, Gigabit Ethernet, Wi-Fi | Technical documentation |
| Price | Research version approx. ¥500,000; Enterprise/Research grade approx. $96,000–$150,000 | Public reports |

## Supply Chain Position

- **Manufacturer**: [Astribot](../companies/company_astribot.md)
- **Core Components/Technology Source**: Self-developed cable-driven actuators, high-performance motors, force/torque sensors, computing platform; externally purchased cameras, LiDAR, batteries.
- **Downstream Applications/Customers**: Folding clothes, cooking, cleaning, calligraphy, brewing Kung Fu tea, scientific research experiments, elderly care, new retail demonstrations.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_astribot_s1`
- Manufacturer Entity: `ent_company_astribot`
- Key Relationships:
  - `rel_ent_company_astribot_manufactures_ent_product_astribot_s1` (`ent_company_astribot` → `manufactures` → `ent_product_astribot_s1`)
  - `ent_product_astribot_s1` -- `uses` --> `ent_component_astribot_cable_actuator`

## Application Scenarios

- **Folding clothes, cooking, cleaning, calligraphy, brewing Kung Fu tea, scientific research experiments, elderly care, new retail demonstrations.**

## Competitive Comparison

| Comparison Item | This Product | Main Competitors |
|-----------------|--------------|------------------|
| Positioning | General-purpose humanoid robot | Similar products vary by specific scenario |
| Core Advantages | Cable-driven actuation, ±0.1 mm repeat positioning accuracy, 100 m/s² end-effector acceleration, force-controlled safety, VR teleoperation and zero-code visual interface | Not disclosed |
| Price | Research version approx. ¥500,000; Enterprise/Research grade approx. $96,000–$150,000 | Not disclosed |

## Selection and Deployment Recommendations

- It is recommended to confirm the latest software version, SDK support, and after-sales training through official channels.
- Research and education users should prioritize evaluating secondary development interfaces, simulation platform compatibility, and community activity.
- Industrial users need to verify load, accuracy, protection level, and integration interfaces based on specific processes.

## References

1. [Astribot official product page](https://www.astribot.com/en/product)
2. [RobotScope – Astribot company profile](https://robotscope.net/companies/astribot/)
3. [Baidu Baike – Astribot S1](https://baike.baidu.com/item/Astribot%20S1/64813493)
