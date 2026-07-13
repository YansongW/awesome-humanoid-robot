---
id: ent_component_5g_module
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 5G 通信模块
  en: 5G Module
status: active
sources:
- id: src_quectel_rm500q_gl
  type: website
  url: https://www.4gltemall.com/quectel-rm500q.html
- id: src_quectel_rm500q_gl2
  type: website
  url: https://satronel.com/products/wireless-modules/5g-modules-en/5g-quectel-modules-en/sub-6-ghz-m2-5g-rm500q-gl.html
- id: src_3gpp_5g
  type: website
  url: https://www.3gpp.org/specifications
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 5G 通信模块 / 5G Module

## 概述

5G 通信模块是集成 5G NR 调制解调器、射频前端与协议栈的蜂窝通信组件，支持 Sub-6 GHz 及部分 mmWave 频段，广泛应用于移动机器人、无人车、工业网关和云机器人。本词条以移远通信 RM500Q-GL 为例给出典型技术参数，该模块符合 3GPP Release 15/16，采用 M.2 形态。

## 工作原理 / 技术架构

模块内部集成基带处理器、射频收发器、功率放大器与多星座 GNSS 接收机，通过 USB 3.1 / PCIe / UART 与主机通信。主机通过 3GPP TS 27.007 标准 AT 指令及厂商增强指令控制模块，实现数据拨号、短信、定位与固件升级。5G NR 支持独立组网（SA）与非独立组网（NSA），并向下兼容 LTE-A 与 WCDMA。

## 关键参数表

| 规格项 | 数值（以 Quectel RM500Q-GL 为例） | 备注/来源 |
|--------|-----------------------------------|-----------|
| 标准 | 3GPP Release 15/16，5G NR Sub-6 GHz | Quectel / 3GPP |
| 形态 | M.2（30 × 52 × 2.3 mm） | Quectel |
| 工作电压 | 3.135–4.4 V，典型 3.7 V | Quectel |
| 5G SA 下行/上行 | 2.1 Gbps / 900 Mbps | Quectel |
| 5G NSA 下行/上行 | 2.5 Gbps / 650 Mbps | Quectel |
| 5G SA 频段 | n1/n2/n3/n5/n7/n8/n12/n20/n25/n28/n38/n40/n41/n48/n66/n71/n77/n78/n79 | Quectel |
| 5G NSA 频段 | n38/n40/n41/n77/n78/n79 等 | Quectel |
| MIMO | DL 4×4；UL 2×2（部分频段） | Quectel |
| 回退网络 | LTE-A Cat 16/18、WCDMA | Quectel |
| GNSS | GPS / GLONASS / BeiDou / Galileo | Quectel |
| 主机接口 | USB 3.1、PCIe、UART、GPIO | Quectel |
| 工作温度 | -30 °C ~ +75 °C | Quectel |

## 应用场景

- 移动机器人远程监控与遥操作
- 自动驾驶车辆 V2X/云端回传
- 工业网关与边缘计算设备
- 云机器人车队管理

## 供应链关系

5G 模块由移远通信、广和通、Sierra Wireless 等厂商供应，上游依赖 Qualcomm 等基带芯片、射频前端及 PCB。在机器人产业链中，5G 模块通常作为通信子系统集成于整机主控板，为上位机提供广域网连接能力。

## 来源与验证

- [Quectel RM500Q-GL 5G Sub-6 GHz Module Datasheet](https://www.4gltemall.com/quectel-rm500q.html)
- [Quectel RM500Q-GL Specifications (SATRON)](https://satronel.com/products/wireless-modules/5g-modules-en/5g-quectel-modules-en/sub-6-ghz-m2-5g-rm500q-gl.html)
- [3GPP Release 15/16 5G NR Specifications](https://www.3gpp.org/specifications)