---
id: ent_company_shuanghuan
schema_version: 1
type: company
title: Shuanghuan Driveline
domain: 02_components
theoretical_depth: system
names:
  zh: 双环传动
  en: Shuanghuan Driveline
status: active
sources:
  - id: src_shuanghuan_official
    type: website
    title: Shuanghuan Driveline Official Website
    url: http://www.shuanghuandrive.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# Shuanghuan Driveline

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 双环传动 |
| **English Name** | Shuanghuan Driveline |
| **Headquarters** | Yuhuan, Zhejiang, China |
| **Founded** | 1980 |
| **Official Website** | [http://www.shuanghuandrive.com](http://www.shuanghuandrive.com) |
| **Supply Chain Segment** | RV Reducer / Harmonic Reducer / Precision Gears |
| **Enterprise Type** | Domestic Brand, Listed Company (002472.SZ) |
| **Parent/Group** | None (independently listed), subsidiary Huandong Technology |
| **Data Source** | Official website, product brochures, public research reports, WAIC 2026 coverage |

## Company Profile

The leading domestic RV reducer subsidiary Huandong Technology specializes in precision gears and robot reducers.

Through its subsidiary Huandong Technology, Shuanghuan Driveline deploys RV reducers, harmonic reducers, and planetary reducers, covering precision reducers required for robots with loads of 3–1000 kg. It has achieved mass supply to leading robot companies such as Unitree.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| SHPR-E RV Reducer | Main bearing built-in type RV | SHPR-40E / SHPR-20E | Heavy-load joints of industrial robots |
| Harmonic/Planetary Reducer | Light-load and humanoid robot joints | Harmonic series / Planetary series | Humanoid robots, collaborative robots |

## Representative Products

### SHPR-40E-121 RV Reducer

> SHPR-40E-121 RV Reducer: Please visit [official materials](http://www.shuanghuandrive.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Model | SHPR-40E-121 | Gearsville product page |
| Reduction Ratio | 121:1 | Gearsville product page |
| Rated Torque | 412 N·m | Gearsville product page |
| Backlash | ≤ 1 arcmin | Gearsville product page |
| Features | Built-in main bearing, high torsional stiffness, compact size | Gearsville product page |
| Application | Industrial robot joints, welding positioners, rotary tables | Gearsville product page |
| Weight | Not disclosed | - |
| Maximum Input Speed | Not disclosed | - |

**Technical Highlights**: Representative model of domestic RV reducers, with performance close to comparable Nabtesco products, offering high cost-effectiveness.

**Application Scenarios**: Six-axis industrial robot J1–J3, humanoid robot waist/hip joints, heavy-duty positioners.

### SHPR-20E RV Reducer

> SHPR-20E RV Reducer: Please visit [official materials](http://www.shuanghuandrive.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Series | SHPR-E | Gearsville product page |
| Reduction Ratio | 57/81/105/121/141/161:1 | Nabtesco RV-E compatible series |
| Rated Torque | Not disclosed | - |
| Backlash | ≤ 1 arcmin | Gearsville product page |
| Structure | Two-stage cycloidal planetary + built-in main bearing | Gearsville product page |
| Features | High rigidity, impact resistance, large reduction ratio | Gearsville product page |

**Technical Highlights**: Medium and small RV reducer, suitable for medium and small load robot joints and precision rotary tables.

**Application Scenarios**: SCARA, collaborative robots, humanoid robot leg joints.

## Supply Chain Position

- **Upstream Key Components/Materials**: Alloy steel, bearings, grease, gear blanks
- **Downstream Customers/Application Scenarios**: Unitree, Estun, EFORT, QJAR Robot, etc.
- **Main Competitors/Benchmarks**: Nabtesco, Zhongda Leader, Qinchuan Machine Tool

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_shuanghuan`
- Product Entities: `ent_component_shuanghuan_shpr_40e_121`, `ent_component_shuanghuan_shpr_20e`
- Key Relationships:
  - `ent_company_shuanghuan` -- `manufactures` --> `ent_component_shuanghuan_shpr_40e_121`
  - `ent_company_shuanghuan` -- `manufactures` --> `ent_component_shuanghuan_shpr_20e`
  - `ent_company_shuanghuan` -- `supplies` --> `ent_company_unitree`

## References

1. [Official Website](http://www.shuanghuandrive.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Brochures and Research Reports](https://www.inovance.com) (Please verify against actual product models)
