# RG52-050 Robot Electric Gripper / Junto RG52-050 Electric Gripper

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Junto Robotics](../companies/company_junto.md) |
| **Product Category** | Electric Gripper / End Effector |
| **Release Date** | Current Main Model |
| **Status** | Mass Production / Commercial |
| **Website/Source** | [Junto Robotics Official Website](https://www.jodell.cn) |

## Product Overview

The RG52-050 is a modular robot electric gripper from Junto Robotics' RG series. It features integrated drive and control, electromechanical integration, precise force control, power-off holding, drop detection, and fast networking capabilities, making it suitable for high-speed precision gripping in space-constrained scenarios.

## Product Image

> RG52-050 Robot Electric Gripper: Please visit the [official website](https://www.jodell.cn) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Not disclosed | - |
| Weight | 0.75 kg | Product Manual |
| Degrees of Freedom | 1 DOF (Two-finger Parallel) | Product Manual |
| Adjustable Stroke | 0–52 mm | Product Manual |
| Single Finger Gripping Force | 2–50 N | Product Manual |
| Recommended Payload | 1 kg | Product Manual |
| Open/Close Time | 0.5 s | Product Manual |
| Supply Voltage | DC 24 V | Product Manual |
| Communication Interface | Modbus RTU (RS485) / I/O | Product Manual |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Junto Robotics](../companies/company_junto.md)
- **Core Components/Technology Sources**: Servo motor, reducer, force sensor, aluminum alloy structural parts, control board.
- **Downstream Applications/Customers**: Medical automation, lithium battery, 3C, semiconductor, food industry equipment manufacturers.

## Knowledge Graph Nodes and Relationships

- Component Entity: `ent_product_junto_hand`
- Manufacturer Entity: `ent_company_junto`
- Key Relationships:
  - `rel_ent_company_junto_manufactures_ent_product_junto_hand` (`ent_company_junto` --> `manufactures` --> `ent_product_junto_hand`)

## Application Scenarios

- **Medical Automation**: In vitro diagnostic tube gripping, sample pre-processing, barcode scanning and cap opening
- **3C Electronics**: PCB handling, precision component assembly
- **New Energy**: Lithium battery cell and module sorting
- **Collaborative Robots**: Integration with collaborative arms for flexible loading and unloading

## Competitive Comparison

| Comparison Item | This Product | International Brands | Domestic Counterparts |
|-----------------|--------------|----------------------|-----------------------|
| Core Advantage | Integrated drive and control, modular, fast response, comprehensive service network | High-end precision and reliability | Performance competition in the same range |
| Delivery Lead Time | Short / Configurable | Long | Short |
| Service Response | Fast | Medium | Fast |
| Price Level | Mid-range | High-end | Mid-to-low end |

## Selection and Deployment Recommendations

- When selecting a model, match the appropriate type based on load, stroke, speed, and precision requirements. Contact the manufacturer for customized solutions if necessary.
- Before deployment, it is recommended to perform load inertia identification, stiffness matching, and vibration suppression debugging to ensure compatibility with the overall system.

## References

1. [Junto Robotics Official Website](https://www.jodell.cn)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Manual and Research Reports](https://www.jodell.cn) (Please verify against the actual product model)
