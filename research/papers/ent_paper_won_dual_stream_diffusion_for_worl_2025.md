---
$id: ent_paper_won_dual_stream_diffusion_for_worl_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model
  zh: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model
  ko: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model
summary:
  en: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model (Dual-Stream Diffusion for World-Model
    Augmented Vision-Language-Action Model), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by KAIST, RLWRLD.
  zh: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model (Dual-Stream Diffusion for World-Model
    Augmented Vision-Language-Action Model), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by KAIST, RLWRLD.
  ko: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model (Dual-Stream Diffusion for World-Model
    Augmented Vision-Language-Action Model), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by KAIST, RLWRLD.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dual_stream_diffusion_for_worl
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.27607v3.
sources:
- id: src_001
  type: paper
  title: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model (arXiv)
  url: https://arxiv.org/abs/2510.27607
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model source
  url: https://doi.org/10.48550/arXiv.2510.27607
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Augmenting vision-language-action models (VLAs) with world models is promising for robotic policy learning but faces challenges in jointly predicting states and actions due to the modality gap. To address this, we propose DUal-STream diffusion (DUST), a world-model augmented VLA framework featuring a multimodal diffusion transformer that maintains separate modality streams while enabling cross-modal knowledge sharing. In addition, DUST utilizes independent noise perturbations and a decoupled flow matching loss to learn cross-modal causal relationships. We further introduce an asynchronous sampling method for action and vision tokens that enhances performance through inference-time scaling. Experimental results on simulated benchmarks like RoboCasa and GR-1 show that DUST achieves up to 6% gains over state-of-the-art VLA and world-modeling baselines, with inference-time scaling providing an additional 2-5% improvement. In real-world tasks using the Franka Research 3, DUST outperforms baselines by 10% in success rate. Finally, we demonstrate that DUST enables effective transfer learning through both pretraining on action-free videos and joint-training with heterogeneous robot and human datasets.

## 核心内容
Augmenting vision-language-action models (VLAs) with world models is promising for robotic policy learning but faces challenges in jointly predicting states and actions due to the modality gap. To address this, we propose DUal-STream diffusion (DUST), a world-model augmented VLA framework featuring a multimodal diffusion transformer that maintains separate modality streams while enabling cross-modal knowledge sharing. In addition, DUST utilizes independent noise perturbations and a decoupled flow matching loss to learn cross-modal causal relationships. We further introduce an asynchronous sampling method for action and vision tokens that enhances performance through inference-time scaling. Experimental results on simulated benchmarks like RoboCasa and GR-1 show that DUST achieves up to 6% gains over state-of-the-art VLA and world-modeling baselines, with inference-time scaling providing an additional 2-5% improvement. In real-world tasks using the Franka Research 3, DUST outperforms baselines by 10% in success rate. Finally, we demonstrate that DUST enables effective transfer learning through both pretraining on action-free videos and joint-training with heterogeneous robot and human datasets.

## 参考
- http://arxiv.org/abs/2510.27607v3

## Overview
Augmenting vision-language-action models (VLAs) with world models is promising for robotic policy learning but faces challenges in jointly predicting states and actions due to the modality gap. To address this, we propose DUal-STream diffusion (DUST), a world-model augmented VLA framework featuring a multimodal diffusion transformer that maintains separate modality streams while enabling cross-modal knowledge sharing. In addition, DUST utilizes independent noise perturbations and a decoupled flow matching loss to learn cross-modal causal relationships. We further introduce an asynchronous sampling method for action and vision tokens that enhances performance through inference-time scaling. Experimental results on simulated benchmarks like RoboCasa and GR-1 show that DUST achieves up to 6% gains over state-of-the-art VLA and world-modeling baselines, with inference-time scaling providing an additional 2-5% improvement. In real-world tasks using the Franka Research 3, DUST outperforms baselines by 10% in success rate. Finally, we demonstrate that DUST enables effective transfer learning through both pretraining on action-free videos and joint-training with heterogeneous robot and human datasets.

## Content
Augmenting vision-language-action models (VLAs) with world models is promising for robotic policy learning but faces challenges in jointly predicting states and actions due to the modality gap. To address this, we propose DUal-STream diffusion (DUST), a world-model augmented VLA framework featuring a multimodal diffusion transformer that maintains separate modality streams while enabling cross-modal knowledge sharing. In addition, DUST utilizes independent noise perturbations and a decoupled flow matching loss to learn cross-modal causal relationships. We further introduce an asynchronous sampling method for action and vision tokens that enhances performance through inference-time scaling. Experimental results on simulated benchmarks like RoboCasa and GR-1 show that DUST achieves up to 6% gains over state-of-the-art VLA and world-modeling baselines, with inference-time scaling providing an additional 2-5% improvement. In real-world tasks using the Franka Research 3, DUST outperforms baselines by 10% in success rate. Finally, we demonstrate that DUST enables effective transfer learning through both pretraining on action-free videos and joint-training with heterogeneous robot and human datasets.

## 개요
비전-언어-행동 모델(VLA)에 월드 모델을 통합하는 것은 로봇 정책 학습에 유망하지만, 모달리티 차이로 인해 상태와 행동을 공동으로 예측하는 데 어려움이 있습니다. 이를 해결하기 위해, 우리는 DUal-STream diffusion (DUST)을 제안합니다. 이는 개별 모달리티 스트림을 유지하면서 교차 모달 지식 공유를 가능하게 하는 다중 모달 확산 트랜스포머를 특징으로 하는 월드 모델 기반 VLA 프레임워크입니다. 또한, DUST는 독립적인 노이즈 섭동과 분리된 흐름 매칭 손실을 활용하여 교차 모달 인과 관계를 학습합니다. 나아가, 행동 및 비전 토큰에 대한 비동기 샘플링 방법을 도입하여 추론 시간 스케일링을 통해 성능을 향상시킵니다. RoboCasa 및 GR-1과 같은 시뮬레이션 벤치마크에서의 실험 결과, DUST는 최신 VLA 및 월드 모델링 기준선 대비 최대 6%의 성능 향상을 달성했으며, 추론 시간 스케일링은 추가로 2-5%의 개선을 제공합니다. Franka Research 3를 사용한 실제 작업에서 DUST는 기준선 대비 성공률에서 10% 더 우수한 성능을 보였습니다. 마지막으로, DUST가 행동 없는 비디오에 대한 사전 학습과 이종 로봇 및 인간 데이터셋을 사용한 공동 학습을 통해 효과적인 전이 학습을 가능하게 함을 입증합니다.

## 핵심 내용
비전-언어-행동 모델(VLA)에 월드 모델을 통합하는 것은 로봇 정책 학습에 유망하지만, 모달리티 차이로 인해 상태와 행동을 공동으로 예측하는 데 어려움이 있습니다. 이를 해결하기 위해, 우리는 DUal-STream diffusion (DUST)을 제안합니다. 이는 개별 모달리티 스트림을 유지하면서 교차 모달 지식 공유를 가능하게 하는 다중 모달 확산 트랜스포머를 특징으로 하는 월드 모델 기반 VLA 프레임워크입니다. 또한, DUST는 독립적인 노이즈 섭동과 분리된 흐름 매칭 손실을 활용하여 교차 모달 인과 관계를 학습합니다. 나아가, 행동 및 비전 토큰에 대한 비동기 샘플링 방법을 도입하여 추론 시간 스케일링을 통해 성능을 향상시킵니다. RoboCasa 및 GR-1과 같은 시뮬레이션 벤치마크에서의 실험 결과, DUST는 최신 VLA 및 월드 모델링 기준선 대비 최대 6%의 성능 향상을 달성했으며, 추론 시간 스케일링은 추가로 2-5%의 개선을 제공합니다. Franka Research 3를 사용한 실제 작업에서 DUST는 기준선 대비 성공률에서 10% 더 우수한 성능을 보였습니다. 마지막으로, DUST가 행동 없는 비디오에 대한 사전 학습과 이종 로봇 및 인간 데이터셋을 사용한 공동 학습을 통해 효과적인 전이 학습을 가능하게 함을 입증합니다.
