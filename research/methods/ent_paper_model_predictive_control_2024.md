---
$id: ent_paper_model_predictive_control_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Model Predictive Control
  zh: 模型预测控制
  ko: Model Predictive Control
summary:
  en: Online optimal-control approach for generating contact-rich whole-body motion.
  zh: 用于生成接触丰富的全身运动的在线最优控制方法。
  ko: 접촉이 풍부한 전신 동작을 생성하기 위한 온라인 최적 제어 접근법.
domains:
- 07_ai_models_algorithms
- 06_design_engineering
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- control
- method
- mpc
- optimization
- whole_body
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-02'
  confidence: medium
  notes: Imported via ingestion framework from source_type=website. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_001
  type: website
  title: Model Predictive Control
  url: https://roboti.us/lab/papers/KoenemannIROS15.pdf
  date: '2024'
  accessed_at: '2026-07-02'
---

## 概述
用于生成接触丰富的全身运动的在线最优控制方法。

## 核心内容
### 模型预测控制的定义与定位
模型预测控制属于 **方法** 类型。 所属领域包括：AI 模型与算法, 设计工程。 价值链层级：智能层, midstream。 用于生成接触丰富的全身运动的在线最优控制方法。 英文名称为 *Model Predictive Control*。 韩文名称为 *Model Predictive Control*。

### 模型预测控制的数学与原理基础
模型预测控制建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，模型预测控制通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现模型预测控制时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
模型预测控制可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- control
- method
- mpc
- optimization
- whole_body

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键方法之一，模型预测控制在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [Model Predictive Control](https://roboti.us/lab/papers/KoenemannIROS15.pdf)


