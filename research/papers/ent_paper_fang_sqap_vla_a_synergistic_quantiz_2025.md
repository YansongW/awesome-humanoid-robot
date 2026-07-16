---
$id: ent_paper_fang_sqap_vla_a_synergistic_quantiz_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SQAP-VLA: A Synergistic Quantization-Aware Pruning Framework for High-Performance Vision-Language-Action Models'
  zh: SQAP-VLA
  ko: 'SQAP-VLA: A Synergistic Quantization-Aware Pruning Framework for High-Performance Vision-Language-Action Models'
summary:
  en: 'SQAP-VLA: A Synergistic Quantization-Aware Pruning Framework for High-Performance Vision-Language-Action Models (SQAP-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by School of Electronic Science and
    Engineering, Nanjing University, University of Arizona.'
  zh: 'SQAP-VLA: A Synergistic Quantization-Aware Pruning Framework for High-Performance Vision-Language-Action Models (SQAP-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by School of Electronic Science and
    Engineering, Nanjing University, University of Arizona.'
  ko: 'SQAP-VLA: A Synergistic Quantization-Aware Pruning Framework for High-Performance Vision-Language-Action Models (SQAP-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by School of Electronic Science and
    Engineering, Nanjing University, University of Arizona.'
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
- sqap_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.09090v1.
sources:
- id: src_001
  type: paper
  title: 'SQAP-VLA: A Synergistic Quantization-Aware Pruning Framework for High-Performance Vision-Language-Action Models
    (arXiv)'
  url: https://arxiv.org/abs/2509.09090
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SQAP-VLA source
  url: https://doi.org/10.48550/arXiv.2509.09090
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models exhibit unprecedented capabilities for embodied intelligence. However, their extensive computational and memory costs hinder their practical deployment. Existing VLA compression and acceleration approaches conduct quantization or token pruning in an ad-hoc manner but fail to enable both for a holistic efficiency improvement due to an observed incompatibility. This work introduces SQAP-VLA, the first structured, training-free VLA inference acceleration framework that simultaneously enables state-of-the-art quantization and token pruning. We overcome the incompatibility by co-designing the quantization and token pruning pipeline, where we propose new quantization-aware token pruning criteria that work on an aggressively quantized model while improving the quantizer design to enhance pruning effectiveness. When applied to standard VLA models, SQAP-VLA yields significant gains in computational efficiency and inference speed while successfully preserving core model performance, achieving a $\times$1.93 speedup and up to a 4.5\% average success rate enhancement compared to the original model.

## 核心内容
Vision-Language-Action (VLA) models exhibit unprecedented capabilities for embodied intelligence. However, their extensive computational and memory costs hinder their practical deployment. Existing VLA compression and acceleration approaches conduct quantization or token pruning in an ad-hoc manner but fail to enable both for a holistic efficiency improvement due to an observed incompatibility. This work introduces SQAP-VLA, the first structured, training-free VLA inference acceleration framework that simultaneously enables state-of-the-art quantization and token pruning. We overcome the incompatibility by co-designing the quantization and token pruning pipeline, where we propose new quantization-aware token pruning criteria that work on an aggressively quantized model while improving the quantizer design to enhance pruning effectiveness. When applied to standard VLA models, SQAP-VLA yields significant gains in computational efficiency and inference speed while successfully preserving core model performance, achieving a $\times$1.93 speedup and up to a 4.5\% average success rate enhancement compared to the original model.

## 参考
- http://arxiv.org/abs/2509.09090v1

## Overview
Vision-Language-Action (VLA) models exhibit unprecedented capabilities for embodied intelligence. However, their extensive computational and memory costs hinder their practical deployment. Existing VLA compression and acceleration approaches conduct quantization or token pruning in an ad-hoc manner but fail to enable both for a holistic efficiency improvement due to an observed incompatibility. This work introduces SQAP-VLA, the first structured, training-free VLA inference acceleration framework that simultaneously enables state-of-the-art quantization and token pruning. We overcome the incompatibility by co-designing the quantization and token pruning pipeline, where we propose new quantization-aware token pruning criteria that work on an aggressively quantized model while improving the quantizer design to enhance pruning effectiveness. When applied to standard VLA models, SQAP-VLA yields significant gains in computational efficiency and inference speed while successfully preserving core model performance, achieving a $\times$1.93 speedup and up to a 4.5\% average success rate enhancement compared to the original model.

## Content
Vision-Language-Action (VLA) models exhibit unprecedented capabilities for embodied intelligence. However, their extensive computational and memory costs hinder their practical deployment. Existing VLA compression and acceleration approaches conduct quantization or token pruning in an ad-hoc manner but fail to enable both for a holistic efficiency improvement due to an observed incompatibility. This work introduces SQAP-VLA, the first structured, training-free VLA inference acceleration framework that simultaneously enables state-of-the-art quantization and token pruning. We overcome the incompatibility by co-designing the quantization and token pruning pipeline, where we propose new quantization-aware token pruning criteria that work on an aggressively quantized model while improving the quantizer design to enhance pruning effectiveness. When applied to standard VLA models, SQAP-VLA yields significant gains in computational efficiency and inference speed while successfully preserving core model performance, achieving a $\times$1.93 speedup and up to a 4.5\% average success rate enhancement compared to the original model.

## 개요
Vision-Language-Action (VLA) 모델은 구현된 지능에서 전례 없는 능력을 보여줍니다. 그러나 이들의 방대한 계산 및 메모리 비용은 실제 배포를 어렵게 만듭니다. 기존 VLA 압축 및 가속 접근 방식은 임시 방식으로 양자화 또는 토큰 가지치기를 수행하지만, 관찰된 비호환성으로 인해 전체적인 효율성 향상을 위해 두 가지를 동시에 활성화하지 못합니다. 본 연구는 SQAP-VLA를 소개합니다. 이는 최첨단 양자화와 토큰 가지치기를 동시에 가능하게 하는 최초의 구조화된, 훈련 없는 VLA 추론 가속 프레임워크입니다. 우리는 양자화와 토큰 가지치기 파이프라인을 공동 설계하여 비호환성을 극복합니다. 여기서는 공격적으로 양자화된 모델에서 작동하는 새로운 양자화 인식 토큰 가지치기 기준을 제안하고, 가지치기 효과를 향상시키기 위해 양자화기 설계를 개선합니다. 표준 VLA 모델에 적용했을 때, SQAP-VLA는 핵심 모델 성능을 성공적으로 유지하면서 계산 효율성과 추론 속도에서 상당한 이점을 제공하며, 원본 모델 대비 $\times$1.93 속도 향상과 최대 4.5%의 평균 성공률 향상을 달성합니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 구현된 지능에서 전례 없는 능력을 보여줍니다. 그러나 이들의 방대한 계산 및 메모리 비용은 실제 배포를 어렵게 만듭니다. 기존 VLA 압축 및 가속 접근 방식은 임시 방식으로 양자화 또는 토큰 가지치기를 수행하지만, 관찰된 비호환성으로 인해 전체적인 효율성 향상을 위해 두 가지를 동시에 활성화하지 못합니다. 본 연구는 SQAP-VLA를 소개합니다. 이는 최첨단 양자화와 토큰 가지치기를 동시에 가능하게 하는 최초의 구조화된, 훈련 없는 VLA 추론 가속 프레임워크입니다. 우리는 양자화와 토큰 가지치기 파이프라인을 공동 설계하여 비호환성을 극복합니다. 여기서는 공격적으로 양자화된 모델에서 작동하는 새로운 양자화 인식 토큰 가지치기 기준을 제안하고, 가지치기 효과를 향상시키기 위해 양자화기 설계를 개선합니다. 표준 VLA 모델에 적용했을 때, SQAP-VLA는 핵심 모델 성능을 성공적으로 유지하면서 계산 효율성과 추론 속도에서 상당한 이점을 제공하며, 원본 모델 대비 $\times$1.93 속도 향상과 최대 4.5%의 평균 성공률 향상을 달성합니다.
