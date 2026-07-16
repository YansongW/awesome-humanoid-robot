---
$id: ent_paper_yang_efficientvla_training_free_acc_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models'
  zh: EfficientVLA
  ko: 'EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models'
summary:
  en: 'EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models (EfficientVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by School of Artificial Intelligence, Shanghai
    Jiao Tong University, Harbin Institute of Technology, Xi’an Jiaotong University, University of Electronic Science and
    Technology of China, Anyverse Intelligence, and published at NIPS25.'
  zh: 'EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models (EfficientVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by School of Artificial Intelligence, Shanghai
    Jiao Tong University, Harbin Institute of Technology, Xi’an Jiaotong University, University of Electronic Science and
    Technology of China, Anyverse Intelligence, and published at NIPS25.'
  ko: 'EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models (EfficientVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by School of Artificial Intelligence, Shanghai
    Jiao Tong University, Harbin Institute of Technology, Xi’an Jiaotong University, University of Electronic Science and
    Technology of China, Anyverse Intelligence, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- efficientvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.10100v1.
sources:
- id: src_001
  type: paper
  title: 'EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2506.10100
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: EfficientVLA source
  url: https://doi.org/10.48550/arXiv.2506.10100
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models, particularly diffusion-based architectures, demonstrate transformative potential for embodied intelligence but are severely hampered by high computational and memory demands stemming from extensive inherent and inference-time redundancies. While existing acceleration efforts often target isolated inefficiencies, such piecemeal solutions typically fail to holistically address the varied computational and memory bottlenecks across the entire VLA pipeline, thereby limiting practical deployability. We introduce EfficientVLA, a structured and training-free inference acceleration framework that systematically eliminates these barriers by cohesively exploiting multifaceted redundancies. EfficientVLA synergistically integrates three targeted strategies: (1) pruning of functionally inconsequential layers from the language module, guided by an analysis of inter-layer redundancies; (2) optimizing the visual processing pathway through a task-aware strategy that selects a compact, diverse set of visual tokens, balancing task-criticality with informational coverage; and (3) alleviating temporal computational redundancy within the iterative diffusion-based action head by strategically caching and reusing key intermediate features. We apply our method to a standard VLA model CogACT, yielding a 1.93X inference speedup and reduces FLOPs to 28.9%, with only a 0.6% success rate drop in the SIMPLER benchmark.

## 核心内容
Vision-Language-Action (VLA) models, particularly diffusion-based architectures, demonstrate transformative potential for embodied intelligence but are severely hampered by high computational and memory demands stemming from extensive inherent and inference-time redundancies. While existing acceleration efforts often target isolated inefficiencies, such piecemeal solutions typically fail to holistically address the varied computational and memory bottlenecks across the entire VLA pipeline, thereby limiting practical deployability. We introduce EfficientVLA, a structured and training-free inference acceleration framework that systematically eliminates these barriers by cohesively exploiting multifaceted redundancies. EfficientVLA synergistically integrates three targeted strategies: (1) pruning of functionally inconsequential layers from the language module, guided by an analysis of inter-layer redundancies; (2) optimizing the visual processing pathway through a task-aware strategy that selects a compact, diverse set of visual tokens, balancing task-criticality with informational coverage; and (3) alleviating temporal computational redundancy within the iterative diffusion-based action head by strategically caching and reusing key intermediate features. We apply our method to a standard VLA model CogACT, yielding a 1.93X inference speedup and reduces FLOPs to 28.9%, with only a 0.6% success rate drop in the SIMPLER benchmark.

## 参考
- http://arxiv.org/abs/2506.10100v1

## Overview
Vision-Language-Action (VLA) models, particularly diffusion-based architectures, demonstrate transformative potential for embodied intelligence but are severely hampered by high computational and memory demands stemming from extensive inherent and inference-time redundancies. While existing acceleration efforts often target isolated inefficiencies, such piecemeal solutions typically fail to holistically address the varied computational and memory bottlenecks across the entire VLA pipeline, thereby limiting practical deployability. We introduce EfficientVLA, a structured and training-free inference acceleration framework that systematically eliminates these barriers by cohesively exploiting multifaceted redundancies. EfficientVLA synergistically integrates three targeted strategies: (1) pruning of functionally inconsequential layers from the language module, guided by an analysis of inter-layer redundancies; (2) optimizing the visual processing pathway through a task-aware strategy that selects a compact, diverse set of visual tokens, balancing task-criticality with informational coverage; and (3) alleviating temporal computational redundancy within the iterative diffusion-based action head by strategically caching and reusing key intermediate features. We apply our method to a standard VLA model CogACT, yielding a 1.93X inference speedup and reduces FLOPs to 28.9%, with only a 0.6% success rate drop in the SIMPLER benchmark.

## Content
Vision-Language-Action (VLA) models, particularly diffusion-based architectures, demonstrate transformative potential for embodied intelligence but are severely hampered by high computational and memory demands stemming from extensive inherent and inference-time redundancies. While existing acceleration efforts often target isolated inefficiencies, such piecemeal solutions typically fail to holistically address the varied computational and memory bottlenecks across the entire VLA pipeline, thereby limiting practical deployability. We introduce EfficientVLA, a structured and training-free inference acceleration framework that systematically eliminates these barriers by cohesively exploiting multifaceted redundancies. EfficientVLA synergistically integrates three targeted strategies: (1) pruning of functionally inconsequential layers from the language module, guided by an analysis of inter-layer redundancies; (2) optimizing the visual processing pathway through a task-aware strategy that selects a compact, diverse set of visual tokens, balancing task-criticality with informational coverage; and (3) alleviating temporal computational redundancy within the iterative diffusion-based action head by strategically caching and reusing key intermediate features. We apply our method to a standard VLA model CogACT, yielding a 1.93X inference speedup and reduces FLOPs to 28.9%, with only a 0.6% success rate drop in the SIMPLER benchmark.

## 개요
Vision-Language-Action (VLA) 모델, 특히 확산 기반 아키텍처는 구현된 지능에 혁신적인 잠재력을 보여주지만, 광범위한 고유 및 추론 시간 중복성으로 인한 높은 계산 및 메모리 요구 사항으로 인해 심각한 제약을 받습니다. 기존의 가속화 노력은 종종 고립된 비효율성을 대상으로 하지만, 이러한 부분적 솔루션은 일반적으로 전체 VLA 파이프라인 전반의 다양한 계산 및 메모리 병목 현상을 전체적으로 해결하지 못하여 실제 배포 가능성을 제한합니다. 우리는 구조화되고 훈련이 필요 없는 추론 가속화 프레임워크인 EfficientVLA를 소개합니다. 이는 다각적인 중복성을 응집력 있게 활용하여 이러한 장벽을 체계적으로 제거합니다. EfficientVLA는 세 가지 목표 전략을 시너지적으로 통합합니다: (1) 계층 간 중복성 분석에 기반한 언어 모듈의 기능적으로 중요하지 않은 계층 제거; (2) 작업 인식 전략을 통해 시각적 처리 경로를 최적화하여 작업 중요성과 정보 범위의 균형을 맞춘 간결하고 다양한 시각적 토큰 세트 선택; (3) 반복적 확산 기반 행동 헤드의 시간적 계산 중복성을 주요 중간 특징을 전략적으로 캐싱 및 재사용하여 완화. 우리는 이 방법을 표준 VLA 모델인 CogACT에 적용하여 1.93배의 추론 속도 향상과 FLOPs를 28.9%로 줄였으며, SIMPLER 벤치마크에서 성공률이 0.6%만 감소했습니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델, 특히 확산 기반 아키텍처는 구현된 지능에 혁신적인 잠재력을 보여주지만, 광범위한 고유 및 추론 시간 중복성으로 인한 높은 계산 및 메모리 요구 사항으로 인해 심각한 제약을 받습니다. 기존의 가속화 노력은 종종 고립된 비효율성을 대상으로 하지만, 이러한 부분적 솔루션은 일반적으로 전체 VLA 파이프라인 전반의 다양한 계산 및 메모리 병목 현상을 전체적으로 해결하지 못하여 실제 배포 가능성을 제한합니다. 우리는 구조화되고 훈련이 필요 없는 추론 가속화 프레임워크인 EfficientVLA를 소개합니다. 이는 다각적인 중복성을 응집력 있게 활용하여 이러한 장벽을 체계적으로 제거합니다. EfficientVLA는 세 가지 목표 전략을 시너지적으로 통합합니다: (1) 계층 간 중복성 분석에 기반한 언어 모듈의 기능적으로 중요하지 않은 계층 제거; (2) 작업 인식 전략을 통해 시각적 처리 경로를 최적화하여 작업 중요성과 정보 범위의 균형을 맞춘 간결하고 다양한 시각적 토큰 세트 선택; (3) 반복적 확산 기반 행동 헤드의 시간적 계산 중복성을 주요 중간 특징을 전략적으로 캐싱 및 재사용하여 완화. 우리는 이 방법을 표준 VLA 모델인 CogACT에 적용하여 1.93배의 추론 속도 향상과 FLOPs를 28.9%로 줄였으며, SIMPLER 벤치마크에서 성공률이 0.6%만 감소했습니다.
