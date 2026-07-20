# Infineon Technologies

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Infineon Technologies AG |
| **English Name** | Infineon Technologies AG |
| **Headquarters** | Neubiberg, Germany |
| **Founded** | 1999 (spun off from Siemens Semiconductor Division) |
| **Website** | [https://www.infineon.com](https://www.infineon.com) |
| **Supply Chain Role** | Power semiconductors, sensors, microcontrollers, security chips |
| **Enterprise Type** | Publicly traded company (Frankfurt Stock Exchange: IFX) |
| **Parent Company/Group** | None (independently listed) |
| **Data Source** | Infineon official press releases, CoolSiC product page |

## Company Profile

Infineon is a globally leading supplier of semiconductor solutions, with top market shares in automotive electronics and power semiconductors.

Its CoolSiC™ silicon carbide MOSFETs and IGBT modules are widely used in electric vehicle drives, photovoltaic inverters, energy storage converters, and industrial drives. For humanoid robots, high-efficiency motor drive inverters and power management chips are core components for improving endurance and dynamic response.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| Power MOSFET | High-efficiency silicon carbide power devices | CoolSiC™ MOSFET | Electric drive inverters, DC/DC, charging stations |
| IGBT Modules | Medium to high power motor drives | HybridPACK / EconoDUAL | New energy vehicles, industrial drives |
| Gate Drivers | Power device drivers | EiceDRIVER | Inverters, power supplies |

## Representative Products

### CoolSiC™ MOSFET 1200 V / 62 mm Module

![CoolSiC](https://www.infineon.com/cms/en/product/power/wide-band-gap-semiconductors/sic/sic-mosfets/)

> Image source: Infineon official website. If the link is invalid or missing, please replace it with an official public image URL.

| Specification | Value | Remarks/Source |
|---|---|---|
| Package | 62 mm half-bridge module | Infineon press release |
| Voltage Rating | 1200 V / 2000 V | Infineon press release |
| On-Resistance | 1 mΩ / 2 mΩ / 5 mΩ, etc. | Infineon press release |
| Rated Current | 180 A / 420 A / 560 A | Infineon press release |
| Operating Junction Temperature | 150 °C (continuous) | Infineon press release |
| Topology | Half-bridge | Infineon press release |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: Based on M1H trench-gate SiC MOSFET technology, featuring a wide gate voltage window, low switching losses, and high power density, suitable for medium-power scenarios above 250 kW.

**Application Scenarios**: Electric drive inverters, energy storage converters, industrial servo drives, humanoid robot joint motor drives.

## Relevance to Humanoid Robots

- Batteries, power semiconductors, and advanced materials are common foundations for achieving long endurance, high dynamics, and lightweight design in humanoid robots.
- Industrial robots and automated production lines provide reusable manufacturing capabilities for the assembly, testing, and mass production of humanoid robots.

## Supply Chain Position

- **Upstream Key Components/Materials**: SiC substrates (SICC, Wolfspeed), epitaxial wafers, packaging materials, silicon wafers.
- **Downstream Customers/Application Scenarios**: Automotive OEMs, photovoltaic/energy storage inverter manufacturers, industrial automation vendors.
- **Main Competitors/Peers**: STMicroelectronics, Wolfspeed, ROHM, Onsemi, Mitsubishi Electric.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_infineon`
- Product Entity: `ent_component_infineon_coolsic_mosfet`
- Key Relationship:
  - `ent_company_infineon` -- `manufactures` --> `ent_component_infineon_coolsic_mosfet`

## References

1. [Infineon Official Website](https://www.infineon.com)
2. [Infineon CoolSiC MOSFET Product Page](https://www.infineon.com/cms/en/product/power/wide-band-gap-semiconductors/sic/sic-mosfets/)
3. [CoolSiC 62mm Module Press Release](https://www.infineon.com/cms/en/about-infineon/press/market-news/2023/INFGIP202311-024.html)
