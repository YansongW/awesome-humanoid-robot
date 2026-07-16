---
$id: ent_paper_xu_wam_flow_parallel_coarse_to_fi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving'
  zh: WAM-Flow
  ko: 'WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving'
summary:
  en: 'WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving (WAM-Flow), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Fudan University, Yinwang Intelligent
    Technology Co., Ltd..'
  zh: 'WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving (WAM-Flow), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Fudan University, Yinwang Intelligent
    Technology Co., Ltd..'
  ko: 'WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving (WAM-Flow), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Fudan University, Yinwang Intelligent
    Technology Co., Ltd..'
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
- wam_flow
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.06112v2.
sources:
- id: src_001
  type: paper
  title: 'WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2512.06112
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: WAM-Flow source
  url: https://doi.org/10.48550/arXiv.2512.06112
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We introduce WAM-Flow, a vision-language-action (VLA) model that casts ego-trajectory planning as discrete flow matching over a structured token space. In contrast to autoregressive decoders, WAM-Flow performs fully parallel, bidirectional denoising, enabling coarse-to-fine refinement with a tunable compute-accuracy trade-off. Specifically, the approach combines a metric-aligned numerical tokenizer that preserves scalar geometry via triplet-margin learning, a geometry-aware flow objective and a simulator-guided GRPO alignment that integrates safety, ego progress, and comfort rewards while retaining parallel generation. A multi-stage adaptation converts a pre-trained auto-regressive backbone (Janus-1.5B) from causal decoding to non-causal flow model and strengthens road-scene competence through continued multimodal pretraining. Thanks to the inherent nature of consistency model training and parallel decoding inference, WAM-Flow achieves superior closed-loop performance against autoregressive and diffusion-based VLA baselines, with 1-step inference attaining 89.1 PDMS and 5-step inference reaching 90.3 PDMS on NAVSIM v1 benchmark. These results establish discrete flow matching as a new promising paradigm for end-to-end autonomous driving. The code will be publicly available soon.

## 核心内容
We introduce WAM-Flow, a vision-language-action (VLA) model that casts ego-trajectory planning as discrete flow matching over a structured token space. In contrast to autoregressive decoders, WAM-Flow performs fully parallel, bidirectional denoising, enabling coarse-to-fine refinement with a tunable compute-accuracy trade-off. Specifically, the approach combines a metric-aligned numerical tokenizer that preserves scalar geometry via triplet-margin learning, a geometry-aware flow objective and a simulator-guided GRPO alignment that integrates safety, ego progress, and comfort rewards while retaining parallel generation. A multi-stage adaptation converts a pre-trained auto-regressive backbone (Janus-1.5B) from causal decoding to non-causal flow model and strengthens road-scene competence through continued multimodal pretraining. Thanks to the inherent nature of consistency model training and parallel decoding inference, WAM-Flow achieves superior closed-loop performance against autoregressive and diffusion-based VLA baselines, with 1-step inference attaining 89.1 PDMS and 5-step inference reaching 90.3 PDMS on NAVSIM v1 benchmark. These results establish discrete flow matching as a new promising paradigm for end-to-end autonomous driving. The code will be publicly available soon.

## 参考
- http://arxiv.org/abs/2512.06112v2

## Overview
We introduce WAM-Flow, a vision-language-action (VLA) model that casts ego-trajectory planning as discrete flow matching over a structured token space. In contrast to autoregressive decoders, WAM-Flow performs fully parallel, bidirectional denoising, enabling coarse-to-fine refinement with a tunable compute-accuracy trade-off. Specifically, the approach combines a metric-aligned numerical tokenizer that preserves scalar geometry via triplet-margin learning, a geometry-aware flow objective and a simulator-guided GRPO alignment that integrates safety, ego progress, and comfort rewards while retaining parallel generation. A multi-stage adaptation converts a pre-trained auto-regressive backbone (Janus-1.5B) from causal decoding to non-causal flow model and strengthens road-scene competence through continued multimodal pretraining. Thanks to the inherent nature of consistency model training and parallel decoding inference, WAM-Flow achieves superior closed-loop performance against autoregressive and diffusion-based VLA baselines, with 1-step inference attaining 89.1 PDMS and 5-step inference reaching 90.3 PDMS on NAVSIM v1 benchmark. These results establish discrete flow matching as a new promising paradigm for end-to-end autonomous driving. The code will be publicly available soon.

## Content
We introduce WAM-Flow, a vision-language-action (VLA) model that casts ego-trajectory planning as discrete flow matching over a structured token space. In contrast to autoregressive decoders, WAM-Flow performs fully parallel, bidirectional denoising, enabling coarse-to-fine refinement with a tunable compute-accuracy trade-off. Specifically, the approach combines a metric-aligned numerical tokenizer that preserves scalar geometry via triplet-margin learning, a geometry-aware flow objective and a simulator-guided GRPO alignment that integrates safety, ego progress, and comfort rewards while retaining parallel generation. A multi-stage adaptation converts a pre-trained auto-regressive backbone (Janus-1.5B) from causal decoding to non-causal flow model and strengthens road-scene competence through continued multimodal pretraining. Thanks to the inherent nature of consistency model training and parallel decoding inference, WAM-Flow achieves superior closed-loop performance against autoregressive and diffusion-based VLA baselines, with 1-step inference attaining 89.1 PDMS and 5-step inference reaching 90.3 PDMS on NAVSIM v1 benchmark. These results establish discrete flow matching as a new promising paradigm for end-to-end autonomous driving. The code will be publicly available soon.

## 개요
우리는 WAM-Flow를 소개합니다. 이는 구조화된 토큰 공간에서 자아 궤적 계획을 이산 흐름 매칭(discrete flow matching)으로 변환하는 비전-언어-행동(VLA) 모델입니다. 자기회귀 디코더와 달리 WAM-Flow는 완전히 병렬적이고 양방향적인 잡음 제거를 수행하여, 조정 가능한 계산-정확도 트레이드오프를 통해 대략적에서 세밀한 정제를 가능하게 합니다. 구체적으로, 이 접근법은 삼중 마진 학습(triplet-margin learning)을 통해 스칼라 기하학을 보존하는 메트릭 정렬 수치 토크나이저, 기하학 인식 흐름 목표, 그리고 시뮬레이터 유도 GRPO 정렬을 결합하여 안전, 자아 진행 및 편안함 보상을 통합하면서 병렬 생성을 유지합니다. 다단계 적응은 사전 훈련된 자기회귀 백본(Janus-1.5B)을 인과 디코딩에서 비인과 흐름 모델로 변환하고, 지속적인 다중 모드 사전 훈련을 통해 도로 장면 능력을 강화합니다. 일관성 모델 훈련과 병렬 디코딩 추론의 본질적 특성 덕분에 WAM-Flow는 자기회귀 및 확산 기반 VLA 기준선보다 우수한 폐루프 성능을 달성하며, NAVSIM v1 벤치마크에서 1단계 추론 시 89.1 PDMS, 5단계 추론 시 90.3 PDMS를 기록합니다. 이러한 결과는 이산 흐름 매칭을 종단간 자율 주행을 위한 새로운 유망 패러다임으로 확립합니다. 코드는 곧 공개될 예정입니다.

## 핵심 내용
우리는 WAM-Flow를 소개합니다. 이는 구조화된 토큰 공간에서 자아 궤적 계획을 이산 흐름 매칭(discrete flow matching)으로 변환하는 비전-언어-행동(VLA) 모델입니다. 자기회귀 디코더와 달리 WAM-Flow는 완전히 병렬적이고 양방향적인 잡음 제거를 수행하여, 조정 가능한 계산-정확도 트레이드오프를 통해 대략적에서 세밀한 정제를 가능하게 합니다. 구체적으로, 이 접근법은 삼중 마진 학습(triplet-margin learning)을 통해 스칼라 기하학을 보존하는 메트릭 정렬 수치 토크나이저, 기하학 인식 흐름 목표, 그리고 시뮬레이터 유도 GRPO 정렬을 결합하여 안전, 자아 진행 및 편안함 보상을 통합하면서 병렬 생성을 유지합니다. 다단계 적응은 사전 훈련된 자기회귀 백본(Janus-1.5B)을 인과 디코딩에서 비인과 흐름 모델로 변환하고, 지속적인 다중 모드 사전 훈련을 통해 도로 장면 능력을 강화합니다. 일관성 모델 훈련과 병렬 디코딩 추론의 본질적 특성 덕분에 WAM-Flow는 자기회귀 및 확산 기반 VLA 기준선보다 우수한 폐루프 성능을 달성하며, NAVSIM v1 벤치마크에서 1단계 추론 시 89.1 PDMS, 5단계 추론 시 90.3 PDMS를 기록합니다. 이러한 결과는 이산 흐름 매칭을 종단간 자율 주행을 위한 새로운 유망 패러다임으로 확립합니다. 코드는 곧 공개될 예정입니다.
