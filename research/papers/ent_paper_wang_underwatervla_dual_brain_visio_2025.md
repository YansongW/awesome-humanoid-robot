---
$id: ent_paper_wang_underwatervla_dual_brain_visio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'UnderwaterVLA: Dual-brain Vision-Language-Action architecture for Autonomous Underwater Navigation'
  zh: UnderwaterVLA
  ko: 'UnderwaterVLA: Dual-brain Vision-Language-Action architecture for Autonomous Underwater Navigation'
summary:
  en: 'UnderwaterVLA: Dual-brain Vision-Language-Action architecture for Autonomous Underwater Navigation (UnderwaterVLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Westlake University, Zhejiang University,
    Australian National University.'
  zh: 'UnderwaterVLA: Dual-brain Vision-Language-Action architecture for Autonomous Underwater Navigation (UnderwaterVLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Westlake University, Zhejiang University,
    Australian National University.'
  ko: 'UnderwaterVLA: Dual-brain Vision-Language-Action architecture for Autonomous Underwater Navigation (UnderwaterVLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Westlake University, Zhejiang University,
    Australian National University.'
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
- underwatervla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.22441v1.
sources:
- id: src_001
  type: paper
  title: 'UnderwaterVLA: Dual-brain Vision-Language-Action architecture for Autonomous Underwater Navigation (arXiv)'
  url: https://arxiv.org/abs/2509.22441
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: UnderwaterVLA source
  url: https://doi.org/10.48550/arXiv.2509.22441
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
This paper presents UnderwaterVLA, a novel framework for autonomous underwater navigation that integrates multimodal foundation models with embodied intelligence systems. Underwater operations remain difficult due to hydrodynamic disturbances, limited communication bandwidth, and degraded sensing in turbid waters. To address these challenges, we introduce three innovations. First, a dual-brain architecture decouples high-level mission reasoning from low-level reactive control, enabling robust operation under communication and computational constraints. Second, we apply Vision-Language-Action(VLA) models to underwater robotics for the first time, incorporating structured chain-of-thought reasoning for interpretable decision-making. Third, a hydrodynamics-informed Model Predictive Control(MPC) scheme compensates for fluid effects in real time without costly task-specific training. Experimental results in field tests show that UnderwaterVLA reduces navigation errors in degraded visual conditions while maintaining higher task completion by 19% to 27% over baseline. By minimizing reliance on underwater-specific training data and improving adaptability across environments, UnderwaterVLA provides a scalable and cost-effective path toward the next generation of intelligent AUVs.

## 核心内容
This paper presents UnderwaterVLA, a novel framework for autonomous underwater navigation that integrates multimodal foundation models with embodied intelligence systems. Underwater operations remain difficult due to hydrodynamic disturbances, limited communication bandwidth, and degraded sensing in turbid waters. To address these challenges, we introduce three innovations. First, a dual-brain architecture decouples high-level mission reasoning from low-level reactive control, enabling robust operation under communication and computational constraints. Second, we apply Vision-Language-Action(VLA) models to underwater robotics for the first time, incorporating structured chain-of-thought reasoning for interpretable decision-making. Third, a hydrodynamics-informed Model Predictive Control(MPC) scheme compensates for fluid effects in real time without costly task-specific training. Experimental results in field tests show that UnderwaterVLA reduces navigation errors in degraded visual conditions while maintaining higher task completion by 19% to 27% over baseline. By minimizing reliance on underwater-specific training data and improving adaptability across environments, UnderwaterVLA provides a scalable and cost-effective path toward the next generation of intelligent AUVs.

## 参考
- http://arxiv.org/abs/2509.22441v1

## Overview
This paper presents UnderwaterVLA, a novel framework for autonomous underwater navigation that integrates multimodal foundation models with embodied intelligence systems. Underwater operations remain difficult due to hydrodynamic disturbances, limited communication bandwidth, and degraded sensing in turbid waters. To address these challenges, we introduce three innovations. First, a dual-brain architecture decouples high-level mission reasoning from low-level reactive control, enabling robust operation under communication and computational constraints. Second, we apply Vision-Language-Action (VLA) models to underwater robotics for the first time, incorporating structured chain-of-thought reasoning for interpretable decision-making. Third, a hydrodynamics-informed Model Predictive Control (MPC) scheme compensates for fluid effects in real time without costly task-specific training. Experimental results in field tests show that UnderwaterVLA reduces navigation errors in degraded visual conditions while maintaining higher task completion by 19% to 27% over baseline. By minimizing reliance on underwater-specific training data and improving adaptability across environments, UnderwaterVLA provides a scalable and cost-effective path toward the next generation of intelligent AUVs.

## Content
This paper presents UnderwaterVLA, a novel framework for autonomous underwater navigation that integrates multimodal foundation models with embodied intelligence systems. Underwater operations remain difficult due to hydrodynamic disturbances, limited communication bandwidth, and degraded sensing in turbid waters. To address these challenges, we introduce three innovations. First, a dual-brain architecture decouples high-level mission reasoning from low-level reactive control, enabling robust operation under communication and computational constraints. Second, we apply Vision-Language-Action (VLA) models to underwater robotics for the first time, incorporating structured chain-of-thought reasoning for interpretable decision-making. Third, a hydrodynamics-informed Model Predictive Control (MPC) scheme compensates for fluid effects in real time without costly task-specific training. Experimental results in field tests show that UnderwaterVLA reduces navigation errors in degraded visual conditions while maintaining higher task completion by 19% to 27% over baseline. By minimizing reliance on underwater-specific training data and improving adaptability across environments, UnderwaterVLA provides a scalable and cost-effective path toward the next generation of intelligent AUVs.

## 개요
본 논문은 다중 모달 기반 모델과 체화된 지능 시스템을 통합한 자율 수중 항법을 위한 새로운 프레임워크인 UnderwaterVLA를 제시합니다. 수중 작업은 유체역학적 교란, 제한된 통신 대역폭, 탁한 수중에서의 센서 성능 저하로 인해 여전히 어려움을 겪고 있습니다. 이러한 문제를 해결하기 위해 세 가지 혁신을 도입합니다. 첫째, 이중 뇌 아키텍처는 고수준 임무 추론과 저수준 반응 제어를 분리하여 통신 및 계산 제약 조건에서도 강건한 작동을 가능하게 합니다. 둘째, Vision-Language-Action(VLA) 모델을 수중 로봇 공학에 최초로 적용하여 구조화된 사고 사슬 추론을 통합함으로써 해석 가능한 의사 결정을 구현합니다. 셋째, 유체역학 기반 모델 예측 제어(MPC) 기법은 비용이 많이 드는 작업별 학습 없이 실시간으로 유체 효과를 보상합니다. 현장 실험 결과, UnderwaterVLA는 시각 조건이 저하된 환경에서 항법 오류를 줄이면서 기준 대비 작업 완료율을 19%에서 27%까지 높게 유지합니다. 수중 특화 학습 데이터에 대한 의존도를 최소화하고 환경 간 적응성을 향상시킴으로써, UnderwaterVLA는 차세대 지능형 AUV를 위한 확장 가능하고 비용 효율적인 경로를 제공합니다.

## 핵심 내용
본 논문은 다중 모달 기반 모델과 체화된 지능 시스템을 통합한 자율 수중 항법을 위한 새로운 프레임워크인 UnderwaterVLA를 제시합니다. 수중 작업은 유체역학적 교란, 제한된 통신 대역폭, 탁한 수중에서의 센서 성능 저하로 인해 여전히 어려움을 겪고 있습니다. 이러한 문제를 해결하기 위해 세 가지 혁신을 도입합니다. 첫째, 이중 뇌 아키텍처는 고수준 임무 추론과 저수준 반응 제어를 분리하여 통신 및 계산 제약 조건에서도 강건한 작동을 가능하게 합니다. 둘째, Vision-Language-Action(VLA) 모델을 수중 로봇 공학에 최초로 적용하여 구조화된 사고 사슬 추론을 통합함으로써 해석 가능한 의사 결정을 구현합니다. 셋째, 유체역학 기반 모델 예측 제어(MPC) 기법은 비용이 많이 드는 작업별 학습 없이 실시간으로 유체 효과를 보상합니다. 현장 실험 결과, UnderwaterVLA는 시각 조건이 저하된 환경에서 항법 오류를 줄이면서 기준 대비 작업 완료율을 19%에서 27%까지 높게 유지합니다. 수중 특화 학습 데이터에 대한 의존도를 최소화하고 환경 간 적응성을 향상시킴으로써, UnderwaterVLA는 차세대 지능형 AUV를 위한 확장 가능하고 비용 효율적인 경로를 제공합니다.
