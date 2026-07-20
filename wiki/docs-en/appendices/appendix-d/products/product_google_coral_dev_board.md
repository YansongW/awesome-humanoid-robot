# Google Coral Dev Board

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Google Coral / Google Coral](../companies/company_google_coral.md) |
| **Product Category** | Edge AI Development Board / Edge TPU Evaluation Platform |
| **Release Date** | 2019 |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [Coral Dev Board Product Page](https://coral.ai/products/dev-board/) |

## Product Overview

The Google Coral Dev Board is an AI development board integrating an Edge TPU, featuring a detachable SoM design. Its Edge TPU delivers 4 TOPS INT8 computing power with a typical power consumption of only about 2 W, enabling efficient local execution of quantized models such as MobileNet and EfficientDet-Lite. The development board offers Raspberry Pi-compatible 40-pin GPIO, MIPI CSI/DSI, HDMI, USB 3.0, and Gigabit Ethernet, making it suitable for rapid prototyping in robot perception, smart cameras, and industrial vision.

## Product Image

> Google Coral Dev Board: Please visit the [official page](https://coral.ai/products/dev-board/) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| SoC | NXP i.MX 8M (Quad-core Cortex-A53 + Cortex-M4F) | Coral Public Information |
| AI Accelerator | Google Edge TPU | Coral Public Information |
| AI Computing Power | Up to 4 TOPS INT8 | Coral Public Information |
| Energy Efficiency | Approximately 2 TOPS/W | Coral Public Information |
| Memory | 1 GB / 4 GB LPDDR4 (depending on version) | Coral Public Information |
| Storage | 8 GB / 16 GB / 64 GB eMMC + MicroSD | Coral Public Information |
| Process Node | Edge TPU not disclosed; i.MX 8M 14 nm | Coral Public Information |
| Interfaces | USB 3.0, GbE, HDMI 2.0, MIPI CSI/DSI, 40-pin GPIO, PCIe (SoM) | Coral Public Information |
| Power Consumption | Approximately 5 W typical (full board) | Coral Public Information |
| Dimensions | Approximately 88 mm × 60 mm (with heatsink) | Coral Public Information |
| Price | Dev Board approximately 150 USD (reference price) | Coral Public Information |

## Supply Chain Position

- **Manufacturer**: [Google Coral / Google Coral](../companies/company_google_coral.md)
- **Core Components/Technology Sources**: Google self-developed Edge TPU, NXP i.MX 8M SoC, LPDDR4/eMMC, PMIC, carrier board/heatsink
- **Downstream Applications/Customers**: Robot OEMs, AIoT solution providers, smart camera manufacturers, universities and developer communities

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_google_coral_dev_board`
- Component Entity: `ent_component_google_coral_edge_tpu`
- Manufacturer Entity: `ent_company_google_coral`
- Key Relationships:
  - `rel_ent_company_google_coral_manufactures_ent_product_google_coral_dev_board` (`ent_company_google_coral` → `manufactures` --> `ent_product_google_coral_dev_board`)
  - `rel_ent_company_google_coral_manufactures_ent_component_google_coral_edge_tpu` (`ent_company_google_coral` → `manufactures` --> `ent_component_google_coral_edge_tpu`)
  - `ent_product_google_coral_dev_board` -- `uses` --> `ent_component_google_coral_edge_tpu`

## Application Scenarios

- **Robot Edge Perception**: Real-time object detection, semantic segmentation, and navigation assistance, reducing cloud dependency
- **Smart Camera Prototyping**: Local event detection and facial recognition, enhancing privacy and response speed
- **Industrial Vision Inspection**: Defect classification, barcode/QR code recognition, and production line quality inspection

## Competitive Comparison

| Comparison Item | Coral Dev Board | NVIDIA Jetson Nano | Raspberry Pi 5 + AI HAT |
|---|---|---|---|
| Computing Power | 4 TOPS | 0.5 TFLOPS | 13 TOPS |
| Power Consumption | Approximately 5 W | 5–10 W | Approximately 7 W |
| Ecosystem | TensorFlow Lite | JetPack / CUDA | Raspberry Pi / Hailo |

## Selection and Deployment Recommendations

Prioritize using the Edge TPU Compiler to quantize and compile TensorFlow Lite models; confirm host interface and driver versions; for mass production, consider using Coral SoM custom carrier boards to optimize BOM.

## Related Entries

- [Manufacturer: Google Coral / Google Coral](../companies/company_google_coral.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [Coral Dev Board Product Page](https://coral.ai/products/dev-board/)
2. [Coral Official Documentation](https://coral.ai/docs/)
3. [Coral Dev Board Datasheet](https://coral.ai/docs/dev-board/datasheet/)
