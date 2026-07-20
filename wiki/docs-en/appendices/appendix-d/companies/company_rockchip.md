# Rockchip

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 瑞芯微 |
| **English Name** | Rockchip |
| **Headquarters** | Fuzhou, Fujian, China |
| **Founded** | 2001 |
| **Website** | [https://www.rock-chips.com](https://www.rock-chips.com) |
| **Supply Chain Role** | AIoT SoC, Robot Main Controller, Industrial Tablet, Edge AI, Multimedia |
| **Company Type** | Listed Company (Shenzhen Stock Exchange: 603893) |
| **Parent Company/Group** | None (Rockchip is the listed entity) |
| **Data Source** | Rockchip official website, RK3588 product documentation, public press releases, industry research reports |

## Company Overview

Rockchip is a leading AIoT and multimedia SoC design company in China. Its products cover tablets, smart TV boxes, industrial control, robotics, and edge AI. The RK3588 is its flagship AIoT chip, integrating a 6 TOPS NPU, 8K video codec, and rich interfaces. It is widely used in robot main controllers, industrial gateways, NVRs, smart commercial displays, and edge AI boxes. Rockchip provides the RKNN toolchain and Linux/Android SDK, supporting rapid model deployment.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| RK3588 Series | Flagship AIoT / Robot SoC | RK3588 / RK3588S | Robot Main Controller, Edge AI, NVR, Industrial HMI, 8K Commercial Display |
| RK3576 / RK3568 Series | Mid-to-High-End AIoT SoC | RK3568 / RK3576 | Industrial Gateway, Smart Camera, Educational Robot, AIoT Terminal |

## Representative Products

### Rockchip RK3588

> Rockchip RK3588: Please visit the [official documentation](https://www.rock-chips.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Process Node | 8 nm LP | Rockchip public data |
| CPU | Octa-core (4× Cortex-A76 @ up to 2.4 GHz + 4× Cortex-A55) | Rockchip public data |
| GPU | Arm Mali-G610 MC4 (~450 GFLOPS) | Rockchip public data |
| NPU | Proprietary Triple-core NPU | Rockchip public data |
| AI Compute | Up to 6.0 TOPS INT8 | Rockchip public data |
| Precision Support | INT4/INT8/INT16/FP16/BF16/TF32 | Rockchip public data |
| Video | 8K@60fps Decode, 8K@30fps Encode, H.265/VP9/AVS2 | Rockchip public data |
| ISP | Dual ISP, 32 MP, supports HDR & 3DNR | Rockchip public data |
| Memory | Supports LPDDR4/LPDDR4x/LPDDR5, up to 32 GB | Rockchip public data |
| Interfaces | PCIe 3.0, USB 3.1, SATA 3.0, GbE, MIPI CSI/DSI, HDMI 2.1/DP/eDP | Rockchip public data |
| Power Consumption | Typical ~5–15 W (full board) | Rockchip public data |
| Price | Development board ~100–200 USD (reference price) | Rockchip public data |

**Technical Highlights**: 8 nm flagship AIoT chip, 6 TOPS NPU, 8K multimedia, multi-camera support, rich expansion interfaces, RKNN toolchain, mature Linux/Android ecosystem.

**Application Scenarios**: **Robot Main Controller**: Multi-camera perception, SLAM, path planning, and robotic arm control; **Edge AI Box & NVR**: 8K decoding, multi-channel video analysis, and local AI inference; **Smart Commercial Display & Self-service Terminal**: Multi-screen display, touch interaction, and advertising playback.

### Rockchip RK3576

> Rockchip RK3576: Please visit the [official documentation](https://www.rock-chips.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Process Node | Not disclosed | Rockchip public data |
| CPU | Octa-core Cortex-A72/A53 or newer architecture | Rockchip public data |
| NPU | ~6 TOPS | Rockchip public data |
| Video | 4K/8K Decode | Rockchip public data |
| Interfaces | PCIe, USB, GbE, MIPI CSI/DSI, HDMI | Rockchip public data |
| Power Consumption | ~3–8 W | Rockchip public data |
| Price | Not disclosed | Rockchip public data |

**Technical Highlights**: Mid-to-high-end AIoT SoC, inheriting the NPU and multimedia capabilities of the RK3588, targeting cost-sensitive robots and edge devices.

**Application Scenarios**: Industrial Gateway, Educational Robot, Smart Camera, AIoT Terminal.

## Supply Chain Position

- **Upstream Key Components/Materials**: TSMC/SMIC foundry, ARM CPU/GPU IP, proprietary NPU, LPDDR4x, eMMC, packaging & testing, substrate
- **Downstream Customers/Application Scenarios**: Robot OEMs, industrial tablet/gateway manufacturers, NVR/security customers, commercial display & education equipment vendors, developers
- **Main Competitors/Comparables**: Allwinner, MediaTek Genio, Qualcomm QCS, NVIDIA Jetson, Amlogic, HiSilicon

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_rockchip`
- Product Entities: `ent_product_rockchip_rk3588`, `ent_product_rockchip_rk3576`
- Component Entities: `ent_component_rockchip_rk3588_soc`, `ent_component_rockchip_rk3576_soc`
- Key Relationships:
  - `ent_company_rockchip` -- `manufactures` --> `ent_product_rockchip_rk3588`
  - `ent_company_rockchip` -- `manufactures` --> `ent_product_rockchip_rk3576`
  - `ent_company_rockchip` -- `manufactures` --> `ent_component_rockchip_rk3588_soc`
  - `ent_company_rockchip` -- `manufactures` --> `ent_component_rockchip_rk3576_soc`
  - `ent_product_rockchip_rk3588` -- `uses` --> `ent_component_rockchip_rk3588_soc`
  - `ent_product_rockchip_rk3576` -- `uses` --> `ent_component_rockchip_rk3576_soc`

## References

1. [Rockchip Official Website](https://www.rock-chips.com)
2. [RK3588 Product Page](https://www.rock-chips.com/a/en/products/RK35_Series/2022/0926/1660.html)
3. [Rockchip RKNN SDK](https://github.com/rockchip-linux/rknpu2)
