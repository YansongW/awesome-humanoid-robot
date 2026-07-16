---
$id: ent_paper_sun_transforming_monolithic_founda_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Transforming Monolithic Foundation Models into Embodied Multi-Agent Architectures for Human-Robot Collaboration
  zh: InteractGen
  ko: Transforming Monolithic Foundation Models into Embodied Multi-Agent Architectures for Human-Robot Collaboration
summary:
  en: Transforming Monolithic Foundation Models into Embodied Multi-Agent Architectures for Human-Robot Collaboration (InteractGen),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, Beijing University
    of Posts and Telecommunications.
  zh: Transforming Monolithic Foundation Models into Embodied Multi-Agent Architectures for Human-Robot Collaboration (InteractGen),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, Beijing University
    of Posts and Telecommunications.
  ko: Transforming Monolithic Foundation Models into Embodied Multi-Agent Architectures for Human-Robot Collaboration (InteractGen),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, Beijing University
    of Posts and Telecommunications.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- interactgen
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.00797v1.
sources:
- id: src_001
  type: paper
  title: Transforming Monolithic Foundation Models into Embodied Multi-Agent Architectures for Human-Robot Collaboration (arXiv)
  url: https://arxiv.org/abs/2512.00797
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: InteractGen source
  url: https://doi.org/10.48550/arXiv.2512.00797
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Foundation models have become central to unifying perception and planning in robotics, yet real-world deployment exposes a mismatch between their monolithic assumption that a single model can handle all cognitive functions and the distributed, dynamic nature of practical service workflows. Vision-language models offer strong semantic understanding but lack embodiment-aware action capabilities while relying on hand-crafted skills. Vision-Language-Action policies enable reactive manipulation but remain brittle across embodiments, weak in geometric grounding, and devoid of proactive collaboration mechanisms. These limitations indicate that scaling a single model alone cannot deliver reliable autonomy for service robots operating in human-populated settings. To address this gap, we present InteractGen, an LLM-powered multi-agent framework that decomposes robot intelligence into specialized agents for continuous perception, dependency-aware planning, decision and verification, failure reflection, and dynamic human delegation, treating foundation models as regulated components within a closed-loop collective. Deployed on a heterogeneous robot team and evaluated in a three-month open-use study, InteractGen improves task success, adaptability, and human-robot collaboration, providing evidence that multi-agent orchestration offers a more feasible path toward socially grounded service autonomy than further scaling standalone models.

## 核心内容
Foundation models have become central to unifying perception and planning in robotics, yet real-world deployment exposes a mismatch between their monolithic assumption that a single model can handle all cognitive functions and the distributed, dynamic nature of practical service workflows. Vision-language models offer strong semantic understanding but lack embodiment-aware action capabilities while relying on hand-crafted skills. Vision-Language-Action policies enable reactive manipulation but remain brittle across embodiments, weak in geometric grounding, and devoid of proactive collaboration mechanisms. These limitations indicate that scaling a single model alone cannot deliver reliable autonomy for service robots operating in human-populated settings. To address this gap, we present InteractGen, an LLM-powered multi-agent framework that decomposes robot intelligence into specialized agents for continuous perception, dependency-aware planning, decision and verification, failure reflection, and dynamic human delegation, treating foundation models as regulated components within a closed-loop collective. Deployed on a heterogeneous robot team and evaluated in a three-month open-use study, InteractGen improves task success, adaptability, and human-robot collaboration, providing evidence that multi-agent orchestration offers a more feasible path toward socially grounded service autonomy than further scaling standalone models.

## 参考
- http://arxiv.org/abs/2512.00797v1

## Overview
Foundation models have become central to unifying perception and planning in robotics, yet real-world deployment exposes a mismatch between their monolithic assumption that a single model can handle all cognitive functions and the distributed, dynamic nature of practical service workflows. Vision-language models offer strong semantic understanding but lack embodiment-aware action capabilities while relying on hand-crafted skills. Vision-Language-Action policies enable reactive manipulation but remain brittle across embodiments, weak in geometric grounding, and devoid of proactive collaboration mechanisms. These limitations indicate that scaling a single model alone cannot deliver reliable autonomy for service robots operating in human-populated settings. To address this gap, we present InteractGen, an LLM-powered multi-agent framework that decomposes robot intelligence into specialized agents for continuous perception, dependency-aware planning, decision and verification, failure reflection, and dynamic human delegation, treating foundation models as regulated components within a closed-loop collective. Deployed on a heterogeneous robot team and evaluated in a three-month open-use study, InteractGen improves task success, adaptability, and human-robot collaboration, providing evidence that multi-agent orchestration offers a more feasible path toward socially grounded service autonomy than further scaling standalone models.

## Content
Foundation models have become central to unifying perception and planning in robotics, yet real-world deployment exposes a mismatch between their monolithic assumption that a single model can handle all cognitive functions and the distributed, dynamic nature of practical service workflows. Vision-language models offer strong semantic understanding but lack embodiment-aware action capabilities while relying on hand-crafted skills. Vision-Language-Action policies enable reactive manipulation but remain brittle across embodiments, weak in geometric grounding, and devoid of proactive collaboration mechanisms. These limitations indicate that scaling a single model alone cannot deliver reliable autonomy for service robots operating in human-populated settings. To address this gap, we present InteractGen, an LLM-powered multi-agent framework that decomposes robot intelligence into specialized agents for continuous perception, dependency-aware planning, decision and verification, failure reflection, and dynamic human delegation, treating foundation models as regulated components within a closed-loop collective. Deployed on a heterogeneous robot team and evaluated in a three-month open-use study, InteractGen improves task success, adaptability, and human-robot collaboration, providing evidence that multi-agent orchestration offers a more feasible path toward socially grounded service autonomy than further scaling standalone models.

## 개요
Foundation models은 로봇 공학에서 인식과 계획을 통합하는 핵심이 되었지만, 실제 배포에서는 단일 모델이 모든 인지 기능을 처리할 수 있다는 모놀리식 가정과 실제 서비스 워크플로우의 분산되고 동적인 특성 간의 불일치가 드러납니다. Vision-language models은 강력한 의미 이해를 제공하지만, 수작업으로 제작된 기술에 의존하면서 체화 인식 행동 능력이 부족합니다. Vision-Language-Action 정책은 반응적 조작을 가능하게 하지만, 체화 간 취약성, 기하학적 근거 부족, 그리고 사전 협력 메커니즘의 결여를 보입니다. 이러한 한계는 단일 모델을 확장하는 것만으로는 인간이 거주하는 환경에서 작동하는 서비스 로봇에 신뢰할 수 있는 자율성을 제공할 수 없음을 시사합니다. 이 격차를 해결하기 위해, 우리는 InteractGen을 제시합니다. 이는 LLM 기반의 다중 에이전트 프레임워크로, 로봇 지능을 지속적 인식, 의존성 인식 계획, 결정 및 검증, 실패 반성, 동적 인간 위임을 위한 특화된 에이전트로 분해하며, foundation models을 폐쇄 루프 집단 내에서 규제된 구성 요소로 취급합니다. 이질적 로봇 팀에 배포되고 3개월간의 공개 사용 연구에서 평가된 InteractGen은 작업 성공, 적응성, 인간-로봇 협력을 향상시켜, 다중 에이전트 오케스트레이션이 독립형 모델을 더 확장하는 것보다 사회적 기반 서비스 자율성에 더 실현 가능한 경로를 제공한다는 증거를 제시합니다.

## 핵심 내용
Foundation models은 로봇 공학에서 인식과 계획을 통합하는 핵심이 되었지만, 실제 배포에서는 단일 모델이 모든 인지 기능을 처리할 수 있다는 모놀리식 가정과 실제 서비스 워크플로우의 분산되고 동적인 특성 간의 불일치가 드러납니다. Vision-language models은 강력한 의미 이해를 제공하지만, 수작업으로 제작된 기술에 의존하면서 체화 인식 행동 능력이 부족합니다. Vision-Language-Action 정책은 반응적 조작을 가능하게 하지만, 체화 간 취약성, 기하학적 근거 부족, 그리고 사전 협력 메커니즘의 결여를 보입니다. 이러한 한계는 단일 모델을 확장하는 것만으로는 인간이 거주하는 환경에서 작동하는 서비스 로봇에 신뢰할 수 있는 자율성을 제공할 수 없음을 시사합니다. 이 격차를 해결하기 위해, 우리는 InteractGen을 제시합니다. 이는 LLM 기반의 다중 에이전트 프레임워크로, 로봇 지능을 지속적 인식, 의존성 인식 계획, 결정 및 검증, 실패 반성, 동적 인간 위임을 위한 특화된 에이전트로 분해하며, foundation models을 폐쇄 루프 집단 내에서 규제된 구성 요소로 취급합니다. 이질적 로봇 팀에 배포되고 3개월간의 공개 사용 연구에서 평가된 InteractGen은 작업 성공, 적응성, 인간-로봇 협력을 향상시켜, 다중 에이전트 오케스트레이션이 독립형 모델을 더 확장하는 것보다 사회적 기반 서비스 자율성에 더 실현 가능한 경로를 제공한다는 증거를 제시합니다.
