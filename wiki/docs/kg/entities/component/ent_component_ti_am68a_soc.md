---
id: ent_component_ti_am68a_soc
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 德州仪器 AM68A 视觉 SoC
  en: Texas Instruments AM68A Vision SoC
status: active
sources:
- id: src_ti_am68a_datasheet
  type: document
- title: AM68A Datasheet
  url: https://www.alldatasheet.com/datasheet-pdf/pdf/1558494/TI/AM68A.html
- id: src_ti_am68a_digikey
  type: website
- title: Texas Instruments AM68 Dual-Core Arm Cortex-A72 MCU - DigiKey
  url: https://www.digikey.com/en/product-highlight/t/texas-instruments/am68-dual-core-arm-cortex-a72-mcu
- id: src_ti_am68a_mouser
  type: website
- title: AM68x 64-Bit Jacinto 8 TOPS Vision SoC Processor - Mouser
  url: https://www.mouser.es/new/texas-instruments/ti-am68a-vision-socs/
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications compiled from TI datasheet, distributor pages and public
    product briefs; exact power figures depend on workload and thermal configuration.
---


# 德州仪器 AM68A 视觉 SoC / Texas Instruments AM68A Vision SoC

## 概述

AM68A 是德州仪器（Texas Instruments）基于 Jacinto 7 架构推出的 64 位视觉 SoC，面向机器视觉相机、智能零售、自主移动机器人（AMR）、无人机、工业 HMI 与边缘 AI 设备。它在单芯片内集成双核 Cortex-A72 应用处理器、四核 Cortex-R5F 实时 MCU、C7x DSP、MMA 深度学习加速器、第七代 ISP、视频编解码器与丰富的工业接口，强调算力、功耗与功能安全的平衡。

## 工作原理 / 技术架构

AM68A 采用异构多核架构，将通用计算、实时控制、AI 推理与视觉预处理分配到不同处理单元：

- **应用处理器**：双核 64-bit Arm Cortex-A72 @ 最高 2 GHz，每核配置 32 KB L1 D-Cache、48 KB L1 I-Cache，双核共享 1 MB L2 Cache，运行 Linux/Android 等操作系统。
- **实时 MCU**：最多四核 Arm Cortex-R5F @ 最高 1 GHz，分为 General Compute 与 Device Management 两个域，支持功能安全与确定性控制。
- **AI 加速器**：C7x DSP 配合 Matrix Multiply Accelerator（MMA），INT8 峰值算力最高 8 TOPS；支持深度学习与传统 CV 算法混合部署。
- **视觉预处理**：第七代 ISP 支持 480 MPixel/s、16-bit RAW 输入、WDR、镜头畸变校正（LDC）与多尺度输出。
- **多媒体**：IMG BXS-64-4 GPU 最高 800 MHz；视频编解码支持 4K60 H.264/H.265 编解码。
- **内存与接口**：最高 4 MB on-chip L3 RAM（带 ECC），双 32-bit LPDDR4 接口（最高 4266 MT/s）；提供 PCIe Gen3、USB 3.0、双千兆以太网、MIPI CSI/DSI、CAN-FD 等接口。

AI 峰值算力 8 TOPS 的估算基于 MMA 在标称频率与 INT8 精度下的 MAC 吞吐：

\[
\text{TOPS} = \text{MAC}_{\text{peak}} \times 2 \times f \times \text{utilization}
\]

实际有效算力受内存带宽、模型结构与量化精度影响。

## 关键参数

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制程 | 16 nm FinFET | TI datasheet |
| CPU | 2× Arm Cortex-A72 @ 2 GHz | TI datasheet / DigiKey |
| 实时 MCU | 4× Arm Cortex-R5F @ 1 GHz | TI datasheet |
| AI 加速器 | C7x DSP + MMA | TI datasheet |
| AI 算力 | 最高 8 TOPS @ INT8 | TI datasheet |
| GPU | IMG BXS-64-4 @ 800 MHz；约 50 GFLOPS | TI datasheet |
| ISP | 第七代 ISP，480 MPixel/s | TI datasheet |
| 视频编解码 | 4K@60 fps H.264/H.265 编码/解码 | TI datasheet |
| 显示输出 | 最多 4 路显示：2× DSI 4L、1× eDP 4L、1× DPI/OLDI-LVDS | TI datasheet |
| 相机接口 | 2× MIPI CSI2 4L RX + 1× CSI2 4L TX（D-PHY，最高 1.5 Gbps/lane） | TI datasheet |
| 内存 | 4 MB on-chip L3 RAM（ECC）；双 32-bit LPDDR4，最高 4266 MT/s | TI datasheet |
| 高速接口 | 1× PCIe Gen3（最多 4 lanes）、1× USB 3.0 DRD、2× GbE、2× CSI2 | TI datasheet |
| 其他接口 | CAN-FD、UART、I2C、SPI、GPIO、GPMC、eMMC 5.1、SD3.0 | TI datasheet |
| 安全 | 安全启动、硬件安全模块、加密加速器、SIL-2 目标 | TI datasheet |
| 封装 | 23 mm × 23 mm，0.8 mm pitch，770-pin FCBGA（ALZ） | TI datasheet |
| 典型功耗 | 约 5–15 W（依配置） | 公开资料 |
| 价格 | 未公开 | — |

## 应用场景

- **机器视觉相机与工业 AMR**：ISP + MMA 实现实时目标检测、缺陷检测与导航避障。
- **自主移动机器人**：多传感器融合、SLAM 与路径规划，支持功能安全认证。
- **智能零售与视频监控**：4K 视频分析与边缘 AI 推理。
- **工业 HMI 与单板计算机**：多显示输出与丰富接口支持复杂人机交互。

## 供应链关系

AM68A 由 **Texas Instruments（实体 `ent_company_texas_instruments`）** 设计。上游依赖台积电/自有晶圆厂、ARM IP、自研 C7x DSP/MMA、LPDDR 存储、PMIC 与封测；下游客户包括汽车 Tier1/OEM、工业自动化厂商、机器人公司、机器视觉集成商与医疗设备厂商。在知识图谱中，该 SoC 实体通过 `manufactures` 关系与公司节点 `ent_company_texas_instruments` 相连，可作为机器人主控或视觉处理核心嵌入到整机产品节点中。

## 来源与验证

- AM68A Datasheet（https://www.alldatasheet.com/datasheet-pdf/pdf/1558494/TI/AM68A.html）
- DigiKey AM68 产品亮点（https://www.digikey.com/en/product-highlight/t/texas-instruments/am68-dual-core-arm-cortex-a72-mcu）
- Mouser AM68x 产品页（https://www.mouser.es/new/texas-instruments/ti-am68a-vision-socs/）

单价与部分功耗细节在公开渠道未完整披露，已标注为“未公开”。