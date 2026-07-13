---
id: ent_component_qrb5165_soc
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Qualcomm QRB5165 机器人系统级芯片
  en: Qualcomm QRB5165 Robotics SoC
status: active
sources:
- id: src_ent_component_qrb5165_soc_qualcomm
  type: document
  url: https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/qrb5165-soc-product-brief_87-28730-1-b.pdf
- id: src_ent_component_qrb5165_soc_einfochips
  type: document
  url: https://static6.arrow.com/aropdfconversion/b8d477ea71f2b0c22bdb152545c4e137d7f42a7c/lcomm-qrb5165-einfochips-qrb5165-som-technical-datasheet.pdf
- id: src_ent_component_qrb5165_soc_lantronix
  type: document
  url: https://cdn.lantronix.com/wp-content/uploads/pdf/Lantronix-QRB5165-SOM-ProductBrief-1.pdf
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# Qualcomm QRB5165 机器人系统级芯片 / Qualcomm QRB5165 Robotics SoC

## 概述

Qualcomm QRB5165 是一款面向高端机器人、无人机、边缘 AI 盒子和协作智能机器的系统级芯片（SoC）。该芯片基于 7 nm 工艺，集成 Kryo 585 CPU、Adreno 650 GPU、Hexagon 698 DSP、Spectra 480 ISP 以及第五代 Qualcomm AI 引擎，提供高达 15 TOPS 的端侧 AI 算力，支持多路摄像头、4K/8K 视频编解码以及 5G 连接扩展，是 Qualcomm Robotics RB5/RB6 平台的核心计算单元。

## 工作原理与技术架构

QRB5165 采用异构计算架构，将通用计算、图形渲染、数字信号处理、计算机视觉和 AI 加速分布在不同专用核上：

- **Kryo 585 CPU**：八核 Arm Cortex-A77/A55，最高主频 2.84 GHz，负责操作系统、ROS/ROS2 控制栈及通用任务。
- **Adreno 650 GPU**：支持 OpenGL ES、OpenCL、Vulkan，用于图形渲染与通用并行计算。
- **Hexagon 698 DSP**：集成 HVX、Hexagon 张量加速器（HTA）和标量加速器，用于低功耗 AI 与 CV 处理。
- **Spectra 480 ISP**：支持 2 Gigapixels/s 吞吐量，最多 7 路并发摄像头、200 MP 照片捕获、8K30 录制。
- **第五代 AI 引擎**：CPU+GPU+DSP+HTA 协同，峰值 AI 性能 15 TOPS。

存储接口方面，QRB5165 支持 LPDDR5（最高 2750 MHz）和 LPDDR4X（最高 2133 MHz），最大容量可达 16 GB；其 64 bit LPDDR5 接口的理论峰值带宽为：

$$
B_{\text{DDR5}} = \frac{5500\ \text{MT/s} \times 64\ \text{bit}}{8} \approx 44\ \text{GB/s}
$$

外部接口包括 MIPI DSI/CSI、USB 3.1、PCIe、SD、Wi-Fi 6 / 蓝牙 5.1（需配套芯片）以及工业以太网 EtherCAT/TSN。

## 关键参数表

| 参数项 | 数值/范围 | 备注 |
|--------|-----------|------|
| 制程工艺 | 7 nm | — |
| CPU | Kryo 585，八核，最高 2.84 GHz | 4×Gold + 4×Silver |
| GPU | Adreno 650 | OpenGL ES / OpenCL / Vulkan |
| DSP | Hexagon 698（HVX + HTA + Scalar） | — |
| ISP | Spectra 480，双 14-bit | — |
| AI 算力 | 最高 15 TOPS | 第五代 AI 引擎 |
| 内存 | LPDDR5 最高 16 GB @ 2750 MHz / LPDDR4X | — |
| 存储 | UFS 2.1 / SD | 依模组配置 |
| 摄像头 | 最高 200 MP 单摄 / 25 MP 双摄 / 7 路并发 | — |
| 视频编码 | 4K@120 fps / 8K@30 fps | H.265/H.264/VP8 |
| 视频解码 | 4K@240 fps / 8K@60 fps | H.265/H.264/VP9/VP8/MPEG-2 |
| 连接 | Wi-Fi 6、BT 5.1（配套芯片）、USB 3.1、PCIe | — |
| 显示 | MIPI DSI / DisplayPort over USB3.1 | — |
| 工作温度 | -30 ℃ ~ +105 ℃ | 工业级 |
| 操作系统 | Ubuntu / Linux | 机器人常用 |
| 典型功耗 | 未公开 | 依赖模组散热设计 |

## 应用场景

- **自主移动机器人（AMR）与配送机器人**：多摄像头感知、VSLAM、路径规划。
- **无人机与无人车**：4K/8K 航拍、实时图传、AI 目标识别。
- **协作机器人与人形机器人**：视觉伺服、语音交互、边缘 AI 推理。
- **边缘 AI 盒子与工业网关**：机器视觉质检、预测性维护。

## 供应链关系

- **设计商**：Qualcomm Technologies, Inc.。
- **上游关键物料**：TSMC/Samsung 7 nm 晶圆代工、LPDDR5/UFS 存储、RF 前端、电源管理 IC、散热/屏蔽结构件。
- **中游模组商**：Lantronix Open-Q QRB5165 SOM、eInfochips QRB5165 SOM、ADLINK LEC-RB5 等核心板/模组厂商。
- **下游集成**：机器人 OEM、无人机厂商、边缘计算设备商。
- **知识图谱关系**：
  - `ent_company_qualcomm` — `designs` → `ent_component_qrb5165_soc`
  - `ent_component_qrb5165_soc` — `used_in` → 机器人整机/开发套件产品节点

## 来源与验证

- Qualcomm 官方产品简报《QRB5165 SoC for IoT Product Brief》披露了 CPU、GPU、DSP、ISP、AI 性能、内存、摄像头、视频、接口及工业温度范围。
- eInfochips QRB5165 SOM 技术数据表给出了模组级别的内存（8 GB LPDDR5）、存储（64 GB UFS 2.1）、供电（12 V/5 A）及机械尺寸（59.7 mm × 32.2 mm）。
- Lantronix Open-Q QRB5165 SOM 产品简报进一步确认了 8 GB LPDDR5 + 128 GB UFS、15 TOPS AI、Ubuntu + ROS2 支持等量产级信息。