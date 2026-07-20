# Japan Solderless Terminal Manufacturing / J.S.T.

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 日本压着端子制造 |
| **English Name** | J.S.T. |
| **Headquarters** | Sakai City, Osaka Prefecture, Japan |
| **Founded** | 1957 |
| **Website** | [https://www.jst-mfg.com](https://www.jst-mfg.com) |
| **Supply Chain Segment** | Crimp terminals, connectors, wire harnesses |
| **Enterprise Attribute** | Listed company (TSE Standard: 7701) |
| **Parent Company/Group** | Independently listed |
| **Data Source** | Official website, product datasheets, public information |

## Company Profile

J.S.T. (Japan Solderless Terminal Manufacturing Co., Ltd.) is one of the world's largest manufacturers of crimp terminals and connectors. Standard series such as PH, XH, SM, and ZH are widely used in consumer and industrial electronics, and are also extensively employed for internal signal and power connections in robots.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|-----------------------|-------------------|
| PH Series | 2.0 mm general-purpose connection | JST PH | Small motors, sensors, controllers |
| XH Series | 2.5 mm general-purpose connection | JST XH | Home appliances, robot power supplies |
| SM / VH Series | Wire-to-wire / high current | SM / VH | Batteries, power distribution |

## Representative Products

### JST PH Series 2.0 mm Wire-to-Board Connector

> JST PH Series 2.0 mm Wire-to-Board Connector: Please visit [Official Documentation](https://www.jst-mfg.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Number of Pins | 2 – 16 (selectable) | Official catalog |
| Rated Current | Not disclosed | Official datasheet |
| Rated Voltage | Not disclosed | Official datasheet |
| Protection Rating | IP20 | Product documentation |
| Pitch | 2.0 mm | Official catalog |
| Application Scenarios | Small motors, sensors, controllers, drones | Product documentation |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: Low cost, comprehensive specifications, wide compatibility; one of the most commonly used signal connectors in robotics and model aircraft.

**Application Scenarios**: Robot servos, encoders, LEDs/indicators, low-power fans, sensors.

### JST XH Series 2.5 mm Wire-to-Board Connector

> JST XH Series 2.5 mm Wire-to-Board Connector: Please visit [Official Documentation](https://www.jst-mfg.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Number of Pins | 2 – 20 (selectable) | Official catalog |
| Rated Current | Not disclosed | Official datasheet |
| Rated Voltage | Not disclosed | Official datasheet |
| Protection Rating | IP20 | Product documentation |
| Pitch | 2.5 mm | Official catalog |
| Application Scenarios | Robot power supplies, battery packs, industrial controllers | Product documentation |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: The 2.5 mm pitch carries higher current; simple structure, suitable for power and low-speed signals.

**Application Scenarios**: Robot battery connections, power distribution boards, low-power motors, industrial controllers.

## Supply Chain Position

- **Upstream Key Components/Materials**: Phosphor bronze, brass, PBT/nylon, plating materials, cables
- **Downstream Customers/Application Scenarios**: Consumer electronics, home appliances, automotive, industrial robots, drones
- **Main Competitors/Comparables**: Hirose, Molex, TE Connectivity, Amphenol, JAE

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_jst`
- Product Entity: `ent_product_jst_ph`
- Component Entity: `ent_component_jst_ph`
- Key Relationships:
  - `rel_ent_company_jst_manufactures_ent_product_jst_ph` (`ent_company_jst` → `manufactures` → `ent_product_jst_ph`)
  - `rel_ent_company_jst_manufactures_ent_component_jst_ph` (`ent_company_jst` → `manufactures` → `ent_component_jst_ph`)

## References

1. [Official Website](https://www.jst-mfg.com)
2. Product datasheets and publicly available technical reports
3. [Appendix D Product Catalog](../index-products.md)
