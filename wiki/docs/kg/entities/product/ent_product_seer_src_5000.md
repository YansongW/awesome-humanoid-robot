---
id: ent_product_seer_src_5000
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 仙工 SRC-5000 一体化具身智能控制器
  en: SEER SRC-5000 Embodied Intelligence Controller
status: active
sources:
- id: src_seer_src5000_official
  type: website
  url: https://seer-robotics.ai/zh/media/196
- title: 展会直击丨2024 工博会，仙工智能全新控制器引领向上时刻
- id: src_seer_src5000_wrc
  type: website
  url: https://www.worldrobotconference.com/expo/product/122.html
- title: 一体化具身智能控制器 SRC-5000 - 2026 世界机器人大会
- id: src_seer_src5000_media
  type: website
  url: https://xueqiu.com/1298751485/310117265
- title: “抢滩”具身智能，仙工智能手握哪些底牌？ - 雪球
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 仙工 SRC-5000 一体化具身智能控制器 / SEER SRC-5000 Embodied Intelligence Controller

## 概述

SRC-5000 是上海仙工智能科技股份有限公司推出的全球首款一体化具身智能控制器，面向轮式人形机器人、高阶复合机器人及四足机器人等具身智能形态。该控制器将传统移动机器人控制、机械臂操作、视觉感知与 AI 决策集成于单一硬件平台，解决“手-眼-脚”协同控制难题，构建“大脑 + 小脑”一体化的感知决策体系。

## 工作原理 / 技术架构

SRC-5000 采用多处理器异构架构，搭载 NVIDIA 边缘 AI 计算单元，并运行实时操作系统与时间敏感网络（TSN）。其控制同步周期为 \(250\,\mu\text{s}\)，对应控制频率

\[
f = \frac{1}{250\times 10^{-6}\,\text{s}} = 4000\,\text{Hz}
\]

时钟抖动低于 \(30\,\mu\text{s}\)，可满足多关节、多传感器的高精度同步需求。控制器支持 EtherCAT 主站通信、高速网口及 GMSL 摄像头接口，并内嵌 2D/3D、VSLAM 与激光 SLAM 混合导航算法，实现多模态感知融合与动态避障。

AI 算力方面，公开报道存在两个量纲：基础配置为 \(20\!\sim\!40\,\text{TOPS}\)，面向高算力需求的应用场景可扩展至 \(156\,\text{TOPS}\)。算力与推理帧率的关系可表示为

\[
\text{FPS} \approx \frac{\text{TOPS} \times 10^{12}}{2 \times \text{OPs}_{\text{model}}}
\]

其中 \(\text{OPs}_{\text{model}}\) 为单次推理所需运算量。SRC-5000 还提供 SDK、API 与 3D 建图工具链，支持业务层 APP 开发与持续学习优化。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 控制架构 | 多处理器异构 + 实时操作系统 |
| AI 算力 | \(20\!\sim\!40\,\text{TOPS}\)（基础）/ 最高 \(156\,\text{TOPS}\) |
| 控制同步周期 | \(250\,\mu\text{s}\) |
| 控制频率 | 4000 Hz |
| 时钟抖动 | \(<30\,\mu\text{s}\) |
| 通信接口 | 高速网口、EtherCAT、GMSL 摄像头接口 |
| 导航方式 | 2D/3D、VSLAM、激光 SLAM、混合导航 |
| 支持自由度 | 40+ |
| 开发支持 | SDK、API、3D 建图工具链 |
| 功耗 / 供电 | 未公开 |

## 应用场景

- 轮式人形机器人全身控制
- 高阶复合机器人的移动 + 操作协同
- 工业 AGV/AMR 的高精度导航与避障
- 半导体、3C、汽车等精密制造场景
- 多机器人协同调度与智能物流

## 供应链关系

SRC-5000 是仙工智能控制技术体系中的旗舰产品。上游包括 NVIDIA 计算模组、网络交换芯片、工业级接口芯片与摄像头模组；中游为仙工自研的实时系统、分布式机器人软件与导航算法；下游面向机器人整机制造商与系统集成商。仙工智能同时提供 SRC-880、SRC-2000、SRC-3000FS 等控制器系列及一站式造车解决方案。

## 来源与验证

参数主要来自仙工智能官方报道及世界机器人大会展商产品页。具体功耗、供电规格、CPU 型号等未在公开资料中披露，标注为“未公开”。