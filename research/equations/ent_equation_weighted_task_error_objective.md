---
$id: ent_equation_weighted_task_error_objective
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: equation
names:
  en: Weighted Task-Error Objective
  zh: 加权任务误差目标函数
  ko: 가중 작업 오차 목적 함수
summary:
  en: The QP objective that penalizes the weighted squared difference between desired and predicted task accelerations plus a regularization term on generalized accelerations.
  zh: 惩罚期望任务加速度与预测任务加速度之间加权平方差，并对广义加速度添加正则项的 QP 目标。
  ko: 원하는 작업 가속도와 예측 작업 가속도 간의 가중 제곱 차이를 벌점으로 부여하고 일반화 가속도에 정규화 항을 추가한 QP 목적 함수이다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
tags:
- qp_objective
- task_error
- weighted_norm
- regularization
- humanoid_control
theoretical_depth:
- formalism
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Standard weighted least-squares objective in WBC.
sources:
- id: src_001
  type: paper
  title: 'Hierarchical QP whole-body control: from theory to practice'
  url: https://arxiv.org/abs/1910.13329
  date: '2019'
  accessed_at: '2026-06-26'
related_entities:
- id: ent_operator_task_jacobian
  relationship: uses
  description:
    en: The objective uses the task Jacobian to map joint accelerations to task accelerations.
    zh: 目标函数使用任务 Jacobian 将关节加速度映射到任务加速度。
    ko: 목적 함수는 작업 Jacobian을 사용하여 관절 가속도를 작업 가속도로 매핑한다.
---

## 抽象

> **生活实例**：你正在指挥一个交响乐团，每个乐器组都有自己的乐谱。指挥的目标是让整个乐团的声音尽量接近理想演奏。如果弦乐稍弱，就多加点弦乐的权重；如果铜管太强，就压低一点。加权任务误差目标函数就是这样一个“指挥”——它给每个任务误差赋予权重，让整体表现最接近目标。
>
> **自然语言逻辑**：把每个任务的期望加速度与实际加速度之差平方后乘以权重，再求和；加上一个对关节加速度的正则项防止解过大；最终得到 QP 的目标函数。

## Overview

The weighted task-error objective in inverse-dynamics WBC is typically written as:

```
min  ½ Σᵢ ‖Jᵢ q̈ + J̇ᵢ q̇ − aᵢ‖²_{Wᵢ} + ½ ρ ‖q̈‖²
```

where `Jᵢ` is the task Jacobian, `aᵢ` is the desired task acceleration, `Wᵢ` is the task weight matrix, and `ρ` is a regularization parameter. The weighted norm `‖x‖²_W` is defined as `xᵀ W x`.

## Relevance to Humanoid Robotics

This equation quantifies the trade-off between tracking multiple tasks. By adjusting the weight matrices, engineers can make balance more important than arm motion, or vice versa.
