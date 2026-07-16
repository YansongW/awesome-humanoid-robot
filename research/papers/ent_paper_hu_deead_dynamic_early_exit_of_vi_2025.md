---
$id: ent_paper_hu_deead_dynamic_early_exit_of_vi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DeeAD: Dynamic Early Exit of Vision-Language Action for Efficient Autonomous Driving'
  zh: DeeAD
  ko: 'DeeAD: Dynamic Early Exit of Vision-Language Action for Efficient Autonomous Driving'
summary:
  en: 'DeeAD: Dynamic Early Exit of Vision-Language Action for Efficient Autonomous Driving (DeeAD), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by City University of Hongkong, Mohamed bin Zayed University of Artificial
    Intelligence.'
  zh: 'DeeAD: Dynamic Early Exit of Vision-Language Action for Efficient Autonomous Driving (DeeAD), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by City University of Hongkong, Mohamed bin Zayed University of Artificial
    Intelligence.'
  ko: 'DeeAD: Dynamic Early Exit of Vision-Language Action for Efficient Autonomous Driving (DeeAD), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by City University of Hongkong, Mohamed bin Zayed University of Artificial
    Intelligence.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- deead
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.20720v1.
sources:
- id: src_001
  type: paper
  title: 'DeeAD: Dynamic Early Exit of Vision-Language Action for Efficient Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2511.20720
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DeeAD source
  url: https://doi.org/10.48550/arXiv.2511.20720
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language Action (VLA) models unify perception, reasoning, and trajectory generation for autonomous driving, but suffer from significant inference latency due to deep transformer stacks. We present DeeAD, a training-free, action-guided early-exit framework that accelerates VLA planning by evaluating the physical feasibility of intermediate trajectories. Instead of relying on confidence scores, DeeAD terminates inference when predicted trajectories align with lightweight planning priors (e.g., Navigation or Low-precision Planning) within a tolerable deviation (<2m). To improve efficiency, we introduce a multi-hop controller that adaptively skips redundant layers based on the change rate of scores. DeeAD integrates into existing VLA models, such as ORION, without requiring retraining. Experiments on the Bench2Drive benchmark demonstrate up to 28% transformer-layer sparsity and 29% latency reduction, while preserving planning quality and safety.

## 核心内容
Vision-Language Action (VLA) models unify perception, reasoning, and trajectory generation for autonomous driving, but suffer from significant inference latency due to deep transformer stacks. We present DeeAD, a training-free, action-guided early-exit framework that accelerates VLA planning by evaluating the physical feasibility of intermediate trajectories. Instead of relying on confidence scores, DeeAD terminates inference when predicted trajectories align with lightweight planning priors (e.g., Navigation or Low-precision Planning) within a tolerable deviation (<2m). To improve efficiency, we introduce a multi-hop controller that adaptively skips redundant layers based on the change rate of scores. DeeAD integrates into existing VLA models, such as ORION, without requiring retraining. Experiments on the Bench2Drive benchmark demonstrate up to 28% transformer-layer sparsity and 29% latency reduction, while preserving planning quality and safety.

## 参考
- http://arxiv.org/abs/2511.20720v1

## Overview
Vision-Language Action (VLA) models unify perception, reasoning, and trajectory generation for autonomous driving, but suffer from significant inference latency due to deep transformer stacks. We present DeeAD, a training-free, action-guided early-exit framework that accelerates VLA planning by evaluating the physical feasibility of intermediate trajectories. Instead of relying on confidence scores, DeeAD terminates inference when predicted trajectories align with lightweight planning priors (e.g., Navigation or Low-precision Planning) within a tolerable deviation (<2m). To improve efficiency, we introduce a multi-hop controller that adaptively skips redundant layers based on the change rate of scores. DeeAD integrates into existing VLA models, such as ORION, without requiring retraining. Experiments on the Bench2Drive benchmark demonstrate up to 28% transformer-layer sparsity and 29% latency reduction, while preserving planning quality and safety.

## Content
Vision-Language Action (VLA) models unify perception, reasoning, and trajectory generation for autonomous driving, but suffer from significant inference latency due to deep transformer stacks. We present DeeAD, a training-free, action-guided early-exit framework that accelerates VLA planning by evaluating the physical feasibility of intermediate trajectories. Instead of relying on confidence scores, DeeAD terminates inference when predicted trajectories align with lightweight planning priors (e.g., Navigation or Low-precision Planning) within a tolerable deviation (<2m). To improve efficiency, we introduce a multi-hop controller that adaptively skips redundant layers based on the change rate of scores. DeeAD integrates into existing VLA models, such as ORION, without requiring retraining. Experiments on the Bench2Drive benchmark demonstrate up to 28% transformer-layer sparsity and 29% latency reduction, while preserving planning quality and safety.

## 개요
Vision-Language Action (VLA) 모델은 자율 주행을 위한 인식, 추론 및 궤적 생성을 통합하지만, 깊은 트랜스포머 스택으로 인해 상당한 추론 지연 시간이 발생합니다. 우리는 중간 궤적의 물리적 실현 가능성을 평가하여 VLA 계획을 가속화하는 훈련 없는 행동 기반 조기 종료 프레임워크인 DeeAD를 제시합니다. DeeAD는 신뢰 점수에 의존하는 대신, 예측된 궤적이 허용 가능한 편차(<2m) 내에서 경량 계획 사전(예: 내비게이션 또는 저정밀 계획)과 일치할 때 추론을 종료합니다. 효율성을 높이기 위해, 점수 변화율에 따라 중복 레이어를 적응적으로 건너뛰는 다중 홉 컨트롤러를 도입합니다. DeeAD는 재훈련 없이 ORION과 같은 기존 VLA 모델에 통합됩니다. Bench2Drive 벤치마크 실험 결과, 계획 품질과 안전성을 유지하면서 최대 28%의 트랜스포머 레이어 희소성과 29%의 지연 시간 감소를 보여줍니다.

## 핵심 내용
Vision-Language Action (VLA) 모델은 자율 주행을 위한 인식, 추론 및 궤적 생성을 통합하지만, 깊은 트랜스포머 스택으로 인해 상당한 추론 지연 시간이 발생합니다. 우리는 중간 궤적의 물리적 실현 가능성을 평가하여 VLA 계획을 가속화하는 훈련 없는 행동 기반 조기 종료 프레임워크인 DeeAD를 제시합니다. DeeAD는 신뢰 점수에 의존하는 대신, 예측된 궤적이 허용 가능한 편차(<2m) 내에서 경량 계획 사전(예: 내비게이션 또는 저정밀 계획)과 일치할 때 추론을 종료합니다. 효율성을 높이기 위해, 점수 변화율에 따라 중복 레이어를 적응적으로 건너뛰는 다중 홉 컨트롤러를 도입합니다. DeeAD는 재훈련 없이 ORION과 같은 기존 VLA 모델에 통합됩니다. Bench2Drive 벤치마크 실험 결과, 계획 품질과 안전성을 유지하면서 최대 28%의 트랜스포머 레이어 희소성과 29%의 지연 시간 감소를 보여줍니다.
