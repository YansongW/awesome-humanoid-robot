---
$id: ent_paper_zhang_gevrm_goal_expressive_video_ge_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GEVRM: Goal-Expressive Video Generation Model For Robust Visual Manipulation'
  zh: GEVRM
  ko: 'GEVRM: Goal-Expressive Video Generation Model For Robust Visual Manipulation'
summary:
  en: 'GEVRM: Goal-Expressive Video Generation Model For Robust Visual Manipulation (GEVRM), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Zhejiang University, Westlake University, and published at ICLR25.'
  zh: 'GEVRM: Goal-Expressive Video Generation Model For Robust Visual Manipulation (GEVRM), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Zhejiang University, Westlake University, and published at ICLR25.'
  ko: 'GEVRM: Goal-Expressive Video Generation Model For Robust Visual Manipulation (GEVRM), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Zhejiang University, Westlake University, and published at ICLR25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- gevrm
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.09268v2.
sources:
- id: src_001
  type: paper
  title: GEVRM source
  url: https://openreview.net/forum?id=hPWWXpCaJ7
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
With the rapid development of embodied artificial intelligence, significant progress has been made in vision-language-action (VLA) models for general robot decision-making. However, the majority of existing VLAs fail to account for the inevitable external perturbations encountered during deployment. These perturbations introduce unforeseen state information to the VLA, resulting in inaccurate actions and consequently, a significant decline in generalization performance. The classic internal model control (IMC) principle demonstrates that a closed-loop system with an internal model that includes external input signals can accurately track the reference input and effectively offset the disturbance. We propose a novel closed-loop VLA method GEVRM that integrates the IMC principle to enhance the robustness of robot visual manipulation. The text-guided video generation model in GEVRM can generate highly expressive future visual planning goals. Simultaneously, we evaluate perturbations by simulating responses, which are called internal embeddings and optimized through prototype contrastive learning. This allows the model to implicitly infer and distinguish perturbations from the external environment. The proposed GEVRM achieves state-of-the-art performance on both standard and perturbed CALVIN benchmarks and shows significant improvements in realistic robot tasks.

## 核心内容
With the rapid development of embodied artificial intelligence, significant progress has been made in vision-language-action (VLA) models for general robot decision-making. However, the majority of existing VLAs fail to account for the inevitable external perturbations encountered during deployment. These perturbations introduce unforeseen state information to the VLA, resulting in inaccurate actions and consequently, a significant decline in generalization performance. The classic internal model control (IMC) principle demonstrates that a closed-loop system with an internal model that includes external input signals can accurately track the reference input and effectively offset the disturbance. We propose a novel closed-loop VLA method GEVRM that integrates the IMC principle to enhance the robustness of robot visual manipulation. The text-guided video generation model in GEVRM can generate highly expressive future visual planning goals. Simultaneously, we evaluate perturbations by simulating responses, which are called internal embeddings and optimized through prototype contrastive learning. This allows the model to implicitly infer and distinguish perturbations from the external environment. The proposed GEVRM achieves state-of-the-art performance on both standard and perturbed CALVIN benchmarks and shows significant improvements in realistic robot tasks.

## 参考
- http://arxiv.org/abs/2502.09268v2

## Overview
With the rapid development of embodied artificial intelligence, significant progress has been made in vision-language-action (VLA) models for general robot decision-making. However, the majority of existing VLAs fail to account for the inevitable external perturbations encountered during deployment. These perturbations introduce unforeseen state information to the VLA, resulting in inaccurate actions and consequently, a significant decline in generalization performance. The classic internal model control (IMC) principle demonstrates that a closed-loop system with an internal model that includes external input signals can accurately track the reference input and effectively offset the disturbance. We propose a novel closed-loop VLA method GEVRM that integrates the IMC principle to enhance the robustness of robot visual manipulation. The text-guided video generation model in GEVRM can generate highly expressive future visual planning goals. Simultaneously, we evaluate perturbations by simulating responses, which are called internal embeddings and optimized through prototype contrastive learning. This allows the model to implicitly infer and distinguish perturbations from the external environment. The proposed GEVRM achieves state-of-the-art performance on both standard and perturbed CALVIN benchmarks and shows significant improvements in realistic robot tasks.

## Content
With the rapid development of embodied artificial intelligence, significant progress has been made in vision-language-action (VLA) models for general robot decision-making. However, the majority of existing VLAs fail to account for the inevitable external perturbations encountered during deployment. These perturbations introduce unforeseen state information to the VLA, resulting in inaccurate actions and consequently, a significant decline in generalization performance. The classic internal model control (IMC) principle demonstrates that a closed-loop system with an internal model that includes external input signals can accurately track the reference input and effectively offset the disturbance. We propose a novel closed-loop VLA method GEVRM that integrates the IMC principle to enhance the robustness of robot visual manipulation. The text-guided video generation model in GEVRM can generate highly expressive future visual planning goals. Simultaneously, we evaluate perturbations by simulating responses, which are called internal embeddings and optimized through prototype contrastive learning. This allows the model to implicitly infer and distinguish perturbations from the external environment. The proposed GEVRM achieves state-of-the-art performance on both standard and perturbed CALVIN benchmarks and shows significant improvements in realistic robot tasks.

## 개요
체화 인공지능의 급속한 발전에 힘입어, 일반 로봇 의사 결정을 위한 시각-언어-행동(VLA) 모델에서 상당한 진전이 이루어졌습니다. 그러나 기존 VLA의 대부분은 배포 중에 발생하는 불가피한 외부 교란을 고려하지 못합니다. 이러한 교란은 VLA에 예상치 못한 상태 정보를 도입하여 부정확한 행동을 초래하고, 결과적으로 일반화 성능이 크게 저하됩니다. 고전적인 내부 모델 제어(IMC) 원리는 외부 입력 신호를 포함하는 내부 모델을 가진 폐루프 시스템이 기준 입력을 정확히 추적하고 교란을 효과적으로 상쇄할 수 있음을 보여줍니다. 우리는 IMC 원리를 통합하여 로봇 시각 조작의 강건성을 향상시키는 새로운 폐루프 VLA 방법인 GEVRM을 제안합니다. GEVRM의 텍스트 유도 비디오 생성 모델은 표현력이 뛰어난 미래 시각 계획 목표를 생성할 수 있습니다. 동시에, 우리는 내부 임베딩이라고 불리는 시뮬레이션 응답을 통해 교란을 평가하고, 프로토타입 대조 학습을 통해 이를 최적화합니다. 이를 통해 모델이 외부 환경의 교란을 암시적으로 추론하고 구별할 수 있습니다. 제안된 GEVRM은 표준 및 교란된 CALVIN 벤치마크 모두에서 최첨단 성능을 달성하며, 실제 로봇 작업에서 상당한 개선을 보여줍니다.

## 핵심 내용
체화 인공지능의 급속한 발전에 힘입어, 일반 로봇 의사 결정을 위한 시각-언어-행동(VLA) 모델에서 상당한 진전이 이루어졌습니다. 그러나 기존 VLA의 대부분은 배포 중에 발생하는 불가피한 외부 교란을 고려하지 못합니다. 이러한 교란은 VLA에 예상치 못한 상태 정보를 도입하여 부정확한 행동을 초래하고, 결과적으로 일반화 성능이 크게 저하됩니다. 고전적인 내부 모델 제어(IMC) 원리는 외부 입력 신호를 포함하는 내부 모델을 가진 폐루프 시스템이 기준 입력을 정확히 추적하고 교란을 효과적으로 상쇄할 수 있음을 보여줍니다. 우리는 IMC 원리를 통합하여 로봇 시각 조작의 강건성을 향상시키는 새로운 폐루프 VLA 방법인 GEVRM을 제안합니다. GEVRM의 텍스트 유도 비디오 생성 모델은 표현력이 뛰어난 미래 시각 계획 목표를 생성할 수 있습니다. 동시에, 우리는 내부 임베딩이라고 불리는 시뮬레이션 응답을 통해 교란을 평가하고, 프로토타입 대조 학습을 통해 이를 최적화합니다. 이를 통해 모델이 외부 환경의 교란을 암시적으로 추론하고 구별할 수 있습니다. 제안된 GEVRM은 표준 및 교란된 CALVIN 벤치마크 모두에서 최첨단 성능을 달성하며, 실제 로봇 작업에서 상당한 개선을 보여줍니다.
