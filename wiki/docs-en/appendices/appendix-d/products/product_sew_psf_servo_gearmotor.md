# SEW-EURODRIVE PS.F / PS.C Planetary Servo Gearmotor

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update date: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [SEW-EURODRIVE](../companies/company_sew_eurodrive.md) |
| **Product Category** | Planetary Servo Gearmotor |
| **Release Date** | Current mainstream model |
| **Status** | Mass production / Commercial |
| **Website/Source** | [SEW-EURODRIVE Official Website](https://www.sew-eurodrive.com) |

## Product Overview

The PS.F and PS.C series are low-backlash planetary gearmotors launched by SEW-EURODRIVE for servo applications. The PS.F features a hollow/flange shaft output, while the PS.C offers a B5/B14 flange solid shaft output. Both can form a compact drive unit with CMP synchronous servo motors.

The series covers common integer ratios from 3 to 100, with a maximum output torque of approximately 4,300 N·m and protection rating up to IP65. When paired with SEW inverters, they enable high-precision, high-dynamic position and torque control.

## Product Image

> SEW-EURODRIVE PS.F / PS.C Planetary Servo Gearmotor: Please visit the [official website](https://www.sew-eurodrive.com) for details.

## Specification Table

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Reduction Ratio | 3:1 – 100:1 (integer ratios, fine grading) | Product manual |
| Rated Output Torque | Up to approx. 4,300 N·m (series range) | Product manual |
| Input Speed | Up to 6,000 rpm | Product manual |
| Backlash | ≤3 – 6 arcmin (series/option) | Product manual |
| Protection Rating | IP65 (standard/optional) | Product manual |
| Mounting Type | B5/B14 flange, solid shaft, keyway | Product manual |
| Efficiency | Single stage approx. 97% / Two stage approx. 94% | Product manual |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [SEW-EURODRIVE](../companies/company_sew_eurodrive.md)
- **Core Components/Technology Source**: CMP synchronous servo motor, planetary gears, bearings, seals, brakes, encoders
- **Downstream Applications/Customers**: Industrial robots, humanoid robot joints, AGV wheel drives, packaging and printing equipment

## Knowledge Graph Nodes and Relationships

- Component entity: `ent_component_sew_psf_servo_gearmotor`
- Manufacturer entity: `ent_company_sew_eurodrive`
- Key relationship:
  - `rel_ent_company_sew_eurodrive_manufactures_ent_component_sew_psf_servo_gearmotor` (`ent_company_sew_eurodrive` --> `manufactures` --> `ent_component_sew_psf_servo_gearmotor`)

## Application Scenarios

- **Industrial Robots**: Robot base, shoulder, and wrist joint drives
- **Humanoid Robots**: High-torque joints such as hip, knee, and shoulder
- **CNC Machine Tools**: Machine tool feed, tool magazine, rotary table
- **Other Automation**: Logistics conveying, food packaging, textile machinery

## Competitive Comparison

| Comparison Item | PS.F / PS.C Planetary Servo Gearmotor | Lenze g500 | Bonfiglioli 300M |
|-----------------|----------------------------------------|------------|------------------|
| Core Advantage | Modular planetary + servo motor, global service | Motion control integrated solution | Heavy-duty planetary, wind power experience |
| Backlash/Precision | ≤3–6 arcmin | Low backlash optional | Industrial-grade backlash |
| Price Level | Mid-to-high end | Mid-to-high end | Mid-to-high end |
| Delivery Lead Time | Medium | Medium | Medium |

## Selection and Deployment Recommendations

Choose PS.F or PS.C based on robot joint torque and speed requirements. Pay attention to matching integer reduction ratios with encoder resolution. For high-speed applications, verify thermal power.

## References

1. [SEW-EURODRIVE Official Website](https://www.sew-eurodrive.com)
2. [SEW-EURODRIVE Servo Gearmotors](https://www.sew-eurodrive.com)
3. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
