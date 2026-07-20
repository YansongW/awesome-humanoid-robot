# Lenze

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 伦茨 |
| **English Name** | Lenze |
| **Headquarters** | Aerzen, Germany |
| **Founded** | 1947 |
| **Website** | [https://www.lenze.com](https://www.lenze.com) |
| **Supply Chain Role** | Motion Control / Gearboxes / Servo Drives |
| **Enterprise Attribute** | Family-owned, international motion control brand |
| **Parent Company/Group** | Independent (Lenze SE) |
| **Data Source** | Official website, product catalogs, WAIC 2026 reports |

## Company Profile

Lenze is a German supplier of motion control and automation technology, offering the g500 series modular gearboxes, m850 servo motors, i950/i700 frequency inverters, and an automation platform based on FAST application software. Its g500 series is characterized by standardized interfaces, low backlash, and lifetime lubrication.

The company's products cover the complete motion control chain from mechanical reduction and motor drives to digital production lines, particularly suitable for packaging, logistics, robotics, and machine tool applications.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Modular Gearboxes | Coaxial/Right-angle/Shaft-mounted | g500-H / g500-B / g500-S | Automation, Robotics |
| Servo Motors and Drives | High dynamics/scalable | m850 / i950 / i700 | Packaging, Machine Tools |
| Automation Platform | Motion control software | FAST / Lenze Smart Motor | Production lines, Logistics |

## Representative Products

### g500-H Helical Gearbox

> g500-H Helical Gearbox: Please visit [Official Documentation](https://www.lenze.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Gear Ratio | Up to approx. i=370 (2/3 stages) | Product manual |
| Rated Output Torque | 45 – 20,000 N·m (series range) | Product manual |
| Number of Stages | 2-stage / 3-stage (some 4-stage) | Product manual |
| Backlash | Low backlash design | Product manual |
| Protection Class | Up to IP65 | Product manual |
| Lubrication | Lifetime lubrication (synthetic grease) | Product manual |
| Mounting Type | Foot / Flange / Solid shaft / Hollow shaft | Product manual |
| Price | Not disclosed | - |

**Technical Highlights**: Modular design, plug-and-play with Lenze motors/inverters, standardized shaft and flange dimensions, maintenance-free lifetime lubrication.

**Application Scenarios**: Packaging machinery, conveyor systems, robot joints, machine tool feeds, warehouse logistics.

### Other Representative Products

g500-B Bevel Gearbox: Torque 45–20,000 N·m, maximum gear ratio 360, suitable for right-angle layouts; m850 synchronous servo motor supports high-dynamic applications.

## Supply Chain Position

- **Upstream Key Components/Materials**: Steel, castings, bearings, seals, motors, magnetic materials, power electronics
- **Downstream Customers/Application Scenarios**: Packaging OEMs, robot integrators, logistics integrators, machine tool manufacturers
- **Main Competitors/Benchmarks**: SEW-Eurodrive, Siemens, Bosch Rexroth, STOBER

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_lenze`
- Component Entity: `ent_component_lenze_g500_h`
- Key Relationships:
  - `ent_company_lenze` -- `manufactures` --> `ent_component_lenze_g500_h`

## References

1. [Lenze Official Website](https://www.lenze.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Lenze g500 Product Manual](https://www.lenze.com/en/products/gearmotors/gearmotors/)
