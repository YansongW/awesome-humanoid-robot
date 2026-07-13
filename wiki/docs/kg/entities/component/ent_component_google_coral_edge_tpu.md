---
id: ent_component_google_coral_edge_tpu
type: component
schema_version: 1
domain: 02_components
status: active
names:
  zh: Google Coral Edge TPU
  en: Google Coral Edge TPU
sources:
- id: src_google_coral_dev_board
  type: website
- title: Coral Dev Board 产品页
  url: https://coral.ai/products/dev-board/
- id: src_google_coral_docs
  type: website
- title: Coral 官方文档
  url: https://coral.ai/docs/
- id: src_google_coral_usb_amazon
  type: website
- title: Coral USB Accelerator with Edge TPU Coprocessor Product Description
  url: https://www.amazon.in/ROBOTICSSIGN-Coral-USB-Accelerator/dp/B0D7VJCL5H
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official Coral product pages and verified reseller
    descriptions; power and form factor vary by carrier board.
---


# Google Coral Edge TPU

## 概述

Google Coral Edge TPU 是 Google 推出的专用边缘 AI 加速器 ASIC，可在极低功耗下完成神经网络推理。Edge TPU 支持 INT8 量化模型，峰值算力 4 TOPS，典型能效约 2 TOPS/W。Coral 平台提供 Dev Board、USB Accelerator、PCIe/M.2 Accelerator 及 SoM 等多种产品形态，面向智能相机、机器人、工业检测与 AIoT 设备，其软件栈基于 TensorFlow Lite，可通过 Edge TPU Compiler 将量化模型高效部署到端侧。

## 工作原理 / 技术架构

Edge TPU 是一款专为神经网络推理设计的低功耗 AI 加速器：

1. **INT8 量化推理**：Edge TPU 仅支持 INT8 量化模型，通过降低权重与激活值的位宽，在保持可接受精度的同时大幅提升推理速度与能效。
2. **张量处理单元**：内部包含固定功能的矩阵乘加单元，针对卷积、全连接等常见算子高度优化。
3. **片上 SRAM 与外部内存**：SoM 版本集成 LPDDR4 内存，USB/PCIe 版本通过主机接口访问系统内存。
4. **TensorFlow Lite 生态**：模型需先转换为 TensorFlow Lite 格式并经 INT8 量化，再由 Edge TPU Compiler 编译生成可执行指令。

在端侧视觉任务中，Edge TPU 的推理帧率 $F$ 与模型单次运算量 $O$、峰值算力 $P$、利用率 $\eta$ 的关系可近似表示为

$$
F = \frac{P \cdot \eta}{O}
$$

例如，MobileNet v2 在 Edge TPU 上可达近 400 fps，体现了其在低功耗视觉任务中的高效性。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制造商 | Google / Alphabet（Google Coral） | 官网 |
| 产品形态 | Edge TPU ASIC / Coral SoM / Dev Board / USB / PCIe / M.2 | Coral 官网 |
| AI 峰值算力 | 4 TOPS（INT8） | Coral 公开资料 |
| 能效 | 约 2 TOPS/W | Coral 公开资料 |
| 支持精度 | INT8 量化 | Coral 官方文档 |
| 模型框架 | TensorFlow Lite（需 INT8 量化） | Coral 官方文档 |
| Dev Board SoC | NXP i.MX 8M（四核 Cortex-A53 + Cortex-M4F） | Coral 公开资料 |
| Dev Board 内存 | 1 GB / 4 GB LPDDR4（依版本） | Coral 公开资料 |
| Dev Board 存储 | 8 GB / 16 GB / 64 GB eMMC + MicroSD | Coral 公开资料 |
| Dev Board 接口 | USB 3.0、GbE、HDMI 2.0、MIPI CSI/DSI、40-pin GPIO、PCIe | Coral 公开资料 |
| Dev Board 尺寸 | 约 88 mm × 60 mm（含散热器） | Coral 公开资料 |
| USB Accelerator 功耗 | 约 2 W | Coral 公开资料 |
| USB Accelerator 尺寸 | 约 65 mm × 30 mm | Coral/经销商资料 |
| Dev Board 参考价格 | 约 150 USD | Coral 公开资料 |
| USB Accelerator 参考价格 | 约 75 USD | Coral/经销商资料 |
| 价格 | 依形态而定 | 公开资料 |

## 应用场景

- **机器人端侧感知**：实时目标检测、语义分割与导航辅助，降低对云端算力的依赖。
- **智能相机与安防**：本地事件检测、人脸识别与异常行为分析，提升隐私保护与响应速度。
- **工业视觉检测**：缺陷分类、条码/二维码识别、产线质检。
- **AIoT 设备**：为智能家居、可穿戴设备、零售分析提供低功耗 AI 能力。
- **开发验证与原型**：Coral Dev Board 与 USB Accelerator 是边缘 AI 原型开发的常用平台。

## 供应链关系

Google Coral（`ent_company_google_coral`）是 Alphabet/Google 旗下的边缘 AI 平台。Edge TPU（`ent_component_google_coral_edge_tpu`）作为其核心 AI 加速器，被应用于 Coral Dev Board（`ent_product_google_coral_dev_board`）与 Coral USB Accelerator（`ent_product_google_coral_usb_accelerator`）等产品中。上游供应链包括台积电晶圆代工、NXP i.MX 8M SoC、LPDDR4/eMMC、封测、PCB/模组；下游客户包括 AIoT 设备商、机器人整机厂、智能相机厂商、工业视觉方案商与开发者。Google Coral 与 Intel Movidius、Hailo、NVIDIA Jetson Nano、Qualcomm QCS、地平线征程等形成竞争。

## 来源与验证

- Coral 官网 Dev Board 产品页与官方文档提供了 Edge TPU 算力、能效、软件栈与开发板规格。
- 经销商与公开评测确认了 USB Accelerator 的 4 TOPS INT8、2 W 功耗、65 mm × 30 mm 尺寸等参数。
- Google Coral 官方文档明确了 Edge TPU 仅支持 INT8 量化 TensorFlow Lite 模型的限制。