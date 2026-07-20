# SmartSens

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).  
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 思特威 |
| **English Name** | SmartSens |
| **Headquarters** | Shanghai, China |
| **Founded** | 2011 |
| **Website** | [https://www.smartsenstech.com](https://www.smartsenstech.com) |
| **Supply Chain Role** | CMOS Image Sensors (Security, Machine Vision, Automotive, Mobile) |
| **Company Type** | Listed on STAR Market (688213), Leading Domestic CIS Design Company |
| **Parent Company/Group** | Independently Listed |
| **Data Source** | SmartSens official website, product launch news, public datasheets |

## Company Overview

SmartSens is a technologically advanced CMOS image sensor supplier, with proprietary technologies such as SmartGS™ Global Shutter, SFCPixel®, and PixGain HDR®. The company's products cover four major areas: security surveillance, machine vision, intelligent automotive electronics, and smartphones, and have expanded into applications such as robot vision and industrial inspection.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Smartphone CIS | High-pixel flagship main camera | SC580XS / SC550XS | Flagship smartphones |
| Machine Vision CIS | Global shutter | SC130GS / SC235HGS, etc. | Industrial cameras, robots |
| Security Surveillance CIS | Starlight-level low illumination | SC850SL / SC880SL | Security, automotive |
| Automotive CIS | Automotive-grade image sensors | SC120AT / SC220AT, etc. | ADAS, DMS |

## Representative Products

### SmartSens SC580XS CMOS Image Sensor

> SmartSens SC580XS CMOS Image Sensor: Please visit [Official Documentation](https://www.smartsenstech.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | 50MP CMOS Image Sensor | SmartSens official website |
| Effective Pixels | 50 MP | SmartSens official website |
| Pixel Size | 1.22 µm | SmartSens official website |
| Optical Format | 1/1.28" | SmartSens official website |
| Process | 22 nm HKMG Stack | SmartSens official website |
| HDR | PixGain HDR® / Triple Exposure HDR | SmartSens official website |
| Dynamic Range | Up to 120 dB | SmartSens official website |
| Read Noise | As low as 0.7 e⁻ | SmartSens official website |
| Autofocus | AllPix ADAF® / Sparse PDAF | SmartSens official website |
| Video | 4K 120 fps (Binning Mode) | SmartSens official website |
| Interface | MIPI C-PHY / D-PHY | SmartSens official website |
| Power Consumption | Approx. 500 mW at 50MP@25fps | SmartSens official website |
| Operating Temperature | -20°C – +70°C | SmartSens official website |
| Price | Not disclosed | - |

**Technical Highlights**: 22 nm HKMG Stack, SFCPixel®-2, PixGain HDR®, AllPix ADAF® full-pixel autofocus, flagship-level imaging performance.

**Application Scenarios**: Flagship smartphone main camera, ultra-wide-angle, robot vision, industrial inspection, drone aerial photography.

### SmartSens SmartGS™ Global Shutter Machine Vision Sensor

> SmartSens SmartGS™ Global Shutter Machine Vision Sensor: Please visit [Official Documentation](https://www.smartsenstech.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | Global Shutter CMOS | SmartSens official website |
| Resolution | 1.3MP – 9MP multiple models | SmartSens official website |
| Features | High frame rate, low noise | SmartSens official website |
| Price | Not disclosed | - |

**Technical Highlights**: SmartGS™ technology, suitable for high-speed moving object capture and machine vision inspection.

**Application Scenarios**: Industrial robot inspection, logistics barcode reading, robot navigation.

## Supply Chain Position

- **Upstream Key Components/Materials**: Wafer foundry, packaging and testing, optical lenses, filters, ISP algorithms
- **Downstream Customers/Application Scenarios**: Smartphone OEMs, security manufacturers, automotive Tier 1 suppliers, robots, industrial cameras
- **Main Competitors/Peers**: Sony, Samsung ISOCELL, OmniVision, GalaxyCore

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_smartsens`
- Product Entity: `ent_product_smartsens_sc580xs`
- Component Entity: `ent_component_smartsens_sc580xs_sensor`
- Key Relationships:
  - `ent_company_smartsens` -- `manufactures` --> `ent_product_smartsens_sc580xs`
  - `ent_company_smartsens` -- `manufactures` --> `ent_component_smartsens_sc580xs_sensor`
  - `ent_product_smartsens_sc580xs` -- `uses` --> `ent_component_smartsens_sc580xs_sensor`

## References

1. [SmartSens Official Website](https://www.smartsenstech.com)
2. [SmartSens SC580XS CMOS Image Sensor Product/Documentation Page](https://www.smartsenstech.com/en/m)
3. Company annual reports, product datasheets, and public press releases
4. [Appendix D Product Catalog](../index-products.md)
