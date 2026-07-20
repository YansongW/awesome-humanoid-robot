# Galbot

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 银河通用机器人 |
| **English Name** | Galbot |
| **Headquarters** | Beijing, China |
| **Founded** | 2023 |
| **Website** | [https://www.galbot.com](https://www.galbot.com) |
| **Supply Chain Role** | Complete Machine OEM / Wheeled Dual-Arm Humanoid Robot |
| **Enterprise Attribute** | Startup, Peking University Background, Embodied Intelligence Large Model |
| **Parent Company/Group** | None |
| **Data Source** | Galbot Official Website, User Manual, East Money Information, WAIC Reports |

## Company Profile

Galbot was founded by a team with a Peking University background, proposing the "Embodied Intelligence Large Model + Wheeled Humanoid" route, with the Galbot G1 as its core product.

The G1 adopts a 360° omnidirectional wheel chassis and a foldable torso, emphasizing generalized manipulation capabilities in structured scenarios such as retail, healthcare, and industry. It has also collaborated with Stanford University to develop the Open6DOR simulation platform.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Wheeled Humanoid | Retail Sorting, Home Service, Medical Assistance | Galbot G1 | Micro-fulfillment Centers, Pharmacies, Supermarkets, Homes |
| Service Robot | Reception, Delivery | Galbot S1 | Exhibition Halls, Hospitals |

## Representative Products

### Galbot G1

> Galbot G1: Please visit the [official materials](https://www.galbot.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Dimensions | 173 cm (maximum, standard posture) | Galbot Official Website / User Manual |
| Weight | Approx. 92.5 kg (complete machine) | Galbot User Manual |
| Degrees of Freedom | 24 DOF (excluding end-effectors) | Galbot User Manual |
| Payload/Torque | Single arm end payload 5 kg, dual arms combined 10 kg | Galbot User Manual |
| Speed/Rotation | Chassis max 1.5 m/s | Galbot User Manual |
| Battery Life | Approx. 8 h (48 V / 30 Ah battery) | Galbot User Manual |
| Interface/Communication | Wi-Fi 2.4/5 GHz, Bluetooth 5.2, USB3.0, HDMI | Galbot User Manual |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: 360° omnidirectional wheel chassis, torso lift 65 cm, 0–2.1 m vertical workspace, NVIDIA AGX Orin 64 GB (275 TOPS), GroceryVLA embodied large model.

**Application Scenarios**: Unmanned pharmacy drug sorting, supermarket shelf restocking, micro-fulfillment center picking, home service.

### Galbot S1

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Dimensions | Not disclosed | - |
| Weight | Not disclosed | - |
| Degrees of Freedom | Not disclosed | - |
| Payload/Torque | Not disclosed | - |
| Speed/Rotation | Not disclosed | - |
| Battery Life | Not disclosed | - |
| Interface/Communication | Not disclosed | - |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: Wheeled service robot platform, designed for light interaction scenarios such as reception and delivery.

**Application Scenarios**: Exhibition halls, hospitals, office spaces.

## Supply Chain Position

- **Upstream Key Components/Materials**: NVIDIA Orin computing platform, omnidirectional wheel chassis, harmonic/planetary reducers, vision sensors.
- **Downstream Customers/Application Scenarios**: Pharmaceutical retail, supermarkets, tertiary hospitals, industrial manufacturing (e.g., Baida Precision).
- **Main Competitors/Comparables**: Zhiyuan A2-W, LimX Dynamics CL-1, collaborative robot + AMR combination solutions.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_galbot`
- Product Entity: `ent_product_galbot_g1`
- Key Relationships:
  - `ent_company_galbot` -- `manufactures` --> `ent_product_galbot_g1`
  - `ent_product_galbot_g1` -- `uses` --> `ent_component_nvidia_jetson_agx_orin`

## References

1. [Galbot Official Website](https://www.galbot.com)
2. [Galbot G1 Product Page](https://www.galbot.com/g1)
3. [Galbot G1 Quick User Manual](https://www.robotsj.cn/shiyongshouce/1654.html)
4. [East Money Information – Galbot Humanoid Robot Layout](https://finance.eastmoney.com/)
5. [Appendix D.4 Key Product Wiki](../index-products.md)
