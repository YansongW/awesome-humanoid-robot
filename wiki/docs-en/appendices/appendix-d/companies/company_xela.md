# XELA Robotics (Japan)

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | XELA Robotics |
| **English Name** | XELA Robotics Inc. |
| **Headquarters** | Tokyo, Japan (Waseda University spin-off) |
| **Founded** | 2018 |
| **Website** | [https://www.xelarobotics.com](https://www.xelarobotics.com) |
| **Supply Chain Role** | High-density 3-axis tactile sensors, robotic electronic skin, tactile integration solutions |
| **Enterprise Type** | Private enterprise, high-tech enterprise |
| **Parent Company/Group** | Independent operation |
| **Data Source** | XELA Robotics official website, product catalog, Engineering.com report |

## Company Profile

XELA Robotics is a robotic tactile sensing technology company spun off from Waseda University in Japan in 2018, focusing on providing "human-like touch" for robots. The company's core product, uSkin, is a high-density three-axis flexible tactile sensor that measures forces in the X/Y/Z directions and is designed with a soft, durable, and minimal-wiring architecture to fit various robotic grippers and dexterous hands.

XELA not only offers standardized sensor modules (uSkin Patch, uSkin Curved, uSkin Protect series) but also provides custom integration services, having integrated uSkin into mainstream grippers and robotic hands such as Robotiq, Weiss Robotics, Wonik Robotics, and Tesollo DG-5F. Its magnetoresistive sensing principle and digital output architecture give the sensor significant advantages in noise immunity, ease of wiring, and scalability.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Patch-type Tactile Sensor | General-purpose planar 3-axis force sensing | uSPa Series | Electronic skin, grippers |
| Fingertip Curved Sensor | Robot dexterous hand fingertips | uSCu Series | Multi-finger dexterous hands |
| Gripper-specific Protective Sensor | Direct integration into commercial grippers | uSPr Series | Industrial grippers |
| Tactile Integration Solution | Custom integration for whole machines/grippers | Custom Integration | Humanoid robots, industrial robots |

## Representative Products

### XELA Robotics uSkin High-Density 3-Axis Tactile Sensor

> XELA uSkin: Please visit the [official page](https://www.xelarobotics.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Sensing Principle | Magnetoresistive 3-axis force sensing | Official website public information |
| Sensing Dimensions | X, Y, Z three-axis force | Official website public information |
| Sensing Point Density | 4 mm × 4 mm (standard); planned reduction to 2.5 mm × 2.5 mm by 2026 | Engineering.com |
| Single Taxel Normal Force Range | Up to 1500 gf (approx. 14.7 N) | XELA Catalog 2025 |
| Resolution | 0.1 gf (approx. 1 mN) | Official website public information |
| Sampling Frequency | 500 Hz | Official website public information |
| Output Method | Digital output | Official website public information |
| Wiring | Minimum 4 wires to read all sensors | Product manual |
| Packaging | Soft elastomer housing, wear-resistant and overload-resistant | Official website public information |
| Standard Models | uSPa 11/21/22/44/46, uSCu, uSPr series | Official website public information |
| Operating Temperature | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: Each sensing unit independently measures three-axis forces like a joystick; digital output greatly simplifies wiring; the soft packaging conforms to curved surfaces, has strong overload resistance, and is compatible with various commercial grippers and dexterous hands.

**Application Scenarios**: Humanoid robot dexterous hands, industrial gripper force control, logistics sorting, agricultural harvesting, medical prosthetics, scientific research experiments.

### XELA uSkin Fingertip Curved Sensor (uSCu)

> XELA uSkin Curved: Please visit the [official page](https://www.xelarobotics.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | 3-axis curved tactile sensor | Product manual |
| Number of Taxels | 30 (typical model) | Distributor information |
| Design Purpose | Robot dexterous hand fingertips | Product manual |
| Features | Soft skin, fingertip fit, natural human-machine interaction | Product manual |
| Price | Not disclosed | - |

**Technical Highlights**: The curved design better conforms to robot fingers, providing a more natural contact geometry, suitable for full-hand tactile coverage of five-finger bionic dexterous hands.

**Application Scenarios**: Five-finger bionic dexterous hands, humanoid robots, teleoperation, precision grasping.

## Supply Chain Position

- **Upstream Key Components/Materials**: Magnetoresistive sensing chips, flexible elastomers, silicone packaging, microcontrollers, flexible PCBs
- **Downstream Customers/Application Scenarios**: Humanoid robot OEMs, collaborative robot grippers, logistics and warehousing, agricultural robots, research institutions
- **Main Competitors/Comparables**: SynTouch, PPS Perception Technology, Tashan Technology, LiGan Technology

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_xela`
- Product Entity: `ent_product_xela_uskin`
- Component Entity: `ent_component_xela_uskin_module`
- Key Relationships:
  - `ent_company_xela` -- `manufactures` --> `ent_product_xela_uskin`
  - `ent_company_xela` -- `manufactures` --> `ent_component_xela_uskin_module`
  - `ent_product_xela_uskin` -- `uses` --> `ent_component_xela_uskin_module`

## References

1. [XELA Robotics Official Website](https://www.xelarobotics.com)
2. [XELA Robotics Product Catalog 2025](https://49063741.fs1.hubspotusercontent-na2.net/hubfs/49063741/XELA%20Robotics%20-%20Catalog%202025.pdf)
3. [Engineering.com – uSkin integrated into Tesollo DG-5F](https://www.engineering.com/uskin-tactile-sensors-integrated-into-tesollo-dg-5f-robot-hand/)
4. [XELA Robotics Technology Page](https://xelarobotics.com/technology/)
5. [Appendix D Product Catalog](../index-products.md)
