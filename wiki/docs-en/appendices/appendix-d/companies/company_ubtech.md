# UBTECH Robotics

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 优必选科技 |
| **English Name** | UBTECH Robotics |
| **Headquarters** | Shenzhen, China |
| **Founded** | 2012 |
| **Official Website** | [https://www.ubtrobot.com](https://www.ubtrobot.com) / [commercial.ubtrobot.com](https://www.commercial.ubtrobot.com/) |
| **Supply Chain Role** | Complete Machine OEM / Industrial & Service Humanoid Robots |
| **Enterprise Attribute** | Listed Company (HKEX 09880.HK), National-level Specialized and New "Little Giant" |
| **Parent Company/Group** | None |
| **Data Source** | UBTECH Official Website, HKEX Announcements, IT Home, WAIC Public Reports |

## Company Profile

UBTECH is one of the earliest companies in China to achieve commercial mass production of humanoid robots, positioning itself as a provider of "full-stack humanoid robot technology + industry solutions."

The company started with educational service robots and gradually expanded into AI education, logistics, healthcare, and industrial manufacturing. After listing on the HKEX in 2023, UBTECH has focused on promoting the large-scale deployment of the Walker series in scenarios such as new energy vehicle final assembly and 3C manufacturing, proposing the "Humanoid Robots Entering Factories" strategy.

## Product Lines

| Product Line | Positioning | Representative Products | Application Fields |
|---|---|---|---|
| Industrial Humanoid | 7×24 hour production line operations, autonomous battery swapping | Walker S / S1 / S2 | Automotive final assembly, 3C assembly, logistics sorting |
| Service Humanoid | Reception guidance, education & research | Walker X / Alpha Series | Exhibition halls, education, research |

## Representative Products

### Walker S2

> UBTECH Walker S2: Please visit [Official Materials](https://www.ubtrobot.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | Approx. 176 cm | Third-party distributor materials |
| Weight | Approx. 70 kg | Third-party distributor materials |
| Degrees of Freedom | 52 DOF | Humanoid.Guide / Distributor materials |
| Payload/Torque | Dual-arm payload 15 kg, single hand 7 kg | Distributor public specifications |
| Speed/RPM | Max 2 m/s (approx. 7.2 km/h) | Public reports |
| Battery Life | Approx. 2–2.5 h | Distributor materials |
| Interface/Communication | Wi-Fi | Distributor materials |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: Fourth-generation bionic dual arms, autonomous hot-swappable battery system (officially claims 3-minute battery swap), BrainNet 2.0 + Co-Agent multimodal task planning.

**Application Scenarios**: Sorting and handling in automotive factories, production line loading/unloading, continuous nighttime operations, etc.

### Walker S1

> UBTECH Walker S1: Please visit [Official Materials](https://www.ubtrobot.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | Approx. 172 cm | Public reports |
| Weight | Approx. 65 kg | Public reports |
| Degrees of Freedom | Not disclosed | - |
| Payload/Torque | Not disclosed | - |
| Speed/RPM | Not disclosed | - |
| Battery Life | Not disclosed | - |
| Interface/Communication | Not disclosed | - |
| Price | Not disclosed | Inquire for pricing |

**Technical Highlights**: An early deployment platform for industrial scenarios, sharing some motion control and perception architecture with Walker S2.

**Application Scenarios**: New energy vehicle production line training, collaborative handling in 3C factories.

## Supply Chain Position

- **Upstream Key Components/Materials**: Self-developed servo motors and joint modules; externally purchased harmonic reducers, force sensors, batteries, structural parts (see [Chapter 7 Supplier Map](../../../chapters/chapter-07.md)).
- **Downstream Customers/Application Scenarios**: Manufacturing customers such as BYD, Foxconn, Airbus, Texas Instruments; education, exhibition halls, healthcare institutions.
- **Main Competitors/Peers**: Tesla Optimus, Figure 02, Unitree H1, Fourier GR Series.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_ubtech`
- Product Entities: `ent_product_ubtech_walker_s2`, `ent_product_ubtech_walker_s1`
- Key Relationships:
  - `ent_company_ubtech` -- `manufactures` --> `ent_product_ubtech_walker_s2`
  - `ent_company_ubtech` -- `manufactures` --> `ent_product_ubtech_walker_s1`
  - `ent_product_ubtech_walker_s2` -- `uses` --> `ent_component_lithium_battery`

## References

1. [UBTECH Official Website](https://www.ubtrobot.com)
2. [UBTECH Commercial Robot Official Website](https://www.commercial.ubtrobot.com/)
3. [IT Home – UBTECH Walker S2 Report](https://www.ithome.com)
4. [Humanoid.Guide – UBTECH Walker S2](https://humanoid.guide/product/walker-s2/)
5. [Appendix D.4 Key Product Wiki](../index-products.md)
