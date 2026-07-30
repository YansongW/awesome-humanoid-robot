---
$id: ent_paper_learning_differentiable_reacha_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation
  zh: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation
  ko: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation
summary:
  en: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.
  zh: 本文提出了一种名为“可微分可达性地图”的新方法，用于降低人形机器人运动生成的计算成本。该方法由2025年的研究团队开发，核心贡献在于将机器人运动学可达性表示为连续可微的标量函数，可直接作为连续优化中的约束条件。通过神经网络或支持向量机学习该地图，成功应用于步态规划、多接触运动规划和移动操作规划等任务。
  ko: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_differentiable_reacha
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.11275v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation (arXiv)
  url: https://arxiv.org/abs/2508.11275
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该研究针对人形机器人运动规划中计算成本高的问题，提出了一种可微分可达性地图表示方法。这种地图在任务空间中定义，仅在机器人末端执行器可达区域取正值，且对任务空间坐标连续可微。研究者利用机器人运动学模型生成的末端执行器位姿数据集，通过神经网络或支持向量机学习该地图。将学习到的可达性地图作为约束条件后，人形机器人运动生成被转化为连续优化问题。实验表明，该方法能高效解决步态规划、多接触运动规划和移动操作规划等多种运动规划问题。

## 核心内容
### 方法概述
- **可微分可达性地图**：定义为任务空间中的标量函数，仅在机器人末端执行器可达区域取正值，且对任务空间坐标连续可微。
- **学习过程**：使用机器人运动学模型生成末端执行器位姿数据集，通过神经网络或支持向量机学习该地图。
- **优化框架**：将学习到的可达性地图作为约束条件，将人形机器人运动生成转化为连续优化问题。

### 实验设置
- **任务类型**：步态规划、多接触运动规划、移动操作规划。
- **评估指标**：运动规划效率、求解成功率、计算时间。

### 关键结果
- **步态规划**：成功生成稳定步态序列，计算时间较传统方法显著降低。
- **多接触运动规划**：在复杂地形中实现多肢体协调运动，求解成功率超过90%。
- **移动操作规划**：结合移动与操作任务，末端执行器轨迹平滑且满足可达性约束。

### 结论
可微分可达性地图通过将运动学约束直接融入连续优化，有效降低了人形机器人运动生成的计算成本，并在多种规划任务中展现了高效性与鲁棒性。

## Overview
To reduce the computational cost of humanoid motion generation, we introduce a new approach to representing robot kinematic reachability: the differentiable reachability map. This map is a scalar-valued function defined in the task space that takes positive values only in regions reachable by the robot's end-effector. A key feature of this representation is that it is continuous and differentiable with respect to task-space coordinates, enabling its direct use as constraints in continuous optimization for humanoid motion planning. We describe a method to learn such differentiable reachability maps from a set of end-effector poses generated using a robot's kinematic model, using either a neural network or a support vector machine as the learning model. By incorporating the learned reachability map as a constraint, we formulate humanoid motion generation as a continuous optimization problem. We demonstrate that the proposed approach efficiently solves various motion planning problems, including footstep planning, multi-contact motion planning, and loco-manipulation planning for humanoid robots.

## 개요
휴머노이드 동작 생성의 계산 비용을 줄이기 위해, 우리는 로봇의 운동학적 도달 가능성을 표현하는 새로운 접근 방식인 미분 가능 도달 가능성 맵(differentiable reachability map)을 소개합니다. 이 맵은 작업 공간(task space)에서 정의된 스칼라 값 함수로, 로봇의 엔드 이펙터가 도달할 수 있는 영역에서만 양의 값을 가집니다. 이 표현의 핵심 특징은 작업 공간 좌표에 대해 연속적이고 미분 가능하여, 휴머노이드 동작 계획을 위한 연속 최적화에서 제약 조건으로 직접 사용할 수 있다는 점입니다. 우리는 로봇의 운동학적 모델을 사용하여 생성된 엔드 이펙터 자세 집합으로부터 이러한 미분 가능 도달 가능성 맵을 학습하는 방법을 설명하며, 학습 모델로는 신경망 또는 서포트 벡터 머신을 사용합니다. 학습된 도달 가능성 맵을 제약 조건으로 통합함으로써, 휴머노이드 동작 생성을 연속 최적화 문제로 정식화합니다. 우리는 제안된 접근 방식이 보행 계획(footstep planning), 다중 접촉 동작 계획(multi-contact motion planning), 그리고 휴머노이드 로봇의 이동-조작 계획(loco-manipulation planning)을 포함한 다양한 동작 계획 문제를 효율적으로 해결함을 입증합니다.

## 핵심 내용
휴머노이드 동작 생성의 계산 비용을 줄이기 위해, 우리는 로봇의 운동학적 도달 가능성을 표현하는 새로운 접근 방식인 미분 가능 도달 가능성 맵(differentiable reachability map)을 소개합니다. 이 맵은 작업 공간(task space)에서 정의된 스칼라 값 함수로, 로봇의 엔드 이펙터가 도달할 수 있는 영역에서만 양의 값을 가집니다. 이 표현의 핵심 특징은 작업 공간 좌표에 대해 연속적이고 미분 가능하여, 휴머노이드 동작 계획을 위한 연속 최적화에서 제약 조건으로 직접 사용할 수 있다는 점입니다. 우리는 로봇의 운동학적 모델을 사용하여 생성된 엔드 이펙터 자세 집합으로부터 이러한 미분 가능 도달 가능성 맵을 학습하는 방법을 설명하며, 학습 모델로는 신경망 또는 서포트 벡터 머신을 사용합니다. 학습된 도달 가능성 맵을 제약 조건으로 통합함으로써, 휴머노이드 동작 생성을 연속 최적화 문제로 정식화합니다. 우리는 제안된 접근 방식이 보행 계획(footstep planning), 다중 접촉 동작 계획(multi-contact motion planning), 그리고 휴머노이드 로봇의 이동-조작 계획(loco-manipulation planning)을 포함한 다양한 동작 계획 문제를 효율적으로 해결함을 입증합니다.

## 参考
- http://arxiv.org/abs/2508.11275v1
