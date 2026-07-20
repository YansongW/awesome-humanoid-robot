# Apptronik / Apptronik

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Apptronik |
| **English Name** | Apptronik |
| **Headquarters** | Austin, Texas, USA |
| **Founded** | 2016 |
| **Website** | [https://apptronik.com](https://apptronik.com) |
| **Supply Chain Role** | General-purpose humanoid robots, NASA collaboration background |
| **Enterprise Type** | Startup |
| **Parent Company/Group** | None |
| **Data Source** | Apptronik official website, Apollo product page, public funding and collaboration reports |

## Company Overview

Apptronik grew out of the NASA Valkyrie project. Apollo is positioned for industrial logistics and manufacturing, supporting modular bases and hot-swappable batteries.

Apollo adopts a modular design, with the upper body mountable on bipedal legs, a wheeled base, or a fixed pedestal to suit different operational scenarios. The company collaborates with Mercedes-Benz, GXO, NASA, and others on pilot programs.

Apptronik's history can be traced back to NASA's Valkyrie humanoid robot project. The team has accumulated experience in space-grade actuators, high-power-density joints, and safe collaborative control. In addition to the complete Apollo robot, Apptronik also provides custom actuators and joint modules to third parties.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Apollo Humanoid Robot | Industrial/Logistics Humanoid | Apollo | Manufacturing, Warehousing, Logistics |
| Apollo Software Stack | Mission Planning & Human-Robot Interaction | Apptronik SDK | On-site deployment, rapid task switching |
| Robot Actuators/Joints | Core Components | Custom Actuators | Third-party robots, Aerospace |

## Representative Product

### Apptronik Apollo

> Apptronik Apollo: Please visit [Official Information](https://apptronik.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 173 cm (height) | Public information |
| Weight | Approx. 72.6–73 kg | Public information |
| Degrees of Freedom | 71 | Public information |
| Payload/Torque | Approx. 25 kg | Public information |
| Speed/Rotation Speed | Approx. 3.4–5.4 km/h (varying sources) | Public information |
| Battery Life | Approx. 4 hours per battery, hot-swap supports 22 hours/day | Public information |
| Interface/Communication | NVIDIA Jetson AGX Orin + Orin NX, Apptronik SDK | Public information |
| Price | Not disclosed (scaling target < 50,000 USD) | Public reports |

**Technical Highlights**: High payload, hot-swappable batteries, modular mobile base (bipedal/wheeled/pedestal), force-controlled safety architecture, NASA collaboration background.

**Application Scenarios**: Automotive manufacturing, warehouse handling, logistics kitting, aerospace and terrestrial applications.

Apollo's force control architecture and modular base allow it to switch between bipedal, wheeled, and fixed pedestal configurations based on mission requirements, reducing deployment and retrofitting costs. Its software stack supports natural language commands and vision-guided grasping, enabling rapid deployment by non-expert operators.

> Note: Apollo is currently available only through enterprise pilot programs. Specific pricing requires direct contact with Apptronik.

## Supply Chain Position

- **Upstream Key Components/Materials**: NVIDIA computing platform, motors/linear actuators, sensors, structural parts.
- **Downstream Customers/Application Scenarios**: Mercedes-Benz, GXO Logistics, NASA, Google.
- **Main Competitors/Comparables**: Tesla Optimus, Figure 02, Boston Dynamics Atlas, Agility Robotics Digit.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_apptronik`
- Product/Platform Entity: `ent_product_apptronik_apollo`
- Key Relationship:
  - `rel_ent_company_apptronik_manufactures_ent_product_apptronik_apollo` (`ent_company_apptronik` → `manufactures` → `ent_product_apptronik_apollo`)

## References

1. [Apptronik Official Website](https://apptronik.com)
2. [Apptronik Apollo Product Page](https://apptronik.com/apollo)
3. [RoboZaps Apptronik Apollo Review](https://blog.robozaps.com/b/apptronik-apollo-review)
