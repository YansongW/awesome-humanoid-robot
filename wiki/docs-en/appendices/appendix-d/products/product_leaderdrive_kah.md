# Leaderdrive KAH Series Harmonic Drive

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Index](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Leaderdrive](../companies/company_leaderdrive.md) |
| **Product Category** | Harmonic Drive / Rotary Actuator |
| **Release Date** | Launched in recent years with the KAH/KAT/KAS rotary actuator series |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [Leaderdrive Official Website](http://www.leaderdrive.com) |

## Product Overview

The Leaderdrive KAH series is a hollow-shaft rotary actuator designed for high-end applications such as robot joints, CNC machine tools, and semiconductor equipment. It integrates a high-precision harmonic drive, frameless torque motor, hollow-shaft high-resolution absolute encoder, brake, and smart sensors into a single unit. Through integrated design, the KAH series reduces joint volume and weight while providing high torque density and a hollow passage for cables, air hoses, or laser beams.

The KAH series covers multiple specifications including KAH-14/17/20/25/32/40, with reduction ratios available in 51:1, 81:1, 101:1, 121:1, 161:1, and other options. Rated output torque ranges from tens of N·m up to 800 N·m, positioning accuracy can reach within 30 arcseconds, and the protection rating can be as high as IP67. This product is widely used in collaborative robots, humanoid robots, precision rotary tables, and medical equipment.

## Product Image

> Leaderdrive KAH Series: Please visit the [official website](http://www.leaderdrive.com) for details.

## Specification Parameter Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Series Specifications | KAH-14/17/20/25/32/40 | Official product manual |
| Reduction Ratio | 51 / 81 / 101 / 121 / 161:1 | Official product manual |
| Output Torque | Up to 800 N·m (KAH-40) | Official product manual |
| Positioning Accuracy | ≤30 arcsec | Official product manual |
| Repeat Positioning Accuracy | ≤10 arcsec | Official product manual |
| Supply Voltage | 220 VAC / 110 VAC / 48 VDC | Official product manual |
| Protection Rating | Up to IP67 | Official product manual |
| Weight | Varies by model | Not disclosed |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Leaderdrive](../companies/company_leaderdrive.md)
- **Core Components/Technology Source**: Self-developed "P tooth profile" harmonic drive, frameless torque motor, encoder, brake; bearings and steel are outsourced.
- **Downstream Applications/Customers**: Collaborative robots, humanoid robot joints, CNC machine tools, semiconductor equipment, medical machinery.

## Knowledge Graph Nodes and Relationships

- Component Entity: `ent_component_leaderdrive_kah`
- Manufacturer Entity: `ent_company_leaderdrive`
- Key Relationships:
  - `rel_ent_company_leaderdrive_manufactures_ent_component_leaderdrive_kah` (`ent_company_leaderdrive` → `manufactures` → `ent_component_leaderdrive_kah`)

## Application Scenarios

- **Humanoid Robot Joints**: Provides high-torque-density integrated rotary actuators for hip, knee, shoulder, and elbow joints.
- **Collaborative Robots**: Used for precision reduction and force-controlled joint modules in collaborative arms.
- **CNC Machine Tools and Rotary Tables**: Rotary worktables requiring high positioning and repeat positioning accuracy.
- **Semiconductor and Medical Equipment**: Precision transmission in clean environments with high reliability.

## Competitive Comparison

| Comparison Item | Leaderdrive KAH | Harmonic Drive CSF Series | Nabtesco RV Series |
|----------------|-----------------|---------------------------|--------------------|
| Type | Harmonic Rotary Actuator | Harmonic Drive | RV Reducer |
| Accuracy | ≤30 arcsec | ≤30 arcsec | ≤1 arcmin |
| Load | Up to 800 N·m | Varies by model | High load / High rigidity |
| Core Advantage | Integrated design, hollow wiring, localized supply | Accuracy and lifespan | Heavy load and rigidity |

## Selection and Deployment Recommendations

- When selecting an integrated rotary actuator, comprehensively consider peak torque, hollow bore diameter, encoder resolution, and bus interface.
- It is recommended to confirm details regarding heat dissipation, braking, and cable routing of the joint module with the Leaderdrive technical team.

## References

1. [Leaderdrive Official Website](http://www.leaderdrive.com)
2. [Leaderdrive KAH Series Rotary Actuator Product Manual](https://www.worldrobotconference.com/uploads/exuser2024/video/5vzzrp.pdf)
3. [East Money – Leaderdrive Research Report](https://pdf.dfcfw.com/pdf/H3_AP202311191611678375_1.pdf)
4. [Imrobotic – Leaderdrive Product Page](https://www.imrobotic.com/parts/detail/9678.html)
