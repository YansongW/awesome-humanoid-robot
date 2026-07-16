---
$id: ent_paper_zhang_ego_centric_predictive_model_c_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Ego-centric Predictive Model Conditioned on Hand Trajectories
  zh: Ego-PM
  ko: Ego-centric Predictive Model Conditioned on Hand Trajectories
summary:
  en: Ego-centric Predictive Model Conditioned on Hand Trajectories (Ego-PM), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Show Lab, National University of Singapore.
  zh: Ego-centric Predictive Model Conditioned on Hand Trajectories (Ego-PM), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Show Lab, National University of Singapore.
  ko: Ego-centric Predictive Model Conditioned on Hand Trajectories (Ego-PM), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Show Lab, National University of Singapore.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ego_pm
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.19852v2.
sources:
- id: src_001
  type: paper
  title: Ego-centric Predictive Model Conditioned on Hand Trajectories (arXiv)
  url: https://arxiv.org/abs/2508.19852
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Ego-PM source
  url: https://doi.org/10.48550/arXiv.2508.19852
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In egocentric scenarios, anticipating both the next action and its visual outcome is essential for understanding human-object interactions and for enabling robotic planning. However, existing paradigms fall short of jointly modeling these aspects. Vision-Language-Action (VLA) models focus on action prediction but lack explicit modeling of how actions influence the visual scene, while video prediction models generate future frames without conditioning on specific actions, often resulting in implausible or contextually inconsistent outcomes. To bridge this gap, we propose a unified two-stage predictive framework that jointly models action and visual future in egocentric scenarios, conditioned on hand trajectories. In the first stage, we perform consecutive state modeling to process heterogeneous inputs (visual observations, language, and action history) and explicitly predict future hand trajectories. In the second stage, we introduce causal cross-attention to fuse multi-modal cues, leveraging inferred action signals to guide an image-based Latent Diffusion Model (LDM) for frame-by-frame future video generation. Our approach is the first unified model designed to handle both egocentric human activity understanding and robotic manipulation tasks, providing explicit predictions of both upcoming actions and their visual consequences. Extensive experiments on Ego4D, BridgeData, and RLBench demonstrate that our method outperforms state-of-the-art baselines in both action prediction and future video synthesis.

## 核心内容
In egocentric scenarios, anticipating both the next action and its visual outcome is essential for understanding human-object interactions and for enabling robotic planning. However, existing paradigms fall short of jointly modeling these aspects. Vision-Language-Action (VLA) models focus on action prediction but lack explicit modeling of how actions influence the visual scene, while video prediction models generate future frames without conditioning on specific actions, often resulting in implausible or contextually inconsistent outcomes. To bridge this gap, we propose a unified two-stage predictive framework that jointly models action and visual future in egocentric scenarios, conditioned on hand trajectories. In the first stage, we perform consecutive state modeling to process heterogeneous inputs (visual observations, language, and action history) and explicitly predict future hand trajectories. In the second stage, we introduce causal cross-attention to fuse multi-modal cues, leveraging inferred action signals to guide an image-based Latent Diffusion Model (LDM) for frame-by-frame future video generation. Our approach is the first unified model designed to handle both egocentric human activity understanding and robotic manipulation tasks, providing explicit predictions of both upcoming actions and their visual consequences. Extensive experiments on Ego4D, BridgeData, and RLBench demonstrate that our method outperforms state-of-the-art baselines in both action prediction and future video synthesis.

## 参考
- http://arxiv.org/abs/2508.19852v2

## Overview
In egocentric scenarios, anticipating both the next action and its visual outcome is essential for understanding human-object interactions and for enabling robotic planning. However, existing paradigms fall short of jointly modeling these aspects. Vision-Language-Action (VLA) models focus on action prediction but lack explicit modeling of how actions influence the visual scene, while video prediction models generate future frames without conditioning on specific actions, often resulting in implausible or contextually inconsistent outcomes. To bridge this gap, we propose a unified two-stage predictive framework that jointly models action and visual future in egocentric scenarios, conditioned on hand trajectories. In the first stage, we perform consecutive state modeling to process heterogeneous inputs (visual observations, language, and action history) and explicitly predict future hand trajectories. In the second stage, we introduce causal cross-attention to fuse multi-modal cues, leveraging inferred action signals to guide an image-based Latent Diffusion Model (LDM) for frame-by-frame future video generation. Our approach is the first unified model designed to handle both egocentric human activity understanding and robotic manipulation tasks, providing explicit predictions of both upcoming actions and their visual consequences. Extensive experiments on Ego4D, BridgeData, and RLBench demonstrate that our method outperforms state-of-the-art baselines in both action prediction and future video synthesis.

## Content
In egocentric scenarios, anticipating both the next action and its visual outcome is essential for understanding human-object interactions and for enabling robotic planning. However, existing paradigms fall short of jointly modeling these aspects. Vision-Language-Action (VLA) models focus on action prediction but lack explicit modeling of how actions influence the visual scene, while video prediction models generate future frames without conditioning on specific actions, often resulting in implausible or contextually inconsistent outcomes. To bridge this gap, we propose a unified two-stage predictive framework that jointly models action and visual future in egocentric scenarios, conditioned on hand trajectories. In the first stage, we perform consecutive state modeling to process heterogeneous inputs (visual observations, language, and action history) and explicitly predict future hand trajectories. In the second stage, we introduce causal cross-attention to fuse multi-modal cues, leveraging inferred action signals to guide an image-based Latent Diffusion Model (LDM) for frame-by-frame future video generation. Our approach is the first unified model designed to handle both egocentric human activity understanding and robotic manipulation tasks, providing explicit predictions of both upcoming actions and their visual consequences. Extensive experiments on Ego4D, BridgeData, and RLBench demonstrate that our method outperforms state-of-the-art baselines in both action prediction and future video synthesis.

## 개요
자기중심적 시나리오에서 다음 행동과 그 시각적 결과를 모두 예측하는 것은 인간-객체 상호작용을 이해하고 로봇 계획을 가능하게 하는 데 필수적입니다. 그러나 기존 패러다임은 이러한 측면을 공동으로 모델링하는 데 부족합니다. Vision-Language-Action(VLA) 모델은 행동 예측에 초점을 맞추지만 행동이 시각적 장면에 미치는 영향을 명시적으로 모델링하지 않으며, 비디오 예측 모델은 특정 행동에 조건화되지 않고 미래 프레임을 생성하여 종종 비현실적이거나 맥락적으로 일관성 없는 결과를 초래합니다. 이러한 격차를 해소하기 위해, 우리는 손 궤적에 조건화된 자기중심적 시나리오에서 행동과 시각적 미래를 공동으로 모델링하는 통합된 2단계 예측 프레임워크를 제안합니다. 첫 번째 단계에서는 연속 상태 모델링을 수행하여 이질적인 입력(시각적 관찰, 언어, 행동 이력)을 처리하고 미래 손 궤적을 명시적으로 예측합니다. 두 번째 단계에서는 인과적 교차 주의를 도입하여 다중 모달 단서를 융합하고, 추론된 행동 신호를 활용하여 이미지 기반 잠재 확산 모델(LDM)을 안내하여 프레임별 미래 비디오를 생성합니다. 우리의 접근 방식은 자기중심적 인간 활동 이해와 로봇 조작 작업을 모두 처리하도록 설계된 최초의 통합 모델로, 다가오는 행동과 그 시각적 결과를 모두 명시적으로 예측합니다. Ego4D, BridgeData 및 RLBench에 대한 광범위한 실험을 통해 우리의 방법이 행동 예측과 미래 비디오 합성 모두에서 최첨단 기준선을 능가함을 입증합니다.

## 핵심 내용
자기중심적 시나리오에서 다음 행동과 그 시각적 결과를 모두 예측하는 것은 인간-객체 상호작용을 이해하고 로봇 계획을 가능하게 하는 데 필수적입니다. 그러나 기존 패러다임은 이러한 측면을 공동으로 모델링하는 데 부족합니다. Vision-Language-Action(VLA) 모델은 행동 예측에 초점을 맞추지만 행동이 시각적 장면에 미치는 영향을 명시적으로 모델링하지 않으며, 비디오 예측 모델은 특정 행동에 조건화되지 않고 미래 프레임을 생성하여 종종 비현실적이거나 맥락적으로 일관성 없는 결과를 초래합니다. 이러한 격차를 해소하기 위해, 우리는 손 궤적에 조건화된 자기중심적 시나리오에서 행동과 시각적 미래를 공동으로 모델링하는 통합된 2단계 예측 프레임워크를 제안합니다. 첫 번째 단계에서는 연속 상태 모델링을 수행하여 이질적인 입력(시각적 관찰, 언어, 행동 이력)을 처리하고 미래 손 궤적을 명시적으로 예측합니다. 두 번째 단계에서는 인과적 교차 주의를 도입하여 다중 모달 단서를 융합하고, 추론된 행동 신호를 활용하여 이미지 기반 잠재 확산 모델(LDM)을 안내하여 프레임별 미래 비디오를 생성합니다. 우리의 접근 방식은 자기중심적 인간 활동 이해와 로봇 조작 작업을 모두 처리하도록 설계된 최초의 통합 모델로, 다가오는 행동과 그 시각적 결과를 모두 명시적으로 예측합니다. Ego4D, BridgeData 및 RLBench에 대한 광범위한 실험을 통해 우리의 방법이 행동 예측과 미래 비디오 합성 모두에서 최첨단 기준선을 능가함을 입증합니다.
