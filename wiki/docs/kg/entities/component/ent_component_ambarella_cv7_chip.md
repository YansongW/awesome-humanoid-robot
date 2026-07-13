---
id: ent_component_ambarella_cv7_chip
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 安霸 CV7 边缘 AI 视觉 SoC
  en: Ambarella CV7 Edge AI Vision SoC
status: active
sources:
- id: src_ambarella_cv7_press
  type: website
- title: Ambarella CV7 Press Release
  url: https://investor.ambarella.com/news-releases/news-release-details/ambarella-launches-powerful-edge-ai-8k-vision-soc-industry
- id: src_ambarella_product
  type: website
- title: Ambarella AIoT & Robotics Product Page
  url: https://www.ambarella.com/products/aiot-industrial-robotics/
- id: src_ithome_cv7
  type: website
- title: IT之家 – 安霸 CV7 4nm 端侧 AI 视觉 SoC
  url: https://www.ithome.com/0/912/838.htm
- id: src_new_electronics_cv7
  type: website
- title: New Electronics – Ambarella CV7 Edge AI Vision Chip
  url: https://www.newelectronics.co.uk/content/news/ces-ambarellas-cv7-edge-ai-vision-chip-targets-8k-imaging-and-multi-sensor-applications
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Absolute AI TOPS value is not publicly disclosed by Ambarella; missing
    values marked as 未公开.
---


# 安霸 CV7 边缘 AI 视觉 SoC / Ambarella CV7 Edge AI Vision SoC

## 概述

CV7 是安霸（Ambarella）在 CES 2026 发布的旗舰边缘 AI 视觉系统级芯片（SoC），采用三星 4 nm 制程，集成四核 Arm Cortex-A73 CPU、第三代 CVflow AI 加速器、ISP、视频编解码与多传感器接口。该芯片支持多路视频流并发处理，最高可达 8Kp60，面向 8K 运动/全景相机、多传感器安防相机、无人机、机器人、工业自动化、视频会议及汽车 AI 视觉网关。

## 工作原理 / 技术架构

CV7 采用 Ambarella “算法优先”的异构 SoC 架构，将 ISP、视频编解码、CVflow AI 加速器、CPU 与高速 I/O 集成于单芯片。CVflow 第三代 AI 加速器支持 CNN 与 Transformer 网络并发执行，并面向大语言模型/视觉语言模型（LLM/VLM）等生成式 AI 进行优化。

视频编码性能较上一代 CV5 提升约 2 倍，支持：

- 单路 4Kp240 编码；
- 双路 8Kp30 编码；
- 多路 4Kp30 并发（适用于多目安防相机）。

低照度性能达 0.01 lux，支持 HDR、鱼眼去畸变与 3D 运动补偿时域滤波（MCTF）。

AI 性能方面，官方仅披露“相较 CV5 提升 2.5 倍以上”，未给出绝对 TOPS 数值。相对性能可写作

$$
\text{Perf}_{\text{CV7}} \approx 2.5 \times \text{Perf}_{\text{CV5}}
$$

功耗方面，CV7 在同等负载下较 CV5 降低约 20%。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制程 | 4 nm（三星） | Ambarella 新闻稿 |
| CPU | 四核 Arm Cortex-A73 | Ambarella 新闻稿 |
| CPU 性能 | 约为上一代 2× | Ambarella 新闻稿 |
| AI 加速器 | 第三代 CVflow | Ambarella 新闻稿 |
| AI 性能 | 较 CV5 提升 >2.5 倍 | Ambarella 新闻稿 |
| AI 算力（TOPS） | 未公开 | - |
| 视频编码 | 8Kp60；单 4Kp240 / 双 8Kp30 / 多 4Kp30 | Ambarella 新闻稿 |
| 视频格式 | H.264 / H.265 / MJPEG | Ambarella 新闻稿 |
| ISP | 集成高性能 ISP，支持 HDR、去畸变、MCTF | Ambarella 新闻稿 |
| 低照度 | 0.01 lux | Ambarella 新闻稿 |
| 内存接口 | 64-bit LPDDR5 | Ambarella 新闻稿 |
| 典型功耗 | 未公开 | - |
| 封装 | 未公开 | - |

## 应用场景

- **机器人视觉**：多路相机实时目标检测、语义分割、导航辅助。
- **8K 运动/全景相机**：高分辨率视频录制与 AI 增强图像处理。
- **多传感器安防相机**：企业级 4K/8K 多目 AI 分析。
- **无人机**：高分辨率航拍、避障与跟踪。
- **视频会议**：4K/8K 智能取景与背景虚化。
- **汽车 AI 网关**：车队视频远程信息处理、360° 环视、DMS/OMS。

## 供应链关系

- **上游**：三星 4 nm 晶圆代工、ARM CPU IP、ISP/视频 IP、LPDDR5 存储、封测、模组。
- **制造商**：`ent_company_ambarella` -- `manufactures` --> `ent_component_ambarella_cv7_chip`。
- **下游关系**：`ent_product_ambarella_cv7` -- `uses` --> `ent_component_ambarella_cv7_chip`。
- **客户**：安防相机厂商、无人机公司、汽车 Tier1/OEM、机器人整机厂、视频会议设备商。
- **竞争对手/对标**：Qualcomm QCS、NVIDIA Jetson、地平线征程、海思 HiSilicon、Renesas RZ/V2H。

## 来源与验证

1. Ambarella CV7 新闻稿：https://investor.ambarella.com/news-releases/news-release-details/ambarella-launches-powerful-edge-ai-8k-vision-soc-industry
2. Ambarella 产品页：https://www.ambarella.com/products/aiot-industrial-robotics/
3. IT之家报道：https://www.ithome.com/0/912/838.htm
4. New Electronics 报道：https://www.newelectronics.co.uk/content/news/ces-ambarellas-cv7-edge-ai-vision-chip-targets-8k-imaging-and-multi-sensor-applications

> 注：安霸官方未公开 CV7 的绝对 AI TOPS、典型功耗及封装信息，已标注为“未公开”。