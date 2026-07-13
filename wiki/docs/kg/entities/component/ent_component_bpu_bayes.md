---
id: ent_component_bpu_bayes
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 地平线贝叶斯（Bayes）BPU 架构
  en: Horizon Robotics Bayes BPU Architecture
status: active
sources:
- id: src_horizon_journey
  type: website
  url: https://www.horizon.auto/solutions/horizon-journey
- id: src_horizon_bayes_press
  type: website
  url: https://www.horizon.auto/news/press/224
- id: src_36kr_journey5
  type: website
  url: https://m.36kr.com/p/1332547894974466
- id: src_42how_journey5
  type: website
  url: https://www.42how.com/article/7018
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 地平线贝叶斯（Bayes）BPU 架构

## 概述

贝叶斯（Bayes）是地平线（Horizon Robotics）自研的第三代 BPU（Brain Processing Unit）智能计算架构，主要搭载于征程 5（Journey 5）车规级 AI 芯片。该架构面向高等级智能驾驶与机器人边缘计算，针对 BEV（Bird's Eye View）、Transformer、LSTM 等先进神经网络进行原生优化，强调小 batch 低延迟、高计算资源利用率与高能效比。

## 工作原理 / 技术架构

BPU 是地平线专为深度学习推理设计的 ASIC 加速器。Bayes 架构采用异构近存计算、高并发数据桥与脉动张量计算核，通过软硬件协同实现高效推理。

其“真实 AI 效能”可概括为：

$$
\text{真实 AI 效能} = \text{理论峰值算力} \times \text{计算资源有效利用率} \times \text{AI 算法效率}
$$

在征程 5 中，Bayes BPU 与双 Vision P6 DSP、双 ISP、8 核 ARM Cortex-A55 及安全岛共同构成异构 SoC。芯片支持 16 路高清摄像头输入，典型算力配置为：

$$
128 \ \text{TOPS} \ \text{@} \ 30 \ \text{W}
$$

对应能效比约为 $4.27 \ \text{TOPS/W}$。在典型目标检测模型上，征程 5 可实现超过 1200 FPS 的推理帧率，端到端延迟约 60 ms。

## 关键参数表

| 参数项 | 数值 / 说明 |
|--------|-------------|
| 架构名称 | BPU® Bayes（贝叶斯） |
| 所属公司 | 地平线（Horizon Robotics） |
| 架构代数 | 第三代 BPU（BPU 3.0） |
| 代表芯片 | 征程 5 / Journey 5 |
| 理论 AI 算力 | 128 TOPS（搭载于征程 5） |
| 典型功耗 | 约 30 W（征程 5 整机） |
| 能效比 | 约 4.27 TOPS/W |
| CPU | 8 核 ARM Cortex-A55 |
| DSP | 双 Vision P6 DSP（0.67 TOPS） |
| ISP | 双 ISP，支持 4K@30fps HDR |
| 摄像头接口 | 16 路车载高清摄像头（4×4 MIPI） |
| 功能安全 | ASIL-B(D) 计算，ASIL-D MCU |
| 车规认证 | AEC-Q100 Grade 2 |
| 制程（BPU 单独） | 未公开 |

## 应用场景

- **高阶智能驾驶**：高速 NOA、城区领航辅助、BEV+Transformer 感知融合。
- **机器人边缘大脑**：服务机器人、物流 AGV、人形机器人视觉感知与决策。
- **多传感器融合**：摄像头、毫米波雷达与激光雷达数据的前融合处理。
- **预测与规划**：基于概率推断对道路参与者轨迹进行预测，支撑博弈决策。

## 供应链关系

在公司—产品—零部件网络中，Bayes BPU 属于**AI 计算架构/半导体 IP 层**：

- **上游**：EDA 工具、半导体 IP、晶圆代工、封装测试。
- **自身位置**：`ent_component_bpu_bayes` 作为地平线征程 5 芯片的核心 AI 加速单元；图谱关系 `ent_product_horizon_journey5 -- uses --> ent_component_bpu_bayes`。
- **下游**：征程 5 芯片、域控制器、汽车 OEM、机器人整机厂及 Tier 1 供应商。

## 来源与验证

- 地平线征程系列产品页：https://www.horizon.auto/solutions/horizon-journey
- 地平线 BPU 架构新闻稿：https://www.horizon.auto/news/press/224
- 36氪 征程 5 报道：https://m.36kr.com/p/1332547894974466
- 42HOW 征程 5 深度解析：https://www.42how.com/article/7018

128 TOPS、30 W、16 路摄像头与 AEC-Q100 Grade 2 等参数来自地平线官方产品页及公开报道；Bayes BPU 单独制程信息未公开。