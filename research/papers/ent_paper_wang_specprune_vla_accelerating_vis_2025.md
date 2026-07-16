---
$id: ent_paper_wang_specprune_vla_accelerating_vis_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning'
  zh: SpecPrune-VLA
  ko: 'SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning'
summary:
  en: 'SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning (SpecPrune-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Shanghai Jiao Tong University, Infinigence-AI,
    SII.'
  zh: 'SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning (SpecPrune-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Shanghai Jiao Tong University, Infinigence-AI,
    SII.'
  ko: 'SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning (SpecPrune-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Shanghai Jiao Tong University, Infinigence-AI,
    SII.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- specprune_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.05614v3.
sources:
- id: src_001
  type: paper
  title: 'SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning (arXiv)'
  url: https://arxiv.org/abs/2509.05614
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SpecPrune-VLA source
  url: https://doi.org/10.48550/arXiv.2509.05614
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Pruning is a typical acceleration technique for compute-bound models by removing computation on unimportant values. Recently, it has been applied to accelerate Vision-Language-Action (VLA) model inference. However, existing acceleration methods focus on local information from the current action step and ignore the global context, leading to >20% success rate drop and limited speedup in some scenarios. In this paper, we point out spatial-temporal consistency in VLA tasks: input images in consecutive steps exhibit high similarity, and propose the key insight that token selection should combine local information with global context of the model. Based on this, we propose SpecPrune-VLA, a training-free, two-level pruning method with heuristic control. (1) Action-level static pruning. We leverage global history and local attention to statically reduce visual tokens per action. (2) Layer-level dynamic pruning. We prune tokens adaptively per layer based on layer-wise importance. (3) Lightweight action-aware controller: We classify actions as coarse- or fine-grained by the speed of the end effector and adjust pruning aggressiveness accordingly. Extensive experiments show that SpecPrune-VLA achieves up to 1.57$\times$ speedup in LIBERO simulation and 1.70$\times$ on real-world tasks, with negligible success rate degradation.

## 核心内容
Pruning is a typical acceleration technique for compute-bound models by removing computation on unimportant values. Recently, it has been applied to accelerate Vision-Language-Action (VLA) model inference. However, existing acceleration methods focus on local information from the current action step and ignore the global context, leading to >20% success rate drop and limited speedup in some scenarios. In this paper, we point out spatial-temporal consistency in VLA tasks: input images in consecutive steps exhibit high similarity, and propose the key insight that token selection should combine local information with global context of the model. Based on this, we propose SpecPrune-VLA, a training-free, two-level pruning method with heuristic control. (1) Action-level static pruning. We leverage global history and local attention to statically reduce visual tokens per action. (2) Layer-level dynamic pruning. We prune tokens adaptively per layer based on layer-wise importance. (3) Lightweight action-aware controller: We classify actions as coarse- or fine-grained by the speed of the end effector and adjust pruning aggressiveness accordingly. Extensive experiments show that SpecPrune-VLA achieves up to 1.57$\times$ speedup in LIBERO simulation and 1.70$\times$ on real-world tasks, with negligible success rate degradation.

## 参考
- http://arxiv.org/abs/2509.05614v3

## Overview
Pruning is a typical acceleration technique for compute-bound models by removing computation on unimportant values. Recently, it has been applied to accelerate Vision-Language-Action (VLA) model inference. However, existing acceleration methods focus on local information from the current action step and ignore the global context, leading to >20% success rate drop and limited speedup in some scenarios. In this paper, we point out spatial-temporal consistency in VLA tasks: input images in consecutive steps exhibit high similarity, and propose the key insight that token selection should combine local information with global context of the model. Based on this, we propose SpecPrune-VLA, a training-free, two-level pruning method with heuristic control. (1) Action-level static pruning. We leverage global history and local attention to statically reduce visual tokens per action. (2) Layer-level dynamic pruning. We prune tokens adaptively per layer based on layer-wise importance. (3) Lightweight action-aware controller: We classify actions as coarse- or fine-grained by the speed of the end effector and adjust pruning aggressiveness accordingly. Extensive experiments show that SpecPrune-VLA achieves up to 1.57$\times$ speedup in LIBERO simulation and 1.70$\times$ on real-world tasks, with negligible success rate degradation.

## Content
Pruning is a typical acceleration technique for compute-bound models by removing computation on unimportant values. Recently, it has been applied to accelerate Vision-Language-Action (VLA) model inference. However, existing acceleration methods focus on local information from the current action step and ignore the global context, leading to >20% success rate drop and limited speedup in some scenarios. In this paper, we point out spatial-temporal consistency in VLA tasks: input images in consecutive steps exhibit high similarity, and propose the key insight that token selection should combine local information with global context of the model. Based on this, we propose SpecPrune-VLA, a training-free, two-level pruning method with heuristic control. (1) Action-level static pruning. We leverage global history and local attention to statically reduce visual tokens per action. (2) Layer-level dynamic pruning. We prune tokens adaptively per layer based on layer-wise importance. (3) Lightweight action-aware controller: We classify actions as coarse- or fine-grained by the speed of the end effector and adjust pruning aggressiveness accordingly. Extensive experiments show that SpecPrune-VLA achieves up to 1.57$\times$ speedup in LIBERO simulation and 1.70$\times$ on real-world tasks, with negligible success rate degradation.

## 개요
Pruning은 중요하지 않은 값에 대한 연산을 제거하여 계산 집약적 모델을 가속화하는 대표적인 기술입니다. 최근에는 Vision-Language-Action(VLA) 모델 추론을 가속화하는 데 적용되었습니다. 그러나 기존 가속 방법은 현재 행동 단계의 지역적 정보에만 집중하고 전역적 맥락을 무시하여, 일부 시나리오에서 20% 이상의 성공률 감소와 제한된 속도 향상을 초래합니다. 본 논문에서는 VLA 작업에서 시공간적 일관성(연속된 단계의 입력 이미지가 높은 유사성을 보임)을 지적하고, 토큰 선택이 지역 정보와 모델의 전역적 맥락을 결합해야 한다는 핵심 통찰을 제안합니다. 이를 바탕으로 훈련이 필요 없고 휴리스틱 제어를 적용한 이중 수준 가지치기 방법인 SpecPrune-VLA를 제안합니다. (1) 행동 수준 정적 가지치기: 전역 기록과 지역 주의를 활용하여 각 행동당 시각적 토큰을 정적으로 줄입니다. (2) 계층 수준 동적 가지치기: 계층별 중요도에 따라 각 계층에서 적응적으로 토큰을 제거합니다. (3) 경량 행동 인식 제어기: 종단 효과기의 속도에 따라 행동을 조립 또는 세밀하게 분류하고, 이에 따라 가지치기 공격성을 조정합니다. 광범위한 실험 결과, SpecPrune-VLA는 LIBERO 시뮬레이션에서 최대 1.57배, 실제 작업에서 최대 1.70배의 속도 향상을 달성하며 성공률 저하는 무시할 수준입니다.

## 핵심 내용
Pruning은 중요하지 않은 값에 대한 연산을 제거하여 계산 집약적 모델을 가속화하는 대표적인 기술입니다. 최근에는 Vision-Language-Action(VLA) 모델 추론을 가속화하는 데 적용되었습니다. 그러나 기존 가속 방법은 현재 행동 단계의 지역적 정보에만 집중하고 전역적 맥락을 무시하여, 일부 시나리오에서 20% 이상의 성공률 감소와 제한된 속도 향상을 초래합니다. 본 논문에서는 VLA 작업에서 시공간적 일관성(연속된 단계의 입력 이미지가 높은 유사성을 보임)을 지적하고, 토큰 선택이 지역 정보와 모델의 전역적 맥락을 결합해야 한다는 핵심 통찰을 제안합니다. 이를 바탕으로 훈련이 필요 없고 휴리스틱 제어를 적용한 이중 수준 가지치기 방법인 SpecPrune-VLA를 제안합니다. (1) 행동 수준 정적 가지치기: 전역 기록과 지역 주의를 활용하여 각 행동당 시각적 토큰을 정적으로 줄입니다. (2) 계층 수준 동적 가지치기: 계층별 중요도에 따라 각 계층에서 적응적으로 토큰을 제거합니다. (3) 경량 행동 인식 제어기: 종단 효과기의 속도에 따라 행동을 조립 또는 세밀하게 분류하고, 이에 따라 가지치기 공격성을 조정합니다. 광범위한 실험 결과, SpecPrune-VLA는 LIBERO 시뮬레이션에서 최대 1.57배, 실제 작업에서 최대 1.70배의 속도 향상을 달성하며 성공률 저하는 무시할 수준입니다.
