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
  en: A generative modeling method that directly regresses a vector field whose flow maps a simple source distribution to a target data distribution.
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
  notes: Standard foundational knowledge; reviewed against standard references.
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
    en: Like score matching, flow matching learns a vector field over data space, but it directly regresses a velocity rather than a score.
    zh: 与分数匹配类似，流匹配也学习数据空间上的向量场，但它直接回归速度而非分数。
    ko: 점수 매칭과 마찬가지로 흐름 매칭은 데이터 공간에 대한 벡터 필드를 학습하지만, 점수가 아닌 속도를 직접 회귀합니다.
- id: ent_ddpm_reverse_process
  relationship: is_alternative_to
  description:
    en: Flow matching offers a deterministic ODE-based alternative to the stochastic reverse diffusion chain used by DDPM.
    zh: 流匹配为 DDPM 使用的随机逆扩散链提供了一种基于确定性 ODE 的替代方案。
    ko: 흐름 매칭은 DDPM에서 사용하는 확률적 역 확산 체인에 대한 결정론적 ODE 기반 대안을 제공합니다.
---

# Flow matching / 流匹配 / 흐름 매칭

## 生活实例 + 自然语言阐述逻辑

> **生活实例**：想象一条河从源头平静的湖泊流向最终形成可辨识地貌。流匹配学习每一点的水流，使湖中的水滴被带到地貌中的正确位置。
>
> **自然语言逻辑**：流匹配不学习密度或分数，而是学习时间相关的速度场。在温和条件下，该速度场定义一个常微分方程，其在时刻 1 的解将样本从基分布传输到数据分布。关键洞见在于可以通过对条件概率路径回归训练速度场，避免显式似然归一化。

## 形式化定义 / Formal Definition

Let $p_0$ be a simple source distribution (e.g., standard Gaussian) and $p_1$ the data distribution. Flow matching constructs a time-dependent vector field $u_t(\mathbf{x})$ such that the ODE

$$\frac{d\mathbf{x}_t}{dt} = u_t(\mathbf{x}_t), \qquad \mathbf{x}_0 \sim p_0,$$

satisfies $\mathbf{x}_1 \sim p_1$. The probability path $p_t$ induced by the flow satisfies the continuity equation

$$\frac{\partial p_t}{\partial t} + \nabla \cdot (p_t u_t) = 0.$$

A conditional flow $p_t(\mathbf{x} \mid \mathbf{x}_1)$ with vector field $u_t(\mathbf{x} \mid \mathbf{x}_1)$ is trained by the flow-matching loss

$$\mathcal{L}_\text{FM}(\theta) = \mathbb{E}_{t, \mathbf{x}_1, \mathbf{x}_t} \left[ \|u_t(\mathbf{x}_t \mid \mathbf{x}_1) - u_\theta(\mathbf{x}_t, t)\|^2 \right],$$

where $t \sim \mathcal{U}[0,1]$, $\mathbf{x}_1 \sim p_1$, and $\mathbf{x}_t \sim p_t(\cdot \mid \mathbf{x}_1)$.

## 关键符号与直觉对应

| 符号 | 名称 | 直觉含义 |
|------|------|----------|
| $p_0$ | 源分布 | 简单、易采样的初始分布 |
| $p_1$ | 目标数据分布 | 需要学习的真实数据分布 |
| $u_t(\mathbf{x})$ | 速度场 | 时刻 t 处数据空间的速度向量场 |
| $p_t$ | 中间分布 | 时刻 t 的插值概率分布 |
| $\nabla \cdot (p_t u_t)$ | 概率流散度 | 描述概率质量随流动变化的项 |
| $u_\theta$ | 参数化速度场 | 神经网络学习的速度场 |

## 与其他知识点的关系

- `builds_on` → [ent_continuity_equation]
- `builds_on` → [ent_score_matching]
- `is_alternative_to` → [ent_ddpm_reverse_process]

## 参考文献

1. Y. Lipman et al., 'Flow Matching for Generative Modeling', ICLR, 2023
