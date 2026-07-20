# ams OSRAM / ams OSRAM

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed".

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 艾迈斯欧司朗 (ams OSRAM) |
| **English Name** | ams OSRAM |
| **Headquarters** | Premstätten, Austria / Munich, Germany |
| **Founded** | 2020 (Merger) |
| **Website** | [https://ams-osram.com](https://ams-osram.com) |
| **Supply Chain Role** | Optical sensors, 3D sensing, LEDs/Lasers, NIR CMOS image sensors |
| **Company Type** | Publicly traded (SIX: AMS), global leader in optical and sensing solutions |
| **Parent/Group** | Independently listed |
| **Data Source** | ams OSRAM official website, product datasheets, annual reports |

## Company Profile

ams OSRAM was formed by the merger of ams and OSRAM, and is a global leading supplier of optical sensors, light sources, and 3D sensing solutions.

Headquartered in Austria and Germany, ams OSRAM's business covers optical sensing, CMOS image sensors, VCSEL/EEL lasers, LEDs, spectral sensing, and automotive lighting. Its Mira series of NIR-enhanced global shutter CMOS sensors, Belago dot projectors, and VCSEL modules are widely used in 3D facial recognition, robot vision guidance, AR/VR gesture recognition, and autonomous driving in-cabin monitoring. ams OSRAM's core strength lies in the vertical integration of optical emission, reception, and sensing algorithms.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| 3D/NIR Image Sensors | NIR Global Shutter | Mira050 / Mira130 / Mira220 | Robot 3D vision, facial recognition |
| VCSEL / EEL Lasers | Structured Light/ToF Projection | Belago / PMS / VESEL | AR/VR, robot obstacle avoidance |
| Ambient/Spectral Sensors | Color/Spectrum/Position Sensing | AS7341 / TCS3701 | Consumer electronics, industrial |
| LED/OLED & Automotive Lighting | General/Automotive/Specialty Lighting | OSLON / SYNIOS | Automotive, industrial |

## Representative Products

### ams OSRAM Mira220 NIR CMOS Image Sensor

> ams OSRAM Mira220 NIR CMOS Image Sensor: Please visit the [official page](https://ams-osram.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Type | NIR-enhanced global shutter CMOS | Official website/datasheet |
| Effective Pixels | 2.2 MP | Official website/datasheet |
| Resolution | Approx. 1920 × 1080 | Official website/datasheet |
| Optical Format | 1/2.7 inch | Official website/datasheet |
| Pixel Size | 2.79 µm | Official website/datasheet |
| Shutter | Global shutter | Official website/datasheet |
| NIR QE | High quantum efficiency at 850/940 nm | Official website/datasheet |
| Max Frame Rate | Up to 90 fps | Official website/datasheet |
| Interface | MIPI CSI-2 | Official website/datasheet |
| Power Consumption | Not disclosed | - |
| Supply Voltage | Not disclosed | - |
| Operating Temperature | Not disclosed | - |
| Package | CSP | Official website/datasheet |
| Price | Not disclosed | - |

**Technical Highlights**: Global shutter pixels specifically optimized for 850/940 nm NIR, offering high quantum efficiency, low noise, and high frame rate, suitable for 3D structured light, ToF, and robot vision.

**Application Scenarios**: Robot 3D vision, structured light/ToF cameras, facial recognition, gesture recognition, in-cabin monitoring, AR/VR tracking.

### ams OSRAM Belago 1.1 Dot Projector

> ams OSRAM Belago 1.1 Dot Projector: Please visit the [official page](https://ams-osram.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Type | VCSEL dot projector | Official website |
| Wavelength | 940 nm | Official website |
| Field of View | Not disclosed | - |
| Application | Structured light 3D sensing, facial recognition | Official website |
| Price | Not disclosed | - |

**Technical Highlights**: Integrates collimating optics and VCSEL array to provide high-quality infrared dot projection for structured light 3D cameras.

**Application Scenarios**: Robot 3D vision, facial payment, access control, AR/VR.

## Supply Chain Position

- **Upstream Key Components/Materials**: Silicon wafers, III-V compound semiconductors (VCSEL/EEL), optical lenses/DOE, packaging materials, driver ICs, wafer-level optics (WLO)
- **Downstream Customers/Applications**: 3D camera module manufacturers, robot OEMs, AR/VR device makers, smartphone OEMs, automotive Tier 1 suppliers, industrial vision companies
- **Main Competitors/Peers**: Sony Semiconductor, Samsung Electro-Mechanics, Lumentum, II-VI/Coherent, Himax, OmniVision

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_ams_osram`
- Product Entity: `ent_product_ams_osram_mira220`
- Component Entity: `ent_component_ams_osram_mira220_sensor`
- Key Relationships:
  - `ent_company_ams_osram` -- `manufactures` --> `ent_product_ams_osram_mira220`
  - `ent_company_ams_osram` -- `manufactures` --> `ent_component_ams_osram_mira220_sensor`
  - `ent_product_ams_osram_mira220` -- `uses` --> `ent_component_ams_osram_mira220_sensor`

## References

1. [ams OSRAM Official Website](https://ams-osram.com)
2. [ams OSRAM Mira220 NIR CMOS Image Sensor Product/Info Page](https://ams-osram.com/products/sensors/area-imaging-sensors/ams-mira220)
3. Company annual reports, product datasheets, and public press releases
4. [Appendix D Product Catalog](../index-products.md)
