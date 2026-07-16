---
$id: ent_paper_li_simplevla_rl_scaling_vla_train_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning'
  zh: SimpleVLA-RL
  ko: 'SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning'
summary:
  en: 'SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning (SimpleVLA-RL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Tsinghua University.'
  zh: 'SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning (SimpleVLA-RL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Tsinghua University.'
  ko: 'SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning (SimpleVLA-RL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Tsinghua University.'
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
- simplevla_rl
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.09674v1.
sources:
- id: src_001
  type: paper
  title: 'SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning (arXiv)'
  url: https://arxiv.org/abs/2509.09674
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SimpleVLA-RL source
  url: https://doi.org/10.48550/arXiv.2509.09674
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have recently emerged as a powerful paradigm for robotic manipulation. Despite substantial progress enabled by large-scale pretraining and supervised fine-tuning (SFT), these models face two fundamental challenges: (i) the scarcity and high cost of large-scale human-operated robotic trajectories required for SFT scaling, and (ii) limited generalization to tasks involving distribution shift. Recent breakthroughs in Large Reasoning Models (LRMs) demonstrate that reinforcement learning (RL) can dramatically enhance step-by-step reasoning capabilities, raising a natural question: Can RL similarly improve the long-horizon step-by-step action planning of VLA? In this work, we introduce SimpleVLA-RL, an efficient RL framework tailored for VLA models. Building upon veRL, we introduce VLA-specific trajectory sampling, scalable parallelization, multi-environment rendering, and optimized loss computation. When applied to OpenVLA-OFT, SimpleVLA-RL achieves SoTA performance on LIBERO and even outperforms $π_0$ on RoboTwin 1.0\&2.0 with the exploration-enhancing strategies we introduce. SimpleVLA-RL not only reduces dependence on large-scale data and enables robust generalization, but also remarkably surpasses SFT in real-world tasks. Moreover, we identify a novel phenomenon ``pushcut'' during RL training, wherein the policy discovers previously unseen patterns beyond those seen in the previous training process. Github: https://github.com/PRIME-RL/SimpleVLA-RL

## 核心内容
Vision-Language-Action (VLA) models have recently emerged as a powerful paradigm for robotic manipulation. Despite substantial progress enabled by large-scale pretraining and supervised fine-tuning (SFT), these models face two fundamental challenges: (i) the scarcity and high cost of large-scale human-operated robotic trajectories required for SFT scaling, and (ii) limited generalization to tasks involving distribution shift. Recent breakthroughs in Large Reasoning Models (LRMs) demonstrate that reinforcement learning (RL) can dramatically enhance step-by-step reasoning capabilities, raising a natural question: Can RL similarly improve the long-horizon step-by-step action planning of VLA? In this work, we introduce SimpleVLA-RL, an efficient RL framework tailored for VLA models. Building upon veRL, we introduce VLA-specific trajectory sampling, scalable parallelization, multi-environment rendering, and optimized loss computation. When applied to OpenVLA-OFT, SimpleVLA-RL achieves SoTA performance on LIBERO and even outperforms $π_0$ on RoboTwin 1.0\&2.0 with the exploration-enhancing strategies we introduce. SimpleVLA-RL not only reduces dependence on large-scale data and enables robust generalization, but also remarkably surpasses SFT in real-world tasks. Moreover, we identify a novel phenomenon ``pushcut'' during RL training, wherein the policy discovers previously unseen patterns beyond those seen in the previous training process. Github: https://github.com/PRIME-RL/SimpleVLA-RL

## 参考
- http://arxiv.org/abs/2509.09674v1

## Overview
Vision-Language-Action (VLA) models have recently emerged as a powerful paradigm for robotic manipulation. Despite substantial progress enabled by large-scale pretraining and supervised fine-tuning (SFT), these models face two fundamental challenges: (i) the scarcity and high cost of large-scale human-operated robotic trajectories required for SFT scaling, and (ii) limited generalization to tasks involving distribution shift. Recent breakthroughs in Large Reasoning Models (LRMs) demonstrate that reinforcement learning (RL) can dramatically enhance step-by-step reasoning capabilities, raising a natural question: Can RL similarly improve the long-horizon step-by-step action planning of VLA? In this work, we introduce SimpleVLA-RL, an efficient RL framework tailored for VLA models. Building upon veRL, we introduce VLA-specific trajectory sampling, scalable parallelization, multi-environment rendering, and optimized loss computation. When applied to OpenVLA-OFT, SimpleVLA-RL achieves SoTA performance on LIBERO and even outperforms $π_0$ on RoboTwin 1.0\&2.0 with the exploration-enhancing strategies we introduce. SimpleVLA-RL not only reduces dependence on large-scale data and enables robust generalization, but also remarkably surpasses SFT in real-world tasks. Moreover, we identify a novel phenomenon ``pushcut'' during RL training, wherein the policy discovers previously unseen patterns beyond those seen in the previous training process. Github: https://github.com/PRIME-RL/SimpleVLA-RL

## Content
Vision-Language-Action (VLA) models have recently emerged as a powerful paradigm for robotic manipulation. Despite substantial progress enabled by large-scale pretraining and supervised fine-tuning (SFT), these models face two fundamental challenges: (i) the scarcity and high cost of large-scale human-operated robotic trajectories required for SFT scaling, and (ii) limited generalization to tasks involving distribution shift. Recent breakthroughs in Large Reasoning Models (LRMs) demonstrate that reinforcement learning (RL) can dramatically enhance step-by-step reasoning capabilities, raising a natural question: Can RL similarly improve the long-horizon step-by-step action planning of VLA? In this work, we introduce SimpleVLA-RL, an efficient RL framework tailored for VLA models. Building upon veRL, we introduce VLA-specific trajectory sampling, scalable parallelization, multi-environment rendering, and optimized loss computation. When applied to OpenVLA-OFT, SimpleVLA-RL achieves SoTA performance on LIBERO and even outperforms $π_0$ on RoboTwin 1.0\&2.0 with the exploration-enhancing strategies we introduce. SimpleVLA-RL not only reduces dependence on large-scale data and enables robust generalization, but also remarkably surpasses SFT in real-world tasks. Moreover, we identify a novel phenomenon ``pushcut'' during RL training, wherein the policy discovers previously unseen patterns beyond those seen in the previous training process. Github: https://github.com/PRIME-RL/SimpleVLA-RL

## 개요
Vision-Language-Action (VLA) 모델은 최근 로봇 조작을 위한 강력한 패러다임으로 부상했습니다. 대규모 사전 학습과 지도 미세 조정(SFT)을 통해 상당한 진전이 이루어졌음에도 불구하고, 이러한 모델은 두 가지 근본적인 과제에 직면해 있습니다: (i) SFT 확장에 필요한 대규모 인간 조작 로봇 궤적의 희소성과 높은 비용, (ii) 분포 변화를 수반하는 작업에 대한 제한된 일반화. 최근 Large Reasoning Models (LRMs)의 획기적인 발전은 강화 학습(RL)이 단계별 추론 능력을 극적으로 향상시킬 수 있음을 보여주며, 자연스러운 질문을 제기합니다: RL이 VLA의 장기적 단계별 행동 계획을 유사하게 개선할 수 있을까요? 본 연구에서는 VLA 모델에 특화된 효율적인 RL 프레임워크인 SimpleVLA-RL을 소개합니다. veRL을 기반으로, VLA 특화 궤적 샘플링, 확장 가능한 병렬화, 다중 환경 렌더링, 최적화된 손실 계산을 도입했습니다. OpenVLA-OFT에 적용했을 때, SimpleVLA-RL은 LIBERO에서 최첨단 성능을 달성하고, 우리가 도입한 탐색 강화 전략을 통해 RoboTwin 1.0\&2.0에서 $π_0$를 능가합니다. SimpleVLA-RL은 대규모 데이터에 대한 의존성을 줄이고 강력한 일반화를 가능하게 할 뿐만 아니라, 실제 작업에서 SFT를 현저히 능가합니다. 또한, RL 훈련 중에 정책이 이전 훈련 과정에서 보지 못한 새로운 패턴을 발견하는 "pushcut"이라는 새로운 현상을 식별했습니다. Github: https://github.com/PRIME-RL/SimpleVLA-RL

## 핵심 내용
Vision-Language-Action (VLA) 모델은 최근 로봇 조작을 위한 강력한 패러다임으로 부상했습니다. 대규모 사전 학습과 지도 미세 조정(SFT)을 통해 상당한 진전이 이루어졌음에도 불구하고, 이러한 모델은 두 가지 근본적인 과제에 직면해 있습니다: (i) SFT 확장에 필요한 대규모 인간 조작 로봇 궤적의 희소성과 높은 비용, (ii) 분포 변화를 수반하는 작업에 대한 제한된 일반화. 최근 Large Reasoning Models (LRMs)의 획기적인 발전은 강화 학습(RL)이 단계별 추론 능력을 극적으로 향상시킬 수 있음을 보여주며, 자연스러운 질문을 제기합니다: RL이 VLA의 장기적 단계별 행동 계획을 유사하게 개선할 수 있을까요? 본 연구에서는 VLA 모델에 특화된 효율적인 RL 프레임워크인 SimpleVLA-RL을 소개합니다. veRL을 기반으로, VLA 특화 궤적 샘플링, 확장 가능한 병렬화, 다중 환경 렌더링, 최적화된 손실 계산을 도입했습니다. OpenVLA-OFT에 적용했을 때, SimpleVLA-RL은 LIBERO에서 최첨단 성능을 달성하고, 우리가 도입한 탐색 강화 전략을 통해 RoboTwin 1.0\&2.0에서 $π_0$를 능가합니다. SimpleVLA-RL은 대규모 데이터에 대한 의존성을 줄이고 강력한 일반화를 가능하게 할 뿐만 아니라, 실제 작업에서 SFT를 현저히 능가합니다. 또한, RL 훈련 중에 정책이 이전 훈련 과정에서 보지 못한 새로운 패턴을 발견하는 "pushcut"이라는 새로운 현상을 식별했습니다. Github: https://github.com/PRIME-RL/SimpleVLA-RL
