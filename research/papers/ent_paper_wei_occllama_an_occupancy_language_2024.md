---
$id: ent_paper_wei_occllama_an_occupancy_language_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OccLLaMA: An Occupancy-Language-Action Generative World Model for Autonomous Driving'
  zh: OccLLaMA
  ko: 'OccLLaMA: An Occupancy-Language-Action Generative World Model for Autonomous Driving'
summary:
  en: 'OccLLaMA: An Occupancy-Language-Action Generative World Model for Autonomous Driving (OccLLaMA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Academy for Engineering & Technology, Fudan University, Institute for AI
    Industry Research, Tsinghua University.'
  zh: 'OccLLaMA: An Occupancy-Language-Action Generative World Model for Autonomous Driving (OccLLaMA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Academy for Engineering & Technology, Fudan University, Institute for AI
    Industry Research, Tsinghua University.'
  ko: 'OccLLaMA: An Occupancy-Language-Action Generative World Model for Autonomous Driving (OccLLaMA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Academy for Engineering & Technology, Fudan University, Institute for AI
    Industry Research, Tsinghua University.'
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
- occllama
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.03272v1.
sources:
- id: src_001
  type: paper
  title: 'OccLLaMA: An Occupancy-Language-Action Generative World Model for Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2409.03272
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OccLLaMA source
  url: https://doi.org/10.48550/arXiv.2409.03272
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
The rise of multi-modal large language models(MLLMs) has spurred their applications in autonomous driving. Recent MLLM-based methods perform action by learning a direct mapping from perception to action, neglecting the dynamics of the world and the relations between action and world dynamics. In contrast, human beings possess world model that enables them to simulate the future states based on 3D internal visual representation and plan actions accordingly. To this end, we propose OccLLaMA, an occupancy-language-action generative world model, which uses semantic occupancy as a general visual representation and unifies vision-language-action(VLA) modalities through an autoregressive model. Specifically, we introduce a novel VQVAE-like scene tokenizer to efficiently discretize and reconstruct semantic occupancy scenes, considering its sparsity and classes imbalance. Then, we build a unified multi-modal vocabulary for vision, language and action. Furthermore, we enhance LLM, specifically LLaMA, to perform the next token/scene prediction on the unified vocabulary to complete multiple tasks in autonomous driving. Extensive experiments demonstrate that OccLLaMA achieves competitive performance across multiple tasks, including 4D occupancy forecasting, motion planning, and visual question answering, showcasing its potential as a foundation model in autonomous driving.

## 核心内容
The rise of multi-modal large language models(MLLMs) has spurred their applications in autonomous driving. Recent MLLM-based methods perform action by learning a direct mapping from perception to action, neglecting the dynamics of the world and the relations between action and world dynamics. In contrast, human beings possess world model that enables them to simulate the future states based on 3D internal visual representation and plan actions accordingly. To this end, we propose OccLLaMA, an occupancy-language-action generative world model, which uses semantic occupancy as a general visual representation and unifies vision-language-action(VLA) modalities through an autoregressive model. Specifically, we introduce a novel VQVAE-like scene tokenizer to efficiently discretize and reconstruct semantic occupancy scenes, considering its sparsity and classes imbalance. Then, we build a unified multi-modal vocabulary for vision, language and action. Furthermore, we enhance LLM, specifically LLaMA, to perform the next token/scene prediction on the unified vocabulary to complete multiple tasks in autonomous driving. Extensive experiments demonstrate that OccLLaMA achieves competitive performance across multiple tasks, including 4D occupancy forecasting, motion planning, and visual question answering, showcasing its potential as a foundation model in autonomous driving.

## 参考
- http://arxiv.org/abs/2409.03272v1

## Overview
The rise of multi-modal large language models (MLLMs) has spurred their applications in autonomous driving. Recent MLLM-based methods perform action by learning a direct mapping from perception to action, neglecting the dynamics of the world and the relations between action and world dynamics. In contrast, human beings possess world model that enables them to simulate the future states based on 3D internal visual representation and plan actions accordingly. To this end, we propose OccLLaMA, an occupancy-language-action generative world model, which uses semantic occupancy as a general visual representation and unifies vision-language-action (VLA) modalities through an autoregressive model. Specifically, we introduce a novel VQVAE-like scene tokenizer to efficiently discretize and reconstruct semantic occupancy scenes, considering its sparsity and classes imbalance. Then, we build a unified multi-modal vocabulary for vision, language and action. Furthermore, we enhance LLM, specifically LLaMA, to perform the next token/scene prediction on the unified vocabulary to complete multiple tasks in autonomous driving. Extensive experiments demonstrate that OccLLaMA achieves competitive performance across multiple tasks, including 4D occupancy forecasting, motion planning, and visual question answering, showcasing its potential as a foundation model in autonomous driving.

## Content
The rise of multi-modal large language models (MLLMs) has spurred their applications in autonomous driving. Recent MLLM-based methods perform action by learning a direct mapping from perception to action, neglecting the dynamics of the world and the relations between action and world dynamics. In contrast, human beings possess world model that enables them to simulate the future states based on 3D internal visual representation and plan actions accordingly. To this end, we propose OccLLaMA, an occupancy-language-action generative world model, which uses semantic occupancy as a general visual representation and unifies vision-language-action (VLA) modalities through an autoregressive model. Specifically, we introduce a novel VQVAE-like scene tokenizer to efficiently discretize and reconstruct semantic occupancy scenes, considering its sparsity and classes imbalance. Then, we build a unified multi-modal vocabulary for vision, language and action. Furthermore, we enhance LLM, specifically LLaMA, to perform the next token/scene prediction on the unified vocabulary to complete multiple tasks in autonomous driving. Extensive experiments demonstrate that OccLLaMA achieves competitive performance across multiple tasks, including 4D occupancy forecasting, motion planning, and visual question answering, showcasing its potential as a foundation model in autonomous driving.

## 개요
멀티모달 대규모 언어 모델(MLLM)의 부상은 자율주행 분야에서의 응용을 촉진했습니다. 최근 MLLM 기반 방법은 인식에서 행동으로의 직접적인 매핑을 학습하여 행동을 수행하지만, 세계의 역학과 행동과 세계 역학 간의 관계를 무시합니다. 반면, 인간은 3D 내부 시각적 표현을 기반으로 미래 상태를 시뮬레이션하고 그에 따라 행동을 계획할 수 있는 세계 모델을 보유하고 있습니다. 이를 위해 우리는 OccLLaMA를 제안합니다. 이는 점유-언어-행동 생성 세계 모델로, 의미적 점유를 일반적인 시각적 표현으로 사용하고 자기회귀 모델을 통해 시각-언어-행동(VLA) 모달리티를 통합합니다. 구체적으로, 우리는 희소성과 클래스 불균형을 고려하여 의미적 점유 장면을 효율적으로 이산화하고 재구성하는 새로운 VQVAE 유사 장면 토크나이저를 도입합니다. 그런 다음, 시각, 언어 및 행동을 위한 통합 멀티모달 어휘를 구축합니다. 또한, LLM, 특히 LLaMA를 개선하여 통합 어휘에 대한 다음 토큰/장면 예측을 수행함으로써 자율주행에서 여러 작업을 완료합니다. 광범위한 실험을 통해 OccLLaMA가 4D 점유 예측, 모션 계획 및 시각 질문 응답을 포함한 여러 작업에서 경쟁력 있는 성능을 달성하여 자율주행의 기초 모델로서의 잠재력을 입증합니다.

## 핵심 내용
멀티모달 대규모 언어 모델(MLLM)의 부상은 자율주행 분야에서의 응용을 촉진했습니다. 최근 MLLM 기반 방법은 인식에서 행동으로의 직접적인 매핑을 학습하여 행동을 수행하지만, 세계의 역학과 행동과 세계 역학 간의 관계를 무시합니다. 반면, 인간은 3D 내부 시각적 표현을 기반으로 미래 상태를 시뮬레이션하고 그에 따라 행동을 계획할 수 있는 세계 모델을 보유하고 있습니다. 이를 위해 우리는 OccLLaMA를 제안합니다. 이는 점유-언어-행동 생성 세계 모델로, 의미적 점유를 일반적인 시각적 표현으로 사용하고 자기회귀 모델을 통해 시각-언어-행동(VLA) 모달리티를 통합합니다. 구체적으로, 우리는 희소성과 클래스 불균형을 고려하여 의미적 점유 장면을 효율적으로 이산화하고 재구성하는 새로운 VQVAE 유사 장면 토크나이저를 도입합니다. 그런 다음, 시각, 언어 및 행동을 위한 통합 멀티모달 어휘를 구축합니다. 또한, LLM, 특히 LLaMA를 개선하여 통합 어휘에 대한 다음 토큰/장면 예측을 수행함으로써 자율주행에서 여러 작업을 완료합니다. 광범위한 실험을 통해 OccLLaMA가 4D 점유 예측, 모션 계획 및 시각 질문 응답을 포함한 여러 작업에서 경쟁력 있는 성능을 달성하여 자율주행의 기초 모델로서의 잠재력을 입증합니다.
