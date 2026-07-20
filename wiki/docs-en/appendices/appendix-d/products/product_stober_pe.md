# STOBER PE Series Planetary Gearbox

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Index](../index-products.md)
> Data update date: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [STOBER](../companies/company_stober.md) |
| **Product Category** | Economy Planetary Gearbox |
| **Release Date** | Current main model |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [STOBER Official Website](https://www.stober.com) |

## Product Overview

The STOBER PE series is an economy planetary gearbox designed for cost-sensitive servo applications, featuring helical planetary gears and an integrated motor adapter (MAI). It offers reduction ratios from 3:1 to 100:1 and a rated torque of up to 160 N·m. The series is available in four sizes: PE21, PE31, PE41, and PE51, with backlash <8 arcmin and efficiency of 97% for single-stage and 95% for two-stage.

The PE series has an IP64 protection rating, lifetime lubrication, and a maximum input speed of 8,000 rpm. It is suitable for small to medium-sized robot joints, automation devices, packaging, and medical equipment.

## Product Image

> STOBER PE Series Planetary Gearbox: Please visit the [official documentation](https://www.stober.com) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Reduction Ratio | 3:1 – 100:1 | Product manual |
| Frame Size | PE21 / PE31 / PE41 / PE51 | Product manual |
| Rated Output Torque | Up to 160 N·m | Product manual |
| Acceleration Torque | Up to 310 N·m | Product manual |
| Backlash | <8 arcmin | Product manual |
| Efficiency | 1-stage 97% / 2-stage 95% | Product manual |
| Max Input Speed | Up to 8,000 rpm | Product manual |
| Protection Rating | IP64 | - |

## Supply Chain Position

- **Manufacturer**: [STOBER](../companies/company_stober.md)
- **Core Components/Technology Sources**: Helical planetary gears, bearings, seals, grease, motor adapter flange, aluminum housing
- **Downstream Applications/Customers**: Small to medium-sized robots, automation equipment, packaging, medical, semiconductor

## Knowledge Graph Nodes and Relationships

- Component entity: `ent_component_stober_pe`
- Manufacturer entity: `ent_company_stober`
- Key relationships:
  - `rel_ent_company_stober_manufactures_ent_component_stober_pe` (`ent_company_stober` --> `manufactures` --> `ent_component_stober_pe`)

## Application Scenarios

- **Industrial Robots**: Small industrial robot joints, rotary tables
- **Humanoid Robots**: Low-torque joints or actuators such as fingers/wrists
- **CNC Machine Tools**: Small CNC machines, inspection platforms
- **Other Automation**: Packaging, medical, semiconductor handling

## Competitive Comparison

| Comparison Item | PE Series Planetary Gearbox | Neugart PLE | Apex Dynamics PA II |
|-----------------|-----------------------------|-------------|---------------------|
| Core Advantage | Economy helical, fast delivery | Economy spur gear, brand reputation | Economy helical, cost-effective |
| Backlash/Precision | <8 arcmin | Economy <8 arcmin | 6–12 arcmin |
| Price Level | Mid-range | Mid-range | Mid-range |
| Delivery Time | Relatively short | Medium | Relatively short |

## Selection and Deployment Recommendations

Suitable for medium to low torque servo axes with low backlash requirements; for high-speed applications, verify critical speed and bearing life.

## References

1. [STOBER Official Website](https://www.stober.com)
2. [STOBER PE Series Inline Planetary Gearbox](https://www.stober.com)
3. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
