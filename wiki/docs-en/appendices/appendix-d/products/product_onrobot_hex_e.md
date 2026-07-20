# OnRobot HEX-E QC 6-Axis Force/Torque Sensor

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [OnRobot](../companies/company_onrobot.md) |
| **Product Category** | Collaborative Robot 6-Axis Force/Torque Sensor |
| **Release Date** | Continuously on sale |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [OnRobot HEX-E QC 6-Axis Force/Torque Sensor Product/Data Page](https://www.onrobot.com/en/products/he-x) |

## Product Overview

The HEX-E QC is a 6-axis force/torque sensor designed by OnRobot for the end-effector of collaborative robots. It integrates a Quick Changer interface, supporting plug-and-play installation. It can measure 6-axis force/torque data in real-time, helping robots perform precision assembly, constant-force polishing, surface finishing, and collision detection.

## Product Image

> OnRobot HEX-E QC 6-Axis Force/Torque Sensor: Please visit the [official page](https://www.onrobot.com/en/products/he-x) for details.

## Specification Table

| Specification Item | Value | Notes/Source |
|-------------------|-------|--------------|
| Type | 6-Axis Force/Torque Sensor | Official Website |
| Force Measurement Range (Fx/Fy/Fz) | ±100 N / ±100 N / ±200 N | Official Website/Datasheet |
| Torque Measurement Range (Mx/My/Mz) | ±10 Nm / ±10 Nm / ±10 Nm | Official Website/Datasheet |
| Accuracy | Not disclosed | - |
| Resolution | Not disclosed | - |
| Sampling Frequency | Not disclosed | - |
| Overload Capacity | Approx. 500% FS | Official Website/Datasheet |
| Protection Rating | IP67 | Official Website/Datasheet |
| Communication Interface | TCP/IP, USB, EtherNet/IP, PROFINET | Official Website/Datasheet |
| Integrated Interface | Quick Changer / Robot Flange | Official Website/Datasheet |
| Power Supply | 24 V DC | Official Website/Datasheet |
| Weight | Approx. 350 g | Official Website/Datasheet |
| Operating Temperature | Not disclosed | - |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [OnRobot](../companies/company_onrobot.md)
- **Core Components/Technology Source**: Self-developed force sensing unit, signal processing and communication circuits, Quick Changer mechanical interface, industrial-grade sealed housing.
- **Downstream Applications/Customers**: Collaborative robot OEMs, automotive and electronics manufacturers, humanoid robot integrators, automation system integrators.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_onrobot_hex_e`
- Component Entity: `ent_component_onrobot_hex_e_sensor`
- Manufacturer Entity: `ent_company_onrobot`
- Key Relationships:
  - `rel_ent_company_onrobot_manufactures_ent_product_onrobot_hex_e` (`ent_company_onrobot` → `manufactures` → `ent_product_onrobot_hex_e`)
  - `rel_ent_company_onrobot_manufactures_ent_component_onrobot_hex_e_sensor` (`ent_company_onrobot` → `manufactures` → `ent_component_onrobot_hex_e_sensor`)
  - `rel_ent_product_onrobot_hex_e_uses_ent_component_onrobot_hex_e_sensor` (`ent_product_onrobot_hex_e` → `uses` → `ent_component_onrobot_hex_e_sensor`)

## Application Scenarios

- **Force-Controlled Assembly**: Compliant insertion and positioning in precision plug-in and gear assembly.
- **Constant-Force Grinding/Polishing**: Maintains constant contact force to improve surface quality consistency.
- **Insertion and Testing**: Force-displacement testing for components like connectors and switches.
- **Humanoid Robot Arms**: End-effector 6-axis force sensing for grasping and interaction.

## Competitive Comparison

| Comparison Item | This Product | Main Competitor A | Main Competitor B |
|----------------|--------------|-------------------|-------------------|
| Type | Collaborative Robot 6-Axis Force Sensor | ATI Nano25 | Bota Systems SensONE |
| Force Range | ±100 N / ±200 N | ±250 N / ±1000 N | ±200 N / ±500 N |
| Communication | TCP/IP/USB/EtherNet/IP | Analog/DAQ/EtherCAT | EtherCAT/Ethernet/CAN |
| Core Advantage | Quick-change integration, mature ecosystem | Extremely small size, high overload | Compact, high cost-performance |

## Selection and Deployment Recommendations

- Select the specific model based on the resolution, range, accuracy, or computational power requirements of the target application.
- Confirm interface, power supply, heat dissipation, mechanical installation, and ambient temperature range compatibility before deployment.
- It is recommended to obtain the latest firmware, SDK, and technical support through official channels or authorized distributors.

## Related Entries

- [Manufacturer: OnRobot](../companies/company_onrobot.md)
- [Appendix D.4 Key Product Wiki](../index-products.md)

## References

1. [OnRobot Official Website](https://www.onrobot.com)
2. [OnRobot HEX-E QC 6-Axis Force/Torque Sensor Product/Data Page](https://www.onrobot.com/en/products/he-x)
3. Product datasheet and public technical reports
4. [Appendix D Company Directory](../index-companies.md)
