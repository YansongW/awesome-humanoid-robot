# Renesas Electronics

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Renesas Electronics |
| **English Name** | Renesas Electronics |
| **Headquarters** | Tokyo, Japan |
| **Founded** | 2010 (merger of NEC Electronics and Hitachi/Mitsubishi semiconductor businesses) |
| **Website** | [https://www.renesas.com](https://www.renesas.com) |
| **Supply Chain Role** | MCU/MPU, Edge AI, Automotive Electronics, Industrial Control, Robot Vision |
| **Enterprise Type** | Public Company (TSE: 6723) |
| **Parent Company/Group** | None (Renesas Electronics is the listed entity) |
| **Data Source** | Renesas official website, RZ/V product manuals, public press releases, industry research reports |

## Company Overview

Renesas Electronics is a world-leading supplier of MCU/MPU and analog semiconductors, with products widely used in automotive, industrial, and infrastructure applications. Its RZ/V series AI MPU integrates the proprietary DRP-AI accelerator, achieving high TOPS visual inference at extremely low power consumption; the RA/RX/RL series MCUs cover a broad range from sensor nodes to real-time control. Renesas also provides a complete AI toolchain and reference designs to support rapid deployment in robotics, smart cameras, and industrial vision.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| RZ/V Series | Vision AI MPU / DRP-AI Accelerator | RZ/V2H / RZ/V2N | Robotics, Smart Cameras, Industrial Vision, ADAS |
| RA / RX / RL MCU | Real-time Control & Security MCU | RA8 / RX700 | Motor Control, Sensor Nodes, Functional Safety |

## Representative Products

### Renesas RZ/V2H

> Renesas RZ/V2H: Please visit [Official Documentation](https://www.renesas.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Process Node | Not disclosed | Renesas public information |
| CPU | Quad-core Arm Cortex-A55 @ 1.8 GHz + Dual-core Cortex-R8 @ 800 MHz + Cortex-M33 @ 200 MHz | Renesas public information |
| AI Accelerator | DRP-AI3 (Dynamically Reconfigurable Processor + AI-MAC) | Renesas public information |
| AI Performance | 8 TOPS (dense models) / Up to 80 TOPS (sparse models) | Renesas public information |
| ISP | Optional Arm Mali-C55 ISP | Renesas public information |
| GPU | GE3D 3D GPU | Renesas public information |
| Memory | LPDDR4 / LPDDR4X interface | Renesas public information |
| Interfaces | PCIe Gen3 x4, USB 3.2 Gen2 x2, GbE x2, MIPI CSI-2 x4, CAN-FD x6 | Renesas public information |
| Power Consumption | Not disclosed (typically below 10 W) | Renesas public information |
| Package | BGA 19 mm × 19 mm, 1368 pins | Renesas public information |
| Price | Not disclosed | Renesas public information |

**Technical Highlights**: DRP-AI3 high performance with low power consumption, supports INT8 quantization and pruning, quad MIPI CSI, PCIe/USB 3.2 high-speed interfaces, fanless operation for high-load AI.

**Application Scenarios**: **Autonomous Mobile Robots**: multi-channel visual perception, SLAM, dynamic obstacle avoidance and path planning; **Smart Industrial Cameras**: high-speed defect detection, object recognition and measurement, no external accelerator required; **Vision-Guided Robots**: real-time pose estimation and grasping positioning, supports Transformer/CNN hybrid networks.

### Renesas RZ/V2N

> Renesas RZ/V2N: Please visit [Official Documentation](https://www.renesas.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| CPU | Quad-core Cortex-A55 + Cortex-M33 | Renesas public information |
| AI Accelerator | DRP-AI3 | Renesas public information |
| AI Performance | Up to 15 TOPS (sparse) | Renesas public information |
| Power Consumption | Low-power fanless design | Renesas public information |
| Interfaces | MIPI CSI, PCIe, USB, GbE, CAN-FD | Renesas public information |
| Package | 15 mm × 15 mm | Renesas public information |
| Price | Not disclosed | Renesas public information |

**Technical Highlights**: Smaller package, lower power consumption, inherits the DRP-AI3 architecture from RZ/V2H, suitable for high-volume vision AI devices.

**Application Scenarios**: Smart security cameras, traffic monitoring, industrial vision, service robots.

## Supply Chain Position

- **Upstream Key Components/Materials**: Renesas proprietary DRP-AI IP, ARM CPU/ISP IP, TSMC foundry, LPDDR4x, packaging and testing, PMIC
- **Downstream Customers/Application Scenarios**: Automotive OEMs/Tier1, industrial automation vendors, robotics companies, smart camera and security customers
- **Main Competitors/Comparables**: NXP i.MX, Texas Instruments Jacinto, NVIDIA Jetson, Horizon Journey, Ambarella

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_renesas`
- Product Entities: `ent_product_renesas_rz_v2h`, `ent_product_renesas_rz_v2n`
- Component Entities: `ent_component_renesas_rz_v2h_soc`, `ent_component_renesas_rz_v2n_soc`
- Key Relationships:
  - `ent_company_renesas` -- `manufactures` --> `ent_product_renesas_rz_v2h`
  - `ent_company_renesas` -- `manufactures` --> `ent_product_renesas_rz_v2n`
  - `ent_company_renesas` -- `manufactures` --> `ent_component_renesas_rz_v2h_soc`
  - `ent_company_renesas` -- `manufactures` --> `ent_component_renesas_rz_v2n_soc`
  - `ent_product_renesas_rz_v2h` -- `uses` --> `ent_component_renesas_rz_v2h_soc`
  - `ent_product_renesas_rz_v2n` -- `uses` --> `ent_component_renesas_rz_v2n_soc`

## References

1. [Renesas Official Website](https://www.renesas.com)
2. [RZ/V2H Product Page](https://www.renesas.com/en/products/rz-v2h)
3. [Renesas RZ/V Series](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rz-v-ai-accelerator)
