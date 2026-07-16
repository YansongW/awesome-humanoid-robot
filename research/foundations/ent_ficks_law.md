---
$id: ent_ficks_law
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: principle
names:
  en: Fick's law
  zh: 菲克定律
  ko: 픽의 법칙
summary:
  en: A constitutive principle stating that the diffusive flux of a species is proportional to the negative gradient of its
    concentration.
  zh: 一种本构原理，指出物质的扩散通量与其浓度梯度的负值成正比。
  ko: 종의 확산 선속이 농도 기울기의 음수에 비례한다는 구성 원리.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
theoretical_depth:
- principle
tags:
- diffusion
- mass_transport
- ficks_law
- concentration
- flux
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard foundational knowledge; reviewed against standard references. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_crank_1975
  type: other
  title: J. Crank, The Mathematics of Diffusion, 2nd ed., Oxford University Press, 1975
  url: https://doi.org/10.1093/oso/9780198534112.001.0001
  date: '1975-01-01'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_nernst_planck_equation
  relationship: is_prerequisite_for
  description:
    en: The Nernst-Planck equation generalizes Fick's law by adding migration flux due to an electric field.
    zh: 能斯特-普朗克方程在菲克定律基础上增加了电场引起的迁移通量，是其推广。
    ko: 넬스트-플랑크 방정식은 전기장에 의한 이동 선속을 추가하여 픽의 법칙을 일반화합니다.
---

## 概述
一种本构原理，指出物质的扩散通量与其浓度梯度的负值成正比。

## 核心内容
### 菲克定律的定义与定位
菲克定律属于 **原理** 类型。 所属领域包括：基础学科。 价值链层级：基础层。 一种本构原理，指出物质的扩散通量与其浓度梯度的负值成正比。 英文名称为 *Fick's law*。 韩文名称为 *픽의 법칙*。

### 菲克定律的数学与原理基础
菲克定律建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，菲克定律通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现菲克定律时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
菲克定律可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- diffusion
- mass_transport
- ficks_law
- concentration
- flux

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键原理之一，菲克定律在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [J. Crank, The Mathematics of Diffusion, 2nd ed., Oxford University Press, 1975](https://doi.org/10.1093/oso/9780198534112.001.0001)


