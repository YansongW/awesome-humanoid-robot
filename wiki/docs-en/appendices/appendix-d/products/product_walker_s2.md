# UBTECH Walker S2

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Index](../index-products.md)
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [UBTECH](../companies/company_ubtech.md) |
| **Product Category** | Industrial-grade humanoid robot |
| **Release Date** | 2024–2025 |
| **Status** | Mass production / Enterprise delivery |
| **Official Website/Source** | [UBTECH Commercial Website](https://www.commercial.ubtrobot.com/) |

## Product Overview

The UBTECH Walker S2 is the second-generation product of the Walker industrial humanoid robot series, designed for automotive manufacturing, 3C electronics, and logistics warehousing scenarios. The entire machine has 52 degrees of freedom, a maximum payload of 15 kg for both arms, and is equipped with a fourth-generation five-finger dexterous hand and ±162° waist rotation, enabling complex industrial actions such as unpacking, material loading, quality inspection, and spraying.

The core highlight of the Walker S2 is its autonomous battery hot-swap system, which can complete battery replacement within 3 minutes, enabling nearly 24-hour continuous operation. Its perception system includes binocular stereo vision, depth LiDAR, six-axis force sensors, and an IMU, powered by the ROSA 2.0 operating system and a multimodal large model, supporting multi-robot collaboration and MES system integration. The Walker S2 has been deployed and validated on production lines or pilot projects at customers such as NIO, BYD, and Airbus.

## Product Image

> UBTECH Walker S2: Please visit the [official website](https://www.commercial.ubtrobot.com/) for details.

## Specification Parameter Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Dimensions | Approx. 176 cm (height) | Public specification |
| Weight | Approx. 70–75 kg | Varies by configuration source |
| Degrees of Freedom (Total) | 52 DOF | Public specification |
| Key Performance Indicators | Max payload for both arms: 15 kg; Waist rotation: ±162° | Public specification |
| Walking Speed | Approx. 2 m/s (7.2 km/h) | Public specification |
| Battery Life | Approx. 2 hours; Supports hot-swappable battery | Public specification |
| Computing Platform | X86 + NVIDIA Jetson Orin | RBTX product page |
| Price | Not disclosed (Industry estimate: 68,000–120,000 USD) | Third-party estimate |

## Supply Chain Position

- **Manufacturer**: [UBTECH](../companies/company_ubtech.md)
- **Core Components/Technology Sources**: Self-developed integrated joints, NVIDIA Jetson Orin computing platform, binocular stereo vision, depth LiDAR, dexterous hand; some reducers and motors are outsourced.
- **Downstream Applications/Customers**: NIO, BYD, Airbus, pilot projects in Saudi Arabia/Singapore/Japan.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_ubtech_walker_s2`
- Manufacturer Entity: `ent_company_ubtech`
- Key Relationships:
  - `rel_ent_company_ubtech_manufactures_ent_product_ubtech_walker_s2` (`ent_company_ubtech` → `manufactures` → `ent_product_ubtech_walker_s2`)

## Application Scenarios

- **Automotive Manufacturing**: Performs appearance inspection, interior assembly, seatbelt inspection, and material handling at factories like NIO and BYD.
- **3C Electronics**: Precision assembly, screw tightening, component insertion, and AOI re-inspection assistance.
- **Commercial Display**: Exhibition hall explanations, shopping mall tours, and brand event interactive displays.

## Competitive Comparison

| Comparison Item | UBTECH Walker S2 | Tesla Optimus Gen 3 | Figure 02 |
|----------------|------------------|---------------------|-----------|
| Positioning | Industrial humanoid | General/Industrial humanoid | Industrial manufacturing humanoid |
| Total DOF | 52 | 28+ torso + 22×2 hands | 28 |
| Arm Payload | 15 kg | Approx. 20 kg | 25 kg |
| Core Advantages | Factory deployment cases, hot-swappable battery, dexterous hand | Cost target, AI data | Helix VLA, BMW deployment |

## Selection and Deployment Recommendations

- Automotive/3C manufacturing enterprises should focus on evaluating the Walker S2's integration capabilities with existing MES/AGV systems.
- It is recommended to plan battery hot-swap stations and multi-robot collaborative scheduling solutions to leverage the advantage of 24-hour continuous operation.

## References

1. [UBTECH Commercial Website](https://www.commercial.ubtrobot.com/)
2. [Robozaps – UBTECH Walker S Review](https://blog.robozaps.com/b/ubtech-walker-s-review)
3. [Humanoid.Guide – Walker S2](https://humanoid.guide/product/walker-s2/)
4. [RBTX – UBTECH Walker S2 Product Page](https://rbtx.com/en-US/components/humanoid/ubtech-humanoid-walker-s2)
