# Heidenhain EQI 1131 Inductive Multi-turn Rotary Encoder

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Index](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Heidenhain](../companies/company_heidenhain.md) |
| **Product Category** | Absolute multi-turn rotary encoder without integral bearing |
| **Release Date** | Current mainstream product |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [Heidenhain Official Website](https://www.heidenhain.com) |

## Product Overview

The Heidenhain EQI 1131 belongs to the ECI/EQI 1100 series inductive rotary encoder platform. It is an absolute multi-turn rotary encoder without an integral bearing. This product uses an inductive scanning principle, offering excellent immunity to contamination, oil, and vibration, making it particularly suitable for high-dynamic, high-reliability servo motor feedback applications.

The EQI 1131 features a resolution of 19 bits per revolution, a multi-turn count of 12 bits (4096 revolutions), a system accuracy of ±120", a maximum shaft speed of up to 12,000 rpm, supports the EnDat 3.0 interface and HMC 2 single-cable technology, and can meet SIL 2 / PL d functional safety requirements (SIL 3 / PL e achievable with external measures).

## Product Image

> Heidenhain EQI 1131: Please visit the [official documentation](https://www.heidenhain.com) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | Absolute multi-turn rotary encoder without integral bearing | Official datasheet |
| Scanning Principle | Inductive scanning | Official datasheet |
| Positions per Revolution | 524,288 (19 bit) | Official datasheet |
| Number of Revolutions | 4096 (12 bit) | Official datasheet |
| System Accuracy | ±120" | Official datasheet |
| Maximum Shaft Speed | ≤ 12,000 rpm | Official datasheet |
| Axial Tolerance | ±0.5 mm | Official datasheet |
| Operating Temperature | -20℃ to +115℃ | Official datasheet |
| External Temperature Sensor | KTY / PT1000 | Official datasheet |
| Interface | EnDat 3.0 / HMC 2 Single Cable | Official datasheet |
| Functional Safety | SIL 2 / PL d (SIL 3 / PL e achievable with external measures) | Official datasheet |
| Housing Diameter | Approx. 37 mm | Official datasheet |
| Vibration Resistance | Stator 400 m/s² / Rotor 600 m/s² | Official datasheet |
| Weight | Not disclosed | - |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Heidenhain](../companies/company_heidenhain.md)
- **Core Component/Technology Source**: Self-developed inductive scanning ASIC, EnDat interface, and functional safety algorithms; high-precision grating materials, semiconductor chips, and structural components are sourced externally.
- **Downstream Applications/Customers**: High-end servo motors, industrial robots, humanoid robot joints, CNC machine tools, semiconductor equipment, medical imaging.

## Knowledge Graph Nodes and Relationships

- Component Entity: `ent_component_heidenhain_eqi_1131`
- Manufacturer Entity: `ent_company_heidenhain`
- Key Relationships:
  - `rel_ent_company_heidenhain_manufactures_ent_component_heidenhain_eqi_1131` (`ent_company_heidenhain` → `manufactures` --> `ent_component_heidenhain_eqi_1131`)

## Application Scenarios

- **Servo Motor Feedback**: Closed-loop control of speed and position for high-dynamic motors.
- **Humanoid Robot Joints**: High-precision feedback for joint angle and speed.
- **CNC Machine Tool Spindles**: Positioning and synchronous control for high-speed spindles.
- **Semiconductor/Medical Equipment**: Feedback for precision rotary stages and motion platforms.

## Competitive Comparison

| Comparison Item | Heidenhain EQI 1131 | OPG JZN/JKN | Tamagawa TS5700 |
|-----------------|---------------------|-------------|-----------------|
| Scanning Principle | Inductive | Optical/Metallic Grating | Magnetic/Optical |
| Resolution | 19 bit/rev + 12 bit revolutions | Up to 29-bit absolute | Varies by model |
| System Accuracy | ±120" | Leading domestically | Varies by model |
| Functional Safety | SIL 2/3 | Not disclosed | Supported in some models |
| Interface | EnDat 3.0 / HMC 2 | Not disclosed | Multi-protocol |
| Core Advantage | International brand, functional safety, single cable | Domestic alternative, price advantage | Stable and reliable |

## Selection and Deployment Recommendations

- Before deployment, confirm the motor shaft dimensions, locating hole specifications, EnDat interface version, and drive compatibility.
- Although inductive encoders have strong resistance to contamination, avoid strong magnetic field interference and ensure the stator-rotor mounting air gap is within the specified range.

## References

1. [Heidenhain Official Website](https://www.heidenhain.com)
2. [Heidenhain ECI/EQI 1100 Datasheet](https://www.heidenhain.de/fileadmin/pdf/zh_CN/Broschueren/BR_Rotary_Encoder_Platform_ECI_EQI_ID1465030_zh.pdf)
3. [Heidenhain China – ECI/EQI 1100 Product Page](https://www.heidenhain.com.cn/%E4%BA%A7%E5%93%81/%E7%BC%96%E7%A0%81%E5%99%A8/%E6%97%8B%E8%BD%AC%E7%BC%96%E7%A0%81%E5%99%A8/%E5%86%85%E9%83%A8%E6%97%8B%E8%BD%AC%E7%BC%96%E7%A0%81%E5%99%A8/eci/ebi/eqi-1100%E7%B3%BB%E5%88%97)
4. [Appendix D Company Directory](../index-companies.md)
