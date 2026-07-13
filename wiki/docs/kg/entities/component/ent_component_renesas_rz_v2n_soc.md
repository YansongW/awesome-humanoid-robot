---
id: ent_component_renesas_rz_v2n_soc
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 瑞萨电子 RZ/V2N 视觉 AI MPU
  en: Renesas RZ/V2N Vision AI MPU / SoC
status: active
sources:
- id: src_renesas_rzv2n_flyer
  type: pdf
- title: Renesas RZ/V2N Group Flyer
  url: https://www.renesas.com/en/document/fly/renesas-rzv2n-group
- id: src_mouser_rzv2n
  type: website
- title: Mouser – Renesas RZ/V2N MPUs
  url: https://www.mouser.cn/new/renesas/renesas-rz-v2n-mpus/
- id: src_hackster_rzv2n
  type: website
- title: Hackster – Renesas RZ/V2N 15 TOPS Edge AI Chip
  url: https://www.hackster.io/news/renesas-announces-the-rz-v2n-a-15-pruned-tops-energy-efficient-chip-for-edge-ai-and-computer-vision-69a0c88c6a02
- id: src_solidrun_rzv2n
  type: website
- title: SolidRun RZ/V2N SOM
  url: https://www.solid-run.com/embedded-industrial-iot/renesas-rz-family/rz-v2n-som/
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official flyer and verified distributor pages;
    missing values marked as 未公开.
---


# 瑞萨电子 RZ/V2N 视觉 AI MPU / Renesas RZ/V2N Vision AI MPU / SoC

## 概述

RZ/V2N 是瑞萨电子（Renesas Electronics）推出的中端视觉 AI 微处理器（MPU/SoC），面向机器人、智能相机、工业视觉、ADAS 驾驶员监控（DMS）及边缘 AI 网关。该芯片集成四核 Arm Cortex-A55 应用处理器、Cortex-M33 实时控制核心，以及瑞萨自研第三代动态可重配置处理器 AI 加速器（DRP-AI3），以无风扇低功耗设计实现较高能效比的神经网络推理。

## 工作原理 / 技术架构

RZ/V2N 采用异构多核架构：

- **应用处理**：四核 Arm Cortex-A55 @ 1.8 GHz，运行 Linux 与高层应用。
- **实时控制**：单核 Arm Cortex-M33 @ 200 MHz，负责低功耗管理与实时任务。
- **AI 加速**：DRP-AI3 结合动态可重配置处理器与 AI-MAC，支持 INT8 量化与剪枝（pruning），稀疏模型下峰值算力达 15 TOPS，稠密模型下约 4 TOPS，官方标称能效约 10 TOPS/W。
- **视觉接口**：双路 4-lane MIPI CSI-2，可选 Arm Mali-C55 ISP；支持 H.264/H.265 硬件编解码。
- **高速外设**：PCIe Gen3（1 lane × 1 或 2 lane × 1，依封装）、USB 3.2 Gen2×1、双 Gigabit Ethernet、6× CAN-FD。
- **内存**：32-bit LPDDR4/LPDDR4X 接口，支持 ECC，带宽约 12.8 GB/s。

AI 推理性能与功耗的关系可近似表示为

$$
E_{\text{op}} = \frac{P}{\text{TOPS}}
$$

其中 $P$ 为芯片功耗，$E_{\text{op}}$ 为每 TOPS 能耗。RZ/V2N 通过 10 TOPS/W 的标称能效，在典型 3–6 W 功耗区间运行中等规模 CNN/Transformer 视觉模型。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| CPU | 4× Arm Cortex-A55 @ 1.8 GHz + Arm Cortex-M33 @ 200 MHz | Renesas 官方 flyer |
| AI 加速器 | DRP-AI3 | Renesas 官方 flyer |
| AI 算力 | 15 TOPS（稀疏）/ 4 TOPS（稠密） | Renesas / Mouser |
| AI 能效 | 约 10 TOPS/W | Renesas 官方 flyer |
| 相机接口 | 2× 4-lane MIPI CSI-2 | Renesas 官方 flyer |
| ISP | 可选 Arm Mali-C55 | Renesas 官方 flyer |
| 视频编解码 | H.264 / H.265 硬件编解码 | Renesas / SolidRun |
| 内存接口 | 32-bit LPDDR4/LPDDR4X，支持 ECC | Renesas 官方 flyer |
| 内存带宽 | 约 12.8 GB/s | Mouser / Renesas |
| 网络 | 2× GbE | Renesas 官方 flyer |
| 扩展接口 | PCIe Gen3、USB 3.2 Gen2×1、6× CAN-FD | Renesas 官方 flyer |
| ADC | 12-bit，24 通道 | Renesas 官方 flyer |
| 封装 | 15 mm × 15 mm，840-pin BGA，0.5 mm pitch | Renesas 官方 flyer |
| 功耗 | 典型 3–6 W（公开报道） | TenXer Labs / SolidRun |
| 制程 | 未公开 | - |

## 应用场景

- **移动机器人**：多路视觉 SLAM、目标检测、动态避障与路径规划。
- **智能工业相机**：缺陷检测、尺寸测量、OCR、条码识别。
- **服务机器人**：人脸识别、手势识别、环境感知。
- **ADAS / DMS**：驾驶员疲劳/分心监测、舱内感知。
- **AI 视觉网关**：多摄像头汇聚与边缘推理。

## 供应链关系

- **上游**：台积电晶圆代工、ARM CPU/ISP IP、LPDDR4x 存储、封测、PMIC。
- **制造商**：`ent_company_renesas` -- `manufactures` --> `ent_component_renesas_rz_v2n_soc`。
- **下游关系**：`ent_product_renesas_rz_v2n` -- `uses` --> `ent_component_renesas_rz_v2n_soc`。
- **客户/应用**：机器人公司、智能相机厂商、汽车 Tier1/OEM、工业视觉集成商。
- **竞争对手/对标**：NXP i.MX、TI Jacinto、NVIDIA Jetson、地平线征程、Ambarella CV7/CV72。

## 来源与验证

1. Renesas RZ/V2N Group Flyer：https://www.renesas.com/en/document/fly/renesas-rzv2n-group
2. Mouser 产品页：https://www.mouser.cn/new/renesas/renesas-rz-v2n-mpus/
3. SolidRun RZ/V2N SOM：https://www.solid-run.com/embedded-industrial-iot/renesas-rz-family/rz-v2n-som/
4. Hackster 报道：https://www.hackster.io/news/renesas-announces-the-rz-v2n-a-15-pruned-tops-energy-efficient-chip-for-edge-ai-and-computer-vision-69a0c88c6a02