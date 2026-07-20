# Renishaw

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 雷尼绍 |
| **English Name** | Renishaw |
| **Headquarters** | Gloucestershire, UK (Wotton-under-Edge) |
| **Founded** | 1973 |
| **Website** | [https://www.renishaw.com](https://www.renishaw.com) |
| **Supply Chain Role** | Precision measurement, encoders, machine tool probes, additive manufacturing, medical instruments |
| **Enterprise Attribute** | Publicly traded company (LSE: RSW), global leader in metrology and motion control feedback |
| **Parent Company/Group** | Independently listed |
| **Data Source** | Renishaw official website, product datasheets, installation guides |

## Company Overview

Renishaw is a multinational engineering technology company specializing in high-precision measurement and motion control feedback technology. Its products include coordinate measuring machine probes, machine tool probes, RESOLUTE absolute optical encoders, additive manufacturing systems, and neurosurgical medical equipment, widely used in machine tools, semiconductors, robotics, and aerospace.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Encoder Systems | High-precision position feedback | RESOLUTE / ATOM / TONiC | Machine tools, robotics, semiconductors |
| Machine Tool Probes | On-machine measurement and alignment | RMP60 / OMP60 | CNC machining |
| Coordinate Measurement & Calibration | Probes and software | SP25 / REVO | CMM, robot calibration |
| Additive Manufacturing & Medical | Metal 3D printing, neurosurgical equipment | RenAM / neuroinspire | Aerospace, medical |

## Representative Products

### Renishaw RESOLUTE Absolute Optical Encoder

> Renishaw RESOLUTE Absolute Optical Encoder: Please visit [Official Documentation](https://www.renishaw.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | True absolute optical encoder | Renishaw datasheet |
| Grating Pitch | 30 µm | Renishaw datasheet |
| Resolution | Up to 1 nm | Renishaw datasheet |
| Accuracy | ±1 µm/m (RELA) / ±5 µm/m (RTLA) | Renishaw datasheet |
| Maximum Speed | Up to 100 m/s | Renishaw datasheet |
| Subdivision Error (SDE) | ±40 nm | Renishaw datasheet |
| Jitter | 7 nm RMS | Renishaw datasheet |
| Interface | BiSS C / DRIVE-CLiQ / FANUC / Mitsubishi / Panasonic | Renishaw datasheet |
| Protection Rating | IP64 | Renishaw datasheet |
| Operating Temperature | 0°C – +55°C | Renishaw datasheet |
| Functional Safety | Optional SIL2 / PL d | Renishaw datasheet |
| Price | Not disclosed | - |

**Technical Highlights**: True absolute position feedback, 1 nm resolution, 100 m/s high speed, multi-protocol support, optional functional safety.

**Application Scenarios**: High-precision CNC machine tools, linear motors, robot joints, semiconductor equipment, coordinate measuring machines, astronomical telescopes.

### Renishaw RMP60 Wireless Machine Tool Probe

> Renishaw RMP60 Wireless Machine Tool Probe: Please visit [Official Documentation](https://www.renishaw.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | Radio trigger probe | Renishaw official website |
| Transmission | 2.4 GHz radio | Renishaw official website |
| Application | CNC on-machine measurement, alignment | Renishaw official website |
| Price | Not disclosed | - |

**Technical Highlights**: 360° transmission, anti-interference, improving machining accuracy and automation level.

**Application Scenarios**: CNC machining centers, lathe on-machine measurement.

## Supply Chain Position

- **Upstream Key Components/Materials**: Optical readheads, glass/steel/low-expansion alloy scales, ASICs, cables and connectors
- **Downstream Customers/Application Scenarios**: Machine tool OEMs, robot manufacturers, semiconductor equipment, CMM manufacturers, aerospace
- **Main Competitors/Peers**: Heidenhain, Mitutoyo, Fagor Automation, Newall

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_renishaw`
- Product Entity: `ent_product_renishaw_resolute_encoder`
- Component Entity: `ent_component_renishaw_resolute_readhead`
- Key Relationships:
  - `ent_company_renishaw` -- `manufactures` --> `ent_product_renishaw_resolute_encoder`
  - `ent_company_renishaw` -- `manufactures` --> `ent_component_renishaw_resolute_readhead`
  - `ent_product_renishaw_resolute_encoder` -- `uses` --> `ent_component_renishaw_resolute_readhead`

## References

1. [Renishaw Official Website](https://www.renishaw.com)
2. [Renishaw RESOLUTE Absolute Optical Encoder Product/Documentation Page](https://www.renishaw.com/en/resolute-absolute-encoder--9533)
3. Company annual reports, product datasheets, and public press releases
4. [Appendix D Product Catalog](../index-products.md)
