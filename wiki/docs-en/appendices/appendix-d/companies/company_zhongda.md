---
id: ent_company_zhongda
schema_version: 1
type: company
title: Zhongda Smart Transmission
domain: 02_components
theoretical_depth: system
names:
  zh: 中大力德
  en: Zhongda Smart Transmission
status: active
sources:
  - id: src_zhongda_official
    type: website
    title: Zhongda Smart Transmission Official Website
    url: https://www.zd-drivers.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# Zhongda Smart Transmission

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 中大力德 |
| **English Name** | Zhongda Smart Transmission |
| **Headquarters** | Cixi, Zhejiang, China |
| **Founded** | 1998 |
| **Official Website** | [https://www.zd-drivers.com](https://www.zd-drivers.com) |
| **Supply Chain Segment** | Planetary Reducer / RV Reducer / Harmonic Reducer / Motor Drive |
| **Enterprise Type** | Domestic Brand, Listed Company (002896.SZ) |
| **Parent Company/Group** | None (Independently Listed) |
| **Data Source** | Official Website, Product Manuals, Public Research Reports, WAIC 2026 Coverage |

## Company Overview

One of the few domestic enterprises that simultaneously mass-produces planetary, RV, and harmonic reducers, as well as integrated intelligent actuation units.

Zhongda Smart Transmission has built an integrated product architecture of "reducer + motor + drive," with products including precision planetary reducers, RV reducers, harmonic reducers, and servo motors. It has supplied core transmission components to robotics companies such as Unitree.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| ZDE/ZDF Precision Planetary Reducers | Economical Precision Planetary | 40ZDE / 60ZDE / 80ZDE | Automation, Robot Joints |
| RV/Harmonic Reducers | Heavy/Light Load Robot Joints | RVE / RVC / Harmonic Series | Industrial Robots, Humanoid Robots |

## Representative Products

### 40ZDE-10 Precision Planetary Gearbox

> 40ZDE-10 Precision Planetary Gearbox: Please visit [Official Documentation](https://www.zd-drivers.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Frame Size | 40 | Zhongda Planetary Reducer Manual |
| Reduction Ratio | 10:1 (Single Stage) | Zhongda Planetary Reducer Manual |
| Output Torque | 4–6 N·m | Wukuang Securities Research Report (citing Zhongda Official Website) |
| Backlash | < 12 arcmin | Zhongda Manual |
| Full Load Efficiency | 96% | Zhongda Manual |
| Weight | 0.4 kg | Zhongda Manual |
| Housing Length | 39 mm | Zhongda Manual |
| Protection Class | IP54 | Zhongda Manual |
| Design Life | 20,000 h | Zhongda Manual |

**Technical Highlights**: Compact structure, high transmission efficiency, low cost, suitable for small-load robot joints and automation modules.

**Application Scenarios**: AGV wheels, collaborative robot joints, humanoid robot fingers/wrists, 3C automation.

### RVE/RVC Series RV Reducer

> RVE/RVC Series RV Reducer: Please visit [Official Documentation](https://www.zd-drivers.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Series | RVE / RVC | Comparison from Huandong Technology Prospectus |
| Transmission Ratio Range | 26–192.4:1 | Huandong Technology Prospectus |
| Rated Torque Range | 58.8–4900 N·m | Huandong Technology Prospectus |
| Backlash | < 1.5 arcmin | Huandong Technology Prospectus |
| Transmission Error | < 90 arcsec | Huandong Technology Prospectus |
| Rated Efficiency | > 78% | Huandong Technology Prospectus |
| Application | Industrial Robots, Machine Tools, Medical Equipment | Zhongda Annual Report |

**Technical Highlights**: High rigidity, high torque, suitable for heavy-load joints such as industrial robot bases and upper arms.

**Application Scenarios**: Industrial Robot J1–J3, Humanoid Robot Waist/Hip, Heavy-Duty Automation Equipment.

## Supply Chain Position

- **Upstream Key Components/Materials**: Alloy Steel, Aluminum, Bearings, Magnetic Materials, Copper Wire, Driver Chips
- **Downstream Customers/Application Scenarios**: Unitree, Agibot, Industrial Robot OEMs
- **Main Competitors/Peers**: Shuanghuan Transmission, Nabtesco, Leaderdrive

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_zhongda`
- Product Entities: `ent_component_zhongda_40zde_10`, `ent_component_zhongda_rv_series`
- Key Relationships:
  - `ent_company_zhongda` -- `manufactures` --> `ent_component_zhongda_40zde_10`
  - `ent_company_zhongda` -- `manufactures` --> `ent_component_zhongda_rv_series`
  - `ent_company_zhongda` -- `supplies` --> `ent_company_unitree`

## References

1. [Official Website](https://www.zd-drivers.com)
2. [WAIC 2026 Exhibition Coverage](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.inovance.com) (Please verify against actual product models)
