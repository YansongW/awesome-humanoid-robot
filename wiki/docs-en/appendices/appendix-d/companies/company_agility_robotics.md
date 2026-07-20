# Agility Robotics

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Agility Robotics |
| **English Name** | Agility Robotics |
| **Headquarters** | Salem, Oregon, USA (RoboFab location) |
| **Founded** | 2015 |
| **Website** | [https://agilityrobotics.com](https://agilityrobotics.com) |
| **Supply Chain Role** | Logistics humanoid robot OEM, RaaS |
| **Enterprise Type** | Startup |
| **Parent Company/Group** | None |
| **Data Source** | Agility Robotics official website, Digit product page, public deployment reports |

## Company Overview

Agility Robotics is a pioneer in the commercial deployment of humanoid robots. Digit has been performing real material handling tasks in warehouses for companies such as Amazon and GXO.

Digit is specifically designed for logistics scenarios, featuring reverse knee joints to optimize walking and handling efficiency. It is supported by the Agility Arc cloud platform for remote monitoring and fleet management. The company operates the RoboFab humanoid robot manufacturing facility in Salem.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Digit Humanoid Robot | Logistics & warehouse humanoid | Digit (Current Gen / Next Gen) | Warehouse sorting, material handling, truck loading/unloading |
| Agility Arc | Cloud-based robot management platform | Agility Arc | Fleet monitoring, task scheduling, data analysis |

## Representative Products

### Agility Robotics Digit (Current Gen)

> Agility Robotics Digit (Current Gen): Please visit the [official website](https://agilityrobotics.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 175 cm (height) | Public information |
| Weight | Approx. 63–65 kg | Public information |
| Degrees of Freedom | 28 total; arms/hands use custom logistics grippers | Public information |
| Payload/Torque | Approx. 16 kg | Public information |
| Speed/RPM | Approx. 5.4 km/h | Public information |
| Battery Life | Approx. 4 hours (task-dependent) | Public information |
| Interfaces/Communication | LiDAR, Intel RealSense depth cameras, IMU, Agility Arc | Official disclosure |
| Price | RaaS lease / Approx. 250,000 USD starting | Third-party quote |

**Technical Highlights**: Reverse knee joints optimize walking; designed for tote/carton handling; LiDAR + depth camera 360° perception; deployed in Amazon/GXO warehouses.

**Application Scenarios**: Warehouse material handling, truck loading/unloading, repetitive logistics tasks.

### Agility Robotics Digit (Next Gen)

> Agility Robotics Digit (Next Gen): Please visit the [official website](https://agilityrobotics.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 175 cm (height) | Public reports |
| Weight | Approx. 63.5 kg | Public reports |
| Degrees of Freedom | 30+ | Public reports |
| Payload/Torque | Approx. 22.6 kg (50 lbs) | Public reports |
| Speed/RPM | Not disclosed | - |
| Battery Life | Under improvement (specific value not disclosed) | - |
| Interfaces/Communication | Agility Arc | - |
| Price | Not disclosed | - |

**Technical Highlights**: Builds on the current Digit with increased payload and upper body dexterity, continuing to target large-scale logistics deployment.

**Application Scenarios**: High-load warehouse handling, more complex logistics tasks.

## Supply Chain Position

- **Upstream Key Components/Materials**: Intel RealSense depth cameras, motors/drives, structural components, batteries, and computing modules.
- **Downstream Customers/Application Scenarios**: Logistics and retail enterprises such as Amazon, GXO Logistics, Mercado Libre.
- **Main Competitors/Comparables**: Tesla Optimus, Apptronik Apollo, Boston Dynamics Stretch.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_agility_robotics`
- Product/Platform Entities: `ent_product_agility_robotics_digit`, `ent_product_agility_robotics_digit_next_gen`
- Key Relationships:
  - `rel_ent_company_agility_robotics_manufactures_ent_product_agility_robotics_digit` (`ent_company_agility_robotics` → `manufactures` → `ent_product_agility_robotics_digit`)
  - `rel_ent_company_agility_robotics_manufactures_ent_product_agility_robotics_digit_next_gen` (`ent_company_agility_robotics` → `manufactures` → `ent_product_agility_robotics_digit_next_gen`)

## References

1. [Agility Robotics Official Website](https://agilityrobotics.com)
2. [RoboZaps Agility Digit Review](https://blog.robozaps.com/b/agility-robotics-digit-review)
3. [Humanoid.guide Digit Specifications](https://humanoid.guide/product/digit/)
