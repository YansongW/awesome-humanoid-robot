---
$id: ent_paper_zhang_a_unified_perception_language_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Unified Perception-Language-Action Framework for Adaptive Autonomous Driving
  zh: PLA
  ko: A Unified Perception-Language-Action Framework for Adaptive Autonomous Driving
summary:
  en: A Unified Perception-Language-Action Framework for Adaptive Autonomous Driving (PLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Technical University of Munich, Chair of Robotics, Artificial Intelligence
    and Embedded Systems.
  zh: A Unified Perception-Language-Action Framework for Adaptive Autonomous Driving (PLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Technical University of Munich, Chair of Robotics, Artificial Intelligence
    and Embedded Systems.
  ko: A Unified Perception-Language-Action Framework for Adaptive Autonomous Driving (PLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Technical University of Munich, Chair of Robotics, Artificial Intelligence
    and Embedded Systems.
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
- pla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.23540v1.
sources:
- id: src_001
  type: paper
  title: A Unified Perception-Language-Action Framework for Adaptive Autonomous Driving (arXiv)
  url: https://arxiv.org/abs/2507.23540
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: PLA source
  url: https://doi.org/10.48550/arXiv.2507.23540
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Autonomous driving systems face significant challenges in achieving human-like adaptability, robustness, and interpretability in complex, open-world environments. These challenges stem from fragmented architectures, limited generalization to novel scenarios, and insufficient semantic extraction from perception. To address these limitations, we propose a unified Perception-Language-Action (PLA) framework that integrates multi-sensor fusion (cameras, LiDAR, radar) with a large language model (LLM)-augmented Vision-Language-Action (VLA) architecture, specifically a GPT-4.1-powered reasoning core. This framework unifies low-level sensory processing with high-level contextual reasoning, tightly coupling perception with natural language-based semantic understanding and decision-making to enable context-aware, explainable, and safety-bounded autonomous driving. Evaluations on an urban intersection scenario with a construction zone demonstrate superior performance in trajectory tracking, speed prediction, and adaptive planning. The results highlight the potential of language-augmented cognitive frameworks for advancing the safety, interpretability, and scalability of autonomous driving systems.

## 核心内容
Autonomous driving systems face significant challenges in achieving human-like adaptability, robustness, and interpretability in complex, open-world environments. These challenges stem from fragmented architectures, limited generalization to novel scenarios, and insufficient semantic extraction from perception. To address these limitations, we propose a unified Perception-Language-Action (PLA) framework that integrates multi-sensor fusion (cameras, LiDAR, radar) with a large language model (LLM)-augmented Vision-Language-Action (VLA) architecture, specifically a GPT-4.1-powered reasoning core. This framework unifies low-level sensory processing with high-level contextual reasoning, tightly coupling perception with natural language-based semantic understanding and decision-making to enable context-aware, explainable, and safety-bounded autonomous driving. Evaluations on an urban intersection scenario with a construction zone demonstrate superior performance in trajectory tracking, speed prediction, and adaptive planning. The results highlight the potential of language-augmented cognitive frameworks for advancing the safety, interpretability, and scalability of autonomous driving systems.

## 参考
- http://arxiv.org/abs/2507.23540v1

## Overview
Autonomous driving systems face significant challenges in achieving human-like adaptability, robustness, and interpretability in complex, open-world environments. These challenges stem from fragmented architectures, limited generalization to novel scenarios, and insufficient semantic extraction from perception. To address these limitations, we propose a unified Perception-Language-Action (PLA) framework that integrates multi-sensor fusion (cameras, LiDAR, radar) with a large language model (LLM)-augmented Vision-Language-Action (VLA) architecture, specifically a GPT-4.1-powered reasoning core. This framework unifies low-level sensory processing with high-level contextual reasoning, tightly coupling perception with natural language-based semantic understanding and decision-making to enable context-aware, explainable, and safety-bounded autonomous driving. Evaluations on an urban intersection scenario with a construction zone demonstrate superior performance in trajectory tracking, speed prediction, and adaptive planning. The results highlight the potential of language-augmented cognitive frameworks for advancing the safety, interpretability, and scalability of autonomous driving systems.

## Content
Autonomous driving systems face significant challenges in achieving human-like adaptability, robustness, and interpretability in complex, open-world environments. These challenges stem from fragmented architectures, limited generalization to novel scenarios, and insufficient semantic extraction from perception. To address these limitations, we propose a unified Perception-Language-Action (PLA) framework that integrates multi-sensor fusion (cameras, LiDAR, radar) with a large language model (LLM)-augmented Vision-Language-Action (VLA) architecture, specifically a GPT-4.1-powered reasoning core. This framework unifies low-level sensory processing with high-level contextual reasoning, tightly coupling perception with natural language-based semantic understanding and decision-making to enable context-aware, explainable, and safety-bounded autonomous driving. Evaluations on an urban intersection scenario with a construction zone demonstrate superior performance in trajectory tracking, speed prediction, and adaptive planning. The results highlight the potential of language-augmented cognitive frameworks for advancing the safety, interpretability, and scalability of autonomous driving systems.

## 개요
자율주행 시스템은 복잡한 개방형 환경에서 인간과 유사한 적응성, 강건성 및 해석 가능성을 달성하는 데 상당한 어려움에 직면해 있습니다. 이러한 어려움은 단편화된 아키텍처, 새로운 시나리오에 대한 일반화의 한계, 그리고 인식에서의 불충분한 의미 추출에서 비롯됩니다. 이러한 한계를 해결하기 위해, 우리는 다중 센서 융합(카메라, LiDAR, 레이더)을 대규모 언어 모델(LLM)로 강화된 Vision-Language-Action (VLA) 아키텍처, 특히 GPT-4.1 기반 추론 코어와 통합하는 통합 Perception-Language-Action (PLA) 프레임워크를 제안합니다. 이 프레임워크는 저수준 감각 처리와 고수준 맥락 추론을 통합하고, 인식을 자연어 기반 의미 이해 및 의사 결정과 긴밀하게 결합하여 맥락 인식, 설명 가능 및 안전이 보장된 자율주행을 가능하게 합니다. 건설 구역이 있는 도시 교차로 시나리오에서의 평가는 궤적 추적, 속도 예측 및 적응형 계획에서 우수한 성능을 입증했습니다. 결과는 언어로 강화된 인지 프레임워크가 자율주행 시스템의 안전성, 해석 가능성 및 확장성을 발전시키는 잠재력을 강조합니다.

## 핵심 내용
자율주행 시스템은 복잡한 개방형 환경에서 인간과 유사한 적응성, 강건성 및 해석 가능성을 달성하는 데 상당한 어려움에 직면해 있습니다. 이러한 어려움은 단편화된 아키텍처, 새로운 시나리오에 대한 일반화의 한계, 그리고 인식에서의 불충분한 의미 추출에서 비롯됩니다. 이러한 한계를 해결하기 위해, 우리는 다중 센서 융합(카메라, LiDAR, 레이더)을 대규모 언어 모델(LLM)로 강화된 Vision-Language-Action (VLA) 아키텍처, 특히 GPT-4.1 기반 추론 코어와 통합하는 통합 Perception-Language-Action (PLA) 프레임워크를 제안합니다. 이 프레임워크는 저수준 감각 처리와 고수준 맥락 추론을 통합하고, 인식을 자연어 기반 의미 이해 및 의사 결정과 긴밀하게 결합하여 맥락 인식, 설명 가능 및 안전이 보장된 자율주행을 가능하게 합니다. 건설 구역이 있는 도시 교차로 시나리오에서의 평가는 궤적 추적, 속도 예측 및 적응형 계획에서 우수한 성능을 입증했습니다. 결과는 언어로 강화된 인지 프레임워크가 자율주행 시스템의 안전성, 해석 가능성 및 확장성을 발전시키는 잠재력을 강조합니다.
