---
$id: ent_continuity_equation
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: equation
names:
  en: Continuity equation
  zh: 连续性方程
  ko: 연속 방정식
summary:
  en: A partial differential equation expressing local conservation of a quantity by equating its rate of change to the negative
    divergence of its flux.
  zh: 一种偏微分方程，通过将某物理量的变化率等于其通量散度的负值来表达局部守恒。
  ko: 어떤 물리량의 변화율을 그 선속의 발산의 음수와 같게 하여 국소 보존을 표현하는 편미분 방정식.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
theoretical_depth:
- principle
tags:
- conservation
- pde
- continuity_equation
- mass_transport
- probability
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard foundational knowledge; reviewed against standard references. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_evans_2010
  type: other
  title: L. C. Evans, Partial Differential Equations, 2nd ed., American Mathematical Society, 2010
  url: https://doi.org/10.1090/gsm/019
  date: '2010-01-01'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_ficks_law
  relationship: builds_on
  description:
    en: Substituting Fick's flux into the continuity equation gives the diffusion equation.
    zh: 将菲克通量代入连续性方程可得到扩散方程。
    ko: 픽의 선속을 연속 방정식에 대입하면 확산 방정식을 얻습니다.
- id: ent_flow_matching
  relationship: is_prerequisite_for
  description:
    en: Flow matching constructs probability paths that satisfy the continuity equation by design.
    zh: 流匹配按设计构造满足连续性方程的概率路径。
    ko: 흐름 매칭은 설계상 연속 방정식을 만족하는 확률 경로를 구성합니다.
- id: ent_ddpm_reverse_process
  relationship: is_prerequisite_for
  description:
    en: The continuous-time probability flow of diffusion models satisfies a Fokker-Planck continuity equation.
    zh: 扩散模型的连续时间概率流满足 Fokker-Planck 连续性方程。
    ko: 확산 모델의 연속 시간 확률 흐름은 포커-플랑크 연속 방정식을 만족합니다.
---

## 概述
一种偏微分方程，通过将某物理量的变化率等于其通量散度的负值来表达局部守恒。

## 核心内容
### 连续性方程的定义与定位
连续性方程属于 **方程** 类型。 所属领域包括：基础学科。 价值链层级：基础层。 一种偏微分方程，通过将某物理量的变化率等于其通量散度的负值来表达局部守恒。 英文名称为 *Continuity equation*。 韩文名称为 *연속 방정식*。

### 连续性方程的数学与原理基础
连续性方程建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，连续性方程通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现连续性方程时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
连续性方程可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- conservation
- pde
- continuity_equation
- mass_transport
- probability

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键方程之一，连续性方程在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [L. C. Evans, Partial Differential Equations, 2nd ed., American Mathematical Society, 2010](https://doi.org/10.1090/gsm/019)


