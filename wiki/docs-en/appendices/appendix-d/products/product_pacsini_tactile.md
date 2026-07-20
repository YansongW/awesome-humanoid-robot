# Pacsini DexH13 Tactile Dexterous Hand

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Index](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Pacsini Technology](../companies/company_pacsini.md) |
| **Product Category** | Multi-dimensional tactile + AI vision dual-modal dexterous hand |
| **Release Date** | Continuous iteration since 2024 |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [Pacsini Official Website](https://paxini.com) |

## Product Overview

The Pacsini DexH13 is the world's first four-finger biomimetic dexterous hand integrating "multi-dimensional tactile + AI vision" dual modalities. A single hand integrates 1140 ITPU multi-dimensional tactile sensing units and an 8-megapixel RGB AI hand-eye camera, capable of synchronously capturing 15 types of tactile information including 3D force, 3D torque, contact position, material, temperature, and hardness, achieving 0.01 N level fine force recognition and 1000 Hz data output.

The DexH13 adopts a 4-finger multi-joint biomimetic structure, featuring 16 degrees of freedom (13 active + 3 passive), fingertip force of 15 N, rated load of 5 kg, driven by coreless motors, supporting EtherCAT / Modbus communication, with a service life of 1 million cycles, providing perception capabilities close to human skin for humanoid robots, precision assembly, logistics sorting, and healthcare services.

## Product Image

> Pacsini DexH13: Please visit the [official materials](https://paxini.com) for details.

## Specification Parameter Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Number of Fingers | 4 | Official public information |
| Degrees of Freedom | 16 (13 active + 3 passive) | Official public information |
| Tactile Sensing Units | 1140 ITPU multi-dimensional tactile sensing units | Official public information |
| Tactile Signal Channels | 3420 channels | Official public information |
| Vision Capability | 8-megapixel high-definition RGB AI hand-eye camera | Official public information |
| Tactile Perception Dimensions | 15 types (including 3D force/torque, temperature, material, hardness, rebound, etc.) | Public reports |
| Force Control Resolution | 0.01 N | Public reports |
| Sampling Frequency | 1000 Hz | Public reports |
| Fingertip Force | 15 N | Official public information |
| Rated Load | 5 kg | Official public information |
| Maximum Grasp Diameter | 15 cm | Official public information |
| Minimum Open/Close Time | 1.5 s | Official public information |
| Drive Method | Coreless motor drive | Official public information |
| Communication Protocol | EtherCAT / Modbus | Official public information |
| Service Life | 1 million cycles | Official public information |
| Achievable Actions | Grasping, holding, pinching, pressing, finger opening/closing and other complex human hand actions | Official public information |
| Weight | Not disclosed | - |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Pacsini Technology](../companies/company_pacsini.md)
- **Core Components/Technology Source**: Self-developed 6D Hall array tactile sensing unit (PX-6AX), ITPU tactile chip, AI hand-eye camera and dexterous hand structure; coreless motors and drivers are purchased externally.
- **Downstream Applications/Customers**: Humanoid robot OEMs, automotive OEMs, logistics and warehousing, medical and healthcare, precision manufacturing.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_pacsini_dexh13`
- Manufacturer Entity: `ent_company_pacsini`
- Component Entity: `ent_component_pacsini_px6ax`
- Key Relationships:
  - `rel_ent_company_pacsini_manufactures_ent_product_pacsini_dexh13` (`ent_company_pacsini` → `manufactures` --> `ent_product_pacsini_dexh13`)
  - `rel_ent_product_pacsini_dexh13_uses_ent_component_pacsini_px6ax` (`ent_product_pacsini_dexh13` → `uses` --> `ent_component_pacsini_px6ax`)

## Application Scenarios

- **Humanoid Robot Dexterous Manipulation**: Grasping, twisting, pressing, tool use and other complex human hand actions.
- **Precision Assembly**: Automotive production line plug insertion, screw tightening, flexible object assembly.
- **Logistics and Warehousing**: Flexible sorting and packaging of irregular, fragile, and soft items.
- **Medical and Healthcare**: Assisted grasping, rehabilitation training, prosthetic control.

## Competitive Comparison

| Comparison Item | Pacsini DexH13 | Shadow Hand | Unitree Dex5 |
|----------------|----------------|-------------|--------------|
| Tactile Sensing Units | 1140 | 800 | Up to 500 |
| Degrees of Freedom | 16 (13 active + 3 passive) | 24 | 20 (16 active + 4 passive) |
| Force Control Resolution | 0.01 N | 0.2 N | 0.15 N |
| Sampling Frequency | 1000 Hz | 500 kHz (local) | 200 kHz (local) |
| Core Advantage | Multi-dimensional tactile + AI vision dual modality | High degrees of freedom, mature ecosystem | Flexible movement, cost optimization |

## Selection and Deployment Recommendations

- Before deployment, confirm the robot arm's payload, communication protocol (EtherCAT/Modbus), and power supply interface.
- Tactile data volume is large and requires high real-time performance; it is recommended to reserve sufficient computing power and network bandwidth on the controller side.

## References

1. [Pacsini Technology Official Website](https://paxini.com)
2. [Pacsini DexH13 Product Page](https://paxini.com/cn/dex/gen2)
3. [Science and Technology Daily – BYD Invests in Pacsini](https://www.stdaily.com/web/gdxw/2025-04/28/content_332431.html)
4. [Appendix D Company Directory](../index-companies.md)
