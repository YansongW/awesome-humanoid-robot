# CATL / Contemporary Amperex Technology Co., Limited

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 宁德时代新能源科技股份有限公司 |
| **English Name** | Contemporary Amperex Technology Co., Limited (CATL) |
| **Headquarters** | Ningde City, Fujian Province, China |
| **Founded** | 2011 |
| **Website** | [https://www.catl.com](https://www.catl.com) |
| **Supply Chain Segment** | Power batteries, energy storage batteries, battery management systems (BMS) |
| **Enterprise Attribute** | Listed company (Shenzhen Stock Exchange: 300750) |
| **Parent Company/Group** | None (independently listed) |
| **Data Sources** | Company website, 2022 Qilin Battery launch event, industry teardown reports |

## Company Profile

CATL is one of the world's largest power battery manufacturers, ranking first globally in power battery installation volume for eight consecutive years.

The company's main business covers power battery systems, energy storage systems, and battery materials. Core customers include Tesla, BMW, NIO, Volkswagen, Ford, Hyundai, and other major global automakers. In the humanoid robot field, high-energy-density, high-safety battery packs are a key bottleneck for overall endurance and lightweight design. CATL's CTP/CTC technology can provide a reference for robot chassis integration.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Power Batteries | High-energy-density battery packs for passenger/commercial vehicles | Qilin Battery (CTP 3.0) | Electric vehicles, humanoid robot platforms |
| Energy Storage Batteries | Large-capacity, long-life electrochemical energy storage | EnerC / EnerOne | Grid energy storage, commercial & industrial energy storage |
| Battery Materials | Cathode, anode, and recycling materials | High-nickel NCM, LFP | Self-supply and external supply |

## Representative Products

### Qilin Battery (CTP 3.0)

![Qilin Battery](https://www.catl.com/en/news/958.html)

> Image source: CATL official website news page. If the link is invalid or missing, please replace it with an official public image URL.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Not disclosed | Pack-level dimensions customized per vehicle model |
| Weight | Not disclosed | Pack-level weight customized per vehicle model |
| Cell Type | Prismatic / Cylindrical (NCM / LFP) | CATL official website |
| Volume Utilization | Up to 72% | CATL official website |
| Energy Density | NCM 255 Wh/kg; LFP 205 Wh/kg | CATL official website |
| Fast Charging Capability | Supports 4C fast charging | CATL official website |
| Cycle Life | ≥1000 cycles (NCM) | Industry public information |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: The third-generation CTP technology eliminates the module structure, improving volume utilization and energy density; supports 4C fast charging, reaching 80% SOC in 10 minutes.

**Application Scenarios**: High-end long-range electric vehicles; provides reference value for integrated battery packs in humanoid robot chassis.

## Relevance to Humanoid Robots

- Batteries, power semiconductors, and advanced materials are common foundations for achieving long endurance, high dynamics, and lightweight design in humanoid robots.
- Industrial robots and automated production lines provide reusable manufacturing capabilities for humanoid robot assembly, testing, and mass production.

## Supply Chain Position

- **Upstream Key Components/Materials**: Lithium, nickel, cobalt, and other cathode metals; separators, electrolytes, copper/aluminum foil; BMS chips.
- **Downstream Customers/Application Scenarios**: Automakers such as Tesla, BMW, NIO, Volkswagen, Ford, Hyundai; energy storage system integrators.
- **Main Competitors/Peers**: BYD, LG Energy Solution, Panasonic, Samsung SDI.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_catl`
- Product Entity: `ent_component_catl_qilin_battery`
- Key Relationships:
  - `ent_company_catl` -- `manufactures` --> `ent_component_catl_qilin_battery`
  - `ent_company_catl` -- `supplies` --> `ent_company_tesla`
  - `ent_company_catl` -- `supplies` --> `ent_company_bmw`

## References

1. [CATL Official Website](https://www.catl.com)
2. [CATL Qilin Battery Launch Event](https://www.catl.com/en/news/958.html)
3. [CATL Research Technology Page](https://www.catl.com/en/research/technology/)
