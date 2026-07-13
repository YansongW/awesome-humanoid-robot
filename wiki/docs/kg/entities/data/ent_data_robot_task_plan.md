---
id: ent_data_robot_task_plan
schema_version: 1
type: data
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 机器人任务规划数据
  en: Robot Task Plan Data
status: active
sources:
- id: src_unidomain
  type: white_paper
  url: https://arxiv.org/abs/2507.21545
- id: src_tapa
  type: white_paper
  url: https://robot.sia.cn/article/doi/10.13973/j.cnki.robot.250193
- id: src_alfred
  type: website
  url: https://askforalfred.com/
- id: src_sharerobot
  type: website
  url: https://www.selectdataset.com/dataset/fbda5cdfa4a276a8f1e6eea3a773973f
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---




# 机器人任务规划数据

## 概述

机器人任务规划数据是用于描述机器人完成复杂任务所需动作序列、环境状态与约束条件的数据集合。其典型表示形式包括 PDDL（Planning Domain Definition Language）领域与问题文件、HTN（Hierarchical Task Network）层次任务网络、行为树（Behavior Tree）以及由大语言模型生成的自然语言/结构化计划。在知识图谱中，该数据实体由具身智能产品（如商汤 Ruyi）生成，并向下游机器人控制器或 VLA（Vision-Language-Action）模型提供高层任务指令。

## 数据结构与建模方法

机器人任务规划数据通常以“状态—动作—转移”三元组为核心。在 PDDL 形式化框架中，一个动作 $a$ 由前置条件（preconditions）与效果（effects）定义：

$$
\text{pre}(a) \subseteq s, \quad s' = (s \setminus \text{del}(a)) \cup \text{add}(a)
$$

其中 $s$ 为当前状态，$s'$ 为执行动作后的新状态。一个完整的任务规划问题由初始状态 $s_0$、目标状态 $g$ 与动作集合 $A$ 组成，规划器搜索动作序列 $\pi = (a_1, a_2, \ldots, a_n)$，使得：

$$
s_0 \xrightarrow{a_1} s_1 \xrightarrow{a_2} \cdots \xrightarrow{a_n} s_n, \quad g \subseteq s_n
$$

计划质量常用累计代价衡量：

$$
c(\pi) = \sum_{i=1}^{n} c(a_i)
$$

其中 $c(a_i)$ 为单个动作代价。现代具身任务规划数据还包含多模态信息，如视觉观测、自然语言指令、物体可供性（affordance）标注与末端执行器轨迹，用于训练与评测大模型驱动的规划器。

## 关键参数表

| 参数项 | 数值 / 说明 |
|--------|-------------|
| 数据类型 | 任务规划数据集 / 知识表示 |
| 常见表示形式 | PDDL、HTN、行为树、JSON/YAML 动作序列 |
| 动作粒度 | 原子技能（移动、抓取、放置、按压、旋转等） |
| 标注维度 | 指令文本、视觉场景、状态谓词、动作序列、轨迹、可供性 |
| 典型规划长度 | 数步至数十步（依任务复杂度） |
| 常用基准 | ALFRED、ShareRobot、RoboWaiter、UniDomain |
| 生成方式 | 人工编写、仿真器采样、LLM/VLM 生成、真实机器人演示 |
| 任务领域 | 家庭服务、工业装配、仓储物流、人形机器人操作 |
| 价格 | 公开基准多可免费获取；商业数据按授权计费 |

## 应用场景

- **家庭服务机器人**：根据自然语言指令生成可执行的清扫、递送、整理计划。
- **工业装配**：将复杂装配任务分解为抓取、插入、拧紧等原子动作序列。
- **仓储物流**：AMR 路径规划与拣选任务调度。
- **人形机器人操作**：结合视觉与语言的大模型生成长程任务计划，并映射到低层动作策略。

## 供应链关系

在公司—产品—零部件网络中，机器人任务规划数据属于**数据/知识资源层**：

- **上游**：大语言模型（LLM）、视觉-语言模型（VLM）、仿真环境（AI2-THOR、Habitat）、真实机器人演示、人工标注。
- **自身位置**：`ent_product_sensetime_ruyi -- generates --> ent_data_robot_task_plan`；该数据可被机器人任务规划器、VLA 模型与运动控制模块消费。
- **下游**：人形机器人整机、服务机器人、工业机器人、自动驾驶决策系统与具身智能评测基准。

## 来源与验证

- UniDomain 论文（arXiv）：https://arxiv.org/abs/2507.21545
- TaPA 论文（《机器人》期刊）：https://robot.sia.cn/article/doi/10.13973/j.cnki.robot.250193
- ALFRED Benchmark：https://askforalfred.com/
- ShareRobot 数据集整理：https://www.selectdataset.com/dataset/fbda5cdfa4a276a8f1e6eea3a773973f

PDDL 形式化方法、HTN 与行为树表示为机器人任务规划领域通用知识；具体数据规模与字段以各数据集官方发布为准。