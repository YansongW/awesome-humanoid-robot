# PAL Robotics

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).  
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | PAL Robotics |
| **English Name** | PAL Robotics |
| **Headquarters** | Barcelona, Spain |
| **Founded** | 2004 |
| **Website** | [https://pal-robotics.com](https://pal-robotics.com) |
| **Supply Chain Role** | Research humanoid robots, open-source ROS platform, service robots |
| **Company Type** | Private company |
| **Parent Company/Group** | None |
| **Data Source** | PAL Robotics official website, TALOS product page, official datasheet |

## Company Overview

PAL Robotics is a leading European service and research robotics company. The TALOS bipedal humanoid robot is renowned for its high-dynamic control, full-stack open-source ROS/ROS 2 architecture, and industrial-grade torque control.

TALOS is designed for AI, machine learning, motion control, and Industry 4.0 research, offering full-joint torque feedback, a 2 kHz control loop, and EtherCAT communication. The company also provides platforms such as TIAGo and REEM-C.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| TALOS | Bipedal humanoid research platform | TALOS | Industrial research, AI & motion control |
| TIAGo / REEM-C | Service/research robots | TIAGo / REEM-C | Human-robot interaction, elderly care, scientific research |

## Representative Products

### PAL Robotics TALOS

> PAL Robotics TALOS: Please visit the [official page](https://pal-robotics.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | 175 cm (height) | PAL Robotics product page |
| Weight | 95 kg | PAL Robotics product page |
| Degrees of Freedom | 32 (legs 6×2, arms 7×2, waist 2, neck 2, grippers 1×2) | Official datasheet |
| Payload/Torque | 6 kg with arm extended | PAL Robotics product page |
| Speed | Approx. 3 km/h | Third-party summary |
| Battery Life | 1.5 h walking / 3 h standby (1080 Wh) | Official datasheet |
| Interfaces/Communication | ROS / ROS 2, EtherCAT, Ubuntu LTS RT | Official datasheet |
| Price | Quoted on request | - |

**Technical Highlights**: Full torque feedback joints, 2 kHz control, ROS/ROS 2 open source, industrial-grade tool operation, customizable head and grippers.

**Application Scenarios**: Robotics research, motion control algorithm validation, Industry 4.0 demonstrations, human-robot interaction research.

### PAL Robotics REEM-C

> PAL Robotics REEM-C: Please visit the [official page](https://pal-robotics.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 165 cm (height) | Public information |
| Weight | Approx. 80 kg | Public information |
| Degrees of Freedom | 44 | Public information |
| Payload/Torque | Not disclosed | - |
| Speed | Not disclosed | - |
| Battery Life | Not disclosed | - |
| Interfaces/Communication | ROS | Public information |
| Price | Quoted on request | - |

**Technical Highlights**: An early full-size humanoid research platform that laid the hardware and ROS control foundation for TALOS.

**Application Scenarios**: Human-robot interaction, navigation, and motion research.

## Supply Chain Position

- **Upstream Key Components/Materials**: Motors/drives, force/torque sensors, computing modules, structural parts, and batteries.
- **Downstream Customers/Application Scenarios**: Research institutions (Inria, NASA, DARPA), EU research projects, service robot clients.
- **Main Competitors/Peers**: Boston Dynamics Atlas (research/industrial), other research humanoid platforms.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_pal_robotics`
- Product/Platform Entities: `ent_product_pal_robotics_talos`, `ent_product_pal_robotics_reem_c`
- Key Relationships:
  - `rel_ent_company_pal_robotics_manufactures_ent_product_pal_robotics_talos` (`ent_company_pal_robotics` → `manufactures` → `ent_product_pal_robotics_talos`)
  - `rel_ent_company_pal_robotics_manufactures_ent_product_pal_robotics_reem_c` (`ent_company_pal_robotics` → `manufactures` → `ent_product_pal_robotics_reem_c`)

## References

1. [PAL Robotics Official Website](https://pal-robotics.com)
2. [TALOS Product Page](https://pal-robotics.com/robot/talos/)
3. [TALOS Official Datasheet PDF](https://pal-robotics.com/wp-content/uploads/2024/05/Datasheet-TALOS.pdf)
