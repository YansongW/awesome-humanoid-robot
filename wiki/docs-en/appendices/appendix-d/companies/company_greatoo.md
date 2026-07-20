# Greatoo Intelligent Equipment

> This entry belongs to [Appendix D: Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 巨轮智能 |
| **English Name** | Greatoo Intelligent Equipment |
| **Headquarters** | Jieyang, China |
| **Founded** | 2001 |
| **Website** | [http://www.greatoo.com](http://www.greatoo.com) |
| **Supply Chain Segment** | RV Reducer / Tire Mold / Industrial Robot / Precision Machinery |
| **Enterprise Attribute** | Listed Company (SZ.002031), Domestic Brand |
| **Parent Company/Group** | Greatoo Intelligent Equipment Inc. |
| **Data Source** | Official website, annual reports, product manuals, WAIC 2026 reports |

## Company Profile

A key domestic supplier of RV reducers, expanding from tire molds to robot core components.

Greatoo Intelligent Equipment started with tire molds and hydraulic tire vulcanizers, later entering the fields of industrial robots and precision reducers. The company's self-developed RV reducers have achieved mass application and are gradually expanding to humanoid robot joint modules, aiming for domestic substitution of reducers, motors, and drives.

## Product Lines

| Product Line | Positioning | Representative Products | Application Fields |
|--------------|-------------|------------------------|--------------------|
| RV Reducer | Heavy-duty robot joints | JR Series | Industrial robots, humanoid robots |
| Tire Mold | Radial tire mold | Segmented mold, two-half mold | Tire manufacturing |
| Industrial Robot | 6-axis/SCARA | GR Series | Handling, grinding |

## Representative Products

### RV Reducer / Greatoo RV Reducer

> RV Reducer: Please visit [official website](http://www.greatoo.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Dimensions | Outer diameter 110–400 mm (series range) | Product manual |
| Weight | 2–60 kg | Product manual |
| Reduction Ratio | 30–200:1 | Product manual |
| Rated Torque | 50–5,000 N·m | Product manual |
| Torsional Stiffness | Not disclosed | Product manual |
| Backlash | ≤ 1 arc-min | Product manual |
| Transmission Accuracy | ≤ 1 arc-min | Product manual |
| Price | Not disclosed | - |

**Technical Highlights**: Proprietary tooth profile and bearing design, high rigidity, long lifespan, suitable for high-torque joints of heavy-duty industrial robots and humanoid robots.

**Application Scenarios**: Industrial robot base/shoulder/elbow, humanoid robot hip/waist/knee joints, heavy-duty rotary tables.

### Industrial Robot / Greatoo Industrial Robot

> Industrial Robot: Please visit [official website](http://www.greatoo.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Payload | 6–220 kg | Product manual |
| Reach | 700–3,200 mm | Product manual |
| Repeat Positioning Accuracy | ±0.05 mm | Product manual |
| Degrees of Freedom | 6 | Product manual |
| Protection Rating | IP54 | Product manual |
| Application Fields | Handling, palletizing, grinding | Product manual |
| Communication Interface | EtherCAT / Modbus | Product manual |
| Price | Not disclosed | - |

**Technical Highlights**: Co-development of 6-axis robot body and RV reducer, achieving independent control of key components.

**Application Scenarios**: Automotive parts, rubber tires, metal processing, logistics handling.

## Supply Chain Position

- **Upstream Key Components/Materials**: Alloy steel, bearings, lubricants, castings, motors, drives
- **Downstream Customers/Application Scenarios**: Tire factories, industrial robot integrators, humanoid robot OEMs, metal processing
- **Main Competitors/Peers**: Nabtesco, Sumitomo, Qinchuan Machine Tool, Shuanghuan Transmission, Zhongda Leader

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_greatoo`
- Product/Component Entities: `ent_component_greatoo_rv_reducer`, `ent_product_greatoo_industrial_robot`
- Key Relationships:
  - `ent_company_greatoo` -- `manufactures` --> `ent_component_greatoo_rv_reducer`
  - `ent_company_greatoo` -- `manufactures` --> `ent_product_greatoo_industrial_robot`

## References

1. [Official Website](http://www.greatoo.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.inovance.com) (Please verify against actual product models)
