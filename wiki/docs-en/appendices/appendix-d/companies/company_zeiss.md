# Carl Zeiss

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 卡尔·蔡司 |
| **English Name** | Carl Zeiss |
| **Headquarters** | Oberkochen, Germany |
| **Founded** | 1846 |
| **Website** | [https://www.zeiss.com](https://www.zeiss.com) |
| **Supply Chain Role** | Optics, Precision Measurement, Coordinate Measuring Machines, Microscopes, Industrial Quality Solutions |
| **Enterprise Type** | Foundation-owned enterprise, global leader in optics and metrology |
| **Parent Company/Group** | Carl Zeiss Foundation (Carl-Zeiss-Stiftung) |
| **Data Source** | ZEISS official website, product brochures, public press releases, annual reports |

## Company Profile

ZEISS is a global leader in optics and optoelectronics. Its Industrial Quality Solutions provide submicron-level geometric, surface, and material inspection for robot components.

Carl Zeiss' business covers semiconductor manufacturing technology, industrial quality and research, medical technology, and consumer optics. The Industrial Quality division offers coordinate measuring machines, optical measurement systems, microscopes, CT, and surface measurement equipment, serving as a core supplier for high-precision inspection of key components such as robot reducers, bearings, gears, and connecting rods.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Coordinate Measuring Machines | Contact high-precision geometric measurement | PRISMO / ACCURA / CONTURA | Precision components, automotive, aerospace |
| Optical & Multi-Sensor Measurement | Non-contact/hybrid measurement | O-INSPECT / COMET | Complex surfaces, small-batch precision parts |
| Microscopes & Surface Analysis | Material and surface micro-inspection | Axio / SmarTact / SEM | Materials research, failure analysis |

## Representative Products

### ZEISS Coordinate Measuring Machine / PRISMO Series

> ZEISS Coordinate Measuring Machine / PRISMO Series: Please visit [official materials](https://www.zeiss.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Measuring Range | From 700×1000×600 mm, multiple specifications | ZEISS product brochure |
| Accuracy | MPE_E up to 0.5 + L/500 µm | ZEISS product brochure |
| Probing System | VAST gold / RDS rotary probe head | ZEISS product brochure |
| Software | CALYPSO | ZEISS official website |
| Structure | Granite, air bearings, high-rigidity bridge | ZEISS product brochure |
| Scanning Technology | Active scanning probe, supports high-speed scanning | ZEISS product brochure |
| Interface | Ethernet | ZEISS product brochure |
| Price | Not disclosed | - |

**Technical Highlights**: Submicron accuracy, active scanning technology, CALYPSO graphical measurement software, suitable for highest-precision component inspection.

**Application Scenarios**: Robot reducer/gear/bearing inspection, automotive powertrain, aerospace precision parts, medical devices.

### ZEISS O-INSPECT Hybrid Measuring Machine

> ZEISS O-INSPECT Hybrid Measuring Machine: Please visit [official materials](https://www.zeiss.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Measuring Range | From 300×200×200 mm | ZEISS product brochure |
| Accuracy | MPE_E approx. 1.5 + L/300 µm | ZEISS product brochure |
| Sensors | Contact probe + optical sensor | ZEISS product brochure |
| Optical Magnification | Zoom lens, high-resolution camera | ZEISS product brochure |
| Software | CALYPSO | ZEISS official website |
| Structure | Compact bridge structure | ZEISS product brochure |
| Application | Hybrid inspection of small parts | ZEISS product brochure |
| Price | Not disclosed | - |

**Technical Highlights**: Integration of contact and optical measurement, suitable for complex small parts, combining high-precision image measurement with 3D tactile probing.

**Application Scenarios**: Electronic connectors, medical devices, precision gears, micro-component inspection for robots.

## Supply Chain Position

- **Upstream Key Components/Materials**: High-precision optical elements, linear encoders, air bearings, granite, probes, industrial software.
- **Downstream Customers/Application Scenarios**: Automotive, aerospace, electronics & semiconductors, medical, robot core component manufacturers.
- **Main Competitors/Peers**: Hexagon, Wenzel, Nikon, Mitutoyo.

## Knowledge Graph Nodes & Relationships

- Company Entity: `ent_company_zeiss`
- Product Entities: `ent_product_zeiss_prismo`, `ent_product_zeiss_oinspect`
- Key Relationships:
  - `ent_company_zeiss` -- `manufactures` --> `ent_product_zeiss_prismo`
  - `ent_company_zeiss` -- `manufactures` --> `ent_product_zeiss_oinspect`
  - `ent_product_zeiss_prismo` -- `uses` --> `ent_component_vast_probe`
  - `ent_product_zeiss_oinspect` -- `uses` --> `ent_component_optical_sensor`

## References

1. [Official Website](https://www.zeiss.com)
2. [ZEISS Official Website](https://www.zeiss.com)
3. ZEISS PRISMO and O-INSPECT product brochures
