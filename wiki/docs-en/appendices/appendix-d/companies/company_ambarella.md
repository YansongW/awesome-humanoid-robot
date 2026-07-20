# Ambarella

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 安霸 |
| **English Name** | Ambarella |
| **Headquarters** | Santa Clara, California, USA |
| **Founded** | 2004 |
| **Official Website** | [https://www.ambarella.com](https://www.ambarella.com) |
| **Supply Chain Role** | Vision AI SoC, ISP, Video Encoding, ADAS/Robotics/Security |
| **Company Type** | Public Company (NASDAQ: AMBA) |
| **Parent Company/Group** | None (Independent listed entity) |
| **Data Source** | Ambarella official website, product manuals, investor press releases, industry research reports |

## Company Profile

Ambarella is a semiconductor company focused on low-power, high-resolution video and edge AI vision processing. Its CVflow architecture AI accelerator integrates ISP, video codec, and multi-sensor fusion capabilities, widely used in security cameras, ADAS, drones, robotics, and industrial vision. New-generation SoCs like CV72 and CV7 adopt 5/4 nm processes, support hybrid Transformer and CNN networks, and offer leading AI performance per watt.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| CV72 / CV72S Series | 5 nm Mainstream Edge AI Vision SoC | CV72S | Professional security, smart cameras, robot vision, industrial inspection |
| CV7 Series | 4 nm Flagship 8K Vision AI SoC | CV7 | High-end security, drones, autonomous driving perception, 8K cameras |

## Representative Products

### Ambarella CV72

> Ambarella CV72: Please visit [official documentation](https://www.ambarella.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Process Node | 5 nm (public reports) | Ambarella public information |
| CPU | Dual-core / Quad-core Arm Cortex-A76 (up to 1.8 GHz depending on version) | Ambarella public information |
| AI Accelerator | 3rd Gen CVflow AI Accelerator | Ambarella public information |
| AI Performance | Approx. 12 TOPS (CV72, public reports) | Ambarella public information |
| ISP | Integrated high-performance ISP, supports low-light HDR, AI-ISP (AISP) | Ambarella public information |
| Video | 4Kp120 / 8Kp30 encoding, multi-stream concurrent | Ambarella public information |
| Memory | Supports LPDDR4x / LPDDR5 / LPDDR5x | Ambarella public information |
| Interfaces | PCIe, USB 3.2, GbE, MIPI CSI, radar fusion interface | Ambarella public information |
| Power Consumption | Typical < 3 W (CV72S, public reports) | Ambarella public information |
| Package | Not disclosed | Ambarella public information |
| Price | Not disclosed | Ambarella public information |

**Technical Highlights**: CVflow 3.0 supports concurrent Transformer and CNN, AI-enhanced ISP, radar-vision fusion, ultra-low power, designed for multi-stream HD cameras.

**Application Scenarios**: **Robot Vision**: Real-time object detection, semantic segmentation, and navigation assistance with multi-camera setups; **Smart Security Cameras**: Edge-side 4K AI analysis, low-light color night vision, face/license plate recognition; **Industrial Vision Inspection**: High-speed defect detection, dimension measurement, OCR and barcode recognition.

### Ambarella CV7

> Ambarella CV7: Please visit [official documentation](https://www.ambarella.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Process Node | 4 nm (public reports) | Ambarella public information |
| CPU | Quad-core Arm Cortex-A73 | Ambarella public information |
| AI Accelerator | 3rd Gen CVflow AI Accelerator | Ambarella public information |
| AI Performance | Over 2.5x improvement over previous generation | Ambarella public information |
| Video | 8Kp60 multi-stream, 4Kp240 encoding | Ambarella public information |
| Power Consumption | Not disclosed | Ambarella public information |
| Price | Not disclosed | Ambarella public information |

**Technical Highlights**: 8K vision AI, 4 nm process, higher CPU performance, designed for flagship AI perception applications.

**Application Scenarios**: 8K action cameras, high-end security, autonomous driving perception, drones, video conferencing.

## Supply Chain Position

- **Upstream Key Components/Materials**: Samsung 5/4 nm wafer foundry, ARM IP, ISP/Video IP, LPDDR5x memory, packaging and testing, modules
- **Downstream Customers/Application Scenarios**: Security camera manufacturers, drone companies, automotive Tier1/OEMs, robot OEMs, video conferencing equipment vendors
- **Main Competitors/Peers**: Qualcomm QCS, NVIDIA Jetson, Horizon Robotics Journey, HiSilicon, Novatek

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_ambarella`
- Product Entities: `ent_product_ambarella_cv72`, `ent_product_ambarella_cv7`
- Component Entities: `ent_component_ambarella_cv72_chip`, `ent_component_ambarella_cv7_chip`
- Key Relationships:
  - `ent_company_ambarella` -- `manufactures` --> `ent_product_ambarella_cv72`
  - `ent_company_ambarella` -- `manufactures` --> `ent_product_ambarella_cv7`
  - `ent_company_ambarella` -- `manufactures` --> `ent_component_ambarella_cv72_chip`
  - `ent_company_ambarella` -- `manufactures` --> `ent_component_ambarella_cv7_chip`
  - `ent_product_ambarella_cv72` -- `uses` --> `ent_component_ambarella_cv72_chip`
  - `ent_product_ambarella_cv7` -- `uses` --> `ent_component_ambarella_cv7_chip`

## References

1. [Ambarella Official Website](https://www.ambarella.com)
2. [Ambarella CV72 Product Page](https://www.ambarella.com/products/aiot-industrial-robotics/cv72-ai-soc/)
3. [Ambarella CV7 Press Release](https://www.ambarella.com/news/ambarella-launches-powerful-edge-ai-8k-vision-soc-with-industry-leading-ai-and-multi-sensor-perception-performance/)
