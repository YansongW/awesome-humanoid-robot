---
$id: ent_score_matching
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: algorithm
names:
  en: Score matching
  zh: 分数匹配
  ko: 점수 매칭
summary:
  en: A parameter-estimation technique that learns the gradient of an unknown log-probability density, called the score, without
    requiring normalized probability densities.
  zh: 一种参数估计技术，学习未知对数概率密度的梯度（称为分数），而无需归一化的概率密度。
  ko: 정규화된 확률 밀도 없이도 미지의 로그 확률 밀도의 기울기(점수)를 학습하는 매개변수 추정 기법.
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
- score_estimation
- score_matching
- diffusion
- hyvarinen
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard foundational knowledge; reviewed against standard references. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_hyvarinen_2005
  type: paper
  title: A. Hyvärinen, 'Estimation of Non-Normalized Statistical Models by Score Matching', J. Machine Learning Research,
    vol. 6, pp. 695–709, 2005
  url: https://jmlr.org/papers/v6/hyvarinen05a.html
  date: '2005-01-01'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_ddpm_reverse_process
  relationship: is_prerequisite_for
  description:
    en: DDPM trains a score-like noise model via denoising score matching and uses it to reverse the diffusion process.
    zh: DDPM 通过去噪分数匹配训练类分数的噪声模型，并用其逆转扩散过程。
    ko: DDPM은 노이즈 제거 점수 매칭을 통해 점수와 유사한 노이즈 모델을 훈련하고 이를 사용하여 확산 과정을 역전시킵니다.
- id: ent_flow_matching
  relationship: builds_on
  description:
    en: Both score matching and flow matching learn vector fields that guide samples between distributions, but flow matching
      directly regresses a velocity field.
    zh: 分数匹配与流匹配都学习引导样本在分布间转移的向量场，但流匹配直接回归速度场。
    ko: 점수 매칭과 흐름 매칭 모두 분포 사이에서 샘플을 안내하는 벡터 필드를 학습하지만, 흐름 매칭은 속도 필드를 직접 회귀합니다.
---
## 概述
一种参数估计技术，学习未知对数概率密度的梯度（称为分数），而无需归一化的概率密度。

## 核心内容
### 分数匹配的定义与定位
分数匹配属于 **algorithm** 类型。 所属领域包括：00_foundations。 价值链层级：foundations。 一种参数估计技术，学习未知对数概率密度的梯度（称为分数），而无需归一化的概率密度。 英文名称为 *Score matching*。 韩文名称为 *점수 매칭*。

### 分数匹配的数学与原理基础
分数匹配建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，分数匹配通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现分数匹配时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
分数匹配可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- generative_modeling
- score_estimation
- score_matching
- diffusion
- hyvarinen

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键algorithm之一，分数匹配在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [A. Hyvärinen, 'Estimation of Non-Normalized Statistical Models by Score Matching', J. Machine Learning Research, vol. 6, pp. 695–709, 2005](https://jmlr.org/papers/v6/hyvarinen05a.html)

