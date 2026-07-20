---
id: ent_company_maxon
schema_version: 1
type: company
title: Maxon Motor
domain: 02_components
theoretical_depth: system
names:
  zh: Maxon Motor
  en: Maxon Motor
status: active
sources:
  - id: src_maxon_official
    type: website
    title: Maxon Motor Official Website
    url: https://www.maxongroup.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# Maxon Motor / Maxon Motor

> This entry belongs to [Appendix D: Company/Product Wiki](../../appendix-d.md).
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Maxon Motor |
| **English Name** | Maxon Motor |
| **Headquarters** | Sachseln, Switzerland |
| **Founded** | 1961 |
| **Official Website** | [https://www.maxongroup.com](https://www.maxongroup.com) |
| **Supply Chain Role** | Motors / Drives / Precision Motion Control |
| **Company Type** | Foreign Brand, Swiss Listed |
| **Parent Company/Group** | maxon Group |
| **Data Sources** | Official website, product catalogs, public research reports, WAIC 2026 coverage |

## Company Overview

A global leader in precision DC motors and drive systems, renowned for high torque density and low cogging torque in brushless DC motors.

Maxon Motor offers brushed/brushless DC motors, gearboxes, encoders, and controllers, widely used in medical, aerospace, robotics, and industrial automation. Its EC-i series iron-core brushless motors, known for high dynamic response and compact design, are commonly employed in collaborative robot and humanoid robot joint drives.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| EC-i / EC Brushless Motors | High torque density servo motors | EC-i 40 / EC 40 | Robot joints, AGVs, medical devices |
| ECX SPEED / ESK Motors | Ultra-high-speed brushless motors | ECX SPEED 16 | Surgical tools, aerospace actuators |

## Representative Products

### EC-i 40 Brushless DC Motor / EC-i 40 Brushless DC Motor

> EC-i 40 Brushless DC Motor: Please visit the [official page](https://www.maxongroup.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Ø40 × 52 mm (reference) | maxon product page |
| Weight | 390 g | maxon product page 488607 |
| Rated Power | 100 W | maxon product page |
| Rated Torque | 224 mNm | maxon product page |
| Stall Torque | 2080 mNm | maxon product page |
| Rated Speed | 4390 rpm | maxon product page |
| Max Speed | 8000 rpm | maxon product page |
| Efficiency | 89% | maxon product page |
| Encoder | Hall sensors, optional encoder | maxon product page |

**Technical Highlights**: Iron-core winding, high torque density, low cogging torque, suitable for compact integration in robot joints.

**Application Scenarios**: Collaborative robot joints, exoskeletons, AGV drive wheels, precision automation equipment.

### EC 40 Brushless DC Motor / EC 40 Brushless DC Motor

> EC 40 Brushless DC Motor: Please visit the [official page](https://www.maxongroup.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Ø40 mm | TraceParts |
| Weight | 390 g | TraceParts |
| Rated Power | 120 W | TraceParts 118896 |
| Rated Torque | 124 mNm | TraceParts |
| Stall Torque | 1280 mNm | TraceParts |
| Rated Speed | 9280 rpm | TraceParts |
| Max Speed | 18000 rpm | TraceParts |
| Efficiency | 84% | TraceParts |
| Operating Temperature | -20 ~ +125 °C | TraceParts |

**Technical Highlights**: High-speed brushless motor, ideal for precision transmission scenarios requiring high speed and small size.

**Application Scenarios**: Medical handheld tools, optical stages, small drones, robot end effectors.

## Supply Chain Position

- **Upstream Key Components/Materials**: Rare earth permanent magnets (NdFeB), copper wire, silicon steel sheets, bearings, aluminum housing
- **Downstream Customers/Application Scenarios**: Collaborative robot, humanoid robot OEMs, medical devices, aerospace manufacturers
- **Main Competitors/Peers**: Kollmorgen, Inovance Technology, Hechuan Technology, Moons' Industries

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_maxon`
- Product Entities: `ent_component_maxon_ec_i_40`, `ent_component_maxon_ec_40`
- Key Relationships:
  - `ent_company_maxon` -- `manufactures` --> `ent_component_maxon_ec_i_40`
  - `ent_company_maxon` -- `manufactures` --> `ent_component_maxon_ec_40`

## References

1. [Official Website](https://www.maxongroup.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Catalogs and Research Reports](https://www.inovance.com) (Please verify against actual product models)
