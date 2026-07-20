# Sanyo SANMOTION R Series Servo Motor

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Sanyo Denki](../companies/company_sanyo_denki.md) |
| **Product Category** | Servo Motor / Precision Motion Core Component |
| **Release Date** | Continuous iteration since the 2010s |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [https://www.sanyodenki.com](https://www.sanyodenki.com) |

## Product Overview

The Sanyo SANMOTION R series is a high-performance AC servo motor designed for semiconductor, medical, robotics, and precision automation equipment, with a power range covering 10 W to 5 kW.

The product features miniaturization, high responsiveness, low cogging torque, and high-resolution encoders, making it suitable for applications with limited space, high precision, and high dynamic response. The SANMOTION R series, paired with Sanyo's R ADVANCED servo drives, provides reliable precision motion solutions for fine joints such as fingers and wrists in humanoid robots.

## Product Image

> Sanyo SANMOTION R: Please visit the [official website](https://www.sanyodenki.com) for details.

## Specification Table

| Specification Item | Value | Notes/Source |
|--------------------|-------|--------------|
| Product Form | AC Servo Motor | Sanyo Official Website |
| Frame Size | 20–130 mm (varies by model) | Product Manual |
| Rated Power | 10 W – 5 kW | Product Manual |
| Rated Speed | 1000–6000 rpm | Product Manual |
| Maximum Torque | Not disclosed (varies by model) | Product Manual |
| Encoder | 20-bit absolute (reference) | Product Manual |
| Protection Class | IP65 (some models) | Product Manual |
| Insulation Class | Class F (reference) | Product Manual |
| Price | Not disclosed | Requires inquiry |

## Supply Chain Position

- **Manufacturer**: [Sanyo Denki](../companies/company_sanyo_denki.md)
- **Core Components/Technology Source**: Self-developed motor design and manufacturing process; rare earth magnetic materials, bearings, encoder chips, copper wire, and insulation materials are externally sourced.
- **Downstream Applications/Customers**: Semiconductor equipment manufacturers, medical robot manufacturers, humanoid robot integrators, collaborative robots, precision positioning platforms.

## Knowledge Graph Nodes and Relationships

- Component Entity: `ent_component_sanyo_sanmotion_r_motor`
- Manufacturer Entity: `ent_company_sanyo_denki`
- Key Relationships:
  - `rel_ent_company_sanyo_denki_manufactures_ent_component_sanyo_sanmotion_r_motor` (`ent_company_sanyo_denki` → `manufactures` → `ent_component_sanyo_sanmotion_r_motor`)
  - `ent_component_sanyo_sanmotion_r_drive` -- `uses` --> `ent_component_sanyo_sanmotion_r_motor`

## Application Scenarios

- **Semiconductor Equipment**: Wafer transfer, precision positioning, pick-and-place machines.
- **Medical Robots**: Fine joints in surgical robots and rehabilitation robots.
- **Humanoid Robots**: Space-constrained joints such as fingers, wrists, and heads.
- **Collaborative Robots**: Lightweight joint modules.

## Competitive Comparison

| Comparison Item | Sanyo SANMOTION R | Yaskawa Σ-7 | Panasonic A6 |
|-----------------|-------------------|-------------|--------------|
| Positioning | Miniaturized high-precision servo motor | High-end general-purpose servo | High-speed response servo |
| Frame Size | 20–130 mm | 20–180 mm | 20–180 mm |
| Encoder | 20-bit absolute (reference) | 24-bit absolute | 23-bit absolute |
| Core Advantage | Miniaturization, low noise, high reliability | High-end precision and reliability | High speed and high response |

## Selection and Deployment Recommendations

- Select the frame size and speed based on installation space, load inertia, and dynamic response requirements.
- It is recommended to pair with the Sanyo R ADVANCED series drive for optimal performance.
- For applications such as humanoid robot fingers, focus on evaluating low-speed smoothness and encoder resolution.

## Related Entries

- [Manufacturer: Sanyo Denki](../companies/company_sanyo_denki.md)
- [Appendix D.4 Key Product Wiki](../index-products.md)

## References

1. [Sanyo Denki Official Website](https://www.sanyodenki.com)
2. Sanyo SANMOTION R Series Product Manual
3. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
