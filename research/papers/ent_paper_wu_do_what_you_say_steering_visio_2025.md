---
$id: ent_paper_wu_do_what_you_say_steering_visio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Do What You Say: Steering Vision-Language-Action Models via Runtime Reasoning-Action Alignment Verification'
  zh: SEAL
  ko: 'Do What You Say: Steering Vision-Language-Action Models via Runtime Reasoning-Action Alignment Verification'
summary:
  en: 'Do What You Say: Steering Vision-Language-Action Models via Runtime Reasoning-Action Alignment Verification (SEAL),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by University of Utah, NVIDIA.'
  zh: 'Do What You Say: Steering Vision-Language-Action Models via Runtime Reasoning-Action Alignment Verification (SEAL),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by University of Utah, NVIDIA.'
  ko: 'Do What You Say: Steering Vision-Language-Action Models via Runtime Reasoning-Action Alignment Verification (SEAL),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by University of Utah, NVIDIA.'
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
- seal
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.16281v2.
sources:
- id: src_001
  type: paper
  title: 'Do What You Say: Steering Vision-Language-Action Models via Runtime Reasoning-Action Alignment Verification (arXiv)'
  url: https://arxiv.org/abs/2510.16281
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SEAL source
  url: https://doi.org/10.48550/arXiv.2510.16281
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Reasoning Vision Language Action (VLA) models improve robotic instruction-following by generating step-by-step textual plans before low-level actions, an approach inspired by Chain-of-Thought (CoT) reasoning in language models. Yet even with a correct textual plan, the generated actions can still miss the intended outcomes in the plan, especially in out-of-distribution (OOD) scenarios. We formalize this phenomenon as a lack of embodied CoT faithfulness, and introduce a training-free, runtime policy steering method for reasoning-action alignment. Given a reasoning VLA's intermediate textual plan, our framework samples multiple candidate action sequences from the same model, predicts their outcomes via simulation, and uses a pre-trained Vision-Language Model (VLM) to select the sequence whose outcome best aligns with the VLA's own textual plan. Only executing action sequences that align with the textual reasoning turns our base VLA's natural action diversity from a source of error into a strength, boosting robustness to semantic and visual OOD perturbations and enabling novel behavior composition without costly re-training. We also contribute a reasoning-annotated extension of LIBERO-100, environment variations tailored for OOD evaluation, and demonstrate up to 15% performance gain over prior work on behavior composition tasks and scales with compute and data diversity. Project Website at: https://yilin-wu98.github.io/steering-reasoning-vla/

## 核心内容
Reasoning Vision Language Action (VLA) models improve robotic instruction-following by generating step-by-step textual plans before low-level actions, an approach inspired by Chain-of-Thought (CoT) reasoning in language models. Yet even with a correct textual plan, the generated actions can still miss the intended outcomes in the plan, especially in out-of-distribution (OOD) scenarios. We formalize this phenomenon as a lack of embodied CoT faithfulness, and introduce a training-free, runtime policy steering method for reasoning-action alignment. Given a reasoning VLA's intermediate textual plan, our framework samples multiple candidate action sequences from the same model, predicts their outcomes via simulation, and uses a pre-trained Vision-Language Model (VLM) to select the sequence whose outcome best aligns with the VLA's own textual plan. Only executing action sequences that align with the textual reasoning turns our base VLA's natural action diversity from a source of error into a strength, boosting robustness to semantic and visual OOD perturbations and enabling novel behavior composition without costly re-training. We also contribute a reasoning-annotated extension of LIBERO-100, environment variations tailored for OOD evaluation, and demonstrate up to 15% performance gain over prior work on behavior composition tasks and scales with compute and data diversity. Project Website at: https://yilin-wu98.github.io/steering-reasoning-vla/

## 参考
- http://arxiv.org/abs/2510.16281v2

## Overview
Reasoning Vision Language Action (VLA) models improve robotic instruction-following by generating step-by-step textual plans before low-level actions, an approach inspired by Chain-of-Thought (CoT) reasoning in language models. Yet even with a correct textual plan, the generated actions can still miss the intended outcomes in the plan, especially in out-of-distribution (OOD) scenarios. We formalize this phenomenon as a lack of embodied CoT faithfulness, and introduce a training-free, runtime policy steering method for reasoning-action alignment. Given a reasoning VLA's intermediate textual plan, our framework samples multiple candidate action sequences from the same model, predicts their outcomes via simulation, and uses a pre-trained Vision-Language Model (VLM) to select the sequence whose outcome best aligns with the VLA's own textual plan. Only executing action sequences that align with the textual reasoning turns our base VLA's natural action diversity from a source of error into a strength, boosting robustness to semantic and visual OOD perturbations and enabling novel behavior composition without costly re-training. We also contribute a reasoning-annotated extension of LIBERO-100, environment variations tailored for OOD evaluation, and demonstrate up to 15% performance gain over prior work on behavior composition tasks and scales with compute and data diversity. Project Website at: https://yilin-wu98.github.io/steering-reasoning-vla/

## Content
Reasoning Vision Language Action (VLA) models improve robotic instruction-following by generating step-by-step textual plans before low-level actions, an approach inspired by Chain-of-Thought (CoT) reasoning in language models. Yet even with a correct textual plan, the generated actions can still miss the intended outcomes in the plan, especially in out-of-distribution (OOD) scenarios. We formalize this phenomenon as a lack of embodied CoT faithfulness, and introduce a training-free, runtime policy steering method for reasoning-action alignment. Given a reasoning VLA's intermediate textual plan, our framework samples multiple candidate action sequences from the same model, predicts their outcomes via simulation, and uses a pre-trained Vision-Language Model (VLM) to select the sequence whose outcome best aligns with the VLA's own textual plan. Only executing action sequences that align with the textual reasoning turns our base VLA's natural action diversity from a source of error into a strength, boosting robustness to semantic and visual OOD perturbations and enabling novel behavior composition without costly re-training. We also contribute a reasoning-annotated extension of LIBERO-100, environment variations tailored for OOD evaluation, and demonstrate up to 15% performance gain over prior work on behavior composition tasks and scales with compute and data diversity. Project Website at: https://yilin-wu98.github.io/steering-reasoning-vla/

## 개요
Reasoning Vision Language Action (VLA) 모델은 저수준 행동 이전에 단계별 텍스트 계획을 생성하여 로봇의 명령 수행 능력을 향상시키며, 이는 언어 모델의 Chain-of-Thought (CoT) 추론에서 영감을 받은 접근 방식입니다. 그러나 올바른 텍스트 계획이 있더라도 생성된 행동은 여전히 계획의 의도된 결과를 놓칠 수 있으며, 특히 분포 외 (OOD) 시나리오에서 그러합니다. 우리는 이 현상을 구현된 CoT 충실성 부족으로 공식화하고, 훈련 없이 실행 중 정책을 조정하는 추론-행동 정렬 방법을 소개합니다. 추론 VLA의 중간 텍스트 계획이 주어지면, 우리 프레임워크는 동일한 모델에서 여러 후보 행동 시퀀스를 샘플링하고, 시뮬레이션을 통해 그 결과를 예측하며, 사전 훈련된 Vision-Language Model (VLM)을 사용하여 VLA 자체의 텍스트 계획과 가장 잘 정렬된 결과를 가진 시퀀스를 선택합니다. 텍스트 추론과 정렬된 행동 시퀀스만 실행함으로써 기본 VLA의 자연스러운 행동 다양성을 오류의 원인에서 강점으로 전환하여 의미적 및 시각적 OOD 교란에 대한 견고성을 높이고, 비용이 많이 드는 재훈련 없이 새로운 행동 구성을 가능하게 합니다. 또한 LIBERO-100의 추론 주석 확장판과 OOD 평가에 맞춤화된 환경 변형을 제공하며, 행동 구성 작업에서 이전 연구 대비 최대 15% 성능 향상을 보여주며, 이는 계산 및 데이터 다양성에 따라 확장됩니다. 프로젝트 웹사이트: https://yilin-wu98.github.io/steering-reasoning-vla/

## 핵심 내용
Reasoning Vision Language Action (VLA) 모델은 저수준 행동 이전에 단계별 텍스트 계획을 생성하여 로봇의 명령 수행 능력을 향상시키며, 이는 언어 모델의 Chain-of-Thought (CoT) 추론에서 영감을 받은 접근 방식입니다. 그러나 올바른 텍스트 계획이 있더라도 생성된 행동은 여전히 계획의 의도된 결과를 놓칠 수 있으며, 특히 분포 외 (OOD) 시나리오에서 그러합니다. 우리는 이 현상을 구현된 CoT 충실성 부족으로 공식화하고, 훈련 없이 실행 중 정책을 조정하는 추론-행동 정렬 방법을 소개합니다. 추론 VLA의 중간 텍스트 계획이 주어지면, 우리 프레임워크는 동일한 모델에서 여러 후보 행동 시퀀스를 샘플링하고, 시뮬레이션을 통해 그 결과를 예측하며, 사전 훈련된 Vision-Language Model (VLM)을 사용하여 VLA 자체의 텍스트 계획과 가장 잘 정렬된 결과를 가진 시퀀스를 선택합니다. 텍스트 추론과 정렬된 행동 시퀀스만 실행함으로써 기본 VLA의 자연스러운 행동 다양성을 오류의 원인에서 강점으로 전환하여 의미적 및 시각적 OOD 교란에 대한 견고성을 높이고, 비용이 많이 드는 재훈련 없이 새로운 행동 구성을 가능하게 합니다. 또한 LIBERO-100의 추론 주석 확장판과 OOD 평가에 맞춤화된 환경 변형을 제공하며, 행동 구성 작업에서 이전 연구 대비 최대 15% 성능 향상을 보여주며, 이는 계산 및 데이터 다양성에 따라 확장됩니다. 프로젝트 웹사이트: https://yilin-wu98.github.io/steering-reasoning-vla/
