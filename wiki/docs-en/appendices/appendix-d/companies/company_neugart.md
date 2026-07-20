# Neugart

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 纽卡特 |
| **English Name** | Neugart |
| **Headquarters** | Kippenheim, Germany |
| **Founded** | 1925 |
| **Website** | [https://www.neugart.com](https://www.neugart.com) |
| **Supply Chain Role** | Planetary Gearboxes / Servo Gearboxes / Precision Drives |
| **Company Type** | Family-owned, international precision gear brand |
| **Parent Company/Group** | Independent family-owned company |
| **Data Source** | Official website, product catalogs, WAIC 2026 reports |

## Company Profile

Neugart is a German manufacturer of precision planetary gearboxes. Since launching its first planetary gearbox in 1967, the company has focused on providing gearboxes with high torque density, low backlash, and low noise for servo applications. Its products are known for ground/honed gear technology and the PCS-2 motor adaptation system.

The product line includes the economy series PLE, high-precision series PLN, right-angle series WPLE/WPLN, and the flange output series PLFE, widely used in machine tools, robotics, packaging, medical, and semiconductor equipment.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| High-Precision Planetary Gearboxes | Low backlash / high rigidity | PLN / PLE | Machine tools, robotics |
| Right-Angle Planetary Gearboxes | Compact / right-angle output | WPLE / WPLN | Automation, medical |
| Flange Output Gearboxes | High tilting stiffness | PLFE | Rotary tables, robotics |

## Representative Products

### PLN High-Precision Planetary Gearbox

> PLN High-Precision Planetary Gearbox: Please visit [official documentation](https://www.neugart.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Reduction Ratio | 3:1 – 100:1 | Product catalog |
| Frame Sizes | PLN 070 / 090 / 115 / 142 / 190 | Product catalog |
| Rated Output Torque | 14 – 800 N·m (1-stage); 43 – 2,880 N·m (2-stage) | Product catalog |
| Backlash | Standard <3 arcmin; optional <1 arcmin | Product catalog |
| Efficiency | Up to approx. 98% | Product catalog |
| Protection Class | IP65 | Product catalog |
| Max Input Speed | Up to 8,000 rpm (depending on size) | Product catalog |
| Price | Not disclosed | - |

**Technical Highlights**: Spur gear high-rigidity design, preloaded tapered roller bearings, long centering shoulder, PCS-2 quick motor mounting, lifetime lubrication.

**Applications**: CNC machine tools, industrial robots, humanoid robot joints, semiconductor equipment, medical instruments.

### Other Representative Products

PLE Economy Series: Reduction ratios 3–512, suitable for cost-sensitive multi-axis systems; WPLN Right-Angle High-Precision Series for space-constrained installation scenarios.

## Supply Chain Position

- **Upstream Key Components/Materials**: Bearing steel, precision bearings, seals, grease, motor adapter flanges, aluminum/steel housings
- **Downstream Customers/Applications**: Machine tool OEMs, robot integrators, automation integrators, medical equipment manufacturers
- **Main Competitors/Comparables**: Wittenstein, STOBER, Apex Dynamics, Harmonic Drive

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_neugart`
- Component Entity: `ent_component_neugart_pln`
- Key Relationship:
  - `ent_company_neugart` -- `manufactures` --> `ent_component_neugart_pln`

## References

1. [Neugart Official Website](https://www.neugart.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Neugart Product Catalog](https://www.neugart.com/en/downloads)
