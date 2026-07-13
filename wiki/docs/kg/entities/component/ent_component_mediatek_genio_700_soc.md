---
id: ent_component_mediatek_genio_700_soc
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
status: active
names:
  zh: MediaTek Genio 700 边缘 AI SoC
  en: MediaTek Genio 700 Edge AI SoC
sources:
- id: src_mediatek_genio700_factsheet
  type: datasheet
- title: MediaTek Genio 700 Factsheet
  url: https://www.mediatek.com/hubfs/Factsheet-Genio-700.pdf
- id: src_mediatek_genio700_web
  type: website
- title: MediaTek Genio 700 Product Page
  url: https://genio.mediatek.com/genio-700
- id: src_rutronik_genio700
  type: article
- title: MediaTek Genio 700 new at Rutronik
  url: https://www.automation-mag.com/news/71281-high-performance,-ai-powered-soc-for-embedded-and-iot-applications-mediatek-genio-700-new-at-rutronik
verification:
  reviewed_by: ai_autonomous
  reviewed_at: '2026-07-13'
---


# MediaTek Genio 700 边缘 AI SoC / MediaTek Genio 700 Edge AI SoC

## 概述

MediaTek Genio 700（MT8390）是联发科面向高端 AIoT、工业边缘计算与机器人主控的异构 SoC，采用台积电 6 nm 制程，集成 2× Arm Cortex-A78 性能核、6× Cortex-A55 能效核、Arm Mali-G57 MC3 GPU、MediaTek 第五代 NPU 及 Cadence Tensilica VP6/Hifi5 DSP。Genio 700 支持 4K 双显、32 MP ISP、TSN 千兆以太网、PCIe/USB3 高速接口与 Wi-Fi 6/BT 5，适用于机器人导航、边缘 AI 网关、智能零售与工业 HMI。

## 工作原理 / 技术架构

Genio 700 通过大小核异构调度与专用 AI 加速器实现高能效比：

- **CPU**：2× Cortex-A78 @ 2.2 GHz 负责高负载任务；6× Cortex-A55 @ 2.0 GHz 负责后台与实时性要求较低的任务。
- **NPU**：MediaTek 第五代 AI 处理器（1× MDLA 3.0 + 1× Tensilica VP6），INT8 峰值算力 4.0 TOPS，支持 INT8/INT16/FP16 混合精度。
- **GPU**：Mali-G57 MC3 @ 950 MHz，支持 OpenGL ES 3.2、Vulkan 1.1、OpenCL 2.2，用于图形渲染与轻量并行计算。
- **多媒体**：双 ISP 支持 32 MP @ 30 fps 单摄或 16 MP + 16 MP 双摄；视频解码 4K75（H.264/H.265/VP9/AV1），编码 4K30（H.264/H.265）。
- **连接**：GbE（TSN）、PCIe 2.0 x1、USB 3.2 Gen1、Wi-Fi 6 / BT 5（外部 Combo）。

NPU 峰值算力公式：
$$T_{NPU} = 4.0\ \text{TOPS INT8}$$
实际推理吞吐受模型算子支持度、内存带宽（LPDDR4X-3733）与 batch size 影响。

## 关键参数表

| 参数 | 数值 | 备注/来源 |
|------|------|-----------|
| 芯片型号 | MT8390 | MediaTek 公开资料 |
| 制程 | 6 nm | MediaTek |
| CPU | 2× Cortex-A78 @ 2.2 GHz + 6× Cortex-A55 @ 2.0 GHz | MediaTek |
| GPU | Arm Mali-G57 MC3 @ 950 MHz | MediaTek |
| NPU | MediaTek 第五代 NPU，4.0 TOPS INT8 | MediaTek Factsheet |
| DSP | Cadence Tensilica VP6 + HiFi5 | MediaTek |
| 内存 | LPDDR4X-3733，最高 8 GB | MediaTek |
| 存储 | eMMC 5.1 / SD 3.0 / SPI-NOR | MediaTek |
| ISP | 双 ISP，32 MP @ 30 fps / 16 MP + 16 MP @ 30 fps | MediaTek |
| 视频解码 | 4K75（H.264/H.265/VP9/AV1） | MediaTek |
| 视频编码 | 4K30（H.264/H.265） | MediaTek |
| 显示 | 4K60 + 4K30 双显 / 4K60 单显 | MediaTek |
| 网络 | 1× GbE MAC（TSN） | MediaTek |
| 高速接口 | PCIe 2.0 x1、USB 3.2 Gen1 | MediaTek |
| 无线 | Wi-Fi 6 / BT 5（外部 MT7921 或 MT7663） | MediaTek |
| 封装 | VFBGA 15 mm × 15 mm × 0.9 mm，0.4 mm pitch | MediaTek |
| 工作结温 | 消费级 -20 °C – 95 °C；工业级 -40 °C – 105 °C | MediaTek |
| 产品供货期 | 至 2034 年 | MediaTek |

## 应用场景

- **机器人主控**：AMR/服务机器人导航、SLAM、多路视觉感知与运动规划。
- **边缘 AI 网关**：工业物联网数据采集、协议转换与本地 AI 推理。
- **智能零售与数字标牌**：4K 双屏、客流分析与广告推送。
- **工业 HMI**：触控交互、设备监控与预测性维护。

## 供应链关系

- **制造商**：MediaTek（ent_company_mediatek），台湾半导体设计公司。
- **上游关键物料**：台积电 6 nm 代工、ARM CPU/GPU IP、自研 APU、LPDDR4X、eMMC/UFS、封测。
- **下游整机集成**：AIoT 设备商、机器人整机厂、智能零售与工业网关客户。
- **竞争/对标**：Qualcomm QCS610/6490、NVIDIA Jetson Orin Nano、Rockchip RK3588、Allwinner T527、NXP i.MX 8M Plus/93。

## 来源与验证

- MediaTek Genio 700 Factsheet：https://www.mediatek.com/hubfs/Factsheet-Genio-700.pdf
- MediaTek Genio 700 产品页：https://genio.mediatek.com/genio-700
- Rutronik 新闻稿：https://www.automation-mag.com/news/71281-high-performance,-ai-powered-soc-for-embedded-and-iot-applications-mediatek-genio-700-new-at-rutronik