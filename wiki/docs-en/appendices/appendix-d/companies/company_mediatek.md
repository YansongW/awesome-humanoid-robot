# MediaTek

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 联发科 |
| **English Name** | MediaTek |
| **Headquarters** | Hsinchu, Taiwan, China |
| **Founded** | 1997 |
| **Website** | [https://www.mediatek.com](https://www.mediatek.com) |
| **Supply Chain Role** | Edge AI SoC, AIoT, Mobile/Computing Platform, Robot Main Controller |
| **Company Type** | Public Company (TWSE: 2454) |
| **Parent Company/Group** | None (MediaTek is the listed entity) |
| **Data Sources** | MediaTek official website, Genio product documentation, public press releases, industry research reports |

## Company Overview

MediaTek is a world-leading semiconductor design company, with products covering smartphones, tablets, TVs, wearables, automotive, and AIoT. Its Genio series edge AI platforms target industrial IoT, robotics, and smart devices, integrating multi-core CPUs, GPUs, APUs (AI processors), and rich multimedia interfaces. They achieve a balance of high performance and low power consumption with advanced 6 nm process technology, and offer NeuroPilot SDK and Yocto/Ubuntu support.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| Genio Series | AIoT Edge AI Platform | Genio 1200 / 700 / 510 | Industrial IoT, Robotics, Smart Retail, Digital Signage, Edge Gateway |
| Filogic / Pentonic | Connectivity & Display Platform | Filogic 880 | Wi-Fi 7 Routing, Smart TV, AIoT Gateway |

## Representative Products

### MediaTek Genio 1200

> MediaTek Genio 1200: Please visit [Official Documentation](https://www.mediatek.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Process | 6 nm | MediaTek public data |
| CPU | Octa-core (4× Cortex-A78 @ up to 2.2 GHz + 4× Cortex-A55) | MediaTek public data |
| GPU | Arm Mali-G57 MC5 | MediaTek public data |
| AI Accelerator | MediaTek Multi-core APU | MediaTek public data |
| AI Performance | Up to 4.8 TOPS INT8 | MediaTek public data |
| Vision | Dual ISP, up to 48 MP single / 16 MP+16 MP dual, 4K90 decode | MediaTek public data |
| DSP | Dual Cadence Tensilica VP6 + HiFi 4 Audio DSP | MediaTek public data |
| Memory | Supports LPDDR4X, up to 16 GB | MediaTek public data |
| Interfaces | PCIe 3.0, USB 3.2 Gen1, GbE (TSN), MIPI CSI/DSI, HDMI, UART/I2C/SPI | MediaTek public data |
| Power Consumption | Typical ~6–10 W (full board/module) | MediaTek public data |
| Price | Dev kit ~200–400 USD (reference price) | MediaTek public data |

**Technical Highlights**: 6 nm flagship AIoT SoC, 4.8 TOPS APU, triple 4K display, dual ISP, rich high-speed interfaces, supports Android/Yocto/Ubuntu and ROS.

**Application Scenarios**: **Industrial Robots & AMRs**: Multi-channel visual perception, SLAM, path planning, and robotic arm control; **Smart Cameras & Security**: 4K real-time object detection, facial recognition, and behavior analysis; **Edge AI Gateways & HMIs**: Multi-screen display, device interconnection, and local AI inference.

### MediaTek Genio 700

> MediaTek Genio 700: Please visit [Official Documentation](https://www.mediatek.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Process | 6 nm | MediaTek public data |
| CPU | Octa-core (4× Cortex-A78 + 4× Cortex-A55) | MediaTek public data |
| GPU | Arm Mali-G57 MC3 | MediaTek public data |
| AI Performance | ~4 TOPS | MediaTek public data |
| Video | 4K60 encode/decode | MediaTek public data |
| Interfaces | PCIe, USB 3.0, GbE, MIPI CSI/DSI | MediaTek public data |
| Power Consumption | ~4–8 W | MediaTek public data |
| Price | Not disclosed | MediaTek public data |

**Technical Highlights**: Mid-to-high-end AIoT platform, 6 nm power efficiency, rich multimedia and connectivity capabilities.

**Application Scenarios**: Smart Retail, Industrial HMI, Smart Cameras, Edge Gateways.

## Supply Chain Position

- **Upstream Key Components/Materials**: TSMC 6 nm foundry, ARM CPU/GPU IP, proprietary APU, LPDDR5, UFS, packaging & testing, substrate
- **Downstream Customers/Application Scenarios**: AIoT device manufacturers, robot OEMs, smart retail & digital signage vendors, industrial gateway customers
- **Main Competitors/Comparables**: Qualcomm QCS, NVIDIA Jetson, Rockchip RK3588, Allwinner T527, Amlogic

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_mediatek`
- Product Entities: `ent_product_mediatek_genio_1200`, `ent_product_mediatek_genio_700`
- Component Entities: `ent_component_mediatek_genio_1200_soc`, `ent_component_mediatek_genio_700_soc`
- Key Relationships:
  - `ent_company_mediatek` -- `manufactures` --> `ent_product_mediatek_genio_1200`
  - `ent_company_mediatek` -- `manufactures` --> `ent_product_mediatek_genio_700`
  - `ent_company_mediatek` -- `manufactures` --> `ent_component_mediatek_genio_1200_soc`
  - `ent_company_mediatek` -- `manufactures` --> `ent_component_mediatek_genio_700_soc`
  - `ent_product_mediatek_genio_1200` -- `uses` --> `ent_component_mediatek_genio_1200_soc`
  - `ent_product_mediatek_genio_700` -- `uses` --> `ent_component_mediatek_genio_700_soc`

## References

1. [MediaTek Official Website](https://www.mediatek.com)
2. [MediaTek Genio 1200](https://genio.mediatek.com/genio-1200)
3. [MediaTek Genio Platform](https://www.mediatek.com/products/iot/genio)
