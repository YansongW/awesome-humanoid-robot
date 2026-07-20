# Heidenhain

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 海德汉 |
| **English Name** | Heidenhain |
| **Headquarters** | Traunreut, Bavaria, Germany |
| **Founded** | 1948 |
| **Website** | [https://www.heidenhain.com](https://www.heidenhain.com) |
| **Supply Chain Segment** | Rotary encoders, angle encoders, linear scales, CNC control systems |
| **Enterprise Attribute** | Private enterprise, global leader in precision measurement and CNC technology |
| **Parent Company/Group** | DR. JOHANNES HEIDENHAIN GmbH |
| **Data Source** | Heidenhain official website, product datasheets, public information |

## Company Profile

Heidenhain is a globally leading supplier of precision measurement and control technology. Its product portfolio covers rotary encoders, angle encoders, linear scales, length gauges, CNC control systems, and machine tool probes.

Heidenhain encoders are renowned for their high precision, high reliability, and excellent resistance to contamination. They are widely used in high-end CNC machine tools, servo motors, robots, electronics manufacturing, medical equipment, and renewable energy sectors. Its inductive ECI/EQI platform, photoelectric ECN/EQN/ERN series, and absolute RCN/RQN series are core feedback components in industrial motion control.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Rotary Encoders | Motor feedback and shaft angle measurement | ECN/EQN/ERN / ECI/EQI | Servo motors, robots, machine tools |
| Angle Encoders | High-precision angle measurement | RCN / RON / ERP | CNC rotary tables, precision instruments |
| Linear Scales | High-precision displacement measurement | LC / LS / LF series | CNC machine tools, coordinate measuring machines |
| CNC Control Systems | Machine tool control | TNC / iTNC 530 | High-end machining centers |

## Representative Products

### Heidenhain EQI 1131 Inductive Multi-turn Rotary Encoder

> Heidenhain EQI 1131: Please visit the [official page](https://www.heidenhain.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | Absolute multi-turn rotary encoder without integral bearing | Official datasheet |
| Scanning Principle | Inductive scanning | Official datasheet |
| Positions per Revolution | 524,288 (19 bit) | Official datasheet |
| Number of Revolutions | 4096 (12 bit) | Official datasheet |
| System Accuracy | ±120" | Official datasheet |
| Maximum Shaft Speed | ≤ 12,000 rpm | Official datasheet |
| Axial Tolerance | ±0.5 mm | Official datasheet |
| Operating Temperature | -20°C to +115°C | Official datasheet |
| External Temperature Sensor | KTY / PT1000 | Official datasheet |
| Interface | EnDat 3.0 / HMC 2 Single Cable | Official datasheet |
| Functional Safety | SIL 2 (SIL 3 achievable with external measures) | Official datasheet |
| Housing Diameter | Approx. 37 mm | Official datasheet |
| Vibration Resistance | Stator 400 m/s² / Rotor 600 m/s² | Official datasheet |
| Weight | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: Inductive scanning offers strong resistance to contamination and vibration. EnDat 3.0 high-speed serial interface supports functional safety and single-cable technology, suitable for high-dynamic servo motors.

**Application Scenarios**: Servo motor feedback, humanoid robot joints, CNC machine tool spindles, industrial robots.

### Heidenhain RCN 8380 High-Precision Angle Encoder

> Heidenhain RCN 8380: Please visit the [official page](https://www.heidenhain.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | Absolute angle encoder | Public information |
| Application | CNC rotary tables, precision rotary tables | Public information |
| Features | High precision, high resolution, integral bearing | Public information |
| Interface | EnDat 2.2 / EnDat 3.0 | Public information |
| Accuracy | Not disclosed | - |
| Weight | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: Features a high-precision integral bearing, pre-adjusted for optimal fit, with low starting torque and smooth motion, ideal for precise angular positioning.

**Application Scenarios**: High-end CNC rotary tables, precision measuring instruments, semiconductor equipment, astronomical telescopes.

## Supply Chain Position

- **Upstream Key Components/Materials**: High-precision grating materials, photoelectric/inductive scanning chips, precision bearings, electronic components, packaging materials
- **Downstream Customers/Applications**: High-end CNC machine tools, servo systems, industrial robots, humanoid robots, semiconductor equipment, medical imaging, aerospace
- **Main Competitors/Comparables**: Renishaw, OPG/Yuheng Optics, Tamagawa, Inovance Technology

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_heidenhain`
- Product Entity: `ent_component_heidenhain_eqi_1131`
- Product Entity: `ent_component_heidenhain_rcn_8380`
- Key Relationships:
  - `ent_company_heidenhain` -- `manufactures` --> `ent_component_heidenhain_eqi_1131`
  - `ent_company_heidenhain` -- `manufactures` --> `ent_component_heidenhain_rcn_8380`
  - `ent_component_heidenhain_eqi_1131` -- `used_in` --> `ent_product_humanoid_robot_joint`

## References

1. [Heidenhain Official Website](https://www.heidenhain.com)
2. [Heidenhain ECI/EQI 1100 Series Datasheet](https://www.heidenhain.de/fileadmin/pdf/zh_CN/Broschueren/BR_Rotary_Encoder_Platform_ECI_EQI_ID1465030_zh.pdf)
3. [Heidenhain China – ECI/EQI 1100 Product Page](https://www.heidenhain.com.cn/%E4%BA%A7%E5%93%81/%E7%BC%96%E7%A0%81%E5%99%A8/%E6%97%8B%E8%BD%AC%E7%BC%96%E7%A0%81%E5%99%A8/%E5%86%85%E9%83%A8%E6%97%8B%E8%BD%AC%E7%BC%96%E7%A0%81%E5%99%A8/eci/ebi/eqi-1100%E7%B3%BB%E5%88%97)
4. [Appendix D Product Catalog](../index-products.md)
