# MediaTek Genio 1200 Edge AI Platform

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [MediaTek](../companies/company_mediatek.md) |
| **Product Category** | AIoT Edge AI SoC / Robotics and Industrial Vision Platform |
| **Release Date** | Released in 2022 |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [MediaTek Genio 1200 Product Page](https://genio.mediatek.com/genio-1200) |

## Product Overview

The MediaTek Genio 1200 is a 6 nm platform for high-end AIoT and edge AI, integrating an octa-core CPU, Mali-G57 MC5 GPU, 4.8 TOPS APU, and dual ISP. Its multimedia capabilities support triple 4K display and 4K90 video encoding/decoding. High-speed interfaces include PCIe 3.0, USB 3.2, Gigabit TSN Ethernet, and multiple MIPI CSI/DSI. It supports systems such as ROS, Yocto, and Ubuntu, making it a mainstream choice for robotics, smart cameras, and industrial gateways.

## Product Image

> MediaTek Genio 1200 Edge AI Platform: Please visit the [official documentation](https://genio.mediatek.com/genio-1200) for details.

## Specification Table

| Specification Item | Value | Notes/Source |
|-------------------|-------|--------------|
| Process Node | 6 nm | MediaTek public information |
| CPU | Octa-core (4× Cortex-A78 @ up to 2.2 GHz + 4× Cortex-A55) | MediaTek public information |
| GPU | Arm Mali-G57 MC5 | MediaTek public information |
| AI Accelerator | MediaTek multi-core APU | MediaTek public information |
| AI Compute | Up to 4.8 TOPS INT8 | MediaTek public information |
| Vision | Dual ISP, up to 48 MP single camera / 16 MP+16 MP dual camera, 4K90 decode | MediaTek public information |
| DSP | Dual Cadence Tensilica VP6 + HiFi 4 Audio DSP | MediaTek public information |
| Memory | Supports LPDDR4X, up to 16 GB | MediaTek public information |
| Interfaces | PCIe 3.0, USB 3.2 Gen1, GbE (TSN), MIPI CSI/DSI, HDMI, UART/I2C/SPI | MediaTek public information |
| Power Consumption | Typical approx. 6–10 W (full board/module) | MediaTek public information |
| Price | Development kit approx. 200–400 USD (reference price) | MediaTek public information |

## Supply Chain Position

- **Manufacturer**: [MediaTek](../companies/company_mediatek.md)
- **Core Components/Technology Sources**: TSMC 6 nm foundry, ARM CPU/GPU IP, MediaTek self-developed APU, LPDDR4X, UFS, PMIC, carrier board
- **Downstream Applications/Customers**: AIoT and robotics OEM/ODM, smart camera manufacturers, digital signage and industrial HMI customers, edge gateway integrators

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_mediatek_genio_1200`
- Component Entity: `ent_component_mediatek_genio_1200_soc`
- Manufacturer Entity: `ent_company_mediatek`
- Key Relationships:
  - `rel_ent_company_mediatek_manufactures_ent_product_mediatek_genio_1200` (`ent_company_mediatek` → `manufactures` --> `ent_product_mediatek_genio_1200`)
  - `rel_ent_company_mediatek_manufactures_ent_component_mediatek_genio_1200_soc` (`ent_company_mediatek` → `manufactures` --> `ent_component_mediatek_genio_1200_soc`)
  - `ent_product_mediatek_genio_1200` -- `uses` --> `ent_component_mediatek_genio_1200_soc`

## Application Scenarios

- **Industrial Robotics and AMR**: Multi-channel visual perception, SLAM, path planning, and robotic arm control
- **Smart Cameras and Security**: 4K real-time object detection, facial recognition, and behavior analysis
- **Edge AI Gateways and HMI**: Multi-screen display, device interconnection, and local AI inference

## Competitive Comparison

| Comparison Item | Genio 1200 | Rockchip RK3588 | Qualcomm QCS8550 |
|---|---|---|---|
| Process Node | 6 nm | 8 nm | 4 nm |
| AI Compute | 4.8 TOPS | 6 TOPS | Approx. 15 TOPS |
| CPU | 4×A78 + 4×A55 | 4×A76 + 4×A55 | 8×Kryo |

## Selection and Deployment Recommendations

Use the MediaTek NeuroPilot SDK to evaluate APU performance; select a core board or SMARC/OSM module based on I/O requirements; confirm Yocto/Ubuntu driver and ROS package support.

## Related Entries

- [Manufacturer: MediaTek](../companies/company_mediatek.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [MediaTek Genio 1200](https://genio.mediatek.com/genio-1200)
2. [MediaTek Genio Platform](https://www.mediatek.com/products/iot/genio)
3. [MediaTek NeuroPilot SDK](https://www.mediatek.com/products/iot/neuropilot)
