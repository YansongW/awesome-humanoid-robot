# Google Coral

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Google Coral |
| **English Name** | Google Coral |
| **Headquarters** | Mountain View, California, USA |
| **Founded** | 2019 (Coral product line launch) |
| **Official Website** | [https://coral.ai](https://coral.ai) |
| **Supply Chain Segment** | Edge TPU, Edge AI Accelerator, AIoT/Robotics Vision |
| **Enterprise Attribute** | Subsidiary of Google / Alphabet (Listed company NASDAQ: GOOGL) |
| **Parent Company/Group** | Alphabet / Google |
| **Data Source** | Coral official website, Google official documentation, public product information |

## Company Profile

Google Coral is an edge AI platform launched by Google, with the core being its self-developed Edge TPU, capable of performing neural network inference at extremely low power consumption. Coral offers various form factors including Dev Board, USB Accelerator, PCIe/M.2 Accelerator, and SoM, targeting smart cameras, robotics, industrial inspection, and AIoT devices. Its software stack is based on TensorFlow Lite and supports the Edge TPU Compiler for efficient deployment of quantized models on the edge.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|---|---|---|---|
| Dev Board / SoM | Integrated SoM development board | Coral Dev Board | AIoT prototyping, robotics perception, edge AI development |
| USB / PCIe / M.2 Accelerator | External Edge TPU accelerator | Coral USB Accelerator | AI upgrade for existing embedded platforms, industrial vision, smart cameras |

## Representative Products

### Coral Dev Board

> Coral Dev Board: Please visit [Official Information](https://coral.ai) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| SoC | NXP i.MX 8M (Quad-core Cortex-A53 + Cortex-M4F) | Coral public information |
| AI Accelerator | Google Edge TPU | Coral public information |
| AI Compute Power | Up to 4 TOPS INT8 | Coral public information |
| Power Efficiency | Approximately 2 TOPS/W | Coral public information |
| Memory | 1 GB / 4 GB LPDDR4 (depending on version) | Coral public information |
| Storage | 8 GB / 16 GB / 64 GB eMMC + MicroSD | Coral public information |
| Process Node | Edge TPU not disclosed; i.MX 8M 14 nm | Coral public information |
| Interfaces | USB 3.0, GbE, HDMI 2.0, MIPI CSI/DSI, 40-pin GPIO, PCIe (SoM) | Coral public information |
| Power Consumption | Approximately 5 W typical (full board) | Coral public information |
| Dimensions | Approximately 88 mm × 60 mm (with heatsink) | Coral public information |
| Price | Dev Board approximately 150 USD (reference price) | Coral public information |

**Technical Highlights**: Removable Coral SoM, heterogeneous integration of Edge TPU and i.MX 8M, Mendel Linux, TensorFlow Lite ecosystem, rapid migration from prototype to custom carrier board.

**Application Scenarios**: **Robotics Edge Perception**: Real-time object detection, semantic segmentation, and navigation assistance, reducing cloud dependency; **Smart Camera Prototyping**: Local event detection and facial recognition, enhancing privacy and response speed; **Industrial Vision Inspection**: Defect classification, barcode/QR code recognition, and production line quality inspection.

### Coral USB Accelerator

> Coral USB Accelerator: Please visit [Official Information](https://coral.ai) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| AI Accelerator | Google Edge TPU | Coral public information |
| AI Compute Power | Up to 4 TOPS INT8 | Coral public information |
| Interface | USB 3.0 Type-C | Coral public information |
| Power Consumption | Approximately 2 W | Coral public information |
| Dimensions | Approximately 65 mm × 30 mm | Coral public information |
| Price | Approximately 75 USD (reference price) | Coral public information |

**Technical Highlights**: Plug-and-play, USB powered, no additional cooling required, quickly adds AI inference capability to existing devices.

**Application Scenarios**: PC/edge box AI expansion, industrial vision, smart cameras, development and validation.

## Supply Chain Position

- **Upstream Key Components/Materials**: TSMC wafer foundry, NXP i.MX 8M SoC, LPDDR4/eMMC, packaging and testing, PCB/module
- **Downstream Customers/Application Scenarios**: AIoT device manufacturers, robotics OEMs, smart camera manufacturers, industrial vision solution providers, developers
- **Main Competitors/Comparables**: Intel Movidius, Hailo, NVIDIA Jetson Nano, Qualcomm QCS, Horizon Robotics Journey

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_google_coral`
- Product Entities: `ent_product_google_coral_dev_board`, `ent_product_google_coral_usb_accelerator`
- Component Entities: `ent_component_google_coral_edge_tpu`, `ent_component_google_coral_edge_tpu_2`
- Key Relationships:
  - `ent_company_google_coral` -- `manufactures` --> `ent_product_google_coral_dev_board`
  - `ent_company_google_coral` -- `manufactures` --> `ent_product_google_coral_usb_accelerator`
  - `ent_company_google_coral` -- `manufactures` --> `ent_component_google_coral_edge_tpu`
  - `ent_company_google_coral` -- `manufactures` --> `ent_component_google_coral_edge_tpu_2`
  - `ent_product_google_coral_dev_board` -- `uses` --> `ent_component_google_coral_edge_tpu`
  - `ent_product_google_coral_usb_accelerator` -- `uses` --> `ent_component_google_coral_edge_tpu_2`

## References

1. [Coral Official Website](https://coral.ai)
2. [Coral Dev Board Product Page](https://coral.ai/products/dev-board/)
3. [Coral Official Documentation](https://coral.ai/docs/)
