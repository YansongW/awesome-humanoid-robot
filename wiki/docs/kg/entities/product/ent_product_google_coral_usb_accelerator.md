---
id: ent_product_google_coral_usb_accelerator
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Google Coral USB Accelerator
  en: Google Coral USB Accelerator
status: active
sources:
- id: src_coral_usb_datasheet
  type: document
  url: https://cdn-reichelt.de/documents/datenblatt/A300/CORAL-USB-ACCELERATOR-DATASHEET.pdf
- title: Coral USB Accelerator Datasheet
- id: src_pi3g_coral_usb
  type: article
  url: https://pi3g.com/products/machine-learning/google-coral/coral-usb-accelerator/
- title: Coral USB Accelerator Product Page
- id: src_ricelee_coral_usb
  type: article
  url: https://ricelee.com/product/google-usb-accelerator
- title: Coral USB Accelerator Edge TPU Coprocessor
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# Coral USB Accelerator / Google Coral USB Accelerator

## 概述

Google Coral USB Accelerator 是一款基于 Edge TPU 的 USB 人工智能推理加速器。它通过 USB 3.0 Type-C 接口为现有主机系统提供高速、低功耗的 TensorFlow Lite 模型推理能力，常用于嵌入式视觉、机器人感知与物联网边缘 AI 应用。Edge TPU 是 Google 设计的专用 ASIC，针对 INT8 量化神经网络进行了优化。

## 工作原理 / 技术架构

Coral USB Accelerator 的核心为单颗 Google Edge TPU：

1. **模型部署**：在主机或服务器上使用 TensorFlow Lite 训练并量化模型，再通过 Edge TPU Compiler 编译为可在 Edge TPU 上执行的 TFLite 图。
2. **推理卸载**：主机通过 USB 3.0 将输入数据发送至 Edge TPU，Edge TPU 执行前向推理后将结果返回主机，显著降低 CPU 负载与推理延迟。
3. **功耗与散热**：默认频率下功耗约 2 W，最大频率下性能翻倍但功耗与发热增加，需要在 25 °C 以下环境使用或加装散热。

峰值算力与能效可表示为

$$
\text{TOPS}=4,\quad \eta=\frac{4\ \text{TOPS}}{2\ \text{W}}=2\ \text{TOPS/W}.
$$

对于 MobileNet v2 等典型移动视觉模型，单颗 Edge TPU 可实现约 400 FPS 的推理帧率。

## 关键参数表

| 参数 | 数值 / 说明 |
|---|---|
| AI 加速器 | Google Edge TPU |
| 峰值算力 | 4 TOPS（INT8） |
| 典型功耗 | 约 2 W |
| 能效 | 2 TOPS/W |
| 主机接口 | USB 3.0 / USB 3.1 Gen1 Type-C |
| 尺寸 | 65 × 30 × 8 mm |
| 典型模型性能 | MobileNet v2 ≈ 400 FPS |
| 主机系统支持 | Linux（Debian/Ubuntu）、macOS、Windows |
| 模型框架 | TensorFlow Lite |
| 频率模式 | 默认 / 最大（性能翻倍，发热增加） |
| 温度限制（默认/最大） | 35 °C / 25 °C 环境温度 |

## 应用场景

- **机器人视觉**：目标检测、语义分割、姿态估计的端侧加速。
- **智能摄像头**：人脸识别、行为分析、入侵检测。
- **工业质检**：缺陷检测、分类与计数。
- **物联网网关**：本地推理，减少云端依赖与隐私风险。
- **科研教育**：边缘 AI 与嵌入式深度学习原型开发。

## 供应链关系

- **上游**：Google 设计 Edge TPU ASIC；华硕等合作伙伴负责制造与销售；上游包括晶圆代工、USB 控制器、PCB 与外壳供应商。
- **同层**：Coral USB Accelerator 作为通用 USB AI 加速器，可搭配 Raspberry Pi、x86/ARM Linux 主机、NVIDIA Jetson 等使用。
- **下游**：机器人开发商、IoT 设备商、智能相机厂商、工业视觉集成商与个人开发者。

## 来源与验证

- Coral USB Accelerator 数据手册：https://cdn-reichelt.de/documents/datenblatt/A300/CORAL-USB-ACCELERATOR-DATASHEET.pdf
- pi3g 产品页：https://pi3g.com/products/machine-learning/google-coral/coral-usb-accelerator/
- Ricelee 产品说明：https://ricelee.com/product/google-usb-accelerator