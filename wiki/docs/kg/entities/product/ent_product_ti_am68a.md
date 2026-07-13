---
id: ent_product_ti_am68a
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 德州仪器 AM68A 视觉 SoC
  en: Texas Instruments AM68A Vision SoC
status: active
sources:
- id: src_ti_am68a_product
  type: website
  url: https://www.ti.com.cn/product/cn/AM68A
- title: AM68A 数据表、产品信息和支持 - 德州仪器 TI.com.cn
- id: src_ti_am68a_press
  type: website
  url: https://www.ti.com.cn/zh-cn/about-ti/newsroom/news-releases/2023/ti-unlocks-scalable-edge-ai-performance-in-smart-camera-applications-with-new-vision-processor-family.html
- title: 德州仪器推出全新视觉处理器系列 - TI.com.cn
- id: src_ti_am68a_edge_impulse
  type: website
  url: https://docs.edgeimpulse.com/hardware/boards/ti-sk-am68a
- title: Texas Instruments SK-AM68A - Edge Impulse
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 德州仪器 AM68A 视觉 SoC / Texas Instruments AM68A Vision SoC

## 概述

AM68A 是德州仪器（Texas Instruments）推出的 AM6xA 系列视觉处理器，面向 1–8 路摄像头的机器视觉、自主移动机器人（AMR）、智能交通与零售自动化等边缘 AI 应用。该芯片在单颗 SoC 内集成 Arm 应用处理器、实时控制核心、ISP、深度学习加速器与视频编解码单元，可在低功耗条件下提供 8 TOPS 的 AI 算力。

## 工作原理 / 技术架构

AM68A 采用异构多核架构：

- **应用处理**：2× Arm Cortex-A72 @ 2.0 GHz，L2 缓存 1 MB，运行 Linux/QNX 等高级操作系统；
- **实时控制**：4× Arm R5F 内核，用于传感器触发、编码器接口、EtherCAT/CAN FD 通信等实时任务；
- **视觉处理**：第三代 ISP，最高 480 MP/s，支持镜头失真校正、多尺度缩放、噪声滤波；
- **AI 加速**：矩阵乘法加速器（MMA，Deep Learning Accelerator），提供 8 TOPS 定点推理能力；
- **视频编解码**：支持 H.264/H.265 硬件编解码。

对于分辨率为 \(W \times H\)、帧率为 \(f\)、每帧运算量为 \(O\) 的神经网络，单路推理所需算力为

\[
\text{OPS}_{\text{req}} = W \cdot H \cdot f \cdot O
\]

AM68A 的 8 TOPS 峰值算力可支持多路轻量模型并行推理。

## 关键参数表

| 参数 | 数值 |
|------|------|
| CPU | 2× Arm Cortex-A72 @ 2.0 GHz |
| 实时内核 | 4× Arm R5F |
| AI 算力 | 8 TOPS |
| 支持摄像头路数 | 1–8 路 |
| ISP 处理能力 | 最高 480 MP/s |
| 显示接口 | eDP、2× DSI、MIPI DPI |
| PCIe | 1× PCIe Gen3 |
| 硬件加速器 | 深度学习加速器、视频编解码加速器、视觉处理加速器 |
| 工作温度范围 | \(-40^\circ\text{C} \sim 105^\circ\text{C}\) |
| 操作系统 | Linux / QNX / RTOS |
| 安全特性 | 加密加速、安全启动、安全存储 |

## 应用场景

- 工业机器视觉检测与缺陷识别
- AMR/服务机器人的多摄像头感知
- 智能交通监控与车牌识别
- 零售自动化与智能结算
- 边缘 AI 摄像头与安防系统

## 供应链关系

AM68A 由德州仪器设计并提供。上游为晶圆代工与封装测试环节；中游为 TI 自研的 SoC、软件开发工具包（Edge AI Studio、Processor SDK）与参考设计；下游面向工业相机、机器人、智能交通与零售设备制造商。AM68A 与 AM62A（1–2 路摄像头）、AM69A（1–12 路摄像头）共同构成 TI 可扩展视觉处理器产品线。

## 来源与验证

参数直接引用德州仪器官方产品页与新闻稿。典型功耗、封装尺寸、具体 SKU 价格等未在公开资料中披露，标注为“未公开”。