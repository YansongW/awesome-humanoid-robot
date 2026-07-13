---
id: ent_product_moore_threads_s80
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 摩尔线程 MTT S80 游戏显卡
  en: Moore Threads MTT S80 Graphics Card
status: active
sources:
- id: src_ithome_mtt_s80_spec
  type: website
  url: https://www.ithome.com/0/802/355.htm
- id: src_ithome_mtt_s80_review
  type: website
  url: https://www.ithome.com/0/772/404.htm
- id: src_ithome_mtt_s80_driver
  type: website
  url: https://www.ithome.com/0/740/570.htm
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 摩尔线程 MTT S80 游戏显卡 / Moore Threads MTT S80 Graphics Card

## 概述

MTT S80 是摩尔线程（Moore Threads）推出的国产全功能游戏显卡，基于自研 MUSA（Moore Threads Unified System Architecture）架构的“春晓”GPU 芯片，采用台积电 7 nm 工艺制造。该产品定位为消费级显卡，同时具备图形渲染、8K 视频编解码、通用计算、AI 推理与物理仿真能力，并是国内首批支持 Windows DirectX 图形接口的国产独立显卡之一。

## 工作原理 / 技术架构

MTT S80 的“春晓”GPU 集成四大计算引擎：图形渲染引擎、视频编解码引擎、通用计算引擎与张量计算引擎。图形渲染采用 MUSA 核心阵列，每个 MUSA 核心支持 FP32、FP16 与 INT8 等计算精度；显存子系统通过 256-bit 位宽连接 8 颗三星 GDDR6 显存，总容量 16 GB。

单精度浮点峰值算力可由核心数与主频估算：

$$
\text{FP32}_{\text{peak}} = N_{\text{cores}} \cdot f_{\text{clk}} \cdot 2
$$

按 4096 个 MUSA 核心、1.8 GHz 主频计算：

$$
\text{FP32}_{\text{peak}} = 4096 \times 1.8\ \text{GHz} \times 2 = 14.7456\ \text{TFLOPS}
$$

公开资料通常简化为 14.4 TFLOPS。

显存带宽为：

$$
B_{\text{mem}} = W_{\text{bus}} \cdot f_{\text{mem}} \cdot 2
$$

其中 $W_{\text{bus}} = 256\ \text{bit}$，GDDR6 等效速率约 14 Gbps，可得带宽约 448 GB/s。

## 关键参数表

| 参数 | 数值 / 说明 |
|------|------------|
| GPU 架构 | MUSA（春晓 GPU） |
| 制造工艺 | 台积电 7 nm |
| MUSA 核心数 | 4096 |
| GPU 主频 | 1.8 GHz |
| 单精度浮点算力 | 14.4 TFLOPS |
| 显存类型 | GDDR6 |
| 显存容量 | 16 GB |
| 显存位宽 | 256 bit |
| 显存带宽 | 约 448 GB/s |
| 晶体管数量 | 220 亿 |
| PCIe 接口 | PCIe Gen5 x16 |
| 显示接口 | 3 × DisplayPort 1.4a + 1 × HDMI 2.1 |
| 最大输出分辨率 | 8K |
| 典型功耗 | 255 W |
| 供电接口 | 8 pin + 6 pin |
| 散热方式 | 双风扇 + 多热管 |
| 支持 API | DirectX、Vulkan、OpenGL、OpenGL ES |
| 发售时间 | 2022 年 11 月 |

## 应用场景

- 桌面游戏与 3D 图形渲染；
- 8K 视频编解码与多媒体内容创作；
- 计算机视觉、自然语言处理等 AI 模型的训练与推理；
- 国产化办公、设计工作站与云桌面 GPU；
- 物理仿真与科学计算入门应用。

## 供应链关系

`ent_product_moore_threads_s80` 由 `ent_company_moore_threads`（摩尔线程）设计，属于国产 GPU/显卡产品节点。其上游依赖台积电晶圆代工、三星 GDDR6 显存、PCB、供电元件、散热模组与封装测试；向下面向消费级显卡市场、国产整机厂商、云计算与边缘 AI 设备。摩尔线程通过持续迭代 Windows/Linux 驱动，逐步扩展 MTT S80 的游戏与 AI 生态。

## 来源与验证

- IT之家报道确认 MTT S80 搭载完整“春晓”芯片，4096 个 MUSA 核心、16 GB GDDR6、1.8 GHz 主频、14.4 TFLOPS 单精度算力，并支持 Windows DirectX 等图形接口。
- IT之家三测文章进一步说明其基于台积电 7 nm、256-bit 显存位宽、220 亿晶体管、PCIe 5.0 x16、三星 GDDR6 显存颗粒及 FP32/FP16/INT8 计算精度支持。
- IT之家驱动新闻列出了 MTT S80 与 S70 的核心参数对比。
- 功耗、供电与接口等参数来自公开评测与京东商品页摘录，未公开项未作臆测。