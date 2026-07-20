# SynTouch (USA)

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | SynTouch |
| **English Name** | SynTouch LLC |
| **Headquarters** | California, USA |
| **Founded** | 2008 |
| **Website** | [https://www.syntouchllc.com](https://www.syntouchllc.com) |
| **Supply Chain Role** | Bionic Tactile Sensors, Machine Touch, Tactile Characterization Services |
| **Enterprise Type** | Private Enterprise, High-Tech Enterprise |
| **Parent Company/Group** | Independent Operation |
| **Data Source** | SynTouch Official Website, BioTac Product Manual, Academic Papers |

## Company Profile

SynTouch is a world-leading bionic tactile sensing technology company, founded in 2008 by researchers from the University of Southern California (USC). The company's core product, BioTac, is a bionic tactile sensor that mimics the mechanical structure and perception capabilities of the human fingertip, capable of simultaneously detecting force, vibration, and temperature. It is widely used in robotic dexterous manipulation, prosthetics, tactile characterization, and academic research.

SynTouch's vision is to endow machines with human-like touch through bionic methods. The BioTac integrates a flexible skin, conductive liquid, pressure sensor, electrode array, and thermal sensor into a compact fingertip form, enabling highly robust tactile perception without exposing electronic components to the external environment. The company also offers extended products such as NumaTac and BioTac SP, as well as integration solutions with mainstream dexterous hands like the Shadow Hand and Allegro Hand.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|---|---|---|---|
| Bionic Fingertip Tactile Sensor | Human-like Fingertip Multimodal Touch | BioTac | Robotic Dexterous Hands, Prosthetics, Research |
| Single-Phalanx Tactile Sensor | Miniaturized Solution with Higher Robustness | BioTac SP | Industrial Dexterous Hands, Service Robots |
| Large-Area Flexible Tactile Sensor | Low-Cost, Shapeable Sensing | NumaTac | Robotic Arms, Safety Protection |
| Tactile Characterization Service | Quantification of Material Tactile Properties | SynTouch Standard | Materials R&D, Quality Control |

## Representative Products

### SynTouch BioTac Bionic Tactile Sensor

![SynTouch BioTac](https://www.syntouchllc.com/Products/BioTac/_media/BioTac_485.jpg)

> Image source: SynTouch official product page. If the link is invalid, please replace it with an official public image URL.

| Specification | Value | Notes/Source |
|---|---|---|
| Dimensions | Human-like Fingertip Size | Official Website Public Info |
| Weight | Not disclosed | - |
| Sensing Principle | Fluid Pressure + Electrode Impedance + Thermal Conduction | Official Website Public Info |
| Perception Dimensions | Force, Vibration, Temperature, Heat Flow | Official Website Public Info |
| Number of Electrodes | 19 Sensing Electrodes + 4 Excitation Electrodes | Academic Papers |
| Force Range | 0 – 50 N | BioTac Manual |
| Force Resolution | 10 mN | BioTac Manual |
| Pressure Range | 0 – 100 kPa | BioTac Manual |
| Pressure Resolution | 37 Pa | BioTac Manual |
| Vibration Range | ±760 Pa | BioTac Manual |
| Vibration Resolution | 0.4 Pa | BioTac Manual |
| Temperature Range | 0 – 75 ℃ | BioTac Manual |
| Temperature Resolution | 0.1 ℃ | BioTac Manual |
| Electrode Impedance Sampling Rate | 100 Hz | Academic Papers |
| Vibration Sampling Rate | 2200 Hz | Academic Papers |
| Communication Interface | Integrated Electronic Module + Host Communication | Official Website Public Info |
| Price | Not disclosed | - |

**Technical Highlights**: The world's most representative bionic fingertip tactile sensor, with all electronic components encapsulated inside a rigid core, a replaceable flexible skin, and compliance and multimodal perception capabilities close to those of the human fingertip.

**Application Scenarios**: Robotic dexterous manipulation, prosthetic tactile feedback, material tactile characterization, object texture/hardness/temperature recognition, slip detection.

### SynTouch BioTac SP Single-Phalanx Tactile Sensor

> SynTouch BioTac SP: Please visit the [official page](https://www.syntouchllc.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Number of Electrodes | 24 (Increased compared to BioTac) | Official Website Public Info |
| Normal Force Capacity | >200 N | Official Website Public Info |
| Volume | Approximately half of BioTac | Official Website Public Info |
| Perception Dimensions | Force, Vibration, Temperature | Official Website Public Info |
| Status | Beta Release | Official Website Public Info |
| Price | Not disclosed | - |

**Technical Highlights**: Integrates more sensors in a smaller volume, offering greater mechanical robustness, suitable for industrial-grade high-load dexterous hands.

**Application Scenarios**: Industrial assembly, service robots, prosthetics and rehabilitation equipment.

## Supply Chain Position

- **Upstream Key Components/Materials**: Flexible silicone skin, conductive liquid, pressure sensor, electrode array, thermal sensor, signal processing circuit
- **Downstream Customers/Application Scenarios**: Robotic dexterous hand OEMs, prosthetic manufacturers, research institutions, materials companies, medical rehabilitation
- **Main Competitors/Comparables**: Pacsini, XELA Robotics, Tashan Technology, Shadow Robot Company

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_syntouch`
- Product Entity: `ent_product_syntouch_biotac`
- Component Entity: `ent_component_syntouch_biotac_transducer`
- Key Relationships:
  - `ent_company_syntouch` -- `manufactures` --> `ent_product_syntouch_biotac`
  - `ent_company_syntouch` -- `manufactures` --> `ent_component_syntouch_biotac_transducer`
  - `ent_product_syntouch_biotac` -- `uses` --> `ent_component_syntouch_biotac_transducer`

## References

1. [SynTouch Official Website](https://www.syntouchllc.com)
2. [SynTouch BioTac Product Page](https://www.syntouchllc.com/Products/BioTac/)
3. [BioTac Brochure](https://www.syntouchllc.com/Products/BioTac/_media/BioTac_Brochure.pdf)
4. [Interpreting and Predicting Tactile Signals for the SynTouch BioTac (arXiv)](https://arxiv.org/pdf/2101.05452.pdf)
5. [Appendix D Product Catalog](../index-products.md)
