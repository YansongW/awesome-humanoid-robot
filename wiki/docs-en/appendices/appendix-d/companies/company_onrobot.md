# OnRobot (Ang Le) / OnRobot

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | OnRobot (Ang Le) |
| **English Name** | OnRobot |
| **Headquarters** | Odense, Denmark |
| **Founded** | 2015 |
| **Website** | [https://www.onrobot.com](https://www.onrobot.com) |
| **Supply Chain Role** | Collaborative robot end-effectors, six-axis force/torque sensors, electric grippers, vacuum grippers |
| **Enterprise Type** | Private company, leading ecosystem provider for collaborative robot end-effectors |
| **Parent Company/Group** | OnRobot A/S (formerly merged with Perception Robotics, OptoForce) |
| **Data Source** | OnRobot official website, product datasheets, industry reports |

## Company Profile

OnRobot is a one-stop supplier of end-of-arm tooling for Danish collaborative robots, offering force/torque sensors, electric grippers, vacuum grippers, and quick changers.

Headquartered in the Danish robotics cluster of Odense, OnRobot is dedicated to providing a plug-and-play end-effector ecosystem for collaborative robots. Its HEX series six-axis force/torque sensors seamlessly integrate with mainstream collaborative robots such as Universal Robots, FANUC, and KUKA, enabling force-controlled assembly, polishing, testing, and human-robot collaboration. In addition to force sensing products, OnRobot also offers the RG2/RG6 electric grippers, VGC vacuum grippers, Gecko suction cups, and the Quick Changer.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| HEX Force/Torque Sensors | Six-axis force control for robot end-effectors | HEX-E / HEX-H / HEX-E QC | Assembly, polishing, testing |
| Electric Grippers | Adaptive gripping | RG2 / RG6 / RG2-FT | Collaborative robot pick-and-place |
| Vacuum/Soft Grippers | Irregular and thin object grasping | VGC10 / Gecko SP | Logistics, packaging, food |
| Quick Changers | Rapid tool change for end-effectors | Quick Changer | Multi-tool collaborative production lines |

## Representative Products

### OnRobot HEX-E QC Six-Axis Force/Torque Sensor

> OnRobot HEX-E QC Six-Axis Force/Torque Sensor: Please visit the [official page](https://www.onrobot.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | Six-axis force/torque sensor | Official website |
| Force Measurement Range (Fx/Fy/Fz) | ±100 N / ±100 N / ±200 N | Official website/datasheet |
| Torque Measurement Range (Mx/My/Mz) | ±10 Nm / ±10 Nm / ±10 Nm | Official website/datasheet |
| Accuracy | Not disclosed | - |
| Resolution | Not disclosed | - |
| Sampling Frequency | Not disclosed | - |
| Overload Capacity | Approx. 500% FS | Official website/datasheet |
| Protection Rating | IP67 | Official website/datasheet |
| Communication Interface | TCP/IP, USB, EtherNet/IP, PROFINET | Official website/datasheet |
| Integration Interface | Quick Changer / Robot flange | Official website/datasheet |
| Power Supply | 24 V DC | Official website/datasheet |
| Weight | Approx. 350 g | Official website/datasheet |
| Operating Temperature | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: A six-axis force sensing solution optimized for collaborative robots, featuring a built-in Quick Changer interface, supporting plug-and-play with mainstream brands such as UR, FANUC, and KUKA, with an IP67 protection rating.

**Application Scenarios**: Force-controlled assembly for collaborative robots, constant-force grinding/polishing, insertion testing, surface quality inspection, and end-effector force sensing for humanoid robot arms.

### OnRobot RG2-FT Smart Gripper

> OnRobot RG2-FT Smart Gripper: Please visit the [official page](https://www.onrobot.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | Electric gripper with force/torque fingertips | Official website |
| Gripping Stroke | Not disclosed | - |
| Gripping Force | Not disclosed | - |
| Force Sensing | Integrated F/T sensing in fingertips | Official website |
| Price | Not disclosed | - |

**Technical Highlights**: Integrates force/torque and proximity sensing into the fingertips of the electric gripper, enabling more precise grip control.

**Application Scenarios**: Collaborative robot pick-and-place, precision assembly, and grasping of fragile/irregular objects.

## Supply Chain Position

- **Upstream Key Components/Materials**: Aluminum structural parts, force-sensitive elements, signal processing chips, connectors, sealing materials, robot quick-change standard parts
- **Downstream Customers/Application Scenarios**: Collaborative robot users, automotive/3C assembly, humanoid robot arms, logistics packaging, automation integrators
- **Main Competitors/Peers**: ATI Industrial Automation, Robotiq, SCHUNK, Bota Systems, Kunwei Technology, Yuli Instruments

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_onrobot`
- Product Entity: `ent_product_onrobot_hex_e`
- Component Entity: `ent_component_onrobot_hex_e_sensor`
- Key Relationships:
  - `ent_company_onrobot` -- `manufactures` --> `ent_product_onrobot_hex_e`
  - `ent_company_onrobot` -- `manufactures` --> `ent_component_onrobot_hex_e_sensor`
  - `ent_product_onrobot_hex_e` -- `uses` --> `ent_component_onrobot_hex_e_sensor`

## References

1. [OnRobot Official Website](https://www.onrobot.com)
2. [OnRobot HEX-E QC Six-Axis Force/Torque Sensor Product/Data Page](https://www.onrobot.com/en/products/he-x)
3. Company annual reports, product datasheets, and public press releases
4. [Appendix D Product Catalog](../index-products.md)
