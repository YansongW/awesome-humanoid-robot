# Allwinner Technology

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 全志科技 |
| **English Name** | Allwinner Technology |
| **Headquarters** | Zhuhai, Guangdong, China |
| **Founded** | 2007 |
| **Website** | [https://www.allwinnertech.com](https://www.allwinnertech.com) |
| **Supply Chain Role** | AIoT SoC, Robot Chips, Industrial Control, Smart Terminals, Edge AI |
| **Company Type** | Publicly Listed (Shenzhen Stock Exchange: 300458) |
| **Parent Company/Group** | None (Allwinner Technology is the listed entity) |
| **Data Source** | Allwinner Technology official website, Orange Pi / MYIR product materials, public press releases, industry research reports |

## Company Profile

Allwinner Technology is a well-known Chinese designer of smart terminal and AIoT application processors, with products covering tablets, set-top boxes, smart cars, industrial control, and robotics. Its T527 series targets AIoT and robotics applications, integrating an octa-core Cortex-A55, a 2 TOPS NPU, a Mali-G57 GPU, and rich industrial interfaces, meeting the needs of robotics, commercial displays, industrial gateways, and edge AI with high cost-effectiveness and long supply cycles.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| T Series Industrial SoC | AIoT / Robotics Application Processor | T527 / T527A / T527N | Robot main controller, industrial gateway, smart commercial display, edge AI |
| A / R / F / H Series | Tablets, Home Appliances, Multimedia & Real-time MCU | A523 / R329 / F133 | Tablets, smart speakers, automotive, AIoT terminals |

## Representative Products

### Allwinner T527

> Allwinner T527: Please visit [Official Documentation](https://www.allwinnertech.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Process Node | Not disclosed | Allwinner/Partner public materials |
| CPU | Octa-core Arm Cortex-A55 (4× @ up to 1.8 GHz + 4× @ 1.42 GHz) | Allwinner/Partner public materials |
| Co-processor | XuanTie E906 RISC-V @ 200 MHz + HiFi4 DSP @ 600 MHz | Allwinner/Partner public materials |
| GPU | Arm Mali-G57 MC1 | Allwinner/Partner public materials |
| NPU | Integrated AI Accelerator | Allwinner/Partner public materials |
| AI Performance | Up to 2 TOPS INT8/INT16/FP16 | Allwinner/Partner public materials |
| Video | 4K@60fps H.265/H.264 Decode, 4K@25fps H.264 Encode | Allwinner/Partner public materials |
| ISP | Supports multi-channel MIPI CSI, up to 8 MP@30fps | Allwinner/Partner public materials |
| Memory | Supports LPDDR4/LPDDR4X, typically 2–4 GB | Allwinner/Partner public materials |
| Interfaces | USB 3.0/2.0, PCIe 2.1, GbE, MIPI CSI/DSI, HDMI 2.0, LVDS/eDP, CAN, RS485, ADC | Allwinner/Partner public materials |
| Power Consumption | Typical approx. 3–7 W (full board) | Allwinner/Partner public materials |
| Price | Development board approx. 50–100 USD (reference price) | Allwinner/Partner public materials |

**Technical Highlights**: High cost-effectiveness with octa-core A55, 2 TOPS NPU, RISC-V co-processor, rich industrial interfaces, supports Android/Linux/Ubuntu, long supply cycle.

**Application Scenarios**: **Robotics & AMR**: Low-cost main controller, visual perception and motion control, supports ROS and Linux; **Smart Commercial Displays & Self-service Terminals**: 4K playback, touch interaction, and remote device management; **Industrial Gateways & Edge AI**: Protocol conversion, data collection, and local 2 TOPS AI inference.

### Allwinner A523

> Allwinner A523: Please visit [Official Documentation](https://www.allwinnertech.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| CPU | Octa-core Cortex-A55 | Allwinner/Partner public materials |
| GPU | Mali-G57 | Allwinner/Partner public materials |
| AI Performance | No dedicated NPU | Allwinner/Partner public materials |
| Video | 4K Decode | Allwinner/Partner public materials |
| Interfaces | USB, MIPI DSI/CSI, HDMI, GbE | Allwinner/Partner public materials |
| Power Consumption | Low-power design | Allwinner/Partner public materials |
| Price | Not disclosed | Allwinner/Partner public materials |

**Technical Highlights**: An octa-core A55 platform for tablets and smart terminals, balancing cost and multimedia capabilities.

**Application Scenarios**: Tablet PCs, educational tablets, AIoT terminals, lightweight control boards.

## Supply Chain Position

- **Upstream Key Components/Materials**: TSMC/SMIC foundry, ARM CPU/GPU IP, proprietary NPU, LPDDR4, eMMC, packaging and testing, substrate
- **Downstream Customers/Application Scenarios**: Robotics and education equipment manufacturers, industrial gateway/commercial display customers, tablet and smart hardware OEMs, developer community
- **Main Competitors/Peers**: Rockchip RK3568/RK3588, MediaTek Genio, Amlogic, HiSilicon, Amlogic Semiconductor

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_allwinner`
- Product Entities: `ent_product_allwinner_t527`, `ent_product_allwinner_a523`
- Component Entities: `ent_component_allwinner_t527_soc`, `ent_component_allwinner_a523_soc`
- Key Relationships:
  - `ent_company_allwinner` -- `manufactures` --> `ent_product_allwinner_t527`
  - `ent_company_allwinner` -- `manufactures` --> `ent_product_allwinner_a523`
  - `ent_company_allwinner` -- `manufactures` --> `ent_component_allwinner_t527_soc`
  - `ent_company_allwinner` -- `manufactures` --> `ent_component_allwinner_a523_soc`
  - `ent_product_allwinner_t527` -- `uses` --> `ent_component_allwinner_t527_soc`
  - `ent_product_allwinner_a523` -- `uses` --> `ent_component_allwinner_a523_soc`

## References

1. [Allwinner Technology Official Website](https://www.allwinnertech.com)
2. [Orange Pi 4A Product Page](https://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-4A.html)
3. [Allwinner T527 Developer Documentation](https://linux-sunxi.org/T527)
