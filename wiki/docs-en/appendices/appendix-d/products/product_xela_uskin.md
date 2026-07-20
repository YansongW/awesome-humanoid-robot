# XELA Robotics uSkin High-Density 3-Axis Tactile Sensor

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [XELA Robotics](../companies/company_xela.md) |
| **Product Category** | High-density 3-axis flexible tactile sensor / Electronic skin |
| **Release Date** | Continuous iteration since 2018 |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [XELA Robotics Official Website](https://www.xelarobotics.com) |

## Product Overview

XELA Robotics uSkin is a high-density three-axis flexible tactile sensor designed for robotic grippers and dexterous hands. uSkin uses a magnetoresistive sensing principle, where each sensing unit (taxel) can independently measure X, Y, and Z three-axis forces, with a resolution of 0.1 gf, a sampling frequency of 500 Hz, and a digital output that simplifies wiring to a minimum of 4 wires.

The soft elastomer shell of uSkin allows it to conform to complex curved surfaces, buffer overloads, and protect grasped objects. It is widely used in mainstream grippers and dexterous hands such as Robotiq, Weiss Robotics, Wonik Robotics, and Tesollo DG-5F. In 2026, XELA plans to reduce the standard sensing point size from 4 mm × 4 mm to 2.5 mm × 2.5 mm, further improving spatial resolution.

## Product Image

> XELA uSkin: Please visit the [official materials](https://www.xelarobotics.com) for details.

## Specification Table

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Sensing Principle | Magnetoresistive 3-axis force sensing | Official website public information |
| Sensing Dimensions | X, Y, Z three-axis force | Official website public information |
| Standard Sensing Point Size | 4 mm × 4 mm | Official website / Public reports |
| Next-Generation Sensing Point Size | 2.5 mm × 2.5 mm (Q2 2026) | Engineering.com |
| Single Taxel Normal Force Range | Up to 1500 gf (approx. 14.7 N) | XELA Catalog 2025 |
| Resolution | 0.1 gf (approx. 1 mN) | Official website public information |
| Sampling Frequency | 500 Hz | Official website public information |
| Output Method | Digital output | Official website public information |
| Wiring Requirement | Minimum 4 wires to read all sensors | Product manual |
| Packaging Material | Soft elastomer | Official website public information |
| Standard Models | uSPa 11/21/22/44/46, uSCu, uSPr series | Official website public information |
| Communication Interface | Digital bus (specific protocol not disclosed) | Product manual |
| Supply Voltage | Not disclosed | - |
| Operating Temperature | Not disclosed | - |
| Protection Rating | Not disclosed | - |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [XELA Robotics](../companies/company_xela.md)
- **Core Components/Technology Source**: Self-developed magnetoresistive 3-axis sensing chip, elastomer shell, and uAi software platform; microcontrollers and flexible substrates are outsourced.
- **Downstream Applications/Customers**: Humanoid robot dexterous hands, industrial grippers, logistics and warehousing, agricultural picking, research institutions, medical prosthetics.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_xela_uskin`
- Manufacturer Entity: `ent_company_xela`
- Component Entity: `ent_component_xela_uskin_module`
- Key Relationships:
  - `rel_ent_company_xela_manufactures_ent_product_xela_uskin` (`ent_company_xela` → `manufactures` --> `ent_product_xela_uskin`)
  - `rel_ent_company_xela_manufactures_ent_component_xela_uskin_module` (`ent_company_xela` → `manufactures` --> `ent_component_xela_uskin_module`)
  - `rel_ent_product_xela_uskin_uses_ent_component_xela_uskin_module` (`ent_product_xela_uskin` → `uses` --> `ent_component_xela_uskin_module`)

## Application Scenarios

- **Humanoid Robot Dexterous Hands**: Full-hand tactile coverage for fingertips, finger pads, and palm.
- **Industrial Gripper Force Control**: Direct integration with grippers such as Robotiq and Weiss Robotics for force/slip feedback.
- **Logistics Sorting**: Safe grasping of irregularly shaped, fragile, or soft items.
- **Agricultural Picking**: Adaptive picking of delicate objects like fruits and vegetables.
- **Medical Prosthetics**: Providing force perception close to human skin for prosthetics.

## Competitive Comparison

| Comparison Item | XELA uSkin | SynTouch BioTac | PX-6AX (Paxini) |
|-----------------|------------|-----------------|-----------------|
| Sensing Principle | Magnetoresistive 3-axis | Fluid/Electrode/Thermal conduction | 6D Hall array |
| Sensing Dimensions | 3-axis force | Force + Vibration + Temperature | 15 types of tactile information |
| Sensing Point Density | 4 mm (standard) / 2.5 mm (planned) | Single-point bionic | Array type |
| Core Advantage | Soft, easy to integrate, digital output | Bionic, robust | High density, full-stack dexterous hand |

## Selection and Deployment Recommendations

- Choose the uSPa (planar), uSCu (curved), or uSPr (gripper protection) series based on the geometric dimensions of the gripper or dexterous hand.
- The sensor is sensitive to magnetic fields; avoid strong magnetic fields and ferromagnetic materials during deployment. Use a reference sensor for compensation if necessary.
- Digital output simplifies hardware integration, but the corresponding driver or SDK must be reserved on the robot controller side.

## References

1. [XELA Robotics Official Website](https://www.xelarobotics.com)
2. [XELA Robotics Product Catalog 2025](https://49063741.fs1.hubspotusercontent-na2.net/hubfs/49063741/XELA%20Robotics%20-%20Catalog%202025.pdf)
3. [Engineering.com – uSkin integrated into Tesollo DG-5F](https://www.engineering.com/uskin-tactile-sensors-integrated-into-tesollo-dg-5f-robot-hand/)
4. [XELA Robotics Technology Page](https://xelarobotics.com/technology/)
5. [Appendix D Company Directory](../index-companies.md)
