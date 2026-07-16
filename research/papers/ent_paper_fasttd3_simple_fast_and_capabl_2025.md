---
$id: ent_paper_fasttd3_simple_fast_and_capabl_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FastTD3: Simple, Fast, and Capable Reinforcement Learning for Humanoid Control'
  zh: 'FastTD3: Simple, Fast, and Capable Reinforcement Learning for Humanoid Control'
  ko: 'FastTD3: Simple, Fast, and Capable Reinforcement Learning for Humanoid Control'
summary:
  en: 'FastTD3: Simple, Fast, and Capable Reinforcement Learning for Humanoid Control is a 2025 work on locomotion for humanoid
    robots.'
  zh: 'FastTD3: Simple, Fast, and Capable Reinforcement Learning for Humanoid Control is a 2025 work on locomotion for humanoid
    robots.'
  ko: 'FastTD3: Simple, Fast, and Capable Reinforcement Learning for Humanoid Control is a 2025 work on locomotion for humanoid
    robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- fasttd3
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.22642v3.
sources:
- id: src_001
  type: paper
  title: 'FastTD3: Simple, Fast, and Capable Reinforcement Learning for Humanoid Control (arXiv)'
  url: https://arxiv.org/abs/2505.22642
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'FastTD3: Simple, Fast, and Capable Reinforcement Learning for Humanoid Control project page'
  url: https://younggyo.me/fast_td3/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Reinforcement learning (RL) has driven significant progress in robotics, but its complexity and long training times remain major bottlenecks. In this report, we introduce FastTD3, a simple, fast, and capable RL algorithm that significantly speeds up training for humanoid robots in popular suites such as HumanoidBench, IsaacLab, and MuJoCo Playground. Our recipe is remarkably simple: we train an off-policy TD3 agent with several modifications -- parallel simulation, large-batch updates, a distributional critic, and carefully tuned hyperparameters. FastTD3 solves a range of HumanoidBench tasks in under 3 hours on a single A100 GPU, while remaining stable during training. We also provide a lightweight and easy-to-use implementation of FastTD3 to accelerate RL research in robotics.

## 核心内容
Reinforcement learning (RL) has driven significant progress in robotics, but its complexity and long training times remain major bottlenecks. In this report, we introduce FastTD3, a simple, fast, and capable RL algorithm that significantly speeds up training for humanoid robots in popular suites such as HumanoidBench, IsaacLab, and MuJoCo Playground. Our recipe is remarkably simple: we train an off-policy TD3 agent with several modifications -- parallel simulation, large-batch updates, a distributional critic, and carefully tuned hyperparameters. FastTD3 solves a range of HumanoidBench tasks in under 3 hours on a single A100 GPU, while remaining stable during training. We also provide a lightweight and easy-to-use implementation of FastTD3 to accelerate RL research in robotics.

## 参考
- http://arxiv.org/abs/2505.22642v3

## Overview
Reinforcement learning (RL) has driven significant progress in robotics, but its complexity and long training times remain major bottlenecks. In this report, we introduce FastTD3, a simple, fast, and capable RL algorithm that significantly speeds up training for humanoid robots in popular suites such as HumanoidBench, IsaacLab, and MuJoCo Playground. Our recipe is remarkably simple: we train an off-policy TD3 agent with several modifications -- parallel simulation, large-batch updates, a distributional critic, and carefully tuned hyperparameters. FastTD3 solves a range of HumanoidBench tasks in under 3 hours on a single A100 GPU, while remaining stable during training. We also provide a lightweight and easy-to-use implementation of FastTD3 to accelerate RL research in robotics.

## Content
Reinforcement learning (RL) has driven significant progress in robotics, but its complexity and long training times remain major bottlenecks. In this report, we introduce FastTD3, a simple, fast, and capable RL algorithm that significantly speeds up training for humanoid robots in popular suites such as HumanoidBench, IsaacLab, and MuJoCo Playground. Our recipe is remarkably simple: we train an off-policy TD3 agent with several modifications -- parallel simulation, large-batch updates, a distributional critic, and carefully tuned hyperparameters. FastTD3 solves a range of HumanoidBench tasks in under 3 hours on a single A100 GPU, while remaining stable during training. We also provide a lightweight and easy-to-use implementation of FastTD3 to accelerate RL research in robotics.

## 개요
강화 학습(Reinforcement Learning, RL)은 로봇 공학 분야에서 상당한 진전을 이끌어냈지만, 그 복잡성과 긴 훈련 시간은 여전히 주요 병목 현상으로 남아 있습니다. 본 보고서에서는 HumanoidBench, IsaacLab, MuJoCo Playground와 같은 인기 있는 제품군에서 휴머노이드 로봇의 훈련 속도를 크게 향상시키는 간단하고 빠르며 강력한 RL 알고리즘인 FastTD3를 소개합니다. 우리의 방법은 놀라울 정도로 간단합니다. 여러 가지 수정 사항(병렬 시뮬레이션, 대규모 배치 업데이트, 분포형 비평가, 세심하게 조정된 하이퍼파라미터)을 적용하여 오프-폴리시 TD3 에이전트를 훈련합니다. FastTD3는 단일 A100 GPU에서 3시간 이내에 다양한 HumanoidBench 작업을 해결하면서도 훈련 중 안정성을 유지합니다. 또한 로봇 공학 RL 연구를 가속화하기 위해 가볍고 사용하기 쉬운 FastTD3 구현을 제공합니다.

## 핵심 내용
강화 학습(RL)은 로봇 공학 분야에서 상당한 진전을 이끌어냈지만, 그 복잡성과 긴 훈련 시간은 여전히 주요 병목 현상으로 남아 있습니다. 본 보고서에서는 HumanoidBench, IsaacLab, MuJoCo Playground와 같은 인기 있는 제품군에서 휴머노이드 로봇의 훈련 속도를 크게 향상시키는 간단하고 빠르며 강력한 RL 알고리즘인 FastTD3를 소개합니다. 우리의 방법은 놀라울 정도로 간단합니다. 여러 가지 수정 사항(병렬 시뮬레이션, 대규모 배치 업데이트, 분포형 비평가, 세심하게 조정된 하이퍼파라미터)을 적용하여 오프-폴리시 TD3 에이전트를 훈련합니다. FastTD3는 단일 A100 GPU에서 3시간 이내에 다양한 HumanoidBench 작업을 해결하면서도 훈련 중 안정성을 유지합니다. 또한 로봇 공학 RL 연구를 가속화하기 위해 가볍고 사용하기 쉬운 FastTD3 구현을 제공합니다.
