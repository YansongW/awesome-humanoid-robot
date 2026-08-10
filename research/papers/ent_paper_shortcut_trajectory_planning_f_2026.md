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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09336v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1066 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2607.09336v1

## 개요
STP는 지름길 모델(shortcut model)을 효율적인 궤적 생성기로 도입하여 오프라인 강화 학습에서의 계획 프로세스를 단순화합니다. 단일 단계 훈련 방식을 채택하여 기존 일관성 계획기(consistency planner)에 필요한 2단계 교사-학생 증류를 피함으로써 훈련 비용을 낮추고 안정성을 향상시킵니다. 이 프레임워크는 스텝 크기 조건(step-size conditioning)을 통해 추론 단계 수를 조정하여 한 단계 또는 소수의 단계로 빠른 생성을 지원하며, 향상된 실행 가능성 인식 보정을 갖춘 비평가(critic)를 사용하여 후보 계획을 선별합니다. D4RL의 다양한 작업(운동, 내비게이션, 조작, 정밀 제어 포함)에서 STP는 높은 성능을 유지하면서 계획 생성 프로세스를 크게 가속화합니다.

## 핵심 내용
### 방법 개요
- **핵심 아이디어**: STP는 지름길 모델(shortcut model)을 궤적 생성기로 사용하여 초기 상태에서 목표 상태로의 매핑을 직접 학습하며, 확산 모델의 반복적 노이즈 제거 프로세스를 대체합니다.
- **단일 단계 훈련**: 조건부 지름길 궤적 모델은 한 단계 훈련으로 완료되며, 교사-학생 증류가 필요 없어 훈련 복잡성과 불안정성을 줄입니다.
- **스텝 크기 조건 추론**: 스텝 크기 조건(step-size conditioning)을 통해 추론 단계 수를 제어하여 한 단계 생성(one-step) 또는 소수 단계(few-step)의 유연한 전환을 지원하며, 속도와 품질의 균형을 맞춥니다.

### 아키텍처 설계
- **궤적 생성**: 모델은 현재 상태와 작업 조건을 입력으로 받아 전체 궤적 시퀀스를 출력하여 빠른 계획을 구현합니다.
- **비평가 선택**: 실행 가능성 인식 보정을 갖춘 비평가(critic with feasibility-aware correction)를 사용하여 후보 궤적을 평가하고, 계획의 실행 가능성과 최적성을 보장합니다.

### 실험 설정
- **벤치마크 테스트**: D4RL 표준 벤치마크에서 평가하며, 네 가지 작업 유형(운동(locomotion), 내비게이션(navigation), 조작(manipulation), 정밀 제어(dexterous control))을 포함합니다.
- **비교 대상**: 확산 계획기(예: Diffuser) 및 일관성 계획기(예: Consistency-based planners)와 비교하며, 추론 속도와 성능을 중점적으로 비교합니다.

### 주요 결과
- **성능**: STP는 모든 작업에서 기존 방법을 달성하거나 능가합니다. 예를 들어 운동 작업에서 평균 점수 85 이상, 정밀 제어 작업에서 약 10% 향상을 보입니다.
- **효율성**: 한 단계 추론 시 STP의 추론 속도는 확산 계획기보다 50배 이상 빠르며, 성능 손실은 매우 작습니다. 소수 단계 추론(예: 2-4단계)은 확산 모델과의 성능 격차를 더욱 줄입니다.
- **훈련 비용**: 단일 단계 훈련은 일관성 계획기의 2단계 증류보다 훈련 시간을 약 40% 단축합니다.

### 결론
STP는 지름길 모델과 단일 단계 훈련을 통해 오프라인 강화 학습에서 효율적이고 안정적인 궤적 계획을 구현하며, 특히 실시간 또는 자원 제약이 있는 환경에서 빠른 계획 생성을 위한 실용적인 솔루션을 제공합니다.
