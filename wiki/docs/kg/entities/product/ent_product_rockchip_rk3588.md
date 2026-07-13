---
id: ent_product_rockchip_rk3588
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Rockchip RK3588
  en: Rockchip RK3588
status: active
sources:
- id: src_ent_product_rockchip_rk3588_official
  type: website
  url: https://www.rock-chips.com/a/en/products/RK35_Series/2022/0926/1660.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
---





# Rockchip RK3588 / Rockchip RK3588

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [瑞芯微 / Rockchip](../../../appendices/appendix-d/companies/company_rockchip.md) |
| **产品类别** | 旗舰 AIoT SoC / 机器人与边缘 AI 主控 |
| **发布时间** | 2022 年发布，2023 年量产 |
| **状态** | 量产/商用 |
| **官网/来源** | [Rockchip RK3588 Product Page](https://www.rock-chips.com/a/en/products/RK35_Series/2022/0926/1660.html) |

## 产品概述

Rockchip RK3588 是瑞芯微旗舰级 AIoT SoC，采用 8 nm 工艺，集成四核 Cortex-A76 与四核 Cortex-A55、Mali-G610 MC4 GPU 和 6 TOPS 三核 NPU。其多媒体引擎支持 8K@60fps 解码与 8K@30fps 编码，ISP 支持 32 MP 多路相机，接口涵盖 PCIe 3.0、USB 3.1、SATA、千兆以太网和多种显示输出，是机器人、NVR、边缘 AI 盒子和智能商显的高性价比选择。

## 产品图片

> Rockchip RK3588 AIoT SoC：请访问 [官方资料](https://www.rock-chips.com/a/en/products/RK35_Series/2022/0926/1660.html) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制程 | 8 nm LP | 瑞芯微公开资料 |
| CPU | 八核（4× Cortex-A76 @ 最高 2.4 GHz + 4× Cortex-A55） | 瑞芯微公开资料 |
| GPU | Arm Mali-G610 MC4（约 450 GFLOPS） | 瑞芯微公开资料 |
| NPU | 自研三核 NPU | 瑞芯微公开资料 |
| AI 算力 | 最高 6.0 TOPS INT8 | 瑞芯微公开资料 |
| 精度支持 | INT4/INT8/INT16/FP16/BF16/TF32 | 瑞芯微公开资料 |
| 视频 | 8K@60fps 解码、8K@30fps 编码、H.265/VP9/AVS2 | 瑞芯微公开资料 |
| ISP | 双 ISP，32 MP，支持 HDR & 3DNR | 瑞芯微公开资料 |
| 内存 | 支持 LPDDR4/LPDDR4x/LPDDR5，最高 32 GB | 瑞芯微公开资料 |
| 接口 | PCIe 3.0、USB 3.1、SATA 3.0、GbE、MIPI CSI/DSI、HDMI 2.1/DP/eDP | 瑞芯微公开资料 |
| 功耗 | 典型约 5–15 W（整板） | 瑞芯微公开资料 |
| 价格 | 开发板约 100–200 USD（参考价） | 瑞芯微公开资料 |

## 供应链位置

- **制造商**：[瑞芯微 / Rockchip](../../../appendices/appendix-d/companies/company_rockchip.md)
- **核心零部件/技术来源**：瑞芯微自研 NPU 与系统 IP、ARM CPU/GPU IP、8 nm 代工、LPDDR4x/5、eMMC、PMIC、载板
- **下游应用/客户**：机器人与无人机厂商、工业 NVR/安防客户、商显与自助设备商、开发板社区

## 知识图谱节点与关系

- 产品实体：`ent_product_rockchip_rk3588`
- 零部件实体：`ent_component_rockchip_rk3588_soc`
- 制造商实体：`ent_company_rockchip`
- 关键关系：
  - `rel_ent_company_rockchip_manufactures_ent_product_rockchip_rk3588`（`ent_company_rockchip` → `manufactures` --> `ent_product_rockchip_rk3588`）
  - `rel_ent_company_rockchip_manufactures_ent_component_rockchip_rk3588_soc`（`ent_company_rockchip` → `manufactures` --> `ent_component_rockchip_rk3588_soc`）
  - `ent_product_rockchip_rk3588` -- `uses` --> `ent_component_rockchip_rk3588_soc`

## 应用场景

- **机器人主控**：多路相机感知、SLAM、路径规划与机械臂控制
- **边缘 AI 盒子与 NVR**：8K 解码、多路视频分析与本地 AI 推理
- **智能商显与自助终端**：多屏异显、触控交互与广告播放

## 竞争对比

| 对比项 | RK3588 | Allwinner T527 | MediaTek Genio 1200 |
|---|---|---|---|
| 制程 | 8 nm | 未公开 | 6 nm |
| AI 算力 | 6 TOPS | 2 TOPS | 4.8 TOPS |
| 视频 | 8K@60 解码 | 4K@60 解码 | 4K90 解码 |

## 选购与部署建议

使用 RKNN-Toolkit2 将模型转换为 INT8 并评估 NPU 利用率；根据散热与接口需求选择核心板或 SBC；确认 Linux/Android BSP 与相机驱动版本。

## 相关词条

- [制造商：瑞芯微 / Rockchip](../../../appendices/appendix-d/companies/company_rockchip.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [瑞芯微 RK3588 产品页](https://www.rock-chips.com/a/en/products/RK35_Series/2022/0926/1660.html)
2. [RKNN-Toolkit2 GitHub](https://github.com/rockchip-linux/rknpu2)
3. [瑞芯微官网](https://www.rock-chips.com)