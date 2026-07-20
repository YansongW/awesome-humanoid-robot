# Tuopu Group

> This entry belongs to [Appendix D: Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 拓普集团 |
| **English Name** | Tuopu Group |
| **Headquarters** | Ningbo, Zhejiang Province, China |
| **Founded** | 1983 |
| **Website** | [https://www.tuopu.com](https://www.tuopu.com) |
| **Supply Chain Role** | Structural parts, precision manufacturing, lightweight chassis, robotic electromechanical actuators |
| **Company Type** | Listed company (SH: 601689), leading Tier 1 automotive parts supplier |
| **Parent Company/Group** | None (independently listed entity) |
| **Data Source** | Tuopu Group official website, annual reports, investor relations announcements, public research reports |

## Company Profile

Tuopu Group is a leading Chinese supplier of automotive NVH, chassis, and lightweight structural parts. It is extending its precision machining, die-casting, and electromechanical integration capabilities into the field of robotic structural parts and actuators.

The company's main products include shock absorbers, interiors, chassis systems, thermal management, automotive electronics, and lightweight body parts, serving major domestic and international new energy vehicle manufacturers. In response to the humanoid robot wave, Tuopu leverages its large-scale die-casting, machining, and assembly capabilities to develop robotic electromechanical actuators, joint module housings, and lightweight structural parts, aiming to become a supplier of core structural parts and actuator assemblies for robots.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| Automotive Chassis/Body Structural Parts | Lightweight and integrated chassis systems | Subframes, control arms, steering knuckles | New energy vehicles, intelligent vehicles |
| Robotic Structural Parts and Actuators | Humanoid robot electromechanical actuators and structural parts | Robot joint housings, lead screw/reducer brackets | Humanoid robots, industrial robots |
| Thermal Management Systems | Vehicle and energy storage thermal management integration | Heat pump assemblies, integrated modules | New energy vehicles, energy storage |

## Representative Products

### Tuopu Robotic Structural Parts / Electromechanical Actuators

> Tuopu Robotic Structural Parts / Electromechanical Actuators: Please visit [official materials](https://www.tuopu.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Product Form | Joint housings, reducer/lead screw brackets, structural frames | Tuopu public materials |
| Material | Aluminum alloy die-casting, high-strength steel, magnesium alloy (depending on the solution) | Industry analysis |
| Manufacturing Process | High-pressure die-casting, CNC precision machining, assembly | Tuopu annual report |
| Dimensions | Vary by joint model | Not disclosed |
| Weight | Varies by structural part specification | Not disclosed |
| Load/Torque | Adapted to customer motor and reducer solutions | Not disclosed |
| Precision | Machining precision depends on drawing requirements | Not disclosed |
| Price | Not disclosed | - |

**Technical Highlights**: Migration of automotive-grade precision manufacturing capabilities, large-scale die-casting and machining, assembly-level delivery, collaborative development with leading automotive/robot customers.

**Application Scenarios**: Humanoid robot joint structural parts, industrial robot actuator housings, new energy vehicle chassis structural parts.

### Tuopu Lightweight Chassis System

> Tuopu Lightweight Chassis System: Please visit [official materials](https://www.tuopu.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Product Form | Integrated die-cast rear compartment/chassis, subframes, control arms | Tuopu official website |
| Material | Heat-treatment-free aluminum alloy, high-strength steel | Tuopu public materials |
| Process | Large-scale die-casting, welding, machining, assembly | Tuopu annual report |
| Weight Reduction Effect | 20%–30% weight reduction compared to traditional steel structures | Industry research reports |
| Dimensions | Customized per vehicle platform | Not disclosed |
| Weight | Customized per vehicle platform | Not disclosed |
| Customer Models | Multiple mainstream new energy vehicle models | Public reports |
| Price | Not disclosed | - |

**Technical Highlights**: Large-scale integrated die-casting, modular chassis design, automotive-grade quality and mass delivery capability.

**Application Scenarios**: New energy passenger car chassis, commercial vehicle chassis, future mobile robot platform structural parts.

## Supply Chain Position

- **Upstream Key Components/Materials**: Aluminum/magnesium alloy ingots, mold steel, die-casting equipment, CNC machine tools, heat treatment and surface treatment materials.
- **Downstream Customers/Application Scenarios**: Tesla, BYD, Geely, NIO, and other automakers; humanoid robot OEMs and Tier 1 suppliers.
- **Main Competitors/Peers**: Wenzhou Co., Ltd., Guangdong Hongtu, IKD; in the field of robotic structural parts, peers include Sanhua Intelligent Controls, Leaderdrive, etc.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_tuopu`
- Product Entities: `ent_product_tuopu_structure`, `ent_product_tuopu_chassis`
- Key Relationships:
  - `ent_company_tuopu` -- `manufactures` --> `ent_product_tuopu_structure`
  - `ent_company_tuopu` -- `manufactures` --> `ent_product_tuopu_chassis`
  - `ent_product_tuopu_structure` -- `uses` --> `ent_component_aluminum_alloy`
  - `ent_product_tuopu_chassis` -- `uses` --> `ent_component_casting_die`

## References

1. [Official Website](https://www.tuopu.com)
2. [Tuopu Group Investor Relations](https://www.tuopu.com)
3. Industry research reports: Supply chain analysis of automotive lightweighting and humanoid robot structural parts
