---
$id: ent_paper_wu_dejavu_towards_experience_feed_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Dejavu: Towards Experience Feedback Learning for Embodied Intelligence'
  zh: Dejavu
  ko: 'Dejavu: Towards Experience Feedback Learning for Embodied Intelligence'
summary:
  en: 'Dejavu: Towards Experience Feedback Learning for Embodied Intelligence (Dejavu), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University.'
  zh: 'Dejavu: Towards Experience Feedback Learning for Embodied Intelligence (Dejavu), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University.'
  ko: 'Dejavu: Towards Experience Feedback Learning for Embodied Intelligence (Dejavu), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dejavu
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.10181v3.
sources:
- id: src_001
  type: paper
  title: 'Dejavu: Towards Experience Feedback Learning for Embodied Intelligence (arXiv)'
  url: https://arxiv.org/abs/2510.10181
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Embodied agents face a fundamental limitation: once deployed in real-world environments, they cannot easily acquire new knowledge to improve task performance. In this paper, we propose Dejavu, a general post-deployment learning framework that augments a frozen Vision-Language-Action (VLA) policy with retrieved execution memories through an Experience Feedback Network (EFN). EFN identifies contextually relevant prior action experiences and conditions action prediction on the retrieved guidance. We train EFN with reinforcement learning and semantic similarity rewards, encouraging the predicted actions to align with past behaviors under the current observation. During deployment, EFN continually expands its memory with new trajectories, enabling the agent to exhibit ``learning from experience.'' Experiments across diverse embodied tasks show that EFN improves adaptability, robustness, and success rates over frozen baselines. Our Project Page is https://dejavu2025.github.io/.

## 核心内容
Embodied agents face a fundamental limitation: once deployed in real-world environments, they cannot easily acquire new knowledge to improve task performance. In this paper, we propose Dejavu, a general post-deployment learning framework that augments a frozen Vision-Language-Action (VLA) policy with retrieved execution memories through an Experience Feedback Network (EFN). EFN identifies contextually relevant prior action experiences and conditions action prediction on the retrieved guidance. We train EFN with reinforcement learning and semantic similarity rewards, encouraging the predicted actions to align with past behaviors under the current observation. During deployment, EFN continually expands its memory with new trajectories, enabling the agent to exhibit ``learning from experience.'' Experiments across diverse embodied tasks show that EFN improves adaptability, robustness, and success rates over frozen baselines. Our Project Page is https://dejavu2025.github.io/.

## 参考
- http://arxiv.org/abs/2510.10181v3

## Overview
Embodied agents face a fundamental limitation: once deployed in real-world environments, they cannot easily acquire new knowledge to improve task performance. In this paper, we propose Dejavu, a general post-deployment learning framework that augments a frozen Vision-Language-Action (VLA) policy with retrieved execution memories through an Experience Feedback Network (EFN). EFN identifies contextually relevant prior action experiences and conditions action prediction on the retrieved guidance. We train EFN with reinforcement learning and semantic similarity rewards, encouraging the predicted actions to align with past behaviors under the current observation. During deployment, EFN continually expands its memory with new trajectories, enabling the agent to exhibit ``learning from experience.'' Experiments across diverse embodied tasks show that EFN improves adaptability, robustness, and success rates over frozen baselines. Our Project Page is https://dejavu2025.github.io/.

## Content
Embodied agents face a fundamental limitation: once deployed in real-world environments, they cannot easily acquire new knowledge to improve task performance. In this paper, we propose Dejavu, a general post-deployment learning framework that augments a frozen Vision-Language-Action (VLA) policy with retrieved execution memories through an Experience Feedback Network (EFN). EFN identifies contextually relevant prior action experiences and conditions action prediction on the retrieved guidance. We train EFN with reinforcement learning and semantic similarity rewards, encouraging the predicted actions to align with past behaviors under the current observation. During deployment, EFN continually expands its memory with new trajectories, enabling the agent to exhibit ``learning from experience.'' Experiments across diverse embodied tasks show that EFN improves adaptability, robustness, and success rates over frozen baselines. Our Project Page is https://dejavu2025.github.io/.

## 개요
임베디드 에이전트는 근본적인 한계에 직면합니다: 실제 환경에 배포된 후에는 작업 성능을 개선하기 위해 새로운 지식을 쉽게 습득할 수 없습니다. 본 논문에서는 Dejavu를 제안합니다. 이는 경험 피드백 네트워크(EFN)를 통해 검색된 실행 메모리로 고정된 Vision-Language-Action(VLA) 정책을 보강하는 일반적인 배포 후 학습 프레임워크입니다. EFN은 맥락적으로 관련된 이전 행동 경험을 식별하고 검색된 지침에 따라 행동 예측을 조건화합니다. 우리는 강화 학습과 의미 유사성 보상을 사용하여 EFN을 훈련하며, 현재 관찰 하에서 예측된 행동이 과거 행동과 일치하도록 장려합니다. 배포 중에 EFN은 새로운 궤적으로 메모리를 지속적으로 확장하여 에이전트가 "경험을 통한 학습"을 나타낼 수 있도록 합니다. 다양한 임베디드 작업에 걸친 실험은 EFN이 고정된 기준선보다 적응성, 견고성 및 성공률을 향상시킴을 보여줍니다. 프로젝트 페이지는 https://dejavu2025.github.io/입니다.

## 핵심 내용
임베디드 에이전트는 근본적인 한계에 직면합니다: 실제 환경에 배포된 후에는 작업 성능을 개선하기 위해 새로운 지식을 쉽게 습득할 수 없습니다. 본 논문에서는 Dejavu를 제안합니다. 이는 경험 피드백 네트워크(EFN)를 통해 검색된 실행 메모리로 고정된 Vision-Language-Action(VLA) 정책을 보강하는 일반적인 배포 후 학습 프레임워크입니다. EFN은 맥락적으로 관련된 이전 행동 경험을 식별하고 검색된 지침에 따라 행동 예측을 조건화합니다. 우리는 강화 학습과 의미 유사성 보상을 사용하여 EFN을 훈련하며, 현재 관찰 하에서 예측된 행동이 과거 행동과 일치하도록 장려합니다. 배포 중에 EFN은 새로운 궤적으로 메모리를 지속적으로 확장하여 에이전트가 "경험을 통한 학습"을 나타낼 수 있도록 합니다. 다양한 임베디드 작업에 걸친 실험은 EFN이 고정된 기준선보다 적응성, 견고성 및 성공률을 향상시킴을 보여줍니다. 프로젝트 페이지는 https://dejavu2025.github.io/입니다.
