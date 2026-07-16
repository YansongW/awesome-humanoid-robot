---
$id: ent_paper_huang_otter_a_vision_language_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction'
  zh: OTTER
  ko: 'OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction'
summary:
  en: 'OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction (OTTER), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of California, Berkeley, Meta AI, and published at ICML25.'
  zh: 'OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction (OTTER), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of California, Berkeley, Meta AI, and published at ICML25.'
  ko: 'OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction (OTTER), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of California, Berkeley, Meta AI, and published at ICML25.'
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
- otter
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.03734v4.
sources:
- id: src_001
  type: paper
  title: OTTER source
  url: https://openreview.net/forum?id=UHF0km7R5M
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models aim to predict robotic actions based on visual observations and language instructions. Existing approaches require fine-tuning pre-trained visionlanguage models (VLMs) as visual and language features are independently fed into downstream policies, degrading the pre-trained semantic alignments. We propose OTTER, a novel VLA architecture that leverages these existing alignments through explicit, text-aware visual feature extraction. Instead of processing all visual features, OTTER selectively extracts and passes only task-relevant visual features that are semantically aligned with the language instruction to the policy transformer. This allows OTTER to keep the pre-trained vision-language encoders frozen. Thereby, OTTER preserves and utilizes the rich semantic understanding learned from large-scale pre-training, enabling strong zero-shot generalization capabilities. In simulation and real-world experiments, OTTER significantly outperforms existing VLA models, demonstrating strong zeroshot generalization to novel objects and environments. Video, code, checkpoints, and dataset: https://ottervla.github.io/.

## 核心内容
Vision-Language-Action (VLA) models aim to predict robotic actions based on visual observations and language instructions. Existing approaches require fine-tuning pre-trained visionlanguage models (VLMs) as visual and language features are independently fed into downstream policies, degrading the pre-trained semantic alignments. We propose OTTER, a novel VLA architecture that leverages these existing alignments through explicit, text-aware visual feature extraction. Instead of processing all visual features, OTTER selectively extracts and passes only task-relevant visual features that are semantically aligned with the language instruction to the policy transformer. This allows OTTER to keep the pre-trained vision-language encoders frozen. Thereby, OTTER preserves and utilizes the rich semantic understanding learned from large-scale pre-training, enabling strong zero-shot generalization capabilities. In simulation and real-world experiments, OTTER significantly outperforms existing VLA models, demonstrating strong zeroshot generalization to novel objects and environments. Video, code, checkpoints, and dataset: https://ottervla.github.io/.

## 参考
- http://arxiv.org/abs/2503.03734v4

## Overview
Vision-Language-Action (VLA) models aim to predict robotic actions based on visual observations and language instructions. Existing approaches require fine-tuning pre-trained vision-language models (VLMs) as visual and language features are independently fed into downstream policies, degrading the pre-trained semantic alignments. We propose OTTER, a novel VLA architecture that leverages these existing alignments through explicit, text-aware visual feature extraction. Instead of processing all visual features, OTTER selectively extracts and passes only task-relevant visual features that are semantically aligned with the language instruction to the policy transformer. This allows OTTER to keep the pre-trained vision-language encoders frozen. Thereby, OTTER preserves and utilizes the rich semantic understanding learned from large-scale pre-training, enabling strong zero-shot generalization capabilities. In simulation and real-world experiments, OTTER significantly outperforms existing VLA models, demonstrating strong zero-shot generalization to novel objects and environments. Video, code, checkpoints, and dataset: https://ottervla.github.io/.

## Content
Vision-Language-Action (VLA) models aim to predict robotic actions based on visual observations and language instructions. Existing approaches require fine-tuning pre-trained vision-language models (VLMs) as visual and language features are independently fed into downstream policies, degrading the pre-trained semantic alignments. We propose OTTER, a novel VLA architecture that leverages these existing alignments through explicit, text-aware visual feature extraction. Instead of processing all visual features, OTTER selectively extracts and passes only task-relevant visual features that are semantically aligned with the language instruction to the policy transformer. This allows OTTER to keep the pre-trained vision-language encoders frozen. Thereby, OTTER preserves and utilizes the rich semantic understanding learned from large-scale pre-training, enabling strong zero-shot generalization capabilities. In simulation and real-world experiments, OTTER significantly outperforms existing VLA models, demonstrating strong zero-shot generalization to novel objects and environments. Video, code, checkpoints, and dataset: https://ottervla.github.io/.

## 개요
Vision-Language-Action (VLA) 모델은 시각적 관찰과 언어 명령을 기반으로 로봇 동작을 예측하는 것을 목표로 합니다. 기존 접근 방식은 시각 및 언어 특징이 독립적으로 하위 정책에 입력되어 사전 학습된 의미적 정렬이 저하되므로, 사전 학습된 시각-언어 모델(VLM)의 미세 조정이 필요합니다. 우리는 명시적이고 텍스트 인식 시각 특징 추출을 통해 이러한 기존 정렬을 활용하는 새로운 VLA 아키텍처인 OTTER를 제안합니다. OTTER는 모든 시각 특징을 처리하는 대신, 언어 명령과 의미적으로 정렬된 작업 관련 시각 특징만 선택적으로 추출하여 정책 트랜스포머에 전달합니다. 이를 통해 OTTER는 사전 학습된 시각-언어 인코더를 고정 상태로 유지할 수 있습니다. 따라서 OTTER는 대규모 사전 학습에서 얻은 풍부한 의미 이해를 보존하고 활용하여 강력한 제로샷 일반화 능력을 가능하게 합니다. 시뮬레이션 및 실제 실험에서 OTTER는 기존 VLA 모델을 크게 능가하며, 새로운 객체와 환경에 대한 강력한 제로샷 일반화를 입증합니다. 비디오, 코드, 체크포인트 및 데이터셋: https://ottervla.github.io/.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 시각적 관찰과 언어 명령을 기반으로 로봇 동작을 예측하는 것을 목표로 합니다. 기존 접근 방식은 시각 및 언어 특징이 독립적으로 하위 정책에 입력되어 사전 학습된 의미적 정렬이 저하되므로, 사전 학습된 시각-언어 모델(VLM)의 미세 조정이 필요합니다. 우리는 명시적이고 텍스트 인식 시각 특징 추출을 통해 이러한 기존 정렬을 활용하는 새로운 VLA 아키텍처인 OTTER를 제안합니다. OTTER는 모든 시각 특징을 처리하는 대신, 언어 명령과 의미적으로 정렬된 작업 관련 시각 특징만 선택적으로 추출하여 정책 트랜스포머에 전달합니다. 이를 통해 OTTER는 사전 학습된 시각-언어 인코더를 고정 상태로 유지할 수 있습니다. 따라서 OTTER는 대규모 사전 학습에서 얻은 풍부한 의미 이해를 보존하고 활용하여 강력한 제로샷 일반화 능력을 가능하게 합니다. 시뮬레이션 및 실제 실험에서 OTTER는 기존 VLA 모델을 크게 능가하며, 새로운 객체와 환경에 대한 강력한 제로샷 일반화를 입증합니다. 비디오, 코드, 체크포인트 및 데이터셋: https://ottervla.github.io/.
