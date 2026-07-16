---
$id: ent_method_whole_body_control
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Whole-Body Control (WBC)
  zh: 全身控制（WBC）
  ko: 전신 제어(WBC)
summary:
  en: A control framework that coordinates all joints and contacts of a humanoid to achieve multiple tasks such as balance,
    gaze, and manipulation.
  zh: 协调人形机器人所有关节与接触点，以同时实现平衡、注视、操作等多任务的统一控制框架。
  ko: 휴로봇의 모든 관절과 접촉점을 조율하여 균형·시선·조작 등 다중 작업을 동시에 수행하는 제어 프레임워크.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
tags:
- method
- chapter_14
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-08.md#8.4.10 全身控制 by scripts/backfill_nonpaper_entries.py. Body backfilled from entity
    metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---

## 概述
协调人形机器人所有关节与接触点，以同时实现平衡、注视、操作等多任务的统一控制框架。

## 核心内容
### 全身控制（WBC）的定义与定位
全身控制（WBC）属于 **方法** 类型。 所属领域包括：AI 模型与算法。 价值链层级：智能层。 协调人形机器人所有关节与接触点，以同时实现平衡、注视、操作等多任务的统一控制框架。 英文名称为 *Whole-Body Control (WBC)*。 韩文名称为 *전신 제어(WBC)*。

### 全身控制（WBC）的数学与原理基础
全身控制（WBC）建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，全身控制（WBC）通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现全身控制（WBC）时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
全身控制（WBC）可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- method
- chapter_14
- wiki_gap

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键方法之一，全身控制（WBC）在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- Wiki extraction


