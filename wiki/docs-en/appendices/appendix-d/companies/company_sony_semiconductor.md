# Sony Semiconductor Solutions

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Sony Semiconductor Solutions |
| **English Name** | Sony Semiconductor Solutions |
| **Headquarters** | Atsugi, Kanagawa Prefecture, Japan |
| **Established** | 2016 |
| **Website** | [https://www.sony-semicon.co.jp](https://www.sony-semicon.co.jp) |
| **Supply Chain Segment** | CMOS Image Sensor, 3D Sensing, Stacked Vision Sensor, LiDAR SPAD |
| **Enterprise Attribute** | Wholly owned subsidiary of Sony Group, global leader in image sensors |
| **Parent Company/Group** | Sony Group Corporation |
| **Data Source** | Sony Semiconductor official website, product datasheets, Sony annual report |

## Company Profile

Sony Semiconductor Solutions is the world's largest supplier of CMOS image sensors, with products covering mobile, automotive, industrial, and robot vision.

Sony Semiconductor Solutions inherits Sony's technological accumulation in the image sensor field, providing a full-stack solution from mobile CIS, automotive CIS, industrial vision to 3D depth sensing. Its stacked CMOS, back-illuminated technology, global shutter, and SPAD dToF sensors play a core role in robot vision, SLAM, obstacle avoidance, and object recognition. The IMX500 series intelligent vision sensors are the first to integrate AI inference capabilities on the sensor side, offering a new paradigm for low-latency edge vision.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Industrial/Robot Image Sensors | High-speed global shutter / High dynamic range | IMX500 / IMX397 / IMX426 | Robot vision, industrial inspection |
| Automotive Image Sensors | ADAS / In-cabin monitoring | IMX490 / IMX623 / OX08D4Q | Autonomous driving, robot navigation |
| 3D/Depth Sensing | iToF / dToF / SPAD | IMX611 / IMX590 / IMX459 | AR/VR, robot obstacle avoidance |
| Intelligent Vision Sensors | Edge AI inference | IMX500 / IMX501 | Edge AI, embodied intelligence |

## Representative Products

### Sony IMX500 Intelligent Vision Sensor

> Sony IMX500 Intelligent Vision Sensor: Please visit the [official page](https://www.sony-semicon.co.jp) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | Stacked CMOS image sensor + AI inference | Official website/datasheet |
| Effective Pixels | Approx. 12.3 million (4056 × 3040) | Official website/datasheet |
| Optical Format | 1/2.3 type | Official website/datasheet |
| Pixel Size | Not disclosed | - |
| Shutter | Rolling shutter | Official website/datasheet |
| Maximum Frame Rate | Not disclosed | - |
| AI Capability | On-sensor AI model inference | Official website/datasheet |
| Output Format | Metadata / Image + Metadata | Official website/datasheet |
| Interface | MIPI D-PHY / SLVS-EC | Official website/datasheet |
| Power Supply | Not disclosed | - |
| Power Consumption | Not disclosed | - |
| Operating Temperature | Not disclosed | - |
| Package | COB / CSP | Official website/datasheet |
| Price | Not disclosed | - |

**Technical Highlights**: The world's first image sensor with on-sensor AI inference, integrating an AI processing unit in a stacked architecture. By outputting only metadata, it achieves low power consumption, low bandwidth, and high privacy for visual recognition.

**Application Scenarios**: Robot visual perception, intelligent surveillance, retail analytics, industrial quality inspection, embodied intelligence edge devices, ADAS.

### Sony IMX611 SPAD dToF Depth Sensor

> Sony IMX611 SPAD dToF Depth Sensor: Please visit the [official page](https://www.sony-semicon.co.jp) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | SPAD dToF depth sensor | Official website |
| Resolution | Not disclosed | - |
| Ranging Range | Not disclosed | - |
| Application | AR/VR, robot obstacle avoidance, 3D scanning | Official website |
| Price | Not disclosed | - |

**Technical Highlights**: dToF depth sensing based on Single Photon Avalanche Diode (SPAD), suitable for medium-to-long-range 3D perception.

**Application Scenarios**: Robot navigation and obstacle avoidance, AR/VR spatial mapping, gesture recognition, 3D measurement.

## Supply Chain Position

- **Upstream Key Components/Materials**: Wafer foundry (TSMC / Sony's own production lines), packaging and testing, optical filters, microlenses, substrates, and driver ICs
- **Downstream Customers/Application Scenarios**: Smartphone OEMs, Automotive Tier 1 suppliers, robot manufacturers, security and industrial vision vendors, AR/VR device manufacturers
- **Main Competitors/Peers**: Samsung Electro-Mechanics, OmniVision, GalaxyCore, SmartSens, ams OSRAM, STMicroelectronics

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_sony_semiconductor`
- Product Entity: `ent_product_sony_semiconductor_imx500`
- Component Entity: `ent_component_sony_semiconductor_imx500_sensor`
- Key Relationships:
  - `ent_company_sony_semiconductor` -- `manufactures` --> `ent_product_sony_semiconductor_imx500`
  - `ent_company_sony_semiconductor` -- `manufactures` --> `ent_component_sony_semiconductor_imx500_sensor`
  - `ent_product_sony_semiconductor_imx500` -- `uses` --> `ent_component_sony_semiconductor_imx500_sensor`

## References

1. [Sony Semiconductor Solutions Official Website](https://www.sony-semicon.co.jp)
2. [Sony IMX500 Intelligent Vision Sensor Product/Information Page](https://www.sony-semicon.co.jp/products/common/IMX500.html)
3. Company annual reports, product datasheets, and public press releases
4. [Appendix D Product Catalog](../index-products.md)
