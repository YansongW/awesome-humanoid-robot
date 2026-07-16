---
$id: ent_paper_kwok_robomonkey_scaling_test_time_s_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models'
  zh: RoboMonkey
  ko: 'RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models'
summary:
  en: 'RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models (RoboMonkey), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Stanford University, UC Berkeley, NVIDIA Research,
    and published at CoRL25.'
  zh: 'RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models (RoboMonkey), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Stanford University, UC Berkeley, NVIDIA Research,
    and published at CoRL25.'
  ko: 'RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models (RoboMonkey), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Stanford University, UC Berkeley, NVIDIA Research,
    and published at CoRL25.'
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
- robomonkey
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.17811v2.
sources:
- id: src_001
  type: paper
  title: 'RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2506.17811
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RoboMonkey source
  url: https://doi.org/10.48550/arXiv.2506.17811
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have demonstrated remarkable capabilities in visuomotor control, yet ensuring their robustness in unstructured real-world environments remains a persistent challenge. In this paper, we investigate test-time scaling through the lens of sampling and verification as means to enhance the robustness and generalization of VLAs. We first demonstrate that the relationship between action error and the number of generated samples follows an exponentiated power law across a range of VLAs, indicating the existence of inference-time scaling laws. Building on these insights, we introduce RoboMonkey, a test-time scaling framework for VLAs. At deployment, RoboMonkey samples a small set of actions from a VLA, applies Gaussian perturbation and majority voting to construct an action proposal distribution, and then uses a Vision Language Model (VLM)-based verifier to select the optimal action. We propose a synthetic data generation pipeline for training such VLM-based action verifiers, and demonstrate that scaling the synthetic dataset consistently improves verification and downstream accuracy. Through extensive simulated and hardware experiments, we show that pairing existing VLAs with RoboMonkey yields significant performance gains, achieving a 25% absolute improvement on out-of-distribution tasks and 9% on in-distribution tasks. Additionally, when adapting to new robot setups, we show that fine-tuning both VLAs and action verifiers yields a 7% performance increase compared to fine-tuning VLAs alone.

## 核心内容
Vision-Language-Action (VLA) models have demonstrated remarkable capabilities in visuomotor control, yet ensuring their robustness in unstructured real-world environments remains a persistent challenge. In this paper, we investigate test-time scaling through the lens of sampling and verification as means to enhance the robustness and generalization of VLAs. We first demonstrate that the relationship between action error and the number of generated samples follows an exponentiated power law across a range of VLAs, indicating the existence of inference-time scaling laws. Building on these insights, we introduce RoboMonkey, a test-time scaling framework for VLAs. At deployment, RoboMonkey samples a small set of actions from a VLA, applies Gaussian perturbation and majority voting to construct an action proposal distribution, and then uses a Vision Language Model (VLM)-based verifier to select the optimal action. We propose a synthetic data generation pipeline for training such VLM-based action verifiers, and demonstrate that scaling the synthetic dataset consistently improves verification and downstream accuracy. Through extensive simulated and hardware experiments, we show that pairing existing VLAs with RoboMonkey yields significant performance gains, achieving a 25% absolute improvement on out-of-distribution tasks and 9% on in-distribution tasks. Additionally, when adapting to new robot setups, we show that fine-tuning both VLAs and action verifiers yields a 7% performance increase compared to fine-tuning VLAs alone.

## 参考
- http://arxiv.org/abs/2506.17811v2

## Overview
Vision-Language-Action (VLA) models have demonstrated remarkable capabilities in visuomotor control, yet ensuring their robustness in unstructured real-world environments remains a persistent challenge. In this paper, we investigate test-time scaling through the lens of sampling and verification as means to enhance the robustness and generalization of VLAs. We first demonstrate that the relationship between action error and the number of generated samples follows an exponentiated power law across a range of VLAs, indicating the existence of inference-time scaling laws. Building on these insights, we introduce RoboMonkey, a test-time scaling framework for VLAs. At deployment, RoboMonkey samples a small set of actions from a VLA, applies Gaussian perturbation and majority voting to construct an action proposal distribution, and then uses a Vision Language Model (VLM)-based verifier to select the optimal action. We propose a synthetic data generation pipeline for training such VLM-based action verifiers, and demonstrate that scaling the synthetic dataset consistently improves verification and downstream accuracy. Through extensive simulated and hardware experiments, we show that pairing existing VLAs with RoboMonkey yields significant performance gains, achieving a 25% absolute improvement on out-of-distribution tasks and 9% on in-distribution tasks. Additionally, when adapting to new robot setups, we show that fine-tuning both VLAs and action verifiers yields a 7% performance increase compared to fine-tuning VLAs alone.

## Content
Vision-Language-Action (VLA) models have demonstrated remarkable capabilities in visuomotor control, yet ensuring their robustness in unstructured real-world environments remains a persistent challenge. In this paper, we investigate test-time scaling through the lens of sampling and verification as means to enhance the robustness and generalization of VLAs. We first demonstrate that the relationship between action error and the number of generated samples follows an exponentiated power law across a range of VLAs, indicating the existence of inference-time scaling laws. Building on these insights, we introduce RoboMonkey, a test-time scaling framework for VLAs. At deployment, RoboMonkey samples a small set of actions from a VLA, applies Gaussian perturbation and majority voting to construct an action proposal distribution, and then uses a Vision Language Model (VLM)-based verifier to select the optimal action. We propose a synthetic data generation pipeline for training such VLM-based action verifiers, and demonstrate that scaling the synthetic dataset consistently improves verification and downstream accuracy. Through extensive simulated and hardware experiments, we show that pairing existing VLAs with RoboMonkey yields significant performance gains, achieving a 25% absolute improvement on out-of-distribution tasks and 9% on in-distribution tasks. Additionally, when adapting to new robot setups, we show that fine-tuning both VLAs and action verifiers yields a 7% performance increase compared to fine-tuning VLAs alone.

## 개요
Vision-Language-Action (VLA) 모델은 시각-운동 제어에서 놀라운 능력을 입증했지만, 구조화되지 않은 실제 환경에서의 견고성을 보장하는 것은 여전히 지속적인 과제로 남아 있습니다. 본 논문에서는 VLA의 견고성과 일반화 능력을 향상시키기 위한 수단으로 샘플링 및 검증을 통한 테스트 시간 스케일링을 조사합니다. 먼저, 다양한 VLA에서 동작 오류와 생성된 샘플 수 간의 관계가 지수화된 멱법칙을 따르며, 이는 추론 시간 스케일링 법칙의 존재를 시사함을 입증합니다. 이러한 통찰을 바탕으로 VLA를 위한 테스트 시간 스케일링 프레임워크인 RoboMonkey를 소개합니다. 배포 시 RoboMonkey는 VLA에서 소수의 동작을 샘플링하고, 가우시안 섭동과 다수결 투표를 적용하여 동작 제안 분포를 구성한 후, Vision Language Model (VLM) 기반 검증기를 사용하여 최적의 동작을 선택합니다. 우리는 이러한 VLM 기반 동작 검증기를 훈련하기 위한 합성 데이터 생성 파이프라인을 제안하고, 합성 데이터셋을 확장하면 검증 및 하위 작업 정확도가 지속적으로 향상됨을 입증합니다. 광범위한 시뮬레이션 및 하드웨어 실험을 통해 기존 VLA와 RoboMonkey를 결합하면 상당한 성능 향상을 얻을 수 있으며, 분포 외 작업에서 25%, 분포 내 작업에서 9%의 절대적 개선을 달성함을 보여줍니다. 또한, 새로운 로봇 설정에 적응할 때 VLA와 동작 검증기를 함께 미세 조정하면 VLA만 미세 조정하는 것보다 7%의 성능 향상을 얻을 수 있음을 입증합니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 시각-운동 제어에서 놀라운 능력을 입증했지만, 구조화되지 않은 실제 환경에서의 견고성을 보장하는 것은 여전히 지속적인 과제로 남아 있습니다. 본 논문에서는 VLA의 견고성과 일반화 능력을 향상시키기 위한 수단으로 샘플링 및 검증을 통한 테스트 시간 스케일링을 조사합니다. 먼저, 다양한 VLA에서 동작 오류와 생성된 샘플 수 간의 관계가 지수화된 멱법칙을 따르며, 이는 추론 시간 스케일링 법칙의 존재를 시사함을 입증합니다. 이러한 통찰을 바탕으로 VLA를 위한 테스트 시간 스케일링 프레임워크인 RoboMonkey를 소개합니다. 배포 시 RoboMonkey는 VLA에서 소수의 동작을 샘플링하고, 가우시안 섭동과 다수결 투표를 적용하여 동작 제안 분포를 구성한 후, Vision Language Model (VLM) 기반 검증기를 사용하여 최적의 동작을 선택합니다. 우리는 이러한 VLM 기반 동작 검증기를 훈련하기 위한 합성 데이터 생성 파이프라인을 제안하고, 합성 데이터셋을 확장하면 검증 및 하위 작업 정확도가 지속적으로 향상됨을 입증합니다. 광범위한 시뮬레이션 및 하드웨어 실험을 통해 기존 VLA와 RoboMonkey를 결합하면 상당한 성능 향상을 얻을 수 있으며, 분포 외 작업에서 25%, 분포 내 작업에서 9%의 절대적 개선을 달성함을 보여줍니다. 또한, 새로운 로봇 설정에 적응할 때 VLA와 동작 검증기를 함께 미세 조정하면 VLA만 미세 조정하는 것보다 7%의 성능 향상을 얻을 수 있음을 입증합니다.
