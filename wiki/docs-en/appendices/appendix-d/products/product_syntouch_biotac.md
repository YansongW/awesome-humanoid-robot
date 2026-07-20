# SynTouch BioTac Biomimetic Tactile Sensor

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [SynTouch](../companies/company_syntouch.md) |
| **Product Category** | Biomimetic Multimodal Tactile Sensor |
| **Release Date** | Continuously iterated since 2008 |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [SynTouch Official Website](https://www.syntouchllc.com) |

## Product Overview

The SynTouch BioTac is one of the world's first and most widely used biomimetic fingertip tactile sensors in both academia and industry. Its design mimics the mechanical structure and perception capabilities of the human fingertip: a rigid bone-like core is covered with a replaceable elastic skin, and the space between the skin and core is filled with a conductive liquid. When the sensor contacts an object, deformation of the skin and liquid layer changes the impedance of the electrode array on the core's surface, while a pressure sensor detects liquid vibrations, and a thermal element senses temperature and heat flow.

The BioTac can simultaneously output three types of tactile information: force, vibration, and temperature. It supports functions such as slip detection, contact localization, texture recognition, hardness estimation, and edge/corner identification. All electronics are encapsulated inside the rigid core, and the flexible skin is replaceable, offering high robustness and maintainability.

## Product Image

![SynTouch BioTac](https://www.syntouchllc.com/Products/BioTac/_media/BioTac_485.jpg)

> Image source: SynTouch official product materials. If replacement is needed, please use an official public image URL.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Sensing Principle | Fluid pressure + Electrode impedance + Thermal conduction | Official public information |
| Perception Dimensions | Force, Vibration, Temperature, Heat flow | Official public information |
| Number of Electrodes | 19 sensing electrodes + 4 excitation electrodes | Academic papers |
| Dimensions | Human-like fingertip size | Official public information |
| Weight | Not disclosed | - |
| Force Range | 0 – 50 N | BioTac Manual |
| Force Resolution | 10 mN | BioTac Manual |
| Pressure Range | 0 – 100 kPa | BioTac Manual |
| Pressure Resolution | 37 Pa | BioTac Manual |
| Vibration Range | ±760 Pa | BioTac Manual |
| Vibration Resolution | 0.4 Pa | BioTac Manual |
| Temperature Range | 0 – 75 ℃ | BioTac Manual |
| Temperature Resolution | 0.1 ℃ | BioTac Manual |
| Heat Flow Range | ±1 ℃/s | BioTac Manual |
| Heat Flow Resolution | 0.001 ℃/s | BioTac Manual |
| Electrode Impedance Sampling Rate | 100 Hz | Academic papers |
| Vibration Sampling Rate | 2200 Hz | Academic papers |
| Communication Interface | Integrated electronic module + Host communication | Official public information |
| Integration Solutions | Shadow Hand / Allegro Hand / PR2, etc. | Official public information |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [SynTouch](../companies/company_syntouch.md)
- **Core Components/Technology Source**: Self-developed flexible skin, conductive liquid, electrode array, pressure sensor, thermal element; signal processing circuit integrated inside the core.
- **Downstream Applications/Customers**: Robotic dexterous hands, prosthetics, research institutions, material characterization, medical rehabilitation.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_syntouch_biotac`
- Manufacturer Entity: `ent_company_syntouch`
- Component Entity: `ent_component_syntouch_biotac_transducer`
- Key Relationships:
  - `rel_ent_company_syntouch_manufactures_ent_product_syntouch_biotac` (`ent_company_syntouch` → `manufactures` --> `ent_product_syntouch_biotac`)
  - `rel_ent_company_syntouch_manufactures_ent_component_syntouch_biotac_transducer` (`ent_company_syntouch` → `manufactures` --> `ent_component_syntouch_biotac_transducer`)
  - `rel_ent_product_syntouch_biotac_uses_ent_component_syntouch_biotac_transducer` (`ent_product_syntouch_biotac` → `uses` --> `ent_component_syntouch_biotac_transducer`)

## Application Scenarios

- **Robotic Dexterous Manipulation**: Grasping, twisting, pressing, slip detection, and material recognition.
- **Prosthetic Tactile Feedback**: Provides force/temperature perception close to human skin for upper limb prosthetics.
- **Material Tactile Characterization**: Quantifies tactile dimensions such as roughness, friction, compliance, and thermal properties of materials.
- **Research and Education**: Standard sensor for tactile perception algorithms, biomimetic robotics, and human-robot interaction research.

## Competitive Comparison

| Comparison Item | SynTouch BioTac | PX-6AX (Pacini) | XELA uSkin |
|----------------|-----------------|-----------------|------------|
| Sensing Principle | Fluid/Electrode/Thermal conduction | 6D Hall array | Magnetoresistive 3-axis |
| Perception Modalities | Force + Vibration + Temperature | 15 types of tactile information | 3-axis force |
| Form Factor | Biomimetic fingertip | Sensing unit/dexterous hand | Flexible skin patch |
| Core Advantage | Biomimetic, robust, replaceable skin | High density, localized production | Soft, easy to integrate |

## Selection and Deployment Recommendations

- Select the corresponding integration kit (Shadow, Allegro, PR2, etc.) based on the target dexterous hand.
- The flexible skin is a consumable; it is recommended to stock spare parts based on usage frequency.
- Vibration and temperature data require high-level surface processing algorithms; it is recommended to use SynTouch software or develop a custom calibration process.

## References

1. [SynTouch Official Website](https://www.syntouchllc.com)
2. [SynTouch BioTac Product Page](https://www.syntouchllc.com/Products/BioTac/)
3. [BioTac Brochure](https://www.syntouchllc.com/Products/BioTac/_media/BioTac_Brochure.pdf)
4. [Interpreting and Predicting Tactile Signals for the SynTouch BioTac (arXiv)](https://arxiv.org/pdf/2101.05452.pdf)
5. [Appendix D Company Directory](../index-companies.md)
