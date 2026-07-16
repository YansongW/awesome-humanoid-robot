---
$id: ent_paper_davies_ebt_policy_energy_unlocks_emer_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EBT-Policy: Energy Unlocks Emergent Physical Reasoning Capabilities'
  zh: EBT-Policy
  ko: 'EBT-Policy: Energy Unlocks Emergent Physical Reasoning Capabilities'
summary:
  en: 'EBT-Policy: Energy Unlocks Emergent Physical Reasoning Capabilities (EBT-Policy), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by ZhiCheng AI, UIUC, Tsinghua University, Peking University.'
  zh: 'EBT-Policy: Energy Unlocks Emergent Physical Reasoning Capabilities (EBT-Policy), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by ZhiCheng AI, UIUC, Tsinghua University, Peking University.'
  ko: 'EBT-Policy: Energy Unlocks Emergent Physical Reasoning Capabilities (EBT-Policy), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by ZhiCheng AI, UIUC, Tsinghua University, Peking University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ebt_policy
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.27545v1.
sources:
- id: src_001
  type: paper
  title: 'EBT-Policy: Energy Unlocks Emergent Physical Reasoning Capabilities (arXiv)'
  url: https://arxiv.org/abs/2510.27545
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: EBT-Policy source
  url: https://doi.org/10.48550/arXiv.2510.27545
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Implicit policies parameterized by generative models, such as Diffusion Policy, have become the standard for policy learning and Vision-Language-Action (VLA) models in robotics. However, these approaches often suffer from high computational cost, exposure bias, and unstable inference dynamics, which lead to divergence under distribution shifts. Energy-Based Models (EBMs) address these issues by learning energy landscapes end-to-end and modeling equilibrium dynamics, offering improved robustness and reduced exposure bias. Yet, policies parameterized by EBMs have historically struggled to scale effectively. Recent work on Energy-Based Transformers (EBTs) demonstrates the scalability of EBMs to high-dimensional spaces, but their potential for solving core challenges in physically embodied models remains underexplored. We introduce a new energy-based architecture, EBT-Policy, that solves core issues in robotic and real-world settings. Across simulated and real-world tasks, EBT-Policy consistently outperforms diffusion-based policies, while requiring less training and inference computation. Remarkably, on some tasks it converges within just two inference steps, a 50x reduction compared to Diffusion Policy's 100. Moreover, EBT-Policy exhibits emergent capabilities not seen in prior models, such as zero-shot recovery from failed action sequences using only behavior cloning and without explicit retry training. By leveraging its scalar energy for uncertainty-aware inference and dynamic compute allocation, EBT-Policy offers a promising path toward robust, generalizable robot behavior under distribution shifts.

## 核心内容
Implicit policies parameterized by generative models, such as Diffusion Policy, have become the standard for policy learning and Vision-Language-Action (VLA) models in robotics. However, these approaches often suffer from high computational cost, exposure bias, and unstable inference dynamics, which lead to divergence under distribution shifts. Energy-Based Models (EBMs) address these issues by learning energy landscapes end-to-end and modeling equilibrium dynamics, offering improved robustness and reduced exposure bias. Yet, policies parameterized by EBMs have historically struggled to scale effectively. Recent work on Energy-Based Transformers (EBTs) demonstrates the scalability of EBMs to high-dimensional spaces, but their potential for solving core challenges in physically embodied models remains underexplored. We introduce a new energy-based architecture, EBT-Policy, that solves core issues in robotic and real-world settings. Across simulated and real-world tasks, EBT-Policy consistently outperforms diffusion-based policies, while requiring less training and inference computation. Remarkably, on some tasks it converges within just two inference steps, a 50x reduction compared to Diffusion Policy's 100. Moreover, EBT-Policy exhibits emergent capabilities not seen in prior models, such as zero-shot recovery from failed action sequences using only behavior cloning and without explicit retry training. By leveraging its scalar energy for uncertainty-aware inference and dynamic compute allocation, EBT-Policy offers a promising path toward robust, generalizable robot behavior under distribution shifts.

## 参考
- http://arxiv.org/abs/2510.27545v1

## Overview
Implicit policies parameterized by generative models, such as Diffusion Policy, have become the standard for policy learning and Vision-Language-Action (VLA) models in robotics. However, these approaches often suffer from high computational cost, exposure bias, and unstable inference dynamics, which lead to divergence under distribution shifts. Energy-Based Models (EBMs) address these issues by learning energy landscapes end-to-end and modeling equilibrium dynamics, offering improved robustness and reduced exposure bias. Yet, policies parameterized by EBMs have historically struggled to scale effectively. Recent work on Energy-Based Transformers (EBTs) demonstrates the scalability of EBMs to high-dimensional spaces, but their potential for solving core challenges in physically embodied models remains underexplored. We introduce a new energy-based architecture, EBT-Policy, that solves core issues in robotic and real-world settings. Across simulated and real-world tasks, EBT-Policy consistently outperforms diffusion-based policies, while requiring less training and inference computation. Remarkably, on some tasks it converges within just two inference steps, a 50x reduction compared to Diffusion Policy's 100. Moreover, EBT-Policy exhibits emergent capabilities not seen in prior models, such as zero-shot recovery from failed action sequences using only behavior cloning and without explicit retry training. By leveraging its scalar energy for uncertainty-aware inference and dynamic compute allocation, EBT-Policy offers a promising path toward robust, generalizable robot behavior under distribution shifts.

## Content
Implicit policies parameterized by generative models, such as Diffusion Policy, have become the standard for policy learning and Vision-Language-Action (VLA) models in robotics. However, these approaches often suffer from high computational cost, exposure bias, and unstable inference dynamics, which lead to divergence under distribution shifts. Energy-Based Models (EBMs) address these issues by learning energy landscapes end-to-end and modeling equilibrium dynamics, offering improved robustness and reduced exposure bias. Yet, policies parameterized by EBMs have historically struggled to scale effectively. Recent work on Energy-Based Transformers (EBTs) demonstrates the scalability of EBMs to high-dimensional spaces, but their potential for solving core challenges in physically embodied models remains underexplored. We introduce a new energy-based architecture, EBT-Policy, that solves core issues in robotic and real-world settings. Across simulated and real-world tasks, EBT-Policy consistently outperforms diffusion-based policies, while requiring less training and inference computation. Remarkably, on some tasks it converges within just two inference steps, a 50x reduction compared to Diffusion Policy's 100. Moreover, EBT-Policy exhibits emergent capabilities not seen in prior models, such as zero-shot recovery from failed action sequences using only behavior cloning and without explicit retry training. By leveraging its scalar energy for uncertainty-aware inference and dynamic compute allocation, EBT-Policy offers a promising path toward robust, generalizable robot behavior under distribution shifts.

## 개요
생성 모델로 파라미터화된 암시적 정책(예: Diffusion Policy)은 로봇공학에서 정책 학습 및 VLA(Vision-Language-Action) 모델의 표준이 되었습니다. 그러나 이러한 접근 방식은 종종 높은 계산 비용, 노출 편향, 불안정한 추론 동역학으로 인해 분포 변화 하에서 발산하는 문제를 겪습니다. 에너지 기반 모델(EBM)은 에너지 랜드스케이프를 종단 간 학습하고 평형 동역학을 모델링하여 이러한 문제를 해결하며, 향상된 강건성과 감소된 노출 편향을 제공합니다. 그러나 EBM으로 파라미터화된 정책은 역사적으로 효과적으로 확장하는 데 어려움을 겪었습니다. 최근 EBT(Energy-Based Transformer)에 대한 연구는 EBM이 고차원 공간으로 확장 가능함을 보여주지만, 물리적으로 구현된 모델의 핵심 과제를 해결할 수 있는 잠재력은 아직 충분히 탐구되지 않았습니다. 우리는 로봇 및 실제 환경의 핵심 문제를 해결하는 새로운 에너지 기반 아키텍처인 EBT-Policy를 소개합니다. 시뮬레이션 및 실제 작업 전반에 걸쳐 EBT-Policy는 더 적은 훈련 및 추론 계산을 요구하면서도 확산 기반 정책을 일관되게 능가합니다. 놀랍게도 일부 작업에서는 단 두 번의 추론 단계만으로 수렴하여, Diffusion Policy의 100단계 대비 50배 감소를 달성합니다. 또한 EBT-Policy는 명시적인 재시도 훈련 없이 행동 복제만을 사용하여 실패한 행동 시퀀스로부터 제로샷 복구하는 등 이전 모델에서는 볼 수 없었던 창발적 능력을 보여줍니다. 스칼라 에너지를 활용한 불확실성 인식 추론 및 동적 계산 할당을 통해 EBT-Policy는 분포 변화 하에서 강건하고 일반화 가능한 로봇 행동을 위한 유망한 경로를 제시합니다.

## 핵심 내용
생성 모델로 파라미터화된 암시적 정책(예: Diffusion Policy)은 로봇공학에서 정책 학습 및 VLA(Vision-Language-Action) 모델의 표준이 되었습니다. 그러나 이러한 접근 방식은 종종 높은 계산 비용, 노출 편향, 불안정한 추론 동역학으로 인해 분포 변화 하에서 발산하는 문제를 겪습니다. 에너지 기반 모델(EBM)은 에너지 랜드스케이프를 종단 간 학습하고 평형 동역학을 모델링하여 이러한 문제를 해결하며, 향상된 강건성과 감소된 노출 편향을 제공합니다. 그러나 EBM으로 파라미터화된 정책은 역사적으로 효과적으로 확장하는 데 어려움을 겪었습니다. 최근 EBT(Energy-Based Transformer)에 대한 연구는 EBM이 고차원 공간으로 확장 가능함을 보여주지만, 물리적으로 구현된 모델의 핵심 과제를 해결할 수 있는 잠재력은 아직 충분히 탐구되지 않았습니다. 우리는 로봇 및 실제 환경의 핵심 문제를 해결하는 새로운 에너지 기반 아키텍처인 EBT-Policy를 소개합니다. 시뮬레이션 및 실제 작업 전반에 걸쳐 EBT-Policy는 더 적은 훈련 및 추론 계산을 요구하면서도 확산 기반 정책을 일관되게 능가합니다. 놀랍게도 일부 작업에서는 단 두 번의 추론 단계만으로 수렴하여, Diffusion Policy의 100단계 대비 50배 감소를 달성합니다. 또한 EBT-Policy는 명시적인 재시도 훈련 없이 행동 복제만을 사용하여 실패한 행동 시퀀스로부터 제로샷 복구하는 등 이전 모델에서는 볼 수 없었던 창발적 능력을 보여줍니다. 스칼라 에너지를 활용한 불확실성 인식 추론 및 동적 계산 할당을 통해 EBT-Policy는 분포 변화 하에서 강건하고 일반화 가능한 로봇 행동을 위한 유망한 경로를 제시합니다.
