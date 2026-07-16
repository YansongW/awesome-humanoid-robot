---
$id: ent_paper_zhang_uni_navid_a_video_based_vision_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks'
  zh: Uni-NaVid
  ko: 'Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks'
summary:
  en: 'Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks (Uni-NaVid), is a 2024
    large vision-language-action model for robotic manipulation, introduced by CFCS, School of Computer Science, Peking University,
    Galbot, Beijing Academy of Artificial Intelligence, and published at RSS25.'
  zh: 'Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks (Uni-NaVid), is a 2024
    large vision-language-action model for robotic manipulation, introduced by CFCS, School of Computer Science, Peking University,
    Galbot, Beijing Academy of Artificial Intelligence, and published at RSS25.'
  ko: 'Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks (Uni-NaVid), is a 2024
    large vision-language-action model for robotic manipulation, introduced by CFCS, School of Computer Science, Peking University,
    Galbot, Beijing Academy of Artificial Intelligence, and published at RSS25.'
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
- uni_navid
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.06224v2.
sources:
- id: src_001
  type: paper
  title: 'Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks (arXiv)'
  url: https://arxiv.org/abs/2412.06224
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Uni-NaVid source
  url: https://doi.org/10.48550/arXiv.2412.06224
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
A practical navigation agent must be capable of handling a wide range of interaction demands, such as following instructions, searching objects, answering questions, tracking people, and more. Existing models for embodied navigation fall short of serving as practical generalists in the real world, as they are often constrained by specific task configurations or pre-defined maps with discretized waypoints. In this work, we present Uni-NaVid, the first video-based vision-language-action (VLA) model designed to unify diverse embodied navigation tasks and enable seamless navigation for mixed long-horizon tasks in unseen real-world environments. Uni-NaVid achieves this by harmonizing the input and output data configurations for all commonly used embodied navigation tasks and thereby integrating all tasks in one model. For training Uni-NaVid, we collect 3.6 million navigation data samples in total from four essential navigation sub-tasks and foster synergy in learning across them. Extensive experiments on comprehensive navigation benchmarks clearly demonstrate the advantages of unification modeling in Uni-NaVid and show it achieves state-of-the-art performance. Additionally, real-world experiments confirm the model's effectiveness and efficiency, shedding light on its strong generalizability.

## 核心内容
A practical navigation agent must be capable of handling a wide range of interaction demands, such as following instructions, searching objects, answering questions, tracking people, and more. Existing models for embodied navigation fall short of serving as practical generalists in the real world, as they are often constrained by specific task configurations or pre-defined maps with discretized waypoints. In this work, we present Uni-NaVid, the first video-based vision-language-action (VLA) model designed to unify diverse embodied navigation tasks and enable seamless navigation for mixed long-horizon tasks in unseen real-world environments. Uni-NaVid achieves this by harmonizing the input and output data configurations for all commonly used embodied navigation tasks and thereby integrating all tasks in one model. For training Uni-NaVid, we collect 3.6 million navigation data samples in total from four essential navigation sub-tasks and foster synergy in learning across them. Extensive experiments on comprehensive navigation benchmarks clearly demonstrate the advantages of unification modeling in Uni-NaVid and show it achieves state-of-the-art performance. Additionally, real-world experiments confirm the model's effectiveness and efficiency, shedding light on its strong generalizability.

## 参考
- http://arxiv.org/abs/2412.06224v2

## Overview
A practical navigation agent must be capable of handling a wide range of interaction demands, such as following instructions, searching objects, answering questions, tracking people, and more. Existing models for embodied navigation fall short of serving as practical generalists in the real world, as they are often constrained by specific task configurations or pre-defined maps with discretized waypoints. In this work, we present Uni-NaVid, the first video-based vision-language-action (VLA) model designed to unify diverse embodied navigation tasks and enable seamless navigation for mixed long-horizon tasks in unseen real-world environments. Uni-NaVid achieves this by harmonizing the input and output data configurations for all commonly used embodied navigation tasks and thereby integrating all tasks in one model. For training Uni-NaVid, we collect 3.6 million navigation data samples in total from four essential navigation sub-tasks and foster synergy in learning across them. Extensive experiments on comprehensive navigation benchmarks clearly demonstrate the advantages of unification modeling in Uni-NaVid and show it achieves state-of-the-art performance. Additionally, real-world experiments confirm the model's effectiveness and efficiency, shedding light on its strong generalizability.

## Content
A practical navigation agent must be capable of handling a wide range of interaction demands, such as following instructions, searching objects, answering questions, tracking people, and more. Existing models for embodied navigation fall short of serving as practical generalists in the real world, as they are often constrained by specific task configurations or pre-defined maps with discretized waypoints. In this work, we present Uni-NaVid, the first video-based vision-language-action (VLA) model designed to unify diverse embodied navigation tasks and enable seamless navigation for mixed long-horizon tasks in unseen real-world environments. Uni-NaVid achieves this by harmonizing the input and output data configurations for all commonly used embodied navigation tasks and thereby integrating all tasks in one model. For training Uni-NaVid, we collect 3.6 million navigation data samples in total from four essential navigation sub-tasks and foster synergy in learning across them. Extensive experiments on comprehensive navigation benchmarks clearly demonstrate the advantages of unification modeling in Uni-NaVid and show it achieves state-of-the-art performance. Additionally, real-world experiments confirm the model's effectiveness and efficiency, shedding light on its strong generalizability.

## 개요
실용적인 내비게이션 에이전트는 지시 따르기, 객체 검색, 질문 응답, 사람 추적 등 다양한 상호작용 요구를 처리할 수 있어야 합니다. 기존의 체화된 내비게이션 모델은 특정 작업 구성이나 이산화된 웨이포인트가 있는 사전 정의된 지도에 제한되어 실제 세계에서 실용적인 범용 모델로 기능하기에 부족합니다. 본 연구에서는 다양한 체화된 내비게이션 작업을 통합하고, 보지 못한 실제 환경에서 혼합된 장기적 작업을 원활하게 내비게이션할 수 있는 최초의 비디오 기반 시각-언어-행동(VLA) 모델인 Uni-NaVid를 제시합니다. Uni-NaVid는 모든 일반적으로 사용되는 체화된 내비게이션 작업의 입력 및 출력 데이터 구성을 조화시켜 하나의 모델에 모든 작업을 통합함으로써 이를 달성합니다. Uni-NaVid 훈련을 위해, 우리는 네 가지 필수 내비게이션 하위 작업에서 총 360만 개의 내비게이션 데이터 샘플을 수집하고, 이들 간의 학습 시너지를 촉진했습니다. 포괄적인 내비게이션 벤치마크에 대한 광범위한 실험은 Uni-NaVid에서 통합 모델링의 장점을 명확히 보여주며, 최첨단 성능을 달성함을 입증합니다. 또한, 실제 환경 실험은 모델의 효과성과 효율성을 확인하며, 강력한 일반화 가능성을 시사합니다.

## 핵심 내용
실용적인 내비게이션 에이전트는 지시 따르기, 객체 검색, 질문 응답, 사람 추적 등 다양한 상호작용 요구를 처리할 수 있어야 합니다. 기존의 체화된 내비게이션 모델은 특정 작업 구성이나 이산화된 웨이포인트가 있는 사전 정의된 지도에 제한되어 실제 세계에서 실용적인 범용 모델로 기능하기에 부족합니다. 본 연구에서는 다양한 체화된 내비게이션 작업을 통합하고, 보지 못한 실제 환경에서 혼합된 장기적 작업을 원활하게 내비게이션할 수 있는 최초의 비디오 기반 시각-언어-행동(VLA) 모델인 Uni-NaVid를 제시합니다. Uni-NaVid는 모든 일반적으로 사용되는 체화된 내비게이션 작업의 입력 및 출력 데이터 구성을 조화시켜 하나의 모델에 모든 작업을 통합함으로써 이를 달성합니다. Uni-NaVid 훈련을 위해, 우리는 네 가지 필수 내비게이션 하위 작업에서 총 360만 개의 내비게이션 데이터 샘플을 수집하고, 이들 간의 학습 시너지를 촉진했습니다. 포괄적인 내비게이션 벤치마크에 대한 광범위한 실험은 Uni-NaVid에서 통합 모델링의 장점을 명확히 보여주며, 최첨단 성능을 달성함을 입증합니다. 또한, 실제 환경 실험은 모델의 효과성과 효율성을 확인하며, 강력한 일반화 가능성을 시사합니다.
