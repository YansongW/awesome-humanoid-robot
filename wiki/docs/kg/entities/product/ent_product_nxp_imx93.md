---
id: ent_product_nxp_imx93
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: NXP i.MX 93
  en: NXP i.MX 93
status: active
sources:
- id: src_nxp_imx93_datasheet
  type: report
  url: https://www.nxp.com/docs/en/data-sheet/IMX93IEC.pdf
- title: i.MX 93 Applications Processors Data Sheet for Industrial Products - NXP
- id: src_nxp_imx93_variscite
  type: website
  url: https://variscite.com/system-on-module-som/i-mx-9/i-mx-93/var-som-mx93/
- title: VAR-SOM-MX93 - NXP i.MX 93 ARM System on Module - Variscite
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# NXP i.MX 93 / NXP i.MX 93

## 概述

NXP i.MX 93 是恩智浦半导体推出的面向工业、物联网边缘、汽车与智能家居应用的异构应用处理器。该芯片集成双核 Arm Cortex-A55、实时 Cortex-M33 协处理器以及可选的 Arm Ethos-U65 microNPU，主打高能效边缘 AI 与功能安全，适用于机器人控制器、工业网关、ADAS 边缘节点等场景。

## 工作原理 / 技术架构

i.MX 93 采用 NXP Energy Flex 架构，通过电源域划分实现高性能与低功耗模式的灵活切换。Cortex-A55 负责运行 Linux/Android 等复杂操作系统与 AI 推理，Cortex-M33 负责实时控制与低功耗待机。Ethos-U65 microNPU 提供约 0.5 TOPS 的 INT8 推理算力，256 MACs @ 1 GHz，2 OPS/MAC。

峰值算力可估算为：

$$
\text{TOPS} = \frac{256 \times 1\,\text{GHz} \times 2}{10^{12}} = 0.512\,\text{TOPS}
$$

芯片支持双千兆以太网（其一支持 TSN）、CAN-FD、MIPI-CSI/DSI、USB 2.0 等工业与机器人常用接口。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 应用处理器 | 双核 Arm Cortex-A55 @ 1.7 GHz |
| 实时协处理器 | Arm Cortex-M33 @ 250 MHz |
| AI 加速器 | Arm Ethos-U65 microNPU，约 0.5 TOPS |
| L1 缓存 | 32 KB I-cache + 32 KB D-cache / 核 |
| L2 缓存 | 64 KB / 核 |
| L3 缓存 | 256 KB 集群共享 |
| Cortex-M33 TCM | 256 KB |
| 内存接口 | LPDDR4/LPDDR4X，最高 3.7 GT/s ×16，支持内联 ECC |
| 存储接口 | 3× SD/SDIO/eMMC 5.1，1× Octal SPI |
| 显示 | MIPI-DSI 1080p60，LVDS 720p60，并行 RGB |
| 摄像头 | MIPI-CSI 1080p60，8-bit 并行 |
| 网络 | 2× GbE（1× TSN），CAN-FD×2 |
| USB | USB 2.0 ×2（OTG） |
| 串行接口 | UART×8，I2C×8，SPI×8，I3C×2 |
| 安全 | EdgeLock Secure Enclave |
| 工艺 | 16/12 nm FinFET 级 |
| 温度范围 | 消费级 0°C–95°C；工业级 -40°C–105°C；扩展工业级 -40°C–125°C |

## 应用场景

- 机器人边缘控制器与运动控制网关
- 工业自动化 HMI 与 PLC 替代方案
- 车载信息娱乐与 ADAS 边缘处理
- 智能安防摄像头与 AIoT 网关

## 供应链关系

NXP 为上游芯片设计商，i.MX 93 由三星等晶圆代工厂制造，封装测试后通过代理商与模组厂商（如 Variscite、AAEON）进入中游整机与控制器厂商。在机器人产业链中，i.MX 93 通常作为“小脑”或边缘 AI 计算节点，与更高性能 GPU/NPU（如 NVIDIA Jetson）形成互补。

## 来源与验证

参数主要来源于 NXP 官方数据手册 IMX93IEC（https://www.nxp.com/docs/en/data-sheet/IMX93IEC.pdf）及 Variscite 模组规格页（https://variscite.com/system-on-module-som/i-mx-9/i-mx-93/var-som-mx93/）。NPU 算力为基于 256 MACs @ 1 GHz 的理论估算值。