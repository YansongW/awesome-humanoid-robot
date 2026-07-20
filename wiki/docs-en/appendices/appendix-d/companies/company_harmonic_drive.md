---
id: ent_company_harmonic_drive
schema_version: 1
type: company
title: Harmonic Drive Systems
domain: 02_components
theoretical_depth: system
names:
  zh: Harmonic Drive Systems
  en: Harmonic Drive Systems
status: active
sources:
  - id: src_harmonic_drive_official
    type: website
    title: Harmonic Drive Systems Official Website
    url: https://www.harmonicdrive.net
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# Harmonic Drive Systems / Harmonic Drive Systems

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Harmonic Drive Systems |
| **English Name** | Harmonic Drive Systems |
| **Headquarters** | Azumino City, Nagano Prefecture, Japan |
| **Founded** | 1970 |
| **Official Website** | [https://www.harmonicdrive.net](https://www.harmonicdrive.net) |
| **Supply Chain Role** | Harmonic Reducer / Precision Reducer / Rotary Actuator |
| **Enterprise Attribute** | Foreign Brand, Japanese Listed Company |
| **Parent Company/Group** | Harmonic Drive Systems Inc. |
| **Data Source** | Official Website, Product Manuals, Public Research Reports, WAIC 2026 Coverage |

## Company Profile

The inventor and leader of global harmonic drives, known for zero backlash, high torque density, and long service life.

Harmonic Drive Systems offers CSF/CSG and SHF/SHG series harmonic reducers, as well as the FHA-C integrated rotary actuator. It is a core transmission component supplier for industrial robots, semiconductor equipment, and humanoid robot joints.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|-------------------------|-------------------|
| CSF/CSG Component Type | Standard/High Torque Harmonic Reducer | CSF-32 / CSG-32 | Robot Joints, Rotary Tables |
| SHF/SHG Hollow Type | Hollow Shaft Harmonic Reducer | SHF-32 / SHG-32 | Collaborative Robots, Humanoid Robots |

## Representative Products

### CSF-32-50-2A-GR Harmonic Drive / CSF-32-50-2A-GR Harmonic Drive

> CSF-32-50-2A-GR Harmonic Drive: Please visit [Official Documentation](https://www.harmonicdrive.net) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Outer Diameter | 110 mm | Electromate |
| Length | 44 mm | Electromate |
| Weight | 0.89 kg | Electromate |
| Reduction Ratio | 50:1 | Electromate |
| Maximum Continuous Torque | 76 N·m | Electromate |
| Maximum Input Speed | 7000 rpm | Electromate |
| Backlash | ≤ 1 arc-min | Electromate |
| Mounting Method | Flange Output / Component Type | Electromate |

**Technical Highlights**: S tooth profile, zero backlash, component-type design for easy integration into robot joints.

**Application Scenarios**: Industrial robot wrists, humanoid robot forearms/wrists, semiconductor rotary tables.

### SHF-32-120 Harmonic Drive / SHF-32-120 Harmonic Drive

> SHF-32-120 Harmonic Drive: Please visit [Official Documentation](https://www.harmonicdrive.net) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Outer Diameter | 147 mm | Amazon Product Page |
| Thickness | 65.5 mm | Amazon Product Page |
| Weight | 1.665 kg | Amazon Product Page |
| Reduction Ratio | 50/80/100/120:1 | Amazon Product Page |
| Rated Torque (at 2000 rpm) | 72/112/130/130 N·m | Amazon Product Page |
| Peak Torque | 363/540/635/652 N·m | Amazon Product Page |
| Maximum Input Speed | 4500 rpm | Amazon Product Page |
| Backlash | 10–20 arcsec | Amazon Product Page |

**Technical Highlights**: Large hollow shaft structure for easy cable routing, suitable for collaborative and humanoid robot joints.

**Application Scenarios**: Collaborative robot shoulders/elbows, humanoid robot waist/hips, medical robots.

## Supply Chain Position

- **Upstream Key Components/Materials**: Alloy Steel (Flexspline/Circular Spline), Crossed Roller Bearings, Grease, Aluminum Housing
- **Downstream Customers/Application Scenarios**: Industrial Robots, Humanoid Robots, Semiconductor Equipment, Medical Robot OEMs
- **Main Competitors/Comparables**: Leaderdrive, Laifual Drive, Nabtesco, Shimpo

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_harmonic_drive`
- Product Entities: `ent_component_harmonic_csf_32_50`, `ent_component_harmonic_shf_32_120`
- Key Relationships:
  - `ent_company_harmonic_drive` -- `manufactures` --> `ent_component_harmonic_csf_32_50`
  - `ent_company_harmonic_drive` -- `manufactures` --> `ent_component_harmonic_shf_32_120`

## References

1. [Official Website](https://www.harmonicdrive.net)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.inovance.com) (Please verify against actual product models)
