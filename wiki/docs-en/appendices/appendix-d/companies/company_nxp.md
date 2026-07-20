# NXP Semiconductors

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 恩智浦 |
| **English Name** | NXP Semiconductors |
| **Headquarters** | Eindhoven, Netherlands |
| **Founded** | 2006 (Spin-off from Philips semiconductor division) |
| **Official Website** | [https://www.nxp.com](https://www.nxp.com) |
| **Supply Chain Role** | MCU/MPU, Edge AI, Industrial Control, Automotive Electronics, Robot Main Controller |
| **Company Type** | Public Company (NASDAQ: NXPI) |
| **Parent Company/Group** | None (NXP Semiconductors is the listed entity) |
| **Data Source** | NXP official website, i.MX product manuals, public press releases, industry research reports |

## Company Profile

NXP Semiconductors is a leading global supplier of embedded semiconductors, covering MCUs, MPUs, security identification, automotive electronics, and analog devices. Its i.MX series of application processors target industrial, automotive, and IoT edge computing. Models such as the i.MX 8M Plus integrate an NPU, providing local AI inference capabilities for robotics, industrial vision, and AIoT, while also offering high reliability and long product lifecycles.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|---|---|---|---|
| i.MX 8 Series | High-performance multimedia and AI application processors | i.MX 8M Plus | Industrial HMI, robot main controller, edge AI, smart gateway |
| i.MX 9 / i.MX 93 Series | Next-generation edge AI processors with integrated NPU | i.MX 93 | AIoT, industrial automation, smart home, robotics |

## Representative Products

### NXP i.MX 8M Plus

> NXP i.MX 8M Plus: Please visit the [official page](https://www.nxp.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Process Node | 14 nm FinFET | NXP public information |
| CPU | Quad-core Arm Cortex-A53 @ up to 1.8 GHz + Cortex-M7 @ 800 MHz | NXP public information |
| NPU | Integrated Neural Processing Unit | NXP public information |
| AI Performance | Up to 2.3 TOPS INT8 | NXP public information |
| ISP | Dual ISP, supports 12MP, HDR, fisheye correction | NXP public information |
| GPU | Vivante GC7000UL 3D GPU + GC520L 2D GPU | NXP public information |
| Memory | Supports LPDDR4/DDR4, up to 6 GB (modules typically 2–4 GB) | NXP public information |
| Interfaces | USB 3.0, PCIe 3.0, 2× GbE (with TSN), 2× CAN-FD, MIPI CSI/DSI, HDMI, LVDS | NXP public information |
| Power Consumption | Not disclosed (typical whole board 2–5 W) | NXP public information |
| Package | FCBGA 15 mm × 15 mm | NXP public information |
| Price | Not disclosed | NXP public information |

**Technical Highlights**: Industrial-grade heterogeneous SoC with integrated NPU, dual ISP, TSN Ethernet, CAN-FD, ECC memory, 15-year supply lifecycle, suitable for functional safety and real-time control scenarios.

**Application Scenarios**: **Industrial Vision Inspection**: NPU accelerates defect classification and OCR, dual ISP supports HDR and high dynamic range scenes; **AGV/AMR Main Controller**: TSN/CAN-FD supports real-time communication, low-power SLAM and navigation; **Smart Gateway and HMI**: Multi-screen display, rich interfaces, and industrial-grade reliability.

### NXP i.MX 93

> NXP i.MX 93: Please visit the [official page](https://www.nxp.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| CPU | Dual-core Cortex-A55 + Cortex-M33 | NXP public information |
| NPU | Integrated Arm Ethos U65 | NXP public information |
| AI Performance | Approx. 0.5 TOPS | NXP public information |
| Process Node | Not disclosed | NXP public information |
| Interfaces | GbE, CAN-FD, USB, MIPI CSI/DSI | NXP public information |
| Power Consumption | Ultra-low power design | NXP public information |
| Price | Not disclosed | NXP public information |

**Technical Highlights**: Low power, low cost, integrated Arm Ethos U65 NPU, suitable for lightweight AIoT and voice/vision wake-up.

**Application Scenarios**: Smart home, industrial sensors, voice assistants, lightweight robot control.

## Supply Chain Position

- **Upstream Key Components/Materials**: TSMC/GlobalFoundries foundry, ARM IP, proprietary NPU, LPDDR4/DDR4, eMMC, packaging and testing, PMIC
- **Downstream Customers/Application Scenarios**: Industrial automation vendors, automotive OEMs/Tier1s, robot integrators, AIoT device manufacturers, gateway vendors
- **Main Competitors/Alternatives**: Texas Instruments Jacinto, Renesas RZ/V, NVIDIA Jetson, Qualcomm QCS, Rockchip RK3588

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_nxp`
- Product Entities: `ent_product_nxp_imx8m_plus`, `ent_product_nxp_imx93`
- Component Entities: `ent_component_nxp_imx8m_plus_soc`, `ent_component_nxp_imx93_soc`
- Key Relationships:
  - `ent_company_nxp` -- `manufactures` --> `ent_product_nxp_imx8m_plus`
  - `ent_company_nxp` -- `manufactures` --> `ent_product_nxp_imx93`
  - `ent_company_nxp` -- `manufactures` --> `ent_component_nxp_imx8m_plus_soc`
  - `ent_company_nxp` -- `manufactures` --> `ent_component_nxp_imx93_soc`
  - `ent_product_nxp_imx8m_plus` -- `uses` --> `ent_component_nxp_imx8m_plus_soc`
  - `ent_product_nxp_imx93` -- `uses` --> `ent_component_nxp_imx93_soc`

## References

1. [NXP Official Website](https://www.nxp.com)
2. [i.MX 8M Plus Product Page](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-8-applications-processors/i-mx-8m-plus-arm-cortex-a53-machine-learning-vision-multimedia-and-industrial-iot:IMX8MPLUS)
3. [NXP i.MX Ecosystem](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors:IMX_HOME)
