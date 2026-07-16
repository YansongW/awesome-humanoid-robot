---
$id: ent_paper_seong_vla_r_vision_language_action_r_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA-R: Vision-Language Action Retrieval toward Open-World End-to-End Autonomous Driving'
  zh: VLA-R
  ko: 'VLA-R: Vision-Language Action Retrieval toward Open-World End-to-End Autonomous Driving'
summary:
  en: 'VLA-R: Vision-Language Action Retrieval toward Open-World End-to-End Autonomous Driving (VLA-R), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by KAIST.'
  zh: 'VLA-R: Vision-Language Action Retrieval toward Open-World End-to-End Autonomous Driving (VLA-R), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by KAIST.'
  ko: 'VLA-R: Vision-Language Action Retrieval toward Open-World End-to-End Autonomous Driving (VLA-R), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by KAIST.'
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
- vision_language_action
- vla
- vla_r
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.12405v1.
sources:
- id: src_001
  type: paper
  title: 'VLA-R: Vision-Language Action Retrieval toward Open-World End-to-End Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2511.12405
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-R source
  url: https://doi.org/10.48550/arXiv.2511.12405
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Exploring open-world situations in an end-to-end manner is a promising yet challenging task due to the need for strong generalization capabilities. In particular, end-to-end autonomous driving in unstructured outdoor environments often encounters conditions that were unfamiliar during training. In this work, we present Vision-Language Action Retrieval (VLA-R), an open-world end-to-end autonomous driving (OW-E2EAD) framework that integrates open-world perception with a novel vision-action retrieval paradigm. We leverage a frozen vision-language model for open-world detection and segmentation to obtain multi-scale, prompt-guided, and interpretable perception features without domain-specific tuning. A Q-Former bottleneck aggregates fine-grained visual representations with language-aligned visual features, bridging perception and action domains. To learn transferable driving behaviors, we introduce a vision-action contrastive learning scheme that aligns vision-language and action embeddings for effective open-world reasoning and action retrieval. Our experiments on a real-world robotic platform demonstrate strong generalization and exploratory performance in unstructured, unseen environments, even with limited data. Demo videos are provided in the supplementary material.

## 核心内容
Exploring open-world situations in an end-to-end manner is a promising yet challenging task due to the need for strong generalization capabilities. In particular, end-to-end autonomous driving in unstructured outdoor environments often encounters conditions that were unfamiliar during training. In this work, we present Vision-Language Action Retrieval (VLA-R), an open-world end-to-end autonomous driving (OW-E2EAD) framework that integrates open-world perception with a novel vision-action retrieval paradigm. We leverage a frozen vision-language model for open-world detection and segmentation to obtain multi-scale, prompt-guided, and interpretable perception features without domain-specific tuning. A Q-Former bottleneck aggregates fine-grained visual representations with language-aligned visual features, bridging perception and action domains. To learn transferable driving behaviors, we introduce a vision-action contrastive learning scheme that aligns vision-language and action embeddings for effective open-world reasoning and action retrieval. Our experiments on a real-world robotic platform demonstrate strong generalization and exploratory performance in unstructured, unseen environments, even with limited data. Demo videos are provided in the supplementary material.

## 参考
- http://arxiv.org/abs/2511.12405v1

## Overview
Exploring open-world situations in an end-to-end manner is a promising yet challenging task due to the need for strong generalization capabilities. In particular, end-to-end autonomous driving in unstructured outdoor environments often encounters conditions that were unfamiliar during training. In this work, we present Vision-Language Action Retrieval (VLA-R), an open-world end-to-end autonomous driving (OW-E2EAD) framework that integrates open-world perception with a novel vision-action retrieval paradigm. We leverage a frozen vision-language model for open-world detection and segmentation to obtain multi-scale, prompt-guided, and interpretable perception features without domain-specific tuning. A Q-Former bottleneck aggregates fine-grained visual representations with language-aligned visual features, bridging perception and action domains. To learn transferable driving behaviors, we introduce a vision-action contrastive learning scheme that aligns vision-language and action embeddings for effective open-world reasoning and action retrieval. Our experiments on a real-world robotic platform demonstrate strong generalization and exploratory performance in unstructured, unseen environments, even with limited data. Demo videos are provided in the supplementary material.

## Content
Exploring open-world situations in an end-to-end manner is a promising yet challenging task due to the need for strong generalization capabilities. In particular, end-to-end autonomous driving in unstructured outdoor environments often encounters conditions that were unfamiliar during training. In this work, we present Vision-Language Action Retrieval (VLA-R), an open-world end-to-end autonomous driving (OW-E2EAD) framework that integrates open-world perception with a novel vision-action retrieval paradigm. We leverage a frozen vision-language model for open-world detection and segmentation to obtain multi-scale, prompt-guided, and interpretable perception features without domain-specific tuning. A Q-Former bottleneck aggregates fine-grained visual representations with language-aligned visual features, bridging perception and action domains. To learn transferable driving behaviors, we introduce a vision-action contrastive learning scheme that aligns vision-language and action embeddings for effective open-world reasoning and action retrieval. Our experiments on a real-world robotic platform demonstrate strong generalization and exploratory performance in unstructured, unseen environments, even with limited data. Demo videos are provided in the supplementary material.

## 개요
종단 간 방식으로 개방형 세계 상황을 탐구하는 것은 강력한 일반화 능력이 필요하기 때문에 유망하면서도 도전적인 과제입니다. 특히, 구조화되지 않은 야외 환경에서의 종단 간 자율 주행은 훈련 중에 익숙하지 않은 조건을 자주 마주하게 됩니다. 본 연구에서는 개방형 세계 인식과 새로운 시각-행동 검색 패러다임을 통합한 개방형 세계 종단 간 자율 주행(OW-E2EAD) 프레임워크인 Vision-Language Action Retrieval (VLA-R)을 제시합니다. 우리는 도메인별 튜닝 없이 다중 스케일, 프롬프트 기반, 해석 가능한 인식 특징을 얻기 위해 고정된 시각-언어 모델을 개방형 세계 탐지 및 분할에 활용합니다. Q-Former 병목은 언어 정렬 시각 특징과 미세한 시각 표현을 집계하여 인식과 행동 도메인을 연결합니다. 전이 가능한 주행 행동을 학습하기 위해, 시각-언어 및 행동 임베딩을 정렬하여 효과적인 개방형 세계 추론 및 행동 검색을 가능하게 하는 시각-행동 대조 학습 기법을 도입합니다. 실제 로봇 플랫폼에서의 실험은 제한된 데이터로도 구조화되지 않고 보지 못한 환경에서 강력한 일반화 및 탐색 성능을 입증합니다. 데모 비디오는 부록 자료에 제공됩니다.

## 핵심 내용
종단 간 방식으로 개방형 세계 상황을 탐구하는 것은 강력한 일반화 능력이 필요하기 때문에 유망하면서도 도전적인 과제입니다. 특히, 구조화되지 않은 야외 환경에서의 종단 간 자율 주행은 훈련 중에 익숙하지 않은 조건을 자주 마주하게 됩니다. 본 연구에서는 개방형 세계 인식과 새로운 시각-행동 검색 패러다임을 통합한 개방형 세계 종단 간 자율 주행(OW-E2EAD) 프레임워크인 Vision-Language Action Retrieval (VLA-R)을 제시합니다. 우리는 도메인별 튜닝 없이 다중 스케일, 프롬프트 기반, 해석 가능한 인식 특징을 얻기 위해 고정된 시각-언어 모델을 개방형 세계 탐지 및 분할에 활용합니다. Q-Former 병목은 언어 정렬 시각 특징과 미세한 시각 표현을 집계하여 인식과 행동 도메인을 연결합니다. 전이 가능한 주행 행동을 학습하기 위해, 시각-언어 및 행동 임베딩을 정렬하여 효과적인 개방형 세계 추론 및 행동 검색을 가능하게 하는 시각-행동 대조 학습 기법을 도입합니다. 실제 로봇 플랫폼에서의 실험은 제한된 데이터로도 구조화되지 않고 보지 못한 환경에서 강력한 일반화 및 탐색 성능을 입증합니다. 데모 비디오는 부록 자료에 제공됩니다.
