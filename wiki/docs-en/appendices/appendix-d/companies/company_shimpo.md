# Nidec-Shimpo

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Nidec-Shimpo |
| **English Name** | Nidec-Shimpo Corporation |
| **Headquarters** | Kyoto, Japan |
| **Founded** | 1952 |
| **Official Website** | [https://www.nidec-shimpo.com](https://www.nidec-shimpo.com) |
| **Supply Chain Role** | Reducers / Transmission Components / Motor Modules |
| **Company Type** | Listed company (TYO.7735 subsidiary), international brand |
| **Parent Company/Group** | Nidec Corporation |
| **Data Source** | Official website, annual reports, product manuals, WAIC 2026 reports |

## Company Overview

A globally renowned manufacturer of precision reducers and ceramic equipment, best known for the VRSF planetary gearbox series.

Nidec-Shimpo specializes in precision planetary gearboxes, harmonic drives, servo motors, and mechatronic modules. Its products are known for high precision, low backlash, and high torque density, and are widely used in industrial robots, collaborative robots, semiconductor equipment, and humanoid robot joints. After joining the Nidec Group in 2003, Shimpo has continued to expand in the direction of motor-reducer integration.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Planetary Gearboxes | Precision low-backlash reduction | VRSF series, VRS series | Industrial robots, humanoid robots |
| Harmonic Drives | Zero-backlash precision transmission | FLEXWAVE series | Collaborative robots, semiconductors |
| Servo Motor Modules | Motor + reducer integration | Smart Flex series | Robot joints, automation |

## Representative Products

### VRSF Series Planetary Gearbox / Nidec-Shimpo VRSF Planetary Gearbox

> VRSF series planetary gearbox: Please visit the [official page](https://www.nidec-shimpo.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Size | 40–200 mm frame size (series range) | Product manual |
| Reduction Ratio | 3:1 – 100:1 | Product manual |
| Rated Output Torque | 5–3,000 N·m | Product manual |
| Backlash | ≤ 3 arcmin (standard) / ≤ 1 arcmin (precision) | Product manual |
| Transmission Efficiency | ≥90% | Product manual |
| Input Speed | Up to 6,000 rpm | Product manual |
| Protection Rating | IP54–IP65 | Product manual |
| Price | Not disclosed | - |

**Technical Highlights**: Helical planetary structure, low backlash, high rigidity, suitable for high-dynamic, high-precision positioning in robot joints and servo systems.

**Application Scenarios**: Humanoid robot joints, industrial robots, collaborative robots, semiconductor equipment, CNC machine tools.

### FLEXWAVE Harmonic Drive / Nidec-Shimpo FLEXWAVE Harmonic Drive

> FLEXWAVE harmonic drive: Please visit the [official page](https://www.nidec-shimpo.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Size | 8–100 mm outer diameter (series range) | Product manual |
| Reduction Ratio | 30:1 – 320:1 | Product manual |
| Rated Output Torque | 0.5–500 N·m | Product manual |
| Backlash | ≤ 1 arcmin | Product manual |
| Transmission Efficiency | ≥80% | Product manual |
| Input Speed | Up to 6,500 rpm | Product manual |
| Design Life | 7,000–10,000 h | Product manual |
| Price | Not disclosed | - |

**Technical Highlights**: Cup/hat-shaped flexspline design, zero backlash, high reduction ratio, suitable for robot end-effector joints and precision rotary stages.

**Application Scenarios**: Collaborative robot joints, humanoid robot wrists/fingers, semiconductor rotary tables, medical robots.

## Supply Chain Position

- **Upstream Key Components/Materials**: Bearings, gear steel, lubricants, seals, motors (supplied within the group)
- **Downstream Customers/Application Scenarios**: Industrial robot manufacturers, humanoid robot integrators, semiconductor equipment suppliers, machine tool manufacturers
- **Main Competitors/Peers**: Harmonic Drive, Nabtesco, Leaderdrive, Laifual Drive, Zhongda Leader

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_shimpo`
- Product/Component Entities: `ent_component_shimpo_vrsf_gearbox`, `ent_component_shimpo_flexwave_harmonic`
- Key Relationships:
  - `ent_company_shimpo` -- `manufactures` --> `ent_component_shimpo_vrsf_gearbox`
  - `ent_company_shimpo` -- `manufactures` --> `ent_component_shimpo_flexwave_harmonic`

## References

1. [Official Website](https://www.nidec-shimpo.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.nidec-shimpo.com/products/) (Please verify against actual product models)
