---
$id: ent_paper_dynamic_rope_manipulation_task_level_ite_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Dynamic Rope Manipulation Using Task-Level Iterative Learning Control
  zh: 仓库 README 亦写作 *Learning Dynamic Rope Manipulation Using Task-Level Iterative Learning Control*）
  ko: Learning Dynamic Rope Manipulation Using Task-Level Iterative Learning Control
summary:
  en: 'We introduce a Task-Level Iterative Learning Control method for dynamic manipulation of ropes. We demonstrate this
    method on a non-planar rope manipulation task called the flying knot. Institutions per source list: Carnegie Mellon University（卡内基梅隆大学）.'
  zh: 本文提出了一种任务级迭代学习控制方法，用于实现绳索的动态操作。该方法通过单次人类演示和简化绳索模型，在真实硬件上直接学习，无需大量演示数据或仿真。实验在7种不同绳索上均能在10次尝试内达到100%成功率，且多数绳索间迁移仅需2-5次尝试。
  ko: 'We introduce a Task-Level Iterative Learning Control method for dynamic manipulation of ropes. We demonstrate this
    method on a non-planar rope manipulation task called the flying knot. Institutions per source list: Carnegie Mellon University（卡内基梅隆大学）.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- dynamic
- rope
- manipulation
- task
- level
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 369 (.staging/ingest_yuanxq). Tier A->full. Title guard: jaccard (score
    0.636). Abstract and metadata from arXiv API (2602.21302v2); zh content by DeepSeek from the abstract. Institutions as
    given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: arXiv:2602.21302 Learning Dynamic Rope Manipulation Using Task-Level Iterative Learning Control
  url: https://arxiv.org/abs/2602.21302
  accessed_at: '2026-07-31'
  date: '2026-02-24'
- id: src_002
  type: website
  title: Project page
  url: https://flying-knots.github.io
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

该研究针对绳索的动态操作难题，提出了一种任务级迭代学习控制方法。方法的核心在于利用单次人类演示和简化绳索模型，通过求解二次规划来反向传播任务空间误差，从而更新动作。该方法在名为“飞结”的非平面绳索操作任务上进行了验证，并评估了7种不同绳索（包括链条、乳胶手术管、编织绳和绞绳），其厚度范围为7-25毫米，密度范围为0.013-0.5千克/米。实验结果显示，所有绳索均在10次尝试内达到100%成功率，且大多数绳索类型间的迁移仅需2-5次尝试。

## 核心内容
### 方法
- **任务级迭代学习控制**：该方法通过迭代过程学习绳索的动态操作。每次迭代中，算法通过求解一个二次规划来反向传播任务空间误差，从而更新机器人动作。该过程依赖于一个简化的机器人-绳索模型，该模型通过单次人类演示进行初始化。
- **模型与演示**：方法仅需一次人类演示和简化的绳索模型，避免了大量演示数据或仿真依赖。模型用于将任务空间误差映射到动作更新。

### 实验设置
- **任务**：非平面绳索操作任务“飞结”（flying knot），要求机器人动态地打一个结。
- **绳索种类**：实验使用了7种不同的绳索，包括链条、乳胶手术管、编织绳和绞绳。绳索厚度范围为7-25毫米，密度范围为0.013-0.5千克/米。
- **硬件**：方法直接在真实硬件上执行，无需仿真。

### 关键结果
- **学习性能**：所有7种绳索均在10次尝试内达到100%的成功率。
- **迁移能力**：方法能够在大多数绳索类型间成功迁移，迁移所需尝试次数为2-5次。
- **结论**：该方法展示了在真实硬件上通过少量演示和迭代学习实现动态绳索操作的有效性，且对绳索类型具有鲁棒性。

## Overview
We introduce a Task-Level Iterative Learning Control method for dynamic manipulation of ropes. We demonstrate this method on a non-planar rope manipulation task called the flying knot. Using a single human demonstration and a simplified rope model, the method learns directly on hardware without reliance on large amounts of demonstration data or massive amounts of simulation. At each iteration, the algorithm inverts a model of the robot and rope by solving a quadratic program to propagate task-space errors into action updates. We evaluate performance across 7 different kinds of ropes, including chain, latex surgical tubing, and braided and twisted ropes, ranging in thicknesses of 7--25\,mm and densities of 0.013--0.5\,kg/m. Learning achieves a 100\% success rate within 10 trials on all ropes. Furthermore, the method can successfully transfer between most rope types in 2--5 trials. https://flying-knots.github.io

## 参考
- https://arxiv.org/abs/2602.21302
- https://flying-knots.github.io
- https://github.com/ImChong/Robotics_Notebooks

## 개요

이 연구는 로프의 동적 조작 문제를 해결하기 위해 작업 수준 반복 학습 제어 방법을 제안합니다. 이 방법의 핵심은 단일 인간 시연과 단순화된 로프 모델을 활용하여, 이차 계획법을 풀어 작업 공간 오차를 역전파함으로써 동작을 업데이트하는 데 있습니다. 이 방법은 "비행 매듭"이라는 비평면 로프 조작 작업에서 검증되었으며, 체인, 라텍스 수술용 튜브, 편조 로프 및 꼬임 로프를 포함한 7가지 다른 로프(두께 범위 7-25mm, 밀도 범위 0.013-0.5kg/m)에 대해 평가되었습니다. 실험 결과, 모든 로프가 10회 시도 내에 100% 성공률을 달성했으며, 대부분의 로프 유형 간 전환은 2-5회 시도만 필요했습니다.

## 핵심 내용
### 방법
- **작업 수준 반복 학습 제어**: 이 방법은 반복 과정을 통해 로프의 동적 조작을 학습합니다. 각 반복에서 알고리즘은 이차 계획법을 풀어 작업 공간 오차를 역전파함으로써 로봇 동작을 업데이트합니다. 이 과정은 단일 인간 시연을 통해 초기화된 단순화된 로봇-로프 모델에 의존합니다.
- **모델 및 시연**: 이 방법은 단 한 번의 인간 시연과 단순화된 로프 모델만 필요로 하며, 대량의 시연 데이터나 시뮬레이션 의존성을 피합니다. 모델은 작업 공간 오차를 동작 업데이트에 매핑하는 데 사용됩니다.

### 실험 설정
- **작업**: 비평면 로프 조작 작업 "비행 매듭"(flying knot)으로, 로봇이 동적으로 매듭을 짓도록 요구합니다.
- **로프 종류**: 실험에는 체인, 라텍스 수술용 튜브, 편조 로프 및 꼬임 로프를 포함한 7가지 다른 로프가 사용되었습니다. 로프 두께 범위는 7-25mm, 밀도 범위는 0.013-0.5kg/m입니다.
- **하드웨어**: 이 방법은 시뮬레이션 없이 실제 하드웨어에서 직접 실행됩니다.

### 주요 결과
- **학습 성능**: 7가지 모든 로프가 10회 시도 내에 100%의 성공률을 달성했습니다.
- **전환 능력**: 이 방법은 대부분의 로프 유형 간에 성공적으로 전환할 수 있었으며, 전환에 필요한 시도 횟수는 2-5회였습니다.
- **결론**: 이 방법은 소수의 시연과 반복 학습을 통해 실제 하드웨어에서 동적 로프 조작을 구현하는 효과성을 보여주며, 로프 유형에 대해 강건함을 입증했습니다.
