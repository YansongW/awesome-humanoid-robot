# Himax Technologies

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 奇景光电 (Himax Technologies) |
| **English Name** | Himax Technologies |
| **Headquarters** | Tainan, Taiwan, China (with offices in Silicon Valley, USA) |
| **Founded** | 2001 |
| **Website** | [https://www.himax.com.tw](https://www.himax.com.tw) |
| **Supply Chain Role** | 3D Sensing Modules, Wafer-Level Optics (WLO), CMOS Image Sensors, Driver ICs |
| **Enterprise Type** | Nasdaq-listed company (NASDAQ: HIMX), Taiwanese driver IC/optical module manufacturer |
| **Parent Company/Group** | Independently listed |
| **Data Source** | Himax official website, annual reports, product press releases |

## Company Profile

Himax Technologies is a global leading supplier of display driver ICs, wafer-level optics (WLO), and 3D sensing solutions.

Himax Technologies focuses on display driver ICs, wafer-level optics (WLO), 3D sensing, and low-power AI vision solutions. Its WLO technology enables the fabrication of micro-optical components at the wafer level, providing miniaturized and low-cost projection and receiving modules for structured light, ToF, and DOE. Himax's complete 3D sensing solution (Structured Light Sensing Module) has been widely adopted in smartphone face unlock, payment-grade 3D recognition, and robot vision obstacle avoidance.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| 3D Sensing Module | Structured Light / Active Stereo | SLiM / 3D Sensing Module | Smartphones, Robotics, AR/VR |
| Wafer-Level Optics WLO | DOE / Collimating Lens | WLO Optical Components | 3D Sensing, Optical Communication |
| CMOS Image Sensor | Low Power / Global Shutter | WiseEye / Custom CIS | AIoT, Robotics |
| Display Driver IC | TDDI / OLED | LCD/OLED Drivers | Smartphones, Automotive |

## Representative Products

### Himax SLiM 3D Sensing Module

> Himax SLiM 3D Sensing Module: Please visit [Official Information](https://www.himax.com.tw) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | Structured Light 3D Sensing Module | Official website/Press release |
| Depth Technology | Structured Light / Active IR Projection | Official website/Press release |
| Depth Resolution | VGA level (640 × 480) @ 30 fps | Official website/Press release |
| Field of View | Approximately 67° horizontal (typical) | Official website/Press release |
| Working Distance | Approximately 0.3 m – 1.0 m | Official website/Press release |
| Depth Accuracy | Not disclosed | - |
| Size | Miniaturized module (specifics not disclosed) | Official website/Press release |
| Power Consumption | Not disclosed | - |
| Interface | MIPI / USB2.0 (varies by solution) | Official website/Press release |
| Emitter | VCSEL / EEL + WLO DOE | Official website/Press release |
| Receiver | NIR-enhanced CMOS / ToF | Official website/Press release |
| Operating Temperature | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: Wafer-level optics (WLO) enables miniaturized structured light projection, integrating emission and reception units, supporting payment-grade 3D recognition and short-range robot perception.

**Application Scenarios**: Smartphone face unlock/payment, robot obstacle avoidance and grasping, AR/VR gesture interaction, smart locks, 3D scanning.

### Himax WiseEye Ultra-Low Power AI Vision Solution

> Himax WiseEye Ultra-Low Power AI Vision Solution: Please visit [Official Information](https://www.himax.com.tw) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | Ultra-low power AI vision sensing solution | Official website |
| Sensor | Proprietary ultra-low power CIS + AI accelerator | Official website |
| Power Consumption | Milliwatt level | Official website |
| Application | Smart home appliances, robotics, AIoT | Official website |
| Price | Not disclosed | - |

**Technical Highlights**: AI inference is performed at the sensor edge, supporting human/object detection, suitable for battery-powered devices.

**Application Scenarios**: Smart locks, security cameras, robot wake-up, wearable devices.

## Supply Chain Position

- **Upstream Key Components/Materials**: Silicon wafers, optical glass/polymers, VCSEL/EEL laser chips, packaging substrates, driver ICs, wafer-level optical materials
- **Downstream Customers/Application Scenarios**: Smartphone OEMs, robot integrators, AR/VR device manufacturers, security and AIoT vendors, automotive Tier 1 suppliers
- **Main Competitors/Peers**: ams OSRAM, Sony Semiconductor, Samsung Electro-Mechanics, Orbbec, Sunny Optical, Q Technology

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_himax`
- Product Entity: `ent_product_himax_slim_3d`
- Component Entity: `ent_component_himax_slim_3d_module`
- Key Relationships:
  - `ent_company_himax` -- `manufactures` --> `ent_product_himax_slim_3d`
  - `ent_company_himax` -- `manufactures` --> `ent_component_himax_slim_3d_module`
  - `ent_product_himax_slim_3d` -- `uses` --> `ent_component_himax_slim_3d_module`

## References

1. [Himax Technologies Official Website](https://www.himax.com.tw)
2. [Himax SLiM 3D Sensing Module Product/Information Page](https://www.himax.com.tw/products/structured-light-sensing/)
3. Company annual reports, product datasheets, and public press releases
4. [Appendix D Product Catalog](../index-products.md)
