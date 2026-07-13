---
id: ent_component_nvidia_jetson_agx_orin
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: NVIDIA Jetson AGX Orin
  en: NVIDIA Jetson AGX Orin
status: active
created_at: 2026-07-01 00:00:00+00:00
updated_at: 2026-07-13 00:00:00+00:00
sources:
- id: src_nvidia_agx_orin_datasheet
  type: datasheet
- title: NVIDIA Jetson AGX Orin Module Series Datasheet
  url: https://openzeka.com/en/wp-content/uploads/2022/08/Jetson-AGX-Orin-Module-Series-Datasheet.pdf
- id: src_nvidia_agx_orin_devkit_datasheet
  type: datasheet
- title: NVIDIA Jetson AGX Orin Developer Kit Datasheet
  url: https://static6.arrow.com/aropdfconversion/arrowresources/3e0f93dc18d2fbe2cceb9b8218d496713cc9b980/jetson-agx-orin-developer-kit-datasheet-nvidia-a4-2203098-r1-web.pdf
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: 参数引自 NVIDIA 官方 datasheet；缺失值标注为“未公开”。
---


# NVIDIA Jetson AGX Orin / NVIDIA Jetson AGX Orin

## 概述

NVIDIA Jetson AGX Orin 是 NVIDIA 面向边缘 AI 与自主机器的高端计算模组，基于 Ampere GPU 架构与 Arm Cortex-A78AE CPU。64 GB 版本可提供最高 275 TOPS INT8 AI 算力（稀疏网络），在 15–60 W 可配置功耗范围内运行，广泛用于机器人主控、自动驾驶、医疗机器人与工业 AMR。

## 工作原理 / 技术架构

Jetson AGX Orin 采用异构计算架构，集成 GPU、CPU、双 NVDLA v2.0 深度学习加速器、PVA v2.0 视觉加速器与 ISP。AI 性能由多计算单元协同贡献，64 GB 版本的峰值 INT8 算力为

$$
\mathrm{TOPS}_{\mathrm{sparse}} = 275 \ \mathrm{TOPS}
$$

dense INT8 性能约为 170 TOPS。统一内存架构下，CPU 与 GPU 共享 64 GB LPDDR5，带宽 204.8 GB/s，支持多路 AI 流水线并发执行。开发者套件提供 PCIe Gen 4、10 GbE、USB 3.2、MIPI CSI-2 等高速接口，便于连接多摄像头、激光雷达与传感器。

## 关键参数表

| 参数 | Jetson AGX Orin 64GB | Jetson AGX Orin 32GB |
|------|----------------------|----------------------|
| AI 算力 | 275 TOPS INT8（稀疏） | 200 TOPS INT8（稀疏） |
| GPU | 2048 CUDA cores / 64 Tensor Cores | 1792 CUDA cores / 56 Tensor Cores |
| GPU 最高频率 | 1.3 GHz | 930 MHz |
| CPU | 12-core Arm Cortex-A78AE v8.2 | 8-core Arm Cortex-A78AE v8.2 |
| CPU 最高频率 | 2.2 GHz | 2.2 GHz |
| L2 / L3 缓存 | 3 MB / 6 MB | 2 MB / 4 MB |
| DL 加速器 | 2× NVDLA v2.0 | 2× NVDLA v2.0 |
| 内存 | 64 GB 256-bit LPDDR5 | 32 GB 256-bit LPDDR5 |
| 内存带宽 | 204.8 GB/s | 204.8 GB/s |
| 存储 | 64 GB eMMC 5.1 | 64 GB eMMC 5.1 |
| 功耗 | 15–60 W | 15–40 W |
| 视频编码 | 2× 4K60 / 4× 4K30 / 8× 1080p60 / 16× 1080p30 (H.265) | 1× 4K60 / 3× 4K30 / 6× 1080p60 / 12× 1080p30 (H.265) |
| 视频解码 | 1× 8K30 / 3× 4K60 / 7× 4K30 / 11× 1080p60 / 22× 1080p30 (H.265) | 1× 8K30 / 3× 4K60 / 7× 4K30 / 11× 1080p60 / 22× 1080p30 (H.265) |
| 相机接口 | 16 lane MIPI CSI-2，最高 6 摄像头 | 16 lane MIPI CSI-2，最高 6 摄像头 |
| 网络 | 10 GbE（开发者套件） | 10 GbE（开发者套件） |
| 模组尺寸 | 100 mm × 87 mm | 100 mm × 87 mm |

## 应用场景

- 人形机器人主控大脑与多模态感知
- 自主移动机器人（AMR/AGV）导航与避障
- 自动驾驶感知与规划
- 医疗影像与手术机器人
- 工业视觉检测与边缘 LLM 推理

## 供应链关系

制造商为 NVIDIA Corporation（`ent_company_nvidia`）。该模组被多家人形机器人产品使用，例如 `ent_product_galbot_g1` 与 `ent_product_booster_t1`。上游关键原材料包括台积电代工、LPDDR5 存储、PMIC、载板与散热方案；下游客户包括机器人整机厂、自动驾驶公司与科研机构。知识图谱中的关键关系为：`ent_company_nvidia` -- `manufactures` --> `ent_component_nvidia_jetson_agx_orin`。

## 来源与验证

本卡片参数引自 NVIDIA Jetson AGX Orin 系列模组与开发者套件官方 datasheet。具体批量价格未公开。