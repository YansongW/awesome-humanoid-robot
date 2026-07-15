---
$id: ent_formalism_thevenin_equivalent_circuit
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: formalism
names:
  en: Thevenin Equivalent Circuit
  zh: Thevenin 等效电路
  ko: 테베닌 등가 회로
summary:
  en: A formalism that replaces any linear electrical network, viewed from two terminals, by an equivalent ideal voltage source
    in series with an equivalent resistance.
  zh: 一种形式化方法，将任意线性电网络从两个端子看进去替换为一个等效理想电压源串联一个等效电阻。
  ko: 두 단자에서 바라본 임의의 선형 전기 네트워크를 등가 이상 전압원과 등가 저항의 직렬 연결로 대체하는 형식화이다.
domains:
- 00_foundations
- 06_design_engineering
layers:
- foundations
- midstream
functional_roles:
- knowledge
tags:
- thevenin
- equivalent_circuit
- linear_network
- battery_model
- humanoid_robot
theoretical_depth:
- formalism
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Standard circuit-theory formalism; widely applied to battery modeling. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_dorf_svoboda_2017
  type: paper
  title: Dorf & Svoboda, Introduction to Electric Circuits, 9th ed.
  url: https://www.wiley.com/en-us/Introduction+to+Electric+Circuits%2C+9th+Edition-p-9781118931897
  date: '2017-01-01'
  accessed_at: '2026-06-26'
related_entities:
- id: ent_equation_thevenin_terminal_voltage
  relationship: includes
  description:
    en: The formalism includes the terminal-voltage equation derived from the equivalent circuit.
    zh: 该形式化包含由等效电路推导出的端电压方程。
    ko: 형식화는 등가 회로에서 유도된 단자 전압 방정식을 포함한다.
---
## 概述
一种形式化方法，将任意线性电网络从两个端子看进去替换为一个等效理想电压源串联一个等效电阻。

## 核心内容
### Thevenin 等效电路的定义与定位
Thevenin 等效电路属于 **formalism** 类型。 所属领域包括：00_foundations, 06_design_engineering。 价值链层级：foundations, midstream。 一种形式化方法，将任意线性电网络从两个端子看进去替换为一个等效理想电压源串联一个等效电阻。 英文名称为 *Thevenin Equivalent Circuit*。 韩文名称为 *테베닌 등가 회로*。

### Thevenin 等效电路的数学与原理基础
Thevenin 等效电路建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，Thevenin 等效电路通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现Thevenin 等效电路时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
Thevenin 等效电路可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- thevenin
- equivalent_circuit
- linear_network
- battery_model
- humanoid_robot

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键formalism之一，Thevenin 等效电路在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [Dorf & Svoboda, Introduction to Electric Circuits, 9th ed.](https://www.wiley.com/en-us/Introduction+to+Electric+Circuits%2C+9th+Edition-p-9781118931897)

