# Kunwei KWR36 6-Axis Force Sensor

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update date: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Kunwei Technology](../companies/company_kunwei.md) |
| **Product Category** | Miniature 6-axis force/torque sensor |
| **Release Date** | Continuously on sale |
| **Status** | Mass production/commercial |
| **Official Website/Source** | [Kunwei Technology Official Website](https://www.kunweitech.com) |

## Product Overview

The Kunwei KWR36 series is a miniature high-precision 6-axis force sensor that measures forces and torques in three orthogonal directions (Fx/Fy/Fz/Mx/My/Mz) in real time. The product is designed based on the strain gauge electrical measurement principle, uses six-axis joint calibration technology to fully suppress inter-axis crosstalk, and employs aerospace alloy materials to achieve a balance of high overload capacity, high stiffness, and high sensitivity.

The KWR36 has a diameter of approximately 36 mm, a height of about 20 mm, and weighs only 40 – 60 g. It has an IP64 protection rating and supports multiple communication methods including RS422/RS485/CAN/EtherCAT/Ethernet/USB and analog output. It is widely used in collaborative robots, medical surgical robots, 3C inspection, and humanoid robot wrist force control.

## Product Image

> Kunwei KWR36: Please visit the [official website](https://www.kunweitech.com) for details.

## Specification Table

| Specification Item | Value | Notes/Source |
|-------------------|-------|--------------|
| Type | Miniature 6-axis force sensor | Official website/dealer information |
| Diameter | 30 – 36 mm (varies by model) | Official website/dealer information |
| Height | Approx. 20 mm | Official website/dealer information |
| Weight | 40 – 60 g | Official website/dealer information |
| Force measurement range (Fx/Fy/Fz) | 30 / 50 / 80 N (typical models) | Official website/dealer information |
| Torque measurement range (Mx/My/Mz) | 1.5 / 2 / 3 Nm | Official website/dealer information |
| Accuracy | 0.1% FS | Official website/dealer information |
| Precision (including crosstalk) | 0.5% FS | Official website/dealer information |
| Overload capacity | 300% FS | Official website/dealer information |
| Protection rating | IP64 | Official website/dealer information |
| Supply voltage | 9 – 24 VDC | Official website/dealer information |
| Communication interface | RS422/RS485/CAN/EtherCAT/Ethernet/USB/Analog | Official website/dealer information |
| Sampling frequency | 1000 Hz | Official website/dealer information |
| Resolution | 24 bit | Official website/dealer information |
| Operating temperature | 0℃ – 80℃ | Official website/dealer information |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Kunwei Technology](../companies/company_kunwei.md)
- **Core Components/Technology Source**: Self-developed six-axis joint calibration and decoupling algorithm, aerospace alloy elastomer; strain gauges, signal processing chips, data acquisition modules are externally purchased.
- **Downstream Applications/Customers**: Collaborative robots, medical robots, humanoid robots, 3C inspection equipment, automotive testing.

## Knowledge Graph Nodes and Relationships

- Component entity: `ent_component_kunwei_kwr36`
- Manufacturer entity: `ent_company_kunwei`
- Key relationships:
  - `rel_ent_company_kunwei_manufactures_ent_component_kunwei_kwr36` (`ent_company_kunwei` → `manufactures` --> `ent_component_kunwei_kwr36`)

## Application Scenarios

- **Collaborative Robots**: End-effector force control, drag teaching, collision detection, and human-robot collaboration.
- **Medical Surgical Robots**: Fine instrument manipulation and tissue interaction force feedback.
- **Humanoid Robots**: Wrist/ankle force perception, supporting balance and grasping.
- **3C Inspection and Assembly**: Micro-force measurement, precision insertion, and surface force control.

## Competitive Comparison

| Comparison Item | Kunwei KWR36 | Yuli M35XX | Keli KL6D-M30-B |
|----------------|--------------|------------|-----------------|
| Type | Miniature 6-axis force sensor | Ultra-thin 6-axis force sensor | Robot-specific 6-axis force sensor |
| Diameter/Thickness | 36 mm / 20 mm | Not disclosed / 9.2 mm | Not disclosed |
| Accuracy | 0.1% FS | Not disclosed | 0.1% FS |
| Communication Interface | RS422/RS485/CAN/EtherCAT/USB/Analog | Ethernet/EtherCAT/RS485/USB/Analog | High-speed digital communication |
| Core Advantage | Miniature high precision, aerospace alloy | Ultra-thin, suitable for humanoid robots | Domestic leader, batch supply |

## Selection and Deployment Recommendations

- Select the appropriate range model based on the robot's end-effector load and torque requirements, and confirm that the communication protocol matches the controller.
- Six-axis joint calibration data is sensitive to installation orientation; it is recommended to avoid additional mechanical pre-stress and perform periodic recalibration.

## References

1. [Kunwei Technology Official Website](https://www.kunweitech.com)
2. [Kunwei Technology KWR36 Product Page](https://www.kunweitech.com/proinfo/56.html)
3. [Robot Online – KWR36 Parameters](https://m.imrobotic.com/appequi/detail/5609.html)
4. [Appendix D Company Directory](../index-companies.md)
