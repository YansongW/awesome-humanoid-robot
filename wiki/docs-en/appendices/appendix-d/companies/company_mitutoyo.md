# Mitutoyo

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Mitutoyo |
| **English Name** | Mitutoyo |
| **Headquarters** | Kawasaki, Kanagawa, Japan |
| **Founded** | 1934 |
| **Website** | [https://www.mitutoyo.com](https://www.mitutoyo.com) |
| **Supply Chain Role** | Precision measurement equipment, coordinate measuring machines, gauges, sensors, industrial software |
| **Enterprise Attribute** | Global leader in metrology and precision measurement, family-owned (unlisted) |
| **Parent Company/Group** | Independently operated |
| **Data Source** | Mitutoyo official website, product manuals, distributor technical materials |

## Company Profile

Mitutoyo is a globally renowned manufacturer of precision measuring instruments. Its product range covers vernier calipers, micrometers, coordinate measuring machines (CMMs), vision measuring systems, roughness/contour/roundness measuring instruments, and sensor systems. The CRYSTA-Apex series CNC CMMs, known for their high precision, high speed, and multi-sensor capabilities, are widely used in automotive, aerospace, electronics, and robotic component inspection.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Coordinate Measuring Machines | High-precision geometric measurement | CRYSTA-Apex V Series | Automotive, aerospace, robotics |
| Handheld/Digital Gauges | Length/angle measurement | Calipers, micrometers, dial indicators | Manufacturing, inspection |
| Vision/Form Measurement | Non-contact and contour measurement | Quick Vision, FORMTRACER | Electronics, molds |
| Sensors and Systems | Probes, controllers, software | SP25M, UC480, MCOSMOS | CMM, production lines |

## Representative Products

### Mitutoyo CRYSTA-Apex V Series CNC Coordinate Measuring Machine

> Mitutoyo CRYSTA-Apex V Series CNC Coordinate Measuring Machine: Please visit the [official page](https://www.mitutoyo.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | CNC Bridge-type CMM | Mitutoyo product manual |
| Measuring Range | 500×400×400 mm to 2000×4000×1500 mm (multiple models) | Mitutoyo product manual |
| Length Measurement Error E0,MPE | (1.7 + 4L/1000) µm (SP25M, V544/776) | Mitutoyo product manual |
| Resolution | 0.1 µm | Mitutoyo product manual |
| Maximum Drive Speed | 519 mm/s (3-axis combined) | Mitutoyo product manual |
| Maximum Acceleration | 2309 mm/s² | Mitutoyo product manual |
| Probe System | TP200 / SP25M / Optical/Laser scanning probe | Mitutoyo product manual |
| Controller | UC480 | Mitutoyo product manual |
| Temperature Compensation | 16℃ – 26℃ real-time compensation | Mitutoyo product manual |
| Air Supply | 0.4 MPa | Mitutoyo product manual |
| Weight | Approx. 542 kg (V544) / 1675 kg (V776) | Mitutoyo product manual |
| Price | Not disclosed | - |

**Technical Highlights**: High-rigidity air-bearing bridge structure, sub-micron accuracy, UC480 multi-sensor controller, real-time temperature compensation, and IoT quality management interface.

**Application Scenarios**: Geometric inspection of robot joints/reducers, automotive parts, aerospace structural components, molds, electronic connector inspection.

### Mitutoyo Quick Vision ELF Vision Measuring System

> Mitutoyo Quick Vision ELF Vision Measuring System: Please visit the [official page](https://www.mitutoyo.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | CNC Vision Measuring System | Mitutoyo official website |
| Feature | Non-contact high-speed measurement | Mitutoyo official website |
| Application | Electronics, injection-molded parts, small components | Mitutoyo official website |
| Price | Not disclosed | - |

**Technical Highlights**: Auto-focus, image edge detection, suitable for batch inspection of small-sized parts.

**Application Scenarios**: 3C structural components, connectors, medical devices.

## Supply Chain Position

- **Upstream Key Components/Materials**: Granite, air bearings, ABS linear scales, probe sensors, controllers, measurement software
- **Downstream Customers/Application Scenarios**: Automotive, aerospace, electronics, medical devices, robotic component manufacturers
- **Main Competitors/Peers**: Hexagon, ZEISS, Wenzel, Nikon Metrology

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_mitutoyo`
- Product Entity: `ent_product_mitutoyo_crysta_apex_v`
- Component Entity: `ent_component_mitutoyo_crysta_apex_cmm`
- Key Relationships:
  - `ent_company_mitutoyo` -- `manufactures` --> `ent_product_mitutoyo_crysta_apex_v`
  - `ent_company_mitutoyo` -- `manufactures` --> `ent_component_mitutoyo_crysta_apex_cmm`
  - `ent_product_mitutoyo_crysta_apex_v` -- `uses` --> `ent_component_mitutoyo_crysta_apex_cmm`

## References

1. [Mitutoyo Official Website](https://www.mitutoyo.com)
2. [Mitutoyo CRYSTA-Apex V Series CNC CMM Product/Information Page](https://www.mitutoyo.com.sg/sg-en/product/detail/crysta-apex-v-series)
3. Company annual reports, product datasheets, and public press releases
4. [Appendix D Product Catalog](../index-products.md)
