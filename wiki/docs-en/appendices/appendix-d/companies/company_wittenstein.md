# WITTENSTEIN alpha

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 威腾斯坦 |
| **English Name** | WITTENSTEIN alpha |
| **Headquarters** | Igersheim, Germany |
| **Founded** | 1949 |
| **Official Website** | [https://www.wittenstein.de](https://www.wittenstein.de) |
| **Supply Chain Role** | Precision Gearboxes / Servo Actuators / Electromechanical Drive Systems |
| **Enterprise Attribute** | Family-owned, International Brand |
| **Parent Company/Group** | WITTENSTEIN SE (Independent Family-owned Company) |
| **Data Source** | Official Website, Product Manuals, WAIC 2026 Reports |

## Company Profile

WITTENSTEIN alpha is a high-end brand under the German WITTENSTEIN SE, specializing in precision servo gearboxes and electromechanical actuators. With low-backlash planetary gearboxes, high-rigidity bearings, and modular motor interfaces, alpha products are widely used in high-dynamic, high-precision motion control applications.

The company offers SP+, TP+, XP+, NPL, CPS series planetary gearboxes, as well as Servo Actuator electromechanical actuators and rack/pinion linear systems. Its engineering tool cymex® supports drive system selection and lifetime calculation.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Planetary Gearboxes | Low Backlash / High Rigidity | SP+ / TP+ / XP+ | Machine Tools, Robotics |
| Electromechanical Actuators | Integrated Linear/Rotary Drive | Servo Actuator | Medical, Automation |
| Linear Drive Systems | Rack & Pinion / Gearboxes | alpha Rack & Pinion | Gantry, Robotics |

## Representative Products

### SP+ Low-Backlash Planetary Gearbox

> SP+ Low-Backlash Planetary Gearbox: Please visit [Official Documentation](https://www.wittenstein.de) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Reduction Ratio | 3:1 – 100:1 | Product Manual |
| Frame Size | 7 sizes (MF) | Product Manual |
| Max Output Torque | 48 – 5,700 N·m | Product Manual |
| Max Input Speed | Up to 8,500 rpm | Product Manual |
| Backlash | Standard ≤3 arcmin / Reduced ≤1 arcmin | Product Manual |
| Torsional Stiffness | 550 N·m/arcmin | Product Manual |
| Max Tilting Moment | 5,000 N·m | Product Manual |
| Price | Not disclosed | - |

**Technical Highlights**: Helical gears, constant low backlash, high torque density, tapered roller bearings for axial/radial loads, multiple output options.

**Application Scenarios**: Industrial robot joints, humanoid robot joints, machine tool feed axes, packaging machinery, medical equipment.

### Other Representative Products

TP+ HIGH TORQUE Series: Reduction ratio 22–302.5, max torque 315–22,000 N·m, suitable for high-rigidity positioning; alpha Servo Actuator integrated actuators for linear/rotary motion.

## Supply Chain Position

- **Upstream Key Components/Materials**: High-strength alloy steel, precision bearings, special lubricants, motors, sensors
- **Downstream Customers/Application Scenarios**: Machine tool OEMs, industrial robots, humanoid robot integrators, medical and packaging equipment manufacturers
- **Main Competitors/Benchmarks**: Neugart, STOBER, Apex Dynamics, Harmonic Drive, Nabtesco

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_wittenstein`
- Component Entity: `ent_component_wittenstein_sp_plus`
- Key Relationship:
  - `ent_company_wittenstein` -- `manufactures` --> `ent_component_wittenstein_sp_plus`

## References

1. [WITTENSTEIN Official Website](https://www.wittenstein.de)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [WITTENSTEIN alpha SP+ Technical Data](https://alpha.wittenstein.de/en-en/products/sp-planetary-gearbox/)
