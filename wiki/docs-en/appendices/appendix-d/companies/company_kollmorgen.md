---
id: ent_company_kollmorgen
schema_version: 1
type: company
title: Kollmorgen
domain: 02_components
theoretical_depth: system
names:
  zh: Kollmorgen
  en: Kollmorgen
status: active
sources:
  - id: src_kollmorgen_official
    type: website
    title: Kollmorgen Official Website
    url: https://www.kollmorgen.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# Kollmorgen / Kollmorgen

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Kollmorgen |
| **English Name** | Kollmorgen |
| **Headquarters** | Radford, Virginia, USA |
| **Founded** | 1916 |
| **Official Website** | [https://www.kollmorgen.com](https://www.kollmorgen.com) |
| **Supply Chain Segment** | Servo Motors / Frameless Torque Motors / Motion Control |
| **Enterprise Type** | Foreign Brand, under Regal Rexnord |
| **Parent Company/Group** | Regal Rexnord |
| **Data Source** | Official website, product manuals, public research reports, WAIC 2026 coverage |

## Company Overview

A global leader in motion control, TBM/KBM frameless torque motors are widely used in robot joints and precision rotary tables.

Kollmorgen offers frameless torque motors, servo motors, drives, and motion controllers. The TBM2G series is specifically designed for collaborative robot and humanoid robot joints, featuring low cogging, high torque density, and low-voltage operation below 48 V.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| TBM2G Frameless Motor | Next-generation robot joint motor | TBM2G-050 / TBM2G-115 | Collaborative/Humanoid robot joints |
| AKM Servo Motor | High-performance servo motor | AKM24 / AKM32 | Industrial automation, CNC |

## Representative Products

### TBM2G-050 Frameless Motor / TBM2G-050 Frameless Motor

> TBM2G-050 Frameless Motor: Please visit [Official Documentation](https://www.kollmorgen.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Outer Diameter | 50 mm | Kollmorgen / INMOCO |
| Weight | Not disclosed | - |
| Continuous Torque | 0.27 N·m | INMOCO 2022 |
| Rated Speed | 8000 rpm | INMOCO 2022 |
| Output Power | 0.205 kW | INMOCO 2022 |
| Voltage | ≤ 48 VDC | Kollmorgen |
| Feedback | Optional integrated Hall sensors | Kollmorgen |
| Motor Constant | 0.061 N·m/√W | INMOCO 2022 |

**Technical Highlights**: Designed for 3–15 kg collaborative robots, low cogging, high responsiveness, compatible with harmonic drive dimensions.

**Application Scenarios**: Collaborative robot joints, humanoid robot forearm/wrist, precision rotary tables.

### TBM2G-115 Frameless Motor / TBM2G-115 Frameless Motor

> TBM2G-115 Frameless Motor: Please visit [Official Documentation](https://www.kollmorgen.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Outer Diameter | 115 mm | Kollmorgen / INMOCO |
| Weight | Not disclosed | - |
| Continuous Torque | 6.03 N·m | INMOCO 2022 |
| Rated Speed | 3100 rpm | INMOCO 2022 |
| Output Power | 1.43 kW | INMOCO 2022 |
| Voltage | ≤ 48 VDC | Kollmorgen |
| Feedback | Optional integrated Hall sensors | Kollmorgen |
| Motor Constant | 0.802 N·m/√W | INMOCO 2022 |

**Technical Highlights**: High-torque frameless motor, can be directly embedded into robot shoulder/hip joints, supporting high-load dynamic motion.

**Application Scenarios**: Large industrial robot joints, humanoid robot waist/hip, heavy-duty collaborative robots.

## Supply Chain Position

- **Upstream Key Components/Materials**: Rare earth magnets, silicon steel sheets, copper wire, insulation materials, bearings
- **Downstream Customers/Application Scenarios**: Collaborative robots, humanoid robots, aerospace, medical device OEMs
- **Main Competitors/Peers**: Maxon, Inovance Technology, Hechuan Technology, Parker

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_kollmorgen`
- Product Entities: `ent_component_kollmorgen_tbm2g_050`, `ent_component_kollmorgen_tbm2g_115`
- Key Relationships:
  - `ent_company_kollmorgen` -- `manufactures` --> `ent_component_kollmorgen_tbm2g_050`
  - `ent_company_kollmorgen` -- `manufactures` --> `ent_component_kollmorgen_tbm2g_115`

## References

1. [Official Website](https://www.kollmorgen.com)
2. [WAIC 2026 Exhibition Coverage](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.inovance.com) (Please verify against actual product models)
