# Johnson Electric

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 德昌电机 |
| **English Name** | Johnson Electric |
| **Headquarters** | Hong Kong, China |
| **Founded** | 1959 |
| **Website** | [https://www.johnsonelectric.com](https://www.johnsonelectric.com) |
| **Supply Chain Role** | Micro Motors / Actuators / Drive Modules |
| **Enterprise Attribute** | Listed Company (HK.0179), International Brand |
| **Parent Company/Group** | Johnson Electric Holdings Limited |
| **Data Source** | Official website, annual reports, product manuals, WAIC 2026 reports |

## Company Overview

A global leading supplier of micro motors and actuators, widely used in automotive, industrial, and medical fields.

Johnson Electric specializes in micro DC motors, actuators, switches, and drive systems, covering automotive electronics, home appliances, industrial automation, medical equipment, and consumer electronics. The company has deep expertise in mass production of micro motors, precision gearboxes, and mechatronic integration. Its products are suitable for applications such as robot end effectors, joint actuation, and sensor feedback.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Micro DC Motors | Brushed/Brushless DC Motors | 300, 500, 700 Series | Automotive, Medical, Consumer Electronics |
| Actuators & Modules | Linear/Rotary Actuators | ECI, Sonic Series | Automotive Seats, Robot Joints |
| Motor Drive Systems | Integrated Drive & Controller | BLDC Drive Board | Industrial, Home Appliances, Robotics |

## Representative Products

### ECI Series Brushless DC Motor / Johnson Electric ECI BLDC Motor

> ECI Series Brushless DC Motor: Please visit [Official Documentation](https://www.johnsonelectric.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Size | Ø22–Ø62 mm (series range) | Product Manual |
| Weight | 50–400 g (depending on model) | Product Manual |
| Rated Voltage | 12–48 VDC | Product Manual |
| Rated Speed | 2,000–10,000 rpm | Product Manual |
| Rated Torque | 5–200 mNm | Product Manual |
| Efficiency | ≥80% | Product Manual |
| Protection Rating | IP40–IP54 | Product Manual |
| Price | Not disclosed | - |

**Technical Highlights**: Brushless design, long life, low EMI, suitable for robot joints and actuators requiring high reliability and low maintenance.

**Application Scenarios**: Humanoid robot joints, collaborative robots, automotive actuators, medical ventilators, automation equipment.

### Micro Actuator / Johnson Electric Micro Actuator

> Micro Actuator: Please visit [Official Documentation](https://www.johnsonelectric.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Size | Not disclosed | Product Manual |
| Weight | Not disclosed | Product Manual |
| Output Force | 5–100 N (depending on model) | Product Manual |
| Stroke | 10–100 mm | Product Manual |
| Supply Voltage | 12–24 VDC | Product Manual |
| Positioning Accuracy | ±0.1 mm | Product Manual |
| Protection Features | Overcurrent, overheat, stall protection | Product Manual |
| Price | Not disclosed | - |

**Technical Highlights**: Integrated motor + gearbox + lead screw, compact design, customizable stroke and interface, suitable for space-constrained actuation mechanisms.

**Application Scenarios**: Robot fingers, smart vehicle cabins, medical pumps and valves, smart home actuators.

## Supply Chain Position

- **Upstream Key Components/Materials**: Magnetic materials, copper wire, silicon steel, plastic pellets, bearings, electronic components
- **Downstream Customers/Application Scenarios**: Automotive OEMs, robot integrators, medical equipment manufacturers, consumer electronics brands
- **Main Competitors/Peers**: Nidec, Mabuchi, Bosch, Moons', Topband

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_johnson_electric`
- Product/Component Entities: `ent_component_johnson_electric_eci_motor`, `ent_component_johnson_electric_micro_actuator`
- Key Relationships:
  - `ent_company_johnson_electric` -- `manufactures` --> `ent_component_johnson_electric_eci_motor`
  - `ent_company_johnson_electric` -- `manufactures` --> `ent_component_johnson_electric_micro_actuator`

## References

1. [Official Website](https://www.johnsonelectric.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.johnsonelectric.com/en/products) (Please verify against actual product models)
