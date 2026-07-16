---
$id: ent_paper_wang_sigma_the_key_for_vision_langu_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Sigma: The Key for Vision-Language-Action Models toward Telepathic Alignment'
  zh: Sigma
  ko: 'Sigma: The Key for Vision-Language-Action Models toward Telepathic Alignment'
summary:
  en: 'Sigma: The Key for Vision-Language-Action Models toward Telepathic Alignment (Sigma), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UCSI University.'
  zh: 'Sigma: The Key for Vision-Language-Action Models toward Telepathic Alignment (Sigma), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UCSI University.'
  ko: 'Sigma: The Key for Vision-Language-Action Models toward Telepathic Alignment (Sigma), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UCSI University.'
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
- sigma
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.00783v3.
sources:
- id: src_001
  type: paper
  title: 'Sigma: The Key for Vision-Language-Action Models toward Telepathic Alignment (arXiv)'
  url: https://arxiv.org/abs/2512.00783
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Sigma source
  url: https://doi.org/10.48550/arXiv.2512.00783
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
To address a fundamental limitation in cognitive systems, namely the absence of a time-updatable mediating thought space between semantics and continuous control, this work constructs and trains a vision-language-action model termed Sigma, deployed on a single RTX 4090. The model is built upon the open-source pi0.5_base backbone, with the svla_so101_pickplace dataset preprocessed into a structured training corpus. An independently designed VLA architecture is introduced to integrate deep semantic understanding with associative reasoning, enabling telepathic-style alignment between perception and action. Training proceeds through iterative optimization of data preprocessing, LoRA-based fine-tuning, and inference-stage adapter design. Evaluation is conducted using offline closed-loop replay, comparing Sigma against the untuned pi0.5_base under identical data conditions. Experimental results indicate a consistent reduction in control MSE across vector-, fragment-, and trajectory-level scales, while preserving the stability of the telepathy norm and semantic-text alignment quality. These findings demonstrate that mind-responsive alignment control can be quantitatively achieved through semantic and associative architectural integration without retraining the base model, providing a reproducible pathway for semantic alignment and intention-driven behavior.

## 核心内容
To address a fundamental limitation in cognitive systems, namely the absence of a time-updatable mediating thought space between semantics and continuous control, this work constructs and trains a vision-language-action model termed Sigma, deployed on a single RTX 4090. The model is built upon the open-source pi0.5_base backbone, with the svla_so101_pickplace dataset preprocessed into a structured training corpus. An independently designed VLA architecture is introduced to integrate deep semantic understanding with associative reasoning, enabling telepathic-style alignment between perception and action. Training proceeds through iterative optimization of data preprocessing, LoRA-based fine-tuning, and inference-stage adapter design. Evaluation is conducted using offline closed-loop replay, comparing Sigma against the untuned pi0.5_base under identical data conditions. Experimental results indicate a consistent reduction in control MSE across vector-, fragment-, and trajectory-level scales, while preserving the stability of the telepathy norm and semantic-text alignment quality. These findings demonstrate that mind-responsive alignment control can be quantitatively achieved through semantic and associative architectural integration without retraining the base model, providing a reproducible pathway for semantic alignment and intention-driven behavior.

## 参考
- http://arxiv.org/abs/2512.00783v3

## Overview
To address a fundamental limitation in cognitive systems, namely the absence of a time-updatable mediating thought space between semantics and continuous control, this work constructs and trains a vision-language-action model termed Sigma, deployed on a single RTX 4090. The model is built upon the open-source pi0.5_base backbone, with the svla_so101_pickplace dataset preprocessed into a structured training corpus. An independently designed VLA architecture is introduced to integrate deep semantic understanding with associative reasoning, enabling telepathic-style alignment between perception and action. Training proceeds through iterative optimization of data preprocessing, LoRA-based fine-tuning, and inference-stage adapter design. Evaluation is conducted using offline closed-loop replay, comparing Sigma against the untuned pi0.5_base under identical data conditions. Experimental results indicate a consistent reduction in control MSE across vector-, fragment-, and trajectory-level scales, while preserving the stability of the telepathy norm and semantic-text alignment quality. These findings demonstrate that mind-responsive alignment control can be quantitatively achieved through semantic and associative architectural integration without retraining the base model, providing a reproducible pathway for semantic alignment and intention-driven behavior.

## Content
To address a fundamental limitation in cognitive systems, namely the absence of a time-updatable mediating thought space between semantics and continuous control, this work constructs and trains a vision-language-action model termed Sigma, deployed on a single RTX 4090. The model is built upon the open-source pi0.5_base backbone, with the svla_so101_pickplace dataset preprocessed into a structured training corpus. An independently designed VLA architecture is introduced to integrate deep semantic understanding with associative reasoning, enabling telepathic-style alignment between perception and action. Training proceeds through iterative optimization of data preprocessing, LoRA-based fine-tuning, and inference-stage adapter design. Evaluation is conducted using offline closed-loop replay, comparing Sigma against the untuned pi0.5_base under identical data conditions. Experimental results indicate a consistent reduction in control MSE across vector-, fragment-, and trajectory-level scales, while preserving the stability of the telepathy norm and semantic-text alignment quality. These findings demonstrate that mind-responsive alignment control can be quantitatively achieved through semantic and associative architectural integration without retraining the base model, providing a reproducible pathway for semantic alignment and intention-driven behavior.

## 개요
인지 시스템의 근본적인 한계, 즉 의미론과 연속 제어 사이에 시간적으로 업데이트 가능한 매개 사고 공간이 없다는 문제를 해결하기 위해, 본 연구는 Sigma라는 비전-언어-행동 모델을 구축 및 훈련하여 단일 RTX 4090에 배포했습니다. 이 모델은 오픈소스 pi0.5_base 백본을 기반으로 하며, svla_so101_pickplace 데이터셋을 구조화된 훈련 코퍼스로 전처리했습니다. 독자적으로 설계된 VLA 아키텍처를 도입하여 심층 의미 이해와 연관 추론을 통합함으로써, 지각과 행동 간의 텔레파시 스타일 정렬을 가능하게 했습니다. 훈련은 데이터 전처리, LoRA 기반 미세 조정, 추론 단계 어댑터 설계의 반복적 최적화를 통해 진행됩니다. 평가는 오프라인 폐루프 재생을 사용하여 동일한 데이터 조건에서 Sigma와 튜닝되지 않은 pi0.5_base를 비교합니다. 실험 결과는 벡터, 조각, 궤적 수준에서 제어 MSE가 일관되게 감소하는 동시에 텔레파시 노름과 의미-텍스트 정렬 품질의 안정성을 유지함을 보여줍니다. 이러한 결과는 기본 모델을 재훈련하지 않고도 의미론적 및 연관 아키텍처 통합을 통해 마음 반응 정렬 제어를 정량적으로 달성할 수 있음을 입증하며, 의미 정렬 및 의도 기반 행동을 위한 재현 가능한 경로를 제공합니다.

## 핵심 내용
인지 시스템의 근본적인 한계, 즉 의미론과 연속 제어 사이에 시간적으로 업데이트 가능한 매개 사고 공간이 없다는 문제를 해결하기 위해, 본 연구는 Sigma라는 비전-언어-행동 모델을 구축 및 훈련하여 단일 RTX 4090에 배포했습니다. 이 모델은 오픈소스 pi0.5_base 백본을 기반으로 하며, svla_so101_pickplace 데이터셋을 구조화된 훈련 코퍼스로 전처리했습니다. 독자적으로 설계된 VLA 아키텍처를 도입하여 심층 의미 이해와 연관 추론을 통합함으로써, 지각과 행동 간의 텔레파시 스타일 정렬을 가능하게 했습니다. 훈련은 데이터 전처리, LoRA 기반 미세 조정, 추론 단계 어댑터 설계의 반복적 최적화를 통해 진행됩니다. 평가는 오프라인 폐루프 재생을 사용하여 동일한 데이터 조건에서 Sigma와 튜닝되지 않은 pi0.5_base를 비교합니다. 실험 결과는 벡터, 조각, 궤적 수준에서 제어 MSE가 일관되게 감소하는 동시에 텔레파시 노름과 의미-텍스트 정렬 품질의 안정성을 유지함을 보여줍니다. 이러한 결과는 기본 모델을 재훈련하지 않고도 의미론적 및 연관 아키텍처 통합을 통해 마음 반응 정렬 제어를 정량적으로 달성할 수 있음을 입증하며, 의미 정렬 및 의도 기반 행동을 위한 재현 가능한 경로를 제공합니다.
