---
$id: ent_paper_bi_motus_a_unified_latent_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Motus: A Unified Latent Action World Model'
  zh: Motus
  ko: 'Motus: A Unified Latent Action World Model'
summary:
  en: 'Motus: A Unified Latent Action World Model (Motus), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Bosch, Tsinghua University, Peking University, Horizon Robotics.'
  zh: 'Motus: A Unified Latent Action World Model (Motus), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Bosch, Tsinghua University, Peking University, Horizon Robotics.'
  ko: 'Motus: A Unified Latent Action World Model (Motus), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Bosch, Tsinghua University, Peking University, Horizon Robotics.'
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
- motus
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.13030v2.
sources:
- id: src_001
  type: paper
  title: 'Motus: A Unified Latent Action World Model (arXiv)'
  url: https://arxiv.org/abs/2512.13030
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Motus source
  url: https://doi.org/10.48550/arXiv.2512.13030
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
While a general embodied agent must function as a unified system, current methods are built on isolated models for understanding, world modeling, and control. This fragmentation prevents unifying multimodal generative capabilities and hinders learning from large-scale, heterogeneous data. In this paper, we propose Motus, a unified latent action world model that leverages existing general pretrained models and rich, sharable motion information. Motus introduces a Mixture-of-Transformer (MoT) architecture to integrate three experts (i.e., understanding, video generation, and action) and adopts a UniDiffuser-style scheduler to enable flexible switching between different modeling modes (i.e., world models, vision-language-action models, inverse dynamics models, video generation models, and video-action joint prediction models). Motus further leverages the optical flow to learn latent actions and adopts a recipe with three-phase training pipeline and six-layer data pyramid, thereby extracting pixel-level "delta action" and enabling large-scale action pretraining. Experiments show that Motus achieves superior performance against state-of-the-art methods in both simulation (a +15% improvement over X-VLA and a +45% improvement over Pi0.5) and real-world scenarios(improved by +11~48%), demonstrating unified modeling of all functionalities and priors significantly benefits downstream robotic tasks.

## 核心内容
While a general embodied agent must function as a unified system, current methods are built on isolated models for understanding, world modeling, and control. This fragmentation prevents unifying multimodal generative capabilities and hinders learning from large-scale, heterogeneous data. In this paper, we propose Motus, a unified latent action world model that leverages existing general pretrained models and rich, sharable motion information. Motus introduces a Mixture-of-Transformer (MoT) architecture to integrate three experts (i.e., understanding, video generation, and action) and adopts a UniDiffuser-style scheduler to enable flexible switching between different modeling modes (i.e., world models, vision-language-action models, inverse dynamics models, video generation models, and video-action joint prediction models). Motus further leverages the optical flow to learn latent actions and adopts a recipe with three-phase training pipeline and six-layer data pyramid, thereby extracting pixel-level "delta action" and enabling large-scale action pretraining. Experiments show that Motus achieves superior performance against state-of-the-art methods in both simulation (a +15% improvement over X-VLA and a +45% improvement over Pi0.5) and real-world scenarios(improved by +11~48%), demonstrating unified modeling of all functionalities and priors significantly benefits downstream robotic tasks.

## 参考
- http://arxiv.org/abs/2512.13030v2

## Overview
While a general embodied agent must function as a unified system, current methods are built on isolated models for understanding, world modeling, and control. This fragmentation prevents unifying multimodal generative capabilities and hinders learning from large-scale, heterogeneous data. In this paper, we propose Motus, a unified latent action world model that leverages existing general pretrained models and rich, sharable motion information. Motus introduces a Mixture-of-Transformer (MoT) architecture to integrate three experts (i.e., understanding, video generation, and action) and adopts a UniDiffuser-style scheduler to enable flexible switching between different modeling modes (i.e., world models, vision-language-action models, inverse dynamics models, video generation models, and video-action joint prediction models). Motus further leverages the optical flow to learn latent actions and adopts a recipe with three-phase training pipeline and six-layer data pyramid, thereby extracting pixel-level "delta action" and enabling large-scale action pretraining. Experiments show that Motus achieves superior performance against state-of-the-art methods in both simulation (a +15% improvement over X-VLA and a +45% improvement over Pi0.5) and real-world scenarios (improved by +11~48%), demonstrating unified modeling of all functionalities and priors significantly benefits downstream robotic tasks.

## Content
While a general embodied agent must function as a unified system, current methods are built on isolated models for understanding, world modeling, and control. This fragmentation prevents unifying multimodal generative capabilities and hinders learning from large-scale, heterogeneous data. In this paper, we propose Motus, a unified latent action world model that leverages existing general pretrained models and rich, sharable motion information. Motus introduces a Mixture-of-Transformer (MoT) architecture to integrate three experts (i.e., understanding, video generation, and action) and adopts a UniDiffuser-style scheduler to enable flexible switching between different modeling modes (i.e., world models, vision-language-action models, inverse dynamics models, video generation models, and video-action joint prediction models). Motus further leverages the optical flow to learn latent actions and adopts a recipe with three-phase training pipeline and six-layer data pyramid, thereby extracting pixel-level "delta action" and enabling large-scale action pretraining. Experiments show that Motus achieves superior performance against state-of-the-art methods in both simulation (a +15% improvement over X-VLA and a +45% improvement over Pi0.5) and real-world scenarios (improved by +11~48%), demonstrating unified modeling of all functionalities and priors significantly benefits downstream robotic tasks.

## 개요
일반적인 임베디드 에이전트는 통합 시스템으로 작동해야 하지만, 현재 방법들은 이해, 세계 모델링, 제어를 위한 개별 모델을 기반으로 구축되어 있습니다. 이러한 분할은 다중 모달 생성 능력을 통합하지 못하게 하고 대규모 이질적 데이터로부터 학습을 방해합니다. 본 논문에서는 기존의 일반 사전 학습 모델과 풍부하고 공유 가능한 모션 정보를 활용하는 통합 잠재 행동 세계 모델인 Motus를 제안합니다. Motus는 Mixture-of-Transformer(MoT) 아키텍처를 도입하여 세 가지 전문가(이해, 비디오 생성, 행동)를 통합하고, UniDiffuser 스타일 스케줄러를 채택하여 다양한 모델링 모드(세계 모델, 시각-언어-행동 모델, 역동역학 모델, 비디오 생성 모델, 비디오-행동 공동 예측 모델) 간의 유연한 전환을 가능하게 합니다. 또한 Motus는 광학 흐름을 활용하여 잠재 행동을 학습하고, 3단계 학습 파이프라인과 6계층 데이터 피라미드를 포함한 레시피를 채택하여 픽셀 수준의 "델타 행동"을 추출하고 대규모 행동 사전 학습을 가능하게 합니다. 실험 결과, Motus는 시뮬레이션(X-VLA 대비 +15%, Pi0.5 대비 +45% 향상)과 실제 환경(+11~48% 향상) 모두에서 최신 방법보다 우수한 성능을 달성하여, 모든 기능과 사전 지식의 통합 모델링이 다운스트림 로봇 작업에 크게 기여함을 보여줍니다.

## 핵심 내용
일반적인 임베디드 에이전트는 통합 시스템으로 작동해야 하지만, 현재 방법들은 이해, 세계 모델링, 제어를 위한 개별 모델을 기반으로 구축되어 있습니다. 이러한 분할은 다중 모달 생성 능력을 통합하지 못하게 하고 대규모 이질적 데이터로부터 학습을 방해합니다. 본 논문에서는 기존의 일반 사전 학습 모델과 풍부하고 공유 가능한 모션 정보를 활용하는 통합 잠재 행동 세계 모델인 Motus를 제안합니다. Motus는 Mixture-of-Transformer(MoT) 아키텍처를 도입하여 세 가지 전문가(이해, 비디오 생성, 행동)를 통합하고, UniDiffuser 스타일 스케줄러를 채택하여 다양한 모델링 모드(세계 모델, 시각-언어-행동 모델, 역동역학 모델, 비디오 생성 모델, 비디오-행동 공동 예측 모델) 간의 유연한 전환을 가능하게 합니다. 또한 Motus는 광학 흐름을 활용하여 잠재 행동을 학습하고, 3단계 학습 파이프라인과 6계층 데이터 피라미드를 포함한 레시피를 채택하여 픽셀 수준의 "델타 행동"을 추출하고 대규모 행동 사전 학습을 가능하게 합니다. 실험 결과, Motus는 시뮬레이션(X-VLA 대비 +15%, Pi0.5 대비 +45% 향상)과 실제 환경(+11~48% 향상) 모두에서 최신 방법보다 우수한 성능을 달성하여, 모든 기능과 사전 지식의 통합 모델링이 다운스트림 로봇 작업에 크게 기여함을 보여줍니다.
