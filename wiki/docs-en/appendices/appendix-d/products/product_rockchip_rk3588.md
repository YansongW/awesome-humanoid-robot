# Rockchip RK3588 AIoT SoC

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Rockchip / Rockchip](../companies/company_rockchip.md) |
| **Product Category** | Flagship AIoT SoC / Robotics and Edge AI Main Controller |
| **Release Date** | Released in 2022, mass production in 2023 |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [Rockchip RK3588 Product Page](https://www.rock-chips.com/a/en/products/RK35_Series/2022/0926/1660.html) |

## Product Overview

The Rockchip RK3588 is Rockchip's flagship AIoT SoC, built on an 8 nm process, integrating a quad-core Cortex-A76 and quad-core Cortex-A55, Mali-G610 MC4 GPU, and a 6 TOPS triple-core NPU. Its multimedia engine supports 8K@60fps decoding and 8K@30fps encoding, the ISP supports 32 MP multi-channel cameras, and interfaces include PCIe 3.0, USB 3.1, SATA, Gigabit Ethernet, and multiple display outputs. It is a cost-effective choice for robotics, NVRs, edge AI boxes, and smart commercial displays.

## Product Image

> Rockchip RK3588 AIoT SoC: Please visit the [official page](https://www.rock-chips.com/a/en/products/RK35_Series/2022/0926/1660.html) for details.

## Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Process | 8 nm LP | Rockchip public information |
| CPU | Octa-core (4× Cortex-A76 @ up to 2.4 GHz + 4× Cortex-A55) | Rockchip public information |
| GPU | Arm Mali-G610 MC4 (approx. 450 GFLOPS) | Rockchip public information |
| NPU | Proprietary triple-core NPU | Rockchip public information |
| AI Compute | Up to 6.0 TOPS INT8 | Rockchip public information |
| Precision Support | INT4/INT8/INT16/FP16/BF16/TF32 | Rockchip public information |
| Video | 8K@60fps decoding, 8K@30fps encoding, H.265/VP9/AVS2 | Rockchip public information |
| ISP | Dual ISP, 32 MP, supports HDR & 3DNR | Rockchip public information |
| Memory | Supports LPDDR4/LPDDR4x/LPDDR5, up to 32 GB | Rockchip public information |
| Interfaces | PCIe 3.0, USB 3.1, SATA 3.0, GbE, MIPI CSI/DSI, HDMI 2.1/DP/eDP | Rockchip public information |
| Power Consumption | Typical approx. 5–15 W (full board) | Rockchip public information |
| Price | Development board approx. 100–200 USD (reference price) | Rockchip public information |

## Supply Chain Position

- **Manufacturer**: [Rockchip / Rockchip](../companies/company_rockchip.md)
- **Core Components/Technology Sources**: Rockchip proprietary NPU and system IP, ARM CPU/GPU IP, 8 nm foundry, LPDDR4x/5, eMMC, PMIC, carrier board
- **Downstream Applications/Customers**: Robotics and drone manufacturers, industrial NVR/security customers, commercial display and self-service equipment vendors, development board community

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_rockchip_rk3588`
- Component Entity: `ent_component_rockchip_rk3588_soc`
- Manufacturer Entity: `ent_company_rockchip`
- Key Relationships:
  - `rel_ent_company_rockchip_manufactures_ent_product_rockchip_rk3588` (`ent_company_rockchip` → `manufactures` --> `ent_product_rockchip_rk3588`)
  - `rel_ent_company_rockchip_manufactures_ent_component_rockchip_rk3588_soc` (`ent_company_rockchip` → `manufactures` --> `ent_component_rockchip_rk3588_soc`)
  - `ent_product_rockchip_rk3588` -- `uses` --> `ent_component_rockchip_rk3588_soc`

## Application Scenarios

- **Robot Main Controller**: Multi-channel camera perception, SLAM, path planning, and robotic arm control
- **Edge AI Boxes and NVRs**: 8K decoding, multi-channel video analysis, and local AI inference
- **Smart Commercial Displays and Self-Service Terminals**: Multi-screen independent display, touch interaction, and advertising playback

## Competitive Comparison

| Comparison Item | RK3588 | Allwinner T527 | MediaTek Genio 1200 |
|---|---|---|---|
| Process | 8 nm | Not disclosed | 6 nm |
| AI Compute | 6 TOPS | 2 TOPS | 4.8 TOPS |
| Video | 8K@60 decoding | 4K@60 decoding | 4K90 decoding |

## Selection and Deployment Recommendations

Use RKNN-Toolkit2 to convert models to INT8 and evaluate NPU utilization; select a core board or SBC based on heat dissipation and interface requirements; confirm Linux/Android BSP and camera driver versions.

## Related Entries

- [Manufacturer: Rockchip / Rockchip](../companies/company_rockchip.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [Rockchip RK3588 Product Page](https://www.rock-chips.com/a/en/products/RK35_Series/2022/0926/1660.html)
2. [RKNN-Toolkit2 GitHub](https://github.com/rockchip-linux/rknpu2)
3. [Rockchip Official Website](https://www.rock-chips.com)
