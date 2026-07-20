# SCHUNK SVH 5-Finger Hand

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Table of Contents](../index-products.md)
> Data update date: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [SCHUNK GmbH / SCHUNK GmbH](../companies/company_schunk.md) |
| **Product Category** | Dexterous Hand / End Effector |
| **Release Date** | Current model |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [SCHUNK GmbH Official Website](https://www.schunk.com) |

## Product Overview

The SCHUNK SVH is a five-finger collaborative dexterous hand launched by SCHUNK, and it is the world's first five-finger gripper certified by DGUV for collaborative operation. Its gear/linkage transmission and anti-slip rubber gripping surface design balance safety and grip stability, making it suitable for service robots and collaborative robots.

## Product Image

> SCHUNK SVH 5-Finger Hand: Please visit [Official Materials](https://www.schunk.com) for details.

## Specification Parameter Table

| Specification Item | Value | Remarks/Source |
|--------------------|-------|----------------|
| Dimensions | Total length 242 mm | Public information |
| Weight | 1.3 kg | Public information |
| Number of Fingers | 5 | Public information |
| Degrees of Freedom | 9 (5 fingers each 1 + wrist 4) | Public information |
| Number of Joints | 20 | Public information |
| Number of Motors | 9 | Public information |
| Supply Voltage | DC 24 V | Public information |
| Communication Interface | RS485 | Public information |
| Recommended Payload | Approx. 2.5 kg | Public information |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [SCHUNK GmbH / SCHUNK GmbH](../companies/company_schunk.md)
- **Core Components/Technology Sources**: Motors, reducers, sensors, aluminum alloy/steel components, seals.
- **Downstream Applications/Customers**: Automotive manufacturing, electronic assembly, collaborative robots, logistics, medical.

## Knowledge Graph Nodes and Relationships

- Component Entity: `ent_product_schunk_svh`
- Manufacturer Entity: `ent_company_schunk`
- Key Relationships:
  - `rel_ent_company_schunk_manufactures_ent_product_schunk_svh` (`ent_company_schunk` --> `manufactures` --> `ent_product_schunk_svh`)

## Application Scenarios

- **Service Robots**: Reception, delivery, human-robot interaction
- **Collaborative Robots**: Flexible assembly, collaborative loading/unloading
- **Medical Rehabilitation**: Assisted grasping, rehabilitation training
- **Research**: Multi-finger grasping and collaborative safety studies

## Competitive Comparison

| Comparison Item | This Product | International Brands | Domestic Counterparts |
|-----------------|--------------|---------------------|-----------------------|
| Core Advantage | DGUV certification, collaborative safety, industrial-grade reliability | High-end precision and reliability | Performance competition in the same range |
| Delivery Lead Time | Short / Configurable | Long | Short |
| Service Response | Fast | Medium | Fast |
| Price Level | High-end | High-end | Mid-to-low end |

## Selection and Deployment Recommendations

- When selecting a model, match the appropriate variant based on load, stroke, speed, and precision requirements; contact the manufacturer for customized solutions if necessary.
- Before deployment, it is recommended to perform load inertia identification, stiffness matching, and vibration suppression debugging to ensure compatibility with the overall system.

## References

1. [SCHUNK GmbH Official Website](https://www.schunk.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.schunk.com) (Please verify against the actual product model)
