---
$id: ent_paper_neau_grasp_vla_graph_based_symbolic_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GraSP-VLA: Graph-based Symbolic Action Representation for Long-Horizon Planning with VLA Policies'
  zh: GraSP-VLA
  ko: 'GraSP-VLA: Graph-based Symbolic Action Representation for Long-Horizon Planning with VLA Policies'
summary:
  en: 'GraSP-VLA: Graph-based Symbolic Action Representation for Long-Horizon Planning with VLA Policies (GraSP-VLA), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Umeå University, PrioriAnalytica, Bretagne
    INP - ENIB, IMT Atlantique, CNRS IRL 2010 CROSSING.'
  zh: 'GraSP-VLA: Graph-based Symbolic Action Representation for Long-Horizon Planning with VLA Policies (GraSP-VLA), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Umeå University, PrioriAnalytica, Bretagne
    INP - ENIB, IMT Atlantique, CNRS IRL 2010 CROSSING.'
  ko: 'GraSP-VLA: Graph-based Symbolic Action Representation for Long-Horizon Planning with VLA Policies (GraSP-VLA), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Umeå University, PrioriAnalytica, Bretagne
    INP - ENIB, IMT Atlantique, CNRS IRL 2010 CROSSING.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- grasp_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.04357v1.
sources:
- id: src_001
  type: paper
  title: 'GraSP-VLA: Graph-based Symbolic Action Representation for Long-Horizon Planning with VLA Policies (arXiv)'
  url: https://arxiv.org/abs/2511.04357
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: GraSP-VLA source
  url: https://doi.org/10.48550/arXiv.2511.04357
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Deploying autonomous robots that can learn new skills from demonstrations is an important challenge of modern robotics. Existing solutions often apply end-to-end imitation learning with Vision-Language Action (VLA) models or symbolic approaches with Action Model Learning (AML). On the one hand, current VLA models are limited by the lack of high-level symbolic planning, which hinders their abilities in long-horizon tasks. On the other hand, symbolic approaches in AML lack generalization and scalability perspectives. In this paper we present a new neuro-symbolic approach, GraSP-VLA, a framework that uses a Continuous Scene Graph representation to generate a symbolic representation of human demonstrations. This representation is used to generate new planning domains during inference and serves as an orchestrator for low-level VLA policies, scaling up the number of actions that can be reproduced in a row. Our results show that GraSP-VLA is effective for modeling symbolic representations on the task of automatic planning domain generation from observations. In addition, results on real-world experiments show the potential of our Continuous Scene Graph representation to orchestrate low-level VLA policies in long-horizon tasks.

## 核心内容
Deploying autonomous robots that can learn new skills from demonstrations is an important challenge of modern robotics. Existing solutions often apply end-to-end imitation learning with Vision-Language Action (VLA) models or symbolic approaches with Action Model Learning (AML). On the one hand, current VLA models are limited by the lack of high-level symbolic planning, which hinders their abilities in long-horizon tasks. On the other hand, symbolic approaches in AML lack generalization and scalability perspectives. In this paper we present a new neuro-symbolic approach, GraSP-VLA, a framework that uses a Continuous Scene Graph representation to generate a symbolic representation of human demonstrations. This representation is used to generate new planning domains during inference and serves as an orchestrator for low-level VLA policies, scaling up the number of actions that can be reproduced in a row. Our results show that GraSP-VLA is effective for modeling symbolic representations on the task of automatic planning domain generation from observations. In addition, results on real-world experiments show the potential of our Continuous Scene Graph representation to orchestrate low-level VLA policies in long-horizon tasks.

## 参考
- http://arxiv.org/abs/2511.04357v1

## Overview
Deploying autonomous robots that can learn new skills from demonstrations is an important challenge of modern robotics. Existing solutions often apply end-to-end imitation learning with Vision-Language Action (VLA) models or symbolic approaches with Action Model Learning (AML). On the one hand, current VLA models are limited by the lack of high-level symbolic planning, which hinders their abilities in long-horizon tasks. On the other hand, symbolic approaches in AML lack generalization and scalability perspectives. In this paper we present a new neuro-symbolic approach, GraSP-VLA, a framework that uses a Continuous Scene Graph representation to generate a symbolic representation of human demonstrations. This representation is used to generate new planning domains during inference and serves as an orchestrator for low-level VLA policies, scaling up the number of actions that can be reproduced in a row. Our results show that GraSP-VLA is effective for modeling symbolic representations on the task of automatic planning domain generation from observations. In addition, results on real-world experiments show the potential of our Continuous Scene Graph representation to orchestrate low-level VLA policies in long-horizon tasks.

## Content
Deploying autonomous robots that can learn new skills from demonstrations is an important challenge of modern robotics. Existing solutions often apply end-to-end imitation learning with Vision-Language Action (VLA) models or symbolic approaches with Action Model Learning (AML). On the one hand, current VLA models are limited by the lack of high-level symbolic planning, which hinders their abilities in long-horizon tasks. On the other hand, symbolic approaches in AML lack generalization and scalability perspectives. In this paper we present a new neuro-symbolic approach, GraSP-VLA, a framework that uses a Continuous Scene Graph representation to generate a symbolic representation of human demonstrations. This representation is used to generate new planning domains during inference and serves as an orchestrator for low-level VLA policies, scaling up the number of actions that can be reproduced in a row. Our results show that GraSP-VLA is effective for modeling symbolic representations on the task of automatic planning domain generation from observations. In addition, results on real-world experiments show the potential of our Continuous Scene Graph representation to orchestrate low-level VLA policies in long-horizon tasks.

## 개요
시연을 통해 새로운 기술을 학습할 수 있는 자율 로봇을 배치하는 것은 현대 로봇 공학의 중요한 과제입니다. 기존 솔루션은 종종 Vision-Language Action(VLA) 모델을 사용한 엔드투엔드 모방 학습이나 Action Model Learning(AML)을 사용한 기호적 접근 방식을 적용합니다. 한편으로, 현재 VLA 모델은 고수준 기호 계획의 부족으로 인해 제한되며, 이는 장기 과제에서의 능력을 저해합니다. 다른 한편으로, AML의 기호적 접근 방식은 일반화 및 확장성 측면에서 부족합니다. 본 논문에서는 새로운 신경-기호 접근 방식인 GraSP-VLA를 제시합니다. 이 프레임워크는 연속 장면 그래프(Continuous Scene Graph) 표현을 사용하여 인간 시연의 기호적 표현을 생성합니다. 이 표현은 추론 중에 새로운 계획 도메인을 생성하는 데 사용되며, 저수준 VLA 정책을 조율하는 오케스트레이터 역할을 하여 연속적으로 재현할 수 있는 행동 수를 확장합니다. 우리의 결과는 GraSP-VLA가 관찰로부터 자동 계획 도메인 생성 작업에서 기호적 표현을 모델링하는 데 효과적임을 보여줍니다. 또한, 실제 실험 결과는 연속 장면 그래프 표현이 장기 과제에서 저수준 VLA 정책을 조율할 수 있는 잠재력을 보여줍니다.

## 핵심 내용
시연을 통해 새로운 기술을 학습할 수 있는 자율 로봇을 배치하는 것은 현대 로봇 공학의 중요한 과제입니다. 기존 솔루션은 종종 Vision-Language Action(VLA) 모델을 사용한 엔드투엔드 모방 학습이나 Action Model Learning(AML)을 사용한 기호적 접근 방식을 적용합니다. 한편으로, 현재 VLA 모델은 고수준 기호 계획의 부족으로 인해 제한되며, 이는 장기 과제에서의 능력을 저해합니다. 다른 한편으로, AML의 기호적 접근 방식은 일반화 및 확장성 측면에서 부족합니다. 본 논문에서는 새로운 신경-기호 접근 방식인 GraSP-VLA를 제시합니다. 이 프레임워크는 연속 장면 그래프(Continuous Scene Graph) 표현을 사용하여 인간 시연의 기호적 표현을 생성합니다. 이 표현은 추론 중에 새로운 계획 도메인을 생성하는 데 사용되며, 저수준 VLA 정책을 조율하는 오케스트레이터 역할을 하여 연속적으로 재현할 수 있는 행동 수를 확장합니다. 우리의 결과는 GraSP-VLA가 관찰로부터 자동 계획 도메인 생성 작업에서 기호적 표현을 모델링하는 데 효과적임을 보여줍니다. 또한, 실제 실험 결과는 연속 장면 그래프 표현이 장기 과제에서 저수준 VLA 정책을 조율할 수 있는 잠재력을 보여줍니다.
