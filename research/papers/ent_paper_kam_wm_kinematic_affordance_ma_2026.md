---
$id: ent_paper_kam_wm_kinematic_affordance_ma_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'KAM-WM: Kinematic Affordance Maps from Latent World Models for Robot Manipulation'
  zh: 'KAM-WM: Kinematic Affordance Maps from Latent World Models for Robot Manipulation'
  ko: 'KAM-WM: Kinematic Affordance Maps from Latent World Models for Robot Manipulation'
summary:
  en: 'arXiv:2607.04652v1 Announce Type: new Abstract: Learning manipulation from few demonstrations requires visual priors
    that capture not only where to interact, but also how the interaction should begin; static priors such as segmentation
    masks encode only the former. We present KAM-WM, a framework that extracts a coarse directional interaction cue from a
    frozen latent video world model without rollout or world-model fine-tuning. KAM-WM queries a Flow Matching image-to-video
    backbone once and interprets its single-step latent velocity as a Kinematic Affordance Map (KAM), which provides task-conditioned
    interaction regions and coarse motion structure. A lightweight Perceiver compresses KAM into tokens that condition a diffusion
    policy together with RGB observations and proprioception. Across LIBERO and RoboTwin2.0, KAM-WM reaches 90.6% average
    success on LIBERO and achieves 65.7% and 22.4% success rates in the Easy and Hard settings on RoboTwin2.0, respectively.
    Controlled comparisons against a zero-order mask prior suggest that part of the gains comes from directional information
    beyond spatial localization alone. These results indicate that, in the evaluated settings, a frozen video model can provide
    a useful first-order visual prior for control without the test-time cost of future rollout.'
  zh: 'arXiv:2607.04652v1 Announce Type: new Abstract: Learning manipulation from few demonstrations requires visual priors
    that capture not only where to interact, but also how the interaction should begin; static priors such as segmentation
    masks encode only the former. We present KAM-WM, a framework that extracts a coarse directional interaction cue from a
    frozen latent video world model without rollout or world-model fine-tuning. KAM-WM queries a Flow Matching image-to-video
    backbone once and interprets its single-step latent velocity as a Kinematic Affordance Map (KAM), which provides task-conditioned
    interaction regions and coarse motion structure. A lightweight Perceiver compresses KAM into tokens that condition a diffusion
    policy together with RGB observations and proprioception. Across LIBERO and RoboTwin2.0, KAM-WM reaches 90.6% average
    success on LIBERO and achieves 65.7% and 22.4% success rates in the Easy and Hard settings on RoboTwin2.0, respectively.
    Controlled comparisons against a zero-order mask prior suggest that part of the gains comes from directional information
    beyond spatial localization alone. These results indicate that, in the evaluated settings, a frozen video model can provide
    a useful first-order visual prior for control without the test-time cost of future rollout.'
  ko: 'arXiv:2607.04652v1 Announce Type: new Abstract: Learning manipulation from few demonstrations requires visual priors
    that capture not only where to interact, but also how the interaction should begin; static priors such as segmentation
    masks encode only the former. We present KAM-WM, a framework that extracts a coarse directional interaction cue from a
    frozen latent video world model without rollout or world-model fine-tuning. KAM-WM queries a Flow Matching image-to-video
    backbone once and interprets its single-step latent velocity as a Kinematic Affordance Map (KAM), which provides task-conditioned
    interaction regions and coarse motion structure. A lightweight Perceiver compresses KAM into tokens that condition a diffusion
    policy together with RGB observations and proprioception. Across LIBERO and RoboTwin2.0, KAM-WM reaches 90.6% average
    success on LIBERO and achieves 65.7% and 22.4% success rates in the Easy and Hard settings on RoboTwin2.0, respectively.
    Controlled comparisons against a zero-order mask prior suggest that part of the gains comes from directional information
    beyond spatial localization alone. These results indicate that, in the evaluated settings, a frozen video model can provide
    a useful first-order visual prior for control without the test-time cost of future rollout.'
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
- kam_wm
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04652v1.
sources:
- id: src_001
  type: paper
  title: 'KAM-WM: Kinematic Affordance Maps from Latent World Models for Robot Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.04652
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Learning manipulation from few demonstrations requires visual priors that capture not only where to interact, but also how the interaction should begin; static priors such as segmentation masks encode only the former. We present KAM-WM, a framework that extracts a coarse directional interaction cue from a frozen latent video world model without rollout or world-model fine-tuning. KAM-WM queries a Flow Matching image-to-video backbone once and interprets its single-step latent velocity as a Kinematic Affordance Map (KAM), which provides task-conditioned interaction regions and coarse motion structure. A lightweight Perceiver compresses KAM into tokens that condition a diffusion policy together with RGB observations and proprioception. Across LIBERO and RoboTwin2.0, KAM-WM reaches 90.6% average success on LIBERO and achieves 65.7% and 22.4% success rates in the Easy and Hard settings on RoboTwin2.0, respectively. Controlled comparisons against a zero-order mask prior suggest that part of the gains comes from directional information beyond spatial localization alone. These results indicate that, in the evaluated settings, a frozen video model can provide a useful first-order visual prior for control without the test-time cost of future rollout.

## 核心内容
Learning manipulation from few demonstrations requires visual priors that capture not only where to interact, but also how the interaction should begin; static priors such as segmentation masks encode only the former. We present KAM-WM, a framework that extracts a coarse directional interaction cue from a frozen latent video world model without rollout or world-model fine-tuning. KAM-WM queries a Flow Matching image-to-video backbone once and interprets its single-step latent velocity as a Kinematic Affordance Map (KAM), which provides task-conditioned interaction regions and coarse motion structure. A lightweight Perceiver compresses KAM into tokens that condition a diffusion policy together with RGB observations and proprioception. Across LIBERO and RoboTwin2.0, KAM-WM reaches 90.6% average success on LIBERO and achieves 65.7% and 22.4% success rates in the Easy and Hard settings on RoboTwin2.0, respectively. Controlled comparisons against a zero-order mask prior suggest that part of the gains comes from directional information beyond spatial localization alone. These results indicate that, in the evaluated settings, a frozen video model can provide a useful first-order visual prior for control without the test-time cost of future rollout.

## 参考
- http://arxiv.org/abs/2607.04652v1

## Overview
Learning manipulation from few demonstrations requires visual priors that capture not only where to interact, but also how the interaction should begin; static priors such as segmentation masks encode only the former. We present KAM-WM, a framework that extracts a coarse directional interaction cue from a frozen latent video world model without rollout or world-model fine-tuning. KAM-WM queries a Flow Matching image-to-video backbone once and interprets its single-step latent velocity as a Kinematic Affordance Map (KAM), which provides task-conditioned interaction regions and coarse motion structure. A lightweight Perceiver compresses KAM into tokens that condition a diffusion policy together with RGB observations and proprioception. Across LIBERO and RoboTwin2.0, KAM-WM reaches 90.6% average success on LIBERO and achieves 65.7% and 22.4% success rates in the Easy and Hard settings on RoboTwin2.0, respectively. Controlled comparisons against a zero-order mask prior suggest that part of the gains comes from directional information beyond spatial localization alone. These results indicate that, in the evaluated settings, a frozen video model can provide a useful first-order visual prior for control without the test-time cost of future rollout.

## Content
Learning manipulation from few demonstrations requires visual priors that capture not only where to interact, but also how the interaction should begin; static priors such as segmentation masks encode only the former. We present KAM-WM, a framework that extracts a coarse directional interaction cue from a frozen latent video world model without rollout or world-model fine-tuning. KAM-WM queries a Flow Matching image-to-video backbone once and interprets its single-step latent velocity as a Kinematic Affordance Map (KAM), which provides task-conditioned interaction regions and coarse motion structure. A lightweight Perceiver compresses KAM into tokens that condition a diffusion policy together with RGB observations and proprioception. Across LIBERO and RoboTwin2.0, KAM-WM reaches 90.6% average success on LIBERO and achieves 65.7% and 22.4% success rates in the Easy and Hard settings on RoboTwin2.0, respectively. Controlled comparisons against a zero-order mask prior suggest that part of the gains comes from directional information beyond spatial localization alone. These results indicate that, in the evaluated settings, a frozen video model can provide a useful first-order visual prior for control without the test-time cost of future rollout.

## 개요
소수의 시연으로부터 조작을 학습하려면 상호작용 위치뿐만 아니라 상호작용이 어떻게 시작되어야 하는지도 포착하는 시각적 사전 지식이 필요합니다. 분할 마스크와 같은 정적 사전 지식은 전자만 인코딩합니다. 본 논문에서는 롤아웃이나 월드 모델 미세 조정 없이 고정된 잠재 비디오 월드 모델로부터 대략적인 방향성 상호작용 단서를 추출하는 프레임워크인 KAM-WM을 제시합니다. KAM-WM은 Flow Matching 이미지-비디오 백본을 한 번 쿼리하고, 단일 단계 잠재 속도를 운동학적 어포던스 맵(KAM)으로 해석하여 작업 조건화된 상호작용 영역과 대략적인 움직임 구조를 제공합니다. 경량화된 Perceiver는 KAM을 토큰으로 압축하여 RGB 관측값 및 고유 감각과 함께 확산 정책을 조건화합니다. LIBERO 및 RoboTwin2.0에서 KAM-WM은 LIBERO에서 평균 90.6%의 성공률을 달성하고, RoboTwin2.0의 Easy 및 Hard 설정에서 각각 65.7% 및 22.4%의 성공률을 기록했습니다. 0차 마스크 사전 지식과의 통제된 비교는 이러한 성능 향상의 일부가 공간적 위치 파악을 넘어선 방향 정보에서 비롯됨을 시사합니다. 이러한 결과는 평가된 설정에서 고정된 비디오 모델이 미래 롤아웃의 테스트 시간 비용 없이 제어에 유용한 1차 시각적 사전 지식을 제공할 수 있음을 나타냅니다.

## 핵심 내용
소수의 시연으로부터 조작을 학습하려면 상호작용 위치뿐만 아니라 상호작용이 어떻게 시작되어야 하는지도 포착하는 시각적 사전 지식이 필요합니다. 분할 마스크와 같은 정적 사전 지식은 전자만 인코딩합니다. 본 논문에서는 롤아웃이나 월드 모델 미세 조정 없이 고정된 잠재 비디오 월드 모델로부터 대략적인 방향성 상호작용 단서를 추출하는 프레임워크인 KAM-WM을 제시합니다. KAM-WM은 Flow Matching 이미지-비디오 백본을 한 번 쿼리하고, 단일 단계 잠재 속도를 운동학적 어포던스 맵(KAM)으로 해석하여 작업 조건화된 상호작용 영역과 대략적인 움직임 구조를 제공합니다. 경량화된 Perceiver는 KAM을 토큰으로 압축하여 RGB 관측값 및 고유 감각과 함께 확산 정책을 조건화합니다. LIBERO 및 RoboTwin2.0에서 KAM-WM은 LIBERO에서 평균 90.6%의 성공률을 달성하고, RoboTwin2.0의 Easy 및 Hard 설정에서 각각 65.7% 및 22.4%의 성공률을 기록했습니다. 0차 마스크 사전 지식과의 통제된 비교는 이러한 성능 향상의 일부가 공간적 위치 파악을 넘어선 방향 정보에서 비롯됨을 시사합니다. 이러한 결과는 평가된 설정에서 고정된 비디오 모델이 미래 롤아웃의 테스트 시간 비용 없이 제어에 유용한 1차 시각적 사전 지식을 제공할 수 있음을 나타냅니다.
