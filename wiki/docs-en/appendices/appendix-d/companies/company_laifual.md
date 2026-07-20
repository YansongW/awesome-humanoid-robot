---
id: ent_company_laifual
schema_version: 1
type: company
title: Laifual
domain: 02_components
theoretical_depth: system
names:
  zh: 来福谐波
  en: Laifual
status: active
sources:
  - id: src_laifual_official
    type: website
    title: Laifual Official Website
    url: https://www.laifual.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# Laifual / 来福谐波

> This entry belongs to [Appendix D: Enterprise/Product Wiki](../../appendix-d.md).
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 来福谐波 |
| **English Name** | Laifual |
| **Headquarters** | Shengzhou, Zhejiang, China |
| **Founded** | 2013 |
| **Official Website** | [https://www.laifual.com](https://www.laifual.com) |
| **Supply Chain Role** | Harmonic Reducers / Planetary Reducers / Joint Modules |
| **Enterprise Type** | Domestic Brand, National High-Tech Enterprise |
| **Parent Company/Group** | None (Independent) |
| **Data Sources** | Official Website, Product Manuals, Public Research Reports, WAIC 2026 Coverage |

## Company Overview

One of the main domestic manufacturers of harmonic reducers, with products covering multiple series such as LSS, LSG, LHT, and LHD.

Laifual is engaged in the R&D and manufacturing of high-precision harmonic reducers and planetary reducers. It operates a 30,000-square-meter standard factory. Its products are widely used in industrial robots, service robots, medical equipment, and high-end automation equipment.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| LSS/LSG Cup-Type Harmonic | Standard/High-Torque Harmonic Reducers | LSS-32 / LSG-32 | Robot Joints |
| LHT/LHD Hollow-Type | Hollow/Ultra-Thin Harmonic Reducers | LHT-25 / LHD-32 | Collaborative/Humanoid Robots |

## Representative Products

### LSS-32-100-U-I Harmonic Reducer / LSS-32-100-U-I Harmonic Reducer

> LSS-32-100-U-I Harmonic Reducer: Please visit [Official Materials](https://www.laifual.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Size | 32 | Laifual LSS Datasheet |
| Reduction Ratio | 50/80/100/120:1 | Laifual LSS Datasheet |
| Rated Torque (2000rpm) | 76/118/137/137 N·m | Laifual LSS Datasheet |
| Start/Stop Allowable Torque | 216/304/333/333 N·m | Laifual LSS Datasheet |
| Average Load Allowable Torque | 108/167/216/216 N·m | Laifual LSS Datasheet |
| Instantaneous Maximum Torque | 382/568/647/686 N·m | Laifual LSS Datasheet |
| Maximum Input Speed | 4800 rpm | Laifual LSS Datasheet |
| Backlash | ≤ 20 arcsec | Laifual LSS Datasheet |
| Weight | 3.11 kg | Laifual LSS Datasheet |

**Technical Highlights**: Standard cup-type structure, high-rigidity crossed roller bearing; load capacity and lifespan approach international mainstream levels.

**Application Scenarios**: Industrial robot joints, humanoid robot arms, automation turntables.

### LHD-32-100-U-I Ultra-thin Harmonic Reducer / LHD-32-100-U-I Ultra-thin Harmonic Reducer

> LHD-32-100-U-I Ultra-thin Harmonic Reducer: Please visit [Official Materials](https://www.laifual.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Size | 32 | Laifual Product Page |
| Reduction Ratio | 50/80/100:1 | Laifual Product Page |
| Rated Torque | Not disclosed | - |
| Axial Length | LHD-I is approximately 50% shorter than standard type | Laifual Product Page |
| Structure | Ultra-thin hollow flanged + crossed roller bearing | Laifual Product Page |
| Weight | Not disclosed | - |
| Backlash | ≤ 20 arcsec | Laifual Product Page |

**Technical Highlights**: Ultra-thin, flat design, suitable for robot joints sensitive to axial dimensions and weight.

**Application Scenarios**: Collaborative robot end-effectors, humanoid robot wrists, medical robotic arms.

## Supply Chain Position

- **Upstream Key Components/Materials**: Alloy steel, flexible bearings, lubricating grease, aluminum alloy
- **Downstream Customers/Application Scenarios**: Industrial robot, service robot, medical equipment, and automation equipment manufacturers
- **Main Competitors/Peers**: Leaderdrive, Harmonic Drive Systems, Tongchuan Precision

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_laifual`
- Product Entities: `ent_component_laifual_lss_32_100`, `ent_component_laifual_lhd_32_100`
- Key Relationships:
  - `ent_company_laifual` -- `manufactures` --> `ent_component_laifual_lss_32_100`
  - `ent_company_laifual` -- `manufactures` --> `ent_component_laifual_lhd_32_100`

## References

1. [Official Website](https://www.laifual.com)
2. [WAIC 2026 Exhibition Coverage](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.inovance.com) (Please verify against actual product models)
