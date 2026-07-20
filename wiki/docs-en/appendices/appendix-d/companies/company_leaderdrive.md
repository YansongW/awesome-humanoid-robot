---
id: ent_company_leaderdrive
schema_version: 1
type: company
title: Leaderdrive
domain: 02_components
theoretical_depth: system
names:
  zh: 绿的谐波
  en: Leaderdrive
status: active
sources:
  - id: src_leaderdrive_official
    type: website
    title: Leaderdrive Official Website
    url: https://www.leaderdrive.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# 绿的谐波 / Leaderdrive

> This entry belongs to [Appendix D: Enterprise/Product Wiki](../../appendix-d.md).
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 绿的谐波 |
| **English Name** | Leaderdrive |
| **Headquarters** | Suzhou, Jiangsu, China |
| **Founded** | 2011 |
| **Website** | [https://www.leaderdrive.com](https://www.leaderdrive.com) |
| **Supply Chain Role** | Harmonic Reducers / Mechatronics / Precision Transmission |
| **Enterprise Type** | Domestic Brand, Listed on STAR Market (688017.SH) |
| **Parent Company/Group** | None (Independently Listed) |
| **Data Sources** | Official Website, Product Manuals, Public Research Reports, WAIC 2026 Coverage |

## Company Overview

A leading domestic manufacturer of harmonic reducers, breaking the long-term monopoly of Japan's Harmonic Drive Systems. Products cover joints for industrial robots and humanoid robots.

Leaderdrive offers the LHS/LCS/LCD series of harmonic reducers and KGM integrated joint modules, featuring independently patented P-type tooth profile. Customers include major domestic robot companies such as Estun, Ubtech, and EFORT.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| LHS/LCS Harmonic Reducers | Standard/Hollow Harmonic Reducers | LHS-32 / LCS-25 | Robot Joints, Rotary Tables |
| LCD Ultra-thin Series | Flat Harmonic Reducers | LCD-14 / LCD-17 | Robot End Effectors, Humanoid Wrists |

## Representative Products

### LHS-32-100 Harmonic Reducer

> LHS-32-100 Harmonic Reducer: Please visit the [official website](https://www.leaderdrive.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Size | 32 (Pitch Circle Diameter) | Leaderdrive Product Manual |
| Reduction Ratio | 50/80/100/120:1 | Leaderdrive Product Manual |
| Rated Torque (2000rpm) | 50/79/91/91 N·m | Leaderdrive Product Manual |
| Allowable Torque at Start/Stop | 143/202/221/235 N·m | Leaderdrive Product Manual |
| Instantaneous Maximum Torque | 255/350/399/423 N·m | Leaderdrive Product Manual |
| Maximum Input Speed | 4500 rpm | Leaderdrive Product Manual |
| Average Input Speed | 3500 rpm | Leaderdrive Product Manual |
| Backlash | ≤ 20 arcsec | Leaderdrive Product Manual |
| Weight | 2.5 kg | Leaderdrive Product Manual |

**Technical Highlights**: High-rigidity hollow structure, high load capacity, long lifespan, suitable for robot shoulder/elbow/wrist joints.

**Application Scenarios**: Industrial robots, humanoid robot joints, collaborative robots, CNC rotary tables.

### LCD-14-100 Ultra-thin Harmonic Reducer

> LCD-14-100 Ultra-thin Harmonic Reducer: Please visit the [official website](https://www.leaderdrive.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Size | 14 | Leaderdrive Product Manual |
| Reduction Ratio | 50/80/100:1 | Leaderdrive Product Manual |
| Rated Torque (2000rpm) | 3.5/5.1/5.1 N·m | Leaderdrive Product Manual |
| Allowable Torque at Start/Stop | 11.4/15/18 N·m | Leaderdrive Product Manual |
| Instantaneous Maximum Torque | 23/29/33 N·m | Leaderdrive Product Manual |
| Maximum Input Speed | 8000/7000/6000 rpm | Leaderdrive Product Manual |
| Backlash | ≤ 20 arcsec | Leaderdrive Product Manual |
| Weight | 0.56/0.48/0.68 kg | Leaderdrive Product Manual |

**Technical Highlights**: Ultra-thin cup-shaped flexspline design, small axial dimensions, lightweight, suitable for robot end effectors and finger joints.

**Application Scenarios**: Collaborative robot end effectors, humanoid robot wrists/fingers, medical robots.

## Supply Chain Position

- **Upstream Key Components/Materials**: Alloy steel (flexspline/rigid spline), flexible bearings, lubricating grease, aluminum
- **Downstream Customers/Application Scenarios**: Robot OEMs such as Estun, Ubtech, EFORT, STEP
- **Main Competitors/Peers**: Harmonic Drive Systems, Laifu Harmonic, Tongchuan Precision

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_leaderdrive`
- Product Entities: `ent_component_leaderdrive_lhs_32_100`, `ent_component_leaderdrive_lcd_14_100`
- Key Relationships:
  - `ent_company_leaderdrive` -- `manufactures` --> `ent_component_leaderdrive_lhs_32_100`
  - `ent_company_leaderdrive` -- `manufactures` --> `ent_component_leaderdrive_lcd_14_100`
  - `ent_company_leaderdrive` -- `supplies` --> `ent_company_estun`
  - `ent_company_leaderdrive` -- `supplies` --> `ent_company_ubtech`

## References

1. [Official Website](https://www.leaderdrive.com)
2. [WAIC 2026 Exhibition Coverage](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.inovance.com) (Please verify against actual product models)
