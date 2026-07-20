# Dobot X-Trainer

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Table of Contents](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Yuejiang Technology / Dobot](../companies/company_dobot.md) |
| **Product Category** | Dual-arm Teleoperation AI Training Platform |
| **Release Date** | 2024 |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [https://www.dobot.cn](https://www.dobot.cn) |

## Product Overview

Embodied intelligence data collection, imitation learning, scientific research and education, AGI scenario simulation and competition.

The Dobot X-Trainer is a representative product of Yuejiang Technology. It features industrial-grade Nova 2 collaborative arms as slave hands, ±0.05 mm repeat positioning accuracy, 25 Hz end-to-end motion interface, VR/controller teleoperation, and data collection SDK. Main specifications include: base 1400×1000 mm (lightweight version, excluding handles) (dimensions), Not disclosed (weight), master hand 6-DOF×2, slave hand Nova 2 collaborative arm×2 (degrees of freedom).

## Product Image

![Dobot X-Trainer](https://www.dobot-robots.com/media/upload/2024/x-trainer/tab.png)

> Image source: Dobot official website product image.

## Specification Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Dimensions | Base 1400×1000 mm (lightweight version, excluding handles) | Dobot X-Trainer User Manual |
| Weight | Not disclosed | - |
| Degrees of Freedom | Master hand 6-DOF×2, slave hand Nova 2 collaborative arm×2 | User Manual |
| Payload/Torque | Single arm can carry 2 kg, dual arms 3 kg; gripper max stroke 95 mm | Brochure |
| Speed/Rotation Speed | End-effector max speed 1.6 m/s | Brochure |
| Battery Life | Mains powered | - |
| Interface/Communication | Gigabit Ethernet, USB, WiFi (Nova 2 optional) | User Manual |
| Price | Not disclosed | Inquire for pricing |

## Supply Chain Position

- **Manufacturer**: [Yuejiang Technology / Dobot](../companies/company_dobot.md)
- **Core Components/Technology Source**: Self-developed collaborative robot joints, motors, reducers, controllers; Intel RealSense D405 depth camera; NVIDIA Jetson computing platform.
- **Downstream Applications/Customers**: Embodied intelligence data collection, imitation learning, scientific research and education, AGI scenario simulation and competition.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_dobot_x_trainer`
- Manufacturer Entity: `ent_company_dobot`
- Key Relationships:
  - `rel_ent_company_dobot_manufactures_ent_product_dobot_x_trainer` (`ent_company_dobot` → `manufactures` → `ent_product_dobot_x_trainer`)
  - `ent_product_dobot_x_trainer` -- `uses` --> `ent_component_dobot_nova2`

## Application Scenarios

- **Embodied intelligence data collection, imitation learning, scientific research and education, AGI scenario simulation and competition.**

## Competitive Comparison

| Comparison Item | This Product | Main Competitors |
|----------------|--------------|------------------|
| Positioning | Dual-arm Teleoperation AI Training Platform | Similar products depend on specific scenarios |
| Core Advantages | Industrial-grade Nova 2 collaborative arm slave hands, ±0.05 mm repeat positioning accuracy, 25 Hz end-to-end motion interface, VR/controller teleoperation, data collection SDK | Not disclosed |
| Price | Not disclosed | Not disclosed |

## Selection and Deployment Recommendations

- It is recommended to confirm the latest software version, SDK support, and after-sales training through official channels.
- Research and education users should prioritize evaluating secondary development interfaces, simulation platform compatibility, and community activity.
- Industrial users need to verify load, accuracy, protection level, and integration interfaces based on specific processes.

## References

1. [Dobot X-Trainer Product Page](https://www.dobot-robots.com/products/humanoid-robots/x-trainer.html)
2. [Dobot X-Trainer Brochure](https://www.roscomponents.com/wp-content/uploads/2026/02/X-Trainer-leaflet-Lightweight-Base_Brochure.pdf)
3. [Yuejiang Technology Official Website](https://www.dobot.cn)
