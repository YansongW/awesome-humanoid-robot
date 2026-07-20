---
id: ent_company_hcfa
schema_version: 1
type: company
title: HCFA
domain: 02_components
theoretical_depth: system
names:
  zh: 禾川科技
  en: HCFA
status: active
sources:
  - id: src_hcfa_official
    type: website
    title: HCFA Official Website
    url: https://www.hcfa.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# HCFA

> This entry belongs to [Appendix D: Enterprise/Product Wiki](../../appendix-d.md).
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 禾川科技 |
| **English Name** | HCFA |
| **Headquarters** | Longyou, Zhejiang, China |
| **Founded** | 2011 |
| **Official Website** | [https://www.hcfa.cn](https://www.hcfa.cn) |
| **Supply Chain Role** | Servo Systems / Motors / Drives / Controllers |
| **Enterprise Type** | Domestic Brand, Listed Company (688320.SH) |
| **Parent Company/Group** | None (Independently Listed) |
| **Data Sources** | Official Website, Product Manuals, Public Research Reports, WAIC 2026 Coverage |

## Company Overview

A domestic supplier of general-purpose servo systems and robot core components, providing servo motors, drives, PLCs, and integrated joint modules.

HCFA's X3E/X5E series servo systems cover 100 W–7.5 kW, support EtherCAT, PROFINET, CANopen, and other fieldbuses, with encoders up to 20-bit. Products are widely used in robotics, photovoltaics, lithium batteries, and logistics automation.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|-------------------------|-------------------|
| X3E Servo System | Economy General-Purpose Servo | SV-X3E + X3E Motor | Robotics, 3C, Photovoltaics |
| X5E Servo System | High-Performance Fieldbus Servo | SV-X5E | Lithium Batteries, Semiconductors, Humanoid Robots |

## Representative Products

### X3E Series Servo Motor

> X3E Series Servo Motor: Please visit [Official Materials](https://www.hcfa.cn) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Power Range | 50 W – 2 kW | HCFA X3E Manual |
| Rated Speed | 3000 rpm | HCFA X3E Manual |
| Encoder | 17-bit Absolute Magnetic / Incremental | HCFA X3E Manual |
| Protection Rating | IP65 | HCFA Corporate Announcement |
| Rated Torque | Not disclosed | - |
| Overload Capacity | Not disclosed | - |
| Voltage Level | AC 200–230 V | HCFA X3E Manual |

**Technical Highlights**: Economical, high-reliability servo motor suitable for general automation and robot joints.

**Application Scenarios**: 3C Automation, Packaging Machinery, AGVs, Collaborative Robots.

### SV-X5E Servo Drive

> SV-X5E Servo Drive: Please visit [Official Materials](https://www.hcfa.cn) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Power Range | 100 W – 7.5 kW | HCFA 2024 Annual Report |
| Voltage Level | 220 V / 380 V | HCFA 2024 Annual Report |
| Communication Protocols | EtherCAT / PROFINET / CANopen / Modbus | HCFA 2024 Annual Report |
| Control Mode | Pulse / Fieldbus / Full Closed-Loop | HCFA 2024 Annual Report |
| Safety Functions | STO, Dynamic Braking, Stall Protection | HCFA 2024 Annual Report |
| Protection | Independent Air Duct, Conformal Coating | HCFA 2024 Annual Report |

**Technical Highlights**: High-performance fieldbus servo drive supporting multi-axis coordination and high-speed robot response.

**Application Scenarios**: Industrial Robots, Humanoid Robots, Lithium Battery/Photovoltaic Production Lines, High-End CNC.

## Supply Chain Position

- **Upstream Key Components/Materials**: Rare Earth Magnets, IGBT, PCB, Chips, Structural Parts
- **Downstream Customers/Application Scenarios**: Industrial Robot, Humanoid Robot, Photovoltaic, Lithium Battery, Logistics Equipment Manufacturers
- **Main Competitors/Peers**: Inovance, Leadshine, Yaskawa, Panasonic

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_hcfa`
- Product Entities: `ent_component_hcfa_x3e_motor`, `ent_component_hcfa_x5e_drive`
- Key Relationships:
  - `ent_company_hcfa` -- `manufactures` --> `ent_component_hcfa_x3e_motor`
  - `ent_company_hcfa` -- `manufactures` --> `ent_component_hcfa_x5e_drive`

## References

1. [Official Website](https://www.hcfa.cn)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.inovance.com) (Please verify against actual product models)
