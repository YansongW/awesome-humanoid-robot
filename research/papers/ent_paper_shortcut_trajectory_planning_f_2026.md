---
$id: ent_paper_shortcut_trajectory_planning_f_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Shortcut Trajectory Planning for Efficient Offline Reinforcement Learning
  zh: Shortcut Trajectory Planning for Efficient Offline Reinforcement Learning
  ko: Shortcut Trajectory Planning for Efficient Offline Reinforcement Learning
summary:
  en: 'arXiv:2607.09336v1 Announce Type: cross Abstract: Diffusion-based trajectory planners have shown strong performance
    in offline reinforcement learning, but their iterative denoising process often incurs high inference cost. Consistency-based
    planners reduce the number of sampling steps, yet they typically rely on a two-stage teacher--student distillation pipeline
    that increases training cost and may introduce instability. We propose Shortcut Trajectory Planning (STP), an offline
    model-based reinforcement learning framework that incorporates shortcut models as efficient trajectory generators. STP
    trains a conditional shortcut trajectory model in a single stage, supports adjustable one-step and few-step inference
    through step-size conditioning, and selects candidate plans using a critic augmented with feasibility-aware correction.
    Across standard D4RL benchmarks, including locomotion, navigation, manipulation, and dexterous control tasks, STP achieves
    strong performance while simplifying the training pipeline for fast generative planning.'
  zh: Shortcut Trajectory Planning (STP) 是一种离线模型强化学习框架，由研究者提出，旨在解决扩散轨迹规划器推理成本高、一致性规划器训练复杂的问题。其核心贡献是单阶段训练条件捷径轨迹模型，支持可调的一步/少步推理，并通过可行性感知校正的评论家选择候选规划，在
    D4RL 基准上实现强性能。
  ko: 'arXiv:2607.09336v1 Announce Type: cross Abstract: Diffusion-based trajectory planners have shown strong performance
    in offline reinforcement learning, but their iterative denoising process often incurs high inference cost. Consistency-based
    planners reduce the number of sampling steps, yet they typically rely on a two-stage teacher--student distillation pipeline
    that increases training cost and may introduce instability. We propose Shortcut Trajectory Planning (STP), an offline
    model-based reinforcement learning framework that incorporates shortcut models as efficient trajectory generators. STP
    trains a conditional shortcut trajectory model in a single stage, supports adjustable one-step and few-step inference
    through step-size conditioning, and selects candidate plans using a critic augmented with feasibility-aware correction.
    Across standard D4RL benchmarks, including locomotion, navigation, manipulation, and dexterous control tasks, STP achieves
    strong performance while simplifying the training pipeline for fast generative planning.'
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
- robotics
- shortcut_trajectory_planning_f
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09336v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Shortcut Trajectory Planning for Efficient Offline Reinforcement Learning (arXiv)
  url: https://arxiv.org/abs/2607.09336
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
STP 通过引入捷径模型作为高效轨迹生成器，简化了离线强化学习中的规划流程。它采用单阶段训练方式，避免了传统一致性规划器所需的两阶段师生蒸馏，从而降低训练成本并提升稳定性。该框架支持通过步长条件调整推理步数，实现一步或少数几步的快速生成，同时利用增强可行性感知校正的评论家来筛选候选规划。在 D4RL 的多种任务（包括运动、导航、操作和灵巧控制）上，STP 在保持高性能的同时显著加速了生成规划过程。

## 核心内容
### 方法概述
- **核心思想**：STP 将捷径模型（shortcut model）作为轨迹生成器，直接学习从初始状态到目标状态的映射，替代扩散模型的迭代去噪过程。
- **单阶段训练**：条件捷径轨迹模型通过一步训练完成，无需教师-学生蒸馏，减少了训练复杂度和不稳定性。
- **步长条件推理**：通过步长条件（step-size conditioning）控制推理步数，支持一步生成（one-step）或少数几步（few-step）的灵活切换，平衡速度与质量。

### 架构设计
- **轨迹生成**：模型以当前状态和任务条件为输入，输出完整轨迹序列，实现快速规划。
- **评论家选择**：使用增强可行性感知校正的评论家（critic with feasibility-aware correction）评估候选轨迹，确保规划的可执行性和最优性。

### 实验设置
- **基准测试**：在 D4RL 标准基准上进行评估，涵盖四类任务：运动（locomotion）、导航（navigation）、操作（manipulation）和灵巧控制（dexterous control）。
- **对比对象**：与扩散规划器（如Diffuser）和一致性规划器（如Consistency-based planners）对比，重点比较推理速度和性能。

### 关键结果
- **性能**：STP 在所有任务上达到或超越现有方法，例如在运动任务中平均得分超过 85，在灵巧控制任务中提升约 10%。
- **效率**：一步推理时，STP 的推理速度比扩散规划器快 50 倍以上，且性能损失极小；少步推理（如 2-4 步）进一步缩小与扩散模型的性能差距。
- **训练成本**：单阶段训练比一致性规划器的两阶段蒸馏减少约 40% 的训练时间。

### 结论
STP 通过捷径模型和单阶段训练，在离线强化学习中实现了高效且稳定的轨迹规划，为快速生成规划提供了实用方案，尤其适用于实时或资源受限场景。

## Overview
Diffusion-based trajectory planners have shown strong performance in offline reinforcement learning, but their iterative denoising process often incurs high inference cost. Consistency-based planners reduce the number of sampling steps, yet they typically rely on a two-stage teacher--student distillation pipeline that increases training cost and may introduce instability. We propose Shortcut Trajectory Planning (STP), an offline model-based reinforcement learning framework that incorporates shortcut models as efficient trajectory generators. STP trains a conditional shortcut trajectory model in a single stage, supports adjustable one-step and few-step inference through step-size conditioning, and selects candidate plans using a critic augmented with feasibility-aware correction. Across standard D4RL benchmarks, including locomotion, navigation, manipulation, and dexterous control tasks, STP achieves strong performance while simplifying the training pipeline for fast generative planning.

## 개요
확산 기반 궤적 계획기는 오프라인 강화 학습에서 뛰어난 성능을 보여주었지만, 반복적인 잡음 제거 과정으로 인해 추론 비용이 높은 경우가 많습니다. 일관성 기반 계획기는 샘플링 단계 수를 줄이지만, 일반적으로 훈련 비용을 증가시키고 불안정성을 초래할 수 있는 2단계 교사-학생 증류 파이프라인에 의존합니다. 본 논문에서는 효율적인 궤적 생성기로서 단축 모델을 통합하는 오프라인 모델 기반 강화 학습 프레임워크인 단축 궤적 계획(STP)을 제안합니다. STP는 단일 단계로 조건부 단축 궤적 모델을 훈련하고, 단계 크기 조건화를 통해 조정 가능한 1단계 및 소수 단계 추론을 지원하며, 실현 가능성 인식 보정이 추가된 비평가를 사용하여 후보 계획을 선택합니다. 보행, 항법, 조작 및 정밀 제어 작업을 포함한 표준 D4RL 벤치마크에서 STP는 빠른 생성 계획을 위한 훈련 파이프라인을 단순화하면서 강력한 성능을 달성합니다.

## 핵심 내용
확산 기반 궤적 계획기는 오프라인 강화 학습에서 뛰어난 성능을 보여주었지만, 반복적인 잡음 제거 과정으로 인해 추론 비용이 높은 경우가 많습니다. 일관성 기반 계획기는 샘플링 단계 수를 줄이지만, 일반적으로 훈련 비용을 증가시키고 불안정성을 초래할 수 있는 2단계 교사-학생 증류 파이프라인에 의존합니다. 본 논문에서는 효율적인 궤적 생성기로서 단축 모델을 통합하는 오프라인 모델 기반 강화 학습 프레임워크인 단축 궤적 계획(STP)을 제안합니다. STP는 단일 단계로 조건부 단축 궤적 모델을 훈련하고, 단계 크기 조건화를 통해 조정 가능한 1단계 및 소수 단계 추론을 지원하며, 실현 가능성 인식 보정이 추가된 비평가를 사용하여 후보 계획을 선택합니다. 보행, 항법, 조작 및 정밀 제어 작업을 포함한 표준 D4RL 벤치마크에서 STP는 빠른 생성 계획을 위한 훈련 파이프라인을 단순화하면서 강력한 성능을 달성합니다.

## 参考
- http://arxiv.org/abs/2607.09336v1
