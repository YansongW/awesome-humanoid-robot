# OmniVision

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 豪威科技 (OmniVision) |
| **English Name** | OmniVision |
| **Headquarters** | Santa Clara, California, USA |
| **Founded** | 1995 |
| **Official Website** | [https://www.ovt.com](https://www.ovt.com) |
| **Supply Chain Role** | CMOS Image Sensors, Automotive/Robotics Vision, Display Drivers |
| **Enterprise Attribute** | Subsidiary of Will Semiconductor, Global CIS Design Leader |
| **Parent Company/Group** | Will Semiconductor (韦尔股份, 603501) |
| **Data Source** | OmniVision Official Website, Will Semiconductor Annual Report, Product Datasheets |

## Company Profile

OmniVision is a world-leading CMOS image sensor design company, with products covering mobile, automotive, security, industrial, and robotics vision.

OmniVision was founded in 1995 and was acquired by China's Will Semiconductor in 2019, now a wholly-owned subsidiary. OmniVision provides CMOS image sensors ranging from VGA to tens of megapixels, covering mobile devices, automotive ADAS, security surveillance, industrial vision, and robot navigation. Its OX series automotive image sensors, OG series global shutter industrial sensors, and OV series mobile sensors are widely used in humanoid robot head vision, SLAM navigation, and object recognition.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| Automotive Image Sensors | ADAS/Surround View/In-Cabin | OX08D10 / OX03C10 / OX05B1S | Autonomous Driving, Robot Navigation |
| Mobile/Robotics Vision | High Pixel/Low Power | OV50H / OV64B / OV32C | Mobile Phones, Robots |
| Machine Vision/Global Shutter | Industrial Inspection & High Speed | OG0VA / OG01A / OG02B | Industrial, Drones |
| Display Driver/Touch | Panel Driver | TD4377, etc. | Mobile Phones, Automotive |

## Representative Products

### OmniVision OX08D10 Automotive/Robotics 8MP Image Sensor

> OmniVision OX08D10 Automotive/Robotics 8MP Image Sensor: Please visit [Official Information](https://www.ovt.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Type | Automotive-grade 8MP CMOS Image Sensor | Official Website/Datasheet |
| Effective Pixels | 8 MP | Official Website/Datasheet |
| Optical Format | 1/1.7" | Official Website/Datasheet |
| Pixel Size | 2.1 µm | Official Website/Datasheet |
| Shutter | Rolling Shutter (with HDR) | Official Website/Datasheet |
| Maximum Frame Rate | Up to 60 fps | Official Website/Datasheet |
| Dynamic Range | 120 dB HDR | Official Website/Datasheet |
| LED Flicker Mitigation | Supports LFM | Official Website/Datasheet |
| Functional Safety | ASIL-B | Official Website/Datasheet |
| Interface | MIPI D-PHY / C-PHY | Official Website/Datasheet |
| Output Format | RAW / YUV | Official Website/Datasheet |
| Operating Temperature | -40℃ – +105℃ (Automotive-grade) | Official Website/Datasheet |
| Package | COB / CSP | Official Website/Datasheet |
| Price | Not disclosed | - |

**Technical Highlights**: High resolution, large pixel, 120 dB HDR with LED flicker mitigation, ASIL-B functional safety level, suitable for high-reliability robotics and automotive vision.

**Application Scenarios**: Humanoid robot head main camera, unmanned vehicle/AMR navigation, ADAS front view, industrial inspection cameras, security surveillance.

### OmniVision OG0VA Global Shutter Image Sensor

> OmniVision OG0VA Global Shutter Image Sensor: Please visit [Official Information](https://www.ovt.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Type | Global Shutter CMOS Image Sensor | Official Website |
| Effective Pixels | Not disclosed | - |
| Shutter | Global Shutter | Official Website |
| Application | Industrial Vision, Robotics Vision, AR/VR | Official Website |
| Price | Not disclosed | - |

**Technical Highlights**: Global shutter design reduces motion artifacts at high speed, suitable for industrial inspection and robotics vision.

**Application Scenarios**: Machine vision cameras, drone obstacle avoidance, AR/VR tracking, high-speed motion analysis.

## Supply Chain Position

- **Upstream Key Components/Materials**: Wafer foundry (TSMC, etc.), packaging and testing, optical filters, microlenses, substrates, ISP algorithm licensing
- **Downstream Customers/Application Scenarios**: Smartphone OEMs, Automotive Tier 1, Robot OEMs, Industrial Camera Manufacturers, Security Surveillance Brands, Medical Equipment Vendors
- **Main Competitors/Peers**: Sony Semiconductor, Samsung Electro-Mechanics, GalaxyCore, SmartSens, Other Will Semiconductor Brands, ams OSRAM

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_omnivision`
- Product Entity: `ent_product_omnivision_ox08d10`
- Component Entity: `ent_component_omnivision_ox08d10_sensor`
- Key Relationships:
  - `ent_company_omnivision` -- `manufactures` --> `ent_product_omnivision_ox08d10`
  - `ent_company_omnivision` -- `manufactures` --> `ent_component_omnivision_ox08d10_sensor`
  - `ent_product_omnivision_ox08d10` -- `uses` --> `ent_component_omnivision_ox08d10_sensor`

## References

1. [OmniVision Official Website](https://www.ovt.com)
2. [OmniVision OX08D10 Automotive/Robotics 8MP Image Sensor Product/Information Page](https://www.ovt.com/products/ox08d10)
3. Company Annual Reports, Product Datasheets, and Public Press Releases
4. [Appendix D Product Catalog](../index-products.md)
