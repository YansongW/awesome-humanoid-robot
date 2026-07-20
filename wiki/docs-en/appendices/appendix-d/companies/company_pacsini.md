# Pacsini Technology

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 帕西尼感知科技 |
| **English Name** | Pacsini Technology |
| **Headquarters** | Shenzhen, China |
| **Founded** | 2021 |
| **Website** | [https://paxini.com](https://paxini.com) |
| **Supply Chain Segment** | Multi-dimensional tactile sensors, tactile dexterous hands, humanoid robots |
| **Enterprise Type** | Private enterprise, high-tech enterprise |
| **Parent Company/Group** | Independently operated (strategic investments from BYD, JD.com, etc.) |
| **Data Source** | Pacsini official website, public reports, Science and Technology Daily |

## Company Profile

Pacsini Technology is one of the few companies in China to achieve independent control over high-precision multi-dimensional tactile sensors and possess a full-stack product matrix of "sensor—dexterous hand—humanoid robot."

Based on 6D Hall array multi-dimensional tactile sensing technology, the company has launched products including the PX-6AX tactile sensing unit, the DexH13 multi-dimensional tactile dexterous hand, and the TORA-ONE humanoid robot. Its core tactile sensors can recognize fine forces as low as 0.01 N, simultaneously capturing 15 types of tactile information such as three-dimensional force, three-dimensional torque, contact position, material, temperature, hardness, and rebound. These are widely used in humanoid robot dexterous manipulation, precision assembly, logistics sorting, and healthcare services.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Multi-dimensional Tactile Sensors | Robot tactile perception | PX-6AX GEN2 | Dexterous hands, electronic skin, precision operations |
| Tactile Dexterous Hands | Multi-dimensional tactile + AI vision dual-modal end-effector | DexH13 / DexH5 | Humanoid robots, industrial assembly, logistics |
| Humanoid Robots | Wheeled embodied intelligent robot | TORA-ONE | Security inspection, logistics, retail, healthcare |
| Tactile Solutions | Data services and algorithms | OmniVTLA model | Cross-scenario tactile-vision modality alignment |

## Representative Products

### Pacsini DexH13 Multi-dimensional Tactile Dexterous Hand

> Pacsini DexH13: Please visit [official materials](https://paxini.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Number of Fingers | 4 | Official website public information |
| Degrees of Freedom | 16 (13 active + 3 passive) | Official website public information |
| Tactile Sensing Units | 1140 ITPU multi-dimensional tactile sensing units | Official website public information |
| Tactile Signal Channels | 3420 channels | Official website public information |
| Vision Capability | 8-megapixel high-definition RGB AI hand-eye camera | Official website public information |
| Tactile Perception Capability | 15 types (including 3D force/torque, temperature, material, hardness, etc.) | Official website public information |
| Fingertip Force | 15 N | Official website public information |
| Rated Load | 5 kg | Official website public information |
| Maximum Grip Diameter | 15 cm | Official website public information |
| Minimum Opening/Closing Time | 1.5 s | Official website public information |
| Drive Method | Coreless motor drive | Official website public information |
| Communication Protocol | EtherCAT / Modbus | Official website public information |
| Service Life | 1 million cycles | Official website public information |
| Force Control Resolution | 0.01 N | Public reports |
| Sampling Frequency | 1000 Hz | Public reports |
| Price | Not disclosed | - |

**Technical Highlights**: The industry's first dual-modal dexterous hand combining multi-dimensional tactile and AI vision, featuring millimeter-level pressing positioning accuracy and million-cycle industrial-grade lifespan.

**Application Scenarios**: Humanoid robot dexterous manipulation, precision assembly, logistics sorting, medical healthcare, retail services.

### Pacsini PX-6AX GEN2 Multi-dimensional Tactile Sensing Unit

> Pacsini PX-6AX: Please visit [official materials](https://paxini.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Sensing Dimensions | 6D (3D force + 3D torque) | Public reports |
| Tactile Information | 15 types including pressure, temperature, texture, hardness, rebound | Public reports |
| Force Recognition Accuracy | As low as 0.01 N | Public reports |
| Sampling Rate | 1000 Hz | Public reports |
| Service Life | Over 3 million presses | Public reports |
| Scanning Principle | 6D Hall array | Public reports |
| Dimensions | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: High manufacturability design and automated calibration solve industry pain points of poor tactile sensor consistency and complex calibration.

**Application Scenarios**: Robot electronic skin, dexterous hand fingertips, industrial inspection, medical prosthetics, smart wearables.

## Supply Chain Position

- **Upstream Key Components/Materials**: Hall sensor arrays, flexible substrates, nano-sensitive materials, coreless motors, AI vision modules, signal processing ASICs
- **Downstream Customers/Application Scenarios**: Humanoid robot OEMs, industrial robots, logistics warehousing, medical healthcare, automotive OEMs
- **Main Competitors/Peers**: Tashan Technology, Lingxin Qiaoshou, Unitree Dex5, Shadow Hand

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_pacsini`
- Component Entity: `ent_component_pacsini_px6ax`
- Product Entity: `ent_product_pacsini_dexh13`
- Product Entity: `ent_product_pacsini_tora_one`
- Key Relationships:
  - `ent_company_pacsini` -- `manufactures` --> `ent_component_pacsini_px6ax`
  - `ent_company_pacsini` -- `manufactures` --> `ent_product_pacsini_dexh13`
  - `ent_company_pacsini` -- `manufactures` --> `ent_product_pacsini_tora_one`
  - `ent_product_pacsini_dexh13` -- `uses` --> `ent_component_pacsini_px6ax`

## References

1. [Pacsini Technology Official Website](https://paxini.com)
2. [Pacsini DexH13 Product Page](https://paxini.com/cn/dex/gen2)
3. [Science and Technology Daily – BYD Invests in Pacsini](https://www.stdaily.com/web/gdxw/2025-04/28/content_332431.html)
4. [36Kr – Humanoid Robots Touching the World](https://m.36kr.com/p/3006232413757953)
5. [Appendix D Product Catalog](../index-products.md)
