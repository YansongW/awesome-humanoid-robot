# GalaxyCore

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed".

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 格科微 |
| **English Name** | GalaxyCore |
| **Headquarters** | Shanghai, China |
| **Founded** | 2003 |
| **Website** | [https://www.gcoreinc.com](https://www.gcoreinc.com) |
| **Supply Chain Role** | CMOS Image Sensor, Display Driver IC |
| **Company Type** | Listed on STAR Market (688728), Fab-Lite CIS design leader |
| **Parent Company/Group** | Independently listed |
| **Data Source** | GalaxyCore official website, prospectus, product press releases |

## Company Overview

GalaxyCore is a leading Chinese CMOS image sensor and display driver IC design company, adopting a Fab-Lite model integrating design, manufacturing, packaging, and testing. Its product portfolio covers the full range of CIS from QVGA to 50MP, widely used in smartphones, wearables, automotive electronics, smart homes, and industrial vision.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Mobile CMOS Sensors | High pixel / Low cost | GC32E2 / GC50 Series | Smartphones |
| Non-Mobile CMOS Sensors | Security / Automotive / Industrial | GC2083 / GC4653, etc. | Security, Automotive, IoT |
| Display Driver ICs | TDDI / AMOLED | FHD TDDI / AMOLED DDIC | Smartphones, Wearables |
| Specialty Process | Single-chip high pixel | Non-stacked 32MP/50MP | Mid-range flagship phones |

## Representative Products

### GalaxyCore GC32E2 CMOS Image Sensor

> GalaxyCore GC32E2 CMOS Image Sensor: Please visit [official page](https://www.gcoreinc.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | 32MP CMOS Image Sensor | GalaxyCore official website |
| Effective Pixels | 32 MP | GalaxyCore official website |
| Pixel Size | 0.7 µm | GalaxyCore official website |
| Optical Format | 1/3.1" | GalaxyCore official website |
| Technology | Backside Illuminated (BSI) | GalaxyCore official website |
| Shutter | Rolling Shutter | GalaxyCore official website |
| HDR | Single-frame DAG HDR | GalaxyCore official website |
| Autofocus | PDAF Phase Detection | GalaxyCore official website |
| Output Format | RAW 10 / 12 | GalaxyCore official website |
| Interface | MIPI D-PHY | GalaxyCore official website |
| Package | COB / COM | GalaxyCore official website |
| Frame Rate | Up to 15 fps (full resolution) | GalaxyCore official website |
| Operating Temperature | -20°C – +70°C | GalaxyCore official website |
| Price | Not disclosed | - |

**Technical Highlights**: Second-generation single-chip 32MP, 0.7 µm pixel, DAG HDR, PDAF, AON low power consumption, balancing high pixel count and cost advantages.

**Application Scenarios**: Smartphone front camera, tablet, robot vision, wearable devices, video calls.

### GalaxyCore GC50 Series 50MP CMOS Image Sensor

> GalaxyCore GC50 Series 50MP CMOS Image Sensor: Please visit [official page](https://www.gcoreinc.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | 50MP CMOS Image Sensor | GalaxyCore official website |
| Feature | Non-stacked 0.61 µm pixel | GalaxyCore official website |
| Application | Smartphone main camera | GalaxyCore official website |
| Price | Not disclosed | - |

**Technical Highlights**: World's first non-stacked 0.61 µm 50MP sensor, driving high pixel count down to lower tiers.

**Application Scenarios**: Mid-range flagship phone main camera, ultra-wide angle.

## Supply Chain Position

- **Upstream Key Components/Materials**: Wafer foundry, packaging and testing, color filters, microlenses, substrates
- **Downstream Customers/Application Scenarios**: Smartphone OEM, ODM, tablets, robots, IoT camera manufacturers
- **Main Competitors/Peers**: Sony, Samsung ISOCELL, OmniVision, SmartSens

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_gcore`
- Product Entity: `ent_product_gcore_gc32e2`
- Component Entity: `ent_component_gcore_gc32e2_sensor`
- Key Relationships:
  - `ent_company_gcore` -- `manufactures` --> `ent_product_gcore_gc32e2`
  - `ent_company_gcore` -- `manufactures` --> `ent_component_gcore_gc32e2_sensor`
  - `ent_product_gcore_gc32e2` -- `uses` --> `ent_component_gcore_gc32e2_sensor`

## References

1. [GalaxyCore official website](https://www.gcoreinc.com)
2. [GalaxyCore GC32E2 CMOS Image Sensor product/info page](https://en.gcoreinc.com/news/detail-67)
3. Company annual reports, product datasheets, and public press releases
4. [Appendix D Product Directory](../index-products.md)
