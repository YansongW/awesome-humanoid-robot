# Sanhua Intelligent Controls

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 三花智控 |
| **English Name** | Sanhua Intelligent Controls |
| **Headquarters** | Shaoxing City, Zhejiang Province, China |
| **Founded** | 1994 |
| **Official Website** | [https://www.sanhuaglobal.com](https://www.sanhuaglobal.com) |
| **Supply Chain Segment** | Thermal management, microchannel heat exchangers, electronic expansion valves, robotic electromechanical actuators |
| **Enterprise Attribute** | Listed company (SZ: 002050), global leader in refrigeration and thermal management control components |
| **Parent Company/Group** | Sanhua Holding Group Co., Ltd. |
| **Data Source** | Sanhua Intelligent Controls official website, annual reports, investor relations announcements, public research reports |

## Company Profile

Sanhua Intelligent Controls is a global leader in refrigeration and air conditioning control components and new energy vehicle thermal management. Leveraging its precision valve, pump, and actuator technologies, the company is expanding into robotic thermal management and electromechanical actuators.

The company's core products include electronic expansion valves, four-way valves, solenoid valves, microchannel heat exchangers, electronic water pumps, oil coolers, and integrated thermal management modules for new energy vehicles. With deep expertise in fluid control, precision electromagnetic drives, and thermal management, Sanhua is actively deploying rotary/linear actuators, servo motors, and thermal management components for humanoid robots, establishing partnerships with several leading robotics companies.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Refrigeration and Air Conditioning Control Components | Valves and heat exchangers | Electronic expansion valves, four-way valves, microchannel heat exchangers | Residential/commercial air conditioning, cold chain |
| New Energy Vehicle Thermal Management | Integrated vehicle thermal management | Electronic water pumps, Chiller, integrated modules | New energy vehicles |
| Robotic Actuators and Thermal Management | Electromechanical actuators and joint thermal management for humanoid robots | Rotary/linear actuators, thermal management valves | Humanoid robots, industrial robots |

## Representative Products

### Sanhua Thermal Management Components / Electronic Expansion Valves

> Sanhua Thermal Management Components / Electronic Expansion Valves: Please visit [Official Materials](https://www.sanhuaglobal.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Product Form | Electronic expansion valves, solenoid valves, electronic water pumps, Chiller, heat exchangers | Sanhua official website |
| Control Accuracy | High-precision flow/pressure regulation | Sanhua public materials |
| Working Pressure | 0–4.5 MPa depending on model | Product manual |
| Medium | R134a, R1234yf, coolant, etc. | Sanhua materials |
| Dimensions | Valve body diameter approx. 20–60 mm (depending on model) | Public specifications |
| Weight | Tens of grams to hundreds of grams | Public specifications |
| Lifespan | >100,000 cycles (typical models) | Sanhua public materials |
| Price | Not disclosed | - |

**Technical Highlights**: Global market share leader in electronic expansion valves, precision fluid control capability, scalable to robotic thermal management and actuator cooling.

**Application Scenarios**: New energy vehicle thermal management, energy storage temperature control, data center liquid cooling, robotic joint thermal management.

### Sanhua Robotic Electromechanical Actuators

> Sanhua Robotic Electromechanical Actuators: Please visit [Official Materials](https://www.sanhuaglobal.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Product Form | Rotary actuators, linear actuators (ball screws/push rods) | Investor relations announcements |
| Drive Method | Servo motor + reducer/ball screw | Industry analysis |
| Torque/Thrust | 10–200 N·m / hundreds to thousands of N depending on design | Not disclosed |
| Control Method | Brushless motor + encoder + driver | Not disclosed |
| Cooling Method | Optional liquid cooling/air cooling | Not disclosed |
| Dimensions | Customized per customer design | Not disclosed |
| Weight | Varies by specification | Not disclosed |
| Price | Not disclosed | - |

**Technical Highlights**: Leveraging electromagnetic drive, fluid control, and precision manufacturing capabilities to develop highly integrated robotic actuators; collaborating with multiple leading humanoid robot companies.

**Application Scenarios**: Humanoid robot joints, industrial robots, collaborative robots.

## Supply Chain Position

- **Upstream Key Components/Materials**: Copper, aluminum, rare earth permanent magnets, electronic components, precision machining equipment, sealing materials.
- **Downstream Customers/Application Scenarios**: Tesla, BYD, Midea, Gree, and other automotive and home appliance companies; humanoid robot OEMs.
- **Main Competitors/Peers**: DunAn Environment, Yinlun Co., Ltd.; in the robotic actuator field, peers include Tuopu Group, Leaderdrive.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_sanhua`
- Product Entities: `ent_product_sanhua_thermal`, `ent_product_sanhua_actuator`
- Key Relationships:
  - `ent_company_sanhua` -- `manufactures` --> `ent_product_sanhua_thermal`
  - `ent_company_sanhua` -- `manufactures` --> `ent_product_sanhua_actuator`
  - `ent_product_sanhua_thermal` -- `uses` --> `ent_component_electronic_expansion_valve`
  - `ent_product_sanhua_actuator` -- `uses` --> `ent_component_servo_motor`

## References

1. [Official Website](https://www.sanhuaglobal.com)
2. [Sanhua Intelligent Controls Official Website](https://www.sanhuaglobal.com)
3. Sanhua Intelligent Controls 2024 Annual Report and Investor Communication Minutes
