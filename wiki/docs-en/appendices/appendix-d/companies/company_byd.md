# BYD

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | BYD Company Limited |
| **English Name** | BYD Company Limited |
| **Headquarters** | Shenzhen, Guangdong Province, China |
| **Founded** | 1995 |
| **Website** | [https://www.byd.com](https://www.byd.com) |
| **Supply Chain Segment** | Power batteries, energy storage batteries, new energy vehicles, electronics manufacturing |
| **Enterprise Type** | Listed company (Shenzhen Stock Exchange: 002594 / Hong Kong Stock Exchange: 1211) |
| **Parent Company/Group** | None (independently listed) |
| **Data Source** | Company website, Fraunhofer IKTS teardown research, public technical materials |

## Company Profile

BYD is a globally leading provider of comprehensive new energy solutions, with businesses spanning four major sectors: automotive, rail transit, new energy, and electronics.

Its subsidiary FinDreams Battery produces the Blade Battery, which uses a lithium iron phosphate (LFP) chemistry system. Through a "Cell-to-Pack" module-free structure, it improves space utilization and safety performance. The Blade Battery has been widely used in BYD's own models and is now being supplied externally to partners such as Toyota.

## Product Lines

| Product Line | Positioning | Representative Product | Application Area |
|--------------|-------------|------------------------|------------------|
| Power Battery | High-safety LFP battery pack | Blade Battery | Passenger vehicles, commercial vehicles, robot platforms |
| Energy Storage Battery | Grid-level energy storage system | BYD B-Box / Cube | Commercial and residential energy storage |
| Automotive Electronics | Motor, electronic control, BMS | Eight-in-one electric powertrain | New energy vehicles |

## Representative Product

### BYD Blade Battery

![Blade Battery](https://www.byd.com/en/news-list/20200329-the-blade-battery)

> Image source: BYD official website. If the link is invalid or missing, please replace it with a publicly available official image URL.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Cell Dimensions | 960 mm × 90 mm × 12 mm (example) | BatteryDesign teardown data |
| Cell Weight | Approx. 2.63 kg (138 Ah version) | BatteryDesign teardown data |
| Chemistry System | Lithium iron phosphate (LFP) | BYD official website |
| Nominal Voltage | 3.2 V | BYD official website |
| Cell Capacity | 138 Ah / 202 Ah, etc. | Public teardown data |
| Energy Density | Approx. 160–169.6 Wh/kg (cell level) | Fraunhofer IKTS / Evlithium |
| Cycle Life | ≥3000 cycles | BYD official website |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: Long, stacked LFP cells are directly assembled into packs; the module-free design improves volumetric utilization. Passes nail penetration test without catching fire, emphasizing intrinsic safety.

**Application Scenarios**: New energy vehicle chassis, energy storage containers, safety-sensitive humanoid robot battery solutions.

## Relevance to Humanoid Robots

- Batteries, power semiconductors, and advanced materials are common foundations for achieving long endurance, high dynamics, and lightweight design in humanoid robots.
- Industrial robots and automated production lines provide reusable manufacturing capabilities for the assembly, testing, and mass production of humanoid robots.

## Supply Chain Position

- **Upstream Key Components/Materials**: Lithium iron phosphate cathode, graphite anode, separator, electrolyte, structural components.
- **Downstream Customers/Application Scenarios**: BYD Auto, Toyota (bZ3 and other collaborative projects), energy storage integrators.
- **Main Competitors/Peers**: CATL, Gotion High-tech, EVE Energy, LG Energy Solution.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_byd`
- Product Entity: `ent_component_byd_blade_battery`
- Key Relationships:
  - `ent_company_byd` -- `manufactures` --> `ent_component_byd_blade_battery`
  - `ent_company_byd` -- `supplies` --> `ent_company_toyota`

## References

1. [BYD Official Website](https://www.byd.com)
2. [BYD Blade Battery Official Introduction](https://www.byd.com/en/news-list/20200329-the-blade-battery)
3. [BatteryDesign BYD Blade Teardown](https://www.batterydesign.net/byd-blade/)
