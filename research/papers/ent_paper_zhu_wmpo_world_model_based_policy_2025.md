---
$id: ent_paper_zhu_wmpo_world_model_based_policy_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WMPO: World Model-based Policy Optimization for Vision-Language-Action Models'
  zh: WMPO
  ko: 'WMPO: World Model-based Policy Optimization for Vision-Language-Action Models'
summary:
  en: 'WMPO: World Model-based Policy Optimization for Vision-Language-Action Models (WMPO), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Hong Kong University of Science and Technology, ByteDance Seed.'
  zh: 'WMPO: World Model-based Policy Optimization for Vision-Language-Action Models (WMPO), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Hong Kong University of Science and Technology, ByteDance Seed.'
  ko: 'WMPO: World Model-based Policy Optimization for Vision-Language-Action Models (WMPO), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Hong Kong University of Science and Technology, ByteDance Seed.'
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
- vision_language_action
- vla
- wmpo
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.09515v1.
sources:
- id: src_001
  type: paper
  title: 'WMPO: World Model-based Policy Optimization for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2511.09515
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: WMPO source
  url: https://doi.org/10.48550/arXiv.2511.09515
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have shown strong potential for general-purpose robotic manipulation, but their reliance on expert demonstrations limits their ability to learn from failures and perform self-corrections. Reinforcement learning (RL) addresses these through self-improving interactions with the physical environment, but suffers from high sample complexity on real robots. We introduce World-Model-based Policy Optimization (WMPO), a principled framework for on-policy VLA RL without interacting with the real environment. In contrast to widely used latent world models, WMPO focuses on pixel-based predictions that align the "imagined" trajectories with the VLA features pretrained with web-scale images. Crucially, WMPO enables the policy to perform on-policy GRPO that provides stronger performance than the often-used off-policy methods. Extensive experiments in both simulation and real-robot settings demonstrate that WMPO (i) substantially improves sample efficiency, (ii) achieves stronger overall performance, (iii) exhibits emergent behaviors such as self-correction, and (iv) demonstrates robust generalization and lifelong learning capabilities.

## 核心内容
Vision-Language-Action (VLA) models have shown strong potential for general-purpose robotic manipulation, but their reliance on expert demonstrations limits their ability to learn from failures and perform self-corrections. Reinforcement learning (RL) addresses these through self-improving interactions with the physical environment, but suffers from high sample complexity on real robots. We introduce World-Model-based Policy Optimization (WMPO), a principled framework for on-policy VLA RL without interacting with the real environment. In contrast to widely used latent world models, WMPO focuses on pixel-based predictions that align the "imagined" trajectories with the VLA features pretrained with web-scale images. Crucially, WMPO enables the policy to perform on-policy GRPO that provides stronger performance than the often-used off-policy methods. Extensive experiments in both simulation and real-robot settings demonstrate that WMPO (i) substantially improves sample efficiency, (ii) achieves stronger overall performance, (iii) exhibits emergent behaviors such as self-correction, and (iv) demonstrates robust generalization and lifelong learning capabilities.

## 参考
- http://arxiv.org/abs/2511.09515v1

## Overview
Vision-Language-Action (VLA) models have shown strong potential for general-purpose robotic manipulation, but their reliance on expert demonstrations limits their ability to learn from failures and perform self-corrections. Reinforcement learning (RL) addresses these through self-improving interactions with the physical environment, but suffers from high sample complexity on real robots. We introduce World-Model-based Policy Optimization (WMPO), a principled framework for on-policy VLA RL without interacting with the real environment. In contrast to widely used latent world models, WMPO focuses on pixel-based predictions that align the "imagined" trajectories with the VLA features pretrained with web-scale images. Crucially, WMPO enables the policy to perform on-policy GRPO that provides stronger performance than the often-used off-policy methods. Extensive experiments in both simulation and real-robot settings demonstrate that WMPO (i) substantially improves sample efficiency, (ii) achieves stronger overall performance, (iii) exhibits emergent behaviors such as self-correction, and (iv) demonstrates robust generalization and lifelong learning capabilities.

## Content
Vision-Language-Action (VLA) models have shown strong potential for general-purpose robotic manipulation, but their reliance on expert demonstrations limits their ability to learn from failures and perform self-corrections. Reinforcement learning (RL) addresses these through self-improving interactions with the physical environment, but suffers from high sample complexity on real robots. We introduce World-Model-based Policy Optimization (WMPO), a principled framework for on-policy VLA RL without interacting with the real environment. In contrast to widely used latent world models, WMPO focuses on pixel-based predictions that align the "imagined" trajectories with the VLA features pretrained with web-scale images. Crucially, WMPO enables the policy to perform on-policy GRPO that provides stronger performance than the often-used off-policy methods. Extensive experiments in both simulation and real-robot settings demonstrate that WMPO (i) substantially improves sample efficiency, (ii) achieves stronger overall performance, (iii) exhibits emergent behaviors such as self-correction, and (iv) demonstrates robust generalization and lifelong learning capabilities.

## 개요
Vision-Language-Action (VLA) 모델은 범용 로봇 조작에 강력한 잠재력을 보여주었지만, 전문가 시연에 의존하기 때문에 실패로부터 학습하고 자가 교정을 수행하는 능력이 제한됩니다. 강화 학습(RL)은 물리적 환경과의 자기 개선 상호작용을 통해 이러한 문제를 해결하지만, 실제 로봇에서는 높은 샘플 복잡성으로 인해 어려움을 겪습니다. 우리는 실제 환경과 상호작용하지 않고 온-폴리시 VLA RL을 수행하는 원칙적 프레임워크인 World-Model 기반 정책 최적화(WMPO)를 소개합니다. 널리 사용되는 잠재 세계 모델과 달리, WMPO는 웹 규모 이미지로 사전 학습된 VLA 특징과 "상상된" 궤적을 정렬하는 픽셀 기반 예측에 초점을 맞춥니다. 결정적으로, WMPO는 정책이 자주 사용되는 오프-폴리시 방법보다 더 강력한 성능을 제공하는 온-폴리시 GRPO를 수행할 수 있게 합니다. 시뮬레이션 및 실제 로봇 환경 모두에서의 광범위한 실험은 WMPO가 (i) 샘플 효율성을 크게 향상시키고, (ii) 더 강력한 전반적 성능을 달성하며, (iii) 자가 교정과 같은 창발적 행동을 보여주고, (iv) 강력한 일반화 및 평생 학습 능력을 입증함을 보여줍니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 범용 로봇 조작에 강력한 잠재력을 보여주었지만, 전문가 시연에 의존하기 때문에 실패로부터 학습하고 자가 교정을 수행하는 능력이 제한됩니다. 강화 학습(RL)은 물리적 환경과의 자기 개선 상호작용을 통해 이러한 문제를 해결하지만, 실제 로봇에서는 높은 샘플 복잡성으로 인해 어려움을 겪습니다. 우리는 실제 환경과 상호작용하지 않고 온-폴리시 VLA RL을 수행하는 원칙적 프레임워크인 World-Model 기반 정책 최적화(WMPO)를 소개합니다. 널리 사용되는 잠재 세계 모델과 달리, WMPO는 웹 규모 이미지로 사전 학습된 VLA 특징과 "상상된" 궤적을 정렬하는 픽셀 기반 예측에 초점을 맞춥니다. 결정적으로, WMPO는 정책이 자주 사용되는 오프-폴리시 방법보다 더 강력한 성능을 제공하는 온-폴리시 GRPO를 수행할 수 있게 합니다. 시뮬레이션 및 실제 로봇 환경 모두에서의 광범위한 실험은 WMPO가 (i) 샘플 효율성을 크게 향상시키고, (ii) 더 강력한 전반적 성능을 달성하며, (iii) 자가 교정과 같은 창발적 행동을 보여주고, (iv) 강력한 일반화 및 평생 학습 능력을 입증함을 보여줍니다.
