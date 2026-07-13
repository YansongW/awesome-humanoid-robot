---
id: ent_product_horizon_journey5
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 地平线 Journey 5 智能驾驶芯片
  en: Horizon Robotics Journey 5 Autonomous Driving Chip
status: active
sources:
- id: src_horizon_journey_official
  type: website
  url: https://www.horizon.auto/en/solutions/horizon-journey
- id: src_techinsights_j5
  type: website
  url: https://www.techinsights.com/blog/desay-horizon-robotics-journey-5-adas-controller-deep-dive-teardown
- id: src_cnevpost_j5
  type: website
  url: https://cnevpost.com/2021/07/30/horizon-robotics-launches-journey-5-chip-with-128-tops-of-ai-computing-power/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 地平线 Journey 5 智能驾驶芯片

## 概述

地平线 Journey 5（中文名：征程 5）是北京地平线机器人技术研发有限公司推出的第三代车规级 AI 系统级芯片（SoC），面向高级辅助驾驶（ADAS）与自动驾驶域控制器。该芯片采用台积电 7 nm 工艺制造，单芯片 AI 算力可达 $128\,\text{TOPS}$，支持多达 16 路高清摄像头输入及毫米波雷达、激光雷达、超声波雷达等多传感器融合。Journey 5 已通过 AEC-Q100 Grade 2 车规可靠性认证，并满足 ISO 26262 ASIL-B 功能安全等级，系统级应用可满足 ASIL-D 要求。

## 工作原理 / 技术架构

Journey 5 集成地平线自研的 BPU（Brain Processing Unit）贝叶斯架构双核 AI 加速器、8 核 ARM Cortex-A55 CPU、2 核 ISP、计算机视觉引擎、2 核 DSP 以及视频编解码单元。BPU 针对卷积神经网络与 Transformer 结构进行优化，能够以较低功耗完成感知、预测、规划等智能驾驶核心算法。其系统架构可概括为：

$$
\text{传感器数据} \xrightarrow{\text{ISP/CV}} \text{感知特征} \xrightarrow{\text{BPU}} \text{目标检测/分割/预测} \xrightarrow{\text{CPU/DSP}} \text{规划与控制指令}.
$$

在算力利用率方面，Journey 5 强调以 FPS/Watt（每瓦帧率）和 MAPS（Mean Average Precision and Speed）衡量实际推理性能，而非单纯的 TOPS 峰值。其安全岛设计、硬件加密引擎（支持 FIPS 140-3 与 ISO 21434）以及完整的 ASIL-B 认证，使其适用于前装量产车辆。

## 关键参数表

| 参数 | 规格 |
|---|---|
| 芯片型号 | Horizon Journey 5 / 征程 5 |
| 制程工艺 | 7 nm |
| AI 算力 | $128\,\text{TOPS}$ |
| CPU | 8 核 ARM Cortex-A55 |
| AI 加速器 | 双核 BPU（Bayes 架构） |
| ISP | 2 核 |
| DSP | 2 核 |
| 摄像头接口 | 4×4 MIPI，最多 16 路高清摄像头 |
| 以太网 | 2× Gigabit Ethernet |
| CAN | 4× CAN-FD |
| PCIe | 2× PCIe 3.0 |
| 功能安全 | ISO 26262 ASIL-B Ready；系统级可满足 ASIL-D |
| 车规认证 | AEC-Q100 Grade 2 |
| 信息安全 | 支持 FIPS 140-3、ISO 21434 |
| 典型应用 | 高速/城市 NOA、多传感器融合感知、泊车 |

## 应用场景

Journey 5 的主要应用集中在智能汽车领域，但其高算力、低功耗与多传感器融合能力也使其向机器人感知计算延伸：

- **城市与高速领航辅助驾驶（NOA）**：在理想汽车 L 系列 Pro/Air 车型等量产车上实现导航辅助驾驶。
- **多传感器融合域控**：将摄像头、雷达、激光雷达数据在单芯片或级联方案中融合，支持 L2+ 至 L4 算法验证。
- **机器人感知主控**：部分人形机器人与自动驾驶移动平台采用 Journey 5 作为视觉感知与 AI 推理主控。
- **数据闭环与影子模式**：通过车载大算力芯片运行多任务模型，为云端数据挖掘提供触发信号。

## 供应链关系

在供应链中，地平线机器人属于无晶圆厂（Fabless）芯片设计公司，Journey 5 由台积电（TSMC）7 nm 工艺代工，封装与测试由 OSAT 完成。芯片经由 Tier 1 供应商（如德赛西威等）设计成域控制器后，供应给整车厂（如理想、比亚迪、长安等）。在机器人产业链中，地平线也直接向机器人本体厂商与算法公司提供 Journey 5 模组及开发工具链，成为“芯片—域控—整车/机器人”链条中的核心 AI 计算平台供应商。

## 来源与验证

- 地平线官网 Journey 平台页确认 Journey 5 的 $128\,\text{TOPS}$ 算力、BPU Bayes、16 路摄像头支持、ASIL-B(D) 及 AEC-Q100 Grade 2 认证。
- TechInsights 拆解报告（Li Auto L7 Pro 的 Journey 5 域控制器）确认该芯片为 7 nm SoC、集成 CPU/GPU/AI 加速器、支持 16 路摄像头输入。
- CNEVPOST 报道详细列出 Journey 5 的 8 核 Cortex-A55、双核 BPU、2 ISP、2 DSP、安全岛、加密引擎、MIPI/CAN-FD/Ethernet/PCIe 接口及量产时间线。