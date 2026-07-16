---
$id: ent_paper_zhang_reasoning_vla_a_fast_and_gener_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Reasoning-VLA: A Fast and General Vision-Language-Action Reasoning Model for Autonomous Driving'
  zh: Reasoning-VLA
  ko: 'Reasoning-VLA: A Fast and General Vision-Language-Action Reasoning Model for Autonomous Driving'
summary:
  en: 'Reasoning-VLA: A Fast and General Vision-Language-Action Reasoning Model for Autonomous Driving (Reasoning-VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Lanzhou University, National University
    of Singapore, University of Science and Technology of China, Tsinghua University, University of New South Wales.'
  zh: 'Reasoning-VLA: A Fast and General Vision-Language-Action Reasoning Model for Autonomous Driving (Reasoning-VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Lanzhou University, National University
    of Singapore, University of Science and Technology of China, Tsinghua University, University of New South Wales.'
  ko: 'Reasoning-VLA: A Fast and General Vision-Language-Action Reasoning Model for Autonomous Driving (Reasoning-VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Lanzhou University, National University
    of Singapore, University of Science and Technology of China, Tsinghua University, University of New South Wales.'
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
- reasoning_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.19912v1.
sources:
- id: src_001
  type: paper
  title: 'Reasoning-VLA: A Fast and General Vision-Language-Action Reasoning Model for Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2511.19912
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Reasoning-VLA source
  url: https://doi.org/10.48550/arXiv.2511.19912
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have recently shown strong decision-making capabilities in autonomous driving. However, existing VLAs often struggle with achieving efficient inference and generalizing to novel autonomous vehicle configurations and driving scenarios. In this paper, we propose Reasoning-VLA, a general and fast action-generation VLA framework. The proposed model employs a set of learnable action queries, initialized via Gaussian sampling from ground-truth trajectories within the training corpus. These learnable queries interact with reasoning-enhanced vision-language features to generate continuous action trajectories in parallel. To promote robust generalization, we consolidate eight publicly available autonomous driving datasets into a standardized, Chain-of-Thought reasoning-based, and easy-to-use data format for model training. Leveraging both supervised learning and reinforcement learning fine-tuning, extensive empirical evaluations across multiple benchmarks demonstrate that Reasoning-VLA achieves state-of-the-art performance, superior generalization capability, and the excellent inference speed reported to date.

## 核心内容
Vision-Language-Action (VLA) models have recently shown strong decision-making capabilities in autonomous driving. However, existing VLAs often struggle with achieving efficient inference and generalizing to novel autonomous vehicle configurations and driving scenarios. In this paper, we propose Reasoning-VLA, a general and fast action-generation VLA framework. The proposed model employs a set of learnable action queries, initialized via Gaussian sampling from ground-truth trajectories within the training corpus. These learnable queries interact with reasoning-enhanced vision-language features to generate continuous action trajectories in parallel. To promote robust generalization, we consolidate eight publicly available autonomous driving datasets into a standardized, Chain-of-Thought reasoning-based, and easy-to-use data format for model training. Leveraging both supervised learning and reinforcement learning fine-tuning, extensive empirical evaluations across multiple benchmarks demonstrate that Reasoning-VLA achieves state-of-the-art performance, superior generalization capability, and the excellent inference speed reported to date.

## 参考
- http://arxiv.org/abs/2511.19912v1

## Overview
Vision-Language-Action (VLA) models have recently shown strong decision-making capabilities in autonomous driving. However, existing VLAs often struggle with achieving efficient inference and generalizing to novel autonomous vehicle configurations and driving scenarios. In this paper, we propose Reasoning-VLA, a general and fast action-generation VLA framework. The proposed model employs a set of learnable action queries, initialized via Gaussian sampling from ground-truth trajectories within the training corpus. These learnable queries interact with reasoning-enhanced vision-language features to generate continuous action trajectories in parallel. To promote robust generalization, we consolidate eight publicly available autonomous driving datasets into a standardized, Chain-of-Thought reasoning-based, and easy-to-use data format for model training. Leveraging both supervised learning and reinforcement learning fine-tuning, extensive empirical evaluations across multiple benchmarks demonstrate that Reasoning-VLA achieves state-of-the-art performance, superior generalization capability, and the excellent inference speed reported to date.

## Content
Vision-Language-Action (VLA) models have recently shown strong decision-making capabilities in autonomous driving. However, existing VLAs often struggle with achieving efficient inference and generalizing to novel autonomous vehicle configurations and driving scenarios. In this paper, we propose Reasoning-VLA, a general and fast action-generation VLA framework. The proposed model employs a set of learnable action queries, initialized via Gaussian sampling from ground-truth trajectories within the training corpus. These learnable queries interact with reasoning-enhanced vision-language features to generate continuous action trajectories in parallel. To promote robust generalization, we consolidate eight publicly available autonomous driving datasets into a standardized, Chain-of-Thought reasoning-based, and easy-to-use data format for model training. Leveraging both supervised learning and reinforcement learning fine-tuning, extensive empirical evaluations across multiple benchmarks demonstrate that Reasoning-VLA achieves state-of-the-art performance, superior generalization capability, and the excellent inference speed reported to date.

## 개요
Vision-Language-Action (VLA) 모델은 최근 자율주행 분야에서 강력한 의사결정 능력을 보여주고 있습니다. 그러나 기존 VLA 모델은 효율적인 추론과 새로운 자율주행 차량 구성 및 주행 시나리오에 대한 일반화에 어려움을 겪는 경우가 많습니다. 본 논문에서는 일반적이고 빠른 행동 생성 VLA 프레임워크인 Reasoning-VLA를 제안합니다. 제안된 모델은 학습 가능한 행동 쿼리 세트를 사용하며, 이는 훈련 코퍼스 내의 실제 궤적에서 가우시안 샘플링을 통해 초기화됩니다. 이러한 학습 가능한 쿼리는 추론이 강화된 시각-언어 특징과 상호작용하여 연속적인 행동 궤적을 병렬로 생성합니다. 강건한 일반화를 촉진하기 위해, 우리는 8개의 공개 자율주행 데이터셋을 표준화된 Chain-of-Thought 추론 기반의 사용하기 쉬운 데이터 형식으로 통합하여 모델 훈련에 활용합니다. 지도 학습과 강화 학습 미세 조정을 모두 활용한 여러 벤치마크에 걸친 광범위한 실증 평가는 Reasoning-VLA가 최첨단 성능, 뛰어난 일반화 능력, 그리고 현재까지 보고된 가장 우수한 추론 속도를 달성함을 보여줍니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 최근 자율주행 분야에서 강력한 의사결정 능력을 보여주고 있습니다. 그러나 기존 VLA 모델은 효율적인 추론과 새로운 자율주행 차량 구성 및 주행 시나리오에 대한 일반화에 어려움을 겪는 경우가 많습니다. 본 논문에서는 일반적이고 빠른 행동 생성 VLA 프레임워크인 Reasoning-VLA를 제안합니다. 제안된 모델은 학습 가능한 행동 쿼리 세트를 사용하며, 이는 훈련 코퍼스 내의 실제 궤적에서 가우시안 샘플링을 통해 초기화됩니다. 이러한 학습 가능한 쿼리는 추론이 강화된 시각-언어 특징과 상호작용하여 연속적인 행동 궤적을 병렬로 생성합니다. 강건한 일반화를 촉진하기 위해, 우리는 8개의 공개 자율주행 데이터셋을 표준화된 Chain-of-Thought 추론 기반의 사용하기 쉬운 데이터 형식으로 통합하여 모델 훈련에 활용합니다. 지도 학습과 강화 학습 미세 조정을 모두 활용한 여러 벤치마크에 걸친 광범위한 실증 평가는 Reasoning-VLA가 최첨단 성능, 뛰어난 일반화 능력, 그리고 현재까지 보고된 가장 우수한 추론 속도를 달성함을 보여줍니다.
