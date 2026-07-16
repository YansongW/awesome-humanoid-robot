---
$id: ent_paper_navdp_learning_sim_to_real_nav_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance'
  zh: 'NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance'
  ko: 'NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance'
summary:
  en: 'NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance is a 2025 work on navigation
    for humanoid robots.'
  zh: 'NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance is a 2025 work on navigation
    for humanoid robots.'
  ko: 'NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance is a 2025 work on navigation
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- navdp
- navigation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.08712v3.
sources:
- id: src_001
  type: paper
  title: 'NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance (arXiv)'
  url: https://arxiv.org/abs/2505.08712
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Learning to navigate in dynamic and complex open-world environments is a critical yet challenging capability for autonomous robots. Existing approaches often rely on cascaded modular frameworks, which require extensive hyperparameter tuning or learning from limited real-world demonstration data. In this paper, we propose Navigation Diffusion Policy (NavDP), an end-to-end network trained solely in simulation that enables zero-shot sim-to-real transfer across diverse environments and robot embodiments. The core of NavDP is a unified transformer-based architecture that jointly learns trajectory generation and trajectory evaluation, both conditioned solely on local RGB-D observation. By learning to predict critic values for contrastive trajectory samples, our proposed approach effectively leverages supervision from privileged information available in simulation, thereby fostering accurate spatial understanding and enabling the distinction between safe and dangerous behaviors. To support this, we develop an efficient data generation pipeline in simulation and construct a large-scale dataset encompassing over one million meters of navigation experience across 3,000 scenes. Empirical experiments in both simulated and real-world environments demonstrate that NavDP significantly outperforms prior state-of-the-art methods. Furthermore, we identify key factors influencing the generalization performance of NavDP. The dataset and code are publicly available at https://wzcai99.github.io/navigation-diffusion-policy.github.io.

## 核心内容
Learning to navigate in dynamic and complex open-world environments is a critical yet challenging capability for autonomous robots. Existing approaches often rely on cascaded modular frameworks, which require extensive hyperparameter tuning or learning from limited real-world demonstration data. In this paper, we propose Navigation Diffusion Policy (NavDP), an end-to-end network trained solely in simulation that enables zero-shot sim-to-real transfer across diverse environments and robot embodiments. The core of NavDP is a unified transformer-based architecture that jointly learns trajectory generation and trajectory evaluation, both conditioned solely on local RGB-D observation. By learning to predict critic values for contrastive trajectory samples, our proposed approach effectively leverages supervision from privileged information available in simulation, thereby fostering accurate spatial understanding and enabling the distinction between safe and dangerous behaviors. To support this, we develop an efficient data generation pipeline in simulation and construct a large-scale dataset encompassing over one million meters of navigation experience across 3,000 scenes. Empirical experiments in both simulated and real-world environments demonstrate that NavDP significantly outperforms prior state-of-the-art methods. Furthermore, we identify key factors influencing the generalization performance of NavDP. The dataset and code are publicly available at https://wzcai99.github.io/navigation-diffusion-policy.github.io.

## 参考
- http://arxiv.org/abs/2505.08712v3

## Overview
Learning to navigate in dynamic and complex open-world environments is a critical yet challenging capability for autonomous robots. Existing approaches often rely on cascaded modular frameworks, which require extensive hyperparameter tuning or learning from limited real-world demonstration data. In this paper, we propose Navigation Diffusion Policy (NavDP), an end-to-end network trained solely in simulation that enables zero-shot sim-to-real transfer across diverse environments and robot embodiments. The core of NavDP is a unified transformer-based architecture that jointly learns trajectory generation and trajectory evaluation, both conditioned solely on local RGB-D observation. By learning to predict critic values for contrastive trajectory samples, our proposed approach effectively leverages supervision from privileged information available in simulation, thereby fostering accurate spatial understanding and enabling the distinction between safe and dangerous behaviors. To support this, we develop an efficient data generation pipeline in simulation and construct a large-scale dataset encompassing over one million meters of navigation experience across 3,000 scenes. Empirical experiments in both simulated and real-world environments demonstrate that NavDP significantly outperforms prior state-of-the-art methods. Furthermore, we identify key factors influencing the generalization performance of NavDP. The dataset and code are publicly available at https://wzcai99.github.io/navigation-diffusion-policy.github.io.

## Content
Learning to navigate in dynamic and complex open-world environments is a critical yet challenging capability for autonomous robots. Existing approaches often rely on cascaded modular frameworks, which require extensive hyperparameter tuning or learning from limited real-world demonstration data. In this paper, we propose Navigation Diffusion Policy (NavDP), an end-to-end network trained solely in simulation that enables zero-shot sim-to-real transfer across diverse environments and robot embodiments. The core of NavDP is a unified transformer-based architecture that jointly learns trajectory generation and trajectory evaluation, both conditioned solely on local RGB-D observation. By learning to predict critic values for contrastive trajectory samples, our proposed approach effectively leverages supervision from privileged information available in simulation, thereby fostering accurate spatial understanding and enabling the distinction between safe and dangerous behaviors. To support this, we develop an efficient data generation pipeline in simulation and construct a large-scale dataset encompassing over one million meters of navigation experience across 3,000 scenes. Empirical experiments in both simulated and real-world environments demonstrate that NavDP significantly outperforms prior state-of-the-art methods. Furthermore, we identify key factors influencing the generalization performance of NavDP. The dataset and code are publicly available at https://wzcai99.github.io/navigation-diffusion-policy.github.io.

## 개요
동적이고 복잡한 오픈월드 환경에서 탐색하는 방법을 학습하는 것은 자율 로봇에게 중요하면서도 도전적인 능력입니다. 기존 접근 방식은 종종 계단식 모듈형 프레임워크에 의존하며, 이는 광범위한 하이퍼파라미터 튜닝이나 제한된 실제 시연 데이터로부터의 학습을 필요로 합니다. 본 논문에서는 시뮬레이션에서만 학습된 종단간 네트워크인 Navigation Diffusion Policy (NavDP)를 제안하며, 이는 다양한 환경과 로봇 구현체에서 제로샷 시뮬레이션-실제 전환을 가능하게 합니다. NavDP의 핵심은 로컬 RGB-D 관찰에만 조건화된 통합 트랜스포머 기반 아키텍처로, 궤적 생성과 궤적 평가를 공동으로 학습합니다. 대조적 궤적 샘플에 대한 비평가 값을 예측하도록 학습함으로써, 제안된 접근 방식은 시뮬레이션에서 이용 가능한 특권 정보로부터의 감독을 효과적으로 활용하여 정확한 공간 이해를 촉진하고 안전한 행동과 위험한 행동을 구별할 수 있게 합니다. 이를 지원하기 위해 시뮬레이션에서 효율적인 데이터 생성 파이프라인을 개발하고, 3,000개 장면에 걸쳐 100만 미터 이상의 탐색 경험을 포함하는 대규모 데이터셋을 구축했습니다. 시뮬레이션 및 실제 환경에서의 실증 실험은 NavDP가 이전 최첨단 방법들을 크게 능가함을 보여줍니다. 또한, NavDP의 일반화 성능에 영향을 미치는 주요 요인들을 식별했습니다. 데이터셋과 코드는 https://wzcai99.github.io/navigation-diffusion-policy.github.io에서 공개적으로 이용 가능합니다.

## 핵심 내용
동적이고 복잡한 오픈월드 환경에서 탐색하는 방법을 학습하는 것은 자율 로봇에게 중요하면서도 도전적인 능력입니다. 기존 접근 방식은 종종 계단식 모듈형 프레임워크에 의존하며, 이는 광범위한 하이퍼파라미터 튜닝이나 제한된 실제 시연 데이터로부터의 학습을 필요로 합니다. 본 논문에서는 시뮬레이션에서만 학습된 종단간 네트워크인 Navigation Diffusion Policy (NavDP)를 제안하며, 이는 다양한 환경과 로봇 구현체에서 제로샷 시뮬레이션-실제 전환을 가능하게 합니다. NavDP의 핵심은 로컬 RGB-D 관찰에만 조건화된 통합 트랜스포머 기반 아키텍처로, 궤적 생성과 궤적 평가를 공동으로 학습합니다. 대조적 궤적 샘플에 대한 비평가 값을 예측하도록 학습함으로써, 제안된 접근 방식은 시뮬레이션에서 이용 가능한 특권 정보로부터의 감독을 효과적으로 활용하여 정확한 공간 이해를 촉진하고 안전한 행동과 위험한 행동을 구별할 수 있게 합니다. 이를 지원하기 위해 시뮬레이션에서 효율적인 데이터 생성 파이프라인을 개발하고, 3,000개 장면에 걸쳐 100만 미터 이상의 탐색 경험을 포함하는 대규모 데이터셋을 구축했습니다. 시뮬레이션 및 실제 환경에서의 실증 실험은 NavDP가 이전 최첨단 방법들을 크게 능가함을 보여줍니다. 또한, NavDP의 일반화 성능에 영향을 미치는 주요 요인들을 식별했습니다. 데이터셋과 코드는 https://wzcai99.github.io/navigation-diffusion-policy.github.io에서 공개적으로 이용 가능합니다.
