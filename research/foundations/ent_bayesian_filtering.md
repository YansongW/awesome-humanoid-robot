---
$id: ent_bayesian_filtering
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: formalism
names:
  en: Bayesian filtering
  zh: 贝叶斯滤波
  ko: 베이지안 필터링
summary:
  en: A recursive probabilistic framework that maintains and updates a belief distribution over a hidden state using a dynamical model and noisy observations.
  zh: 利用动力学模型与带噪观测递归地维护并更新隐状态信念分布的概率框架。
  ko: 동역학 모델과 잡음이 있는 관측을 사용하여 은닉 상태에 대한 믿음 분포를 재귀적으로 유지하고 업데이트하는 확률적 프레임워크.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
theoretical_depth:
- formalism
tags:
- state_estimation
- bayesian_inference
- filtering
- kalman_filter
- hidden_state
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard foundational knowledge; reviewed against standard references.
sources:
- id: src_sarkka_2013
  type: other
  title: S. Särkkä, Bayesian Filtering and Smoothing, Cambridge University Press, 2013
  url: https://doi.org/10.1017/CBO9781139344203
  date: '2013-01-01'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_ddpm_reverse_process
  relationship: builds_on
  description:
    en: Both Bayesian filtering and the DDPM reverse process recursively refine a distribution using conditional information, though the latter is generative rather than estimative.
    zh: 贝叶斯滤波与 DDPM 逆过程都利用条件信息递归地精化分布，只是后者用于生成而非估计。
    ko: 베이지안 필터링과 DDPM 역 과정 모두 조걶 정보를 사용하여 분포를 재귀적으로 정제하지만 후자는 추정이 아닌 생성을 위한 것입니다.
---

# Bayesian filtering / 贝叶斯滤波 / 베이지안 필터링

## 生活实例 + 自然语言阐述逻辑

> **生活实例**：想象在雾中公园里追踪朋友：你先根据他走的方向猜测位置（预测），再在一瞥到身影时修正猜测（更新）。贝叶斯滤波用概率分布把这种两步循环形式化。
>
> **自然语言逻辑**：贝叶斯滤波将不确定性显式表示为隐状态上的概率分布。每个时间步包含两个阶段：预测步骤通过状态转移模型传播先验信念，更新步骤利用贝叶斯规则和新观测似然修正预测信念。

## 形式化定义 / Formal Definition

Let $x_t$ be the hidden state and $y_t$ the observation at time $t$. The joint model is

$$x_t \sim p(x_t \mid x_{t-1}), \qquad y_t \sim p(y_t \mid x_t).$$

The filtering distribution $p(x_t \mid y_{1:t})$ is computed recursively:

**Prediction:**

$$p(x_t \mid y_{1:t-1}) = \int p(x_t \mid x_{t-1}) \, p(x_{t-1} \mid y_{1:t-1}) \, dx_{t-1}.$$

**Update:**

$$p(x_t \mid y_{1:t}) = \frac{p(y_t \mid x_t) \, p(x_t \mid y_{1:t-1})}{\int p(y_t \mid x_t') \, p(x_t' \mid y_{1:t-1}) \, dx_t'}.$$

For linear-Gaussian models this reduces to the Kalman filter; for nonlinear/non-Gaussian models approximations such as particle filters or variational filters are used.

## 关键符号与直觉对应

| 符号 | 名称 | 直觉含义 |
|------|------|----------|
| $x_t$ | 隐状态 | 无法直接观测的系统状态 |
| $y_t$ | 观测 | 带噪声的传感器读数 |
| $p(x_t \mid x_{t-1})$ | 状态转移概率 | 描述状态如何演化的动力学模型 |
| $p(y_t \mid x_t)$ | 观测似然 | 给定状态时观测出现的概率 |
| $p(x_t \mid y_{1:t})$ | 滤波分布 | 融合所有历史观测后的状态信念 |
| $y_{1:t}$ | 观测历史 | 从时刻 1 到 t 的所有观测 |

## 与其他知识点的关系

- `builds_on` → [ent_ddpm_reverse_process]

## 参考文献

1. S. Särkkä, Bayesian Filtering and Smoothing, Cambridge University Press, 2013
