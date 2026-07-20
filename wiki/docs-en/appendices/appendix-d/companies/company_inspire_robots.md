# Inspire Robots

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).  
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 因时机器人 |
| **English Name** | Inspire Robots |
| **Headquarters** | Beijing, China |
| **Founded** | 2016 |
| **Website** | [https://www.inspiterobots.com](https://www.inspiterobots.com) |
| **Supply Chain Role** | Dexterous Hands / Micro Linear Actuators / Joint Modules |
| **Company Type** | Domestic Startup, High-Tech Enterprise |
| **Parent Company/Group** | Beijing Inspire Robots Technology Co., Ltd. |
| **Data Source** | Official website, product manuals, public reports, WAIC 2026 coverage |

## Company Overview

A leading domestic supplier of dexterous hands and micro servo joints for humanoid robots, focusing on high-degree-of-freedom end effectors.

Inspire Robots specializes in micro servo electric cylinders, dexterous hands, and integrated joint modules, characterized by high integration, small size, and high torque density. Its RH series dexterous hands have been applied in multiple humanoid robots, prosthetics, and research platforms, supporting independent multi-degree-of-freedom control and tactile sensing expansion.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Dexterous Hands | Multi-DOF End Effectors | RH56DFX, RH56BFX | Humanoid Robots, Prosthetics |
| Micro Servo Electric Cylinders | Integrated Linear Actuators | LA Series | Robot Joints, Precision Gripping |
| Rotary Joint Modules | Integrated Rotary Actuators | RJ Series | Collaborative Robots, Humanoid Robots |

## Representative Products

### RH56DFX Series Dexterous Hand / Inspire RH56DFX Dexterous Hand

> RH56DFX Series Dexterous Hand: Please visit [Official Documentation](https://www.inspiterobots.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 230×85×35 mm (palm) | Product Manual |
| Weight | Approx. 480 g | Product Manual |
| Degrees of Freedom | 6 Active + 6 Passive / 11 Active (optional) | Product Manual |
| Payload | 1.5 kg per finger (fingertip) | Product Manual |
| Motion Speed | Joint 180°/s | Product Manual |
| Supply Voltage | DC 24 V | Product Manual |
| Communication Interface | CAN / RS485 | Product Manual |
| Price | Not disclosed | - |

**Technical Highlights**: High DOF, integrated micro drive units, expandable tactile and force control, suitable for fine manipulation by humanoid robots.

**Application Scenarios**: Humanoid robot manipulation, prosthetics, service robot grasping, industrial quality inspection.

### Micro Servo Electric Cylinder / Inspire Micro Linear Actuator

> Micro Servo Electric Cylinder: Please visit [Official Documentation](https://www.inspiterobots.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Ø8–Ø16 mm (series range) | Product Manual |
| Weight | 10–50 g | Product Manual |
| Stroke | 10–100 mm | Product Manual |
| Push/Pull Force | 30–500 N | Product Manual |
| Maximum Speed | 100 mm/s | Product Manual |
| Supply Voltage | DC 12–24 V | Product Manual |
| Communication Interface | PWM / CAN | Product Manual |
| Price | Not disclosed | - |

**Technical Highlights**: Integrated motor + leadscrew + drive, small size, high torque, suitable for robot fingers and micro joints.

**Application Scenarios**: Dexterous hand finger actuation, micro robots, medical precision instruments, adaptive grippers.

## Supply Chain Position

- **Upstream Key Components/Materials**: Micro motors, ball screws, bearings, driver ICs, tactile sensors, structural parts
- **Downstream Customers/Application Scenarios**: Humanoid robot OEMs, prosthetic manufacturers, service robot companies, research institutions
- **Main Competitors/Peers**: Shadow Robot, SCHUNK, CloudMinds, AGIBOT, Fourier Intelligence

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_inspire_robots`
- Product/Component Entities: `ent_product_inspire_dexterous_hand`, `ent_component_inspire_micro_linear_actuator`
- Key Relationships:
  - `ent_company_inspire_robots` -- `manufactures` --> `ent_product_inspire_dexterous_hand`
  - `ent_company_inspire_robots` -- `manufactures` --> `ent_component_inspire_micro_linear_actuator`

## References

1. [Official Website](https://www.inspiterobots.com)
2. [WAIC 2026 Exhibition Coverage](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.inovance.com) (Please verify against actual product models)
