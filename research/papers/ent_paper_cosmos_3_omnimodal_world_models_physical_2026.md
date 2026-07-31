---
$id: ent_paper_cosmos_3_omnimodal_world_models_physical_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Cosmos 3: Omnimodal World Models for Physical AI'
  zh: 'Cosmos 3: Omnimodal World Models for Physical AI'
  ko: 'Cosmos 3: Omnimodal World Models for Physical AI'
summary:
  en: 'We introduce Cosmos 3, a family of omnimodal world models designed to jointly process and generate language, image,
    video, audio, and action sequences within a unified mixture-of-transformers architecture. Institutions per source list:
    NVIDIA.'
  zh: Cosmos 3 是由 NVIDIA 推出的全模态世界模型系列，采用统一的混合 Transformer 架构，可联合处理语言、图像、视频、音频和动作序列。其核心贡献在于首次将视觉-语言模型、视频生成器、世界模拟器和世界-动作模型整合为单一框架，并在多项理解与生成任务上达到新最优水平，同时作为开源模型在
    Artificial Analysis 和 RoboArena 评测中取得领先排名。
  ko: 'We introduce Cosmos 3, a family of omnimodal world models designed to jointly process and generate language, image,
    video, audio, and action sequences within a unified mixture-of-transformers architecture. Institutions per source list:
    NVIDIA.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- cosmos
- '3'
- omnimodal
- world
- models
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 335 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2606.02800 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2606.02800v4); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.02800 Cosmos 3: Omnimodal World Models for Physical AI'
  url: https://arxiv.org/abs/2606.02800
  accessed_at: '2026-07-31'
  date: '2026-06-01'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

Cosmos 3 通过混合 Transformer 架构实现了对语言、图像、视频、音频和动作五种模态的统一处理与生成。该模型支持高度灵活的输入-输出配置，能够无缝整合 Physical AI 所需的关键模态，从而将视觉-语言模型、视频生成器、世界模拟器和世界-动作模型融合为一个通用框架。实验评估表明，Cosmos 3 在多种理解与生成任务上均取得了新的最优结果，证明了全模态世界模型可作为具身智能体的可扩展通用骨干网络。此外，其后训练版本在 Artificial Analysis 的 Text-to-Image 和 Image-to-Video 评测中被评为最佳开源模型，并在 RoboArena 策略模型评测中排名第一。

## 核心内容
### 方法架构
Cosmos 3 采用统一的混合 Transformer 架构，核心设计包括：
- **全模态统一处理**：模型可同时处理语言、图像、视频、音频和动作序列，支持任意模态组合的输入与输出。
- **灵活配置**：通过可变的输入-输出接口，模型能适应从纯文本到多模态交互的多种任务场景。
- **单一框架整合**：将视觉-语言模型、视频生成器、世界模拟器和世界-动作模型的功能合并，无需为不同任务分别训练独立模型。

### 实验设置与关键结果
- **评测任务**：涵盖理解任务（如视觉问答、多模态推理）和生成任务（如文本到图像、图像到视频、视频到音频等）。
- **性能表现**：在多个基准测试中，Cosmos 3 均达到新最优水平，具体包括：
  - **Text-to-Image**：在 Artificial Analysis 评测中被评为最佳开源模型。
  - **Image-to-Video**：同样在 Artificial Analysis 评测中排名第一。
  - **策略模型**：在 RoboArena 评测中取得最佳策略模型成绩。
- **开源资源**：代码、模型检查点、合成数据集和评测基准均已在 Linux Foundation 的 OpenMDW-1.1 许可下开源，可通过 GitHub 和 Hugging Face 获取。

### 结论
Cosmos 3 证明了全模态世界模型作为 Physical AI 通用骨干网络的可行性，通过统一架构显著简化了具身智能体的开发流程。其开源发布旨在加速 Physical AI 领域的研究与部署，为社区提供可复现的基准和工具。

## Overview
We introduce Cosmos 3, a family of omnimodal world models designed to jointly process and generate language, image, video, audio, and action sequences within a unified mixture-of-transformers architecture. By supporting highly flexible input-output configurations, Cosmos 3 seamlessly unifies critical modalities for Physical AI -- effectively subsuming vision-language models, video generators, world simulators, and world-action models into a single framework. Our evaluation demonstrates that Cosmos 3 establishes a new state-of-the-art across a diverse suite of understanding and generation tasks, demonstrating omnimodal world models as scalable, general-purpose backbones for embodied agents. Our post-trained Cosmos 3 models were ranked as the best open-source Text-to-Image and Image-to-Video models by Artificial Analysis, and the best policy model by RoboArena at the time the technical report was written. To accelerate open research and deployment in Physical AI, we make our code, model checkpoints, curated synthetic datasets, and evaluation benchmark available under the Linux Foundation's OpenMDW-1.1 License at https://github.com/nvidia/cosmos and https://huggingface.co/collections/nvidia/cosmos3. The project website is available at https://research.nvidia.com/labs/cosmos-lab/cosmos3.

## 参考
- https://arxiv.org/abs/2606.02800
- https://github.com/ImChong/Robotics_Notebooks

## 개요

Cosmos 3는 하이브리드 트랜스포머 아키텍처를 통해 언어, 이미지, 비디오, 오디오 및 동작의 다섯 가지 모달리티를 통합적으로 처리하고 생성합니다. 이 모델은 매우 유연한 입력-출력 구성을 지원하며, Physical AI에 필요한 핵심 모달리티를 원활하게 통합하여 비전-언어 모델, 비디오 생성기, 세계 시뮬레이터 및 세계-동작 모델을 하나의 범용 프레임워크로 융합합니다. 실험 평가에 따르면, Cosmos 3는 다양한 이해 및 생성 작업에서 새로운 최고 성능을 달성하여, 전모달리티 세계 모델이 구현형 에이전트를 위한 확장 가능한 범용 백본 네트워크로 사용될 수 있음을 입증했습니다. 또한, 후훈련 버전은 Artificial Analysis의 Text-to-Image 및 Image-to-Video 평가에서 최고의 오픈소스 모델로 선정되었으며, RoboArena 정책 모델 평가에서 1위를 차지했습니다.

## 핵심 내용
### 방법 아키텍처
Cosmos 3는 통합된 하이브리드 트랜스포머 아키텍처를 채택하며, 핵심 설계는 다음과 같습니다:
- **전모달리티 통합 처리**: 모델은 언어, 이미지, 비디오, 오디오 및 동작 시퀀스를 동시에 처리할 수 있으며, 임의의 모달리티 조합으로 입력과 출력을 지원합니다.
- **유연한 구성**: 가변적인 입력-출력 인터페이스를 통해 모델은 순수 텍스트에서 다중 모달리티 상호작용에 이르기까지 다양한 작업 시나리오에 적응할 수 있습니다.
- **단일 프레임워크 통합**: 비전-언어 모델, 비디오 생성기, 세계 시뮬레이터 및 세계-동작 모델의 기능을 병합하여, 각 작업마다 별도의 모델을 훈련할 필요가 없습니다.

### 실험 설정 및 주요 결과
- **평가 작업**: 이해 작업(예: 시각 질의응답, 다중 모달리티 추론) 및 생성 작업(예: 텍스트-이미지, 이미지-비디오, 비디오-오디오 등)을 포함합니다.
- **성능**: 여러 벤치마크에서 Cosmos 3는 새로운 최고 수준에 도달했으며, 구체적으로는 다음과 같습니다:
  - **Text-to-Image**: Artificial Analysis 평가에서 최고의 오픈소스 모델로 선정됨.
  - **Image-to-Video**: 동일한 Artificial Analysis 평가에서 1위를 차지함.
  - **정책 모델**: RoboArena 평가에서 최고의 정책 모델 성과를 기록함.
- **오픈소스 리소스**: 코드, 모델 체크포인트, 합성 데이터셋 및 평가 벤치마크는 Linux Foundation의 OpenMDW-1.1 라이선스 하에 오픈소스로 제공되며, GitHub 및 Hugging Face를 통해 접근할 수 있습니다.

### 결론
Cosmos 3는 전모달리티 세계 모델이 Physical AI의 범용 백본 네트워크로 사용될 수 있음을 입증했으며, 통합 아키텍처를 통해 구현형 에이전트의 개발 프로세스를 크게 간소화했습니다. 오픈소스 공개는 Physical AI 분야의 연구와 배포를 가속화하고, 커뮤니티에 재현 가능한 벤치마크와 도구를 제공하는 것을 목표로 합니다.
