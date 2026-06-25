---
$id: ent_ddpm_reverse_process
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: algorithm
names:
  en: DDPM reverse process
  zh: DDPM 逆过程
  ko: DDPM 역 과정
summary:
  en: The learned backward Markov chain in Denoising Diffusion Probabilistic Models that gradually transforms Gaussian noise into data-like samples.
  zh: 去噪扩散概率模型（DDPM）中学习的反向马尔可夫链，逐步将高斯噪声转化为类数据样本。
  ko: 디노이징 확산 확률 모델(DDPM)에서 학습된 역방향 마르코프 체인으로, 점진적으로 가우시안 노이즈를 데이터와 유사한 샘플로 변환합니다.
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
- diffusion_model
- ddpm
- reverse_process
- score_estimation
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard foundational knowledge; reviewed against standard references.
sources:
- id: src_ho_2020
  type: paper
  title: J. Ho, A. Jain, and P. Abbeel, 'Denoising Diffusion Probabilistic Models', NeurIPS, 2020
  url: https://proceedings.neurips.cc/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html
  date: '2020-01-01'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_score_matching
  relationship: uses
  description:
    en: DDPM trains its noise-prediction network using a denoising score-matching objective.
    zh: DDPM 使用去噪分数匹配目标训练其噪声预测网络。
    ko: DDPM은 노이즈 제거 점수 매칭 목적함수를 사용하여 노이즈 예측 네트워크를 훈련합니다.
- id: ent_continuity_equation
  relationship: is_prerequisite_for
  description:
    en: The continuous-time limit of DDPM is described by a reverse-time stochastic differential equation whose probability flow obeys a continuity equation.
    zh: DDPM 的连续时间极限由反向时间随机微分方程描述，其概率流满足连续性方程。
    ko: DDPM의 연속 시간 극한은 역시간 확률 미분 방정식으로 설명되며 그 확률 흐름은 연속 방정식을 따릅니다.
- id: ent_flow_matching
  relationship: is_alternative_to
  description:
    en: Flow matching provides an alternative generative framework that directly learns a deterministic probability flow instead of a stochastic reverse diffusion chain.
    zh: 流匹配提供了一种替代生成框架，直接学习确定性的概率流而非随机逆扩散链。
    ko: 흐름 매칭은 확률적 역 확산 체인 대신 결정론적 확률 흐름을 직접 학습하는 대안 생성 프레임워크를 제공합니다.
---

# DDPM reverse process / DDPM 逆过程 / DDPM 역 과정

## 抽象

> **生活实例**：想象一位雕塑家从一块噪声大理石开始，参照成品雕像照片慢慢凿去错误部分。DDPM 逆过程就是这位雕塑家，一步一步将纯随机性转化为结构化图像。
>
> **自然语言逻辑**：DDPM 首先定义前向过程，每步加入少量噪声直到数据近似高斯。逆过程学习如何逆转这一退化。由于每步前向转移都是高斯分布，最优逆步也是高斯分布，其均值可通过神经网络预测，该网络经分数匹配训练以估计所加噪声。

## 形式化定义 / Formal Definition

Let $\mathbf{x}_0$ be a data sample. The forward process adds Gaussian noise over $T$ steps:

$$q(\mathbf{x}_t \mid \mathbf{x}_{t-1}) = \mathcal{N}(\mathbf{x}_t; \sqrt{1-\beta_t}\,\mathbf{x}_{t-1}, \beta_t I),$$

with a variance schedule $\{\beta_t\}_{t=1}^T$.

The reverse process is a learned Markov chain starting at $p(\mathbf{x}_T) = \mathcal{N}(0, I)$:

$$p_\theta(\mathbf{x}_{t-1} \mid \mathbf{x}_t) = \mathcal{N}\bigl(\mathbf{x}_{t-1}; \mu_\theta(\mathbf{x}_t, t), \Sigma_\theta(\mathbf{x}_t, t)\bigr).$$

Ho et al. showed that $\mu_\theta$ can be parametrized by predicting the noise $\boldsymbol{\epsilon}$ in $\mathbf{x}_t$, and the simplified training objective is

$$\mathcal{L}_\text{simple}(\theta) = \mathbb{E}_{\mathbf{x}_0, \boldsymbol{\epsilon}, t} \left[ \|\boldsymbol{\epsilon} - \boldsymbol{\epsilon}_\theta(\sqrt{\bar{\alpha}_t}\mathbf{x}_0 + \sqrt{1-\bar{\alpha}_t}\boldsymbol{\epsilon}, t)\|^2 \right],$$

where $\bar{\alpha}_t = \prod_{s=1}^t (1-\beta_s)$.

## 关键符号与直觉对应

| 符号 | 名称 | 直觉含义 |
|------|------|----------|
| $\mathbf{x}_0$ | 原始数据 | 未加噪声的真实样本 |
| $\mathbf{x}_t$ | 时刻 t 的含噪样本 | 前向过程第 t 步的状态 |
| $\beta_t$ | 噪声调度 | 第 t 步添加噪声的方差 |
| $\bar{\alpha}_t$ | 累积信号保留率 | 到时刻 t 为止保留原始信号的比例 |
| $\boldsymbol{\epsilon}$ | 添加的高斯噪声 | 前向过程中注入的随机噪声 |
| $\boldsymbol{\epsilon}_\theta$ | 噪声预测网络 | 学习估计噪声的神经网络 |

## 与其他知识点的关系

- `uses` → [ent_score_matching]
- `is_prerequisite_for` → [ent_continuity_equation]
- `is_alternative_to` → [ent_flow_matching]

## 参考文献

1. J. Ho, A. Jain, and P. Abbeel, 'Denoising Diffusion Probabilistic Models', NeurIPS, 2020
