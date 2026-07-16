---
$id: ent_paper_traversing_narrow_paths_a_two_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Traversing Narrow Paths: A Two-Stage RL Framework for Robust and Safe Humanoid Walking'
  zh: 'Traversing Narrow Paths: A Two-Stage RL Framework for Robust and Safe Humanoid Walking'
  ko: 'Traversing Narrow Paths: A Two-Stage RL Framework for Robust and Safe Humanoid Walking'
summary:
  en: 'Traversing Narrow Paths: A Two-Stage RL Framework for Robust and Safe Humanoid Walking is a 2025 work on locomotion
    for humanoid robots.'
  zh: 'Traversing Narrow Paths: A Two-Stage RL Framework for Robust and Safe Humanoid Walking is a 2025 work on locomotion
    for humanoid robots.'
  ko: 'Traversing Narrow Paths: A Two-Stage RL Framework for Robust and Safe Humanoid Walking is a 2025 work on locomotion
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- traversing_narrow_paths
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.20661v4.
sources:
- id: src_001
  type: paper
  title: 'Traversing Narrow Paths: A Two-Stage RL Framework for Robust and Safe Humanoid Walking (arXiv)'
  url: https://arxiv.org/abs/2508.20661
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Traversing narrow paths is challenging for humanoid robots due to the sparse and safety-critical footholds required. Purely template-based or end-to-end reinforcement learning-based methods suffer from such harsh terrains. This paper proposes a two stage training framework for such narrow path traversing tasks, coupling a template-based foothold planner with a low-level foothold tracker from Stage-I training and a lightweight perception aided foothold modifier from Stage-II training. With the curriculum setup from flat ground to narrow paths across stages, the resulted controller in turn learns to robustly track and safely modify foothold targets to ensure precise foot placement over narrow paths. This framework preserves the interpretability from the physics-based template and takes advantage of the generalization capability from reinforcement learning, resulting in easy sim-to-real transfer. The learned policies outperform purely template-based or reinforcement learning-based baselines in terms of success rate, centerline adherence and safety margins. Validation on a Unitree G1 humanoid robot yields successful traversal of a 0.2m wide and 3m long beam for 20 trials without any failure.

## 核心内容
Traversing narrow paths is challenging for humanoid robots due to the sparse and safety-critical footholds required. Purely template-based or end-to-end reinforcement learning-based methods suffer from such harsh terrains. This paper proposes a two stage training framework for such narrow path traversing tasks, coupling a template-based foothold planner with a low-level foothold tracker from Stage-I training and a lightweight perception aided foothold modifier from Stage-II training. With the curriculum setup from flat ground to narrow paths across stages, the resulted controller in turn learns to robustly track and safely modify foothold targets to ensure precise foot placement over narrow paths. This framework preserves the interpretability from the physics-based template and takes advantage of the generalization capability from reinforcement learning, resulting in easy sim-to-real transfer. The learned policies outperform purely template-based or reinforcement learning-based baselines in terms of success rate, centerline adherence and safety margins. Validation on a Unitree G1 humanoid robot yields successful traversal of a 0.2m wide and 3m long beam for 20 trials without any failure.

## 参考
- http://arxiv.org/abs/2508.20661v4

## Overview
Traversing narrow paths is challenging for humanoid robots due to the sparse and safety-critical footholds required. Purely template-based or end-to-end reinforcement learning-based methods suffer from such harsh terrains. This paper proposes a two-stage training framework for such narrow path traversing tasks, coupling a template-based foothold planner with a low-level foothold tracker from Stage-I training and a lightweight perception-aided foothold modifier from Stage-II training. With the curriculum setup from flat ground to narrow paths across stages, the resulting controller in turn learns to robustly track and safely modify foothold targets to ensure precise foot placement over narrow paths. This framework preserves the interpretability from the physics-based template and takes advantage of the generalization capability from reinforcement learning, resulting in easy sim-to-real transfer. The learned policies outperform purely template-based or reinforcement learning-based baselines in terms of success rate, centerline adherence, and safety margins. Validation on a Unitree G1 humanoid robot yields successful traversal of a 0.2m wide and 3m long beam for 20 trials without any failure.

## Content
Traversing narrow paths is challenging for humanoid robots due to the sparse and safety-critical footholds required. Purely template-based or end-to-end reinforcement learning-based methods suffer from such harsh terrains. This paper proposes a two-stage training framework for such narrow path traversing tasks, coupling a template-based foothold planner with a low-level foothold tracker from Stage-I training and a lightweight perception-aided foothold modifier from Stage-II training. With the curriculum setup from flat ground to narrow paths across stages, the resulting controller in turn learns to robustly track and safely modify foothold targets to ensure precise foot placement over narrow paths. This framework preserves the interpretability from the physics-based template and takes advantage of the generalization capability from reinforcement learning, resulting in easy sim-to-real transfer. The learned policies outperform purely template-based or reinforcement learning-based baselines in terms of success rate, centerline adherence, and safety margins. Validation on a Unitree G1 humanoid robot yields successful traversal of a 0.2m wide and 3m long beam for 20 trials without any failure.

## 개요
인간형 로봇이 좁은 경로를 이동하는 것은 필요한 발판이 드물고 안전에 매우 중요하기 때문에 어려운 과제입니다. 순수 템플릿 기반 또는 종단간 강화 학습 기반 방법은 이러한 험난한 지형에서 성능이 저하됩니다. 본 논문은 이러한 좁은 경로 이동 작업을 위한 2단계 훈련 프레임워크를 제안하며, 1단계 훈련의 템플릿 기반 발판 계획기와 저수준 발판 추적기를 결합하고, 2단계 훈련의 경량 인식 기반 발판 수정기를 결합합니다. 단계별로 평지에서 좁은 경로로 이어지는 커리큘럼 설정을 통해, 결과적으로 얻어진 제어기는 좁은 경로에서 정확한 발 위치를 보장하기 위해 발판 목표를 강건하게 추적하고 안전하게 수정하는 방법을 학습합니다. 이 프레임워크는 물리 기반 템플릿의 해석 가능성을 유지하고 강화 학습의 일반화 능력을 활용하여, 시뮬레이션에서 실제 환경으로의 쉬운 전이를 가능하게 합니다. 학습된 정책은 성공률, 중심선 준수 및 안전 마진 측면에서 순수 템플릿 기반 또는 강화 학습 기반 기준선을 능가합니다. Unitree G1 인간형 로봇에서의 검증을 통해 0.2m 너비, 3m 길이의 빔을 20회 시도 동안 단 한 번의 실패 없이 성공적으로 이동했습니다.

## 핵심 내용
인간형 로봇이 좁은 경로를 이동하는 것은 필요한 발판이 드물고 안전에 매우 중요하기 때문에 어려운 과제입니다. 순수 템플릿 기반 또는 종단간 강화 학습 기반 방법은 이러한 험난한 지형에서 성능이 저하됩니다. 본 논문은 이러한 좁은 경로 이동 작업을 위한 2단계 훈련 프레임워크를 제안하며, 1단계 훈련의 템플릿 기반 발판 계획기와 저수준 발판 추적기를 결합하고, 2단계 훈련의 경량 인식 기반 발판 수정기를 결합합니다. 단계별로 평지에서 좁은 경로로 이어지는 커리큘럼 설정을 통해, 결과적으로 얻어진 제어기는 좁은 경로에서 정확한 발 위치를 보장하기 위해 발판 목표를 강건하게 추적하고 안전하게 수정하는 방법을 학습합니다. 이 프레임워크는 물리 기반 템플릿의 해석 가능성을 유지하고 강화 학습의 일반화 능력을 활용하여, 시뮬레이션에서 실제 환경으로의 쉬운 전이를 가능하게 합니다. 학습된 정책은 성공률, 중심선 준수 및 안전 마진 측면에서 순수 템플릿 기반 또는 강화 학습 기반 기준선을 능가합니다. Unitree G1 인간형 로봇에서의 검증을 통해 0.2m 너비, 3m 길이의 빔을 20회 시도 동안 단 한 번의 실패 없이 성공적으로 이동했습니다.
