---
$id: ent_paper_zhang_safevla_towards_safety_alignme_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning'
  zh: SafeVLA
  ko: 'SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning'
summary:
  en: 'SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning (SafeVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Key Laboratory of General Artificial Intelligence,
    Peking University, and published at NIPS25.'
  zh: 'SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning (SafeVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Key Laboratory of General Artificial Intelligence,
    Peking University, and published at NIPS25.'
  ko: 'SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning (SafeVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Key Laboratory of General Artificial Intelligence,
    Peking University, and published at NIPS25.'
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
- safevla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.03480v4.
sources:
- id: src_001
  type: paper
  title: 'SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning (arXiv)'
  url: https://arxiv.org/abs/2503.03480
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action models (VLAs) show potential as generalist robot policies. However, these models pose extreme safety challenges during real-world deployment, including the risk of harm to the environment, the robot itself, and humans. How can safety constraints be explicitly integrated into VLAs? We address this by exploring an integrated safety approach (ISA), systematically modeling safety requirements, then actively eliciting diverse unsafe behaviors, effectively constraining VLA policies via safe reinforcement learning, and rigorously assuring their safety through targeted evaluations. Leveraging the constrained Markov decision process (CMDP) paradigm, ISA optimizes VLAs from a min-max perspective against elicited safety risks. Thus, policies aligned through this comprehensive approach achieve the following key features: (I) effective safety-performance trade-offs, reducing the cumulative cost of safety violations by 83.58% compared to the state-of-the-art method, while also maintaining task success rate (+3.85%). (II) strong safety assurance, with the ability to mitigate long-tail risks and handle extreme failure scenarios. (III) robust generalization of learned safety behaviors to various out-of-distribution perturbations. The effectiveness is evaluated on long-horizon mobile manipulation tasks. Our data, models and newly proposed benchmark environment are available at https://pku-safevla.github.io.

## 核心内容
Vision-language-action models (VLAs) show potential as generalist robot policies. However, these models pose extreme safety challenges during real-world deployment, including the risk of harm to the environment, the robot itself, and humans. How can safety constraints be explicitly integrated into VLAs? We address this by exploring an integrated safety approach (ISA), systematically modeling safety requirements, then actively eliciting diverse unsafe behaviors, effectively constraining VLA policies via safe reinforcement learning, and rigorously assuring their safety through targeted evaluations. Leveraging the constrained Markov decision process (CMDP) paradigm, ISA optimizes VLAs from a min-max perspective against elicited safety risks. Thus, policies aligned through this comprehensive approach achieve the following key features: (I) effective safety-performance trade-offs, reducing the cumulative cost of safety violations by 83.58% compared to the state-of-the-art method, while also maintaining task success rate (+3.85%). (II) strong safety assurance, with the ability to mitigate long-tail risks and handle extreme failure scenarios. (III) robust generalization of learned safety behaviors to various out-of-distribution perturbations. The effectiveness is evaluated on long-horizon mobile manipulation tasks. Our data, models and newly proposed benchmark environment are available at https://pku-safevla.github.io.

## 参考
- http://arxiv.org/abs/2503.03480v4

## Overview
Vision-language-action models (VLAs) show potential as generalist robot policies. However, these models pose extreme safety challenges during real-world deployment, including the risk of harm to the environment, the robot itself, and humans. How can safety constraints be explicitly integrated into VLAs? We address this by exploring an integrated safety approach (ISA), systematically modeling safety requirements, then actively eliciting diverse unsafe behaviors, effectively constraining VLA policies via safe reinforcement learning, and rigorously assuring their safety through targeted evaluations. Leveraging the constrained Markov decision process (CMDP) paradigm, ISA optimizes VLAs from a min-max perspective against elicited safety risks. Thus, policies aligned through this comprehensive approach achieve the following key features: (I) effective safety-performance trade-offs, reducing the cumulative cost of safety violations by 83.58% compared to the state-of-the-art method, while also maintaining task success rate (+3.85%). (II) strong safety assurance, with the ability to mitigate long-tail risks and handle extreme failure scenarios. (III) robust generalization of learned safety behaviors to various out-of-distribution perturbations. The effectiveness is evaluated on long-horizon mobile manipulation tasks. Our data, models and newly proposed benchmark environment are available at https://pku-safevla.github.io.

## Content
Vision-language-action models (VLAs) show potential as generalist robot policies. However, these models pose extreme safety challenges during real-world deployment, including the risk of harm to the environment, the robot itself, and humans. How can safety constraints be explicitly integrated into VLAs? We address this by exploring an integrated safety approach (ISA), systematically modeling safety requirements, then actively eliciting diverse unsafe behaviors, effectively constraining VLA policies via safe reinforcement learning, and rigorously assuring their safety through targeted evaluations. Leveraging the constrained Markov decision process (CMDP) paradigm, ISA optimizes VLAs from a min-max perspective against elicited safety risks. Thus, policies aligned through this comprehensive approach achieve the following key features: (I) effective safety-performance trade-offs, reducing the cumulative cost of safety violations by 83.58% compared to the state-of-the-art method, while also maintaining task success rate (+3.85%). (II) strong safety assurance, with the ability to mitigate long-tail risks and handle extreme failure scenarios. (III) robust generalization of learned safety behaviors to various out-of-distribution perturbations. The effectiveness is evaluated on long-horizon mobile manipulation tasks. Our data, models and newly proposed benchmark environment are available at https://pku-safevla.github.io.

## 개요
Vision-language-action models (VLAs)는 범용 로봇 정책으로서 잠재력을 보여줍니다. 그러나 이러한 모델은 실제 환경에서 배포 시 환경, 로봇 자체, 인간에 대한 위험을 포함한 극심한 안전 문제를 제기합니다. 어떻게 안전 제약 조건을 VLA에 명시적으로 통합할 수 있을까요? 우리는 통합 안전 접근법(ISA)을 탐구하여 이 문제를 해결합니다. 이 접근법은 안전 요구 사항을 체계적으로 모델링한 후, 다양한 불안전 행동을 적극적으로 유도하고, 안전 강화 학습을 통해 VLA 정책을 효과적으로 제약하며, 목표 지향 평가를 통해 엄격하게 안전을 보장합니다. 제약된 마르코프 결정 과정(CMDP) 패러다임을 활용하여 ISA는 유도된 안전 위험에 대해 최소-최대 관점에서 VLA를 최적화합니다. 따라서 이 포괄적인 접근법을 통해 정렬된 정책은 다음과 같은 주요 특징을 달성합니다: (I) 효과적인 안전-성능 트레이드오프, 최신 방법 대비 안전 위반 누적 비용을 83.58% 감소시키면서 작업 성공률을 유지(+3.85%). (II) 강력한 안전 보장, 긴 꼬리 위험을 완화하고 극단적인 실패 시나리오를 처리할 수 있는 능력. (III) 학습된 안전 행동의 다양한 분포 외 교란에 대한 강건한 일반화. 효과성은 장기 이동 조작 작업에서 평가됩니다. 우리의 데이터, 모델 및 새롭게 제안된 벤치마크 환경은 https://pku-safevla.github.io에서 확인할 수 있습니다.

## 핵심 내용
Vision-language-action models (VLAs)는 범용 로봇 정책으로서 잠재력을 보여줍니다. 그러나 이러한 모델은 실제 환경에서 배포 시 환경, 로봇 자체, 인간에 대한 위험을 포함한 극심한 안전 문제를 제기합니다. 어떻게 안전 제약 조건을 VLA에 명시적으로 통합할 수 있을까요? 우리는 통합 안전 접근법(ISA)을 탐구하여 이 문제를 해결합니다. 이 접근법은 안전 요구 사항을 체계적으로 모델링한 후, 다양한 불안전 행동을 적극적으로 유도하고, 안전 강화 학습을 통해 VLA 정책을 효과적으로 제약하며, 목표 지향 평가를 통해 엄격하게 안전을 보장합니다. 제약된 마르코프 결정 과정(CMDP) 패러다임을 활용하여 ISA는 유도된 안전 위험에 대해 최소-최대 관점에서 VLA를 최적화합니다. 따라서 이 포괄적인 접근법을 통해 정렬된 정책은 다음과 같은 주요 특징을 달성합니다: (I) 효과적인 안전-성능 트레이드오프, 최신 방법 대비 안전 위반 누적 비용을 83.58% 감소시키면서 작업 성공률을 유지(+3.85%). (II) 강력한 안전 보장, 긴 꼬리 위험을 완화하고 극단적인 실패 시나리오를 처리할 수 있는 능력. (III) 학습된 안전 행동의 다양한 분포 외 교란에 대한 강건한 일반화. 효과성은 장기 이동 조작 작업에서 평가됩니다. 우리의 데이터, 모델 및 새롭게 제안된 벤치마크 환경은 https://pku-safevla.github.io에서 확인할 수 있습니다.
