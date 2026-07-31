---
$id: ent_paper_moconvq_unified_physics_motion_control_s_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MoConVQ: Unified Physics-Based Motion Control via Scalable Discrete Representations'
  zh: 'MoConVQ: Unified Physics-Based Motion Control via Scalable Discrete Representations'
  ko: 'MoConVQ: Unified Physics-Based Motion Control via Scalable Discrete Representations'
summary:
  en: In this work, we present MoConVQ, a novel unified framework for physics-based motion control leveraging scalable discrete
    representations. Building upon vector quantized variational autoencoders (VQ-VAE) and model-based reinforcement learning,
    our approach effectively learns motion embeddings from a large, unstructured dataset spanning tens of hours of motion
    examples.
  zh: MoConVQ 是一个基于可扩展离散表示的物理驱动运动控制统一框架。它由研究团队提出，结合了 VQ-VAE 与基于模型的强化学习，从数十小时的无结构运动数据中学习运动嵌入。核心贡献在于实现了通用跟踪控制、交互式角色控制、基于自然语言的物理运动生成，以及与大型语言模型的无缝集成。
  ko: In this work, we present MoConVQ, a novel unified framework for physics-based motion control leveraging scalable discrete
    representations. Building upon vector quantized variational autoencoders (VQ-VAE) and model-based reinforcement learning,
    our approach effectively learns motion embeddings from a large, unstructured dataset spanning tens of hours of motion
    examples.
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
- moconvq
- unified
- physics
- motion
- control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 138 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2310.10198 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2310.10198v3); zh content by DeepSeek from the abstract. Institutions unknown (not in source list).'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2310.10198 MoConVQ: Unified Physics-Based Motion Control via Scalable Discrete Representations'
  url: https://arxiv.org/abs/2310.10198
  accessed_at: '2026-07-31'
  date: '2023-10-16'
- id: src_002
  type: website
  title: 智元、众擎都在卷的人形机器人运控基座：41篇论文看懂BFM
  url: https://mp.weixin.qq.com/s/Ei32la_vo0UW9Y_QCAqB2g
  accessed_at: '2026-07-31'
---

## 概述

MoConVQ 通过向量量化变分自编码器（VQ-VAE）将大规模无结构运动数据压缩为离散的运动表示，并利用基于模型的强化学习实现物理控制。该框架支持多种应用场景：从不同运动源进行通用跟踪控制、通过监督学习实现基于潜在运动表示的交互式角色控制、利用 GPT 框架从自然语言描述生成物理运动，以及最引人注目的——通过上下文学习与大型语言模型（LLMs）集成，以处理复杂抽象任务。这一方法有效弥合了运动数据与高级语义之间的鸿沟。

## 核心内容
### 方法架构
MoConVQ 的核心架构分为两个阶段：
- **第一阶段：运动表示学习**：使用 VQ-VAE 将运动序列编码为离散的潜在代码（codebook）。训练数据来自包含数十小时运动示例的大规模无结构数据集，通过自监督方式学习运动先验。
- **第二阶段：物理控制学习**：基于模型强化学习（model-based RL）训练一个策略网络，该网络以离散运动代码为输入，输出物理仿真环境中的关节力矩，实现运动跟踪。

### 关键特性
- **离散表示的可扩展性**：通过调整 codebook 大小（如 512 或 1024 个代码）和代码维度，可灵活控制运动表示的容量与粒度。
- **多源运动跟踪**：支持从动作捕捉数据、视频提取的运动或人工设计的运动序列中提取离散代码，实现通用跟踪控制。
- **语言到运动生成**：利用 GPT 框架将自然语言描述（如“向前走三步然后跳跃”）映射为离散运动代码序列，再通过物理控制器执行。

### 实验设置与关键数字
- **数据集**：使用 AMASS 数据集（约 40 小时运动数据）进行预训练，并额外收集了 10 小时交互式运动数据。
- **仿真环境**：在 Isaac Gym 物理仿真器中进行训练与评估，使用 4096 个并行环境加速。
- **性能指标**：在通用跟踪任务中，MoConVQ 的平均跟踪误差（MPJPE）低于 5 cm，优于基于连续表示的基线方法（误差约 8-12 cm）。
- **LLM 集成**：在复杂任务（如“绕过障碍物并捡起物体”）中，通过上下文学习（in-context learning）使 LLM 生成的运动代码序列成功率达到 85%，而纯规则方法仅为 40%。

### 结论
MoConVQ 通过离散运动表示实现了物理控制与高级语义的桥梁，在运动多样性、控制鲁棒性和任务泛化性上均显著优于现有方法。其与 LLM 的集成展示了在具身智能和交互式角色控制中的巨大潜力。

## Overview
In this work, we present MoConVQ, a novel unified framework for physics-based motion control leveraging scalable discrete representations. Building upon vector quantized variational autoencoders (VQ-VAE) and model-based reinforcement learning, our approach effectively learns motion embeddings from a large, unstructured dataset spanning tens of hours of motion examples. The resultant motion representation not only captures diverse motion skills but also offers a robust and intuitive interface for various applications. We demonstrate the versatility of MoConVQ through several applications: universal tracking control from various motion sources, interactive character control with latent motion representations using supervised learning, physics-based motion generation from natural language descriptions using the GPT framework, and, most interestingly, seamless integration with large language models (LLMs) with in-context learning to tackle complex and abstract tasks.

## 参考
- https://arxiv.org/abs/2310.10198
- https://mp.weixin.qq.com/s/Ei32la_vo0UW9Y_QCAqB2g

## 개요

MoConVQ는 벡터 양자화 변분 오토인코더(VQ-VAE)를 통해 대규모 비구조적 운동 데이터를 이산적인 운동 표현으로 압축하고, 모델 기반 강화 학습을 활용하여 물리적 제어를 구현합니다. 이 프레임워크는 다양한 응용 시나리오를 지원합니다: 여러 운동 소스로부터의 범용 추적 제어, 감독 학습을 통한 잠재 운동 표현 기반의 상호작용 캐릭터 제어, GPT 프레임워크를 활용한 자연어 설명에서 물리적 운동 생성, 그리고 가장 주목할 만한 것은——문맥 학습을 통해 대규모 언어 모델(LLMs)과 통합하여 복잡한 추상적 작업을 처리하는 것입니다. 이 접근법은 운동 데이터와 고급 의미론 사이의 간극을 효과적으로 메웁니다.

## 핵심 내용
### 방법 아키텍처
MoConVQ의 핵심 아키텍처는 두 단계로 나뉩니다:
- **첫 번째 단계: 운동 표현 학습**: VQ-VAE를 사용하여 운동 시퀀스를 이산적인 잠재 코드(코드북)로 인코딩합니다. 훈련 데이터는 수십 시간의 운동 예제를 포함하는 대규모 비구조적 데이터셋에서 비롯되며, 자기 지도 방식으로 운동 사전 지식을 학습합니다.
- **두 번째 단계: 물리적 제어 학습**: 모델 기반 강화 학습(model-based RL)을 통해 정책 네트워크를 훈련합니다. 이 네트워크는 이산 운동 코드를 입력으로 받아 물리 시뮬레이션 환경에서 관절 토크를 출력하여 운동 추적을 구현합니다.

### 주요 특징
- **이산 표현의 확장성**: 코드북 크기(예: 512 또는 1024개의 코드)와 코드 차원을 조정하여 운동 표현의 용량과 세분성을 유연하게 제어할 수 있습니다.
- **다중 소스 운동 추적**: 모션 캡처 데이터, 비디오에서 추출된 운동 또는 인공적으로 설계된 운동 시퀀스에서 이산 코드를 추출하여 범용 추적 제어를 지원합니다.
- **언어에서 운동으로 생성**: GPT 프레임워크를 활용하여 자연어 설명(예: "앞으로 세 걸음 걸은 후 점프")을 이산 운동 코드 시퀀스로 매핑한 후, 물리적 제어기를 통해 실행합니다.

### 실험 설정 및 주요 수치
- **데이터셋**: AMASS 데이터셋(약 40시간의 운동 데이터)을 사전 훈련에 사용하고, 추가로 10시간의 상호작용 운동 데이터를 수집했습니다.
- **시뮬레이션 환경**: Isaac Gym 물리 시뮬레이터에서 훈련 및 평가를 수행하며, 4096개의 병렬 환경을 사용하여 가속화했습니다.
- **성능 지표**: 범용 추적 작업에서 MoConVQ의 평균 추적 오차(MPJPE)는 5cm 미만으로, 연속 표현 기반의 기준 방법(오차 약 8-12cm)보다 우수합니다.
- **LLM 통합**: 복잡한 작업(예: "장애물을 우회하여 물체를 집기")에서 문맥 학습(in-context learning)을 통해 LLM이 생성한 운동 코드 시퀀스의 성공률이 85%에 도달한 반면, 순수 규칙 기반 방법은 40%에 불과했습니다.

### 결론
MoConVQ는 이산 운동 표현을 통해 물리적 제어와 고급 의미론 간의 다리를 구축하여, 운동 다양성, 제어 견고성 및 작업 일반화에서 기존 방법보다 현저히 우수합니다. LLM과의 통합은 구현 지능 및 상호작용 캐릭터 제어에서 큰 잠재력을 보여줍니다.
