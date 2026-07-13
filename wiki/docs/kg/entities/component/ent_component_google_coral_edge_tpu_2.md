---
id: ent_component_google_coral_edge_tpu_2
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: Google Coral Edge TPU（USB 加速器形态）
  en: Google Coral Edge TPU (USB Accelerator Form Factor)
status: active
created_at: 2026-07-01 00:00:00+00:00
updated_at: 2026-07-13 00:00:00+00:00
sources:
- id: src_coral_usb_datasheet
  type: datasheet
- title: Coral USB Accelerator Datasheet
  url: https://cdn-reichelt.de/documents/datenblatt/A300/CORAL-USB-ACCELERATOR-DATASHEET.pdf
- id: src_coral_official
  type: website
- title: Coral USB Accelerator Official Page
  url: https://coral.ai/products/usb-accelerator/
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: 参数引自 Coral 官方 datasheet 与产品页；缺失值标注为“未公开”。
---


# Google Coral Edge TPU（USB 加速器形态） / Google Coral Edge TPU (USB Accelerator Form Factor)

## 概述

Google Coral USB Accelerator 是一款基于 Edge TPU 的即插即用式 AI 推理加速器，通过 USB 3.0 Type-C 接口为现有主机系统提供 4 TOPS INT8 峰值算力。它主要用于机器人视觉、工业检测、智能相机原型与 AIoT 边缘推理场景，支持 Debian/Ubuntu Linux、macOS 与 Windows 10 主机平台。

## 工作原理 / 技术架构

Edge TPU 是 Google 专为 TensorFlow Lite 量化模型设计的低功耗 ASIC。其峰值算力与功耗关系可表示为

$$
\eta = \frac{4 \ \mathrm{TOPS}}{2 \ \mathrm{W}} = 2 \ \mathrm{TOPS/W}
$$

即在最大工作频率下，单颗 Edge TPU 可提供 4 TOPS INT8 峰值算力，典型功耗约 2 W。以 MobileNet v2 为例，理论推理帧率可达约 400 FPS。加速器通过 USB 3.1 Gen 1（5 Gbps）与主机交换数据，由主机端 Edge TPU Runtime 与 TensorFlow Lite 解释器驱动模型推理。

## 关键参数表

| 参数 | 典型值 | 备注 |
|------|--------|------|
| AI 加速器 | Google Edge TPU coprocessor | Coral 官方 |
| 峰值算力 | 4 TOPS（INT8） | 产品手册 |
| 能效 | 2 TOPS/W | 产品手册 |
| 接口 | USB 3.1 Gen 1 Type-C | 向下兼容 USB 2.0 |
| 典型功耗 | 约 2 W（满载） | 产品手册 |
| 空闲功耗 | 375–400 mW | M.2  datasheet 参考 |
| 尺寸 | 65 mm × 30 mm × 8 mm | 产品手册 |
| 工作温度 | 默认频率：最高 35 ℃；最大频率：最高 25 ℃ | 产品手册 |
| 软件支持 | TensorFlow Lite、Edge TPU Compiler、Debian/Ubuntu、Windows 10、macOS | 官方文档 |
| 配件 | USB Type-C 转 Type-A 线缆（300 mm ± 20 mm） | 产品手册 |
| 制程 | 未公开 | - |

## 应用场景

- 机器人端侧目标检测与语义分割
- 智能相机与 AIoT 设备原型
- 工业视觉质检与条码/二维码识别
- 边缘 AI 开发验证与模型部署
- 现有嵌入式平台的 AI 能力升级

## 供应链关系

制造商为 Google / Alphabet 旗下 Coral 团队（`ent_company_google_coral`）。上游关键原材料包括台积电晶圆代工、LPDDR/eMMC、PMIC、PCB 与模组；下游客户包括 AIoT 设备商、机器人整机厂、智能相机厂商与开发者。知识图谱中的关键关系为：`ent_company_google_coral` -- `manufactures` --> `ent_component_google_coral_edge_tpu_2`，并被产品实体 `ent_product_google_coral_usb_accelerator` 使用。

## 来源与验证

本卡片参数引自 Coral USB Accelerator 官方产品页与 datasheet。芯片制程、部分热参数未公开。