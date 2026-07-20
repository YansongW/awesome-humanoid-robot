# Unitree H1

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Index](../index-products.md)
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Unitree Robotics](../companies/company_unitree.md) |
| **Product Category** | Full-size high-dynamic humanoid robot |
| **Release Date** | 2023 |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [Unitree Official Website](https://www.unitree.com) |

## Product Overview

Unitree H1 is a full-size high-dynamic humanoid robot launched by Unitree Robotics, positioned as a platform for scientific research, embodied intelligence research, and high-dynamic motion validation. The H1 uses Unitree's self-developed M107 permanent magnet synchronous motor, with a peak torque of 360 N·m at the knee joint and a peak torque density of approximately 189 N·m/kg. It once set a running speed record of 3.3 m/s for full-size humanoid robots.

The basic version of the H1 has 4 DOF arms, with an optional H1-2 upgrade that increases arm DOF to 7 and enhances overall load capacity. The robot supports ROS2 and Unitree SDK, features Wi-Fi, Bluetooth, and hot-swappable batteries, making it suitable for university laboratories, AI research institutions, and industrial prototype validation.

## Product Image

> Unitree H1: Please visit the [official website](https://www.unitree.com) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 180 cm (height) | Public specification |
| Weight | Approx. 47 kg (H1 basic version) | Public specification |
| Degrees of Freedom (Total) | 26–27 DOF | Basic version: 26 DOF; H1-2: 27 DOF |
| Key Performance Indicators | Knee joint peak torque 360 N·m; torque density 189 N·m/kg | Public specification |
| Walking Speed | Approx. 1.5 m/s; running speed 3.3 m/s | Public specification |
| Battery Life | Approx. 1.5–2 hours (864 Wh battery) | Public specification |
| Computing Platform | Optional Intel Core / NVIDIA Jetson Orin NX | Public specification |
| Price | Approx. 90,000 USD / Approx. 650,000 RMB domestically | Dealer and media reports |

## Supply Chain Position

- **Manufacturer**: [Unitree Robotics](../companies/company_unitree.md)
- **Core Components/Technology Source**: Self-developed M107 motors and drivers, Intel RealSense / LIVOX sensors; reducers and bearings are externally sourced.
- **Downstream Applications/Customers**: Universities, research institutes, embodied intelligence research teams, industrial prototype clients.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_unitree_h1`
- Manufacturer Entity: `ent_company_unitree`
- Key Relationships:
  - `rel_ent_company_unitree_manufactures_ent_product_unitree_h1` (`ent_company_unitree` → `manufactures` → `ent_product_unitree_h1`)

## Application Scenarios

- **Bipedal Motion Research**: Universities and research institutions conduct gait planning, reinforcement learning, and dynamic balance algorithm validation.
- **Embodied Intelligence Platform**: Serves as a hardware carrier for combining large models with robot control, used for VLA/VLM deployment testing.
- **Industrial Prototype Validation**: Logistics and manufacturing enterprises use it for high-dynamic handling, obstacle crossing, and complex terrain traversal testing.

## Competitive Comparison

| Comparison Item | Unitree H1 | Unitree G1 | Tesla Optimus Gen 3 |
|-----------------|------------|------------|---------------------|
| Positioning | Full-size high-dynamic research platform | Compact development platform | General/industrial humanoid |
| Height | 180 cm | 127 cm | 173 cm |
| Price | Approx. 90,000 USD | Approx. 16,000 USD | Target 20,000–30,000 USD |
| Core Advantage | High-dynamic motion, torque density, ROS2 ecosystem | Low cost, accessibility, dexterous hand | Manufacturing scale target, dexterous hand |

## Purchase and Deployment Recommendations

- High-dynamic motion research teams are advised to opt for the H1-2 upgrade to enhance arm DOF and overall load capacity.
- Since the basic version of the H1 has limited arm DOF, projects requiring dexterous manipulation should configure additional end effectors.

## References

1. [Unitree Official Website](https://www.unitree.com)
2. [Robozaps – Unitree H1 Review](https://blog.robozaps.com/b/unitree-h1-review)
3. [OpenELAB – Unitree H1-2](https://openelab.com/products/unitree-h1-2-humanoid-robot)
4. [Appendix D.4 Key Product Wiki](../index-products.md)
