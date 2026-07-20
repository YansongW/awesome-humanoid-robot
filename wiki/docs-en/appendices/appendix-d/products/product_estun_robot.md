# Estun Robot

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Estun Automation / Estun Automation](../companies/company_estun.md) |
| **Product Category** | Industrial Robots / Collaborative Robots / Humanoid Components |
| **Release Date** | Founded in 1993, robot business continuously iterated |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | See references in the main text |

## Product Overview

Estun robots cover six-axis industrial robots, SCARA, collaborative robots, and core components for humanoid robots. The company insists on self-reliance and controllability, self-developing servo systems, motion controllers, and robot bodies, and enhancing welding and motion control technologies through overseas acquisitions. It is a core force in the domestic substitution and intelligent upgrade of Chinese industrial robots.

## Product Images

> Estun Robot: Please visit [Official Website](https://www.estun.com) for details.

## Specification Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Product Form | Six-axis Robot, SCARA, Collaborative Robot, Delta | Estun Official Website |
| Load Range | 3–600 kg | Product Manual |
| Repeat Positioning Accuracy | ±0.02–±0.05 mm | Product Manual |
| Reach | 500–3200 mm | Product Manual |
| Degrees of Freedom | 4–6 DOF | Public Specifications |
| Protection Level | IP40–IP67 (depending on model) | Product Manual |
| Controller | Self-developed ESTUN Controller | Estun Official Website |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Estun Automation / Estun Automation](../companies/company_estun.md)
- **Core Components/Technology Sources**: Servo motors, reducers, controllers, castings, cables, sensors.
- **Downstream Applications/Customers**: Automotive, 3C, lithium battery, photovoltaic, metal processing, logistics, humanoid robot OEMs.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_estun_robot`
- Manufacturer Entity: `ent_company_estun`
- Key Relationships:
  - `rel_ent_company_estun_manufactures_ent_product_estun_robot` (`ent_company_estun` → `manufactures` → `ent_product_estun_robot`)
  - `ent_product_estun_robot` -- `uses` --> `ent_component_estun_servo`
  - `ent_product_estun_robot` -- `uses` --> `ent_component_harmonic_drive`

## Application Scenarios

- **Welding**: After acquiring Cloos, it possesses high-end welding robots and processes.
- **Handling and Assembly**: Six-axis/SCARA used in 3C, lithium battery, and automotive parts production lines.
- **Humanoid Components**: Supply of harmonic reducers, frameless torque motors, and joint modules.

## Competitive Comparison

| Comparison Item | Estun | Inovance Technology | Fanuc/ABB |
|----------------|-------|---------------------|-----------|
| Positioning | Leading domestic industrial robot manufacturer | Industrial control + robot synergy | Foreign high-end |
| Core Advantage | Full series + M&A technology | Servo/PLC synergy | Brand and precision |
| Price | Domestic mid-range | Domestic mid-range | High-end |

## Selection and Deployment Recommendations

- Select the corresponding model based on computing power, precision, and scenario requirements, prioritizing the official toolchain and ecosystem compatibility.
- Before deployment, confirm whether the power supply, heat dissipation, mechanical interface, and communication protocol meet the overall system requirements.
- It is recommended to obtain the latest firmware, SDK, and technical support through official channels or authorized distributors.

## Related Entries

- [Manufacturer: Estun Automation / Estun Automation](../companies/company_estun.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [Estun Automation / Estun Automation Official Product/Company Page](https://www.estun.com)
2. Estun Official Website Product Page
3. Estun 2024 Annual Report
