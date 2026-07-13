---
id: ent_product_ambarella_cv7
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Ambarella CV7
  en: Ambarella CV7
status: active
sources:
- id: src_ambarella_cv7_press
  type: website
  url: https://investor.ambarella.com/news-releases/news-release-details/ambarella-launches-powerful-edge-ai-8k-vision-soc-industry
- title: Ambarella Launches Powerful Edge AI 8K Vision SoC - Ambarella Inc.
- id: src_ambarella_cv7_consumer
  type: website
  url: https://www.ambarella.com/products/consumer/
- title: Consumer Products - Ambarella
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# Ambarella CV7 / Ambarella CV7

## 概述

Ambarella CV7 是安霸（Ambarella）于 CES 2026 发布的 4 nm 边缘 AI 视觉 SoC，面向 8K 消费相机、多目企业安防相机、无人机、工业机器人、ADAS 及视频会议等场景。CV7 集成第三代 CVflow AI 加速器、图像信号处理器（ISP）、硬件视频编解码器与四核 Arm Cortex-A73 CPU，在同等负载下功耗较上一代 CV5 降低约 20%。

## 工作原理 / 技术架构

CV7 采用三星 4 nm 工艺与安霸“算法优先”架构，将 AI 推理、ISP 处理、视频编码/解码及通用计算集成于单芯片。其 CVflow 加速器针对 CNN 与 Transformer 网络同时运行优化，AI 性能约为 CV5 的 2.5 倍。视频编码单元支持 H.264/H.265/MJPEG，可编码单路 4K@240 fps、双路 8K@30 fps 或四路以上 4K@30 fps。

算力方面，虽然安霸未公布 CV7 的绝对 TOPS 数值，但 AI 性能提升倍数可表示为：

$$
\text{Performance}_{CV7} \approx 2.5 \times \text{Performance}_{CV5}
$$

ISP 支持 HDR、鱼眼去畸变、3D 运动补偿时域滤波（MCTF）及低至 0.01 lux 的低照度成像。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 制程 | 三星 4 nm |
| CPU | 四核 Arm Cortex-A73（性能约为 CV5 的 2 倍） |
| AI 加速器 | 第三代 CVflow |
| AI 性能 | 约为 CV5 的 2.5 倍 |
| 视频编码 | 单路 4K@240 fps / 双路 8K@30 fps / 多路 4K@30 fps |
| 视频格式 | H.264 / H.265 / MJPEG |
| ISP 特性 | HDR、鱼眼去畸变、3D MCTF |
| 最低照度 | 0.01 lux |
| 内存接口 | 64-bit LPDDR5 |
| 功耗 | 较 CV5 降低约 20% |
| 目标应用 | 8K 运动/全景相机、安防、无人机、工业机器人、ADAS、视频会议 |

## 应用场景

- 人形机器人/无人机的视觉感知与前处理
- 多目企业安防相机的实时 AI 分析
- 8K 运动相机与全景相机
- 车队管理 AI 视觉网关与 360° 环视系统
- 高性能视频会议终端

## 供应链关系

Ambarella 为上游 fabless 芯片设计公司，CV7 由三星代工制造，下游面向相机 OEM、汽车 Tier-1、安防厂商与机器人企业。在机器人产业链中，CV7 可作为视觉前处理与边缘 AI 推理芯片，与主控 SoC、激光雷达、IMU 等形成多传感器融合方案。

## 来源与验证

参数来源于安霸官方新闻稿（https://investor.ambarella.com/news-releases/news-release-details/ambarella-launches-powerful-edge-ai-8k-vision-soc-industry）及安霸官网消费产品线页面（https://www.ambarella.com/products/consumer/）。安霸未公开 CV7 的绝对 TOPS 与定价，绝对算力标注为“未公开”。