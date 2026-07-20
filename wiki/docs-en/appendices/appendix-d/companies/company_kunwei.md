# Kunwei Technology

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 坤维科技 |
| **English Name** | Kunwei Technology |
| **Headquarters** | Changzhou, Jiangsu, China (Changzhou Kunwei Sensing Technology Co., Ltd.) |
| **Founded** | 2018 |
| **Website** | [https://www.kunweitech.com](https://www.kunweitech.com) |
| **Supply Chain Role** | Six-axis force/torque sensors, force sensors, force control solutions |
| **Enterprise Type** | Private enterprise, high-tech enterprise |
| **Parent Company/Group** | Independent operation |
| **Data Source** | Kunwei Technology official website, public product datasheets, Imrobotic |

## Company Profile

Kunwei Technology is a high-tech enterprise specializing in the R&D and manufacturing of high-precision force sensors. Its core team comes from national aerospace research institutions and has nearly 20 years of experience in multi-axis force sensor development.

The company's products cover conventional six-axis force sensors, joint torque sensors, industrial weighing instruments, force measurement platforms, and wind tunnel balances, with diameters ranging from 36 mm to 200 mm and force ranges covering 30 N to 20 kN. Kunwei Technology is distinguished by its six-axis joint calibration technology, aerospace alloy structures, and highly integrated embedded data acquisition systems. It has entered scenarios such as collaborative robots, humanoid robots, medical surgery, and aerospace testing.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| Conventional Six-Axis Force Sensors | Robot end-effector force sensing | KWR36 / KWR46 / KWR75 / KWR82 | Collaborative robots, medical robots, test & measurement |
| Six-Axis Force Sensors for Humanoid Robots | Wrist/ankle force control | Custom series | Humanoid robots |
| Joint Torque Sensors | Rotary joint torque | KWR85N / KWR86N series | Industrial robot joints, humanoid robot joints |
| Industrial Weighing Instruments / Force Measurement Platforms | Force measurement and weighing | KWT1 series | Automated production lines, testing equipment |

## Representative Products

### Kunwei Technology KWR36 Series Six-Axis Force Sensor

> Kunwei KWR36: Please visit [official materials](https://www.kunweitech.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Type | Miniature six-axis force sensor | Official website/dealer materials |
| Diameter | 30 – 36 mm (varies by model) | Official website/dealer materials |
| Height | Approx. 20 mm | Official website/dealer materials |
| Force Measurement Range (Fx/Fy/Fz) | 30 / 50 / 80 N (typical models) | Official website/dealer materials |
| Torque Measurement Range (Mx/My/Mz) | 1.5 / 2 / 3 Nm | Official website/dealer materials |
| Accuracy | 0.1% FS | Official website/dealer materials |
| Precision (including crosstalk) | 0.5% FS | Official website/dealer materials |
| Overload Capacity | 300% FS | Official website/dealer materials |
| Weight | 40 – 60 g | Official website/dealer materials |
| Supply Voltage | 9 – 24 VDC | Official website/dealer materials |
| Communication Interface | RS422/RS485/CAN/EtherCAT/Ethernet/USB/Analog | Official website/dealer materials |
| Protection Rating | IP64 | Official website/dealer materials |
| Sampling Frequency | 1000 Hz | Official website/dealer materials |
| Price | Not disclosed | - |

**Technical Highlights**: Miniaturized design, six-axis joint calibration to suppress crosstalk, aerospace alloy balancing high stiffness and high sensitivity, suitable for medical and collaborative robot end-effectors.

**Application Scenarios**: Collaborative robot drag teaching, medical surgical robots, 3C inspection, small industrial robots, humanoid robot wrist force control.

### Kunwei Technology KWR75 Series Six-Axis Force Sensor

> Kunwei KWR75: Please visit [official materials](https://www.kunweitech.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Type | Highly integrated six-axis force sensor | Official public materials |
| Integrated Data Acquisition | Built-in high-precision embedded intelligent circuit | Official public materials |
| Communication Interface | RS422/RS485/CAN/EtherCAT/USB/Analog | Official public materials |
| Installation Compatibility | Compatible with most collaborative robot end-effectors on the market | Official public materials |
| Application Scenarios | Drag teaching, automated testing, medical inspection, cutting & grinding | Official public materials |
| Accuracy | Not disclosed | - |
| Weight | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: Built-in embedded data acquisition, easy installation, highly compatible with collaborative robot end-effectors.

**Application Scenarios**: Collaborative robot end-effector force control, drag teaching, automated testing, 3C inspection, automotive testing.

## Supply Chain Position

- **Upstream Key Components/Materials**: Aerospace alloy, strain gauges, ASIC signal processing chips, precision machining, data acquisition modules
- **Downstream Customers/Application Scenarios**: Collaborative robots, medical robots, humanoid robots, automotive testing, 3C inspection, aerospace
- **Main Competitors/Benchmarks**: Yuli Instrument, Keli Sensing, ATI Industrial Automation, Blue Point Touch

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_kunwei`
- Product Entity: `ent_component_kunwei_kwr36`
- Product Entity: `ent_component_kunwei_kwr75`
- Key Relationships:
  - `ent_company_kunwei` -- `manufactures` --> `ent_component_kunwei_kwr36`
  - `ent_company_kunwei` -- `manufactures` --> `ent_component_kunwei_kwr75`
  - `ent_component_kunwei_kwr36` -- `used_in` --> `ent_product_humanoid_robot_wrist`

## References

1. [Kunwei Technology Official Website](https://www.kunweitech.com)
2. [Kunwei Technology KWR36 Product Page](https://www.kunweitech.com/proinfo/56.html)
3. [Imrobotic – KWR36 Parameters](https://m.imrobotic.com/appequi/detail/5609.html)
4. [Appendix D Product Catalog](../index-products.md)
