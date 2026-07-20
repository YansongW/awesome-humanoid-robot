---
id: ent_company_nabtesco
schema_version: 1
type: company
title: Nabtesco
domain: 02_components
theoretical_depth: system
names:
  zh: Nabtesco（纳博特斯克）
  en: Nabtesco
status: active
sources:
  - id: src_nabtesco_official
    type: website
    title: Nabtesco Official Website
    url: https://www.nabtesco-motion.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# Nabtesco（纳博特斯克） / Nabtesco

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Nabtesco（纳博特斯克） |
| **English Name** | Nabtesco |
| **Headquarters** | Tokyo, Japan |
| **Founded** | 2003 |
| **Official Website** | [https://www.nabtesco-motion.cn](https://www.nabtesco-motion.cn) |
| **Supply Chain Segment** | RV Reducer / Precision Reducer / Actuator |
| **Enterprise Type** | Foreign Brand, Subsidiary of Nabtesco Corporation |
| **Parent Company/Group** | Nabtesco Corporation |
| **Data Source** | Official Website, Product Manuals, Public Research Reports, WAIC 2026 Coverage |

## Company Profile

Global leader in RV reducers, with cumulative shipments exceeding 7 million units, dominating the heavy-load joint market for industrial robots.

Nabtesco's RV-E, RV-C, and RV-N series RV reducers are renowned for high rigidity, high torque, low backlash, and long service life, widely used in heavy-load joints such as industrial robot bases, arms, and shoulders.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| RV-E Series | Standard RV Reducer | RV-20E / RV-40E / RV-80E | Heavy-load joints of industrial robots |
| RV-N Series | Compact High-Torque RV Reducer | RV-25N / RV-42N | Collaborative/Humanoid Robots |

## Representative Products

### RV-40E-105 RV Reducer / RV-40E-105 Precision Reducer

> RV-40E-105 RV Reducer: Please visit [Official Documentation](https://www.nabtesco-motion.cn) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Outer Diameter | Approx. 105 mm | Nabtesco RV-E Manual |
| Weight | 9.3 kg | Industry Report / Nabtesco Parameter Table |
| Reduction Ratio | 105:1 | Nabtesco Product Page |
| Rated Torque | 412 N·m | Nabtesco Product Page |
| Allowable Starting/Stopping Torque | 1029 N·m | Nabtesco Product Page |
| Instantaneous Maximum Torque | 2058 N·m | Nabtesco Product Page |
| Allowable Output Speed | 70 rpm (100% Duty Cycle) | Nabtesco Product Page |
| Backlash | < 1 arc-min | Nabtesco Product Page |
| Rated Life | 6000 h | Nabtesco Product Page |

**Technical Highlights**: Built-in main bearing, high rigidity, impact resistance; standard choice for industrial robot shoulder/waist joints.

**Application Scenarios**: J1–J3 joints of six-axis industrial robots, waist/hip joints of humanoid robots, heavy-duty positioners.

### RV-20E-81 RV Reducer / RV-20E-81 Precision Reducer

> RV-20E-81 RV Reducer: Please visit [Official Documentation](https://www.nabtesco-motion.cn) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Outer Diameter | Approx. 65 mm | Nabtesco RV-E Manual |
| Weight | Approx. 4.7 kg | Nabtesco Parameter Table |
| Reduction Ratio | 81:1 | Nabtesco Product Page |
| Rated Torque | 167 N·m | Nabtesco Product Page |
| Allowable Starting/Stopping Torque | 412 N·m | Nabtesco Product Page |
| Instantaneous Maximum Torque | 833 N·m | Nabtesco Product Page |
| Allowable Output Speed | 75 rpm (100% Duty Cycle) | Nabtesco Product Page |
| Backlash | < 1 arc-min | Nabtesco Product Page |
| Rated Life | 6000 h | Nabtesco Product Page |

**Technical Highlights**: Medium/small RV reducer, suitable for medium-load robot joints and precision rotary tables.

**Application Scenarios**: SCARA, small six-axis robots, leg joints of humanoid robots, CNC rotary tables.

## Supply Chain Position

- **Upstream Key Components/Materials**: Alloy steel, cycloidal gears, pin housing, bearings, grease
- **Downstream Customers/Application Scenarios**: Big Four industrial robot families, domestic robots, humanoid robot OEMs
- **Main Competitors/Peers**: Shuanghuan Transmission, Zhongda Leader, Sumitomo Heavy Industries

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_nabtesco`
- Product Entities: `ent_component_nabtesco_rv_40e_105`, `ent_component_nabtesco_rv_20e_81`
- Key Relationships:
  - `ent_company_nabtesco` -- `manufactures` --> `ent_component_nabtesco_rv_40e_105`
  - `ent_company_nabtesco` -- `manufactures` --> `ent_component_nabtesco_rv_20e_81`

## References

1. [Official Website](https://www.nabtesco-motion.cn)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.inovance.com) (Please verify against actual product models)
