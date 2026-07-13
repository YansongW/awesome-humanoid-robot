---
id: ent_product_qualcomm_rb1_rb2
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 高通机器人 RB1/RB2 开发平台
  en: Qualcomm Robotics RB1/RB2 Development Platform
status: active
sources:
- id: src_qualcomm_rb1_rb2_dev
  type: website
  url: https://developer.qualcomm.com/hardware/qualcomm-robotics-rb1-rb2-kits
- id: src_codico_rb1_rb2
  type: website
  url: https://www.codico.com/en/current/news/new-rb1-and-rb2-robotics-devices-from-qualcomm
- id: src_96boards_rb1
  type: website
  url: https://www.96boards.org/product/qualcomm-robotics-rb1/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 高通机器人 RB1/RB2 开发平台

## 概述

Qualcomm Robotics RB1 与 RB2 是高通（Qualcomm）推出的入门级与中端机器人开发平台，分别基于 QRB2210 与 QRB4210 机器人专用 SoC，面向成本敏感、功耗受限的小型机器人与物联网设备。两款平台采用 pin-to-pin 兼容设计，支持 Linux 与 Robot Operating System 2（ROS 2），并提供丰富的摄像头、传感器与外设接口。RB1 主打清洁机器人、玩具与陪伴机器人等轻量级应用；RB2 则升级 CPU/GPU/DSP 性能并引入专用 AI 引擎，适用于服务机器人、无人机与割草机器人等对感知与算力要求更高的场景。

## 工作原理 / 技术架构

RB1/RB2 采用异构计算架构，将通用计算（CPU）、图形渲染（GPU）、数字信号处理（DSP）与 AI 加速（Qualcomm AI Engine）集成于单芯片，以低功耗完成机器人所需的感知、定位、导航与交互任务。平台内置双 ISP，可同时处理多达 3 路摄像头输入，支持视觉 SLAM、目标检测与避障算法。RB2  additionally 集成安全 DSP、安全 UI 与安全摄像头能力，满足设备认证与执行安全需求。

平台的软件栈基于 Yocto Linux，提供机器人中间件、ROS 2 支持、预集成驱动及示例应用，开发者可在 RB1 上完成原型验证后平滑迁移至 RB2 以获得更高性能。

## 关键参数表

| 参数 | RB1（QRB2210） | RB2（QRB4210） |
|---|---|---|
| CPU | 四核 Cortex-A53 @ $2.0\,\text{GHz}$ | 八核 Kryo 260（4×A73@$2.0\,\text{GHz}$ + 4×A53@$1.8\,\text{GHz}$） |
| GPU | Adreno 702 @ $845\,\text{MHz}$ | Adreno 610 @ $845\,\text{MHz}$ |
| DSP | Hexagon QDSP6 v66 | Hexagon 683（带 HVX） |
| AI 算力 | $0.5\,\text{TOPS}$ | $1.2\,\text{TOPS}$（实测约 $1.7\,\text{TOPS}$） |
| 内存 | $1\text{–}2\,\text{GB}$ LPDDR4X | 未公开 |
| 存储 | $8\text{–}16\,\text{GB}$ eMMC / microSD | $16\,\text{GB}$ eMMC / microSD / UFS 2.1 |
| 视频编解码 | $1080\text{p}@30$ | $1080\text{p}@60$ |
| ISP | 双 ISP，最多 3 路摄像头 | 三 ISP，最多 3 路摄像头 |
| 摄像头支持 | 最高 $13\,\text{MP}$ | 最高 $25\,\text{MP}$ |
| 显示 | MIPI-DSI，HD+ $1680\times720@60\,\text{fps}$ | MIPI-DSI，FHD+ $1080\times2520@60\,\text{fps}$ |
| 无线 | Wi-Fi 5（802.11ac）、蓝牙 5.0 | Wi-Fi 5（802.11ac）、蓝牙 5.0 |
| 有线接口 | USB 3.1 Type-C、千兆以太网、eMMC 5.1、SD 3.0 | USB 3.1 Type-C、千兆以太网、UFS 2.1、GPIO、UART、I2C/I3C |
| 安全特性 | 基础安全启动 | 安全 DSP、安全 UI、安全摄像头、TEE |
| 操作系统 | Linux / ROS 2 | Linux / ROS 2 |
| 典型应用 | 清洁机器人、玩具、陪伴机器人 | 服务机器人、无人机、割草机器人 |

## 应用场景

RB1/RB2 平台覆盖从消费级到轻工业级的多种机器人形态：

- **家用清洁机器人**：RB1 的低成本、低功耗方案适合扫地机器人，支持 VSLAM 与避障。
- **教育与陪伴机器人**：为语音交互、情感识别与移动底盘控制提供完整开发环境。
- **商用服务机器人**：RB2 的 AI 引擎可运行目标检测与人脸识别，支撑导览、配送机器人。
- **无人机与割草机器人**：RB2 的更高算力与 ISP 性能适用于视觉导航与室外环境感知。
- **ROS 2 原型开发**：pin-to-pin 兼容设计便于开发者从 RB1 快速升级至 RB2，缩短产品迭代周期。

## 供应链关系

在供应链中，高通作为 SoC 与开发平台提供商位于上游。QRB2210/QRB4210 芯片由高通设计并委托台积电等代工厂生产；中游为 Thundercomm（创通联达）、Lantronix 等模块与开发套件合作伙伴，负责核心板、载板与整机套件的制造与销售；下游面向 OEM、ODM、IoT 开发者与机器人初创公司。RB1/RB2 在 Qualcomm 机器人平台家族中定位低于 RB3/RB5/RB6，是高通拓展中低端机器人与边缘 AI 市场的重要产品组合。

## 来源与验证

- 高通官方开发者页面确认 RB1/RB2 的异构计算、802.11ac/蓝牙 5.0、$13\,\text{MP}$/$25\,\text{MP}$ 摄像头支持、$1080\text{p}$ 视频、ROS 2 支持及 pin-to-pin 兼容性。
- CODICO 新闻稿列出 RB1 的 QRB2210 四核 A53/Adreno 702/$0.5\,\text{TOPS}$ 与 RB2 的 QRB4210 八核 Kryo 260/Adreno 610/$1.2\,\text{TOPS}$ 等核心参数。
- 96Boards RB1 页面提供详细开发板规格，包括 CPU、GPU、RAM、存储、摄像头、显示、USB、网络、传感器及 96Boards 扩展接口。