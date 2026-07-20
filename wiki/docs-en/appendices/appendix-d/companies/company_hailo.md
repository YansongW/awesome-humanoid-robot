# Hailo

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Hailo (Israel Edge AI Chip Company) |
| **English Name** | Hailo Technologies |
| **Headquarters** | Tel Aviv, Israel |
| **Founded** | 2017 |
| **Website** | [https://hailo.ai](https://hailo.ai) |
| **Supply Chain Role** | Edge AI Processors, On-device NPU, Robotics/Automotive Vision |
| **Company Type** | Unicorn, Private Company |
| **Parent Company/Group** | None (Independent Entity) |
| **Data Sources** | Hailo Official Website, Product Manuals, Public Press Releases, Industry Research Reports |

## Company Overview

Hailo is a leading Israeli edge AI chip company, specializing in high-performance, low-power neural network processors for edge devices.

Hailo's Hailo-8 AI processor adopts an innovative dataflow architecture, delivering high TOPS computing power at typical power consumption. It is widely used in automotive ADAS, smart cameras, industrial inspection, robotics, and drones. The Hailo-15 further integrates ISP and AI, targeting smart camera SoCs. Hailo provides a complete SDK and model optimization tools, supporting mainstream deep learning frameworks.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Hailo-8 | Edge AI Accelerator | Hailo-8 / Hailo-8L | Robotics, Automotive, Security, Industrial |
| Hailo-15 | Vision Processor with Integrated ISP | Hailo-15 | Smart Cameras, AIoT |
| Development Kits | Evaluation and Prototyping | Hailo-8 M.2 / PCIe Development Kits | Developers, Solution Providers |
| Software Stack | Model Optimization and Inference | Hailo Dataflow Compiler / TAPPAS | Full Chip Series |

## Representative Products

### Hailo-8 AI Processor

> Hailo-8 AI Processor: Please visit [Official Documentation](https://hailo.ai) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Architecture | Dataflow Architecture | Hailo Public Information |
| Computing Power | Up to 26 TOPS INT8 | Hailo Public Information |
| Energy Efficiency | Approx. 3 TOPS/W Typical | Hailo Public Information |
| Process Node | 16 nm (Public Reports) | Public Reports |
| Interfaces | PCIe Gen3 / M.2 / BGA Package | Hailo Public Information |
| Dimensions | Approx. 15 mm × 15 mm (BGA) | Hailo Public Information |
| Power Consumption | Approx. 2.5 W Typical | Hailo Public Information |
| Price | Not Disclosed | - |

**Technical Highlights**: High utilization with dataflow architecture, low power with high computing power, support for multi-precision quantization, small size for easy integration.

**Application Scenarios**: On-device perception for robotics, ADAS, smart cameras, industrial quality inspection, drones, AIoT.

### Hailo-15 Vision Processor

> Hailo-15 Vision Processor: Please visit [Official Documentation](https://hailo.ai) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Positioning | Vision Processor with Integrated ISP and AI | Hailo Public Information |
| AI Computing Power | Up to 20 TOPS INT8 | Hailo Public Information |
| ISP | Integrated High-Performance ISP | Hailo Public Information |
| Video | Supports Multiple High-Resolution Video Streams | Hailo Public Information |
| Interfaces | MIPI, Ethernet, USB, etc. | Hailo Public Information |
| Power Consumption | Not Disclosed | - |
| Application Scenarios | Smart Cameras, Robotic Vision, AIoT | Hailo Public Information |
| Price | Not Disclosed | - |

**Technical Highlights**: ISP+AI single chip, end-to-end vision processing, reduces system cost and power consumption.

**Application Scenarios**: Smart security cameras, robot navigation, facial recognition, industrial vision inspection.

## Supply Chain Position

- **Upstream Key Components/Materials**: Wafer foundry, packaging and testing, memory, ISP IP, PCB/modules.
- **Downstream Customers/Application Scenarios**: Automotive Tier1/OEM, security equipment manufacturers, industrial camera companies, robot OEMs, AIoT device vendors.
- **Main Competitors/Peers**: Intel Movidius, Qualcomm QCS, Horizon Journey, Ambarella, Renesas R-Car.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_hailo`
- Product Entity: `ent_product_hailo_8`
- Component Entity: `ent_component_hailo_8_npu`
- Key Relationships:
  - `ent_company_hailo` -- `manufactures` --> `ent_product_hailo_8`
  - `ent_company_hailo` -- `manufactures` --> `ent_component_hailo_8_npu`
  - `ent_product_hailo_8` -- `uses` --> `ent_component_hailo_8_npu`

## References

1. [Hailo Official Website](https://hailo.ai)
2. [Hailo-8 Product Page](https://hailo.ai/products/hailo-8/)
3. [Hailo-15 Product Page](https://hailo.ai/products/hailo-15/)
