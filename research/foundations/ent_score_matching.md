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
  en: A parameter-estimation technique that learns the gradient of an unknown log-probability density, called the score, without requiring normalized probability densities.
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
  notes: Standard foundational knowledge; reviewed against standard references.
sources:
- id: src_hyvarinen_2005
  type: paper
  title: A. Hyvärinen, 'Estimation of Non-Normalized Statistical Models by Score Matching', J. Machine Learning Research, vol. 6, pp. 695–709, 2005
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
    en: Both score matching and flow matching learn vector fields that guide samples between distributions, but flow matching directly regresses a velocity field.
    zh: 分数匹配与流匹配都学习引导样本在分布间转移的向量场，但流匹配直接回归速度场。
    ko: 점수 매칭과 흐름 매칭 모두 분포 사이에서 샘플을 안내하는 벡터 필드를 학습하지만, 흐름 매칭은 속도 필드를 직접 회귀합니다.
---

# Score matching / 分数匹配 / 점수 매칭

## 生活实例 + 自然语言阐述逻辑

> **生活实例**：想象一名登山者从未见过完整海拔图，但学会了每一步的上下坡方向。分数匹配训练模型指向概率密度最陡上升的方向。
>
> **自然语言逻辑**：许多生成模型需要概率密度的归一化常数，通常难以计算。分数匹配只学习分数函数（对数密度的梯度）来绕过这一难点。Hyvärinen 分数匹配指出，模型分数与数据分数之间期望平方差可以重写为仅涉及模型分数导数的可计算项。

## 形式化定义 / Formal Definition

Let $p_\theta(\mathbf{x})$ be a parametric density model and let $\mathbf{s}_\theta(\mathbf{x}) = \nabla_\mathbf{x} \log p_\theta(\mathbf{x})$ be its score. Given data samples from an unknown density $p_\text{data}(\mathbf{x})$, score matching minimizes

$$\mathcal{J}_\text{SM}(\theta) = \mathbb{E}_{p_\text{data}} \left[ \frac{1}{2} \|\mathbf{s}_\theta(\mathbf{x}) - \nabla_\mathbf{x} \log p_\text{data}(\mathbf{x})\|_2^2 \right].$$

Because the data score is unknown, Hyvärinen showed that up to a constant this is equivalent to minimizing the tractable objective

$$\mathcal{J}_\text{SM}(\theta) = \mathbb{E}_{p_\text{data}} \left[ \operatorname{tr}\big(\nabla_\mathbf{x} \mathbf{s}_\theta(\mathbf{x})\big) + \frac{1}{2} \|\mathbf{s}_\theta(\mathbf{x})\|_2^2 \right],$$

where $\nabla_\mathbf{x} \mathbf{s}_\theta(\mathbf{x})$ is the Jacobian of the score. Denoising score matching learns scores of perturbed data distributions, which is central to diffusion models.

## 关键符号与直觉对应

| 符号 | 名称 | 直觉含义 |
|------|------|----------|
| $p_\theta(\mathbf{x})$ | 参数化密度模型 | 待学习的概率分布 |
| $\mathbf{s}_\theta(\mathbf{x})$ | 分数（score） | 对数密度对数据的梯度 |
| $\nabla_\mathbf{x}$ | 关于数据的梯度 | 数据空间中的方向导数 |
| $\operatorname{tr}$ | 迹 | 雅可比矩阵对角元之和 |
| $p_\text{data}$ | 数据分布 | 真实但未知的样本分布 |
| $\|\cdot\|_2$ | L2 范数 | 向量欧几里得长度 |

## 与其他知识点的关系

- `is_prerequisite_for` → [ent_ddpm_reverse_process]
- `builds_on` → [ent_flow_matching]

## 参考文献

1. A. Hyvärinen, 'Estimation of Non-Normalized Statistical Models by Score Matching', J. Machine Learning Research, vol. 6, pp. 695–709, 2005
