---
$id: ent_flow_matching
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Flow matching
  zh: 流匹配
  ko: 흐름 매칭
summary:
  en: A generative modeling method that directly regresses a vector field whose flow maps a simple source distribution to
    a target data distribution.
  zh: 一种生成建模方法，直接回归一个向量场，使其流将简单源分布映射到目标数据分布。
  ko: 간단한 소스 분포를 목표 데이터 분포로 매핑하는 흐름을 가진 벡터 필드를 직접 회귀하는 생성 모델링 방법.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
theoretical_depth:
- method
tags:
- generative_modeling
- flow_matching
- ode
- vector_field
- normalizing_flow
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard foundational knowledge; reviewed against standard references. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_lipman_2023
  type: paper
  title: Y. Lipman et al., 'Flow Matching for Generative Modeling', ICLR, 2023
  url: https://openreview.net/forum?id=PqvMRDCJT9t
  date: '2023-01-01'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_continuity_equation
  relationship: builds_on
  description:
    en: Flow matching explicitly constructs vector fields whose probability paths satisfy the continuity equation.
    zh: 流匹配显式构造其概率路径满足连续性方程的向量场。
    ko: 흐름 매칭은 확률 경로가 연속 방정식을 만족하는 벡터 필드를 명시적으로 구성합니다.
- id: ent_score_matching
  relationship: builds_on
  description:
    en: Like score matching, flow matching learns a vector field over data space, but it directly regresses a velocity rather
      than a score.
    zh: 与分数匹配类似，流匹配也学习数据空间上的向量场，但它直接回归速度而非分数。
    ko: 점수 매칭과 마찬가지로 흐름 매칭은 데이터 공간에 대한 벡터 필드를 학습하지만, 점수가 아닌 속도를 직접 회귀합니다.
- id: ent_ddpm_reverse_process
  relationship: is_alternative_to
  description:
    en: Flow matching offers a deterministic ODE-based alternative to the stochastic reverse diffusion chain used by DDPM.
    zh: 流匹配为 DDPM 使用的随机逆扩散链提供了一种基于确定性 ODE 的替代方案。
    ko: 흐름 매칭은 DDPM에서 사용하는 확률적 역 확산 체인에 대한 결정론적 ODE 기반 대안을 제공합니다.
---

## 概述
一种生成建模方法，直接回归一个向量场，使其流将简单源分布映射到目标数据分布。

## 核心内容
### 流匹配的定义与定位
流匹配属于 **方法** 类型。 所属领域包括：基础学科。 价值链层级：基础层。 一种生成建模方法，直接回归一个向量场，使其流将简单源分布映射到目标数据分布。 英文名称为 *Flow matching*。 韩文名称为 *흐름 매칭*。

### 流匹配的数学与原理基础
流匹配建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，流匹配通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现流匹配时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
流匹配可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- generative_modeling
- flow_matching
- ode
- vector_field
- normalizing_flow

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键方法之一，流匹配在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [Y. Lipman et al., 'Flow Matching for Generative Modeling', ICLR, 2023](https://openreview.net/forum?id=PqvMRDCJT9t)


