---
$id: ent_paper_han_muvla_learning_to_explore_obje_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MUVLA: Learning to Explore Object Navigation via Map Understanding'
  zh: MUVLA
  ko: 'MUVLA: Learning to Explore Object Navigation via Map Understanding'
summary:
  en: 'MUVLA: Learning to Explore Object Navigation via Map Understanding (MUVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tianjin University, Dexmal, Beijing Institute of Technology.'
  zh: 'MUVLA: Learning to Explore Object Navigation via Map Understanding (MUVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tianjin University, Dexmal, Beijing Institute of Technology.'
  ko: 'MUVLA: Learning to Explore Object Navigation via Map Understanding (MUVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tianjin University, Dexmal, Beijing Institute of Technology.'
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
- muvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.25966v1.
sources:
- id: src_001
  type: paper
  title: 'MUVLA: Learning to Explore Object Navigation via Map Understanding (arXiv)'
  url: https://arxiv.org/abs/2509.25966
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MUVLA source
  url: https://doi.org/10.48550/arXiv.2509.25966
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In this paper, we present MUVLA, a Map Understanding Vision-Language-Action model tailored for object navigation. It leverages semantic map abstractions to unify and structure historical information, encoding spatial context in a compact and consistent form. MUVLA takes the current and history observations, as well as the semantic map, as inputs and predicts the action sequence based on the description of goal object. Furthermore, it amplifies supervision through reward-guided return modeling based on dense short-horizon progress signals, enabling the model to develop a detailed understanding of action value for reward maximization. MUVLA employs a three-stage training pipeline: learning map-level spatial understanding, imitating behaviors from mixed-quality demonstrations, and reward amplification. This strategy allows MUVLA to unify diverse demonstrations into a robust spatial representation and generate more rational exploration strategies. Experiments on HM3D and Gibson benchmarks demonstrate that MUVLA achieves great generalization and learns effective exploration behaviors even from low-quality or partially successful trajectories.

## 核心内容
In this paper, we present MUVLA, a Map Understanding Vision-Language-Action model tailored for object navigation. It leverages semantic map abstractions to unify and structure historical information, encoding spatial context in a compact and consistent form. MUVLA takes the current and history observations, as well as the semantic map, as inputs and predicts the action sequence based on the description of goal object. Furthermore, it amplifies supervision through reward-guided return modeling based on dense short-horizon progress signals, enabling the model to develop a detailed understanding of action value for reward maximization. MUVLA employs a three-stage training pipeline: learning map-level spatial understanding, imitating behaviors from mixed-quality demonstrations, and reward amplification. This strategy allows MUVLA to unify diverse demonstrations into a robust spatial representation and generate more rational exploration strategies. Experiments on HM3D and Gibson benchmarks demonstrate that MUVLA achieves great generalization and learns effective exploration behaviors even from low-quality or partially successful trajectories.

## 参考
- http://arxiv.org/abs/2509.25966v1

## Overview
In this paper, we present MUVLA, a Map Understanding Vision-Language-Action model tailored for object navigation. It leverages semantic map abstractions to unify and structure historical information, encoding spatial context in a compact and consistent form. MUVLA takes the current and history observations, as well as the semantic map, as inputs and predicts the action sequence based on the description of goal object. Furthermore, it amplifies supervision through reward-guided return modeling based on dense short-horizon progress signals, enabling the model to develop a detailed understanding of action value for reward maximization. MUVLA employs a three-stage training pipeline: learning map-level spatial understanding, imitating behaviors from mixed-quality demonstrations, and reward amplification. This strategy allows MUVLA to unify diverse demonstrations into a robust spatial representation and generate more rational exploration strategies. Experiments on HM3D and Gibson benchmarks demonstrate that MUVLA achieves great generalization and learns effective exploration behaviors even from low-quality or partially successful trajectories.

## Content
In this paper, we present MUVLA, a Map Understanding Vision-Language-Action model tailored for object navigation. It leverages semantic map abstractions to unify and structure historical information, encoding spatial context in a compact and consistent form. MUVLA takes the current and history observations, as well as the semantic map, as inputs and predicts the action sequence based on the description of goal object. Furthermore, it amplifies supervision through reward-guided return modeling based on dense short-horizon progress signals, enabling the model to develop a detailed understanding of action value for reward maximization. MUVLA employs a three-stage training pipeline: learning map-level spatial understanding, imitating behaviors from mixed-quality demonstrations, and reward amplification. This strategy allows MUVLA to unify diverse demonstrations into a robust spatial representation and generate more rational exploration strategies. Experiments on HM3D and Gibson benchmarks demonstrate that MUVLA achieves great generalization and learns effective exploration behaviors even from low-quality or partially successful trajectories.

## 개요
본 논문에서는 객체 탐색을 위한 지도 이해 비전-언어-행동 모델인 MUVLA를 제안합니다. MUVLA는 의미론적 지도 추상화를 활용하여 과거 정보를 통합하고 구조화하며, 공간적 맥락을 간결하고 일관된 형태로 인코딩합니다. MUVLA는 현재 및 과거 관측 데이터와 의미론적 지도를 입력으로 받아 목표 객체의 설명을 기반으로 행동 시퀀스를 예측합니다. 또한, 밀집된 단기 진행 신호를 기반으로 보상 유도 반환 모델링을 통해 감독을 강화하여, 모델이 보상 최대화를 위한 행동 가치에 대한 세부적인 이해를 발전시킬 수 있도록 합니다. MUVLA는 지도 수준의 공간 이해 학습, 혼합 품질의 시연에서 행동 모방, 보상 증폭의 세 단계 학습 파이프라인을 사용합니다. 이 전략을 통해 MUVLA는 다양한 시연을 강력한 공간 표현으로 통합하고 더 합리적인 탐색 전략을 생성할 수 있습니다. HM3D 및 Gibson 벤치마크 실험은 MUVLA가 뛰어난 일반화 성능을 달성하고, 낮은 품질이나 부분적으로 성공한 궤적에서도 효과적인 탐색 행동을 학습함을 보여줍니다.

## 핵심 내용
본 논문에서는 객체 탐색을 위한 지도 이해 비전-언어-행동 모델인 MUVLA를 제안합니다. MUVLA는 의미론적 지도 추상화를 활용하여 과거 정보를 통합하고 구조화하며, 공간적 맥락을 간결하고 일관된 형태로 인코딩합니다. MUVLA는 현재 및 과거 관측 데이터와 의미론적 지도를 입력으로 받아 목표 객체의 설명을 기반으로 행동 시퀀스를 예측합니다. 또한, 밀집된 단기 진행 신호를 기반으로 보상 유도 반환 모델링을 통해 감독을 강화하여, 모델이 보상 최대화를 위한 행동 가치에 대한 세부적인 이해를 발전시킬 수 있도록 합니다. MUVLA는 지도 수준의 공간 이해 학습, 혼합 품질의 시연에서 행동 모방, 보상 증폭의 세 단계 학습 파이프라인을 사용합니다. 이 전략을 통해 MUVLA는 다양한 시연을 강력한 공간 표현으로 통합하고 더 합리적인 탐색 전략을 생성할 수 있습니다. HM3D 및 Gibson 벤치마크 실험은 MUVLA가 뛰어난 일반화 성능을 달성하고, 낮은 품질이나 부분적으로 성공한 궤적에서도 효과적인 탐색 행동을 학습함을 보여줍니다.
