---
$id: ent_paper_li_discrete_diffusion_for_reflect_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving
  zh: ReflectDrive
  ko: Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving
summary:
  en: Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving (ReflectDrive), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute for AI Industry Research.
  zh: Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving (ReflectDrive), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute for AI Industry Research.
  ko: Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving (ReflectDrive), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute for AI Industry Research.
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
- reflectdrive
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.20109v1.
sources:
- id: src_001
  type: paper
  title: Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving (arXiv)
  url: https://arxiv.org/abs/2509.20109
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ReflectDrive source
  url: https://doi.org/10.48550/arXiv.2509.20109
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
End-to-End (E2E) solutions have emerged as a mainstream approach for autonomous driving systems, with Vision-Language-Action (VLA) models representing a new paradigm that leverages pre-trained multimodal knowledge from Vision-Language Models (VLMs) to interpret and interact with complex real-world environments. However, these methods remain constrained by the limitations of imitation learning, which struggles to inherently encode physical rules during training. Existing approaches often rely on complex rule-based post-refinement, employ reinforcement learning that remains largely limited to simulation, or utilize diffusion guidance that requires computationally expensive gradient calculations. To address these challenges, we introduce ReflectDrive, a novel learning-based framework that integrates a reflection mechanism for safe trajectory generation via discrete diffusion. We first discretize the two-dimensional driving space to construct an action codebook, enabling the use of pre-trained Diffusion Language Models for planning tasks through fine-tuning. Central to our approach is a safety-aware reflection mechanism that performs iterative self-correction without gradient computation. Our method begins with goal-conditioned trajectory generation to model multi-modal driving behaviors. Based on this, we apply local search methods to identify unsafe tokens and determine feasible solutions, which then serve as safe anchors for inpainting-based regeneration. Evaluated on the NAVSIM benchmark, ReflectDrive demonstrates significant advantages in safety-critical trajectory generation, offering a scalable and reliable solution for autonomous driving systems.

## 核心内容
End-to-End (E2E) solutions have emerged as a mainstream approach for autonomous driving systems, with Vision-Language-Action (VLA) models representing a new paradigm that leverages pre-trained multimodal knowledge from Vision-Language Models (VLMs) to interpret and interact with complex real-world environments. However, these methods remain constrained by the limitations of imitation learning, which struggles to inherently encode physical rules during training. Existing approaches often rely on complex rule-based post-refinement, employ reinforcement learning that remains largely limited to simulation, or utilize diffusion guidance that requires computationally expensive gradient calculations. To address these challenges, we introduce ReflectDrive, a novel learning-based framework that integrates a reflection mechanism for safe trajectory generation via discrete diffusion. We first discretize the two-dimensional driving space to construct an action codebook, enabling the use of pre-trained Diffusion Language Models for planning tasks through fine-tuning. Central to our approach is a safety-aware reflection mechanism that performs iterative self-correction without gradient computation. Our method begins with goal-conditioned trajectory generation to model multi-modal driving behaviors. Based on this, we apply local search methods to identify unsafe tokens and determine feasible solutions, which then serve as safe anchors for inpainting-based regeneration. Evaluated on the NAVSIM benchmark, ReflectDrive demonstrates significant advantages in safety-critical trajectory generation, offering a scalable and reliable solution for autonomous driving systems.

## 参考
- http://arxiv.org/abs/2509.20109v1

## Overview
End-to-End (E2E) solutions have emerged as a mainstream approach for autonomous driving systems, with Vision-Language-Action (VLA) models representing a new paradigm that leverages pre-trained multimodal knowledge from Vision-Language Models (VLMs) to interpret and interact with complex real-world environments. However, these methods remain constrained by the limitations of imitation learning, which struggles to inherently encode physical rules during training. Existing approaches often rely on complex rule-based post-refinement, employ reinforcement learning that remains largely limited to simulation, or utilize diffusion guidance that requires computationally expensive gradient calculations. To address these challenges, we introduce ReflectDrive, a novel learning-based framework that integrates a reflection mechanism for safe trajectory generation via discrete diffusion. We first discretize the two-dimensional driving space to construct an action codebook, enabling the use of pre-trained Diffusion Language Models for planning tasks through fine-tuning. Central to our approach is a safety-aware reflection mechanism that performs iterative self-correction without gradient computation. Our method begins with goal-conditioned trajectory generation to model multi-modal driving behaviors. Based on this, we apply local search methods to identify unsafe tokens and determine feasible solutions, which then serve as safe anchors for inpainting-based regeneration. Evaluated on the NAVSIM benchmark, ReflectDrive demonstrates significant advantages in safety-critical trajectory generation, offering a scalable and reliable solution for autonomous driving systems.

## Content
End-to-End (E2E) solutions have emerged as a mainstream approach for autonomous driving systems, with Vision-Language-Action (VLA) models representing a new paradigm that leverages pre-trained multimodal knowledge from Vision-Language Models (VLMs) to interpret and interact with complex real-world environments. However, these methods remain constrained by the limitations of imitation learning, which struggles to inherently encode physical rules during training. Existing approaches often rely on complex rule-based post-refinement, employ reinforcement learning that remains largely limited to simulation, or utilize diffusion guidance that requires computationally expensive gradient calculations. To address these challenges, we introduce ReflectDrive, a novel learning-based framework that integrates a reflection mechanism for safe trajectory generation via discrete diffusion. We first discretize the two-dimensional driving space to construct an action codebook, enabling the use of pre-trained Diffusion Language Models for planning tasks through fine-tuning. Central to our approach is a safety-aware reflection mechanism that performs iterative self-correction without gradient computation. Our method begins with goal-conditioned trajectory generation to model multi-modal driving behaviors. Based on this, we apply local search methods to identify unsafe tokens and determine feasible solutions, which then serve as safe anchors for inpainting-based regeneration. Evaluated on the NAVSIM benchmark, ReflectDrive demonstrates significant advantages in safety-critical trajectory generation, offering a scalable and reliable solution for autonomous driving systems.

## 개요
엔드투엔드(E2E) 솔루션은 자율주행 시스템의 주류 접근 방식으로 부상했으며, 비전-언어-행동(VLA) 모델은 사전 훈련된 비전-언어 모델(VLM)의 멀티모달 지식을 활용하여 복잡한 실제 환경을 해석하고 상호작용하는 새로운 패러다임을 대표합니다. 그러나 이러한 방법들은 훈련 중 물리적 규칙을 본질적으로 인코딩하는 데 어려움을 겪는 모방 학습의 한계에 여전히 제약을 받습니다. 기존 접근 방식은 종종 복잡한 규칙 기반 후처리 정제에 의존하거나, 대부분 시뮬레이션에 국한된 강화 학습을 사용하거나, 계산 비용이 많이 드는 그래디언트 계산이 필요한 확산 가이던스를 활용합니다. 이러한 문제를 해결하기 위해, 우리는 이산 확산을 통해 안전한 궤적 생성을 위한 반성 메커니즘을 통합한 새로운 학습 기반 프레임워크인 ReflectDrive를 소개합니다. 먼저 2차원 주행 공간을 이산화하여 행동 코드북을 구축함으로써, 사전 훈련된 확산 언어 모델을 미세 조정을 통해 계획 작업에 사용할 수 있게 합니다. 우리 접근 방식의 핵심은 그래디언트 계산 없이 반복적인 자기 수정을 수행하는 안전 인식 반성 메커니즘입니다. 우리 방법은 목표 조건 궤적 생성을 통해 다중 모드 주행 행동을 모델링하는 것으로 시작합니다. 이를 기반으로 로컬 탐색 방법을 적용하여 안전하지 않은 토큰을 식별하고 실행 가능한 솔루션을 결정한 다음, 이는 인페인팅 기반 재생성을 위한 안전 앵커 역할을 합니다. NAVSIM 벤치마크에서 평가된 ReflectDrive는 안전이 중요한 궤적 생성에서 상당한 이점을 보여주며, 자율주행 시스템을 위한 확장 가능하고 신뢰할 수 있는 솔루션을 제공합니다.

## 핵심 내용
엔드투엔드(E2E) 솔루션은 자율주행 시스템의 주류 접근 방식으로 부상했으며, 비전-언어-행동(VLA) 모델은 사전 훈련된 비전-언어 모델(VLM)의 멀티모달 지식을 활용하여 복잡한 실제 환경을 해석하고 상호작용하는 새로운 패러다임을 대표합니다. 그러나 이러한 방법들은 훈련 중 물리적 규칙을 본질적으로 인코딩하는 데 어려움을 겪는 모방 학습의 한계에 여전히 제약을 받습니다. 기존 접근 방식은 종종 복잡한 규칙 기반 후처리 정제에 의존하거나, 대부분 시뮬레이션에 국한된 강화 학습을 사용하거나, 계산 비용이 많이 드는 그래디언트 계산이 필요한 확산 가이던스를 활용합니다. 이러한 문제를 해결하기 위해, 우리는 이산 확산을 통해 안전한 궤적 생성을 위한 반성 메커니즘을 통합한 새로운 학습 기반 프레임워크인 ReflectDrive를 소개합니다. 먼저 2차원 주행 공간을 이산화하여 행동 코드북을 구축함으로써, 사전 훈련된 확산 언어 모델을 미세 조정을 통해 계획 작업에 사용할 수 있게 합니다. 우리 접근 방식의 핵심은 그래디언트 계산 없이 반복적인 자기 수정을 수행하는 안전 인식 반성 메커니즘입니다. 우리 방법은 목표 조건 궤적 생성을 통해 다중 모드 주행 행동을 모델링하는 것으로 시작합니다. 이를 기반으로 로컬 탐색 방법을 적용하여 안전하지 않은 토큰을 식별하고 실행 가능한 솔루션을 결정한 다음, 이는 인페인팅 기반 재생성을 위한 안전 앵커 역할을 합니다. NAVSIM 벤치마크에서 평가된 ReflectDrive는 안전이 중요한 궤적 생성에서 상당한 이점을 보여주며, 자율주행 시스템을 위한 확장 가능하고 신뢰할 수 있는 솔루션을 제공합니다.
