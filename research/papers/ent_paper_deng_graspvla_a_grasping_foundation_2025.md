---
$id: ent_paper_deng_graspvla_a_grasping_foundation_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data'
  zh: GraspVLA
  ko: 'GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data'
summary:
  en: 'GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data (GraspVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Galbot, Peking University, The University of Hong
    Kong, Beijing Academy of Artificial Intelligence, and published at CoRL25.'
  zh: 'GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data (GraspVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Galbot, Peking University, The University of Hong
    Kong, Beijing Academy of Artificial Intelligence, and published at CoRL25.'
  ko: 'GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data (GraspVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Galbot, Peking University, The University of Hong
    Kong, Beijing Academy of Artificial Intelligence, and published at CoRL25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- graspvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.03233v3.
sources:
- id: src_001
  type: paper
  title: 'GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data (arXiv)'
  url: https://arxiv.org/abs/2505.03233
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: GraspVLA source
  url: https://doi.org/10.48550/arXiv.2505.03233
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Embodied foundation models are gaining increasing attention for their zero-shot generalization, scalability, and adaptability to new tasks through few-shot post-training. However, existing models rely heavily on real-world data, which is costly and labor-intensive to collect. Synthetic data offers a cost-effective alternative, yet its potential remains largely underexplored. To bridge this gap, we explore the feasibility of training Vision-Language-Action models entirely with large-scale synthetic action data. We curate SynGrasp-1B, a billion-frame robotic grasping dataset generated in simulation with photorealistic rendering and extensive domain randomization. Building on this, we present GraspVLA, a VLA model pretrained on large-scale synthetic action data as a foundational model for grasping tasks. GraspVLA integrates autoregressive perception tasks and flow-matching-based action generation into a unified Chain-of-Thought process, enabling joint training on synthetic action data and Internet semantics data. This design helps mitigate sim-to-real gaps and facilitates the transfer of learned actions to a broader range of Internet-covered objects, achieving open-vocabulary generalization in grasping. Extensive evaluations across real-world and simulation benchmarks demonstrate GraspVLA's advanced zero-shot generalizability and few-shot adaptability to specific human preferences. We will release SynGrasp-1B dataset and pre-trained weights to benefit the community.

## 核心内容
Embodied foundation models are gaining increasing attention for their zero-shot generalization, scalability, and adaptability to new tasks through few-shot post-training. However, existing models rely heavily on real-world data, which is costly and labor-intensive to collect. Synthetic data offers a cost-effective alternative, yet its potential remains largely underexplored. To bridge this gap, we explore the feasibility of training Vision-Language-Action models entirely with large-scale synthetic action data. We curate SynGrasp-1B, a billion-frame robotic grasping dataset generated in simulation with photorealistic rendering and extensive domain randomization. Building on this, we present GraspVLA, a VLA model pretrained on large-scale synthetic action data as a foundational model for grasping tasks. GraspVLA integrates autoregressive perception tasks and flow-matching-based action generation into a unified Chain-of-Thought process, enabling joint training on synthetic action data and Internet semantics data. This design helps mitigate sim-to-real gaps and facilitates the transfer of learned actions to a broader range of Internet-covered objects, achieving open-vocabulary generalization in grasping. Extensive evaluations across real-world and simulation benchmarks demonstrate GraspVLA's advanced zero-shot generalizability and few-shot adaptability to specific human preferences. We will release SynGrasp-1B dataset and pre-trained weights to benefit the community.

## 参考
- http://arxiv.org/abs/2505.03233v3

## Overview
Embodied foundation models are gaining increasing attention for their zero-shot generalization, scalability, and adaptability to new tasks through few-shot post-training. However, existing models rely heavily on real-world data, which is costly and labor-intensive to collect. Synthetic data offers a cost-effective alternative, yet its potential remains largely underexplored. To bridge this gap, we explore the feasibility of training Vision-Language-Action models entirely with large-scale synthetic action data. We curate SynGrasp-1B, a billion-frame robotic grasping dataset generated in simulation with photorealistic rendering and extensive domain randomization. Building on this, we present GraspVLA, a VLA model pretrained on large-scale synthetic action data as a foundational model for grasping tasks. GraspVLA integrates autoregressive perception tasks and flow-matching-based action generation into a unified Chain-of-Thought process, enabling joint training on synthetic action data and Internet semantics data. This design helps mitigate sim-to-real gaps and facilitates the transfer of learned actions to a broader range of Internet-covered objects, achieving open-vocabulary generalization in grasping. Extensive evaluations across real-world and simulation benchmarks demonstrate GraspVLA's advanced zero-shot generalizability and few-shot adaptability to specific human preferences. We will release SynGrasp-1B dataset and pre-trained weights to benefit the community.

## Content
Embodied foundation models are gaining increasing attention for their zero-shot generalization, scalability, and adaptability to new tasks through few-shot post-training. However, existing models rely heavily on real-world data, which is costly and labor-intensive to collect. Synthetic data offers a cost-effective alternative, yet its potential remains largely underexplored. To bridge this gap, we explore the feasibility of training Vision-Language-Action models entirely with large-scale synthetic action data. We curate SynGrasp-1B, a billion-frame robotic grasping dataset generated in simulation with photorealistic rendering and extensive domain randomization. Building on this, we present GraspVLA, a VLA model pretrained on large-scale synthetic action data as a foundational model for grasping tasks. GraspVLA integrates autoregressive perception tasks and flow-matching-based action generation into a unified Chain-of-Thought process, enabling joint training on synthetic action data and Internet semantics data. This design helps mitigate sim-to-real gaps and facilitates the transfer of learned actions to a broader range of Internet-covered objects, achieving open-vocabulary generalization in grasping. Extensive evaluations across real-world and simulation benchmarks demonstrate GraspVLA's advanced zero-shot generalizability and few-shot adaptability to specific human preferences. We will release SynGrasp-1B dataset and pre-trained weights to benefit the community.

## 개요
Embodied foundation models는 제로샷 일반화, 확장성, 그리고 소수의 샷 후속 훈련을 통한 새로운 작업 적응 능력으로 점점 더 주목받고 있습니다. 그러나 기존 모델은 수집 비용과 노동력이 많이 드는 실제 데이터에 크게 의존합니다. 합성 데이터는 비용 효율적인 대안을 제공하지만, 그 잠재력은 아직 충분히 탐구되지 않았습니다. 이러한 격차를 해소하기 위해, 우리는 대규모 합성 행동 데이터만으로 Vision-Language-Action 모델을 완전히 훈련하는 가능성을 탐구합니다. 우리는 사실적인 렌더링과 광범위한 도메인 무작위화를 통해 시뮬레이션에서 생성된 10억 프레임의 로봇 파지 데이터셋인 SynGrasp-1B를 큐레이션했습니다. 이를 바탕으로, 우리는 파지 작업을 위한 기초 모델로서 대규모 합성 행동 데이터로 사전 훈련된 VLA 모델인 GraspVLA를 제시합니다. GraspVLA는 자기회귀적 인식 작업과 흐름 매칭 기반 행동 생성을 통합된 Chain-of-Thought 프로세스로 통합하여, 합성 행동 데이터와 인터넷 의미 데이터에 대한 공동 훈련을 가능하게 합니다. 이 설계는 시뮬레이션-실제 격차를 완화하고 학습된 행동을 더 넓은 범위의 인터넷 적용 객체로 전이하여, 파지에서 개방형 어휘 일반화를 달성하는 데 도움을 줍니다. 실제 환경 및 시뮬레이션 벤치마크에 걸친 광범위한 평가는 GraspVLA의 고급 제로샷 일반화 능력과 특정 인간 선호도에 대한 소수의 샷 적응 능력을 입증합니다. 우리는 SynGrasp-1B 데이터셋과 사전 훈련된 가중치를 커뮤니티에 공개할 예정입니다.

## 핵심 내용
Embodied foundation models는 제로샷 일반화, 확장성, 그리고 소수의 샷 후속 훈련을 통한 새로운 작업 적응 능력으로 점점 더 주목받고 있습니다. 그러나 기존 모델은 수집 비용과 노동력이 많이 드는 실제 데이터에 크게 의존합니다. 합성 데이터는 비용 효율적인 대안을 제공하지만, 그 잠재력은 아직 충분히 탐구되지 않았습니다. 이러한 격차를 해소하기 위해, 우리는 대규모 합성 행동 데이터만으로 Vision-Language-Action 모델을 완전히 훈련하는 가능성을 탐구합니다. 우리는 사실적인 렌더링과 광범위한 도메인 무작위화를 통해 시뮬레이션에서 생성된 10억 프레임의 로봇 파지 데이터셋인 SynGrasp-1B를 큐레이션했습니다. 이를 바탕으로, 우리는 파지 작업을 위한 기초 모델로서 대규모 합성 행동 데이터로 사전 훈련된 VLA 모델인 GraspVLA를 제시합니다. GraspVLA는 자기회귀적 인식 작업과 흐름 매칭 기반 행동 생성을 통합된 Chain-of-Thought 프로세스로 통합하여, 합성 행동 데이터와 인터넷 의미 데이터에 대한 공동 훈련을 가능하게 합니다. 이 설계는 시뮬레이션-실제 격차를 완화하고 학습된 행동을 더 넓은 범위의 인터넷 적용 객체로 전이하여, 파지에서 개방형 어휘 일반화를 달성하는 데 도움을 줍니다. 실제 환경 및 시뮬레이션 벤치마크에 걸친 광범위한 평가는 GraspVLA의 고급 제로샷 일반화 능력과 특정 인간 선호도에 대한 소수의 샷 적응 능력을 입증합니다. 우리는 SynGrasp-1B 데이터셋과 사전 훈련된 가중치를 커뮤니티에 공개할 예정입니다.
