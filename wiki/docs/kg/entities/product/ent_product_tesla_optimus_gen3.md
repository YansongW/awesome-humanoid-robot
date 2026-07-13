---
id: ent_product_tesla_optimus_gen3
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Tesla Optimus Gen 3 人形机器人
  en: Tesla Optimus Gen 3 Humanoid Robot
status: active
sources:
- id: src_tesla_official
  type: website
  url: https://www.tesla.com
- title: Tesla Official Website
- id: src_optimusk_2026_analysis
  type: article
  url: https://optimusk.blog/blog/tesla-optimus-humanoid-robot-latest-version-2026/
- title: Tesla Optimus Latest Version 2026
- id: src_wevolver_tesla_bot_specs
  type: article
  url: https://www.wevolver.com/specs/tesla-bot-aka-optimus
- title: Tesla Bot a.k.a Optimus Specifications
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# Tesla Optimus Gen 3 / Tesla Optimus Gen 3

## 概述

Tesla Optimus Gen 3 是特斯拉人形机器人平台的第三代演进形态。公开报道中存在命名区分：“Gen 3”通常指在 Gen 2 本体上升级的 22 自由度灵巧手方案；而面向量产的全新机体被称为“Optimus V3”。截至 2026 年中，Optimus 主要在特斯拉弗里蒙特、奥斯汀等工厂内部进行测试与任务学习，尚未向公众开放销售。该平台强调 22 自由度灵巧手、定制 AI5 计算芯片以及大规模制造能力。

## 工作原理 / 技术架构

Optimus 采用与特斯拉自动驾驶相似的纯视觉感知与端到端神经网络架构：

1. **感知层**：头部集成多颗 Autopilot 摄像头，通过 Occupancy Network 与 BEV（Bird’s Eye View）表征构建环境模型。
2. **决策与运动控制**：基于模仿学习与强化学习训练全身运动与操作策略，结合低层级全身控制（WBC）实现平衡与操作。
3. **灵巧操作**：每只手配备 22 自由度与约 25 个执行器（双手共 50 个执行器），通过高带宽力/位控制完成抓取与工具使用。
4. **计算平台**：搭载特斯拉自研 AI5 芯片，内存带宽约为前代 AI4 的 5 倍，用于本地大模型推理。

人形机器人运动学可写作关节空间到任务空间的映射

$$
\mathbf{x}=f(\mathbf{q}),\quad \mathbf{q}\in\mathbb{R}^n,
$$

其中 $n$ 为全身关节自由度。对于 Optimus V3，公开报道指出全身关节数约为 37。手部独立自由度为

$$
DoF_{\text{hand}}=22\ \text{（单侧）},
\quad DoF_{\text{hands}}=44.
$$

## 关键参数表

| 参数 | 数值 / 说明 |
|---|---|
| 平台命名 | Gen 3（灵巧手升级）/ V3（全新量产机体） |
| 身高 | 173 cm |
| 体重 | 约 57 kg（V3 待最终确认） |
| 全身关节 | 约 37（V3 报道） |
| 手部自由度 | 22 DoF / 手 |
| 手部执行器 | 约 50 个（双手合计） |
| 行走速度 | 约 1.2 m/s（V3 报道） |
| 负载能力 | 约 20 kg |
| 主控芯片 | Tesla AI5 |
| 价格目标 | 长期 20,000–30,000 USD |
| 销售状态 | 仅内部工厂使用，未公开销售 |

## 应用场景

- **汽车制造**：电池模组搬运、零件分拣、装配线辅助。
- **工厂物流**：在受控环境中执行重复性搬运与上下料。
- **数据采集**：在特斯拉产线中积累真实任务数据，反哺机器人大模型训练。
- **未来消费级**：家庭服务、养老辅助等长期目标场景。

## 供应链关系

- **上游**：特斯拉自研 AI5 芯片、执行器、电池与结构件；外部供应半导体晶圆、稀土磁材、传感器、线缆与结构材料。
- **同层**：Optimus 与特斯拉汽车业务共享视觉算法、FSD 数据闭环与制造能力。
- **下游**：首先服务于特斯拉自有工厂，未来计划向 B2B 工业客户及消费级市场扩展。

## 来源与验证

- 特斯拉官网：https://www.tesla.com
- Optimusk 2026 年分析报道：https://optimusk.blog/blog/tesla-optimus-humanoid-robot-latest-version-2026/
- Wevolver Tesla Bot 规格页：https://www.wevolver.com/specs/tesla-bot-aka-optimus

部分关于 V3 机体的参数（如最终重量、关节数、速度）来自第三方分析，官方尚未在 2026 年夏季发布会前完全确认。