---
id: ent_component_nxp_imx93_soc
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
status: active
names:
  zh: NXP i.MX 93 应用处理器 SoC
  en: NXP i.MX 93 Applications Processor SoC
sources:
- id: src_nxp_imx93_overview
  type: website
- title: NXP i.MX 93 Applications Processors
  url: https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-9-applications-processors/i-mx-93-applications-processors:IMX93
- id: src_aaeon_ucom_imx93
  type: datasheet
- title: AAEON uCOM-IMX93 SMARC Module Datasheet
  url: https://www.aaeon.com/en/product/detail/com_express_cpu_modules_ucom-imx93/order_info
- id: src_phytec_imx93
  type: datasheet
- title: phyCORE-i.MX 93 System on Module
  url: https://www.phytec.cn/produkte/system-on-modules/phycore-imx-91-93
verification:
  reviewed_by: ai_autonomous
  reviewed_at: '2026-07-13'
  review_notes: Specifications from NXP public materials and partner module datasheets;
    exact SKUs may vary.
---


# NXP i.MX 93 应用处理器 SoC / NXP i.MX 93 Applications Processor SoC

## 概述

NXP i.MX 93 是恩智浦 i.MX 9 系列面向边缘 AI 与工业物联网的应用处理器，采用异构多核架构：双核 Arm Cortex-A55 负责高性能计算与 Linux/Android 系统运行，Cortex-M33 实时内核处理低延迟控制与唤醒，Arm Ethos-U65 microNPU 提供轻量 AI 加速。i.MX 93 集成 EdgeLock 安全飞地、双 ISP、TSN 千兆以太网与丰富工业接口，适用于机器人主控、工业网关、HMI 与智能相机等场景。

## 工作原理 / 技术架构

i.MX 93 的异构计算架构通过功能分区实现能效与实时性的平衡：

- **Cortex-A55 集群**：2× 64 位 Cortex-A55 @ 最高 1.7 GHz，配备 32 kB L1 I/D 缓存、64 kB L2/核及 256 kB L3 共享缓存，运行 Linux/Yocto/Ubuntu，负责视觉处理、SLAM、网络通信与上层算法。
- **Cortex-M33 实时核**：@ 最高 250 MHz，运行 FreeRTOS/QNX/Zephyr，用于电机控制、传感器融合、低功耗唤醒与 CAN-FD 实时通信。
- **Arm Ethos-U65 microNPU**：最高 0.5 TOPS INT8，用于轻量神经网络推理，如语音唤醒、姿态检测与缺陷分类。
- **Energy Flex 架构**：支持独立开关各计算域，降低待机功耗。

AI 推理峰值吞吐可近似表示为：
$$T_{NPU} = 0.5\ \text{TOPS INT8}$$
实际有效吞吐受模型结构、内存带宽与量化策略影响。

## 关键参数表

| 参数 | 数值 | 备注/来源 |
|------|------|-----------|
| 制程 | 16/12 nm FinFET 级 | NXP 公开资料 |
| CPU | 2× Arm Cortex-A55 @ 1.7 GHz + 1× Cortex-M33 @ 250 MHz | NXP / AAEON / Phytec |
| NPU | Arm Ethos-U65，最高 0.5 TOPS | NXP / AAEON |
| L1 缓存（A55） | 32 kB I / 32 kB D | Phytec |
| L2 缓存（A55） | 64 kB/核 | Phytec |
| L3 缓存 | 256 kB 集群 | Phytec |
| 内部 SRAM | 640 kB | Phytec |
| GPU | 未集成独立 GPU | NXP 公开资料 |
| ISP | 双 ISP，最高 12 MP，支持 HDR、鱼眼矫正 | NXP 公开资料 |
| 视频解码 | H.264/H.265/VP9 等 | NXP 公开资料 |
| 内存 | LPDDR4/LPDDR4X，常见 1–2 GB（模块），最高支持未公开 | 模块资料 |
| 存储 | eMMC、SD、SPI-NOR | 模块资料 |
| 以太网 | 2× GbE，含 TSN | AAEON / Phytec |
| USB | USB 2.0 Host/OTG、USB 3.0 | AAEON / NXP |
| 工业接口 | CAN-FD、UART、SPI、I2C、I3C、GPIO、PWM | NXP 公开资料 |
| 显示 | MIPI DSI、LVDS、HDMI（依 SKU） | 模块资料 |
| 摄像头 | MIPI CSI-2 | NXP 公开资料 |
| 安全 | EdgeLock 安全飞地、TrustZone、安全启动 | NXP 公开资料 |
| 温度范围 | 工业级 -40 °C – +85 °C（模块） | AAEON / Phytec |
| 供货周期 | 15 年 | NXP 公开资料 |

## 应用场景

- **机器人主控**：AMR/人形机器人导航、SLAM、多传感器融合与通信网关。
- **工业 HMI 与网关**：双屏显示、TSN 实时以太网、设备互联。
- **智能相机**：双 ISP + NPU 实现本地缺陷检测与 OCR。
- **智能家居/楼宇**：语音唤醒、安防监控与能耗管理。

## 供应链关系

- **制造商**：NXP Semiconductors（ent_company_nxp），荷兰嵌入式半导体供应商。
- **上游关键物料**：台积电/格芯代工、ARM IP、LPDDR4、eMMC、PMIC、封测。
- **下游整机集成**：机器人整机厂、工业自动化厂商、汽车 OEM/Tier1、AIoT 设备商。
- **竞争/对标**：Texas Instruments Jacinto、Renesas RZ/V、NVIDIA Jetson Nano、Rockchip RK3588、MediaTek Genio 700。

## 来源与验证

- NXP i.MX 93 产品页：https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-9-applications-processors/i-mx-93-applications-processors:IMX93
- AAEON uCOM-IMX93 模块规格：https://www.aaeon.com/en/product/detail/com_express_cpu_modules_ucom-imx93/order_info
- Phytec phyCORE-i.MX 93 模块规格：https://www.phytec.cn/produkte/system-on-modules/phycore-imx-91-93