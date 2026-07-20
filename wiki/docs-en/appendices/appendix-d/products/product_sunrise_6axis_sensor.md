# 宇立仪器 M35XX 超薄六维力传感器 / Sunrise M35XX Ultra-thin 6-Axis Force Sensor

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Sunrise Instruments](../companies/company_sunrise.md) |
| **Product Category** | Ultra-thin 6-axis force/torque sensor |
| **Release Date** | Continuously on sale |
| **Status** | Mass production/commercial |
| **Official Website/Source** | [Sunrise Instruments Official Website](https://www.srisensor.com.cn) |

## Product Overview

The Sunrise M35XX series is an ultra-thin commercial 6-axis force sensor designed for scenarios with limited installation space but high precision requirements for multi-dimensional force measurement. The product has a thickness as low as 9.2 mm, offers 3 times the rated range overload capacity, and features nonlinearity/hysteresis less than 1% FS. It is officially positioned as "an ideal choice for humanoid robots."

Based on strain gauge measurement principles, the M35XX supports multiple output interfaces including Ethernet TCP/IP, EtherCAT, RS485, RS232, USB, and analog signals. It can be seamlessly integrated into collaborative robot end-effectors, humanoid robot wrists/ankles, and medical surgical robots for applications such as drag teaching, force-controlled grinding, precision assembly, and compliant interaction.

## Product Image

> Sunrise M35XX: Please visit the [official website](https://www.srisensor.com.cn) for details.

## Specification Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Type | Ultra-thin commercial 6-axis force sensor | Official website public information |
| Thickness | As low as 9.2 mm | Official website public information |
| Overload Capacity | 3 times rated range | Official website public information |
| Nonlinearity/Hysteresis | < 1% FS | Official website public information |
| Zero Drift Performance | 0.05%/10°C (public indicator for the same series) | Official website public information |
| Communication Interface | Ethernet TCP/IP, EtherCAT, RS485, RS232, USB, Analog | Official website public information |
| Protection Level | Not disclosed | - |
| Weight | Not disclosed | - |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Sunrise Instruments](../companies/company_sunrise.md)
- **Core Components/Technology Source**: Self-developed strain gauge elastomer structure, signal conditioning circuit, multi-interface data acquisition module; strain gauges and structural components are outsourced.
- **Downstream Applications/Customers**: Humanoid robot OEMs, collaborative robot manufacturers, medical surgical robots, automotive testing and precision assembly equipment suppliers.

## Knowledge Graph Nodes and Relationships

- Component Entity: `ent_component_sunrise_m35xx`
- Manufacturer Entity: `ent_company_sunrise`
- Key Relationships:
  - `rel_ent_company_sunrise_manufactures_ent_component_sunrise_m35xx` (`ent_company_sunrise` → `manufactures` --> `ent_component_sunrise_m35xx`)

## Application Scenarios

- **Humanoid Robots**: Wrist/ankle force control for compliant grasping, balance adjustment, and safe interaction.
- **Collaborative Robots**: End-effector force feedback for drag teaching and precision assembly.
- **Medical Surgical Robots**: Force measurement at the instrument tip to enhance operational precision and safety.
- **3C Inspection and Assembly**: Precision insertion, screw tightening, and surface mounting force control.

## Competitive Comparison

| Comparison Item | Sunrise M35XX | Kunwei KWR36 | ATI Nano25 |
|----------------|---------------|--------------|------------|
| Type | Ultra-thin 6-axis force sensor | Miniature 6-axis force sensor | Miniature 6-axis force sensor |
| Thickness | 9.2 mm | Approx. 20 mm | 21.6 mm |
| Overload Capacity | 3 times | 3 times | 7.1 – 15.1 times |
| Core Advantage | Ultra-thin, rich interfaces | Miniature, high precision | International brand, ultra-high overload |

## Selection and Deployment Recommendations

- When selecting, focus on confirming installation space, range, interface protocol, and compatibility with the robot controller.
- The ultra-thin structure is sensitive to mounting surface flatness and tightening torque. It is recommended to follow the official installation specifications and perform on-site calibration.

## References

1. [Sunrise Instruments Official Website](https://www.srisensor.com.cn)
2. [Sunrise Instruments 6-axis Force Sensor Product Page](https://www.srisensor.com.cn)
3. [Appendix D Company Directory](../index-companies.md)
