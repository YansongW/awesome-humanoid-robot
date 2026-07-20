# Bota Systems SensONE 6-Axis Force/Torque Sensor

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Bota Systems](../companies/company_bota_systems.md) |
| **Product Category** | 6-Axis Force/Torque Sensor |
| **Release Date** | Continuously on sale |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [Bota Systems SensONE 6-Axis Force/Torque Sensor Product/Data Page](https://www.bota-systems.com/sensone) |

## Product Overview

SensONE is Bota Systems' mainstream 6-axis force/torque sensor designed for collaborative robots and humanoid robots, supporting drag teaching, force-controlled assembly, polishing, and collision detection. Its compact disc-shaped structure can be directly mounted on the robot's end flange, offering multiple range and communication interface options.

## Product Image

> Bota Systems SensONE 6-Axis Force/Torque Sensor: Please visit the [official page](https://www.bota-systems.com/sensone) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | 6-Axis Force/Torque Sensor | Official website |
| Diameter | Approx. 80 mm | Official website/datasheet |
| Height | Approx. 21 mm | Official website/datasheet |
| Weight | Approx. 290 g | Official website/datasheet |
| Force Measurement Range (Fx/Fy) | ±200 N | Official website/datasheet |
| Force Measurement Range (Fz) | ±500 N | Official website/datasheet |
| Torque Measurement Range (Mx/My/Mz) | ±8 Nm | Official website/datasheet |
| Accuracy | Not disclosed | - |
| Overload Capacity | Approx. 500% FS | Official website/datasheet |
| Sampling Frequency | Up to 1000 Hz | Official website/datasheet |
| Communication Interface | EtherCAT / Ethernet / USB / RS485 / CAN | Official website/datasheet |
| Protection Rating | IP67 | Official website/datasheet |
| Power Supply | Not disclosed | - |
| Operating Temperature | Not disclosed | - |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Bota Systems](../companies/company_bota_systems.md)
- **Core Components/Technology Source**: Self-developed six-axis force sensing elastomer and decoupling algorithm, silicon strain gauges, signal conditioning circuit, industrial-grade housing and connectors.
- **Downstream Applications/Customers**: Collaborative robot OEMs, humanoid robot integrators, medical rehabilitation equipment, automation integrators, research institutions.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_bota_systems_sensone`
- Component Entity: `ent_component_bota_systems_sensone_sensor`
- Manufacturer Entity: `ent_company_bota_systems`
- Key Relationships:
  - `rel_ent_company_bota_systems_manufactures_ent_product_bota_systems_sensone` (`ent_company_bota_systems` → `manufactures` → `ent_product_bota_systems_sensone`)
  - `rel_ent_company_bota_systems_manufactures_ent_component_bota_systems_sensone_sensor` (`ent_company_bota_systems` → `manufactures` → `ent_component_bota_systems_sensone_sensor`)
  - `rel_ent_product_bota_systems_sensone_uses_ent_component_bota_systems_sensone_sensor` (`ent_product_bota_systems_sensone` → `uses` → `ent_component_bota_systems_sensone_sensor`)

## Application Scenarios

- **Collaborative Robot Force Control**: End-effector force feedback enables compliant assembly, polishing, and grinding.
- **Humanoid Robot Wrist**: Provides 6-axis force sensing to support grasping, balance, and collision detection.
- **Drag Teaching**: Fast trajectory teaching and programming based on force feedback.
- **Medical Rehabilitation Robot**: Low-latency force feedback for rehabilitation training and surgical assistance.

## Competitive Comparison

| Comparison Item | This Product | Main Competitor A | Main Competitor B |
|-----------------|--------------|-------------------|-------------------|
| Type | Collaborative Robot 6-Axis Force Sensor | ATI Nano Series | OnRobot HEX-E |
| Range | Fx/Fy ±200 N / Fz ±500 N | Multiple models | ±100 N / ±10 Nm |
| Communication | EtherCAT/Ethernet/USB/CAN | Analog/DAQ/EtherCAT | TCP/IP/USB/EtherNet/IP |
| Core Advantage | Compact, cost-effective | Extremely small size, high overload | Plug-and-play ecosystem |

## Selection and Deployment Recommendations

- Select the specific model based on the resolution, range, accuracy, or computational requirements of the target application.
- Before deployment, confirm that the interface, power supply, heat dissipation, mechanical mounting, and ambient temperature range are compatible.
- It is recommended to obtain the latest firmware, SDK, and technical support through official channels or authorized distributors.

## Related Entries

- [Manufacturer: Bota Systems](../companies/company_bota_systems.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [Bota Systems Official Website](https://www.bota-systems.com)
2. [Bota Systems SensONE 6-Axis Force/Torque Sensor Product/Data Page](https://www.bota-systems.com/sensone)
3. Product datasheet and public technical reports
4. [Appendix D Company Directory](../index-companies.md)
