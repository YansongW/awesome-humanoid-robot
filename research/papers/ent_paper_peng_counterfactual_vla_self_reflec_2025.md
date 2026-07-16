---
$id: ent_paper_peng_counterfactual_vla_self_reflec_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning'
  zh: Counterfactual VLA
  ko: 'Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning'
summary:
  en: 'Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning (Counterfactual VLA), is a
    2025 large vision-language-action model for robotic manipulation, introduced by NVIDIA, UCLA, Stanford University.'
  zh: 'Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning (Counterfactual VLA), is a
    2025 large vision-language-action model for robotic manipulation, introduced by NVIDIA, UCLA, Stanford University.'
  ko: 'Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning (Counterfactual VLA), is a
    2025 large vision-language-action model for robotic manipulation, introduced by NVIDIA, UCLA, Stanford University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- counterfactual_vla
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.24426v1.
sources:
- id: src_001
  type: paper
  title: 'Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning (arXiv)'
  url: https://arxiv.org/abs/2512.24426
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Counterfactual VLA source
  url: https://doi.org/10.48550/arXiv.2512.24426
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent reasoning-augmented Vision-Language-Action (VLA) models have improved the interpretability of end-to-end autonomous driving by generating intermediate reasoning traces. Yet these models primarily describe what they perceive and intend to do, rarely questioning whether their planned actions are safe or appropriate. This work introduces Counterfactual VLA (CF-VLA), a self-reflective VLA framework that enables the model to reason about and revise its planned actions before execution. CF-VLA first generates time-segmented meta-actions that summarize driving intent, and then performs counterfactual reasoning conditioned on both the meta-actions and the visual context. This step simulates potential outcomes, identifies unsafe behaviors, and outputs corrected meta-actions that guide the final trajectory generation. To efficiently obtain such self-reflective capabilities, we propose a rollout-filter-label pipeline that mines high-value scenes from a base (non-counterfactual) VLA's rollouts and labels counterfactual reasoning traces for subsequent training rounds. Experiments on large-scale driving datasets show that CF-VLA improves trajectory accuracy by up to 17.6%, enhances safety metrics by 20.5%, and exhibits adaptive thinking: it only enables counterfactual reasoning in challenging scenarios. By transforming reasoning traces from one-shot descriptions to causal self-correction signals, CF-VLA takes a step toward self-reflective autonomous driving agents that learn to think before they act.

## 核心内容
Recent reasoning-augmented Vision-Language-Action (VLA) models have improved the interpretability of end-to-end autonomous driving by generating intermediate reasoning traces. Yet these models primarily describe what they perceive and intend to do, rarely questioning whether their planned actions are safe or appropriate. This work introduces Counterfactual VLA (CF-VLA), a self-reflective VLA framework that enables the model to reason about and revise its planned actions before execution. CF-VLA first generates time-segmented meta-actions that summarize driving intent, and then performs counterfactual reasoning conditioned on both the meta-actions and the visual context. This step simulates potential outcomes, identifies unsafe behaviors, and outputs corrected meta-actions that guide the final trajectory generation. To efficiently obtain such self-reflective capabilities, we propose a rollout-filter-label pipeline that mines high-value scenes from a base (non-counterfactual) VLA's rollouts and labels counterfactual reasoning traces for subsequent training rounds. Experiments on large-scale driving datasets show that CF-VLA improves trajectory accuracy by up to 17.6%, enhances safety metrics by 20.5%, and exhibits adaptive thinking: it only enables counterfactual reasoning in challenging scenarios. By transforming reasoning traces from one-shot descriptions to causal self-correction signals, CF-VLA takes a step toward self-reflective autonomous driving agents that learn to think before they act.

## 参考
- http://arxiv.org/abs/2512.24426v1

## Overview
Recent reasoning-augmented Vision-Language-Action (VLA) models have improved the interpretability of end-to-end autonomous driving by generating intermediate reasoning traces. Yet these models primarily describe what they perceive and intend to do, rarely questioning whether their planned actions are safe or appropriate. This work introduces Counterfactual VLA (CF-VLA), a self-reflective VLA framework that enables the model to reason about and revise its planned actions before execution. CF-VLA first generates time-segmented meta-actions that summarize driving intent, and then performs counterfactual reasoning conditioned on both the meta-actions and the visual context. This step simulates potential outcomes, identifies unsafe behaviors, and outputs corrected meta-actions that guide the final trajectory generation. To efficiently obtain such self-reflective capabilities, we propose a rollout-filter-label pipeline that mines high-value scenes from a base (non-counterfactual) VLA's rollouts and labels counterfactual reasoning traces for subsequent training rounds. Experiments on large-scale driving datasets show that CF-VLA improves trajectory accuracy by up to 17.6%, enhances safety metrics by 20.5%, and exhibits adaptive thinking: it only enables counterfactual reasoning in challenging scenarios. By transforming reasoning traces from one-shot descriptions to causal self-correction signals, CF-VLA takes a step toward self-reflective autonomous driving agents that learn to think before they act.

## Content
Recent reasoning-augmented Vision-Language-Action (VLA) models have improved the interpretability of end-to-end autonomous driving by generating intermediate reasoning traces. Yet these models primarily describe what they perceive and intend to do, rarely questioning whether their planned actions are safe or appropriate. This work introduces Counterfactual VLA (CF-VLA), a self-reflective VLA framework that enables the model to reason about and revise its planned actions before execution. CF-VLA first generates time-segmented meta-actions that summarize driving intent, and then performs counterfactual reasoning conditioned on both the meta-actions and the visual context. This step simulates potential outcomes, identifies unsafe behaviors, and outputs corrected meta-actions that guide the final trajectory generation. To efficiently obtain such self-reflective capabilities, we propose a rollout-filter-label pipeline that mines high-value scenes from a base (non-counterfactual) VLA's rollouts and labels counterfactual reasoning traces for subsequent training rounds. Experiments on large-scale driving datasets show that CF-VLA improves trajectory accuracy by up to 17.6%, enhances safety metrics by 20.5%, and exhibits adaptive thinking: it only enables counterfactual reasoning in challenging scenarios. By transforming reasoning traces from one-shot descriptions to causal self-correction signals, CF-VLA takes a step toward self-reflective autonomous driving agents that learn to think before they act.

## 개요
최근 추론 기능이 강화된 Vision-Language-Action (VLA) 모델은 중간 추론 과정을 생성함으로써 엔드투엔드 자율 주행의 해석 가능성을 향상시켰습니다. 그러나 이러한 모델들은 주로 인식한 내용과 의도한 행동을 설명할 뿐, 계획된 행동이 안전하거나 적절한지에 대해 거의 의문을 제기하지 않습니다. 본 연구는 Counterfactual VLA (CF-VLA)를 소개합니다. 이는 자체 반성적 VLA 프레임워크로, 모델이 실행 전에 계획된 행동에 대해 추론하고 수정할 수 있도록 합니다. CF-VLA는 먼저 시간 분할된 메타 액션을 생성하여 주행 의도를 요약한 후, 메타 액션과 시각적 맥락을 조건으로 반사실적 추론을 수행합니다. 이 단계는 잠재적 결과를 시뮬레이션하고, 안전하지 않은 행동을 식별하며, 최종 궤적 생성을 안내하는 수정된 메타 액션을 출력합니다. 이러한 자체 반성 능력을 효율적으로 획득하기 위해, 우리는 기본(비반사실적) VLA의 롤아웃에서 고가치 장면을 발굴하고, 이후 훈련 라운드를 위한 반사실적 추론 과정을 레이블링하는 롤아웃-필터-레이블 파이프라인을 제안합니다. 대규모 주행 데이터셋에 대한 실험 결과, CF-VLA는 궤적 정확도를 최대 17.6% 향상시키고, 안전 지표를 20.5% 개선하며, 적응형 사고를 보여줍니다: 즉, 어려운 시나리오에서만 반사실적 추론을 활성화합니다. 추론 과정을 일회성 설명에서 인과적 자기 수정 신호로 변환함으로써, CF-VLA는 행동하기 전에 생각하는 법을 배우는 자체 반성적 자율 주행 에이전트를 향한 한 걸음을 내딛습니다.

## 핵심 내용
최근 추론 기능이 강화된 Vision-Language-Action (VLA) 모델은 중간 추론 과정을 생성함으로써 엔드투엔드 자율 주행의 해석 가능성을 향상시켰습니다. 그러나 이러한 모델들은 주로 인식한 내용과 의도한 행동을 설명할 뿐, 계획된 행동이 안전하거나 적절한지에 대해 거의 의문을 제기하지 않습니다. 본 연구는 Counterfactual VLA (CF-VLA)를 소개합니다. 이는 자체 반성적 VLA 프레임워크로, 모델이 실행 전에 계획된 행동에 대해 추론하고 수정할 수 있도록 합니다. CF-VLA는 먼저 시간 분할된 메타 액션을 생성하여 주행 의도를 요약한 후, 메타 액션과 시각적 맥락을 조건으로 반사실적 추론을 수행합니다. 이 단계는 잠재적 결과를 시뮬레이션하고, 안전하지 않은 행동을 식별하며, 최종 궤적 생성을 안내하는 수정된 메타 액션을 출력합니다. 이러한 자체 반성 능력을 효율적으로 획득하기 위해, 우리는 기본(비반사실적) VLA의 롤아웃에서 고가치 장면을 발굴하고, 이후 훈련 라운드를 위한 반사실적 추론 과정을 레이블링하는 롤아웃-필터-레이블 파이프라인을 제안합니다. 대규모 주행 데이터셋에 대한 실험 결과, CF-VLA는 궤적 정확도를 최대 17.6% 향상시키고, 안전 지표를 20.5% 개선하며, 적응형 사고를 보여줍니다: 즉, 어려운 시나리오에서만 반사실적 추론을 활성화합니다. 추론 과정을 일회성 설명에서 인과적 자기 수정 신호로 변환함으로써, CF-VLA는 행동하기 전에 생각하는 법을 배우는 자체 반성적 자율 주행 에이전트를 향한 한 걸음을 내딛습니다.
