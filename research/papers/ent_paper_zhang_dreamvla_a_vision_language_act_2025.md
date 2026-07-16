---
$id: ent_paper_zhang_dreamvla_a_vision_language_act_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge'
  zh: DreamVLA
  ko: 'DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge'
summary:
  en: 'DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge (DreamVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University, Eastern Institute of Technology, Tsinghua
    University, Galbot, Peking University, University of Illinois at Urbana-Champaign, University of Science and Technology
    of China.'
  zh: 'DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge (DreamVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University, Eastern Institute of Technology, Tsinghua
    University, Galbot, Peking University, University of Illinois at Urbana-Champaign, University of Science and Technology
    of China.'
  ko: 'DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge (DreamVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University, Eastern Institute of Technology, Tsinghua
    University, Galbot, Peking University, University of Illinois at Urbana-Champaign, University of Science and Technology
    of China.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dreamvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.04447v3.
sources:
- id: src_001
  type: paper
  title: 'DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge (arXiv)'
  url: https://arxiv.org/abs/2507.04447
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DreamVLA source
  url: https://doi.org/10.48550/arXiv.2507.04447
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent advances in vision-language-action (VLA) models have shown promise in integrating image generation with action prediction to improve generalization and reasoning in robot manipulation. However, existing methods are limited to challenging image-based forecasting, which suffers from redundant information and lacks comprehensive and critical world knowledge, including dynamic, spatial and semantic information. To address these limitations, we propose DreamVLA, a novel VLA framework that integrates comprehensive world knowledge forecasting to enable inverse dynamics modeling, thereby establishing a perception-prediction-action loop for manipulation tasks. Specifically, DreamVLA introduces a dynamic-region-guided world knowledge prediction, integrated with the spatial and semantic cues, which provide compact yet comprehensive representations for action planning. This design aligns with how humans interact with the world by first forming abstract multimodal reasoning chains before acting. To mitigate interference among the dynamic, spatial and semantic information during training, we adopt a block-wise structured attention mechanism that masks their mutual attention, preventing information leakage and keeping each representation clean and disentangled. Moreover, to model the conditional distribution over future actions, we employ a diffusion-based transformer that disentangles action representations from shared latent features. Extensive experiments on both real-world and simulation environments demonstrate that DreamVLA achieves 76.7% success rate on real robot tasks and 4.44 average length on the CALVIN ABC-D benchmarks.

## 核心内容
Recent advances in vision-language-action (VLA) models have shown promise in integrating image generation with action prediction to improve generalization and reasoning in robot manipulation. However, existing methods are limited to challenging image-based forecasting, which suffers from redundant information and lacks comprehensive and critical world knowledge, including dynamic, spatial and semantic information. To address these limitations, we propose DreamVLA, a novel VLA framework that integrates comprehensive world knowledge forecasting to enable inverse dynamics modeling, thereby establishing a perception-prediction-action loop for manipulation tasks. Specifically, DreamVLA introduces a dynamic-region-guided world knowledge prediction, integrated with the spatial and semantic cues, which provide compact yet comprehensive representations for action planning. This design aligns with how humans interact with the world by first forming abstract multimodal reasoning chains before acting. To mitigate interference among the dynamic, spatial and semantic information during training, we adopt a block-wise structured attention mechanism that masks their mutual attention, preventing information leakage and keeping each representation clean and disentangled. Moreover, to model the conditional distribution over future actions, we employ a diffusion-based transformer that disentangles action representations from shared latent features. Extensive experiments on both real-world and simulation environments demonstrate that DreamVLA achieves 76.7% success rate on real robot tasks and 4.44 average length on the CALVIN ABC-D benchmarks.

## 参考
- http://arxiv.org/abs/2507.04447v3

## Overview
Recent advances in vision-language-action (VLA) models have shown promise in integrating image generation with action prediction to improve generalization and reasoning in robot manipulation. However, existing methods are limited to challenging image-based forecasting, which suffers from redundant information and lacks comprehensive and critical world knowledge, including dynamic, spatial and semantic information. To address these limitations, we propose DreamVLA, a novel VLA framework that integrates comprehensive world knowledge forecasting to enable inverse dynamics modeling, thereby establishing a perception-prediction-action loop for manipulation tasks. Specifically, DreamVLA introduces a dynamic-region-guided world knowledge prediction, integrated with the spatial and semantic cues, which provide compact yet comprehensive representations for action planning. This design aligns with how humans interact with the world by first forming abstract multimodal reasoning chains before acting. To mitigate interference among the dynamic, spatial and semantic information during training, we adopt a block-wise structured attention mechanism that masks their mutual attention, preventing information leakage and keeping each representation clean and disentangled. Moreover, to model the conditional distribution over future actions, we employ a diffusion-based transformer that disentangles action representations from shared latent features. Extensive experiments on both real-world and simulation environments demonstrate that DreamVLA achieves 76.7% success rate on real robot tasks and 4.44 average length on the CALVIN ABC-D benchmarks.

## Content
Recent advances in vision-language-action (VLA) models have shown promise in integrating image generation with action prediction to improve generalization and reasoning in robot manipulation. However, existing methods are limited to challenging image-based forecasting, which suffers from redundant information and lacks comprehensive and critical world knowledge, including dynamic, spatial and semantic information. To address these limitations, we propose DreamVLA, a novel VLA framework that integrates comprehensive world knowledge forecasting to enable inverse dynamics modeling, thereby establishing a perception-prediction-action loop for manipulation tasks. Specifically, DreamVLA introduces a dynamic-region-guided world knowledge prediction, integrated with the spatial and semantic cues, which provide compact yet comprehensive representations for action planning. This design aligns with how humans interact with the world by first forming abstract multimodal reasoning chains before acting. To mitigate interference among the dynamic, spatial and semantic information during training, we adopt a block-wise structured attention mechanism that masks their mutual attention, preventing information leakage and keeping each representation clean and disentangled. Moreover, to model the conditional distribution over future actions, we employ a diffusion-based transformer that disentangles action representations from shared latent features. Extensive experiments on both real-world and simulation environments demonstrate that DreamVLA achieves 76.7% success rate on real robot tasks and 4.44 average length on the CALVIN ABC-D benchmarks.

## 개요
최근 시각-언어-행동(VLA) 모델의 발전은 이미지 생성과 행동 예측을 통합하여 로봇 조작에서 일반화 및 추론 능력을 향상시키는 가능성을 보여주었습니다. 그러나 기존 방법은 까다로운 이미지 기반 예측에 국한되어 있으며, 이는 중복 정보로 인해 어려움을 겪고 동적, 공간적 및 의미적 정보를 포함한 포괄적이고 중요한 세계 지식이 부족합니다. 이러한 한계를 해결하기 위해, 우리는 포괄적인 세계 지식 예측을 통합하여 역동역학 모델링을 가능하게 하고, 이를 통해 조작 작업을 위한 인식-예측-행동 루프를 구축하는 새로운 VLA 프레임워크인 DreamVLA를 제안합니다. 구체적으로, DreamVLA는 동적 영역 기반 세계 지식 예측을 도입하며, 이는 공간적 및 의미적 단서와 통합되어 행동 계획을 위한 간결하면서도 포괄적인 표현을 제공합니다. 이 설계는 인간이 행동하기 전에 먼저 추상적인 다중 모달 추론 체인을 형성하는 방식과 일치합니다. 훈련 중 동적, 공간적 및 의미적 정보 간의 간섭을 완화하기 위해, 우리는 블록 단위 구조적 주의 메커니즘을 채택하여 상호 주의를 마스킹함으로써 정보 누출을 방지하고 각 표현을 깔끔하고 분리된 상태로 유지합니다. 또한, 미래 행동에 대한 조건부 분포를 모델링하기 위해, 우리는 확산 기반 트랜스포머를 사용하여 공유 잠재 특징에서 행동 표현을 분리합니다. 실제 환경과 시뮬레이션 환경 모두에서의 광범위한 실험을 통해 DreamVLA는 실제 로봇 작업에서 76.7%의 성공률과 CALVIN ABC-D 벤치마크에서 평균 길이 4.44를 달성함을 입증했습니다.

## 핵심 내용
최근 시각-언어-행동(VLA) 모델의 발전은 이미지 생성과 행동 예측을 통합하여 로봇 조작에서 일반화 및 추론 능력을 향상시키는 가능성을 보여주었습니다. 그러나 기존 방법은 까다로운 이미지 기반 예측에 국한되어 있으며, 이는 중복 정보로 인해 어려움을 겪고 동적, 공간적 및 의미적 정보를 포함한 포괄적이고 중요한 세계 지식이 부족합니다. 이러한 한계를 해결하기 위해, 우리는 포괄적인 세계 지식 예측을 통합하여 역동역학 모델링을 가능하게 하고, 이를 통해 조작 작업을 위한 인식-예측-행동 루프를 구축하는 새로운 VLA 프레임워크인 DreamVLA를 제안합니다. 구체적으로, DreamVLA는 동적 영역 기반 세계 지식 예측을 도입하며, 이는 공간적 및 의미적 단서와 통합되어 행동 계획을 위한 간결하면서도 포괄적인 표현을 제공합니다. 이 설계는 인간이 행동하기 전에 먼저 추상적인 다중 모달 추론 체인을 형성하는 방식과 일치합니다. 훈련 중 동적, 공간적 및 의미적 정보 간의 간섭을 완화하기 위해, 우리는 블록 단위 구조적 주의 메커니즘을 채택하여 상호 주의를 마스킹함으로써 정보 누출을 방지하고 각 표현을 깔끔하고 분리된 상태로 유지합니다. 또한, 미래 행동에 대한 조건부 분포를 모델링하기 위해, 우리는 확산 기반 트랜스포머를 사용하여 공유 잠재 특징에서 행동 표현을 분리합니다. 실제 환경과 시뮬레이션 환경 모두에서의 광범위한 실험을 통해 DreamVLA는 실제 로봇 작업에서 76.7%의 성공률과 CALVIN ABC-D 벤치마크에서 평균 길이 4.44를 달성함을 입증했습니다.
