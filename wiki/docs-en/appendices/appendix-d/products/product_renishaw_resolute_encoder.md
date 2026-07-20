# Renishaw RESOLUTE Absolute Encoder

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Renishaw](../companies/company_renishaw.md) |
| **Product Category** | Absolute optical encoder (Linear/Rotary) |
| **Release Date** | Continuously available/iterated |
| **Status** | Mass production/Commercial |
| **Official Website/Source** | [Renishaw RESOLUTE Absolute Encoder Product/Data Page](https://www.renishaw.com/en/resolute-absolute-encoder--9533) |

## Product Overview

RESOLUTE is a true absolute optical encoder system launched by Renishaw. It uses a single-track 30 µm pitch scale and advanced optical readhead to determine the absolute position instantly upon power-up. The system offers a maximum resolution of 1 nm, a maximum speed of 100 m/s, and supports multiple serial interfaces such as BiSS C, DRIVE-CLiQ, FANUC, and Mitsubishi. It is widely used in high-precision machine tools, robot joints, and semiconductor equipment.

## Product Image

> Renishaw RESOLUTE Absolute Encoder: Please visit the [official page](https://www.renishaw.com/en/resolute-absolute-encoder--9533) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | True absolute optical encoder | Renishaw datasheet |
| Scale pitch | 30 µm | Renishaw datasheet |
| Resolution | Up to 1 nm | Renishaw datasheet |
| Accuracy | ±1 µm/m (RELA) / ±5 µm/m (RTLA) | Renishaw datasheet |
| Maximum speed | Up to 100 m/s | Renishaw datasheet |
| Sub-divisional error (SDE) | ±40 nm | Renishaw datasheet |
| Jitter | 7 nm RMS | Renishaw datasheet |
| Interface | BiSS C / DRIVE-CLiQ / FANUC / Mitsubishi / Panasonic | Renishaw datasheet |
| Ingress protection | IP64 | Renishaw datasheet |
| Operating temperature | 0°C – +55°C | Renishaw datasheet |
| Functional safety | Optional SIL2 / PL d | Renishaw datasheet |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [Renishaw](../companies/company_renishaw.md)
- **Core Components/Technology Source**: Optical readhead, glass/steel/low-expansion alloy scale, ASIC, cables and connectors
- **Downstream Applications/Customers**: Machine tool OEMs, robot manufacturers, semiconductor equipment, CMM manufacturers, aerospace

## Knowledge Graph Nodes and Relationships

- Product entity: `ent_product_renishaw_resolute_encoder`
- Component entity: `ent_component_renishaw_resolute_readhead`
- Manufacturer entity: `ent_company_renishaw`
- Key relationships:
  - `rel_ent_company_renishaw_manufactures_ent_product_renishaw_resolute_encoder` (`ent_company_renishaw` → `manufactures` → `ent_product_renishaw_resolute_encoder`)
  - `rel_ent_company_renishaw_manufactures_ent_component_renishaw_resolute_readhead` (`ent_company_renishaw` → `manufactures` → `ent_component_renishaw_resolute_readhead`)
  - `ent_product_renishaw_resolute_encoder` -- `uses` --> `ent_component_renishaw_resolute_readhead`

## Application Scenarios

- **High-precision CNC machine tools, linear motors, robot joints, semiconductor equipment, coordinate measuring machines, astronomical telescopes**

## Competitive Comparison

| Comparison Item | This Product | Main Competitor A | Main Competitor B |
|-----------------|--------------|-------------------|-------------------|
| Type | See specification table | Similar product | Similar product |
| Core Advantage | Official publicly available performance indicators | Competitor's public indicators | Competitor's public indicators |
| Ecosystem/Service | Official manufacturer support | Competitor ecosystem | Competitor ecosystem |

## Selection and Deployment Recommendations

- Select the specific model based on the resolution, range, accuracy, or computational requirements of the target application.
- Before deployment, confirm that the interface, power supply, cooling, mechanical installation, and ambient temperature range are compatible.
- It is recommended to obtain the latest firmware, SDK, and technical support through official channels or authorized distributors.

## Related Entries

- [Manufacturer: Renishaw](../companies/company_renishaw.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [Renishaw Official Website](https://www.renishaw.com)
2. [Renishaw RESOLUTE Absolute Encoder Product/Data Page](https://www.renishaw.com/en/resolute-absolute-encoder--9533)
3. Product datasheet and public technical reports
4. [Appendix D Company Directory](../index-companies.md)
