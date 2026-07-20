# Will Semiconductor

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 韦尔股份 |
| **English Name** | Will Semiconductor |
| **Headquarters** | Shanghai, China |
| **Founded** | 2007 (Acquired OmniVision in 2019) |
| **Website** | [https://www.willsemi.com / https://www.ovt.com](https://www.willsemi.com) |
| **Supply Chain Role** | CMOS Image Sensors (OmniVision), Discrete Semiconductor Devices, Power Management ICs |
| **Company Type** | Listed Company (603501), Top 3 Global CMOS Image Sensor Supplier |
| **Parent Company/Group** | Independently Listed |
| **Data Source** | Will Semiconductor Annual Report, OmniVision Official Website, Public Product Briefs |

## Company Overview

Will Semiconductor is a leading semiconductor design company in China. Its subsidiary, OmniVision, is a globally renowned supplier of CMOS image sensors. OmniVision products cover mobile phones, automotive, security, medical, and industrial vision. High-pixel sensors like the 50MP OV50H are widely used in high-end domestic flagship smartphones.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| Mobile CIS | High-pixel Main Camera/Wide Angle | OV50H / OV64B / OV32C | Smartphones |
| Automotive CIS | Surround View/Front View/In-Cabin | OX08B / OX03C, etc. | Smart Vehicles |
| Security/Industrial CIS | Low Light, Global Shutter | OS02 / OG0 Series | Security, Robotics |
| Discrete Devices & PMIC | Power Devices, Power Management | MOSFET, LDO, etc. | Consumer Electronics, Automotive |

## Representative Products

### Will Semiconductor OmniVision OV50H Image Sensor

> Will Semiconductor OmniVision OV50H Image Sensor: Please visit the [official page](https://www.willsemi.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Type | 50MP CMOS Image Sensor | OmniVision Official Website |
| Effective Pixels | 50 MP (8192 × 6144) | OmniVision Official Website |
| Pixel Size | 1.197 µm | OmniVision Official Website |
| Optical Format | 1/1.3" | OmniVision Official Website |
| Technology | PureCel®Plus-S, DCG™ HDR, H/V QPD | OmniVision Official Website |
| Frame Rate | 50MP@30fps / 12.5MP@120fps | OmniVision Official Website |
| HDR | DCG / Staggered HDR | OmniVision Official Website |
| Autofocus | H/V QPD PDAF, 100% Coverage | OmniVision Official Website |
| Output Format | 10/12/14-bit RGB RAW | OmniVision Official Website |
| Interface | 4-lane MIPI / C-PHY | OmniVision Official Website |
| Power Consumption | Active Mode ~1395 mW (50MP@30fps) | OmniVision Official Website |
| Operating Temperature | -30℃ – +85℃ | OmniVision Official Website |
| Package | COB / RW | OmniVision Official Website |
| Price | Not Disclosed | - |

**Technical Highlights**: PureCel®Plus-S Stack, DCG™ HDR, H/V QPD Omnidirectional Autofocus, excellent low-light and high-speed autofocus performance.

**Application Scenarios**: High-end smartphone main camera/wide angle, laptop webcams, video conferencing, robotic vision, automotive perception.

### Will Semiconductor OmniVision Automotive Image Sensor

> Will Semiconductor OmniVision Automotive Image Sensor: Please visit the [official page](https://www.willsemi.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Type | Automotive-Grade CMOS Image Sensor | OmniVision Official Website |
| Application | ADAS, Surround View, In-Cabin Monitoring | OmniVision Official Website |
| Features | High Dynamic Range, LED Flicker Mitigation | OmniVision Official Website |
| Price | Not Disclosed | - |

**Technical Highlights**: ASIL functional safety support, meeting stringent automotive electronics standards.

**Application Scenarios**: Autonomous driving perception, DMS/OMS, electronic rearview mirrors.

## Supply Chain Position

- **Upstream Key Components/Materials**: Wafer Foundry, Packaging & Testing, Optical Lenses, Filters, ISP Algorithms
- **Downstream Customers/Application Scenarios**: Smartphone OEMs, Laptop Manufacturers, Automotive Tier1 Suppliers, Robotics, Medical Devices
- **Main Competitors/Peers**: Sony, Samsung ISOCELL, SmartSens, GalaxyCore

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_willsemi`
- Product Entity: `ent_product_willsemi_ov50h`
- Component Entity: `ent_component_willsemi_ov50h_sensor`
- Key Relationships:
  - `ent_company_willsemi` -- `manufactures` --> `ent_product_willsemi_ov50h`
  - `ent_company_willsemi` -- `manufactures` --> `ent_component_willsemi_ov50h_sensor`
  - `ent_product_willsemi_ov50h` -- `uses` --> `ent_component_willsemi_ov50h_sensor`

## References

1. [Will Semiconductor Official Website](https://www.willsemi.com)
2. [Will Semiconductor OmniVision OV50H Image Sensor Product/Data Page](https://www.ovt.com/products/ov50h/)
3. Company Annual Reports, Product Datasheets, and Public Press Releases
4. [Appendix D Product Catalog](../index-products.md)
