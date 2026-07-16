---
$id: ent_paper_dong_emma_generalizing_real_world_r_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer'
  zh: EMMA
  ko: 'EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer'
summary:
  en: 'EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer (EMMA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Singapore University of Technology and Design, Deepmind.'
  zh: 'EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer (EMMA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Singapore University of Technology and Design, Deepmind.'
  ko: 'EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer (EMMA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Singapore University of Technology and Design, Deepmind.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- emma
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.22407v2.
sources:
- id: src_001
  type: paper
  title: 'EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer (arXiv)'
  url: https://arxiv.org/abs/2509.22407
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: EMMA source
  url: https://doi.org/10.48550/arXiv.2509.22407
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The generalization of vision-language-action (VLA) models heavily relies on diverse training data. However, acquiring large-scale data for robot manipulation across varied object appearances is costly and labor-intensive. To address this limitation, we introduce Embodied Manipulation Media Adaptation (EMMA), a framework for augmenting VLA policies that combines a generative data engine with an effective training pipeline. We introduce DreamTransfer, a diffusion Transformer-based architecture for generating multi-view consistent and geometrically grounded embodied manipulation videos. DreamTransfer enables visual editing of robot videos through prompts, allowing for changes to the foreground, background, and lighting while preserving their 3D structure and geometric validity. We also utilize a hybrid training set of real and generated data and propose AdaMix to enhance the training process. AdaMix is a training strategy that adaptively weights samples according to policy performance to emphasize challenging samples. Comprehensive evaluations demonstrate that videos created by DreamTransfer yield substantial improvements over previous video generation techniques in multi-view consistency, geometric accuracy, and text-conditioning precision. We conduct extensive evaluations with a total of more than 1800 trials in both simulated and real-world robotic environments. In real-world robotic tasks with zero-shot visual settings, our framework achieves a relative performance increase of over 92% compared to training with real data alone, and improves by an additional 17% with AdaMix, demonstrating its efficacy in enhancing policy generalization.

## 核心内容
The generalization of vision-language-action (VLA) models heavily relies on diverse training data. However, acquiring large-scale data for robot manipulation across varied object appearances is costly and labor-intensive. To address this limitation, we introduce Embodied Manipulation Media Adaptation (EMMA), a framework for augmenting VLA policies that combines a generative data engine with an effective training pipeline. We introduce DreamTransfer, a diffusion Transformer-based architecture for generating multi-view consistent and geometrically grounded embodied manipulation videos. DreamTransfer enables visual editing of robot videos through prompts, allowing for changes to the foreground, background, and lighting while preserving their 3D structure and geometric validity. We also utilize a hybrid training set of real and generated data and propose AdaMix to enhance the training process. AdaMix is a training strategy that adaptively weights samples according to policy performance to emphasize challenging samples. Comprehensive evaluations demonstrate that videos created by DreamTransfer yield substantial improvements over previous video generation techniques in multi-view consistency, geometric accuracy, and text-conditioning precision. We conduct extensive evaluations with a total of more than 1800 trials in both simulated and real-world robotic environments. In real-world robotic tasks with zero-shot visual settings, our framework achieves a relative performance increase of over 92% compared to training with real data alone, and improves by an additional 17% with AdaMix, demonstrating its efficacy in enhancing policy generalization.

## 参考
- http://arxiv.org/abs/2509.22407v2

## Overview
The generalization of vision-language-action (VLA) models heavily relies on diverse training data. However, acquiring large-scale data for robot manipulation across varied object appearances is costly and labor-intensive. To address this limitation, we introduce Embodied Manipulation Media Adaptation (EMMA), a framework for augmenting VLA policies that combines a generative data engine with an effective training pipeline. We introduce DreamTransfer, a diffusion Transformer-based architecture for generating multi-view consistent and geometrically grounded embodied manipulation videos. DreamTransfer enables visual editing of robot videos through prompts, allowing for changes to the foreground, background, and lighting while preserving their 3D structure and geometric validity. We also utilize a hybrid training set of real and generated data and propose AdaMix to enhance the training process. AdaMix is a training strategy that adaptively weights samples according to policy performance to emphasize challenging samples. Comprehensive evaluations demonstrate that videos created by DreamTransfer yield substantial improvements over previous video generation techniques in multi-view consistency, geometric accuracy, and text-conditioning precision. We conduct extensive evaluations with a total of more than 1800 trials in both simulated and real-world robotic environments. In real-world robotic tasks with zero-shot visual settings, our framework achieves a relative performance increase of over 92% compared to training with real data alone, and improves by an additional 17% with AdaMix, demonstrating its efficacy in enhancing policy generalization.

## Content
The generalization of vision-language-action (VLA) models heavily relies on diverse training data. However, acquiring large-scale data for robot manipulation across varied object appearances is costly and labor-intensive. To address this limitation, we introduce Embodied Manipulation Media Adaptation (EMMA), a framework for augmenting VLA policies that combines a generative data engine with an effective training pipeline. We introduce DreamTransfer, a diffusion Transformer-based architecture for generating multi-view consistent and geometrically grounded embodied manipulation videos. DreamTransfer enables visual editing of robot videos through prompts, allowing for changes to the foreground, background, and lighting while preserving their 3D structure and geometric validity. We also utilize a hybrid training set of real and generated data and propose AdaMix to enhance the training process. AdaMix is a training strategy that adaptively weights samples according to policy performance to emphasize challenging samples. Comprehensive evaluations demonstrate that videos created by DreamTransfer yield substantial improvements over previous video generation techniques in multi-view consistency, geometric accuracy, and text-conditioning precision. We conduct extensive evaluations with a total of more than 1800 trials in both simulated and real-world robotic environments. In real-world robotic tasks with zero-shot visual settings, our framework achieves a relative performance increase of over 92% compared to training with real data alone, and improves by an additional 17% with AdaMix, demonstrating its efficacy in enhancing policy generalization.

## 개요
시각-언어-행동(VLA) 모델의 일반화는 다양한 훈련 데이터에 크게 의존합니다. 그러나 다양한 객체 외형에 걸친 로봇 조작을 위한 대규모 데이터를 확보하는 것은 비용과 노동이 많이 듭니다. 이러한 한계를 해결하기 위해, 우리는 생성적 데이터 엔진과 효과적인 훈련 파이프라인을 결합한 VLA 정책 증강 프레임워크인 Embodied Manipulation Media Adaptation (EMMA)을 소개합니다. 우리는 다중 시점 일관성과 기하학적 기반을 갖춘 구현된 조작 비디오를 생성하기 위한 확산 Transformer 기반 아키텍처인 DreamTransfer를 도입합니다. DreamTransfer는 프롬프트를 통해 로봇 비디오의 시각적 편집을 가능하게 하여, 3D 구조와 기하학적 유효성을 유지하면서 전경, 배경 및 조명을 변경할 수 있습니다. 또한 실제 데이터와 생성 데이터의 혼합 훈련 세트를 활용하고, 훈련 과정을 강화하기 위해 AdaMix를 제안합니다. AdaMix는 정책 성능에 따라 샘플에 적응적으로 가중치를 부여하여 어려운 샘플을 강조하는 훈련 전략입니다. 포괄적인 평가는 DreamTransfer가 생성한 비디오가 다중 시점 일관성, 기하학적 정확성 및 텍스트 조건 정밀도에서 이전 비디오 생성 기술보다 상당한 개선을 제공함을 보여줍니다. 우리는 시뮬레이션 및 실제 로봇 환경에서 총 1800회 이상의 시험을 통해 광범위한 평가를 수행합니다. 제로샷 시각 설정의 실제 로봇 작업에서, 우리 프레임워크는 실제 데이터만으로 훈련한 경우보다 상대적 성능이 92% 이상 향상되었으며, AdaMix를 통해 추가로 17% 개선되어 정책 일반화 향상에 대한 효능을 입증합니다.

## 핵심 내용
시각-언어-행동(VLA) 모델의 일반화는 다양한 훈련 데이터에 크게 의존합니다. 그러나 다양한 객체 외형에 걸친 로봇 조작을 위한 대규모 데이터를 확보하는 것은 비용과 노동이 많이 듭니다. 이러한 한계를 해결하기 위해, 우리는 생성적 데이터 엔진과 효과적인 훈련 파이프라인을 결합한 VLA 정책 증강 프레임워크인 Embodied Manipulation Media Adaptation (EMMA)을 소개합니다. 우리는 다중 시점 일관성과 기하학적 기반을 갖춘 구현된 조작 비디오를 생성하기 위한 확산 Transformer 기반 아키텍처인 DreamTransfer를 도입합니다. DreamTransfer는 프롬프트를 통해 로봇 비디오의 시각적 편집을 가능하게 하여, 3D 구조와 기하학적 유효성을 유지하면서 전경, 배경 및 조명을 변경할 수 있습니다. 또한 실제 데이터와 생성 데이터의 혼합 훈련 세트를 활용하고, 훈련 과정을 강화하기 위해 AdaMix를 제안합니다. AdaMix는 정책 성능에 따라 샘플에 적응적으로 가중치를 부여하여 어려운 샘플을 강조하는 훈련 전략입니다. 포괄적인 평가는 DreamTransfer가 생성한 비디오가 다중 시점 일관성, 기하학적 정확성 및 텍스트 조건 정밀도에서 이전 비디오 생성 기술보다 상당한 개선을 제공함을 보여줍니다. 우리는 시뮬레이션 및 실제 로봇 환경에서 총 1800회 이상의 시험을 통해 광범위한 평가를 수행합니다. 제로샷 시각 설정의 실제 로봇 작업에서, 우리 프레임워크는 실제 데이터만으로 훈련한 경우보다 상대적 성능이 92% 이상 향상되었으며, AdaMix를 통해 추가로 17% 개선되어 정책 일반화 향상에 대한 효능을 입증합니다.
