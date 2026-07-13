---
id: ent_product_mediatek_genio_1200
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: MediaTek Genio 1200
  en: MediaTek Genio 1200
status: active
sources:
- id: src_ent_product_mediatek_genio_1200_official
  type: website
  url: https://genio.mediatek.com/genio-1200
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
---





# MediaTek Genio 1200 / MediaTek Genio 1200

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [联发科 / MediaTek](../../../appendices/appendix-d/companies/company_mediatek.md) |
| **产品类别** | AIoT 边缘 AI SoC / 机器人与工业视觉平台 |
| **发布时间** | 2022 年发布 |
| **状态** | 量产/商用 |
| **官网/来源** | [MediaTek Genio 1200 Product Page](https://genio.mediatek.com/genio-1200) |

## 产品概述

MediaTek Genio 1200 是面向高端 AIoT 与边缘 AI 的 6 nm 平台，集成八核 CPU、Mali-G57 MC5 GPU、4.8 TOPS APU 与双 ISP。其多媒体能力支持三屏 4K 显示与 4K90 视频编解码，高速接口包括 PCIe 3.0、USB 3.2、千兆 TSN 以太网与多路 MIPI CSI/DSI，并支持 ROS、Yocto、Ubuntu 等系统，是机器人、智能相机与工业网关的主流选择。

## 产品图片

> MediaTek Genio 1200 边缘 AI 平台：请访问 [官方资料](https://genio.mediatek.com/genio-1200) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制程 | 6 nm | MediaTek 公开资料 |
| CPU | 八核（4× Cortex-A78 @ 最高 2.2 GHz + 4× Cortex-A55） | MediaTek 公开资料 |
| GPU | Arm Mali-G57 MC5 | MediaTek 公开资料 |
| AI 加速器 | MediaTek 多核 APU | MediaTek 公开资料 |
| AI 算力 | 最高 4.8 TOPS INT8 | MediaTek 公开资料 |
| 视觉 | 双 ISP，最高 48 MP 单摄 / 16 MP+16 MP 双摄，4K90 解码 | MediaTek 公开资料 |
| DSP | 双 Cadence Tensilica VP6 + HiFi 4 Audio DSP | MediaTek 公开资料 |
| 内存 | 支持 LPDDR4X，最高 16 GB | MediaTek 公开资料 |
| 接口 | PCIe 3.0、USB 3.2 Gen1、GbE（TSN）、MIPI CSI/DSI、HDMI、UART/I2C/SPI | MediaTek 公开资料 |
| 功耗 | 典型约 6–10 W（整板/模组） | MediaTek 公开资料 |
| 价格 | 开发套件约 200–400 USD（参考价） | MediaTek 公开资料 |

## 供应链位置

- **制造商**：[联发科 / MediaTek](../../../appendices/appendix-d/companies/company_mediatek.md)
- **核心零部件/技术来源**：台积电 6 nm 代工、ARM CPU/GPU IP、MediaTek 自研 APU、LPDDR4X、UFS、PMIC、载板
- **下游应用/客户**：AIoT 与机器人 OEM/ODM、智能相机厂商、数字标牌与工业 HMI 客户、边缘网关集成商

## 知识图谱节点与关系

- 产品实体：`ent_product_mediatek_genio_1200`
- 零部件实体：`ent_component_mediatek_genio_1200_soc`
- 制造商实体：`ent_company_mediatek`
- 关键关系：
  - `rel_ent_company_mediatek_manufactures_ent_product_mediatek_genio_1200`（`ent_company_mediatek` → `manufactures` --> `ent_product_mediatek_genio_1200`）
  - `rel_ent_company_mediatek_manufactures_ent_component_mediatek_genio_1200_soc`（`ent_company_mediatek` → `manufactures` --> `ent_component_mediatek_genio_1200_soc`）
  - `ent_product_mediatek_genio_1200` -- `uses` --> `ent_component_mediatek_genio_1200_soc`

## 应用场景

- **工业机器人与 AMR**：多路视觉感知、SLAM、路径规划与机械臂控制
- **智能相机与安防**：4K 实时目标检测、人脸识别与行为分析
- **边缘 AI 网关与 HMI**：多屏显示、设备互联与本地 AI 推理

## 竞争对比

| 对比项 | Genio 1200 | Rockchip RK3588 | Qualcomm QCS8550 |
|---|---|---|---|
| 制程 | 6 nm | 8 nm | 4 nm |
| AI 算力 | 4.8 TOPS | 6 TOPS | 约 15 TOPS |
| CPU | 4×A78 + 4×A55 | 4×A76 + 4×A55 | 8×Kryo |

## 选购与部署建议

使用 MediaTek NeuroPilot SDK 评估 APU 性能；根据 I/O 需求选择核心板或 SMARC/OSM 模组；确认 Yocto/Ubuntu 驱动与 ROS 包支持。

## 相关词条

- [制造商：联发科 / MediaTek](../../../appendices/appendix-d/companies/company_mediatek.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [MediaTek Genio 1200](https://genio.mediatek.com/genio-1200)
2. [MediaTek Genio 平台](https://www.mediatek.com/products/iot/genio)
3. [MediaTek NeuroPilot SDK](https://www.mediatek.com/products/iot/neuropilot)